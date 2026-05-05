from __future__ import annotations

import os
from importlib.util import find_spec

from fastapi import Request

from scoutflow_api.bridge.schemas import BridgeError, BridgeErrorCode, BridgeVaultConfigResponse


def _bridge_module_exists(module_name: str) -> bool:
    return find_spec(f"scoutflow_api.bridge.{module_name}") is not None


def build_bridge_vault_config(request: Request) -> BridgeVaultConfigResponse:
    vault_root = os.environ.get("SCOUTFLOW_VAULT_ROOT")
    preview_enabled = bool(vault_root) and _bridge_module_exists("vault_preview")

    if not vault_root:
        return BridgeVaultConfigResponse(
            vault_root_resolved=False,
            vault_root=None,
            preview_enabled=False,
            write_enabled=False,
            frontmatter_mode="raw_4_field",
            error=BridgeError(
                code=BridgeErrorCode.vault_root_unset,
                message="SCOUTFLOW_VAULT_ROOT is not configured.",
            ),
        )

    return BridgeVaultConfigResponse(
        vault_root_resolved=True,
        vault_root=vault_root,
        preview_enabled=preview_enabled,
        write_enabled=False,
        frontmatter_mode="raw_4_field",
        error=None,
    )
