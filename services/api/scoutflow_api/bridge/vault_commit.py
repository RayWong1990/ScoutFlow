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


def build_bridge_vault_commit_dry_run(capture_id: str, request: Request) -> BridgeVaultCommitResponse | JSONResponse:
    preview = build_bridge_vault_preview(capture_id, request)
    if isinstance(preview, JSONResponse):
        return preview

    preview_response = preview if isinstance(preview, BridgeVaultPreviewResponse) else None
    if preview_response is None:
        raise TypeError("build_bridge_vault_preview must return BridgeVaultPreviewResponse or JSONResponse")

    return BridgeVaultCommitResponse(
        capture_id=capture_id,
        committed=False,
        dry_run=True,
        write_enabled=False,
        target_path=preview_response.target_path,
        error=BridgeError(
            code=BridgeErrorCode.write_disabled,
            message="Bridge write path is not approved in the current phase.",
        ),
    )
