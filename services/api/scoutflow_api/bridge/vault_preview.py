from __future__ import annotations

import os
import re
from datetime import UTC, datetime
from pathlib import PurePosixPath

from fastapi import Request
from fastapi.responses import JSONResponse

from scoutflow_api.bridge.schemas import (
    BridgeErrorCode,
    BridgeFrontmatter,
    BridgeVaultPreviewResponse,
)
from scoutflow_api.models import ErrorResponse
from scoutflow_api.vault.renderer import build_preview_markdown


SLUG_RE = re.compile(r"[^a-z0-9]+")


def error_response(http_status: int, code: BridgeErrorCode, message: str) -> JSONResponse:
    body = ErrorResponse(code=code.value, message=message).model_dump()
    return JSONResponse(status_code=http_status, content=body)


def _slugify(value: str) -> str:
    lowered = value.lower()
    normalized = SLUG_RE.sub("-", lowered).strip("-")
    return normalized or "capture"


def _load_capture(request: Request, capture_id: str):
    storage = request.app.state.storage
    with storage._connect() as conn:  # noqa: SLF001 - read-only contract probe over existing storage seam
        return conn.execute(
            """
            SELECT capture_id, platform_item_id, canonical_url, source_kind, capture_mode
            FROM captures
            WHERE capture_id = ?
            """,
            (capture_id,),
        ).fetchone()


def build_bridge_vault_preview(capture_id: str, request: Request) -> BridgeVaultPreviewResponse | JSONResponse:
    vault_root = os.environ.get("SCOUTFLOW_VAULT_ROOT")
    if not vault_root:
        return error_response(409, BridgeErrorCode.vault_root_unset, "SCOUTFLOW_VAULT_ROOT is not configured.")

    capture = _load_capture(request, capture_id)
    if capture is None:
        return error_response(404, BridgeErrorCode.capture_not_found, "Capture does not exist.")

    if capture["source_kind"] != "manual_url" or capture["capture_mode"] != "metadata_only":
        return error_response(
            409,
            BridgeErrorCode.capture_state_blocked,
            "Current capture state is not allowed to produce a vault preview.",
        )

    title = f"ScoutFlow {capture['platform_item_id']}"
    frontmatter = BridgeFrontmatter(
        title=title,
        date=datetime.now(UTC).date().isoformat(),
        tags="调研/ScoutFlow采集",
        status="pending",
    )
    slug = _slugify(capture["platform_item_id"])
    target_path = str(PurePosixPath(vault_root, "00-Inbox", f"scoutflow-{capture_id}-{slug}.md"))
    body_markdown = "\n".join(
        build_preview_markdown(
            capture_id,
            capture["platform_item_id"],
            capture["canonical_url"],
            frontmatter=frontmatter,
            source_kind=capture["source_kind"],
            capture_mode=capture["capture_mode"],
        ).splitlines()
    )

    return BridgeVaultPreviewResponse(
        capture_id=capture_id,
        target_path=target_path,
        frontmatter=frontmatter,
        body_markdown=body_markdown,
        warnings=[],
    )
