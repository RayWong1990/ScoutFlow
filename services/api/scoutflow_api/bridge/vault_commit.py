from __future__ import annotations

from fastapi import Request
from fastapi.responses import JSONResponse

from scoutflow_api.bridge.schemas import (
    BridgeError,
    BridgeErrorCode,
    BridgeVaultCommitResponse,
    BridgeVaultPreviewResponse,
)
from scoutflow_api.bridge.vault_preview import build_bridge_vault_preview
from scoutflow_api.vault.commit import build_commit_candidate_from_preview


def build_bridge_vault_commit_dry_run(capture_id: str, request: Request) -> BridgeVaultCommitResponse | JSONResponse:
    preview = build_bridge_vault_preview(capture_id, request)
    if isinstance(preview, JSONResponse):
        return preview

    preview_response = preview if isinstance(preview, BridgeVaultPreviewResponse) else None
    if preview_response is None:
        raise TypeError("build_bridge_vault_preview must return BridgeVaultPreviewResponse or JSONResponse")

    storage = request.app.state.storage
    with storage._connect() as conn:  # noqa: SLF001 - existing storage seam reused for dry-run contract readback
        capture = conn.execute(
            """
            SELECT capture_id, platform_item_id, canonical_url, created_at, source_kind, capture_mode
            FROM captures
            WHERE capture_id = ?
            """,
            (capture_id,),
        ).fetchone()

    if capture is None:
        return JSONResponse(
            status_code=404,
            content={"code": BridgeErrorCode.capture_not_found.value, "message": "Capture does not exist."},
        )

    return BridgeVaultCommitResponse(
        capture_id=capture_id,
        committed=False,
        dry_run=True,
        write_enabled=False,
        target_path=preview_response.target_path,
        candidate=build_commit_candidate_from_preview(preview_response, capture),
        error=BridgeError(
            code=BridgeErrorCode.write_disabled,
            message="Bridge write path is not approved in the current phase.",
        ),
    )
