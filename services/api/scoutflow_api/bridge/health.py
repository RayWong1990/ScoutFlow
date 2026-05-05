from __future__ import annotations

import os
from importlib.util import find_spec

from fastapi import Request

from scoutflow_api.bridge.schemas import BridgeErrorCode, BridgeHealthResponse


def _bridge_module_exists(module_name: str) -> bool:
    return find_spec(f"scoutflow_api.bridge.{module_name}") is not None


def build_bridge_health(request: Request) -> BridgeHealthResponse:
    blocked_by = [BridgeErrorCode.write_disabled]

    if not _bridge_module_exists("vault_preview"):
        blocked_by.insert(0, BridgeErrorCode.bridge_not_implemented)

    if not os.environ.get("SCOUTFLOW_VAULT_ROOT"):
        blocked_by.append(BridgeErrorCode.vault_root_unset)

    deduped = list(dict.fromkeys(blocked_by))
    return BridgeHealthResponse(
        bridge_available=True,
        spec_version="v1",
        write_enabled=False,
        blocked_by=deduped,
    )
