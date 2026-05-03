from __future__ import annotations

from typing import Any


SENSITIVE_KEYS = {
    "cookie",
    "authorization",
    "set-cookie",
    "sessdata",
    "bili_jct",
    "dedeuserid",
    "access_token",
    "refresh_token",
}


def redact_sensitive_mapping(payload: Any) -> Any:
    if isinstance(payload, dict):
        redacted: dict[str, Any] = {}
        for key, value in payload.items():
            if key.lower() in SENSITIVE_KEYS:
                continue
            redacted[key] = redact_sensitive_mapping(value)
        return redacted
    if isinstance(payload, list):
        return [redact_sensitive_mapping(item) for item in payload]
    return payload
