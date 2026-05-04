"""Dry-run metadata_fetch orchestrator.

Connects the existing injected-runner BBDown ``-info`` adapter
(:mod:`scoutflow_api.external_tools.bbdown_info_adapter`) and the metadata
receipt bridge (:mod:`scoutflow_api.metadata_probe_receipt_bridge`) into a
single function that takes a fake / injected runner and returns a structured
outcome. This is the only orchestration seam approved during T-P1A-019; it
lives outside ``storage.py`` / ``jobs.py`` / ``captures.py`` (T-P1A-018
conflict-domain owned) by design.

The orchestrator MUST NOT:

* call ``subprocess.run`` or any other live process surface;
* invoke real BBDown / yt-dlp / ffmpeg / ASR;
* download media or write to ``media/`` / ``audio/`` / ``transcript/`` zones;
* persist raw stdout / stderr beyond the redacted excerpt already produced by
  :func:`scoutflow_api.external_tools.bbdown_info_adapter.run_bbdown_info_probe`.

Success-evidence emission (materialised assets + receipt candidate) is gated
on the same T-P1A-011C auth-present source contract enforced by the bridge:
the orchestrator delegates that decision to
:meth:`MetadataProbeEvidenceSource.validate_for_success_evidence`.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from scoutflow_api.external_tools.bbdown_info_adapter import (
    DEFAULT_BBDOWN_EXECUTABLE,
    BBDownInfoProbeResult,
    BBDownInfoRunner,
    run_bbdown_info_probe,
)
from scoutflow_api.external_tools.bbdown_info_parser import BBDownInfoParseResult
from scoutflow_api.metadata_probe_receipt_bridge import (
    MaterializedMetadataProbeAsset,
    MetadataProbeEvidenceSource,
    build_metadata_fetch_receipt,
    materialize_metadata_probe_assets,
    prepare_success_metadata_probe_assets,
)
from scoutflow_api.models import (
    CURRENT_METADATA_EVIDENCE_PROBE_MODE,
    CURRENT_METADATA_EVIDENCE_REPORT_PATH,
    CURRENT_METADATA_EVIDENCE_TASK_ID,
    WorkerReceipt,
)
from scoutflow_api.platform_result import PlatformResult


def default_evidence_source() -> MetadataProbeEvidenceSource:
    """Return the only currently-approved success-evidence source.

    Defaults match the T-P1A-011C auth-present probe report. Callers that
    pass a different :class:`MetadataProbeEvidenceSource` will be rejected by
    the bridge's success-evidence validator, and the orchestrator will record
    ``success_blocker="evidence_source_not_authorized:..."`` instead of
    emitting a receipt candidate.
    """

    return MetadataProbeEvidenceSource(
        task_id=CURRENT_METADATA_EVIDENCE_TASK_ID,
        report_path=CURRENT_METADATA_EVIDENCE_REPORT_PATH,
        probe_mode=CURRENT_METADATA_EVIDENCE_PROBE_MODE,
    )


@dataclass(frozen=True)
class DryRunMetadataProbeOutcome:
    """Structured outcome of a dry-run metadata_fetch probe.

    ``success_evidence_emitted`` is true iff
    ``platform_result == PlatformResult.ok`` AND the evidence source passes
    the T-P1A-011C auth-present validator. Otherwise ``materialized_assets``
    is empty, ``receipt_candidate`` is ``None``, and ``success_blocker``
    describes the gate that rejected emission.
    """

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
    materialized_assets: tuple[MaterializedMetadataProbeAsset, ...]
    receipt_candidate: WorkerReceipt | None
    success_evidence_emitted: bool
    success_blocker: str | None


def dry_run_metadata_probe(
    *,
    capture_id: str,
    job_id: str,
    dedupe_key: str,
    manual_url: str,
    job_temp_dir: Path,
    artifacts_root: Path,
    runner: BBDownInfoRunner,
    source_kind: str = "manual_url",
    executable: str = DEFAULT_BBDOWN_EXECUTABLE,
    evidence_source: MetadataProbeEvidenceSource | None = None,
) -> DryRunMetadataProbeOutcome:
    """Run an injected-runner BBDown -info probe and conditionally emit a receipt candidate.

    Parameters
    ----------
    capture_id, job_id, dedupe_key:
        Identity fields supplied by the caller. ``dedupe_key`` is propagated
        verbatim into the receipt candidate's ``idempotency.dedupe_key`` so
        downstream completion stays consistent with T-P1A-018's enqueue
        contract (``bilibili:<platform_item_id>:metadata_fetch``).
    manual_url:
        Bilibili manual URL. Validated by the adapter; non-manual sources
        and credential-bearing URLs are rejected before any runner call.
    job_temp_dir:
        Working directory passed to BBDown via ``--work-dir``. Must be a
        repo-external temp dir for live runs; in the dry-run path it is only
        used to build the command and is otherwise inert.
    artifacts_root:
        Root under which materialised assets are written when a success
        receipt is produced. The bridge's materialiser enforces containment
        (``bundle/`` subtree, no traversal).
    runner:
        Injected callable. The orchestrator NEVER calls ``subprocess.run``
        and has no implicit fallback to a live runner.
    evidence_source:
        Optional override. Defaults to :func:`default_evidence_source`
        (T-P1A-011C auth-present). Any other source is rejected by the
        bridge and the orchestrator returns a no-success outcome.
    """

    if evidence_source is None:
        evidence_source = default_evidence_source()

    probe = run_bbdown_info_probe(
        manual_url=manual_url,
        job_temp_dir=Path(job_temp_dir),
        runner=runner,
        source_kind=source_kind,
        executable=executable,
    )

    if probe.platform_result is not PlatformResult.ok:
        return _no_success_outcome(
            probe=probe,
            blocker=f"platform_result_not_ok:{probe.platform_result.value}",
        )

    try:
        evidence_source.validate_for_success_evidence()
    except ValueError as exc:
        return _no_success_outcome(
            probe=probe,
            blocker=f"evidence_source_not_authorized:{exc}",
        )

    parsed = BBDownInfoParseResult(
        platform_result=probe.platform_result,
        platform_item_id=probe.platform_item_id,
        title=probe.title,
        duration_seconds=probe.duration_seconds,
        page_count=probe.page_count,
        selected_page=probe.selected_page,
        uploader_name=probe.uploader_name,
        estimated_media_bytes=probe.estimated_media_bytes,
        safe_stdout_excerpt=probe.safe_stdout_excerpt,
        redaction_applied=probe.redaction_applied,
    )

    prepared_assets = prepare_success_metadata_probe_assets(
        parsed=parsed,
        source_url=manual_url,
        evidence_source=evidence_source,
    )
    materialized = tuple(
        materialize_metadata_probe_assets(
            artifacts_root=Path(artifacts_root),
            capture_id=capture_id,
            assets=prepared_assets,
        )
    )
    receipt = build_metadata_fetch_receipt(
        capture_id=capture_id,
        job_id=job_id,
        dedupe_key=dedupe_key,
        source_url=manual_url,
        evidence_source=evidence_source,
        materialized_assets=materialized,
    )

    return DryRunMetadataProbeOutcome(
        platform_result=probe.platform_result,
        platform_item_id=probe.platform_item_id,
        title=probe.title,
        duration_seconds=probe.duration_seconds,
        page_count=probe.page_count,
        selected_page=probe.selected_page,
        uploader_name=probe.uploader_name,
        estimated_media_bytes=probe.estimated_media_bytes,
        safe_stdout_excerpt=probe.safe_stdout_excerpt,
        redaction_applied=probe.redaction_applied,
        tool_exit_code=probe.tool_exit_code,
        materialized_assets=materialized,
        receipt_candidate=receipt,
        success_evidence_emitted=True,
        success_blocker=None,
    )


def _no_success_outcome(*, probe: BBDownInfoProbeResult, blocker: str) -> DryRunMetadataProbeOutcome:
    return DryRunMetadataProbeOutcome(
        platform_result=probe.platform_result,
        platform_item_id=probe.platform_item_id,
        title=probe.title,
        duration_seconds=probe.duration_seconds,
        page_count=probe.page_count,
        selected_page=probe.selected_page,
        uploader_name=probe.uploader_name,
        estimated_media_bytes=probe.estimated_media_bytes,
        safe_stdout_excerpt=probe.safe_stdout_excerpt,
        redaction_applied=probe.redaction_applied,
        tool_exit_code=probe.tool_exit_code,
        materialized_assets=(),
        receipt_candidate=None,
        success_evidence_emitted=False,
        success_blocker=blocker,
    )
