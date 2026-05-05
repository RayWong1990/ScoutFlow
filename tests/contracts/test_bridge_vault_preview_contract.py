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


def test_vault_preview_renders_capture_truth_only(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("SCOUTFLOW_VAULT_ROOT", "/tmp/scoutflow-vault")
    client = build_client(tmp_path)
    capture = create_capture(client)

    response = client.get(f"/captures/{capture['capture_id']}/vault-preview")
    assert response.status_code == 200
    body = response.json()
    assert body["capture_id"] == capture["capture_id"]
    assert body["target_path"].startswith(f"/tmp/scoutflow-vault/00-Inbox/scoutflow-{capture['capture_id']}-")
    assert body["frontmatter"]["status"] == "pending"
    assert "canonical_url" in body["body_markdown"]


def test_vault_preview_requires_vault_root(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.delenv("SCOUTFLOW_VAULT_ROOT", raising=False)
    client = build_client(tmp_path)
    capture = create_capture(client)

    response = client.get(f"/captures/{capture['capture_id']}/vault-preview")
    assert response.status_code == 409
    assert response.json()["code"] == "vault_root_unset"


def test_vault_preview_rejects_unknown_capture(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("SCOUTFLOW_VAULT_ROOT", "/tmp/scoutflow-vault")
    client = build_client(tmp_path)

    response = client.get("/captures/cap_missing/vault-preview")
    assert response.status_code == 404
    assert response.json()["code"] == "capture_not_found"
