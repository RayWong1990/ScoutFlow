from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from enum import StrEnum
import os
from pathlib import Path
import re
import shutil
import subprocess
from typing import Protocol

from scoutflow_api.redaction import redact_sensitive_text


DEFAULT_BBDOWN_EXECUTABLE = "BBDown"
DEFAULT_VERSION_TIMEOUT_SECONDS = 5.0
SAFE_EXCERPT_CHARS = 1000
LOCAL_PATH_PLACEHOLDER = "[REDACTED_LOCAL_PATH]"

_VERSION_RE = re.compile(
    r"(?:\bBBDown\b[\s:/-]*(?:version\s*)?)?v?(?P<version>\d+(?:\.\d+){1,3}(?:[-+][A-Za-z0-9.-]+)?)",
    re.IGNORECASE,
)
_LOCAL_PATH_RE = re.compile(
    r"(?:(?:/Users|/private|/tmp|/var|/Volumes)/[^\s\"'`<>]+|[A-Za-z]:\\Users\\[^\\\s\"'`<>]+(?:\\[^\\\s\"'`<>]+)*)"
)


class ToolPreflightResult(StrEnum):
    executable_found = "executable_found"
    executable_not_found = "executable_not_found"
    not_executable = "not_executable"
    version_timeout = "version_timeout"
    version_parse_failed = "version_parse_failed"
    subprocess_error = "subprocess_error"


@dataclass(frozen=True)
class ToolVersionProcessResult:
    returncode: int
    stdout: str
    stderr: str


@dataclass(frozen=True)
class ToolPreflightCheck:
    tool_name: str
    result: ToolPreflightResult
    safe_diagnostic: str
    version: str | None
    safe_stdout_excerpt: str
    safe_stderr_excerpt: str


class ToolVersionRunner(Protocol):
    def __call__(
        self,
        command: Sequence[str],
        *,
        timeout_seconds: float,
    ) -> ToolVersionProcessResult: ...


class ToolVersionTimeoutError(Exception):
    def __init__(self, *, stdout: str = "", stderr: str = "") -> None:
        super().__init__("tool version command timed out")
        self.stdout = stdout
        self.stderr = stderr


def preflight_bbdown_tool(
    configured_executable: str | os.PathLike[str] | None = None,
    *,
    runner: ToolVersionRunner | None = None,
    timeout_seconds: float = DEFAULT_VERSION_TIMEOUT_SECONDS,
    path_env: str | None = None,
) -> ToolPreflightCheck:
    """Check local BBDown availability without touching platform URLs or media."""

    version_runner = runner or run_tool_version_subprocess
    executable = _resolve_executable(configured_executable=configured_executable, path_env=path_env)
    if executable is None:
        return _check(
            result=ToolPreflightResult.executable_not_found,
            safe_diagnostic="BBDown executable was not found by explicit configuration or PATH lookup.",
        )

    if not executable.exists():
        return _check(
            result=ToolPreflightResult.executable_not_found,
            safe_diagnostic="Configured BBDown executable path does not exist.",
        )

    if not executable.is_file() or not os.access(executable, os.X_OK):
        return _check(
            result=ToolPreflightResult.not_executable,
            safe_diagnostic="Configured BBDown executable is not an executable file.",
        )

    command = [str(executable), "--version"]
    try:
        version_result = version_runner(command, timeout_seconds=timeout_seconds)
    except ToolVersionTimeoutError as exc:
        return _check(
            result=ToolPreflightResult.version_timeout,
            safe_diagnostic="BBDown --version timed out during bounded preflight.",
            safe_stdout_excerpt=_safe_excerpt(exc.stdout),
            safe_stderr_excerpt=_safe_excerpt(exc.stderr),
        )
    except Exception:
        return _check(
            result=ToolPreflightResult.subprocess_error,
            safe_diagnostic="BBDown --version failed before a safe version result could be returned.",
        )

    safe_stdout = _safe_excerpt(version_result.stdout)
    safe_stderr = _safe_excerpt(version_result.stderr)
    if version_result.returncode != 0:
        return _check(
            result=ToolPreflightResult.subprocess_error,
            safe_diagnostic="BBDown --version exited with a non-zero status.",
            safe_stdout_excerpt=safe_stdout,
            safe_stderr_excerpt=safe_stderr,
        )

    version = _parse_version("\n".join([safe_stdout, safe_stderr]))
    if version is None:
        return _check(
            result=ToolPreflightResult.version_parse_failed,
            safe_diagnostic="BBDown executable responded, but version text could not be parsed.",
            safe_stdout_excerpt=safe_stdout,
            safe_stderr_excerpt=safe_stderr,
        )

    return _check(
        result=ToolPreflightResult.executable_found,
        safe_diagnostic="BBDown executable found and version parsed.",
        version=version,
        safe_stdout_excerpt=safe_stdout,
        safe_stderr_excerpt=safe_stderr,
    )


def run_tool_version_subprocess(command: Sequence[str], *, timeout_seconds: float) -> ToolVersionProcessResult:
    completed: subprocess.CompletedProcess[str]
    try:
        completed = subprocess.run(
            list(command),
            capture_output=True,
            check=False,
            shell=False,
            text=True,
            timeout=timeout_seconds,
        )
    except subprocess.TimeoutExpired as exc:
        raise ToolVersionTimeoutError(
            stdout=_decode_stream(exc.stdout),
            stderr=_decode_stream(exc.stderr),
        ) from exc

    return ToolVersionProcessResult(
        returncode=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
    )


def _resolve_executable(
    *,
    configured_executable: str | os.PathLike[str] | None,
    path_env: str | None,
) -> Path | None:
    if configured_executable is not None:
        return Path(configured_executable).expanduser()

    discovered = shutil.which(DEFAULT_BBDOWN_EXECUTABLE, path=path_env)
    if discovered is None:
        return None
    return Path(discovered)


def _parse_version(text: str) -> str | None:
    match = _VERSION_RE.search(text)
    if not match:
        return None
    return match.group("version")


def _safe_excerpt(text: str) -> str:
    redacted = redact_sensitive_text(text)
    redacted = _LOCAL_PATH_RE.sub(LOCAL_PATH_PLACEHOLDER, redacted)
    excerpt = "\n".join(line.rstrip() for line in redacted.strip().splitlines())
    if len(excerpt) <= SAFE_EXCERPT_CHARS:
        return excerpt
    return excerpt[: SAFE_EXCERPT_CHARS - 3] + "..."


def _decode_stream(stream: str | bytes | None) -> str:
    if stream is None:
        return ""
    if isinstance(stream, bytes):
        return stream.decode("utf-8", errors="replace")
    return stream


def _check(
    *,
    result: ToolPreflightResult,
    safe_diagnostic: str,
    version: str | None = None,
    safe_stdout_excerpt: str = "",
    safe_stderr_excerpt: str = "",
) -> ToolPreflightCheck:
    return ToolPreflightCheck(
        tool_name=DEFAULT_BBDOWN_EXECUTABLE,
        result=result,
        safe_diagnostic=safe_diagnostic,
        version=version,
        safe_stdout_excerpt=safe_stdout_excerpt,
        safe_stderr_excerpt=safe_stderr_excerpt,
    )
