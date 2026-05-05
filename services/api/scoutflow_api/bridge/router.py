from __future__ import annotations

from importlib import import_module
from typing import Any, Callable

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from scoutflow_api.bridge.schemas import (
    BridgeError,
    BridgeErrorCode,
    BridgeHealthResponse,
    BridgeVaultCommitResponse,
    BridgeVaultConfigResponse,
    BridgeVaultPreviewResponse,
)
from scoutflow_api.models import ErrorResponse


router = APIRouter(tags=["bridge"])


def error_response(http_status: int, code: BridgeErrorCode, message: str) -> JSONResponse:
    body = ErrorResponse(code=code.value, message=message).model_dump()
    return JSONResponse(status_code=http_status, content=body)


def _load_handler(module_name: str, attr_name: str) -> Callable[..., Any] | None:
    try:
        module = import_module(f"scoutflow_api.bridge.{module_name}")
    except ModuleNotFoundError:
        return None
    return getattr(module, attr_name, None)


def _default_bridge_health() -> BridgeHealthResponse:
    return BridgeHealthResponse(
        bridge_available=False,
        spec_version="v0",
        write_enabled=False,
        blocked_by=[BridgeErrorCode.bridge_not_implemented],
    )


def _default_bridge_vault_config() -> BridgeVaultConfigResponse:
    return BridgeVaultConfigResponse(
        vault_root_resolved=False,
        vault_root=None,
        preview_enabled=False,
        write_enabled=False,
        frontmatter_mode="raw_4_field",
        error=BridgeError(
            code=BridgeErrorCode.bridge_not_implemented,
            message="Bridge vault config route is scaffolded but not yet implemented.",
        ),
    )


@router.get(
    "/bridge/health",
    response_model=BridgeHealthResponse,
    summary="Bridge feature availability",
    description="Show bridge feature availability without mutating state.",
)
def bridge_health(request: Request) -> BridgeHealthResponse:
    handler = _load_handler("health", "build_bridge_health")
    if handler is None:
        return _default_bridge_health()
    return handler(request)


@router.get(
    "/bridge/vault/config",
    response_model=BridgeVaultConfigResponse,
    summary="Resolved vault config",
    description="Expose resolved vault config and fail-loud state without writing any files.",
)
def bridge_vault_config(request: Request) -> BridgeVaultConfigResponse:
    handler = _load_handler("config", "build_bridge_vault_config")
    if handler is None:
        return _default_bridge_vault_config()
    return handler(request)


@router.get(
    "/captures/{capture_id}/vault-preview",
    response_model=BridgeVaultPreviewResponse,
    responses={
        404: {"model": ErrorResponse},
        409: {"model": ErrorResponse},
        503: {"model": ErrorResponse},
    },
    summary="Render vault preview",
    description="Render a markdown preview for a capture without writing to the vault.",
)
def bridge_vault_preview(capture_id: str, request: Request) -> BridgeVaultPreviewResponse | JSONResponse:
    handler = _load_handler("vault_preview", "build_bridge_vault_preview")
    if handler is None:
        return error_response(
            503,
            BridgeErrorCode.bridge_not_implemented,
            "Bridge vault preview is scaffolded but not yet implemented.",
        )
    return handler(capture_id, request)


@router.post(
    "/captures/{capture_id}/vault-commit",
    response_model=BridgeVaultCommitResponse,
    responses={
        404: {"model": ErrorResponse},
        409: {"model": ErrorResponse},
        503: {"model": ErrorResponse},
    },
    summary="Dry-run vault commit",
    description="Return the gated commit contract without writing to the vault.",
)
def bridge_vault_commit(capture_id: str, request: Request) -> BridgeVaultCommitResponse | JSONResponse:
    handler = _load_handler("vault_commit", "build_bridge_vault_commit_dry_run")
    if handler is None:
        return error_response(
            503,
            BridgeErrorCode.bridge_not_implemented,
            "Bridge vault commit dry-run is scaffolded but not yet implemented.",
        )
    return handler(capture_id, request)
