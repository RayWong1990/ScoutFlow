"""Contract tests for the T-P1A-019 dry-run metadata orchestrator.

These tests pin the orchestration seam's invariants:

* the orchestrator only ever calls the injected runner; it MUST NOT touch
  ``subprocess.run`` or any live BBDown surface;
* success evidence (materialised assets + receipt candidate) is gated on
  ``platform_result == ok`` AND a T-P1A-011C auth-present source;
* parser_drift / auth_required / vip / region / not_found / rate_limited
  outcomes never emit success evidence;
* materialised asset paths stay inside the capture bundle and never escape
  through traversal;
* the redacted stdout excerpt does not carry signed-media URLs;
* the dedupe_key is propagated verbatim into the receipt candidate's
  ``idempotency.dedupe_key`` so 18's enqueue contract is preserved.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]
API_ROOT = ROOT / "services" / "api"
FIXTURE_ROOT = ROOT / "tests" / "fixtures" / "bbdown"
if str(API_ROOT) not in sys.path:
    sys.path.insert(0, str(API_ROOT))


SAMPLE_URL = "https://www.bilibili.com/video/BV19D9eB9Etg/?spm_id_from=333.1007.tianma.3-1-7.click"
SAMPLE_CAPTURE_ID = "01CAPTUREDRYRUN0000000019"
SAMPLE_JOB_ID = "01JOBDRYRUN0000000000019"
SAMPLE_DEDUPE_KEY = "bilibili:BVSCOUTFLOW1:metadata_fetch"


def _read_fixture(name: str) -> str:
    return (FIXTURE_ROOT / name).read_text(encoding="utf-8")


def _build_runner(stdout_fixture: str, *, exit_code: int = 0):
    from scoutflow_api.external_tools.bbdown_info_adapter import BBDownInfoCommand, BBDownInfoRunnerOutput

    seen: list[BBDownInfoCommand] = []

    def runner(command: BBDownInfoCommand) -> BBDownInfoRunnerOutput:
        seen.append(command)
        return BBDownInfoRunnerOutput(exit_code=exit_code, stdout_text=_read_fixture(stdout_fixture))

    return runner, seen


def test_happy_path_emits_receipt_candidate_with_dedupe_key(tmp_path: Path) -> None:
    from scoutflow_api.orchestration import dry_run_metadata_probe
    from scoutflow_api.platform_result import PlatformResult

    runner, seen = _build_runner("info_public_ok_sanitized.txt")
    artifacts_root = tmp_path / "artifacts"

    outcome = dry_run_metadata_probe(
        capture_id=SAMPLE_CAPTURE_ID,
        job_id=SAMPLE_JOB_ID,
        dedupe_key=SAMPLE_DEDUPE_KEY,
        manual_url=SAMPLE_URL,
        job_temp_dir=tmp_path / "bbdown-info-job",
        artifacts_root=artifacts_root,
        runner=runner,
    )

    assert len(seen) == 1, "runner must be called exactly once"
    assert outcome.platform_result is PlatformResult.ok
    assert outcome.success_evidence_emitted is True
    assert outcome.success_blocker is None
    assert outcome.receipt_candidate is not None
    assert outcome.receipt_candidate.idempotency.dedupe_key == SAMPLE_DEDUPE_KEY
    assert outcome.receipt_candidate.platform_result.value == "ok"
    assert outcome.receipt_candidate.job_type == "metadata_fetch"
    assert outcome.receipt_candidate.next_status == "metadata_fetched"
    assert len(outcome.materialized_assets) == 2
    kinds = {asset.artifact_kind for asset in outcome.materialized_assets}
    assert kinds == {"safe_metadata_evidence", "metadata_probe_summary"}


def test_materialized_assets_stay_inside_capture_bundle(tmp_path: Path) -> None:
    from scoutflow_api.orchestration import dry_run_metadata_probe

    runner, _ = _build_runner("info_public_ok_sanitized.txt")
    artifacts_root = tmp_path / "artifacts"

    outcome = dry_run_metadata_probe(
        capture_id=SAMPLE_CAPTURE_ID,
        job_id=SAMPLE_JOB_ID,
        dedupe_key=SAMPLE_DEDUPE_KEY,
        manual_url=SAMPLE_URL,
        job_temp_dir=tmp_path / "bbdown-info-job",
        artifacts_root=artifacts_root,
        runner=runner,
    )

    capture_root = (artifacts_root / "bilibili" / SAMPLE_CAPTURE_ID).resolve()
    for asset in outcome.materialized_assets:
        assert asset.relative_path.startswith("bundle/")
        assert ".." not in Path(asset.relative_path).parts
        actual = (artifacts_root / "bilibili" / SAMPLE_CAPTURE_ID / asset.relative_path).resolve()
        actual.relative_to(capture_root)
        assert actual.is_file()


@pytest.mark.parametrize(
    ("fixture", "exit_code", "expected_blocker_token"),
    [
        ("info_parser_drift_sanitized.txt", 0, "parser_drift"),
        ("info_auth_required_sanitized.txt", 1, "auth_required"),
        ("info_vip_required_sanitized.txt", 1, "vip_required"),
        ("info_region_blocked_sanitized.txt", 1, "region_blocked"),
        ("info_not_found_sanitized.txt", 1, "not_found"),
        ("info_rate_limited_sanitized.txt", 1, "rate_limited"),
        ("info_forbidden_sanitized.txt", 1, "forbidden"),
    ],
)
def test_non_ok_platform_results_do_not_emit_success_evidence(
    tmp_path: Path, fixture: str, exit_code: int, expected_blocker_token: str
) -> None:
    from scoutflow_api.orchestration import dry_run_metadata_probe

    runner, _ = _build_runner(fixture, exit_code=exit_code)

    outcome = dry_run_metadata_probe(
        capture_id=SAMPLE_CAPTURE_ID,
        job_id=SAMPLE_JOB_ID,
        dedupe_key=SAMPLE_DEDUPE_KEY,
        manual_url=SAMPLE_URL,
        job_temp_dir=tmp_path / "bbdown-info-job",
        artifacts_root=tmp_path / "artifacts",
        runner=runner,
    )

    assert outcome.success_evidence_emitted is False
    assert outcome.materialized_assets == ()
    assert outcome.receipt_candidate is None
    assert outcome.success_blocker is not None
    assert outcome.success_blocker.startswith("platform_result_not_ok:")
    assert expected_blocker_token in outcome.success_blocker

    capture_root = tmp_path / "artifacts" / "bilibili" / SAMPLE_CAPTURE_ID
    assert not capture_root.exists() or not any(capture_root.rglob("*.json"))


def test_evidence_source_other_than_T_P1A_011C_blocks_success(tmp_path: Path) -> None:
    from scoutflow_api.metadata_probe_receipt_bridge import MetadataProbeEvidenceSource
    from scoutflow_api.orchestration import dry_run_metadata_probe

    runner, _ = _build_runner("info_public_ok_sanitized.txt")
    rogue_source = MetadataProbeEvidenceSource(
        task_id="T-P1A-009",
        report_path="docs/research/t-p1a-009-bbdown-local-runtime-spike-report-2026-05-03.md",
        probe_mode="no-auth",
    )

    outcome = dry_run_metadata_probe(
        capture_id=SAMPLE_CAPTURE_ID,
        job_id=SAMPLE_JOB_ID,
        dedupe_key=SAMPLE_DEDUPE_KEY,
        manual_url=SAMPLE_URL,
        job_temp_dir=tmp_path / "bbdown-info-job",
        artifacts_root=tmp_path / "artifacts",
        runner=runner,
        evidence_source=rogue_source,
    )

    assert outcome.success_evidence_emitted is False
    assert outcome.success_blocker is not None
    assert outcome.success_blocker.startswith("evidence_source_not_authorized:")
    assert outcome.materialized_assets == ()
    assert outcome.receipt_candidate is None


def test_default_evidence_source_matches_T_P1A_011C() -> None:
    from scoutflow_api.models import (
        CURRENT_METADATA_EVIDENCE_PROBE_MODE,
        CURRENT_METADATA_EVIDENCE_REPORT_PATH,
        CURRENT_METADATA_EVIDENCE_TASK_ID,
    )
    from scoutflow_api.orchestration import default_evidence_source

    src = default_evidence_source()
    assert src.task_id == CURRENT_METADATA_EVIDENCE_TASK_ID == "T-P1A-011C"
    assert src.probe_mode == CURRENT_METADATA_EVIDENCE_PROBE_MODE == "auth-present"
    assert src.report_path == CURRENT_METADATA_EVIDENCE_REPORT_PATH


def test_orchestrator_never_invokes_subprocess_run(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Pin the no-live-subprocess invariant via a tripwire on subprocess.run."""

    from scoutflow_api.orchestration import dry_run_metadata_probe

    runner, _ = _build_runner("info_public_ok_sanitized.txt")
    calls: list[object] = []

    def tripwire(*args: object, **kwargs: object) -> object:
        calls.append((args, kwargs))
        raise AssertionError("dry_run_metadata_probe must not call subprocess.run")

    monkeypatch.setattr(subprocess, "run", tripwire)

    outcome = dry_run_metadata_probe(
        capture_id=SAMPLE_CAPTURE_ID,
        job_id=SAMPLE_JOB_ID,
        dedupe_key=SAMPLE_DEDUPE_KEY,
        manual_url=SAMPLE_URL,
        job_temp_dir=tmp_path / "bbdown-info-job",
        artifacts_root=tmp_path / "artifacts",
        runner=runner,
    )

    assert calls == []
    assert outcome.success_evidence_emitted is True


