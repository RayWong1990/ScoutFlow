from __future__ import annotations

import sys
from pathlib import Path

import pytest
from pydantic import ValidationError


ROOT = Path(__file__).resolve().parents[2]
API_ROOT = ROOT / "services" / "api"
if str(API_ROOT) not in sys.path:
    sys.path.insert(0, str(API_ROOT))


def valid_receipt_payload() -> dict[str, object]:
    return {
        "job_id": "job-metadata-1",
        "capture_id": "capture-1",
        "job_type": "metadata_fetch",
        "producer": "workers.bili",
        "producer_version": "0.1.0",
        "engine": "BBDown",
        "engine_version": "1.6.2",
        "idempotency": {
            "job_attempt": 1,
            "dedupe_key": "bilibili:BV1AB411c7mD:metadata_fetch",
        },
        "platform_result": "ok",
        "produced_assets": [
            {
                "zone": "bundle",
                "artifact_kind": "raw_api_response",
                "relative_path": "bundle/raw-api-response.json",
                "sha256": "a" * 64,
                "bytes": 2,
                "mime_type": "application/json",
                "is_raw_evidence": True,
                "is_derived": False,
                "redaction_applied": True,
                "redaction_policy": "credentials-v1",
                "sensitive_fields_removed": ["headers.cookie"],
                "source_url": "https://www.bilibili.com/video/BV1AB411c7mD",
                "created_by_job": "job-metadata-1",
            }
        ],
        "logs": {
            "job_log_path": "logs/jobs/metadata-fetch.log",
            "stderr_path": None,
        },
        "duration_seconds": 1.25,
        "next_status": "metadata_fetched",
    }


def test_receipt_model_forbids_extra_fields() -> None:
    from scoutflow_api.models import WorkerReceipt

    payload = valid_receipt_payload()
    payload["unexpected"] = True

    with pytest.raises(ValidationError):
        WorkerReceipt.model_validate(payload)


def test_receipt_zone_enum_matches_contract() -> None:
    from scoutflow_api.models import ArtifactZone

    assert {zone.value for zone in ArtifactZone} == {
        "bundle",
        "media",
        "transcript",
        "normalized",
        "links",
        "logs",
    }


def test_receipt_platform_result_uses_existing_enum() -> None:
    from scoutflow_api.models import WorkerReceipt

    payload = valid_receipt_payload()
    payload["platform_result"] = "parser_drift"

    receipt = WorkerReceipt.model_validate(payload)

    assert receipt.platform_result.value == "parser_drift"


def test_unknown_platform_result_rejected_by_contract() -> None:
    from scoutflow_api.models import WorkerReceipt

    payload = valid_receipt_payload()
    payload["platform_result"] = "unknown_new_value"

    with pytest.raises(ValidationError):
        WorkerReceipt.model_validate(payload)


def test_raw_api_response_requires_redaction_metadata() -> None:
    from scoutflow_api.models import WorkerReceipt

    payload = valid_receipt_payload()
    asset = payload["produced_assets"][0]  # type: ignore[index]
    asset["redaction_applied"] = False
    asset["redaction_policy"] = None
    asset["sensitive_fields_removed"] = []

    with pytest.raises(ValidationError):
        WorkerReceipt.model_validate(payload)


def test_relative_path_must_match_zone() -> None:
    from scoutflow_api.models import WorkerReceipt

    payload = valid_receipt_payload()
    asset = payload["produced_assets"][0]  # type: ignore[index]
    asset["zone"] = "media"

    with pytest.raises(ValidationError):
        WorkerReceipt.model_validate(payload)


def test_relative_path_rejects_backslash_traversal() -> None:
    from scoutflow_api.models import WorkerReceipt

    payload = valid_receipt_payload()
    asset = payload["produced_assets"][0]  # type: ignore[index]
    asset["relative_path"] = "bundle\\..\\logs\\raw-api-response.json"

    with pytest.raises(ValidationError):
        WorkerReceipt.model_validate(payload)


def test_created_by_job_must_match_receipt_job_id() -> None:
    from scoutflow_api.models import WorkerReceipt

    payload = valid_receipt_payload()
    asset = payload["produced_assets"][0]  # type: ignore[index]
    asset["created_by_job"] = "different-job"

    with pytest.raises(ValidationError):
        WorkerReceipt.model_validate(payload)


def test_metadata_probe_evidence_asset_requires_evidence_source_fields() -> None:
    from scoutflow_api.models import WorkerReceipt

    payload = valid_receipt_payload()
    asset = payload["produced_assets"][0]  # type: ignore[index]
    asset["artifact_kind"] = "safe_metadata_evidence"
    asset["relative_path"] = "bundle/safe-metadata-evidence.json"
    asset["evidence_source_task_id"] = None
    asset["evidence_source_report_path"] = None
    asset["probe_mode"] = None

    with pytest.raises(ValidationError):
        WorkerReceipt.model_validate(payload)


def test_metadata_fetch_rejects_media_artifact_kinds() -> None:
    from scoutflow_api.models import WorkerReceipt

    payload = valid_receipt_payload()
    asset = payload["produced_assets"][0]  # type: ignore[index]
    asset["artifact_kind"] = "video"
    asset["zone"] = "bundle"

    with pytest.raises(ValidationError):
        WorkerReceipt.model_validate(payload)


def test_current_phase_metadata_probe_success_evidence_rejects_blocked_task_id() -> None:
    from scoutflow_api.models import WorkerReceipt

    payload = valid_receipt_payload()
    asset = payload["produced_assets"][0]  # type: ignore[index]
    asset["artifact_kind"] = "safe_metadata_evidence"
    asset["relative_path"] = "bundle/safe-metadata-evidence.json"
    asset["evidence_source_task_id"] = "T-P1A-011"
    asset["evidence_source_report_path"] = "docs/research/t-p1a-011-bbdown-noauth-info-probe-report-2026-05-03.md"
    asset["probe_mode"] = "no-auth"

    with pytest.raises(ValidationError):
        WorkerReceipt.model_validate(payload)


def test_current_phase_metadata_probe_success_evidence_rejects_wrong_report_path() -> None:
    from scoutflow_api.models import WorkerReceipt

    payload = valid_receipt_payload()
    asset = payload["produced_assets"][0]  # type: ignore[index]
    asset["artifact_kind"] = "metadata_probe_summary"
    asset["relative_path"] = "bundle/metadata-probe-summary.json"
    asset["evidence_source_task_id"] = "T-P1A-011C"
    asset["evidence_source_report_path"] = "docs/research/t-p1a-011c-some-other-report.md"
    asset["probe_mode"] = "auth-present"

    with pytest.raises(ValidationError):
        WorkerReceipt.model_validate(payload)
