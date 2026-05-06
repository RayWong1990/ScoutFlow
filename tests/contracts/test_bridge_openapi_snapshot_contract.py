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


def test_bridge_openapi_paths_and_schema_refs_are_stable(tmp_path: Path) -> None:
    client = build_client(tmp_path)
    openapi = client.app.openapi()

    expected_paths = {
        "/bridge/health": ("get", "BridgeHealthResponse"),
        "/bridge/vault/config": ("get", "BridgeVaultConfigResponse"),
        "/captures/{capture_id}/vault-preview": ("get", "BridgeVaultPreviewResponse"),
        "/captures/{capture_id}/vault-commit": ("post", "BridgeVaultCommitResponse"),
    }

    for path, (method, schema_name) in expected_paths.items():
        assert path in openapi["paths"]
        response_schema = openapi["paths"][path][method]["responses"]["200"]["content"]["application/json"]["schema"]
        assert response_schema["$ref"] == f"#/components/schemas/{schema_name}"


def test_bridge_error_responses_reference_error_response_schema(tmp_path: Path) -> None:
    client = build_client(tmp_path)
    openapi = client.app.openapi()

    for path, method in [
        ("/captures/{capture_id}/vault-preview", "get"),
        ("/captures/{capture_id}/vault-commit", "post"),
    ]:
        responses = openapi["paths"][path][method]["responses"]
        for status_code in ("404", "409", "503"):
            schema = responses[status_code]["content"]["application/json"]["schema"]
            assert schema["$ref"] == "#/components/schemas/ErrorResponse"


def test_bridge_commit_schema_exposes_dry_run_flag(tmp_path: Path) -> None:
    client = build_client(tmp_path)
    openapi = client.app.openapi()

    commit_schema = openapi["components"]["schemas"]["BridgeVaultCommitResponse"]["properties"]
    assert commit_schema["dry_run"]["type"] == "boolean"
    assert commit_schema["committed"]["type"] == "boolean"
    assert commit_schema["target_path"]["anyOf"][0]["type"] == "string"


def test_bridge_error_code_enum_retains_local_namespace(tmp_path: Path) -> None:
    client = build_client(tmp_path)
    openapi = client.app.openapi()

    enum_values = set(openapi["components"]["schemas"]["BridgeErrorCode"]["enum"])
    assert "write_disabled" in enum_values
    assert "capture_not_found" in enum_values
    assert "vault_root_unset" in enum_values
