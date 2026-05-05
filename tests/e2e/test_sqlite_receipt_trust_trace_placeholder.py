from __future__ import annotations

import json
import sys
from pathlib import Path

from fastapi.testclient import TestClient


ROOT = Path(__file__).resolve().parents[2]
API_ROOT = ROOT / "services" / "api"
FIXTURE_PATH = ROOT / "tests" / "fixtures" / "walking_skeleton" / "trust_trace_placeholder.json"
if str(API_ROOT) not in sys.path:
    sys.path.insert(0, str(API_ROOT))


def _build_client(tmp_path: Path) -> TestClient:
    from scoutflow_api.main import create_app

    runtime_root = tmp_path / "runtime"
    db_path = runtime_root / "data" / "db" / "scoutflow.sqlite"
    artifacts_root = runtime_root / "data" / "artifacts"
    app = create_app(db_path=db_path, artifacts_root=artifacts_root)
    return TestClient(app)


def _load_fixture() -> dict[str, object]:
    return json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))


def _create_capture(client: TestClient) -> dict[str, str]:
    response = client.post(
        "/captures/discover",
        json={
            "platform": "bilibili",
            "canonical_url": "https://www.bilibili.com/video/BV1PLACEHOLDER",
            "source_kind": "manual_url",
            "quick_capture_preset": "metadata_only",
        },
    )
    assert response.status_code == 201
    return response.json()


def test_sqlite_trust_trace_placeholder_matches_safe_fixture(tmp_path: Path) -> None:
    client = _build_client(tmp_path)
    fixture = _load_fixture()
    capture = _create_capture(client)

    enqueue = client.post(f"/captures/{capture['capture_id']}/metadata-fetch/jobs")
    assert enqueue.status_code == 200

    response = client.get(f"/captures/{capture['capture_id']}/trust-trace")
    assert response.status_code == 200
    body = response.json()

    assert body["label"] == fixture["label"]
    assert body["capture"]["source_kind"] == fixture["capture"]["source_kind"]
    assert body["capture"]["capture_mode"] == fixture["capture"]["capture_mode"]
    assert body["capture_state"]["status"] == fixture["capture_state"]["status"]
    assert body["metadata_job"]["present"] == fixture["metadata_job"]["present"]
    assert body["metadata_job"]["job_type"] == fixture["metadata_job"]["job_type"]
    assert body["metadata_job"]["status"] == fixture["metadata_job"]["status"]
    assert body["metadata_job"]["platform_result"] == fixture["metadata_job"]["platform_result"]
    assert body["probe_evidence"]["present"] == fixture["probe_evidence"]["present"]
    assert body["probe_evidence"]["probe_mode"] == fixture["probe_evidence"]["probe_mode"]
    assert body["receipt_ledger"]["present"] == fixture["receipt_ledger"]["present"]
    assert body["receipt_ledger"]["artifact_count"] == fixture["receipt_ledger"]["artifact_count"]
    assert body["receipt_ledger"]["redaction"] == fixture["receipt_ledger"]["redaction"]
    assert body["media_audio"] == fixture["media_audio"]

    dump = json.dumps(body)
    assert "stdout" not in dump
    assert "stderr" not in dump
    assert "cookie" not in dump
