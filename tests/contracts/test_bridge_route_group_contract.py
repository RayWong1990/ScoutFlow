from __future__ import annotations

import sys
from pathlib import Path

import pytest
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


def test_bridge_routes_are_registered_on_a_host_app(tmp_path: Path) -> None:
    client = build_client(tmp_path)

    route_paths = {route.path for route in client.app.routes}
    assert "/bridge/health" in route_paths
    assert "/bridge/vault/config" in route_paths
    assert "/captures/{capture_id}/vault-preview" in route_paths
    assert "/captures/{capture_id}/vault-commit" in route_paths


def test_bridge_health_stays_non_mutating_and_write_disabled(tmp_path: Path) -> None:
    client = build_client(tmp_path)

    response = client.get("/bridge/health")
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body["bridge_available"], bool)
    assert body["write_enabled"] is False
    assert body["blocked_by"]


def test_bridge_vault_config_uses_raw_4_field_contract(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("SCOUTFLOW_VAULT_ROOT", raising=False)
    client = build_client(tmp_path)

    response = client.get("/bridge/vault/config")
    assert response.status_code == 200
    body = response.json()
    assert body["frontmatter_mode"] == "raw_4_field"
    assert body["write_enabled"] is False
    assert body["error"]["code"] in {"bridge_not_implemented", "vault_root_unset"}


def test_bridge_openapi_exposes_bridge_error_codes(tmp_path: Path) -> None:
    client = build_client(tmp_path)

    openapi = client.app.openapi()
    assert "/bridge/health" in openapi["paths"]
    assert "/bridge/vault/config" in openapi["paths"]
    assert "BridgeHealthResponse" in openapi["components"]["schemas"]
    assert "BridgeVaultConfigResponse" in openapi["components"]["schemas"]
    assert "BridgeVaultPreviewResponse" in openapi["components"]["schemas"]
    assert "BridgeVaultCommitResponse" in openapi["components"]["schemas"]
    assert set(openapi["components"]["schemas"]["BridgeErrorCode"]["enum"]) == {
        "bridge_not_implemented",
        "vault_root_unset",
        "capture_not_found",
        "capture_state_blocked",
        "metadata_missing",
        "frontmatter_invalid",
        "path_escape_blocked",
        "write_disabled",
    }
