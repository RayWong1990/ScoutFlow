from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI

from scoutflow_api.bridge import router as bridge_router
from scoutflow_api.captures import router as captures_router
from scoutflow_api.jobs import router as jobs_router
from scoutflow_api.storage import Storage, StorageConfig


def create_app(db_path: str | Path | None = None, artifacts_root: str | Path | None = None) -> FastAPI:
    resolved_db_path = Path(db_path) if db_path is not None else Path("data/db/scoutflow.sqlite")
    resolved_artifacts_root = Path(artifacts_root) if artifacts_root is not None else Path("data/artifacts")

    app = FastAPI(
        title="ScoutFlow API",
        version="0.1.0",
        description=(
            "ScoutFlow metadata-only capture API.\n\n"
            "**Authority**: `docs/PRD-v2-2026-05-04.md` / `docs/SRD-v2-2026-05-04.md`.\n\n"
            "**Locked Principles enforced**: "
            "LP-001 (single discover-path entry: only `manual_url` can create captures); "
            "LP-006 (single writer per resource); "
            "LP-007 (lane=3 + writer=1 governance).\n\n"
            "**Boundary**: `metadata_only` is the only supported `quick_capture_preset`. "
            "`audio_transcript` runtime is blocked. "
            "BBDown / yt-dlp / ffmpeg / ASR runtime are not approved by this API surface."
        ),
        openapi_tags=[
            {
                "name": "captures",
                "description": (
                    "Capture lifecycle. LP-001 enforces a single discover-path entry. "
                    "Only `platform=bilibili`, `source_kind=manual_url`, and "
                    "`quick_capture_preset=metadata_only` are supported."
                ),
            },
            {
                "name": "jobs",
                "description": (
                    "Job lifecycle. `metadata_fetch` enqueue is idempotent on "
                    "`(capture_id, job_type, dedupe_key)`. Worker `complete` is "
                    "idempotent on receipt content. The API layer does not execute BBDown."
                ),
            },
            {
                "name": "ops",
                "description": "Operational probes. Process liveness only; no database or storage check.",
            },
        ],
    )
    app.state.storage = Storage(
        StorageConfig(
            db_path=resolved_db_path,
            artifacts_root=resolved_artifacts_root,
        )
    )
    app.include_router(captures_router)
    app.include_router(jobs_router)
    app.include_router(bridge_router)

    @app.get(
        "/healthz",
        tags=["ops"],
        summary="Liveness probe",
        description="Returns ok if the API process is alive. Does not check database or storage.",
    )
    def healthz() -> dict[str, str]:
        return {"status": "ok"}

    return app
