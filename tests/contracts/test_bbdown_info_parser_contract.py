from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
API_ROOT = ROOT / "services" / "api"
FIXTURE_ROOT = ROOT / "tests" / "fixtures" / "bbdown"
if str(API_ROOT) not in sys.path:
    sys.path.insert(0, str(API_ROOT))


def read_fixture(name: str) -> str:
    return (FIXTURE_ROOT / name).read_text(encoding="utf-8")


def test_ok_fixture_parses_typed_metadata() -> None:
    from scoutflow_api.external_tools.bbdown_info_parser import parse_bbdown_info_output
    from scoutflow_api.platform_result import PlatformResult

    result = parse_bbdown_info_output(read_fixture("info_public_ok_sanitized.txt"))

    assert result.platform_result is PlatformResult.ok
    assert result.platform_item_id == "BVSCOUTFLOW1"
    assert result.title == "ScoutFlow public fixture title"
    assert result.duration_seconds == 252
    assert result.page_count == 1
    assert result.selected_page == "P1"
    assert result.uploader_name == "ScoutFlow Fixture Uploader"
    assert result.estimated_media_bytes == 10485760
    assert result.redaction_applied is True


def test_failure_fixtures_map_to_existing_platform_results() -> None:
    from scoutflow_api.external_tools.bbdown_info_parser import blocks_quick_capture, parse_bbdown_info_output
    from scoutflow_api.platform_result import PlatformResult

    cases = {
        "info_auth_required_sanitized.txt": PlatformResult.auth_required,
        "info_forbidden_sanitized.txt": PlatformResult.forbidden,
        "info_region_blocked_sanitized.txt": PlatformResult.region_blocked,
        "info_rate_limited_sanitized.txt": PlatformResult.rate_limited,
        "info_not_found_sanitized.txt": PlatformResult.not_found,
        "info_vip_required_sanitized.txt": PlatformResult.vip_required,
        "info_parser_drift_sanitized.txt": PlatformResult.parser_drift,
    }

    for fixture_name, expected in cases.items():
        result = parse_bbdown_info_output(read_fixture(fixture_name))
        assert result.platform_result is expected
        assert blocks_quick_capture(result) is True


def test_unknown_error_classifies_without_parallel_enum() -> None:
    from scoutflow_api.external_tools.bbdown_info_parser import parse_bbdown_info_output
    from scoutflow_api.platform_result import PlatformResult

    result = parse_bbdown_info_output("BBDown -info sanitized fixture\nFatal error: tool exited with code 9")

    assert result.platform_result is PlatformResult.unknown_error
    assert type(result.platform_result) is PlatformResult


def test_missing_required_success_fields_becomes_parser_drift() -> None:
    from scoutflow_api.external_tools.bbdown_info_parser import blocks_quick_capture, parse_bbdown_info_output
    from scoutflow_api.platform_result import PlatformResult

    result = parse_bbdown_info_output("BBDown -info sanitized fixture\nResult: ok\nPlatform Item ID: BVSCOUTFLOW4")

    assert result.platform_result is PlatformResult.parser_drift
    assert blocks_quick_capture(result) is True


def test_redaction_before_parse_is_mandatory(monkeypatch) -> None:
    from scoutflow_api.external_tools import bbdown_info_parser
    from scoutflow_api.platform_result import PlatformResult

    calls: list[str] = []
    original_redactor = bbdown_info_parser.redact_sensitive_text

    def tracking_redactor(text: str) -> str:
        calls.append(text)
        return original_redactor(text)

    monkeypatch.setattr(bbdown_info_parser, "redact_sensitive_text", tracking_redactor)
    media_url = "https://media.example.invalid/" + "video" + ".m4s"
    raw_stdout = "\n".join(
        [
            "BBDown -info sanitized fixture",
            "Platform Item ID: BVSCOUTFLOW5",
            "Title: fixture with in-memory media URL",
            "Duration: 00:01:00",
            media_url + "?" + "si" + "gn=placeholder&dead" + "line=1900000000",
        ]
    )

    result = bbdown_info_parser.parse_bbdown_info_output(raw_stdout)

    assert calls == [raw_stdout]
    assert result.platform_result is PlatformResult.ok
    assert media_url not in result.safe_stdout_excerpt
    assert "[REDACTED_SIGNED_MEDIA_URL]" in result.safe_stdout_excerpt
    assert "placeholder" not in result.safe_stdout_excerpt


def test_no_raw_stdout_persistence_and_safe_excerpt_only() -> None:
    from scoutflow_api.external_tools.bbdown_info_parser import BBDownInfoParseResult, parse_bbdown_info_output

    result = parse_bbdown_info_output(read_fixture("info_public_ok_sanitized.txt"))

    assert isinstance(result, BBDownInfoParseResult)
    assert "raw_stdout" not in result.__dict__
    assert set(result.__dict__) == {
        "platform_item_id",
        "title",
        "duration_seconds",
        "page_count",
        "selected_page",
        "uploader_name",
        "estimated_media_bytes",
        "platform_result",
        "safe_stdout_excerpt",
        "redaction_applied",
    }
    assert "safe_stdout_excerpt" in result.__dict__


def test_signed_url_placeholder_fixture_remains_safe_after_redaction() -> None:
    from scoutflow_api.external_tools.bbdown_info_parser import parse_bbdown_info_output
    from scoutflow_api.platform_result import PlatformResult

    result = parse_bbdown_info_output(read_fixture("info_signed_url_redacted_sanitized.txt"))

    assert result.platform_result is PlatformResult.ok
    assert "[REDACTED_SIGNED_MEDIA_URL]" in result.safe_stdout_excerpt
    assert "http" not in result.safe_stdout_excerpt


def test_temporary_media_url_placeholder_fixture_remains_safe_after_redaction() -> None:
    from scoutflow_api.external_tools.bbdown_info_parser import parse_bbdown_info_output
    from scoutflow_api.platform_result import PlatformResult

    result = parse_bbdown_info_output(read_fixture("info_temporary_media_url_redacted_sanitized.txt"))

    assert result.platform_result is PlatformResult.ok
    assert "[REDACTED_TEMPORARY_MEDIA_URL]" in result.safe_stdout_excerpt
    assert "http" not in result.safe_stdout_excerpt


def test_in_memory_temporary_media_url_collapses_after_redaction_stage() -> None:
    from scoutflow_api.external_tools.bbdown_info_parser import parse_bbdown_info_output

    media_url = "https://media.example.invalid/" + "audio" + ".m4s"
    raw_stdout = "\n".join(
        [
            "BBDown -info sanitized fixture",
            "Platform Item ID: BVSCOUTFLOW6",
            "Title: fixture with temporary media URL",
            "Duration: 90 seconds",
            media_url,
        ]
    )

    result = parse_bbdown_info_output(raw_stdout)

    assert media_url not in result.safe_stdout_excerpt
    assert "[REDACTED_TEMPORARY_MEDIA_URL]" in result.safe_stdout_excerpt
