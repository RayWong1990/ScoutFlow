from __future__ import annotations

from dataclasses import dataclass
import re
from urllib.parse import urlsplit

from scoutflow_api.platform_result import PlatformResult
from scoutflow_api.redaction import redact_sensitive_text


SIGNED_MEDIA_URL_PLACEHOLDER = "[REDACTED_SIGNED_MEDIA_URL]"
TEMPORARY_MEDIA_URL_PLACEHOLDER = "[REDACTED_TEMPORARY_MEDIA_URL]"
SAFE_STDOUT_EXCERPT_CHARS = 2000

_URL_RE = re.compile(r"https?://[^\s<>'\"]+")
_MEDIA_URL_EXTENSIONS = (".m4s", ".mp4", ".flv", ".m3u8", ".mp3", ".aac", ".wav", ".webm", ".mov")
_INTEGER_RE = re.compile(r"(\d+)")
_FIELD_RES = {
    "platform_item_id": re.compile(
        r"^\s*(?:Platform Item ID|Item ID|BV|AID|AV|EP|SS|视频ID)\s*[:：]\s*(?P<value>[A-Za-z0-9_-]+)\s*$",
        re.IGNORECASE | re.MULTILINE,
    ),
    "title": re.compile(r"^\s*(?:Title|标题)\s*[:：]\s*(?P<value>.+?)\s*$", re.IGNORECASE | re.MULTILINE),
    "duration": re.compile(
        r"^\s*(?:Duration|Total Duration|时长)\s*[:：]\s*(?P<value>.+?)\s*$",
        re.IGNORECASE | re.MULTILINE,
    ),
    "page_count": re.compile(
        r"^\s*(?:Page Count|Pages|分P数量|分P)\s*[:：]\s*(?P<value>\d+)\s*$",
        re.IGNORECASE | re.MULTILINE,
    ),
    "selected_page": re.compile(
        r"^\s*(?:Selected Page|Page Selected|当前分P)\s*[:：]\s*(?P<value>.+?)\s*$",
        re.IGNORECASE | re.MULTILINE,
    ),
    "uploader_name": re.compile(
        r"^\s*(?:Uploader|UP|UP主|Author)\s*[:：]\s*(?P<value>.+?)\s*$",
        re.IGNORECASE | re.MULTILINE,
    ),
    "estimated_media_bytes": re.compile(
        r"^\s*(?:Estimated Media Bytes|Media Bytes|Estimated Size|估算媒体大小)\s*[:：]\s*(?P<value>.+?)\s*$",
        re.IGNORECASE | re.MULTILINE,
    ),
}

_RESULT_PATTERNS: tuple[tuple[PlatformResult, tuple[re.Pattern[str], ...]], ...] = (
    (
        PlatformResult.auth_required,
        (
            re.compile(r"\b(login required|not logged in|auth required|credential required)\b", re.IGNORECASE),
            re.compile(r"(需要登录|未登录|登录态失效|凭据缺失|账号登录)"),
        ),
    ),
    (
        PlatformResult.rate_limited,
        (
            re.compile(r"\b(rate limit|too many requests|cooldown|anti-abuse|risk control)\b", re.IGNORECASE),
            re.compile(r"(风控|限流|冷却|请求过于频繁)"),
        ),
    ),
    (
        PlatformResult.forbidden,
        (
            re.compile(r"\b(403|forbidden|access denied|permission denied)\b", re.IGNORECASE),
            re.compile(r"(拒绝访问|无权访问)"),
        ),
    ),
    (
        PlatformResult.not_found,
        (
            re.compile(r"\b(not found|invalid id|invalid page|deleted|missing item)\b", re.IGNORECASE),
            re.compile(r"(不存在|已删除|无效链接|无效分P)"),
        ),
    ),
    (
        PlatformResult.region_blocked,
        (
            re.compile(r"\b(region blocked|area restriction|not available in your region|intl limitation)\b", re.IGNORECASE),
            re.compile(r"(地区限制|区域限制|当前地区不可用)"),
        ),
    ),
    (
        PlatformResult.vip_required,
        (
            re.compile(r"\b(vip required|paid content|premium only|member only|course permission)\b", re.IGNORECASE),
            re.compile(r"(大会员|付费|课程权限|会员专享)"),
        ),
    ),
    (
        PlatformResult.network_error,
        (
            re.compile(r"\b(dns|tls|connection reset|connect reset|network error|proxy error)\b", re.IGNORECASE),
        ),
    ),
    (
        PlatformResult.timeout,
        (
            re.compile(r"\b(timeout|timed out)\b", re.IGNORECASE),
        ),
    ),
    (
        PlatformResult.unavailable,
        (
            re.compile(r"\b(service unavailable|upstream unavailable|http 5\d\d|server error)\b", re.IGNORECASE),
        ),
    ),
    (
        PlatformResult.parser_drift,
        (
            re.compile(r"\b(parser drift|layout drift|parse exception|cannot parse|new bv shape)\b", re.IGNORECASE),
            re.compile(r"(解析结构变化|解析失败|输出结构变化)"),
        ),
    ),
    (
        PlatformResult.unknown_error,
        (
            re.compile(r"\b(unknown error|unhandled exception|fatal error|tool exited)\b", re.IGNORECASE),
            re.compile(r"(未知错误|未处理异常)"),
        ),
    ),
)


@dataclass(frozen=True)
class BBDownInfoParseResult:
    platform_item_id: str | None
    title: str | None
    duration_seconds: int | None
    page_count: int | None
    selected_page: str | None
    uploader_name: str | None
    estimated_media_bytes: int | None
    platform_result: PlatformResult
    safe_stdout_excerpt: str
    redaction_applied: bool


