from __future__ import annotations

import json
import sqlite3
import sys
from pathlib import Path

from fastapi.testclient import TestClient


ROOT = Path(__file__).resolve().parents[2]
API_ROOT = ROOT / "services" / "api"
if str(API_ROOT) not in sys.path:
    sys.path.insert(0, str(API_ROOT))


def build_client(tmp_path: Path) -> tuple[TestClient, Path, Path]:
    from scoutflow_api.main import create_app

    runtime_root = tmp_path / "runtime"
    db_path = runtime_root / "data" / "db" / "scoutflow.sqlite"
    artifacts_root = runtime_root / "data" / "artifacts"
    app = create_app(db_path=db_path, artifacts_root=artifacts_root)
    return TestClient(app), db_path, artifacts_root


def create_capture(client: TestClient) -> dict[str, str]:
    response = client.post(
        "/captures/discover",
        json={
            "platform": "bilibili",
            "canonical_url": "https://www.bilibili.com/video/BV1AB411c7mD",
            "source_kind": "manual_url",
            "quick_capture_preset": "metadata_only",
        },
    )
    assert response.status_code == 201
    return response.json()


def enqueue_metadata_fetch(client: TestClient, capture_id: str) -> dict[str, str]:
    response = client.post(f"/captures/{capture_id}/metadata-fetch/jobs")
    assert response.status_code == 200
    return response.json()


def mark_job_running(db_path: Path, job_id: str) -> None:
    with sqlite3.connect(db_path) as conn:
        conn.execute(
            """
            UPDATE jobs
            SET status = ?, started_at = datetime('now')
            WHERE job_id = ?
            """,
            ("running", job_id),
        )
        conn.commit()


def complete_failed_metadata_fetch(client: TestClient, capture_id: str, job: dict[str, str]) -> None:
    response = client.post(
        f"/jobs/{job['job_id']}/complete",
        json={
            "job_id": job["job_id"],
            "capture_id": capture_id,
            "job_type": "metadata_fetch",
            "producer": "workers.bili",
            "producer_version": "0.1.0",
            "engine": "BBDown",
            "engine_version": "1.6.3",
            "idempotency": {
                "job_attempt": 1,
                "dedupe_key": job["dedupe_key"],
            },
            "platform_result": "parser_drift",
            "produced_assets": [],
            "logs": {
                "job_log_path": "logs/jobs/metadata-fetch.log",
                "stderr_path": None,
            },
            "duration_seconds": 0.5,
            "next_status": "metadata_fetched",
        },
    )
    assert response.status_code == 200


def complete_ok_metadata_fetch(
    client: TestClient,
    capture_id: str,
    job: dict[str, str],
    artifacts_root: Path,
) -> None:
    from scoutflow_api.external_tools.bbdown_info_parser import parse_bbdown_info_output
    from scoutflow_api.metadata_probe_receipt_bridge import (
        MetadataProbeEvidenceSource,
        build_metadata_fetch_receipt,
        materialize_metadata_probe_assets,
        prepare_success_metadata_probe_assets,
    )

    parsed = parse_bbdown_info_output(
        "\n".join(
            [
                "BBDown -info sanitized fixture",
                "Result: ok",
                "Platform Item ID: BV1AB411c7mD",
                "Title: Trust Trace snapshot",
                "Duration: 00:07:10",
                "Page Count: 1",
                "Selected Page: P1",
            ]
        )
    )
    source = MetadataProbeEvidenceSource(
        task_id="T-P1A-011C",
        report_path="docs/research/t-p1a-011c-bbdown-auth-present-info-probe-report-2026-05-04.md",
        probe_mode="auth-present",
    )
    prepared = prepare_success_metadata_probe_assets(
        parsed=parsed,
        source_url="https://www.bilibili.com/video/BV1AB411c7mD",
        evidence_source=source,
    )
    materialized = materialize_metadata_probe_assets(
        artifacts_root=artifacts_root,
        capture_id=capture_id,
        assets=list(prepared),
    )
    receipt = build_metadata_fetch_receipt(
        capture_id=capture_id,
        job_id=job["job_id"],
        dedupe_key=job["dedupe_key"],
        source_url="https://www.bilibili.com/video/BV1AB411c7mD",
        evidence_source=source,
        materialized_assets=materialized,
    )
    response = client.post(f"/jobs/{job['job_id']}/complete", json=receipt.model_dump(mode="json"))
    assert response.status_code == 200


def trust_trace(client: TestClient, capture_id: str) -> dict[str, object]:
    response = client.get(f"/captures/{capture_id}/trust-trace")
    assert response.status_code == 200
    return response.json()


def stable_trace(body: dict[str, object]) -> dict[str, object]:
    stable = json.loads(json.dumps(body))
    capture_id = stable["capture"]["capture_id"]
    stable["capture"]["capture_id"] = "<capture_id>"

    if stable["metadata_job"]["job_id"] is not None:
        stable["metadata_job"]["job_id"] = "<job_id>"

    evidence_file_path = stable["audit"]["evidence_file_path"]
    if evidence_file_path is not None:
        stable["audit"]["evidence_file_path"] = evidence_file_path.replace(capture_id, "<capture_id>")

    return stable


