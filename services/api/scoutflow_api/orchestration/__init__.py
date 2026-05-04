"""ScoutFlow orchestration seam.

Holds dry-run / injected-runner orchestrators that connect existing adapters
and the metadata receipt bridge into a testable end-to-end flow without ever
invoking real BBDown, real Bilibili URLs, media download, ffmpeg, ASR, or
credential material. T-P1A-019 introduced this module so 19's contract tests
and e2e tests can exercise the full metadata_fetch path while leaving 18's
storage / jobs / captures / main untouched.
"""

from scoutflow_api.orchestration.dry_run_metadata import (
    DryRunMetadataProbeOutcome,
    default_evidence_source,
    dry_run_metadata_probe,
)


__all__ = [
    "DryRunMetadataProbeOutcome",
    "default_evidence_source",
    "dry_run_metadata_probe",
]
