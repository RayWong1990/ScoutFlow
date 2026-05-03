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
    app = create_app(
        db_path=runtime_root / "data" / "db" / "scoutflow.sqlite",
        artifacts_root=runtime_root / "data" / "artifacts",
    )
    return TestClient(app)


def test_recommendation_direct_capture_is_rejected(tmp_path: Path) -> None:
    client = build_client(tmp_path)

    response = client.post(
        "/captures/discover",
        json={
            "platform": "bilibili",
            "canonical_url": "https://www.bilibili.com/video/BV1AB411c7mD",
            "source_kind": "recommendation",
            "quick_capture_preset": "metadata_only",
        },
    )

    assert response.status_code == 422
    assert response.json()["code"] == "lp001_direct_capture_forbidden"


def test_keyword_direct_capture_is_rejected(tmp_path: Path) -> None:
    client = build_client(tmp_path)

    response = client.post(
        "/captures/discover",
        json={
            "platform": "bilibili",
            "canonical_url": "https://www.bilibili.com/video/BV1AB411c7mD",
            "source_kind": "keyword",
            "quick_capture_preset": "metadata_only",
        },
    )

    assert response.status_code == 422
    assert response.json()["code"] == "lp001_direct_capture_forbidden"


def test_raw_gap_direct_capture_is_rejected(tmp_path: Path) -> None:
    client = build_client(tmp_path)

    response = client.post(
        "/captures/discover",
        json={
            "platform": "bilibili",
            "canonical_url": "https://www.bilibili.com/video/BV1AB411c7mD",
            "source_kind": "raw_gap",
            "quick_capture_preset": "metadata_only",
        },
    )

    assert response.status_code == 422
    assert response.json()["code"] == "lp001_direct_capture_forbidden"


def test_capture_plan_is_rejected_in_t_p1a_001(tmp_path: Path) -> None:
    client = build_client(tmp_path)

    response = client.post(
        "/captures/discover",
        json={
            "platform": "bilibili",
            "canonical_url": "https://www.bilibili.com/video/BV1AB411c7mD",
            "source_kind": "capture_plan",
            "quick_capture_preset": "metadata_only",
        },
    )

    assert response.status_code == 422
    assert response.json()["code"] == "source_kind_not_allowed"


def test_xhs_platform_is_rejected(tmp_path: Path) -> None:
    client = build_client(tmp_path)

    response = client.post(
        "/captures/discover",
        json={
            "platform": "xhs",
            "canonical_url": "https://www.xiaohongshu.com/explore/123",
            "source_kind": "manual_url",
            "quick_capture_preset": "metadata_only",
        },
    )

    assert response.status_code == 422
    assert response.json()["code"] == "unsupported_platform"


def test_youtube_platform_is_rejected(tmp_path: Path) -> None:
    client = build_client(tmp_path)

    response = client.post(
        "/captures/discover",
        json={
            "platform": "youtube",
            "canonical_url": "https://www.youtube.com/watch?v=abc123",
            "source_kind": "manual_url",
            "quick_capture_preset": "metadata_only",
        },
    )

    assert response.status_code == 422
    assert response.json()["code"] == "unsupported_platform"
