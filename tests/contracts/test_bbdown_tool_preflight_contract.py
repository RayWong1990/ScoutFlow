from __future__ import annotations

import os
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
API_ROOT = ROOT / "services" / "api"
if str(API_ROOT) not in sys.path:
    sys.path.insert(0, str(API_ROOT))


def _touch(path: Path, mode: int) -> Path:
    path.write_text("#!/bin/sh\n", encoding="utf-8")
    path.chmod(mode)
    return path


def test_path_lookup_executable_not_found_without_runner_call() -> None:
    from scoutflow_api.external_tools.bbdown_preflight import ToolPreflightResult, preflight_bbdown_tool

    calls: list[object] = []

    def fake_runner(command: list[str], *, timeout_seconds: float):  # pragma: no cover - must not be called
        calls.append(command)
        raise AssertionError("runner should not be called when discovery fails")

    result = preflight_bbdown_tool(path_env=os.devnull, runner=fake_runner)

    assert result.result is ToolPreflightResult.executable_not_found
    assert result.version is None
    assert calls == []


def test_explicit_path_not_found_does_not_echo_local_path(tmp_path: Path) -> None:
    from scoutflow_api.external_tools.bbdown_preflight import ToolPreflightResult, preflight_bbdown_tool

    missing_path = tmp_path / "missing" / "BBDown"

    result = preflight_bbdown_tool(configured_executable=missing_path)

    assert result.result is ToolPreflightResult.executable_not_found
    assert str(missing_path) not in result.safe_diagnostic
    assert result.safe_stdout_excerpt == ""
    assert result.safe_stderr_excerpt == ""


def test_explicit_path_not_executable(tmp_path: Path) -> None:
    from scoutflow_api.external_tools.bbdown_preflight import ToolPreflightResult, preflight_bbdown_tool

    executable_path = _touch(tmp_path / "BBDown", 0o644)

    result = preflight_bbdown_tool(configured_executable=executable_path)

    assert result.result is ToolPreflightResult.not_executable
    assert result.version is None


def test_version_success_parses_version_and_uses_command_array(tmp_path: Path) -> None:
    from scoutflow_api.external_tools.bbdown_preflight import (
        ToolPreflightResult,
        ToolVersionProcessResult,
        preflight_bbdown_tool,
    )

    executable_path = _touch(tmp_path / "BBDown", 0o755)
    seen_commands: list[object] = []

    def fake_runner(command: list[str], *, timeout_seconds: float) -> ToolVersionProcessResult:
        seen_commands.append(command)
        assert command == [str(executable_path), "--version"]
        assert not isinstance(command, str)
        assert timeout_seconds == 5.0
        return ToolVersionProcessResult(returncode=0, stdout="BBDown version 1.6.3\n", stderr="")

    result = preflight_bbdown_tool(configured_executable=executable_path, runner=fake_runner)

    assert result.result is ToolPreflightResult.executable_found
    assert result.version == "1.6.3"
    assert result.safe_stdout_excerpt == "BBDown version 1.6.3"
    assert seen_commands == [[str(executable_path), "--version"]]


def test_version_timeout_returns_safe_excerpts(tmp_path: Path) -> None:
    from scoutflow_api.external_tools.bbdown_preflight import (
        LOCAL_PATH_PLACEHOLDER,
        ToolPreflightResult,
        ToolVersionTimeoutError,
        preflight_bbdown_tool,
    )

    executable_path = _touch(tmp_path / "BBDown", 0o755)
    cookie_header = "Co" + "okie"
    sess_key = "SESS" + "DATA"
    secret_stdout = f"{cookie_header}: {sess_key}=secret-value\n"
    local_path_stderr = f"stuck at {tmp_path}/debug.log"

    def fake_runner(command: list[str], *, timeout_seconds: float):
        raise ToolVersionTimeoutError(stdout=secret_stdout, stderr=local_path_stderr)

    result = preflight_bbdown_tool(configured_executable=executable_path, runner=fake_runner)

    assert result.result is ToolPreflightResult.version_timeout
    assert "secret-value" not in result.safe_stdout_excerpt
    assert f"{cookie_header}: [REDACTED]" in result.safe_stdout_excerpt
    assert str(tmp_path) not in result.safe_stderr_excerpt
    assert LOCAL_PATH_PLACEHOLDER in result.safe_stderr_excerpt


def test_version_parse_failure_after_successful_exit(tmp_path: Path) -> None:
    from scoutflow_api.external_tools.bbdown_preflight import (
        ToolPreflightResult,
        ToolVersionProcessResult,
        preflight_bbdown_tool,
    )

    executable_path = _touch(tmp_path / "BBDown", 0o755)

    def fake_runner(command: list[str], *, timeout_seconds: float) -> ToolVersionProcessResult:
        return ToolVersionProcessResult(returncode=0, stdout="BBDown development build\n", stderr="")

    result = preflight_bbdown_tool(configured_executable=executable_path, runner=fake_runner)

    assert result.result is ToolPreflightResult.version_parse_failed
    assert result.version is None
    assert result.safe_stdout_excerpt == "BBDown development build"


