from __future__ import annotations

import json
import re
import sqlite3
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from datetime import UTC, datetime
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


def create_capture(client: TestClient, canonical_url: str = "https://www.bilibili.com/video/BV1AB411c7mD") -> dict[str, str]:
    response = client.post(
        "/captures/discover",
        json={
            "platform": "bilibili",
            "canonical_url": canonical_url,
            "source_kind": "manual_url",
            "quick_capture_preset": "metadata_only",
        },
    )
    assert response.status_code == 201
    return response.json()


def enqueue_metadata_fetch(client: TestClient, capture_id: str):
    return client.post(f"/captures/{capture_id}/metadata-fetch/jobs")


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


def test_metadata_fetch_enqueue_creates_queued_job_without_side_effects(tmp_path: Path) -> None:
    client, db_path, _ = build_client(tmp_path)
    capture = create_capture(client)

    response = enqueue_metadata_fetch(client, capture["capture_id"])

    assert response.status_code == 200
    body = response.json()
    assert re.fullmatch(r"job_[0-9A-HJKMNP-TV-Z]{26}", body["job_id"])
    assert body == {
        "job_id": body["job_id"],
        "capture_id": capture["capture_id"],
        "job_type": "metadata_fetch",
        "status": "queued",
        "dedupe_key": "bilibili:BV1AB411c7mD:metadata_fetch",
    }

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        job = conn.execute(
            """
            SELECT job_id, capture_id, job_type, status, dedupe_key, queued_at, started_at, completed_at, platform_result
            FROM jobs
            WHERE capture_id = ?
            """,
            (capture["capture_id"],),
        ).fetchone()
        assert job is not None
        assert job["job_id"] == body["job_id"]
        assert job["status"] == "queued"
        assert job["dedupe_key"] == "bilibili:BV1AB411c7mD:metadata_fetch"
        assert job["queued_at"]
        assert job["started_at"] is None
        assert job["completed_at"] is None
        assert job["platform_result"] is None

        capture_status = conn.execute(
            "SELECT status FROM captures WHERE capture_id = ?",
            (capture["capture_id"],),
        ).fetchone()[0]
        assert capture_status == "discovered"

        artifact_rows = conn.execute(
            """
            SELECT artifact_kind
            FROM artifact_assets
            WHERE capture_id = ?
            """,
            (capture["capture_id"],),
        ).fetchall()
        assert [row[0] for row in artifact_rows] == ["capture_manifest"]

        event_count = conn.execute(
            "SELECT COUNT(*) FROM job_events WHERE job_id = ?",
            (body["job_id"],),
        ).fetchone()[0]
        assert event_count == 0


def test_metadata_fetch_enqueue_is_idempotent_for_same_capture(tmp_path: Path) -> None:
    client, db_path, _ = build_client(tmp_path)
    capture = create_capture(client)

    first = enqueue_metadata_fetch(client, capture["capture_id"])
    second = enqueue_metadata_fetch(client, capture["capture_id"])

    assert first.status_code == 200
    assert second.status_code == 200
    assert second.json() == first.json()

    with sqlite3.connect(db_path) as conn:
        job_count = conn.execute(
            """
            SELECT COUNT(*)
            FROM jobs
            WHERE capture_id = ? AND job_type = ? AND dedupe_key = ?
            """,
            (capture["capture_id"], "metadata_fetch", "bilibili:BV1AB411c7mD:metadata_fetch"),
        ).fetchone()[0]
        assert job_count == 1


def test_metadata_fetch_enqueue_replays_existing_completed_job(tmp_path: Path) -> None:
    client, db_path, _ = build_client(tmp_path)
    capture = create_capture(client)
    first = enqueue_metadata_fetch(client, capture["capture_id"])
    assert first.status_code == 200
    first_body = first.json()

    with sqlite3.connect(db_path) as conn:
        conn.execute(
            """
            UPDATE jobs
            SET status = ?, completed_at = ?, platform_result = ?
            WHERE job_id = ?
            """,
            ("succeeded", datetime.now(UTC).isoformat(), "ok", first_body["job_id"]),
        )
        conn.execute(
            "UPDATE captures SET status = ? WHERE capture_id = ?",
            ("metadata_fetched", capture["capture_id"]),
        )
        conn.commit()

    second = enqueue_metadata_fetch(client, capture["capture_id"])

    assert second.status_code == 200
    assert second.json() == {
        **first_body,
        "status": "succeeded",
    }

    with sqlite3.connect(db_path) as conn:
        job_count = conn.execute(
            "SELECT COUNT(*) FROM jobs WHERE capture_id = ?",
            (capture["capture_id"],),
        ).fetchone()[0]
        assert job_count == 1


