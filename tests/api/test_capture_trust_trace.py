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


def seed_job(
    db_path: Path,
    capture_id: str,
    *,
    job_id: str = "job-metadata-1",
    dedupe_key: str = "bilibili:BV19D9eB9Etg:metadata_fetch",
    status: str = "running",
) -> None:
    with sqlite3.connect(db_path) as conn:
        conn.execute(
            """
            INSERT INTO jobs (job_id, capture_id, job_type, status, dedupe_key, queued_at, started_at)
            VALUES (?, ?, ?, ?, ?, datetime('now'), datetime('now'))
            """,
            (job_id, capture_id, "metadata_fetch", status, dedupe_key),
        )
        conn.commit()


def test_trust_trace_without_receipt_uses_status_label(tmp_path: Path) -> None:
    client, _, _ = build_client(tmp_path)
    capture = create_capture(client)

    response = client.get(f"/captures/{capture['capture_id']}/trust-trace")

    assert response.status_code == 200
    body = response.json()
    assert body["label"] == "Status / Trust Trace / 采集状态"
    assert body["capture"]["source_kind"] == "manual_url"
    assert body["capture_state"]["status"] == "discovered"
    assert body["metadata_job"]["present"] is False
    assert body["probe_evidence"] == {
        "present": False,
        "probe_mode": "not-run",
        "source_task_id": None,
        "source_report_path": None,
        "platform_result": None,
    }
    assert body["receipt_ledger"]["present"] is False
    assert body["receipt_ledger"]["artifact_count"] == 0
    assert body["receipt_ledger"]["artifact_kinds"] == []
    assert body["media_audio"] == {"status": "not_approved", "audio_transcript": "blocked"}
    assert "stdout" not in json.dumps(body)
    assert "stderr" not in json.dumps(body)


def test_trust_trace_metadata_fetch_queued_and_running_are_status_trace(tmp_path: Path) -> None:
    client, db_path, _ = build_client(tmp_path)
    capture = create_capture(client)

    enqueue = client.post(f"/captures/{capture['capture_id']}/metadata-fetch/jobs")
    assert enqueue.status_code == 200
    queued_trace = client.get(f"/captures/{capture['capture_id']}/trust-trace")
    assert queued_trace.status_code == 200

    queued_body = queued_trace.json()
    assert queued_body["label"] == "Status / Trust Trace / 采集状态"
    assert queued_body["capture_state"]["status"] == "discovered"
    assert queued_body["metadata_job"]["present"] is True
    assert queued_body["metadata_job"]["job_type"] == "metadata_fetch"
    assert queued_body["metadata_job"]["status"] == "queued"
    assert queued_body["metadata_job"]["platform_result"] is None
    assert queued_body["probe_evidence"]["present"] is False
    assert queued_body["receipt_ledger"]["present"] is False
    assert queued_body["media_audio"] == {"status": "not_approved", "audio_transcript": "blocked"}

    with sqlite3.connect(db_path) as conn:
        conn.execute(
            """
            UPDATE jobs
            SET status = ?, started_at = datetime('now')
            WHERE job_id = ?
            """,
            ("running", enqueue.json()["job_id"]),
        )
        conn.commit()

    running_trace = client.get(f"/captures/{capture['capture_id']}/trust-trace")
    assert running_trace.status_code == 200
    running_body = running_trace.json()
    assert running_body["label"] == "Status / Trust Trace / 采集状态"
    assert running_body["capture_state"]["status"] == "discovered"
    assert running_body["metadata_job"]["present"] is True
    assert running_body["metadata_job"]["job_type"] == "metadata_fetch"
    assert running_body["metadata_job"]["status"] == "running"
    assert running_body["metadata_job"]["platform_result"] is None
    assert running_body["probe_evidence"]["present"] is False
    assert running_body["receipt_ledger"]["present"] is False
    assert running_body["media_audio"] == {"status": "not_approved", "audio_transcript": "blocked"}


