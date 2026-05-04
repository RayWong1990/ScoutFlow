from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

from scoutflow_api.external_tools.bbdown_info_parser import BBDownInfoParseResult
from scoutflow_api.models import (
    ArtifactZone,
    CURRENT_METADATA_EVIDENCE_PROBE_MODE,
    CURRENT_METADATA_EVIDENCE_REPORT_PATH,
    CURRENT_METADATA_EVIDENCE_TASK_ID,
    ReceiptIdempotency,
    WorkerReceipt,
)
from scoutflow_api.platform_result import PlatformResult


DEFAULT_REDACTION_POLICY = "credentials-v1"
DEFAULT_SENSITIVE_FIELDS_REMOVED = (
    "signed_url",
    "headers.cookie",
    "headers.authorization",
)


@dataclass(frozen=True)
class MetadataProbeEvidenceSource:
    task_id: str
    report_path: str
    probe_mode: str
    engine: str = "BBDown"
    engine_version: str = "1.6.3"

    def validate_for_success_evidence(self) -> None:
        if self.task_id != CURRENT_METADATA_EVIDENCE_TASK_ID:
            raise ValueError("Successful metadata receipt evidence must come from T-P1A-011C.")
        if self.probe_mode != CURRENT_METADATA_EVIDENCE_PROBE_MODE:
            raise ValueError("Successful metadata receipt evidence must be labeled probe_mode=auth-present.")
        if self.report_path != CURRENT_METADATA_EVIDENCE_REPORT_PATH:
            raise ValueError("Successful metadata receipt evidence must use the T-P1A-011C auth-present report path.")


@dataclass(frozen=True)
class PreparedMetadataProbeAsset:
    artifact_kind: str
    relative_path: str
    content_bytes: bytes
    mime_type: str
    is_raw_evidence: bool
    is_derived: bool


@dataclass(frozen=True)
class MaterializedMetadataProbeAsset:
    artifact_kind: str
    relative_path: str
    mime_type: str
    is_raw_evidence: bool
    is_derived: bool
    sha256: str
    bytes: int


def prepare_success_metadata_probe_assets(
    *,
    parsed: BBDownInfoParseResult,
    source_url: str,
    evidence_source: MetadataProbeEvidenceSource,
) -> tuple[PreparedMetadataProbeAsset, PreparedMetadataProbeAsset]:
    evidence_source.validate_for_success_evidence()
    if parsed.platform_result is not PlatformResult.ok:
        raise ValueError("Successful metadata receipt evidence requires platform_result=ok.")

    safe_metadata_evidence = {
        "evidence_source": {
            "task_id": evidence_source.task_id,
            "report_path": evidence_source.report_path,
            "probe_mode": evidence_source.probe_mode,
        },
        "engine": evidence_source.engine,
        "engine_version": evidence_source.engine_version,
        "source_url": source_url,
        "platform_result": parsed.platform_result.value,
        "platform_item_id": parsed.platform_item_id,
        "title": parsed.title,
        "duration_seconds": parsed.duration_seconds,
        "page_count": parsed.page_count,
        "selected_page": parsed.selected_page,
        "uploader_name": parsed.uploader_name,
        "estimated_media_bytes": parsed.estimated_media_bytes,
        "redaction_applied": parsed.redaction_applied,
    }
    metadata_probe_summary = {
        "evidence_kind": "auth_present_metadata_probe",
        "evidence_source_task_id": evidence_source.task_id,
        "probe_mode": evidence_source.probe_mode,
        "platform_result": parsed.platform_result.value,
        "platform_item_id": parsed.platform_item_id,
        "title": parsed.title,
        "duration_seconds": parsed.duration_seconds,
        "page_count": parsed.page_count,
        "selected_page": parsed.selected_page,
    }

    return (
        PreparedMetadataProbeAsset(
            artifact_kind="safe_metadata_evidence",
            relative_path="bundle/safe-metadata-evidence.json",
            content_bytes=_to_json_bytes(safe_metadata_evidence),
            mime_type="application/json",
            is_raw_evidence=True,
            is_derived=False,
        ),
        PreparedMetadataProbeAsset(
            artifact_kind="metadata_probe_summary",
            relative_path="bundle/metadata-probe-summary.json",
            content_bytes=_to_json_bytes(metadata_probe_summary),
            mime_type="application/json",
            is_raw_evidence=False,
            is_derived=True,
        ),
    )


