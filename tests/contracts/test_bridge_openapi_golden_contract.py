from __future__ import annotations

import json
import sys
from pathlib import Path

from fastapi.testclient import TestClient


ROOT = Path(__file__).resolve().parents[2]
API_ROOT = ROOT / "services" / "api"
DEFAULT_GOLDEN_PATH = ROOT / "tests" / "contracts" / "golden" / "bridge-openapi-2026-05-06.json"
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


def normalize_openapi(schema: dict) -> dict:
    def response_ref(path: str, method: str, status: str) -> str:
        return schema["paths"][path][method]["responses"][status]["content"]["application/json"]["schema"]["$ref"].split("/")[-1]

    def signature(name: str) -> dict:
        component = schema["components"]["schemas"][name]
        properties = component.get("properties", {})
        payload = {
            "required": sorted(component.get("required", [])),
            "properties": sorted(properties.keys()),
        }
        if name == "BridgeVaultCommitResponse":
            payload["write_enabled_const"] = properties["write_enabled"].get("const")
        if name == "BridgeErrorCode":
            return {"enum": component["enum"]}
        return payload

    return {
        "paths": {
            "/bridge/health": {
                "get": {
                    "status_200": response_ref("/bridge/health", "get", "200"),
                }
            },
            "/bridge/vault/config": {
                "get": {
                    "status_200": response_ref("/bridge/vault/config", "get", "200"),
                }
            },
            "/captures/{capture_id}/vault-preview": {
                "get": {
                    "status_200": response_ref("/captures/{capture_id}/vault-preview", "get", "200"),
                    "status_404": response_ref("/captures/{capture_id}/vault-preview", "get", "404"),
                    "status_409": response_ref("/captures/{capture_id}/vault-preview", "get", "409"),
                }
            },
            "/captures/{capture_id}/vault-commit": {
                "post": {
                    "status_200": response_ref("/captures/{capture_id}/vault-commit", "post", "200"),
                    "status_404": response_ref("/captures/{capture_id}/vault-commit", "post", "404"),
                    "status_409": response_ref("/captures/{capture_id}/vault-commit", "post", "409"),
                }
            },
        },
        "schemas": {
            "BridgeHealthResponse": signature("BridgeHealthResponse"),
            "BridgeVaultConfigResponse": signature("BridgeVaultConfigResponse"),
            "BridgeVaultPreviewResponse": signature("BridgeVaultPreviewResponse"),
            "BridgeVaultCommitResponse": signature("BridgeVaultCommitResponse"),
            "BridgeErrorCode": signature("BridgeErrorCode"),
            "ErrorResponse": signature("ErrorResponse"),
        },
    }


def load_golden_path(request) -> Path:
    golden_arg = request.config.getoption("golden")
    return Path(golden_arg) if golden_arg else DEFAULT_GOLDEN_PATH


def test_bridge_openapi_matches_golden_contract(tmp_path: Path, request) -> None:
    client = build_client(tmp_path)
    actual = normalize_openapi(client.app.openapi())
    expected = json.loads(load_golden_path(request).read_text(encoding="utf-8"))
    assert actual == expected


def test_bridge_schema_fields_match_lp13_contract(tmp_path: Path) -> None:
    client = build_client(tmp_path)
    normalized = normalize_openapi(client.app.openapi())

    assert normalized["schemas"]["BridgeHealthResponse"]["properties"] == [
        "blocked_by",
        "bridge_available",
        "spec_version",
        "write_enabled",
    ]
    assert normalized["schemas"]["BridgeVaultPreviewResponse"]["properties"] == [
        "body_markdown",
        "capture_id",
        "frontmatter",
        "target_path",
        "warnings",
    ]
    assert normalized["schemas"]["BridgeVaultCommitResponse"]["properties"] == [
        "capture_id",
        "committed",
        "dry_run",
        "error",
        "target_path",
        "write_enabled",
    ]
    assert normalized["schemas"]["BridgeVaultCommitResponse"]["write_enabled_const"] is False


def test_bridge_write_enabled_and_preview_excerpt_stay_bounded(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("SCOUTFLOW_VAULT_ROOT", "/tmp/scoutflow-vault")
    client = build_client(tmp_path)

    health = client.get("/bridge/health")
    assert health.status_code == 200
    assert health.json()["write_enabled"] is False

    config = client.get("/bridge/vault/config")
    assert config.status_code == 200
    assert config.json()["write_enabled"] is False

    capture = create_capture(client)

    preview = client.get(f"/captures/{capture['capture_id']}/vault-preview")
    assert preview.status_code == 200
    assert len(preview.json()["body_markdown"].splitlines()) >= 20

    commit = client.post(f"/captures/{capture['capture_id']}/vault-commit")
    assert commit.status_code == 200
    assert commit.json()["write_enabled"] is False
