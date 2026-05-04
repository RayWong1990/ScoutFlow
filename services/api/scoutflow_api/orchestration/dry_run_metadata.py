"""Dry-run metadata_fetch orchestrator.

Connects the existing injected-runner BBDown ``-info`` adapter
(:mod:`scoutflow_api.external_tools.bbdown_info_adapter`) and the metadata
receipt bridge (:mod:`scoutflow_api.metadata_probe_receipt_bridge`) into a
single function that takes a fake / injected runner and returns a structured
outcome. This is the only orchestration seam approved during T-P1A-019; it
lives outside ``storage.py`` / ``jobs.py`` / ``captures.py`` (T-P1A-018
conflict-domain owned) by design.

Receipt emission semantics:

* ``platform_result == ok`` AND URL-derived ``platform_item_id`` matches the
  parsed value AND evidence source passes the T-P1A-011C auth-present gate
  → success ``WorkerReceipt`` candidate with materialised
  ``safe_metadata_evidence`` + ``metadata_probe_summary`` artifacts;
  ``success_evidence_emitted=True``.
* ``platform_result != ok`` → failure ``WorkerReceipt`` candidate with
  ``produced_assets=[]``; storage will advance the job to ``failed`` and
  leave the capture in ``discovered``; ``success_evidence_emitted=False``,
  ``success_blocker="platform_result_not_ok:<value>"``.
* ``platform_result == ok`` but provenance / evidence-source guards reject
  the result → no receipt is emitted; ``success_blocker`` records the gate
  that fired (``platform_item_id_mismatch:...`` or
  ``evidence_source_not_authorized:...``). The caller decides whether to
  retry, escalate, or quarantine the capture.

The orchestrator MUST NOT:

* call ``subprocess.run`` or any other live process surface;
* invoke real BBDown / yt-dlp / ffmpeg / ASR;
* download media or write to ``media/`` / ``audio/`` / ``transcript/`` zones;
* persist raw stdout / stderr beyond the redacted excerpt already produced
  by :func:`scoutflow_api.external_tools.bbdown_info_adapter.run_bbdown_info_probe`.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from scoutflow_api.external_tools.bbdown_info_adapter import (
    DEFAULT_BBDOWN_EXECUTABLE,
    BBDownInfoProbeResult,
    BBDownInfoRunner,
    run_bbdown_info_probe,
    validate_manual_bilibili_url,
)
from scoutflow_api.external_tools.bbdown_info_parser import BBDownInfoParseResult
from scoutflow_api.metadata_probe_receipt_bridge import (
    MaterializedMetadataProbeAsset,
    MetadataProbeEvidenceSource,
    build_metadata_fetch_failure_receipt,
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
    """Return the only currently-approved success-evidence source."""

    return MetadataProbeEvidenceSource(
        task_id=CURRENT_METADATA_EVIDENCE_TASK_ID,
        report_path=CURRENT_METADATA_EVIDENCE_REPORT_PATH,
        probe_mode=CURRENT_METADATA_EVIDENCE_PROBE_MODE,
    )


@dataclass(frozen=True)
class DryRunMetadataProbeOutcome:
    """Structured outcome of a dry-run metadata_fetch probe.

    ``receipt_candidate`` is non-None for both success and failure receipts.
    The two cases are distinguished by ``success_evidence_emitted``:

    * success: ``platform_result == ok`` AND provenance + evidence-source
      gates passed; ``materialized_assets`` contains the two bundle JSONs.
    * failure: ``platform_result != ok``; ``materialized_assets`` is empty
      and ``produced_assets`` on the receipt is empty.

    When provenance or evidence-source gates reject an ok probe,
    ``receipt_candidate`` is ``None`` and ``success_blocker`` records the
    rejecting gate.
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
    """Run an injected-runner BBDown -info probe and emit success / failure receipts.

    Never calls ``subprocess.run`` and has no live-runner fallback. Success
    evidence is double-gated: probe must report ``platform_result=ok`` AND
    ``probe.platform_item_id`` must equal the URL-derived BV id AND the
    evidence source must pass the T-P1A-011C auth-present validator.
    """

    if evidence_source is None:
        evidence_source = default_evidence_source()

    expected_platform_item_id = validate_manual_bilibili_url(
        manual_url=manual_url,
        source_kind=source_kind,
    )

    probe = run_bbdown_info_probe(
        manual_url=manual_url,
        job_temp_dir=Path(job_temp_dir),
        runner=runner,
        source_kind=source_kind,
        executable=executable,
    )

    if probe.platform_result is not PlatformResult.ok:
        failure_receipt = build_metadata_fetch_failure_receipt(
            capture_id=capture_id,
            job_id=job_id,
            dedupe_key=dedupe_key,
            platform_result=probe.platform_result,
        )
        return _outcome(
            probe=probe,
            materialized=(),
            receipt_candidate=failure_receipt,
            success_evidence_emitted=False,
            success_blocker=f"platform_result_not_ok:{probe.platform_result.value}",
        )

    if probe.platform_item_id != expected_platform_item_id:
        return _outcome(
            probe=probe,
            materialized=(),
            receipt_candidate=None,
            success_evidence_emitted=False,
            success_blocker=(
                "platform_item_id_mismatch:"
                f"expected={expected_platform_item_id}:actual={probe.platform_item_id}"
            ),
        )

    try:
        evidence_source.validate_for_success_evidence()
    except ValueError as exc:
        return _outcome(
            probe=probe,
            materialized=(),
            receipt_candidate=None,
            success_evidence_emitted=False,
            success_blocker=f"evidence_source_not_authorized:{exc}",
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

    return _outcome(
        probe=probe,
        materialized=materialized,
        receipt_candidate=receipt,
        success_evidence_emitted=True,
        success_blocker=None,
    )


def _outcome(
    *,
    probe: BBDownInfoProbeResult,
    materialized: tuple[MaterializedMetadataProbeAsset, ...],
    receipt_candidate: WorkerReceipt | None,
    success_evidence_emitted: bool,
    success_blocker: str | None,
) -> DryRunMetadataProbeOutcome:
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
        receipt_candidate=receipt_candidate,
        success_evidence_emitted=success_evidence_emitted,
        success_blocker=success_blocker,
    )
