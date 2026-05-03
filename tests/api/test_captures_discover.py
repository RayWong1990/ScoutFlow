from __future__ import annotations

import json
import re
import sqlite3
import sys
from pathlib import Path

import pytest
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


def test_duplicate_manual_url_is_idempotent_without_orphan_manifest(tmp_path: Path) -> None:
    client, db_path, artifacts_root = build_client(tmp_path)
    payload = {
        "platform": "bilibili",
        "canonical_url": "https://www.bilibili.com/video/BV1AB411c7mD",
        "source_kind": "manual_url",
        "quick_capture_preset": "metadata_only",
    }

    first_response = client.post("/captures/discover", json=payload)
    second_response = client.post("/captures/discover", json=payload)

    assert first_response.status_code == 201
    assert second_response.status_code in {200, 201}
    first_body = first_response.json()
    second_body = second_response.json()
    assert second_body["capture_id"] == first_body["capture_id"]

    with sqlite3.connect(db_path) as conn:
        capture_count = conn.execute(
            """
            SELECT COUNT(*)
            FROM captures
            WHERE platform = ? AND platform_item_id = ?
            """,
            ("bilibili", "BV1AB411c7mD"),
        ).fetchone()[0]
        assert capture_count == 1

        artifact_count = conn.execute(
            """
            SELECT COUNT(*)
            FROM artifact_assets
            WHERE capture_id = ? AND artifact_kind = ?
            """,
            (first_body["capture_id"], "capture_manifest"),
        ).fetchone()[0]
        assert artifact_count == 1

    capture_dirs = list((artifacts_root / "bilibili").glob("*"))
    manifests = list((artifacts_root / "bilibili").glob("*/bundle/capture-manifest.json"))
    assert len(capture_dirs) == 1
    assert len(manifests) == 1


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


@pytest.mark.parametrize(
    "canonical_url",
    (
        "https://bilibili.com.evil.example/video/BV1AB411c7mD",
        "https://evil-bilibili.com/video/BV1AB411c7mD",
        "https://notbilibili.com/video/BV1AB411c7mD",
    ),
)
def test_bilibili_host_spoof_is_rejected(tmp_path: Path, canonical_url: str) -> None:
    client, _, _ = build_client(tmp_path)

    response = client.post(
        "/captures/discover",
        json={
            "platform": "bilibili",
            "canonical_url": canonical_url,
            "source_kind": "manual_url",
            "quick_capture_preset": "metadata_only",
        },
    )

    assert response.status_code == 422
    assert response.json()["code"] == "unsupported_platform"


def test_bilibili_subdomain_is_accepted(tmp_path: Path) -> None:
    client, _, _ = build_client(tmp_path)

    response = client.post(
        "/captures/discover",
        json={
            "platform": "bilibili",
            "canonical_url": "https://m.bilibili.com/video/BV1AB411c7mD",
            "source_kind": "manual_url",
            "quick_capture_preset": "metadata_only",
        },
    )

    assert response.status_code == 201
    assert response.json()["platform_item_id"] == "BV1AB411c7mD"


def test_non_http_scheme_is_rejected(tmp_path: Path) -> None:
    client, _, _ = build_client(tmp_path)

    response = client.post(
        "/captures/discover",
        json={
            "platform": "bilibili",
            "canonical_url": "ftp://www.bilibili.com/video/BV1AB411c7mD",
            "source_kind": "manual_url",
            "quick_capture_preset": "metadata_only",
        },
    )

    assert response.status_code == 422
    assert response.json()["code"] == "invalid_bilibili_url"


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