def test_trust_trace_with_auth_present_receipt_uses_receipt_label(tmp_path: Path) -> None:
    from scoutflow_api.external_tools.bbdown_info_parser import parse_bbdown_info_output
    from scoutflow_api.metadata_probe_receipt_bridge import (
        MetadataProbeEvidenceSource,
        build_metadata_fetch_receipt,
        materialize_metadata_probe_assets,
        prepare_success_metadata_probe_assets,
    )

    client, db_path, artifacts_root = build_client(tmp_path)
    capture = create_capture(client)
    seed_job(db_path, capture["capture_id"])

    parsed = parse_bbdown_info_output(
        "\n".join(
            [
                "BBDown -info sanitized fixture",
                "Result: ok",
                "Platform Item ID: 116493572377107",
                "Title: Trust Trace sample",
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
        source_url="https://www.bilibili.com/video/BV19D9eB9Etg",
        evidence_source=source,
    )
    materialized = materialize_metadata_probe_assets(
        artifacts_root=artifacts_root,
        capture_id=capture["capture_id"],
        assets=list(prepared),
    )
    receipt = build_metadata_fetch_receipt(
        capture_id=capture["capture_id"],
        job_id="job-metadata-1",
        dedupe_key="bilibili:BV19D9eB9Etg:metadata_fetch",
        source_url="https://www.bilibili.com/video/BV19D9eB9Etg",
        evidence_source=source,
        materialized_assets=materialized,
    )
    complete = client.post("/jobs/job-metadata-1/complete", json=receipt.model_dump(mode="json"))
    assert complete.status_code == 200

    response = client.get(f"/captures/{capture['capture_id']}/trust-trace")

    assert response.status_code == 200
    body = response.json()
    assert body["label"] == "Receipt / Ledger Trace"
    assert body["capture_state"]["status"] == "metadata_fetched"
    assert body["metadata_job"]["present"] is True
    assert body["metadata_job"]["status"] == "succeeded"
    assert body["metadata_job"]["platform_result"] == "ok"
    assert body["probe_evidence"]["present"] is True
    assert body["probe_evidence"]["probe_mode"] == "auth-present"
    assert body["probe_evidence"]["source_task_id"] == "T-P1A-011C"
    assert body["receipt_ledger"]["present"] is True
    assert body["receipt_ledger"]["artifact_count"] == 2
    assert body["receipt_ledger"]["artifact_kinds"] == [
        "safe_metadata_evidence",
        "metadata_probe_summary",
    ]
    assert body["audit"]["redaction_policy"] == "credentials-v1"
    assert body["audit"]["safe_parsed_fields"]["platform_item_id"] == "116493572377107"
    dump = json.dumps(body)
    assert "stdout" not in dump
    assert "stderr" not in dump
    assert "cookie" not in dump
    assert "authorization" not in dump
    assert "signed_url" not in dump


def test_trust_trace_non_ok_job_keeps_capture_state_without_receipt(tmp_path: Path) -> None:
    client, db_path, _ = build_client(tmp_path)
    capture = create_capture(client)
    seed_job(db_path, capture["capture_id"])

    payload = {
        "job_id": "job-metadata-1",
        "capture_id": capture["capture_id"],
        "job_type": "metadata_fetch",
        "producer": "workers.bili",
        "producer_version": "0.1.0",
        "engine": "BBDown",
        "engine_version": "1.6.3",
        "idempotency": {
            "job_attempt": 1,
            "dedupe_key": "bilibili:BV19D9eB9Etg:metadata_fetch",
        },
        "platform_result": "parser_drift",
        "produced_assets": [],
        "logs": {
            "job_log_path": "logs/jobs/metadata-fetch.log",
            "stderr_path": None,
        },
        "duration_seconds": 0.5,
        "next_status": "metadata_fetched",
    }
    complete = client.post("/jobs/job-metadata-1/complete", json=payload)
    assert complete.status_code == 200

    response = client.get(f"/captures/{capture['capture_id']}/trust-trace")

    assert response.status_code == 200
    body = response.json()
    assert body["label"] == "Status / Trust Trace / 采集状态"
    assert body["metadata_job"]["status"] == "failed"
    assert body["metadata_job"]["platform_result"] == "parser_drift"
    assert body["capture_state"]["status"] == "discovered"
    assert body["receipt_ledger"]["present"] is False
    assert body["probe_evidence"]["present"] is False


def test_trust_trace_refuses_non_manual_source_kind(tmp_path: Path) -> None:
    client, db_path, _ = build_client(tmp_path)
    capture = create_capture(client)
    with sqlite3.connect(db_path) as conn:
        conn.execute(
            "UPDATE captures SET source_kind = ?, created_by_path = ? WHERE capture_id = ?",
            ("recommendation", "signal", capture["capture_id"]),
        )
        conn.commit()

    response = client.get(f"/captures/{capture['capture_id']}/trust-trace")

    assert response.status_code == 409
    assert response.json()["code"] == "trust_trace_source_kind_not_allowed"