def materialize_metadata_probe_assets(
    *,
    artifacts_root: Path,
    capture_id: str,
    assets: tuple[PreparedMetadataProbeAsset, ...] | list[PreparedMetadataProbeAsset],
) -> list[MaterializedMetadataProbeAsset]:
    written_assets: list[MaterializedMetadataProbeAsset] = []
    capture_root = (artifacts_root / "bilibili" / capture_id).resolve()

    for asset in assets:
        target = _validated_capture_target(capture_root=capture_root, relative_path=asset.relative_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(asset.content_bytes)
        written_assets.append(
            MaterializedMetadataProbeAsset(
                artifact_kind=asset.artifact_kind,
                relative_path=asset.relative_path,
                mime_type=asset.mime_type,
                is_raw_evidence=asset.is_raw_evidence,
                is_derived=asset.is_derived,
                sha256=hashlib.sha256(asset.content_bytes).hexdigest(),
                bytes=len(asset.content_bytes),
            )
        )

    return written_assets


def build_metadata_fetch_receipt(
    *,
    capture_id: str,
    job_id: str,
    dedupe_key: str,
    source_url: str,
    evidence_source: MetadataProbeEvidenceSource,
    materialized_assets: tuple[MaterializedMetadataProbeAsset, ...] | list[MaterializedMetadataProbeAsset],
    producer: str = "scoutflow.metadata_probe_bridge",
    producer_version: str = "0.1.0",
) -> WorkerReceipt:
    evidence_source.validate_for_success_evidence()

    return WorkerReceipt.model_validate(
        {
            "job_id": job_id,
            "capture_id": capture_id,
            "job_type": "metadata_fetch",
            "producer": producer,
            "producer_version": producer_version,
            "engine": evidence_source.engine,
            "engine_version": evidence_source.engine_version,
            "idempotency": ReceiptIdempotency(job_attempt=1, dedupe_key=dedupe_key).model_dump(mode="json"),
            "platform_result": PlatformResult.ok.value,
            "produced_assets": [
                {
                    "zone": ArtifactZone.bundle.value,
                    "artifact_kind": asset.artifact_kind,
                    "relative_path": asset.relative_path,
                    "sha256": asset.sha256,
                    "bytes": asset.bytes,
                    "mime_type": asset.mime_type,
                    "is_raw_evidence": asset.is_raw_evidence,
                    "is_derived": asset.is_derived,
                    "redaction_applied": True,
                    "redaction_policy": DEFAULT_REDACTION_POLICY,
                    "sensitive_fields_removed": list(DEFAULT_SENSITIVE_FIELDS_REMOVED),
                    "source_url": source_url,
                    "evidence_source_task_id": evidence_source.task_id,
                    "evidence_source_report_path": evidence_source.report_path,
                    "probe_mode": evidence_source.probe_mode,
                    "created_by_job": job_id,
                }
                for asset in materialized_assets
            ],
            "logs": {
                "job_log_path": "logs/jobs/metadata-receipt-bridge.log",
                "stderr_path": None,
            },
            "duration_seconds": 0.0,
            "next_status": "metadata_fetched",
        }
    )


def _to_json_bytes(payload: dict[str, object]) -> bytes:
    return json.dumps(payload, ensure_ascii=True, indent=2, sort_keys=True).encode("utf-8")


def _validated_capture_target(*, capture_root: Path, relative_path: str) -> Path:
    posix_path = PurePosixPath(relative_path)
    if posix_path.is_absolute():
        raise ValueError("metadata probe asset relative_path must not be absolute")
    if not posix_path.parts:
        raise ValueError("metadata probe asset relative_path must not be empty")
    if any(part in {"", ".", ".."} for part in posix_path.parts):
        raise ValueError("metadata probe asset relative_path must not contain empty, dot, or dot-dot parts")
    if posix_path.parts[0] != ArtifactZone.bundle.value:
        raise ValueError("metadata probe asset relative_path must stay under bundle/")

    target = (capture_root / Path(*posix_path.parts)).resolve()
    try:
        target.relative_to(capture_root)
    except ValueError as exc:
        raise ValueError("metadata probe asset relative_path resolves outside capture root") from exc
    return target