def test_metadata_fetch_enqueue_is_safe_under_parallel_duplicate_posts(tmp_path: Path) -> None:
    from scoutflow_api.main import create_app

    runtime_root = tmp_path / "runtime"
    db_path = runtime_root / "data" / "db" / "scoutflow.sqlite"
    artifacts_root = runtime_root / "data" / "artifacts"
    app = create_app(db_path=db_path, artifacts_root=artifacts_root)

    with TestClient(app) as client:
        capture = create_capture(client)

    barrier = threading.Barrier(4)

    def post_job() -> tuple[int, dict[str, object]]:
        with TestClient(app) as client:
            barrier.wait()
            response = enqueue_metadata_fetch(client, capture["capture_id"])
            return response.status_code, response.json()

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(post_job) for _ in range(4)]
        results = [future.result(timeout=10) for future in futures]

    status_codes = [status_code for status_code, _ in results]
    bodies = [body for _, body in results]
    assert status_codes == [200, 200, 200, 200]
    assert len({body["job_id"] for body in bodies}) == 1
    assert len({body["dedupe_key"] for body in bodies}) == 1

    with sqlite3.connect(db_path) as conn:
        job_count = conn.execute(
            """
            SELECT COUNT(*)
            FROM jobs
            WHERE capture_id = ? AND job_type = ? AND dedupe_key = ?
            """,
            (capture["capture_id"], "metadata_fetch", "bilibili:BV1AB411c7mD:metadata_fetch"),
        ).fetchone()[0]
        assert job_count == 1


def test_metadata_fetch_enqueue_rejects_non_manual_capture(tmp_path: Path) -> None:
    client, db_path, _ = build_client(tmp_path)
    capture = create_capture(client)
    with sqlite3.connect(db_path) as conn:
        conn.execute(
            "UPDATE captures SET source_kind = ? WHERE capture_id = ?",
            ("recommendation", capture["capture_id"]),
        )
        conn.commit()

    response = enqueue_metadata_fetch(client, capture["capture_id"])

    assert response.status_code == 409
    assert response.json()["code"] == "metadata_fetch_source_kind_not_allowed"


def test_metadata_fetch_enqueue_keeps_audio_transcript_blocked(tmp_path: Path) -> None:
    client, db_path, _ = build_client(tmp_path)
    capture = create_capture(client)
    with sqlite3.connect(db_path) as conn:
        conn.execute(
            "UPDATE captures SET capture_mode = ? WHERE capture_id = ?",
            ("audio_transcript", capture["capture_id"]),
        )
        conn.commit()

    response = enqueue_metadata_fetch(client, capture["capture_id"])

    assert response.status_code == 409
    assert response.json()["code"] == "metadata_fetch_capture_mode_not_allowed"


def test_metadata_fetch_enqueue_rejects_raw_seeded_capture_without_discover_provenance(tmp_path: Path) -> None:
    client, db_path, _ = build_client(tmp_path)
    capture_id = "raw-seeded-capture"
    with sqlite3.connect(db_path) as conn:
        artifact_root_path = f"data/artifacts/bilibili/{capture_id}"
        conn.execute(
            """
            INSERT INTO captures (
                capture_id, platform, platform_item_id, canonical_url, source_kind,
                capture_mode, created_by_path, status, artifact_root_path,
                manifest_path, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                capture_id,
                "bilibili",
                "BV1AB411c7mD",
                "https://www.bilibili.com/video/BV1AB411c7mD",
                "manual_url",
                "metadata_only",
                "manual_seed",
                "discovered",
                artifact_root_path,
                f"{artifact_root_path}/bundle/capture-manifest.json",
                datetime.now(UTC).isoformat(),
            ),
        )
        conn.commit()

    response = enqueue_metadata_fetch(client, capture_id)

    assert response.status_code == 409
    assert response.json()["code"] == "capture_not_from_discover"
    with sqlite3.connect(db_path) as conn:
        job_count = conn.execute(
            "SELECT COUNT(*) FROM jobs WHERE capture_id = ?",
            (capture_id,),
        ).fetchone()[0]
        assert job_count == 0
