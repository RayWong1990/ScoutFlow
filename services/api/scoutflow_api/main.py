from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI

from scoutflow_api.captures import router as captures_router
from scoutflow_api.jobs import router as jobs_router
from scoutflow_api.storage import Storage, StorageConfig


def create_app(db_path: str | Path | None = None, artifacts_root: str | Path | None = None) -> FastAPI:
    resolved_db_path = Path(db_path) if db_path is not None else Path("data/db/scoutflow.sqlite")
    resolved_artifacts_root = Path(artifacts_root) if artifacts_root is not None else Path("data/artifacts")

    app = FastAPI(title="ScoutFlow API", version="0.1.0")
    app.state.storage = Storage(
        StorageConfig(
            db_path=resolved_db_path,
            artifacts_root=resolved_artifacts_root,
        )
    )
    app.include_router(captures_router)
    app.include_router(jobs_router)

    @app.get("/healthz")
    def healthz() -> dict[str, str]:
        return {"status": "ok"}

    return app
