from __future__ import annotations

import sys
from pathlib import Path

from fastapi.testclient import TestClient


ROOT = Path(__file__).resolve().parents[2]
API_ROOT = ROOT / "services" / "api"
if str(API_ROOT) not in sys.path:
    sys.path.insert(0, str(API_ROOT))


def build_client(tmp_path: Path) -> TestClient:
    from scoutflow_api.bridge import router as bridge_router
    from scoutflow_api.main import create_app

    runtime_root = tmp_path / "runtime"
    db_path = runtime_root / "data" / "db" / "scoutflow.sqlite"
    artifacts_root = runtime_root / "data" / "artifacts"
    app = create_app(db_path=db_path, artifacts_root=artifacts_root)
    app.include_router(bridge_router)
    return TestClient(app)


def test_bridge_health_reports_write_disabled(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.delenv("SCOUTFLOW_VAULT_ROOT", raising=False)
    client = build_client(tmp_path)

    response = client.get("/bridge/health")
    assert response.status_code == 200
    body = response.json()
    assert body["bridge_available"] is True
    assert body["write_enabled"] is False
    assert "write_disabled" in body["blocked_by"]


def test_bridge_config_fails_loud_when_vault_root_missing(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.delenv("SCOUTFLOW_VAULT_ROOT", raising=False)
    client = build_client(tmp_path)

    response = client.get("/bridge/vault/config")
    assert response.status_code == 200
    body = response.json()
    assert body["vault_root_resolved"] is False
    assert body["preview_enabled"] is False
    assert body["write_enabled"] is False
    assert body["error"]["code"] == "vault_root_unset"


def test_bridge_config_echoes_resolved_root_without_enabling_write(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("SCOUTFLOW_VAULT_ROOT", "/tmp/scoutflow-vault")
    client = build_client(tmp_path)

    response = client.get("/bridge/vault/config")
    assert response.status_code == 200
    body = response.json()
    assert body["vault_root_resolved"] is True
    assert body["vault_root"] == "/tmp/scoutflow-vault"
    assert isinstance(body["preview_enabled"], bool)
    assert body["write_enabled"] is False