def test_version_help_fallback_parses_version_when_dashdash_version_requires_root_url(tmp_path: Path) -> None:
    from scoutflow_api.external_tools.bbdown_preflight import (
        ToolPreflightResult,
        ToolVersionProcessResult,
        preflight_bbdown_tool,
    )

    executable_path = _touch(tmp_path / "BBDown", 0o755)
    seen_commands: list[object] = []

    def fake_runner(command: list[str], *, timeout_seconds: float) -> ToolVersionProcessResult:
        seen_commands.append(command)
        if command == [str(executable_path), "--version"]:
            return ToolVersionProcessResult(
                returncode=1,
                stdout="",
                stderr="Required argument missing for command: 'BBDown'.\n请使用 BBDown --help 查看帮助\n",
            )
        assert command == [str(executable_path), "--help"]
        assert timeout_seconds == 5.0
        return ToolVersionProcessResult(
            returncode=0,
            stdout="BBDown version 1.6.3, Bilibili Downloader.\nUsage:\n  BBDown <url> [command] [options]\n",
            stderr="",
        )

    result = preflight_bbdown_tool(configured_executable=executable_path, runner=fake_runner)

    assert result.result is ToolPreflightResult.executable_found
    assert result.version == "1.6.3"
    assert result.safe_stdout_excerpt.startswith("BBDown version 1.6.3")
    assert result.safe_diagnostic == "BBDown executable found and version parsed."
    assert seen_commands == [
        [str(executable_path), "--version"],
        [str(executable_path), "--help"],
    ]


def test_version_help_fallback_not_used_for_unrelated_nonzero_exit(tmp_path: Path) -> None:
    from scoutflow_api.external_tools.bbdown_preflight import (
        ToolPreflightResult,
        ToolVersionProcessResult,
        preflight_bbdown_tool,
    )

    executable_path = _touch(tmp_path / "BBDown", 0o755)
    seen_commands: list[object] = []

    def fake_runner(command: list[str], *, timeout_seconds: float) -> ToolVersionProcessResult:
        seen_commands.append(command)
        return ToolVersionProcessResult(returncode=2, stdout="", stderr="fatal error")

    result = preflight_bbdown_tool(configured_executable=executable_path, runner=fake_runner)

    assert result.result is ToolPreflightResult.subprocess_error
    assert result.safe_stderr_excerpt == "fatal error"
    assert seen_commands == [[str(executable_path), "--version"]]


def test_subprocess_error_redacts_safe_output_without_raw_fields(tmp_path: Path) -> None:
    from scoutflow_api.external_tools.bbdown_preflight import (
        ToolPreflightCheck,
        ToolPreflightResult,
        ToolVersionProcessResult,
        preflight_bbdown_tool,
    )

    executable_path = _touch(tmp_path / "BBDown", 0o755)
    auth_header = "Authori" + "zation"

    def fake_runner(command: list[str], *, timeout_seconds: float) -> ToolVersionProcessResult:
        return ToolVersionProcessResult(
            returncode=2,
            stdout="",
            stderr=f"{auth_header}: bearer-secret\nfailed",
        )

    result = preflight_bbdown_tool(configured_executable=executable_path, runner=fake_runner)

    assert isinstance(result, ToolPreflightCheck)
    assert result.result is ToolPreflightResult.subprocess_error
    assert "bearer-secret" not in result.safe_stderr_excerpt
    assert f"{auth_header}: [REDACTED]" in result.safe_stderr_excerpt
    assert "raw_stdout" not in result.__dict__
    assert "raw_stderr" not in result.__dict__
    assert set(result.__dict__) == {
        "tool_name",
        "result",
        "safe_diagnostic",
        "version",
        "safe_stdout_excerpt",
        "safe_stderr_excerpt",
    }


def test_tool_preflight_result_is_not_platform_result() -> None:
    from scoutflow_api.external_tools.bbdown_preflight import ToolPreflightResult, preflight_bbdown_tool
    from scoutflow_api.platform_result import PlatformResult

    result = preflight_bbdown_tool(path_env=os.devnull)

    assert result.result is ToolPreflightResult.executable_not_found
    assert not isinstance(result.result, PlatformResult)
    assert "executable_not_found" not in {item.value for item in PlatformResult}


def test_default_subprocess_runner_uses_array_without_shell(monkeypatch) -> None:
    import subprocess

    from scoutflow_api.external_tools import bbdown_preflight

    def fake_run(args, **kwargs):
        assert args == ["/tmp/BBDown", "--version"]
        assert isinstance(args, list)
        assert kwargs["shell"] is False
        assert kwargs["capture_output"] is True
        assert kwargs["check"] is False
        assert kwargs["text"] is True
        assert kwargs["timeout"] == 1.0
        return subprocess.CompletedProcess(args=args, returncode=0, stdout="BBDown version 1.6.3", stderr="")

    monkeypatch.setattr(bbdown_preflight.subprocess, "run", fake_run)

    result = bbdown_preflight.run_tool_version_subprocess(["/tmp/BBDown", "--version"], timeout_seconds=1.0)

    assert result.returncode == 0
    assert result.stdout == "BBDown version 1.6.3"
