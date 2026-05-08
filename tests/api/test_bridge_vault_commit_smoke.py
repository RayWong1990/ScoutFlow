from __future__ import annotations

import sys
from pathlib import Path

from fastapi.testclient import TestClient


ROOT = Path(__file__).resolve().parents[2]
API_ROOT = ROOT / "services" / "api"
if str(API_ROOT) not in sys.path:
    sys.path.insert(0, str(API_ROOT))


def build_client(tmp_path: Path) -> TestClient:
    from scoutflow_api.main import create_app

    runtime_root = tmp_path / "runtime"
    db_path = runtime_root / "data" / "db" / "scoutflow.sqlite"
    artifacts_root = runtime_root / "data" / "artifacts"
    app = create_app(db_path=db_path, artifacts_root=artifacts_root)
    return TestClient(app)


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


def test_commit_smoke_returns_candidate_only_and_keeps_write_disabled(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("SCOUTFLOW_VAULT_ROOT", "/tmp/scoutflow-vault")
    client = build_client(tmp_path)
    capture = create_capture(client)

    response = client.post(f"/captures/{capture['capture_id']}/vault-commit")
    assert response.status_code == 200
    body = response.json()
    assert body["capture_id"] == capture["capture_id"]
    assert body["committed"] is False
    assert body["dry_run"] is True
    assert body["write_enabled"] is False
    assert body["candidate"]["spec_version"] == "VaultCommitCandidateV1"
    assert len(body["candidate"]["roles"]) == 12
    assert body["candidate"]["secret_scan"]["blocked"] is False
    assert body["candidate"]["atomic_write_preconditions"]["ready_for_true_write"] is False
    assert body["candidate"]["future_same_payload_gate"]["p3b_state"] == "blocked_pending_explicit_true_write_gate"
