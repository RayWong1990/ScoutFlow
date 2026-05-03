from __future__ import annotations

import hashlib
import json
import os
import shutil
import sqlite3
import time
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path


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
        migration_path = Path(__file__).resolve().parent.parent / "migrations" / "001_phase1a_capture_creation.sql"
        sql = migration_path.read_text(encoding="utf-8")
        with self._connect() as conn:
            conn.executescript(sql)

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
