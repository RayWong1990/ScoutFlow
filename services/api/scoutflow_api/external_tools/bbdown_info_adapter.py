from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import parse_qsl, urlparse

from scoutflow_api.captures import LP001_REJECTED_SOURCE_KINDS, extract_bilibili_bv_id, is_bilibili_host
from scoutflow_api.external_tools.bbdown_info_parser import BBDownInfoParseResult, parse_bbdown_info_output
from scoutflow_api.platform_result import PlatformResult
from scoutflow_api.redaction import SENSITIVE_KEYS, redact_sensitive_text


DEFAULT_BBDOWN_EXECUTABLE = "BBDown"
SUPPORTED_SCHEMES = {"http", "https"}


class BBDownInfoAdapterInputError(ValueError):
    """Raised when input would cross the current manual_url metadata-only boundary."""


@dataclass(frozen=True)
class BBDownInfoCommand:
    argv: tuple[str, ...]
    work_dir: Path
    platform_item_id: str


@dataclass(frozen=True)
class BBDownInfoRunnerOutput:
    exit_code: int
    stdout_text: str
    stderr_text: str = ""


BBDownInfoRunner = Callable[[BBDownInfoCommand], BBDownInfoRunnerOutput]


@dataclass(frozen=True)
class BBDownInfoProbeResult:
    platform_result: PlatformResult
    platform_item_id: str | None
    title: str | None
    duration_seconds: int | None
    page_count: int | None
    selected_page: str | None
    uploader_name: str | None
    estimated_media_bytes: int | None
    safe_stdout_excerpt: str
    redaction_applied: bool
    tool_exit_code: int


def build_bbdown_info_command(
    *,
    manual_url: str,
    job_temp_dir: Path,
    source_kind: str = "manual_url",
    executable: str = DEFAULT_BBDOWN_EXECUTABLE,
) -> BBDownInfoCommand:
    """Build a BBDown -info command array without invoking the tool."""

    platform_item_id = validate_manual_bilibili_url(manual_url=manual_url, source_kind=source_kind)
    if not executable or any(char.isspace() for char in executable):
        raise BBDownInfoAdapterInputError("BBDown executable must be one command argv element.")

    work_dir = Path(job_temp_dir)
    return BBDownInfoCommand(
        argv=(executable, "-info", "--work-dir", str(work_dir), manual_url),
        work_dir=work_dir,
        platform_item_id=platform_item_id,
    )


def run_bbdown_info_probe(
    *,
    manual_url: str,
    job_temp_dir: Path,
    runner: BBDownInfoRunner,
    source_kind: str = "manual_url",
    executable: str = DEFAULT_BBDOWN_EXECUTABLE,
) -> BBDownInfoProbeResult:
    """Run the injected BBDown -info runner and parse redacted stdout only."""

    command = build_bbdown_info_command(
        manual_url=manual_url,
        job_temp_dir=job_temp_dir,
        source_kind=source_kind,
        executable=executable,
    )
    runner_output = runner(command)
    redacted_stdout = redact_sensitive_text(runner_output.stdout_text)
    parsed = parse_bbdown_info_output(redacted_stdout)
    platform_result = _platform_result_from_runner(parsed=parsed, exit_code=runner_output.exit_code)

    return BBDownInfoProbeResult(
        platform_result=platform_result,
        platform_item_id=parsed.platform_item_id,
        title=parsed.title,
        duration_seconds=parsed.duration_seconds,
        page_count=parsed.page_count,
        selected_page=parsed.selected_page,
        uploader_name=parsed.uploader_name,
        estimated_media_bytes=parsed.estimated_media_bytes,
        safe_stdout_excerpt=parsed.safe_stdout_excerpt,
        redaction_applied=parsed.redaction_applied,
        tool_exit_code=runner_output.exit_code,
    )


def validate_manual_bilibili_url(*, manual_url: str, source_kind: str = "manual_url") -> str:
    if source_kind in LP001_REJECTED_SOURCE_KINDS:
        raise BBDownInfoAdapterInputError("recommendation / keyword / RAW gap cannot directly create capture.")
    if source_kind != "manual_url":
        raise BBDownInfoAdapterInputError("Only source_kind=manual_url is allowed for T-P1A-010B.")

    parsed = urlparse(manual_url)
    if parsed.scheme.lower() not in SUPPORTED_SCHEMES:
        raise BBDownInfoAdapterInputError("manual_url must use http or https.")
    if not is_bilibili_host(parsed):
        raise BBDownInfoAdapterInputError("manual_url must be a bilibili URL.")
    if parsed.username or parsed.password:
        raise BBDownInfoAdapterInputError("manual_url must not contain credential userinfo.")

    query_keys = {key.lower() for key, _ in parse_qsl(parsed.query, keep_blank_values=True)}
    sensitive_query_keys = query_keys.intersection(SENSITIVE_KEYS)
    if sensitive_query_keys:
        raise BBDownInfoAdapterInputError("manual_url must not contain credential query parameters.")

    platform_item_id = extract_bilibili_bv_id(manual_url)
    if platform_item_id is None:
        raise BBDownInfoAdapterInputError("manual_url must contain a Bilibili BV id.")
    return platform_item_id


def _platform_result_from_runner(*, parsed: BBDownInfoParseResult, exit_code: int) -> PlatformResult:
    if exit_code != 0 and parsed.platform_result is PlatformResult.ok:
        return PlatformResult.unknown_error
    return parsed.platform_result
