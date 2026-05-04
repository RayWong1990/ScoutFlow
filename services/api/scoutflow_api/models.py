from __future__ import annotations

from enum import StrEnum
from pathlib import PurePosixPath

from pydantic import BaseModel, ConfigDict, Field, model_validator

from scoutflow_api.platform_result import PlatformResult


class DiscoverCaptureRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    platform: str
    canonical_url: str
    source_kind: str
    quick_capture_preset: str


class DiscoverCaptureResponse(BaseModel):
    capture_id: str
    platform: str
    platform_item_id: str
    source_kind: str
    capture_mode: str
    created_by_path: str
    status: str
    artifact_root_path: str
    manifest_path: str


class ErrorResponse(BaseModel):
    code: str
    message: str


class ArtifactZone(StrEnum):
    bundle = "bundle"
    media = "media"
    transcript = "transcript"
    normalized = "normalized"
    links = "links"
    logs = "logs"


class ReceiptIdempotency(BaseModel):
    model_config = ConfigDict(extra="forbid")

    job_attempt: int = Field(ge=1)
    dedupe_key: str = Field(min_length=1)


class ReceiptLogs(BaseModel):
    model_config = ConfigDict(extra="forbid")

    job_log_path: str | None = None
    stderr_path: str | None = None


class ProducedAsset(BaseModel):
    model_config = ConfigDict(extra="forbid")

    zone: ArtifactZone
    artifact_kind: str = Field(min_length=1)
    relative_path: str = Field(min_length=1)
    sha256: str = Field(min_length=64, max_length=64)
    bytes: int = Field(ge=0)
    mime_type: str | None = None
    is_raw_evidence: bool
    is_derived: bool
    redaction_applied: bool
    redaction_policy: str | None = None
    sensitive_fields_removed: list[str] | None = None
    source_url: str | None = None
    evidence_source_task_id: str | None = None
    evidence_source_report_path: str | None = None
    probe_mode: str | None = None
    created_by_job: str = Field(min_length=1)

    @model_validator(mode="after")
    def validate_asset_contract(self) -> "ProducedAsset":
        if "\\" in self.relative_path:
            raise ValueError("relative_path must use POSIX separators and must not contain backslashes")

        relative_path = PurePosixPath(self.relative_path)
        if relative_path.is_absolute():
            raise ValueError("relative_path must not be absolute")
        if not relative_path.parts:
            raise ValueError("relative_path must not be empty")
        if any(part in {"", ".", ".."} for part in relative_path.parts):
            raise ValueError("relative_path must not contain empty, dot, or dot-dot components")
        if relative_path.parts[0] != self.zone.value:
            raise ValueError("zone must match the first relative_path component")

        if self.artifact_kind == "raw_api_response":
            if not self.redaction_applied:
                raise ValueError("raw_api_response requires redaction_applied=true")
            if not self.redaction_policy:
                raise ValueError("raw_api_response requires redaction_policy")
            if not self.sensitive_fields_removed:
                raise ValueError("raw_api_response requires non-empty sensitive_fields_removed")

        if self.artifact_kind in {"metadata_probe_summary", "safe_metadata_evidence"}:
            if self.zone is not ArtifactZone.bundle:
                raise ValueError("metadata probe evidence assets must stay in zone=bundle")
            if not self.redaction_applied:
                raise ValueError("metadata probe evidence assets require redaction_applied=true")
            if not self.redaction_policy:
                raise ValueError("metadata probe evidence assets require redaction_policy")
            if not self.sensitive_fields_removed:
                raise ValueError("metadata probe evidence assets require non-empty sensitive_fields_removed")
            if not self.evidence_source_task_id:
                raise ValueError("metadata probe evidence assets require evidence_source_task_id")
            if not self.evidence_source_report_path:
                raise ValueError("metadata probe evidence assets require evidence_source_report_path")
            if self.probe_mode not in {"auth-present", "no-auth"}:
                raise ValueError("metadata probe evidence assets require probe_mode=auth-present|no-auth")

        return self


class WorkerReceipt(BaseModel):
    model_config = ConfigDict(extra="forbid")

    job_id: str = Field(min_length=1)
    capture_id: str = Field(min_length=1)
    job_type: str = Field(min_length=1)
    producer: str = Field(min_length=1)
    producer_version: str = Field(min_length=1)
    engine: str | None = None
    engine_version: str | None = None
    idempotency: ReceiptIdempotency
    platform_result: PlatformResult
    produced_assets: list[ProducedAsset]
    logs: ReceiptLogs | None = None
    duration_seconds: float | None = Field(default=None, ge=0)
    next_status: str = Field(min_length=1)

    @model_validator(mode="after")
    def validate_receipt_contract(self) -> "WorkerReceipt":
        if self.job_type == "metadata_fetch":
            allowed_artifact_kinds = {
                "raw_api_response",
                "metadata_probe_summary",
                "safe_metadata_evidence",
            }
            for asset in self.produced_assets:
                if asset.artifact_kind not in allowed_artifact_kinds:
                    raise ValueError(
                        "metadata_fetch only allows artifact_kind raw_api_response, metadata_probe_summary, or safe_metadata_evidence"
                    )

        for asset in self.produced_assets:
            if asset.created_by_job != self.job_id:
                raise ValueError("produced_assets[].created_by_job must match receipt job_id")
        return self


class JobCompleteResponse(BaseModel):
    job_id: str
    capture_id: str
    job_type: str
    status: str
    platform_result: str
    artifact_count: int
    idempotent: bool


class TrustTraceCapture(BaseModel):
    model_config = ConfigDict(extra="forbid")

    capture_id: str
    platform: str
    platform_item_id: str
    source_kind: str
    capture_mode: str
    created_by_path: str


class TrustTraceCaptureState(BaseModel):
    model_config = ConfigDict(extra="forbid")

    capture_created: bool
    status: str


class TrustTraceMetadataJob(BaseModel):
    model_config = ConfigDict(extra="forbid")

    present: bool
    job_id: str | None = None
    job_type: str | None = None
    status: str | None = None
    platform_result: str | None = None


class TrustTraceProbeEvidence(BaseModel):
    model_config = ConfigDict(extra="forbid")

    present: bool
    probe_mode: str
    source_task_id: str | None = None
    source_report_path: str | None = None
    platform_result: str | None = None


class TrustTraceReceiptLedger(BaseModel):
    model_config = ConfigDict(extra="forbid")

    present: bool
    artifact_count: int
    artifact_kinds: list[str]
    redaction: str


class TrustTraceMediaAudio(BaseModel):
    model_config = ConfigDict(extra="forbid")

    status: str
    audio_transcript: str


class TrustTraceAuditBlock(BaseModel):
    model_config = ConfigDict(extra="forbid")

    platform_result: str | None = None
    evidence_file_path: str | None = None
    artifact_count: int
    redaction_policy: str | None = None
    safe_parsed_fields: dict[str, str | int | None]


class TrustTraceResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    label: str
    capture: TrustTraceCapture
    capture_state: TrustTraceCaptureState
    metadata_job: TrustTraceMetadataJob
    probe_evidence: TrustTraceProbeEvidence
    receipt_ledger: TrustTraceReceiptLedger
    media_audio: TrustTraceMediaAudio
    audit: TrustTraceAuditBlock
