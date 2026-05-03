from __future__ import annotations

import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]
API_ROOT = ROOT / "services" / "api"
FIXTURE_ROOT = ROOT / "tests" / "fixtures" / "bbdown"
if str(API_ROOT) not in sys.path:
    sys.path.insert(0, str(API_ROOT))


SAMPLE_URL = "https://www.bilibili.com/video/BV19D9eB9Etg/?spm_id_from=333.1007.tianma.3-1-7.click"


def read_fixture(name: str) -> str:
    return (FIXTURE_ROOT / name).read_text(encoding="utf-8")


def test_command_builder_returns_argv_array_with_workdir_and_url(tmp_path: Path) -> None:
    from scoutflow_api.external_tools.bbdown_info_adapter import build_bbdown_info_command

    job_temp_dir = tmp_path / "bbdown-info-job"
    command = build_bbdown_info_command(manual_url=SAMPLE_URL, job_temp_dir=job_temp_dir)

    assert command.argv == ("BBDown", "-info", "--work-dir", str(job_temp_dir), SAMPLE_URL)
    assert command.work_dir == job_temp_dir
    assert command.platform_item_id == "BV19D9eB9Etg"


def test_command_builder_keeps_url_as_single_arg_without_shell_interpolation(tmp_path: Path) -> None:
    from scoutflow_api.external_tools.bbdown_info_adapter import build_bbdown_info_command

    command = build_bbdown_info_command(manual_url=SAMPLE_URL, job_temp_dir=tmp_path)

    assert isinstance(command.argv, tuple)
    assert SAMPLE_URL in command.argv
    assert all("\n" not in arg for arg in command.argv)
    assert not any(arg.startswith("sh ") or arg.startswith("bash ") for arg in command.argv)


def test_sample_url_uses_injected_runner_only_and_is_not_executed_live(tmp_path: Path) -> None:
    from scoutflow_api.external_tools.bbdown_info_adapter import (
        BBDownInfoCommand,
        BBDownInfoRunnerOutput,
        run_bbdown_info_probe,
    )
    from scoutflow_api.platform_result import PlatformResult

    seen_commands: list[BBDownInfoCommand] = []

    def fake_runner(command: BBDownInfoCommand) -> BBDownInfoRunnerOutput:
        seen_commands.append(command)
        return BBDownInfoRunnerOutput(exit_code=0, stdout_text=read_fixture("info_public_ok_sanitized.txt"))

    result = run_bbdown_info_probe(manual_url=SAMPLE_URL, job_temp_dir=tmp_path, runner=fake_runner)

    assert len(seen_commands) == 1
    assert seen_commands[0].argv[-1] == SAMPLE_URL
    assert result.platform_result is PlatformResult.ok


def test_fake_success_stdout_parses_to_platform_result_ok(tmp_path: Path) -> None:
    from scoutflow_api.external_tools.bbdown_info_adapter import (
        BBDownInfoCommand,
        BBDownInfoRunnerOutput,
        run_bbdown_info_probe,
    )
    from scoutflow_api.platform_result import PlatformResult

    def fake_runner(_: BBDownInfoCommand) -> BBDownInfoRunnerOutput:
        return BBDownInfoRunnerOutput(exit_code=0, stdout_text=read_fixture("info_public_ok_sanitized.txt"))

    result = run_bbdown_info_probe(manual_url=SAMPLE_URL, job_temp_dir=tmp_path, runner=fake_runner)

    assert result.platform_result is PlatformResult.ok
    assert result.platform_item_id == "BVSCOUTFLOW1"
    assert result.title == "ScoutFlow public fixture title"
    assert result.duration_seconds == 252


