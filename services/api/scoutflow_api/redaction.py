from __future__ import annotations

import re
from typing import Any
from urllib.parse import parse_qsl, urlsplit, urlunsplit


REDACTION_MARKER = "[REDACTED]"
BROWSER_PROFILE_PATH_MARKER = "[REDACTED_BROWSER_PROFILE_PATH]"


SENSITIVE_KEYS = {
    "cookie",
    "authorization",
    "proxy-authorization",
    "set-cookie",
    "x-api-key",
    "sessdata",
    "bili_jct",
    "dedeuserid",
    "access_token",
    "refresh_token",
    "auth_key",
    "token",
    "session_id",
    "csrf",
    "access_key",
    "refresh_key",
}

SENSITIVE_HEADER_RE = re.compile(
    r"\b(Proxy-Authorization|Authorization|X-API-Key|Set-Cookie|Cookie)\s*:\s*([^\r\n]*)",
    re.IGNORECASE,
)
COOKIE_ASSIGNMENT_RE = re.compile(
    r"\b(SESSDATA|bili_jct|DedeUserID)(\s*=\s*)([^&;\s\"'`]+)",
    re.IGNORECASE,
)
TOKEN_ASSIGNMENT_RE = re.compile(
    r"\b(access_token|refresh_token|auth_key|token)(\s*=\s*)([^&;\s\"'`]+)",
    re.IGNORECASE,
)
URL_RE = re.compile(r"https?://[^\s<>'\"]+")
MEDIA_URL_EXTENSIONS = (
    ".m4s",
    ".mp4",
    ".flv",
    ".m3u8",
    ".mp3",
    ".aac",
    ".wav",
    ".webm",
    ".mov",
)
SIGNED_QUERY_KEYS = {
    "sign",
    "signature",
    "sig",
    "expires",
    "expire",
    "deadline",
    "txsecret",
    "wssecret",
    "x-amz-signature",
    "x-signature",
}
BROWSER_PROFILE_PATH_RES = (
    re.compile(
        r"(?:/Users/[^/\s]+|~)/Library/Application Support/"
        r"(?:Google/Chrome|Chromium|BraveSoftware/Brave-Browser|Microsoft Edge|Firefox|Mozilla|Safari)"
        r"(?:/[^ \t\r\n\"']+)*",
        re.IGNORECASE,
    ),
    re.compile(
        r"C:\\Users\\[^\\\s]+\\AppData\\(?:Local|Roaming)\\"
        r"(?:Google\\Chrome|Chromium|BraveSoftware\\Brave-Browser|Microsoft\\Edge|Mozilla\\Firefox)"
        r"(?:\\[^ \t\r\n\"']+)*",
        re.IGNORECASE,
    ),
)


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


def redact_sensitive_text(text: str) -> str:
    """Mask obvious credential-bearing text before stdout/stderr/log persistence."""

    redacted = SENSITIVE_HEADER_RE.sub(_redact_header, text)
    redacted = URL_RE.sub(_redact_signed_url_query, redacted)
    redacted = COOKIE_ASSIGNMENT_RE.sub(_redact_assignment, redacted)
    redacted = TOKEN_ASSIGNMENT_RE.sub(_redact_assignment, redacted)
    for path_re in BROWSER_PROFILE_PATH_RES:
        redacted = path_re.sub(BROWSER_PROFILE_PATH_MARKER, redacted)
    return redacted


def _redact_header(match: re.Match[str]) -> str:
    return f"{match.group(1)}: {REDACTION_MARKER}"


def _redact_assignment(match: re.Match[str]) -> str:
    return f"{match.group(1)}{match.group(2)}{REDACTION_MARKER}"


def _redact_signed_url_query(match: re.Match[str]) -> str:
    raw_url = match.group(0)
    url, trailing = _split_trailing_punctuation(raw_url)

    try:
        parts = urlsplit(url)
    except ValueError:
        return raw_url

    if not parts.query:
        return raw_url

    path = parts.path.lower()
    query_keys = {key.lower() for key, _ in parse_qsl(parts.query, keep_blank_values=True)}
    has_media_extension = any(path.endswith(extension) for extension in MEDIA_URL_EXTENSIONS)
    has_signed_query = bool(query_keys.intersection(SIGNED_QUERY_KEYS))

    if not has_media_extension and not has_signed_query:
        return raw_url

    safe_url = urlunsplit((parts.scheme, parts.netloc, parts.path, "REDACTED_QUERY", parts.fragment))
    return safe_url + trailing


def _split_trailing_punctuation(url: str) -> tuple[str, str]:
    trailing = ""
    while url and url[-1] in ".,);]":
        trailing = url[-1] + trailing
        url = url[:-1]
    return url, trailing
