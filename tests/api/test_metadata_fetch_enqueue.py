from __future__ import annotations

import re
import sqlite3
import sys
from datetime import UTC, datetime
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
