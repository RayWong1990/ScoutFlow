from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
API_ROOT = ROOT / "services" / "api"
if str(API_ROOT) not in sys.path:
    sys.path.insert(0, str(API_ROOT))


def test_sensitive_headers_and_tokens_are_redacted() -> None:
    from scoutflow_api.redaction import redact_sensitive_mapping

    payload = {
        "headers": {
            "Cookie": "SESSDATA=abc",
            "Authorization": "Bearer secret",
            "Set-Cookie": "DedeUserID=1",
        },
        "session": {
            "access_token": "token-1",
            "refresh_token": "token-2",
            "bili_jct": "csrf",
        },
        "nested": {
            "DedeUserID": "10001",
            "safe": "keep-me",
        },
    }

    redacted = redact_sensitive_mapping(payload)
    serialized = json.dumps(redacted, sort_keys=True)

    for forbidden in (
        "Cookie",
        "Authorization",
        "Set-Cookie",
        "SESSDATA",
        "bili_jct",
        "DedeUserID",
        "access_token",
        "refresh_token",
    ):
        assert forbidden not in serialized

    assert redacted["nested"]["safe"] == "keep-me"