@pytest.mark.parametrize(
    ("fixture_name", "expected_result"),
    (
        ("info_auth_required_sanitized.txt", "auth_required"),
        ("info_vip_required_sanitized.txt", "vip_required"),
        ("info_parser_drift_sanitized.txt", "parser_drift"),
    ),
)
def test_fake_failure_stdout_maps_to_existing_platform_result(
    tmp_path: Path,
    fixture_name: str,
    expected_result: str,
) -> None:
    from scoutflow_api.external_tools.bbdown_info_adapter import (
        BBDownInfoCommand,
        BBDownInfoRunnerOutput,
        run_bbdown_info_probe,
    )

    def fake_runner(_: BBDownInfoCommand) -> BBDownInfoRunnerOutput:
        return BBDownInfoRunnerOutput(exit_code=1, stdout_text=read_fixture(fixture_name))

    result = run_bbdown_info_probe(manual_url=SAMPLE_URL, job_temp_dir=tmp_path, runner=fake_runner)

    assert result.platform_result.value == expected_result


def test_qr_auth_wording_maps_to_auth_required_without_auth_workflow(tmp_path: Path) -> None:
    from scoutflow_api.external_tools.bbdown_info_adapter import (
        BBDownInfoCommand,
        BBDownInfoRunnerOutput,
        run_bbdown_info_probe,
    )
    from scoutflow_api.platform_result import PlatformResult

    def fake_runner(_: BBDownInfoCommand) -> BBDownInfoRunnerOutput:
        return BBDownInfoRunnerOutput(
            exit_code=1,
            stdout_text="BBDown -info sanitized fixture\nError: scan QR code to login before continuing.",
        )

    result = run_bbdown_info_probe(manual_url=SAMPLE_URL, job_temp_dir=tmp_path, runner=fake_runner)

    assert result.platform_result is PlatformResult.auth_required
    assert not hasattr(result, "qr_login_url")
    assert not hasattr(result, "auth_workflow")


def test_output_redaction_occurs_before_existing_parser_is_called(monkeypatch, tmp_path: Path) -> None:
    from scoutflow_api.external_tools import bbdown_info_adapter
    from scoutflow_api.external_tools.bbdown_info_parser import BBDownInfoParseResult
    from scoutflow_api.platform_result import PlatformResult

    calls: list[tuple[str, str]] = []

    def fake_redactor(text: str) -> str:
        calls.append(("redact", text))
        return "\n".join(
            [
                "BBDown -info sanitized fixture",
                "Platform Item ID: BVREDACTED1",
                "Title: redacted fixture",
                "Duration: 00:01:00",
            ]
        )

    def fake_parser(text: str) -> BBDownInfoParseResult:
        calls.append(("parse", text))
        assert "Authorization" not in text
        return BBDownInfoParseResult(
            platform_item_id="BVREDACTED1",
            title="redacted fixture",
            duration_seconds=60,
            page_count=None,
            selected_page=None,
            uploader_name=None,
            estimated_media_bytes=None,
            platform_result=PlatformResult.ok,
            safe_stdout_excerpt=text,
            redaction_applied=True,
        )

    monkeypatch.setattr(bbdown_info_adapter, "redact_sensitive_text", fake_redactor)
    monkeypatch.setattr(bbdown_info_adapter, "parse_bbdown_info_output", fake_parser)

    def fake_runner(_: bbdown_info_adapter.BBDownInfoCommand) -> bbdown_info_adapter.BBDownInfoRunnerOutput:
        return bbdown_info_adapter.BBDownInfoRunnerOutput(
            exit_code=0,
            stdout_text="Authorization: [REDACTED]\nTitle: unsafe before redaction",
        )

    result = bbdown_info_adapter.run_bbdown_info_probe(manual_url=SAMPLE_URL, job_temp_dir=tmp_path, runner=fake_runner)

    assert calls[0] == ("redact", "Authorization: [REDACTED]\nTitle: unsafe before redaction")
    assert calls[1][0] == "parse"
    assert result.platform_result is PlatformResult.ok