def test_safe_stdout_excerpt_does_not_contain_signed_media_url(tmp_path: Path) -> None:
    from scoutflow_api.orchestration import dry_run_metadata_probe

    runner, _ = _build_runner("info_signed_url_redacted_sanitized.txt")

    outcome = dry_run_metadata_probe(
        capture_id=SAMPLE_CAPTURE_ID,
        job_id=SAMPLE_JOB_ID,
        dedupe_key=SAMPLE_DEDUPE_KEY,
        manual_url=SAMPLE_URL,
        job_temp_dir=tmp_path / "bbdown-info-job",
        artifacts_root=tmp_path / "artifacts",
        runner=runner,
    )

    excerpt = outcome.safe_stdout_excerpt
    assert "upos-sz-mirrorcoso1.bilivideo.com" not in excerpt
    assert "?token=" not in excerpt
    assert "x-oss-credential=" not in excerpt.lower()
    assert outcome.redaction_applied is True


def test_non_manual_source_is_rejected_before_any_runner_call(tmp_path: Path) -> None:
    from scoutflow_api.external_tools.bbdown_info_adapter import BBDownInfoAdapterInputError
    from scoutflow_api.orchestration import dry_run_metadata_probe

    runner, seen = _build_runner("info_public_ok_sanitized.txt")

    with pytest.raises(BBDownInfoAdapterInputError):
        dry_run_metadata_probe(
            capture_id=SAMPLE_CAPTURE_ID,
            job_id=SAMPLE_JOB_ID,
            dedupe_key=SAMPLE_DEDUPE_KEY,
            manual_url=SAMPLE_URL,
            job_temp_dir=tmp_path / "bbdown-info-job",
            artifacts_root=tmp_path / "artifacts",
            runner=runner,
            source_kind="recommendation",
        )

    assert seen == []
