from __future__ import annotations

import sys
from pathlib import Path

import pytest
from pydantic import ValidationError


ROOT = Path(__file__).resolve().parents[2]
API_ROOT = ROOT / "services" / "api"
if str(API_ROOT) not in sys.path:
    sys.path.insert(0, str(API_ROOT))


def test_platform_result_enum_contains_required_values() -> None:
    from scoutflow_api.platform_result import PlatformResult

    assert {item.value for item in PlatformResult} == {
        "ok",
        "auth_required",
        "rate_limited",
        "forbidden",
        "not_found",
        "region_blocked",
        "vip_required",
        "parser_drift",
        "network_error",
        "timeout",
        "unavailable",
        "unknown_error",
    }


def test_platform_result_model_rejects_unknown_value() -> None:
    from scoutflow_api.platform_result import PlatformResultModel

    with pytest.raises(ValidationError):
        PlatformResultModel(platform_result="made_up")
