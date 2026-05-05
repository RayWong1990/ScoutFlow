from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
API_ROOT = ROOT / "services" / "api"
if str(API_ROOT) not in sys.path:
    sys.path.insert(0, str(API_ROOT))


def test_bridge_error_helper_serializes_bridge_namespace_only() -> None:
    from scoutflow_api.bridge.errors import bridge_error_response
    from scoutflow_api.bridge.schemas import BridgeErrorCode

    response = bridge_error_response(409, BridgeErrorCode.write_disabled, "Bridge write path is not approved.")
    assert response.status_code == 409
    assert json.loads(response.body) == {
        "code": "write_disabled",
        "message": "Bridge write path is not approved.",
    }


def test_bridge_error_codes_do_not_overlap_platform_result() -> None:
    from scoutflow_api.bridge.schemas import BridgeErrorCode
    from scoutflow_api.platform_result import PlatformResult

    bridge_codes = {item.value for item in BridgeErrorCode}
    platform_codes = {item.value for item in PlatformResult}
    assert bridge_codes.isdisjoint(platform_codes)


def test_bridge_route_error_keeps_status_and_message() -> None:
    from scoutflow_api.bridge.errors import BridgeRouteError
    from scoutflow_api.bridge.schemas import BridgeErrorCode

    err = BridgeRouteError(status_code=404, code=BridgeErrorCode.capture_not_found, message="Capture does not exist.")
    assert err.status_code == 404
    assert err.code is BridgeErrorCode.capture_not_found
    assert str(err) == "capture_not_found: Capture does not exist."
