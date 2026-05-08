from __future__ import annotations

import json
from pathlib import Path
import sys

import pytest


ROOT = Path(__file__).resolve().parents[2]
API_ROOT = ROOT / "services" / "api"
FIXTURE_ROOT = ROOT / "tests" / "fixtures" / "runtime_tools"
if str(API_ROOT) not in sys.path:
    sys.path.insert(0, str(API_ROOT))


def _read_text_fixture(name: str) -> str:
    return (FIXTURE_ROOT / name).read_text(encoding="utf-8")


def _read_json_fixture(name: str) -> dict[str, object]:
    return json.loads((FIXTURE_ROOT / name).read_text(encoding="utf-8"))


def test_build_runtime_canary_manifest_uses_conservative_defaults() -> None:
    from scoutflow_api.external_tools.runtime_tools_canary_contract import (
        DEFAULT_REMAINING_HOLDS,
        build_runtime_canary_manifest,
    )

    manifest = build_runtime_canary_manifest(repo_root=ROOT)

    assert manifest.manifest_version == "RuntimeCanaryManifestV1"
    assert manifest.lane_id == "Lane B"
    assert manifest.task_id == "T-P1A-161"
    assert manifest.source_family == "bilibili"
    assert manifest.source_kind == "manual_url"
    assert manifest.route_hypothesis == "yt-dlp metadata-first"
    assert manifest.fallback_hypothesis == "BBDown fallback-comparator"
    assert manifest.tool_execution_status == "not_executed"
    assert manifest.network_used is False
    assert manifest.media_downloaded is False
    assert manifest.raw_stdout_tracked is False
    assert manifest.raw_stderr_tracked is False
    assert manifest.credential_material_seen is False
    assert manifest.platform_result is None
    assert manifest.failure_classification_reason == "not_executed_by_dispatch_boundary"
    assert manifest.remaining_holds == DEFAULT_REMAINING_HOLDS
    assert manifest.human_runtime_gate_required is True


@pytest.mark.parametrize(
    "temp_root",
    [
        ROOT / "tmp" / "runtime-tools",
        ROOT / "data" / "runtime-tools",
        ROOT / "referencerepo" / "runtime-tools",
    ],
)
def test_repo_external_temp_root_rejects_repo_internal_paths(temp_root: Path) -> None:
    from scoutflow_api.external_tools.runtime_tools_canary_contract import build_runtime_canary_manifest

    with pytest.raises(ValueError):
        build_runtime_canary_manifest(repo_root=ROOT, repo_external_temp_root=temp_root)


def test_repo_external_temp_root_accepts_external_path(tmp_path: Path) -> None:
    from scoutflow_api.external_tools.runtime_tools_canary_contract import build_runtime_canary_manifest

    external_root = tmp_path / "runtime-tools"
    manifest = build_runtime_canary_manifest(repo_root=ROOT, repo_external_temp_root=external_root)

    assert manifest.repo_external_temp_root == str(external_root)


def test_safe_excerpt_fixtures_pass_contract_scan() -> None:
    from scoutflow_api.external_tools.runtime_tools_canary_contract import validate_safe_excerpt_text

    assert validate_safe_excerpt_text(_read_text_fixture("safe_stdout_excerpt.txt")) == []
    assert validate_safe_excerpt_text(_read_text_fixture("safe_stderr_excerpt.txt")) == []


@pytest.mark.parametrize(
    ("sample", "expected_token"),
    [
        ("Cookie: SESSDATA=secret", "cookie header"),
        ("Authorization: bearer secret", "authorization header"),
        ("https://media.example/video.m4s?token=secret", "signed url"),
        ("/Users/demo/Library/Application Support/Google/Chrome/Profile 1", "browser profile path"),
    ],
)
def test_safe_excerpt_scan_rejects_forbidden_content(sample: str, expected_token: str) -> None:
    from scoutflow_api.external_tools.runtime_tools_canary_contract import validate_safe_excerpt_text

    violations = validate_safe_excerpt_text(sample)
    assert expected_token in violations


def test_manifest_fixture_round_trips_through_model() -> None:
    from scoutflow_api.external_tools.runtime_tools_canary_contract import RuntimeCanaryManifestV1

    payload = _read_json_fixture("runtime_canary_manifest_v1_candidate.json")
    manifest = RuntimeCanaryManifestV1.model_validate(payload)

    assert manifest.tool_execution_status == "not_executed"
    assert manifest.safe_stdout_excerpt_path == "tests/fixtures/runtime_tools/safe_stdout_excerpt.txt"
    assert manifest.safe_stderr_excerpt_path == "tests/fixtures/runtime_tools/safe_stderr_excerpt.txt"
    assert manifest.platform_result is None
