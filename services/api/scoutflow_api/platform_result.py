from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, ConfigDict


class PlatformResult(StrEnum):
    ok = "ok"
    auth_required = "auth_required"
    rate_limited = "rate_limited"
    forbidden = "forbidden"
    not_found = "not_found"
    region_blocked = "region_blocked"
    vip_required = "vip_required"
    parser_drift = "parser_drift"
    network_error = "network_error"
    timeout = "timeout"
    unavailable = "unavailable"
    unknown_error = "unknown_error"


class PlatformResultModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    platform_result: PlatformResult
