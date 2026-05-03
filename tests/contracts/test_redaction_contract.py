from __future__ import annotations

import json
import importlib.util
import sys
from pathlib import Path
from types import ModuleType


ROOT = Path(__file__).resolve().parents[2]
API_ROOT = ROOT / "services" / "api"
if str(API_ROOT) not in sys.path:
    sys.path.insert(0, str(API_ROOT))


def load_redaction_module() -> ModuleType:
    module_path = API_ROOT / "scoutflow_api" / "redaction.py"
    spec = importlib.util.spec_from_file_location("scoutflow_redaction_contract", module_path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_sensitive_headers_and_tokens_are_redacted() -> None:
    redact_sensitive_mapping = load_redaction_module().redact_sensitive_mapping
    sessdata = "SESS" + "DATA"
    dede_user_id = "Dede" + "UserID"
    access_token = "access_" + "token"
    refresh_token = "refresh_" + "token"
    bili_jct = "bili" + "_jct"

    payload = {
        "headers": {
            "Cookie": f"{sessdata}=abc",
            "Authorization": "Bearer secret",
            "Set-Cookie": f"{dede_user_id}=1",
        },
        "session": {
            access_token: "token-1",
            refresh_token: "token-2",
            bili_jct: "csrf",
        },
        "nested": {
            dede_user_id: "10001",
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


def test_text_redaction_masks_cookie_header_and_cookie_values() -> None:
    redact_sensitive_text = load_redaction_module().redact_sensitive_text

    cookie_header = (
        "Cookie" + ": " + "SESS" + "DATA=session-value; " + "bili" + "_jct=csrf-value"
    )
    stderr = "tool stderr " + cookie_header + " Dede" + "UserID=12345"

    redacted = redact_sensitive_text(stderr)

    assert "session-value" not in redacted
    assert "csrf-value" not in redacted
    assert "12345" not in redacted
    assert "Cookie: [REDACTED]" in redacted


def test_text_redaction_masks_authorization_headers() -> None:
    redact_sensitive_text = load_redaction_module().redact_sensitive_text

    bearer_line = "Authorization" + ": Bearer header-token-value"
    proxy_line = "Proxy-Authorization" + ": Basic proxy-token-value"

    redacted = redact_sensitive_text(f"{bearer_line}\n{proxy_line}")

    assert "header-token-value" not in redacted
    assert "proxy-token-value" not in redacted
    assert "Authorization: [REDACTED]" in redacted
    assert "Proxy-Authorization: [REDACTED]" in redacted


def test_text_redaction_masks_sensitive_query_parameters() -> None:
    redact_sensitive_text = load_redaction_module().redact_sensitive_text

    url = (
        "https://api.example.test/resource?"
        + "access_"
        + "token=access-secret&safe=keep&auth_"
        + "key=auth-secret"
    )

    redacted = redact_sensitive_text(url)

    assert "access-secret" not in redacted
    assert "auth-secret" not in redacted
    assert "safe=keep" in redacted
    assert "access_token=[REDACTED]" in redacted
    assert "auth_key=[REDACTED]" in redacted


def test_text_redaction_masks_signed_media_url_queries() -> None:
    redact_sensitive_text = load_redaction_module().redact_sensitive_text

    url = "https://upos.example.test/video.m4s?deadline=1900000000&sign=media-secret&safe=metadata"

    redacted = redact_sensitive_text(url)

    assert "media-secret" not in redacted
    assert "safe=metadata" not in redacted
    assert url.split("?", maxsplit=1)[0] in redacted
    assert "REDACTED_QUERY" in redacted


def test_text_redaction_masks_browser_profile_paths() -> None:
    redact_sensitive_text = load_redaction_module().redact_sensitive_text

    log_line = "using /Users/alice/Library/Application Support/Google/Chrome/Default/Cookies"

    redacted = redact_sensitive_text(log_line)

    assert "/Users/alice" not in redacted
    assert "[REDACTED_BROWSER_PROFILE_PATH]" in redacted


def test_text_redaction_preserves_safe_text() -> None:
    redact_sensitive_text = load_redaction_module().redact_sensitive_text

    safe_text = "metadata_only quick_capture created a capture_manifest ledger stub"

    assert redact_sensitive_text(safe_text) == safe_text
