"""End-to-end test for the T-P1A-019 dry-run metadata orchestrator (path A).

Path A integration: discover capture (T-P1A-001) → enqueue metadata_fetch job
(T-P1A-018) → dry-run probe with injected fake ok runner (T-P1A-019) → POST
/jobs/{job_id}/complete with the receipt candidate (T-P1A-012) → GET
trust-trace (T-P1A-013) and verify the metadata_job + receipt_ledger layers.

This test never invokes real BBDown, never uses live URLs, never downloads
media, and never enables audio_transcript runtime. The injected runner is the
sole execution surface; the fixture stdout is a sanitized capture from
T-P1A-011C.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient


ROOT = Path(__file__).resolve().parents[2]
API_ROOT = ROOT / "services" / "api"
FIXTURE_ROOT = ROOT / "tests" / "fixtures" / "bbdown"
if str(API_ROOT) not in sys.path:
    sys.path.insert(0, str(API_ROOT))


SAMPLE_URL = "https://www.bilibili.com/video/BV1AB411c7mD"


def _read_fixture(name: str) -> str:
    return (FIXTURE_ROOT / name).read_text(encoding="utf-8")


def _build_client(tmp_path: Path) -> tuple[TestClient, Path, Path]:
    from scoutflow_api.main import create_app

    runtime_root = tmp_path / "runtime"
    db_path = runtime_root / "data" / "db" / "scoutflow.sqlite"
    artifacts_root = runtime_root / "data" / "artifacts"
    app = create_app(db_path=db_path, artifacts_root=artifacts_root)
    return TestClient(app), db_path, artifacts_root


def _discover_capture(client: TestClient, *, canonical_url: str = SAMPLE_URL) -> dict[str, str]:
    response = client.post(
        "/captures/discover",
        json={
            "platform": "bilibili",
            "canonical_url": canonical_url,
            "source_kind": "manual_url",
            "quick_capture_preset": "metadata_only",
        },
    )
    assert response.status_code == 201, response.text
    return response.json()


def _enqueue_job(client: TestClient, capture_id: str) -> dict[str, str]:
    response = client.post(f"/captures/{capture_id}/metadata-fetch/jobs")
    assert response.status_code == 200, response.text
    return response.json()


def _ok_runner():
    from scoutflow_api.external_tools.bbdown_info_adapter import BBDownInfoCommand, BBDownInfoRunnerOutput

    def runner(_: BBDownInfoCommand) -> BBDownInfoRunnerOutput:
        return BBDownInfoRunnerOutput(exit_code=0, stdout_text=_read_fixture("info_public_ok_sanitized.txt"))

    return runner


def test_dry_run_to_complete_flows_through_18_endpoints_and_lights_up_trust_trace(tmp_path: Path) -> None:
    from scoutflow_api.orchestration import dry_run_metadata_probe

    client, _db_path, artifacts_root = _build_client(tmp_path)

    capture = _discover_capture(client)
    capture_id = capture["capture_id"]

    enqueue = _enqueue_job(client, capture_id)
    job_id = enqueue["job_id"]
    dedupe_key = enqueue["dedupe_key"]
    assert enqueue["status"] == "queued"
    assert dedupe_key.startswith("bilibili:")
    assert dedupe_key.endswith(":metadata_fetch")

    outcome = dry_run_metadata_probe(
        capture_id=capture_id,
        job_id=job_id,
        dedupe_key=dedupe_key,
        manual_url=SAMPLE_URL,
        job_temp_dir=tmp_path / "bbdown-info-job",
        artifacts_root=artifacts_root,
        runner=_ok_runner(),
    )

    assert outcome.success_evidence_emitted is True
    assert outcome.receipt_candidate is not None
    assert outcome.receipt_candidate.idempotency.dedupe_key == dedupe_key

    receipt_payload = outcome.receipt_candidate.model_dump(mode="json")
    response = client.post(f"/jobs/{job_id}/complete", json=receipt_payload)
    assert response.status_code == 200, response.text
    body = response.json()
    assert body["status"] == "succeeded"
    assert body["platform_result"] == "ok"
    assert body["job_type"] == "metadata_fetch"
    assert body["artifact_count"] >= 2

    trust_response = client.get(f"/captures/{capture_id}/trust-trace")
    assert trust_response.status_code == 200, trust_response.text
    trust = trust_response.json()
    assert trust["metadata_job"]["present"] is True
    assert trust["metadata_job"]["status"] == "succeeded"
    assert trust["receipt_ledger"]["present"] is True
    assert trust["media_audio"]["audio_transcript"] == "blocked"


def test_replayed_completion_remains_idempotent_through_the_same_flow(tmp_path: Path) -> None:
    from scoutflow_api.orchestration import dry_run_metadata_probe

    client, _db_path, artifacts_root = _build_client(tmp_path)
    capture = _discover_capture(client)
    capture_id = capture["capture_id"]
    enqueue = _enqueue_job(client, capture_id)
    job_id = enqueue["job_id"]

    outcome = dry_run_metadata_probe(
        capture_id=capture_id,
        job_id=job_id,
        dedupe_key=enqueue["dedupe_key"],
        manual_url=SAMPLE_URL,
        job_temp_dir=tmp_path / "bbdown-info-job",
        artifacts_root=artifacts_root,
        runner=_ok_runner(),
    )
    receipt_payload = outcome.receipt_candidate.model_dump(mode="json")

    first = client.post(f"/jobs/{job_id}/complete", json=receipt_payload)
    second = client.post(f"/jobs/{job_id}/complete", json=receipt_payload)

    assert first.status_code == 200
    assert second.status_code == 200
    assert second.json()["idempotent"] is True


@pytest.mark.parametrize("fixture", ["info_auth_required_sanitized.txt", "info_parser_drift_sanitized.txt"])
def test_non_ok_outcome_does_not_produce_receipt_to_post(tmp_path: Path, fixture: str) -> None:
    from scoutflow_api.external_tools.bbdown_info_adapter import BBDownInfoCommand, BBDownInfoRunnerOutput
    from scoutflow_api.orchestration import dry_run_metadata_probe

    client, _db_path, artifacts_root = _build_client(tmp_path)
    capture = _discover_capture(client)
    capture_id = capture["capture_id"]
    enqueue = _enqueue_job(client, capture_id)

    def runner(_: BBDownInfoCommand) -> BBDownInfoRunnerOutput:
        return BBDownInfoRunnerOutput(exit_code=1, stdout_text=_read_fixture(fixture))

    outcome = dry_run_metadata_probe(
        capture_id=capture_id,
        job_id=enqueue["job_id"],
        dedupe_key=enqueue["dedupe_key"],
        manual_url=SAMPLE_URL,
        job_temp_dir=tmp_path / "bbdown-info-job",
        artifacts_root=artifacts_root,
        runner=runner,
    )

    assert outcome.success_evidence_emitted is False
    assert outcome.receipt_candidate is None

    trust = client.get(f"/captures/{capture_id}/trust-trace").json()
    assert trust["metadata_job"]["status"] == "queued"
    assert trust["receipt_ledger"]["present"] is False
    assert trust["media_audio"]["audio_transcript"] == "blocked"
