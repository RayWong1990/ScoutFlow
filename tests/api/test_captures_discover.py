from __future__ import annotations

import json
import re
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


def test_happy_path_creates_metadata_only_capture(tmp_path: Path) -> None:
    client, db_path, artifacts_root = build_client(tmp_path)

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
    body = response.json()
    assert re.fullmatch(r"[0-9A-HJKMNP-TV-Z]{26}", body["capture_id"])
    assert body["platform"] == "bilibili"
    assert body["platform_item_id"] == "BV1AB411c7mD"
    assert body["source_kind"] == "manual_url"
    assert body["capture_mode"] == "metadata_only"
    assert body["created_by_path"] == "quick_capture"
    assert body["status"] == "discovered"
    assert body["artifact_root_path"] == f"data/artifacts/bilibili/{body['capture_id']}"
    assert body["manifest_path"] == (
        f"data/artifacts/bilibili/{body['capture_id']}/bundle/capture-manifest.json"
    )

    manifest_file = artifacts_root / "bilibili" / body["capture_id"] / "bundle" / "capture-manifest.json"
    assert manifest_file.is_file()
    manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
    assert manifest["capture_id"] == body["capture_id"]
    assert manifest["capture_mode"] == "metadata_only"

    with sqlite3.connect(db_path) as conn:
        capture_row = conn.execute(
            """
            SELECT source_kind, capture_mode, created_by_path, status, artifact_root_path, manifest_path
            FROM captures
            WHERE capture_id = ?
            """,
            (body["capture_id"],),
        ).fetchone()
        assert capture_row == (
            "manual_url",
            "metadata_only",
            "quick_capture",
            "discovered",
            body["artifact_root_path"],
            body["manifest_path"],
        )

        artifact_row = conn.execute(
            """
            SELECT artifact_zone, artifact_kind, file_path
            FROM artifact_assets
            WHERE capture_id = ?
            """,
            (body["capture_id"],),
        ).fetchone()
        assert artifact_row == (
            "bundle",
            "capture_manifest",
            body["manifest_path"],
        )


def test_audio_transcript_is_rejected_for_t_p1a_001(tmp_path: Path) -> None:
    client, _, _ = build_client(tmp_path)

    response = client.post(
        "/captures/discover",
        json={
            "platform": "bilibili",
            "canonical_url": "https://www.bilibili.com/video/BV1AB411c7mD",
            "source_kind": "manual_url",
            "quick_capture_preset": "audio_transcript",
        },
    )

    assert response.status_code == 422
    assert response.json()["code"] == "not_implemented_in_T-P1A-001"


def test_non_bilibili_url_is_rejected(tmp_path: Path) -> None:
    client, _, _ = build_client(tmp_path)

    response = client.post(
        "/captures/discover",
        json={
            "platform": "bilibili",
            "canonical_url": "https://example.com/video/BV1AB411c7mD",
            "source_kind": "manual_url",
            "quick_capture_preset": "metadata_only",
        },
    )

    assert response.status_code == 422
    assert response.json()["code"] == "unsupported_platform"


def test_bilibili_url_without_bv_id_is_rejected(tmp_path: Path) -> None:
    client, _, _ = build_client(tmp_path)

    response = client.post(
        "/captures/discover",
        json={
            "platform": "bilibili",
            "canonical_url": "https://www.bilibili.com/video/av123456",
            "source_kind": "manual_url",
            "quick_capture_preset": "metadata_only",
        },
    )

    assert response.status_code == 422
    assert response.json()["code"] == "invalid_bilibili_url"
