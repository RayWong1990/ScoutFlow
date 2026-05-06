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


def test_create_app_mounts_bridge_routes(tmp_path: Path) -> None:
    client = build_client(tmp_path)

    route_paths = {route.path for route in client.app.routes}
    assert "/bridge/health" in route_paths
    assert "/captures/{capture_id}/vault-preview" in route_paths
    assert "/captures/{capture_id}/vault-commit" in route_paths


def test_create_app_bridge_health_stays_write_disabled(tmp_path: Path) -> None:
    client = build_client(tmp_path)

    response = client.get("/bridge/health")
    assert response.status_code == 200
    body = response.json()
    assert body["write_enabled"] is False
    assert "write_disabled" in body["blocked_by"]


def test_create_app_bridge_commit_schema_and_dry_run_write_flag(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("SCOUTFLOW_VAULT_ROOT", "/tmp/scoutflow-vault")
    client = build_client(tmp_path)
    capture = create_capture(client)

    schema = client.app.openapi()
    commit_properties = schema["components"]["schemas"]["BridgeVaultCommitResponse"]["properties"]
    assert "write_enabled" in commit_properties

    response = client.post(f"/captures/{capture['capture_id']}/vault-commit")
    assert response.status_code == 200
    body = response.json()
    assert body["dry_run"] is True
    assert body["write_enabled"] is False
