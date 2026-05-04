from __future__ import annotations

import hashlib
import json
import os
import shutil
import sqlite3
import time
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path, PurePosixPath
from typing import Any

from scoutflow_api.models import ProducedAsset, TrustTraceResponse, WorkerReceipt


CROCKFORD32 = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"


def _encode_base32(value: int, length: int) -> str:
    chars: list[str] = []
    for _ in range(length):
        chars.append(CROCKFORD32[value & 0x1F])
        value >>= 5
    return "".join(reversed(chars))


def generate_capture_id() -> str:
    timestamp_ms = int(time.time() * 1000)
    randomness = int.from_bytes(os.urandom(10), "big")
    return _encode_base32(timestamp_ms, 10) + _encode_base32(randomness, 16)


@dataclass(frozen=True)
class StorageConfig:
    db_path: Path
    artifacts_root: Path
    artifact_prefix: Path = Path("data/artifacts")


class ReceiptStorageError(Exception):
    def __init__(self, http_status: int, code: str, message: str) -> None:
        super().__init__(message)
        self.http_status = http_status
        self.code = code
        self.message = message


class Storage:
    def __init__(self, config: StorageConfig) -> None:
        self.config = config
        self._init_schema()

    def _connect(self) -> sqlite3.Connection:
        self.config.db_path.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(self.config.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_schema(self) -> None:
        migrations_dir = Path(__file__).resolve().parent.parent / "migrations"
        with self._connect() as conn:
            for migration_path in sorted(migrations_dir.glob("*.sql")):
                conn.executescript(migration_path.read_text(encoding="utf-8"))

    def _find_metadata_capture(self, platform_item_id: str) -> dict[str, str] | None:
        with self._connect() as conn:
            row = conn.execute(
                """
                SELECT
                    capture_id, platform, platform_item_id, source_kind, capture_mode,
                    created_by_path, status, artifact_root_path, manifest_path
                FROM captures
                WHERE platform = ? AND platform_item_id = ?
                """,
                ("bilibili", platform_item_id),
            ).fetchone()

        if row is None:
            return None

        return {
            "capture_id": row["capture_id"],
            "platform": row["platform"],
            "platform_item_id": row["platform_item_id"],
            "source_kind": row["source_kind"],
            "capture_mode": row["capture_mode"],
            "created_by_path": row["created_by_path"],
            "status": row["status"],
            "artifact_root_path": row["artifact_root_path"],
            "manifest_path": row["manifest_path"],
        }

    def _remove_capture_artifacts(self, capture_id: str) -> None:
        shutil.rmtree(self.config.artifacts_root / "bilibili" / capture_id, ignore_errors=True)

    def create_metadata_capture(self, canonical_url: str, platform_item_id: str) -> dict[str, str]:
        existing = self._find_metadata_capture(platform_item_id)
        if existing is not None:
            return existing

        capture_id = generate_capture_id()
        created_at = datetime.now(UTC).isoformat()
        artifact_root_path = str(self.config.artifact_prefix / "bilibili" / capture_id)
        manifest_path = f"{artifact_root_path}/bundle/capture-manifest.json"
        manifest = {
            "capture_id": capture_id,
            "platform": "bilibili",
            "platform_item_id": platform_item_id,
            "canonical_url": canonical_url,
            "source_kind": "manual_url",
            "capture_mode": "metadata_only",
            "created_by_path": "quick_capture",
            "status": "discovered",
            "created_at": created_at,
        }

        try:
            manifest_file = self.config.artifacts_root / "bilibili" / capture_id / "bundle" / "capture-manifest.json"
            manifest_file.parent.mkdir(parents=True, exist_ok=True)
            manifest_json = json.dumps(manifest, ensure_ascii=True, indent=2)
            manifest_file.write_text(manifest_json, encoding="utf-8")
            manifest_sha = hashlib.sha256(manifest_json.encode("utf-8")).hexdigest()
            manifest_size = manifest_file.stat().st_size

            with self._connect() as conn:
                conn.execute(
                    """
                    INSERT INTO captures (
                        capture_id, platform, platform_item_id, canonical_url, source_kind,
                        capture_mode, created_by_path, status, artifact_root_path,
                        manifest_path, created_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        capture_id,
                        "bilibili",
                        platform_item_id,
                        canonical_url,
                        "manual_url",
                        "metadata_only",
                        "quick_capture",
                        "discovered",
                        artifact_root_path,
                        manifest_path,
                        created_at,
                    ),
                )
                conn.execute(
                    """
                    INSERT INTO artifact_assets (
                        capture_id, artifact_zone, artifact_kind, file_path,
                        size_bytes, sha256, metadata_json, created_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        capture_id,
                        "bundle",
                        "capture_manifest",
                        manifest_path,
                        manifest_size,
                        manifest_sha,
                        json.dumps(
                            {
                                "is_raw_evidence": False,
                                "is_derived": False,
                                "redaction_applied": False,
                                "source_url": canonical_url,
                                "producer": "scoutflow_api",
                                "created_by_job": None,
                            },
                            ensure_ascii=True,
                        ),
                        created_at,
                    ),
                )
                conn.commit()
        except sqlite3.IntegrityError:
            self._remove_capture_artifacts(capture_id)
            existing_after_conflict = self._find_metadata_capture(platform_item_id)
            if existing_after_conflict is not None:
                return existing_after_conflict
            raise
        except Exception:
            self._remove_capture_artifacts(capture_id)
            raise

        return {
            "capture_id": capture_id,
            "platform": "bilibili",
            "platform_item_id": platform_item_id,
            "source_kind": "manual_url",
            "capture_mode": "metadata_only",
            "created_by_path": "quick_capture",
            "status": "discovered",
            "artifact_root_path": artifact_root_path,
            "manifest_path": manifest_path,
        }

    def _capture_root(self, platform: str, capture_id: str) -> Path:
        return self.config.artifacts_root / platform / capture_id

    def _artifact_actual_path(self, platform: str, capture_id: str, relative_path: str) -> Path:
        parts = PurePosixPath(relative_path).parts
        return self._capture_root(platform, capture_id) / Path(*parts)

    def _artifact_ledger_path(self, platform: str, capture_id: str, relative_path: str) -> str:
        return str(self.config.artifact_prefix / platform / capture_id / relative_path)

    def _ledger_path_to_relative_path(self, platform: str, capture_id: str, ledger_path: str) -> str | None:
        prefix = str(self.config.artifact_prefix / platform / capture_id) + "/"
        if not ledger_path.startswith(prefix):
            return None
        return ledger_path[len(prefix) :]

    def _hash_file(self, path: Path) -> str:
        digest = hashlib.sha256()
        with path.open("rb") as file:
            for chunk in iter(lambda: file.read(1024 * 1024), b""):
                digest.update(chunk)
        return digest.hexdigest()

    def _verify_asset_file(self, platform: str, capture_id: str, asset: ProducedAsset) -> str:
        actual_path = self._artifact_actual_path(platform, capture_id, asset.relative_path)
        capture_root = self._capture_root(platform, capture_id)
        try:
            actual_path.resolve().relative_to(capture_root.resolve())
        except ValueError as exc:
            raise ReceiptStorageError(422, "artifact_path_outside_root", "Artifact path is outside capture root.") from exc

        if not actual_path.is_file():
            raise ReceiptStorageError(422, "artifact_file_missing", "Produced asset file must exist before ledger insertion.")

        actual_bytes = actual_path.stat().st_size
        if actual_bytes != asset.bytes:
            raise ReceiptStorageError(422, "artifact_bytes_mismatch", "Produced asset bytes do not match actual file size.")

        actual_sha = self._hash_file(actual_path)
        if actual_sha != asset.sha256:
            raise ReceiptStorageError(422, "artifact_sha256_mismatch", "Produced asset sha256 does not match actual file.")

        return self._artifact_ledger_path(platform, capture_id, asset.relative_path)

    def _asset_metadata(self, receipt: WorkerReceipt, asset: ProducedAsset) -> dict[str, Any]:
        metadata = {
            "is_raw_evidence": asset.is_raw_evidence,
            "is_derived": asset.is_derived,
            "redaction_applied": asset.redaction_applied,
            "redaction_policy": asset.redaction_policy,
            "sensitive_fields_removed": asset.sensitive_fields_removed or [],
            "source_url": asset.source_url,
            "created_by_job": asset.created_by_job,
            "producer": receipt.producer,
            "producer_version": receipt.producer_version,
            "engine": receipt.engine,
            "engine_version": receipt.engine_version,
            "source_surface": "worker_receipt",
            "job_attempt": receipt.idempotency.job_attempt,
            "dedupe_key": receipt.idempotency.dedupe_key,
            "platform_result": receipt.platform_result.value,
        }
        if asset.evidence_source_task_id is not None:
            metadata["evidence_source_task_id"] = asset.evidence_source_task_id
        if asset.evidence_source_report_path is not None:
            metadata["evidence_source_report_path"] = asset.evidence_source_report_path
        if asset.probe_mode is not None:
            metadata["probe_mode"] = asset.probe_mode
        return metadata

    def _job_event_json(self, receipt: WorkerReceipt, ledger_paths: list[str]) -> str:
        return json.dumps(
            {
                "job_id": receipt.job_id,
                "capture_id": receipt.capture_id,
                "job_type": receipt.job_type,
                "producer": receipt.producer,
                "producer_version": receipt.producer_version,
                "engine": receipt.engine,
                "engine_version": receipt.engine_version,
                "idempotency": receipt.idempotency.model_dump(mode="json"),
                "platform_result": receipt.platform_result.value,
                "next_status": receipt.next_status,
                "duration_seconds": receipt.duration_seconds,
                "artifact_paths": ledger_paths,
            },
            ensure_ascii=True,
        )

    def _verify_idempotent_assets(
        self,
        conn: sqlite3.Connection,
        capture_id: str,
        assets: list[ProducedAsset],
        ledger_paths: list[str],
    ) -> None:
        for asset, ledger_path in zip(assets, ledger_paths, strict=True):
            row = conn.execute(
                """
                SELECT artifact_kind, size_bytes, sha256
                FROM artifact_assets
                WHERE capture_id = ? AND file_path = ?
                """,
                (capture_id, ledger_path),
            ).fetchone()
            if row is None:
                raise ReceiptStorageError(
                    409,
                    "idempotent_ledger_missing",
                    "Succeeded job receipt replay did not find the expected artifact ledger row.",
                )
            if row["artifact_kind"] != asset.artifact_kind or row["size_bytes"] != asset.bytes or row["sha256"] != asset.sha256:
                raise ReceiptStorageError(
                    409,
                    "idempotent_ledger_conflict",
                    "Succeeded job receipt replay conflicts with existing artifact ledger row.",
                )

    def complete_job_receipt(self, receipt: WorkerReceipt) -> dict[str, Any]:
        completed_at = datetime.now(UTC).isoformat()

        with self._connect() as conn:
            job = conn.execute(
                """
                SELECT job_id, capture_id, job_type, status, dedupe_key, platform_result
                FROM jobs
                WHERE job_id = ?
                """,
                (receipt.job_id,),
            ).fetchone()
            if job is None:
                raise ReceiptStorageError(404, "job_not_found", "Receipt job_id does not exist.")
            if job["capture_id"] != receipt.capture_id:
                raise ReceiptStorageError(409, "job_capture_mismatch", "Receipt capture_id does not match job record.")
            if job["job_type"] != receipt.job_type:
                raise ReceiptStorageError(409, "job_type_mismatch", "Receipt job_type does not match job record.")
            if job["dedupe_key"] != receipt.idempotency.dedupe_key:
                raise ReceiptStorageError(409, "job_dedupe_key_mismatch", "Receipt dedupe_key does not match job record.")

            capture = conn.execute(
                """
                SELECT capture_id, platform, status
                FROM captures
                WHERE capture_id = ?
                """,
                (receipt.capture_id,),
            ).fetchone()
            if capture is None:
                raise ReceiptStorageError(404, "capture_not_found", "Receipt capture_id does not exist.")

            platform = capture["platform"]
            ledger_paths = [
                self._verify_asset_file(platform, receipt.capture_id, asset) for asset in receipt.produced_assets
            ]

            if receipt.next_status != "metadata_fetched":
                raise ReceiptStorageError(
                    409,
                    "next_status_not_supported",
                    "T-P1A-002 only supports next_status=metadata_fetched.",
                )
            if capture["status"] not in {"discovered", "metadata_fetched"}:
                raise ReceiptStorageError(
                    409,
                    "capture_state_conflict",
                    "next_status=metadata_fetched is only allowed from discovered.",
                )

            if job["status"] == "succeeded":
                if job["platform_result"] != receipt.platform_result.value:
                    raise ReceiptStorageError(
                        409,
                        "idempotent_platform_result_conflict",
                        "Succeeded job receipt replay conflicts with existing platform_result.",
                    )
                self._verify_idempotent_assets(conn, receipt.capture_id, receipt.produced_assets, ledger_paths)
                return {
                    "job_id": receipt.job_id,
                    "capture_id": receipt.capture_id,
                    "job_type": receipt.job_type,
                    "status": "succeeded",
                    "platform_result": receipt.platform_result.value,
                    "artifact_count": len(receipt.produced_assets),
                    "idempotent": True,
                }

            inserted_assets = 0
            for asset, ledger_path in zip(receipt.produced_assets, ledger_paths, strict=True):
                existing = conn.execute(
                    """
                    SELECT artifact_kind, size_bytes, sha256
                    FROM artifact_assets
                    WHERE capture_id = ? AND file_path = ?
                    """,
                    (receipt.capture_id, ledger_path),
                ).fetchone()
                if existing is not None:
                    if (
                        existing["artifact_kind"] != asset.artifact_kind
                        or existing["size_bytes"] != asset.bytes
                        or existing["sha256"] != asset.sha256
                    ):
                        raise ReceiptStorageError(
                            409,
                            "artifact_ledger_conflict",
                            "Produced asset conflicts with an existing artifact ledger row.",
                        )
                    continue

                conn.execute(
                    """
                    INSERT INTO artifact_assets (
                        capture_id, artifact_zone, artifact_kind, file_path,
                        size_bytes, sha256, metadata_json, created_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        receipt.capture_id,
                        asset.zone.value,
                        asset.artifact_kind,
                        ledger_path,
                        asset.bytes,
                        asset.sha256,
                        json.dumps(self._asset_metadata(receipt, asset), ensure_ascii=True),
                        completed_at,
                    ),
                )
                inserted_assets += 1

            job_status = "succeeded" if receipt.platform_result.value == "ok" else "failed"
            conn.execute(
                """
                UPDATE jobs
                SET status = ?, completed_at = ?, platform_result = ?
                WHERE job_id = ?
                """,
                (job_status, completed_at, receipt.platform_result.value, receipt.job_id),
            )
            if job_status == "succeeded":
                conn.execute(
                    """
                    UPDATE captures
                    SET status = ?
                    WHERE capture_id = ?
                    """,
                    (receipt.next_status, receipt.capture_id),
                )
            conn.execute(
                """
                INSERT INTO job_events (job_id, event_type, event_json, created_at)
                VALUES (?, ?, ?, ?)
                """,
                (receipt.job_id, "complete", self._job_event_json(receipt, ledger_paths), completed_at),
            )
            conn.commit()

        return {
            "job_id": receipt.job_id,
            "capture_id": receipt.capture_id,
            "job_type": receipt.job_type,
            "status": job_status,
            "platform_result": receipt.platform_result.value,
            "artifact_count": inserted_assets,
            "idempotent": False,
        }

    def get_capture_trust_trace(self, capture_id: str) -> dict[str, Any]:
        with self._connect() as conn:
            capture = conn.execute(
                """
                SELECT capture_id, platform, platform_item_id, source_kind, capture_mode, created_by_path, status
                FROM captures
                WHERE capture_id = ?
                """,
                (capture_id,),
            ).fetchone()
            if capture is None:
                raise ReceiptStorageError(404, "capture_not_found", "Capture does not exist.")
            if capture["source_kind"] != "manual_url":
                raise ReceiptStorageError(
                    409,
                    "trust_trace_source_kind_not_allowed",
                    "Trust Trace only supports manual_url captures.",
                )

            metadata_job = conn.execute(
                """
                SELECT job_id, job_type, status, platform_result
                FROM jobs
                WHERE capture_id = ? AND job_type = ?
                ORDER BY COALESCE(completed_at, started_at, queued_at) DESC, rowid DESC
                LIMIT 1
                """,
                (capture_id, "metadata_fetch"),
            ).fetchone()

            artifact_rows = conn.execute(
                """
                SELECT artifact_kind, file_path, metadata_json
                FROM artifact_assets
                WHERE capture_id = ?
                ORDER BY created_at ASC, file_path ASC
                """,
                (capture_id,),
            ).fetchall()

        metadata_job_id = metadata_job["job_id"] if metadata_job is not None else None
        receipt_assets: list[dict[str, Any]] = []
        for row in artifact_rows:
            metadata_json = json.loads(row["metadata_json"])
            if metadata_job_id is None:
                continue
            if metadata_json.get("created_by_job") != metadata_job_id:
                continue
            receipt_assets.append(
                {
                    "artifact_kind": row["artifact_kind"],
                    "file_path": row["file_path"],
                    "metadata_json": metadata_json,
                }
            )

        receipt_present = len(receipt_assets) > 0
        label = "Receipt / Ledger Trace" if receipt_present else "Status / Trust Trace / 采集状态"

        evidence_asset = next(
            (asset for asset in receipt_assets if asset["artifact_kind"] == "safe_metadata_evidence"),
            None,
        )
        summary_asset = next(
            (asset for asset in receipt_assets if asset["artifact_kind"] == "metadata_probe_summary"),
            None,
        )

        probe_metadata = evidence_asset["metadata_json"] if evidence_asset is not None else (
            summary_asset["metadata_json"] if summary_asset is not None else {}
        )
        probe_present = bool(probe_metadata.get("evidence_source_task_id"))
        probe_mode = probe_metadata.get("probe_mode", "not-run")

        safe_parsed_fields: dict[str, str | int | None] = {}
        evidence_file_path: str | None = None
        redaction_policy: str | None = None
        if evidence_asset is not None:
            evidence_file_path = evidence_asset["file_path"]
            redaction_policy = evidence_asset["metadata_json"].get("redaction_policy")
            relative_path = self._ledger_path_to_relative_path(capture["platform"], capture_id, evidence_file_path)
            if relative_path is not None:
                actual_path = self._artifact_actual_path(capture["platform"], capture_id, relative_path)
                if actual_path.is_file():
                    payload = json.loads(actual_path.read_text(encoding="utf-8"))
                    safe_parsed_fields = {
                        "platform_item_id": payload.get("platform_item_id"),
                        "title": payload.get("title"),
                        "duration_seconds": payload.get("duration_seconds"),
                        "page_count": payload.get("page_count"),
                        "selected_page": payload.get("selected_page"),
                    }

        artifact_kind_priority = {
            "safe_metadata_evidence": 0,
            "metadata_probe_summary": 1,
            "raw_api_response": 2,
        }
        artifact_kinds = sorted(
            [asset["artifact_kind"] for asset in receipt_assets],
            key=lambda item: (artifact_kind_priority.get(item, 99), item),
        )

        response = {
            "label": label,
            "capture": {
                "capture_id": capture["capture_id"],
                "platform": capture["platform"],
                "platform_item_id": capture["platform_item_id"],
                "source_kind": capture["source_kind"],
                "capture_mode": capture["capture_mode"],
                "created_by_path": capture["created_by_path"],
            },
            "capture_state": {
                "capture_created": True,
                "status": capture["status"],
            },
            "metadata_job": {
                "present": metadata_job is not None,
                "job_id": metadata_job["job_id"] if metadata_job is not None else None,
                "job_type": metadata_job["job_type"] if metadata_job is not None else None,
                "status": metadata_job["status"] if metadata_job is not None else None,
                "platform_result": metadata_job["platform_result"] if metadata_job is not None else None,
            },
            "probe_evidence": {
                "present": probe_present,
                "probe_mode": probe_mode,
                "source_task_id": probe_metadata.get("evidence_source_task_id"),
                "source_report_path": probe_metadata.get("evidence_source_report_path"),
                "platform_result": probe_metadata.get("platform_result"),
            },
            "receipt_ledger": {
                "present": receipt_present,
                "artifact_count": len(receipt_assets),
                "artifact_kinds": artifact_kinds,
                "redaction": "applied" if receipt_present else "not_applicable",
            },
            "media_audio": {
                "status": "not_approved",
                "audio_transcript": "blocked",
            },
            "audit": {
                "platform_result": metadata_job["platform_result"] if metadata_job is not None else None,
                "evidence_file_path": evidence_file_path,
                "artifact_count": len(receipt_assets),
                "redaction_policy": redaction_policy,
                "safe_parsed_fields": safe_parsed_fields,
            },
        }
        return TrustTraceResponse.model_validate(response).model_dump(mode="json")
