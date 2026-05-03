from __future__ import annotations

import hashlib
import json
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


def seed_job(
    db_path: Path,
    capture_id: str,
    *,
    job_id: str = "job-metadata-1",
    job_type: str = "metadata_fetch",
    dedupe_key: str = "bilibili:BV1AB411c7mD:metadata_fetch",
    status: str = "running",
) -> None:
    with sqlite3.connect(db_path) as conn:
        conn.execute(
            """
            INSERT INTO jobs (job_id, capture_id, job_type, status, dedupe_key, queued_at, started_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                job_id,
                capture_id,
                job_type,
                status,
                dedupe_key,
                datetime.now(UTC).isoformat(),
                datetime.now(UTC).isoformat(),
            ),
        )
        conn.commit()


def write_asset(artifacts_root: Path, capture_id: str, relative_path: str, content: bytes) -> tuple[str, int]:
    path = artifacts_root / "bilibili" / capture_id / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)
    return hashlib.sha256(content).hexdigest(), len(content)


def receipt_payload(
    capture_id: str,
    job_id: str,
    sha256: str,
    size: int,
    *,
    zone: str = "bundle",
    artifact_kind: str = "raw_api_response",
    relative_path: str = "bundle/raw-api-response.json",
    platform_result: str = "ok",
    redaction_applied: bool = True,
    redaction_policy: str | None = "credentials-v1",
    sensitive_fields_removed: list[str] | None = None,
) -> dict[str, object]:
    if sensitive_fields_removed is None:
        sensitive_fields_removed = ["headers.cookie", "headers.authorization"]

    return {
        "job_id": job_id,
        "capture_id": capture_id,
        "job_type": "metadata_fetch",
        "producer": "workers.bili",
        "producer_version": "0.1.0",
        "engine": "BBDown",
        "engine_version": "1.6.2",
        "idempotency": {
            "job_attempt": 1,
            "dedupe_key": "bilibili:BV1AB411c7mD:metadata_fetch",
        },
        "platform_result": platform_result,
        "produced_assets": [
            {
                "zone": zone,
                "artifact_kind": artifact_kind,
                "relative_path": relative_path,
                "sha256": sha256,
                "bytes": size,
                "mime_type": "application/json",
                "is_raw_evidence": True,
                "is_derived": False,
                "redaction_applied": redaction_applied,
                "redaction_policy": redaction_policy,
                "sensitive_fields_removed": sensitive_fields_removed,
                "source_url": "https://www.bilibili.com/video/BV1AB411c7mD",
                "created_by_job": job_id,
            }
        ],
        "logs": {
            "job_log_path": "logs/jobs/metadata-fetch.log",
            "stderr_path": None,
        },
        "duration_seconds": 1.25,
        "next_status": "metadata_fetched",
    }


def test_happy_path_receipt_inserts_artifact_row(tmp_path: Path) -> None:
    client, db_path, artifacts_root = build_client(tmp_path)
    capture = create_capture(client)
    job_id = "job-metadata-1"
    seed_job(db_path, capture["capture_id"], job_id=job_id)
    sha256, size = write_asset(
        artifacts_root,
        capture["capture_id"],
        "bundle/raw-api-response.json",
        b'{"title":"safe metadata"}',
    )

    response = client.post(
        f"/jobs/{job_id}/complete",
        json=receipt_payload(capture["capture_id"], job_id, sha256, size),
    )

    assert response.status_code == 200
    assert response.json() == {
        "job_id": job_id,
        "capture_id": capture["capture_id"],
        "job_type": "metadata_fetch",
        "status": "succeeded",
        "platform_result": "ok",
        "artifact_count": 1,
        "idempotent": False,
    }

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        artifact = conn.execute(
            """
            SELECT artifact_zone, artifact_kind, file_path, size_bytes, sha256, metadata_json
            FROM artifact_assets
            WHERE capture_id = ? AND artifact_kind = ?
            """,
            (capture["capture_id"], "raw_api_response"),
        ).fetchone()
        assert artifact is not None
        assert artifact["artifact_zone"] == "bundle"
        assert artifact["file_path"] == f"data/artifacts/bilibili/{capture['capture_id']}/bundle/raw-api-response.json"
        assert artifact["size_bytes"] == size
        assert artifact["sha256"] == sha256
        metadata = json.loads(artifact["metadata_json"])
        assert metadata["redaction_applied"] is True
        assert metadata["redaction_policy"] == "credentials-v1"
        assert metadata["created_by_job"] == job_id
        assert metadata["producer"] == "workers.bili"

        capture_status = conn.execute(
            "SELECT status FROM captures WHERE capture_id = ?",
            (capture["capture_id"],),
        ).fetchone()[0]
        assert capture_status == "metadata_fetched"


def test_path_traversal_rejected(tmp_path: Path) -> None:
    client, db_path, artifacts_root = build_client(tmp_path)
    capture = create_capture(client)
    job_id = "job-metadata-1"
    seed_job(db_path, capture["capture_id"], job_id=job_id)
    sha256, size = write_asset(artifacts_root, capture["capture_id"], "bundle/raw-api-response.json", b"{}")

    payload = receipt_payload(
        capture["capture_id"],
        job_id,
        sha256,
        size,
        relative_path="bundle/../logs/raw-api-response.json",
    )
    response = client.post(f"/jobs/{job_id}/complete", json=payload)

    assert response.status_code == 422


def test_absolute_path_rejected(tmp_path: Path) -> None:
    client, db_path, artifacts_root = build_client(tmp_path)
    capture = create_capture(client)
    job_id = "job-metadata-1"
    seed_job(db_path, capture["capture_id"], job_id=job_id)
    sha256, size = write_asset(artifacts_root, capture["capture_id"], "bundle/raw-api-response.json", b"{}")

    payload = receipt_payload(capture["capture_id"], job_id, sha256, size, relative_path="/bundle/raw-api-response.json")
    response = client.post(f"/jobs/{job_id}/complete", json=payload)

    assert response.status_code == 422


def test_zone_path_mismatch_rejected(tmp_path: Path) -> None:
    client, db_path, artifacts_root = build_client(tmp_path)
    capture = create_capture(client)
    job_id = "job-metadata-1"
    seed_job(db_path, capture["capture_id"], job_id=job_id)
    sha256, size = write_asset(artifacts_root, capture["capture_id"], "bundle/raw-api-response.json", b"{}")

    payload = receipt_payload(capture["capture_id"], job_id, sha256, size, zone="media")
    response = client.post(f"/jobs/{job_id}/complete", json=payload)

    assert response.status_code == 422


def test_missing_redaction_for_raw_api_response_rejected(tmp_path: Path) -> None:
    client, db_path, artifacts_root = build_client(tmp_path)
    capture = create_capture(client)
    job_id = "job-metadata-1"
    seed_job(db_path, capture["capture_id"], job_id=job_id)
    sha256, size = write_asset(artifacts_root, capture["capture_id"], "bundle/raw-api-response.json", b"{}")

    payload = receipt_payload(
        capture["capture_id"],
        job_id,
        sha256,
        size,
        redaction_applied=False,
        redaction_policy=None,
        sensitive_fields_removed=[],
    )
    response = client.post(f"/jobs/{job_id}/complete", json=payload)

    assert response.status_code == 422


def test_unknown_platform_result_rejected(tmp_path: Path) -> None:
    client, db_path, artifacts_root = build_client(tmp_path)
    capture = create_capture(client)
    job_id = "job-metadata-1"
    seed_job(db_path, capture["capture_id"], job_id=job_id)
    sha256, size = write_asset(artifacts_root, capture["capture_id"], "bundle/raw-api-response.json", b"{}")

    payload = receipt_payload(capture["capture_id"], job_id, sha256, size, platform_result="made_up")
    response = client.post(f"/jobs/{job_id}/complete", json=payload)

    assert response.status_code == 422


def test_duplicate_receipt_is_idempotent_without_duplicate_artifact(tmp_path: Path) -> None:
    client, db_path, artifacts_root = build_client(tmp_path)
    capture = create_capture(client)
    job_id = "job-metadata-1"
    seed_job(db_path, capture["capture_id"], job_id=job_id)
    sha256, size = write_asset(artifacts_root, capture["capture_id"], "bundle/raw-api-response.json", b"{}")
    payload = receipt_payload(capture["capture_id"], job_id, sha256, size)

    first = client.post(f"/jobs/{job_id}/complete", json=payload)
    second = client.post(f"/jobs/{job_id}/complete", json=payload)

    assert first.status_code == 200
    assert second.status_code == 200
    assert second.json()["idempotent"] is True

    with sqlite3.connect(db_path) as conn:
        artifact_count = conn.execute(
            """
            SELECT COUNT(*)
            FROM artifact_assets
            WHERE capture_id = ? AND artifact_kind = ?
            """,
            (capture["capture_id"], "raw_api_response"),
        ).fetchone()[0]
        assert artifact_count == 1


def test_sha_mismatch_rejected(tmp_path: Path) -> None:
    client, db_path, artifacts_root = build_client(tmp_path)
    capture = create_capture(client)
    job_id = "job-metadata-1"
    seed_job(db_path, capture["capture_id"], job_id=job_id)
    _, size = write_asset(artifacts_root, capture["capture_id"], "bundle/raw-api-response.json", b"{}")

    payload = receipt_payload(capture["capture_id"], job_id, "0" * 64, size)
    response = client.post(f"/jobs/{job_id}/complete", json=payload)

    assert response.status_code == 422
    assert response.json()["code"] == "artifact_sha256_mismatch"


def test_bytes_mismatch_rejected(tmp_path: Path) -> None:
    client, db_path, artifacts_root = build_client(tmp_path)
    capture = create_capture(client)
    job_id = "job-metadata-1"
    seed_job(db_path, capture["capture_id"], job_id=job_id)
    sha256, size = write_asset(artifacts_root, capture["capture_id"], "bundle/raw-api-response.json", b"{}")

    payload = receipt_payload(capture["capture_id"], job_id, sha256, size + 1)
    response = client.post(f"/jobs/{job_id}/complete", json=payload)

    assert response.status_code == 422
    assert response.json()["code"] == "artifact_bytes_mismatch"


def test_non_existent_capture_rejected(tmp_path: Path) -> None:
    client, _, _ = build_client(tmp_path)
    payload = receipt_payload("missing-capture", "job-metadata-1", "0" * 64, 0)

    response = client.post("/jobs/job-metadata-1/complete", json=payload)

    assert response.status_code == 404
    assert response.json()["code"] == "capture_not_found"


def test_path_job_id_mismatch_rejected(tmp_path: Path) -> None:
    client, db_path, artifacts_root = build_client(tmp_path)
    capture = create_capture(client)
    job_id = "job-metadata-1"
    seed_job(db_path, capture["capture_id"], job_id=job_id)
    sha256, size = write_asset(artifacts_root, capture["capture_id"], "bundle/raw-api-response.json", b"{}")
    payload = receipt_payload(capture["capture_id"], job_id, sha256, size)

    response = client.post("/jobs/different-job/complete", json=payload)

    assert response.status_code == 422
    assert response.json()["code"] == "job_id_mismatch"