def expected_status_trace(job_status: str | None, platform_result: str | None = None) -> dict[str, object]:
    return {
        "label": "Status / Trust Trace / 采集状态",
        "capture": {
            "capture_id": "<capture_id>",
            "platform": "bilibili",
            "platform_item_id": "BV1AB411c7mD",
            "source_kind": "manual_url",
            "capture_mode": "metadata_only",
            "created_by_path": "quick_capture",
        },
        "capture_state": {
            "capture_created": True,
            "status": "discovered",
        },
        "metadata_job": {
            "present": job_status is not None,
            "job_id": "<job_id>" if job_status is not None else None,
            "job_type": "metadata_fetch" if job_status is not None else None,
            "status": job_status,
            "platform_result": platform_result,
        },
        "probe_evidence": {
            "present": False,
            "probe_mode": "not-run",
            "source_task_id": None,
            "source_report_path": None,
            "platform_result": None,
        },
        "receipt_ledger": {
            "present": False,
            "artifact_count": 0,
            "artifact_kinds": [],
            "redaction": "not_applicable",
        },
        "media_audio": {
            "status": "not_approved",
            "audio_transcript": "blocked",
        },
        "audit": {
            "platform_result": platform_result,
            "evidence_file_path": None,
            "artifact_count": 0,
            "redaction_policy": None,
            "safe_parsed_fields": {},
        },
    }


def test_trust_trace_created_without_job_snapshot(tmp_path: Path) -> None:
    client, _, _ = build_client(tmp_path)
    capture = create_capture(client)

    assert stable_trace(trust_trace(client, capture["capture_id"])) == expected_status_trace(None)


def test_trust_trace_queued_job_snapshot(tmp_path: Path) -> None:
    client, _, _ = build_client(tmp_path)
    capture = create_capture(client)
    enqueue_metadata_fetch(client, capture["capture_id"])

    assert stable_trace(trust_trace(client, capture["capture_id"])) == expected_status_trace("queued")


def test_trust_trace_running_job_snapshot(tmp_path: Path) -> None:
    client, db_path, _ = build_client(tmp_path)
    capture = create_capture(client)
    job = enqueue_metadata_fetch(client, capture["capture_id"])
    mark_job_running(db_path, job["job_id"])

    assert stable_trace(trust_trace(client, capture["capture_id"])) == expected_status_trace("running")


def test_trust_trace_failed_job_snapshot(tmp_path: Path) -> None:
    client, _, _ = build_client(tmp_path)
    capture = create_capture(client)
    job = enqueue_metadata_fetch(client, capture["capture_id"])
    complete_failed_metadata_fetch(client, capture["capture_id"], job)

    assert stable_trace(trust_trace(client, capture["capture_id"])) == expected_status_trace("failed", "parser_drift")


def test_trust_trace_metadata_fetched_receipt_snapshot(tmp_path: Path) -> None:
    client, _, artifacts_root = build_client(tmp_path)
    capture = create_capture(client)
    job = enqueue_metadata_fetch(client, capture["capture_id"])
    complete_ok_metadata_fetch(client, capture["capture_id"], job, artifacts_root)

    assert stable_trace(trust_trace(client, capture["capture_id"])) == {
        "label": "Receipt / Ledger Trace",
        "capture": {
            "capture_id": "<capture_id>",
            "platform": "bilibili",
            "platform_item_id": "BV1AB411c7mD",
            "source_kind": "manual_url",
            "capture_mode": "metadata_only",
            "created_by_path": "quick_capture",
        },
        "capture_state": {
            "capture_created": True,
            "status": "metadata_fetched",
        },
        "metadata_job": {
            "present": True,
            "job_id": "<job_id>",
            "job_type": "metadata_fetch",
            "status": "succeeded",
            "platform_result": "ok",
        },
        "probe_evidence": {
            "present": True,
            "probe_mode": "auth-present",
            "source_task_id": "T-P1A-011C",
            "source_report_path": "docs/research/t-p1a-011c-bbdown-auth-present-info-probe-report-2026-05-04.md",
            "platform_result": "ok",
        },
        "receipt_ledger": {
            "present": True,
            "artifact_count": 2,
            "artifact_kinds": [
                "safe_metadata_evidence",
                "metadata_probe_summary",
            ],
            "redaction": "applied",
        },
        "media_audio": {
            "status": "not_approved",
            "audio_transcript": "blocked",
        },
        "audit": {
            "platform_result": "ok",
            "evidence_file_path": "data/artifacts/bilibili/<capture_id>/bundle/safe-metadata-evidence.json",
            "artifact_count": 2,
            "redaction_policy": "credentials-v1",
            "safe_parsed_fields": {
                "platform_item_id": "BV1AB411c7mD",
                "title": "Trust Trace snapshot",
                "duration_seconds": 430,
                "page_count": 1,
                "selected_page": "P1",
            },
        },
    }


def test_trust_trace_snapshots_do_not_expose_runtime_or_candidate_fields(tmp_path: Path) -> None:
    client, _, artifacts_root = build_client(tmp_path)
    capture = create_capture(client)
    job = enqueue_metadata_fetch(client, capture["capture_id"])
    complete_ok_metadata_fetch(client, capture["capture_id"], job, artifacts_root)

    serialized = json.dumps(trust_trace(client, capture["capture_id"]), ensure_ascii=False)

    assert "stdout" not in serialized
    assert "stderr" not in serialized
    assert "cookie" not in serialized.lower()
    assert "authorization" not in serialized.lower()
    assert "signed_url" not in serialized.lower()
    assert "comments" not in serialized.lower()
    assert "danmaku" not in serialized.lower()
    assert "screenshot" not in serialized.lower()
    assert "token_count" not in serialized.lower()
    assert "cost_estimate" not in serialized.lower()
    assert "audio_transcript" in serialized
    assert "blocked" in serialized