def test_probe_result_does_not_persist_raw_stdout_or_stderr(tmp_path: Path) -> None:
    from scoutflow_api.external_tools.bbdown_info_adapter import (
        BBDownInfoCommand,
        BBDownInfoRunnerOutput,
        run_bbdown_info_probe,
    )

    def fake_runner(_: BBDownInfoCommand) -> BBDownInfoRunnerOutput:
        return BBDownInfoRunnerOutput(
            exit_code=0,
            stdout_text=read_fixture("info_public_ok_sanitized.txt"),
            stderr_text="diagnostic stderr must not be exposed",
        )

    result = run_bbdown_info_probe(manual_url=SAMPLE_URL, job_temp_dir=tmp_path, runner=fake_runner)

    assert "raw_stdout" not in result.__dict__
    assert "stdout_text" not in result.__dict__
    assert "raw_stderr" not in result.__dict__
    assert "stderr_text" not in result.__dict__
    assert set(result.__dict__) == {
        "platform_result",
        "platform_item_id",
        "title",
        "duration_seconds",
        "page_count",
        "selected_page",
        "uploader_name",
        "estimated_media_bytes",
        "safe_stdout_excerpt",
        "redaction_applied",
        "tool_exit_code",
    }


def test_adapter_result_has_no_artifact_receipt_or_capture_state_advancement(tmp_path: Path) -> None:
    from scoutflow_api.external_tools.bbdown_info_adapter import (
        BBDownInfoCommand,
        BBDownInfoRunnerOutput,
        run_bbdown_info_probe,
    )

    def fake_runner(_: BBDownInfoCommand) -> BBDownInfoRunnerOutput:
        return BBDownInfoRunnerOutput(exit_code=0, stdout_text=read_fixture("info_public_ok_sanitized.txt"))

    result = run_bbdown_info_probe(manual_url=SAMPLE_URL, job_temp_dir=tmp_path, runner=fake_runner)

    forbidden_fields = {
        "artifact_assets",
        "produced_assets",
        "receipt",
        "capture_status",
        "next_status",
        "job_event",
    }
    assert forbidden_fields.isdisjoint(result.__dict__)


@pytest.mark.parametrize("source_kind", ("recommendation", "keyword", "raw_gap", "account"))
def test_adapter_refuses_non_manual_url_source_kind(tmp_path: Path, source_kind: str) -> None:
    from scoutflow_api.external_tools.bbdown_info_adapter import BBDownInfoAdapterInputError, build_bbdown_info_command

    with pytest.raises(BBDownInfoAdapterInputError):
        build_bbdown_info_command(manual_url=SAMPLE_URL, job_temp_dir=tmp_path, source_kind=source_kind)


def test_adapter_refuses_credential_query_material(tmp_path: Path) -> None:
    from scoutflow_api.external_tools.bbdown_info_adapter import BBDownInfoAdapterInputError, build_bbdown_info_command

    unsafe_url = "https://www.bilibili.com/video/BV19D9eB9Etg/?access_token=[REDACTED]"

    with pytest.raises(BBDownInfoAdapterInputError):
        build_bbdown_info_command(manual_url=unsafe_url, job_temp_dir=tmp_path)


def test_tool_availability_values_are_not_platform_results(tmp_path: Path) -> None:
    from scoutflow_api.external_tools.bbdown_info_adapter import (
        BBDownInfoCommand,
        BBDownInfoRunnerOutput,
        run_bbdown_info_probe,
    )
    from scoutflow_api.platform_result import PlatformResult

    def fake_runner(_: BBDownInfoCommand) -> BBDownInfoRunnerOutput:
        return BBDownInfoRunnerOutput(exit_code=0, stdout_text=read_fixture("info_public_ok_sanitized.txt"))

    result = run_bbdown_info_probe(manual_url=SAMPLE_URL, job_temp_dir=tmp_path, runner=fake_runner)

    assert "executable_not_found" not in {item.value for item in PlatformResult}
    assert result.platform_result is PlatformResult.ok