def parse_bbdown_info_output(stdout_text: str) -> BBDownInfoParseResult:
    """Parse BBDown -info stdout after mandatory credential/media URL redaction."""

    redacted_text = redact_sensitive_text(stdout_text)
    safe_text = _collapse_media_urls(redacted_text)
    platform_result = classify_bbdown_info_output(safe_text)

    platform_item_id = _extract_field("platform_item_id", safe_text)
    title = _extract_field("title", safe_text)
    duration_seconds = _parse_duration_seconds(_extract_field("duration", safe_text))
    page_count = _parse_int(_extract_field("page_count", safe_text))
    selected_page = _extract_field("selected_page", safe_text)
    uploader_name = _extract_field("uploader_name", safe_text)
    estimated_media_bytes = _parse_size_bytes(_extract_field("estimated_media_bytes", safe_text))

    if platform_result == PlatformResult.ok and _missing_required_ok_fields(
        platform_item_id=platform_item_id,
        title=title,
        duration_seconds=duration_seconds,
    ):
        platform_result = PlatformResult.parser_drift

    return BBDownInfoParseResult(
        platform_item_id=platform_item_id,
        title=title,
        duration_seconds=duration_seconds,
        page_count=page_count,
        selected_page=selected_page,
        uploader_name=uploader_name,
        estimated_media_bytes=estimated_media_bytes,
        platform_result=platform_result,
        safe_stdout_excerpt=_safe_excerpt(safe_text),
        redaction_applied=True,
    )


def classify_bbdown_info_output(safe_text: str) -> PlatformResult:
    for result, patterns in _RESULT_PATTERNS:
        if any(pattern.search(safe_text) for pattern in patterns):
            return result
    return PlatformResult.ok


def blocks_quick_capture(result: BBDownInfoParseResult) -> bool:
    return result.platform_result in {
        PlatformResult.auth_required,
        PlatformResult.rate_limited,
        PlatformResult.forbidden,
        PlatformResult.not_found,
        PlatformResult.region_blocked,
        PlatformResult.vip_required,
        PlatformResult.parser_drift,
        PlatformResult.unknown_error,
    }


def _missing_required_ok_fields(
    *,
    platform_item_id: str | None,
    title: str | None,
    duration_seconds: int | None,
) -> bool:
    return not platform_item_id or not title or duration_seconds is None


def _extract_field(field_name: str, text: str) -> str | None:
    match = _FIELD_RES[field_name].search(text)
    if not match:
        return None
    value = match.group("value").strip()
    return value or None


def _parse_int(value: str | None) -> int | None:
    if value is None:
        return None
    match = _INTEGER_RE.search(value.replace(",", ""))
    if not match:
        return None
    return int(match.group(1))


def _parse_duration_seconds(value: str | None) -> int | None:
    if value is None:
        return None
    stripped = value.strip()
    clock_match = re.search(r"\b(?:(\d{1,3}):)?(\d{1,2}):(\d{2})\b", stripped)
    if clock_match:
        hours = int(clock_match.group(1) or 0)
        minutes = int(clock_match.group(2))
        seconds = int(clock_match.group(3))
        return hours * 3600 + minutes * 60 + seconds

    seconds_match = re.search(r"\b(\d+)\s*(?:seconds?|sec|s|秒)\b", stripped, re.IGNORECASE)
    if seconds_match:
        return int(seconds_match.group(1))

    return None


def _parse_size_bytes(value: str | None) -> int | None:
    if value is None:
        return None
    match = re.search(r"(?P<number>\d+(?:[\d,]*\d)?(?:\.\d+)?)\s*(?P<unit>GiB|MiB|KiB|GB|MB|KB|bytes?|B)?", value)
    if not match:
        return None
    number = float(match.group("number").replace(",", ""))
    unit = (match.group("unit") or "B").lower()
    multipliers = {
        "b": 1,
        "byte": 1,
        "bytes": 1,
        "kb": 1000,
        "mb": 1000**2,
        "gb": 1000**3,
        "kib": 1024,
        "mib": 1024**2,
        "gib": 1024**3,
    }
    return int(number * multipliers[unit])


def _safe_excerpt(safe_text: str) -> str:
    excerpt = "\n".join(line.rstrip() for line in safe_text.strip().splitlines())
    if len(excerpt) <= SAFE_STDOUT_EXCERPT_CHARS:
        return excerpt
    return excerpt[: SAFE_STDOUT_EXCERPT_CHARS - 3] + "..."


def _collapse_media_urls(text: str) -> str:
    def replace(match: re.Match[str]) -> str:
        raw_url = match.group(0)
        url, trailing = _split_trailing_punctuation(raw_url)
        try:
            parts = urlsplit(url)
        except ValueError:
            return raw_url
        path = parts.path.lower()
        if not any(path.endswith(extension) for extension in _MEDIA_URL_EXTENSIONS):
            return raw_url
        if parts.query == "REDACTED_QUERY":
            return SIGNED_MEDIA_URL_PLACEHOLDER + trailing
        return TEMPORARY_MEDIA_URL_PLACEHOLDER + trailing

    return _URL_RE.sub(replace, text)


def _split_trailing_punctuation(url: str) -> tuple[str, str]:
    trailing = ""
    while url and url[-1] in ".,);]":
        trailing = url[-1] + trailing
        url = url[:-1]
    return url, trailing
