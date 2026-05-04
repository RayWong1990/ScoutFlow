from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]
API_ROOT = ROOT / "services" / "api"
FIXTURE_ROOT = ROOT / "tests" / "fixtures" / "bbdown"
if str(API_ROOT) not in sys.path:
    sys.path.insert(0, str(API_ROOT))


def read_fixture(name: str) -> str:
    return (FIXTURE_ROOT / name).read_text(encoding="utf-8")


def test_success_bridge_prepares_bundle_only_safe_assets() -> None:
    from scoutflow_api.external_tools.bbdown_info_parser import parse_bbdown_info_output
    from scoutflow_api.metadata_probe_receipt_bridge import (
        MetadataProbeEvidenceSource,
        prepare_success_metadata_probe_assets,
    )

    parsed = parse_bbdown_info_output(read_fixture("info_public_ok_sanitized.txt"))
    source = MetadataProbeEvidenceSource(
        task_id="T-P1A-011C",
        report_path="docs/research/t-p1a-011c-bbdown-auth-present-info-probe-report-2026-05-04.md",
        probe_mode="auth-present",
    )

    assets = prepare_success_metadata_probe_assets(
        parsed=parsed,
        source_url="https://www.bilibili.com/video/BV19D9eB9Etg",
        evidence_source=source,
    )

    assert [asset.artifact_kind for asset in assets] == [
        "safe_metadata_evidence",
        "metadata_probe_summary",
    ]
    assert all(asset.relative_path.startswith("bundle/") for asset in assets)
    assert not any(kind in {"media", "audio", "video", "transcript", "audio_transcript"} for kind in [asset.artifact_kind for asset in assets])

    safe_payload = json.loads(assets[0].content_bytes.decode("utf-8"))
    assert safe_payload["evidence_source"]["task_id"] == "T-P1A-011C"
    assert safe_payload["evidence_source"]["probe_mode"] == "auth-present"
    assert "stdout_text" not in safe_payload
    assert "stderr_text" not in safe_payload


def test_success_bridge_rejects_blocked_no_auth_report() -> None:
    from scoutflow_api.external_tools.bbdown_info_parser import parse_bbdown_info_output
    from scoutflow_api.metadata_probe_receipt_bridge import (
        MetadataProbeEvidenceSource,
        prepare_success_metadata_probe_assets,
    )

    parsed = parse_bbdown_info_output(read_fixture("info_public_ok_sanitized.txt"))
    source = MetadataProbeEvidenceSource(
        task_id="T-P1A-011",
        report_path="docs/research/t-p1a-011-bbdown-noauth-info-probe-report-2026-05-03.md",
        probe_mode="no-auth",
    )

    with pytest.raises(ValueError, match="T-P1A-011C"):
        prepare_success_metadata_probe_assets(
            parsed=parsed,
            source_url="https://www.bilibili.com/video/BV19D9eB9Etg",
            evidence_source=source,
        )


def test_success_bridge_receipt_candidate_labels_auth_present_source(tmp_path: Path) -> None:
    from scoutflow_api.external_tools.bbdown_info_parser import parse_bbdown_info_output
    from scoutflow_api.metadata_probe_receipt_bridge import (
        MetadataProbeEvidenceSource,
        build_metadata_fetch_receipt,
        materialize_metadata_probe_assets,
        prepare_success_metadata_probe_assets,
    )

    parsed = parse_bbdown_info_output(read_fixture("info_public_ok_sanitized.txt"))
    source = MetadataProbeEvidenceSource(
        task_id="T-P1A-011C",
        report_path="docs/research/t-p1a-011c-bbdown-auth-present-info-probe-report-2026-05-04.md",
        probe_mode="auth-present",
    )
    prepared_assets = prepare_success_metadata_probe_assets(
        parsed=parsed,
        source_url="https://www.bilibili.com/video/BV19D9eB9Etg",
        evidence_source=source,
    )
    materialized_assets = materialize_metadata_probe_assets(
        artifacts_root=tmp_path,
        capture_id="capture-1",
        assets=list(prepared_assets),
    )

    receipt = build_metadata_fetch_receipt(
        capture_id="capture-1",
        job_id="job-metadata-1",
        dedupe_key="bilibili:BV19D9eB9Etg:metadata_fetch",
        source_url="https://www.bilibili.com/video/BV19D9eB9Etg",
        evidence_source=source,
        materialized_assets=materialized_assets,
    )

    assert receipt.platform_result.value == "ok"
    assert receipt.next_status == "metadata_fetched"
    assert {asset.artifact_kind for asset in receipt.produced_assets} == {
        "safe_metadata_evidence",
        "metadata_probe_summary",
    }
    assert all(asset.evidence_source_task_id == "T-P1A-011C" for asset in receipt.produced_assets)
    assert all(asset.probe_mode == "auth-present" for asset in receipt.produced_assets)


@pytest.mark.parametrize(
    "relative_path",
    (
        "../outside.json",
        "/bundle/absolute.json",
        "bundle/../escape.json",
        "logs/not-allowed.json",
    ),
)
def test_materialize_metadata_probe_assets_rejects_unsafe_paths(tmp_path: Path, relative_path: str) -> None:
    from scoutflow_api.metadata_probe_receipt_bridge import (
        PreparedMetadataProbeAsset,
        materialize_metadata_probe_assets,
    )

    asset = PreparedMetadataProbeAsset(
        artifact_kind="safe_metadata_evidence",
        relative_path=relative_path,
        content_bytes=b"{}",
        mime_type="application/json",
        is_raw_evidence=True,
        is_derived=False,
    )

    with pytest.raises(ValueError):
        materialize_metadata_probe_assets(
            artifacts_root=tmp_path,
            capture_id="capture-1",
            assets=[asset],
        )


def test_materialize_metadata_probe_assets_does_not_write_outside_capture_root(tmp_path: Path) -> None:
    from scoutflow_api.metadata_probe_receipt_bridge import (
        PreparedMetadataProbeAsset,
        materialize_metadata_probe_assets,
    )

    capture_root = tmp_path / "bilibili" / "capture-1"
    outside_target = tmp_path / "escape.json"
    asset = PreparedMetadataProbeAsset(
        artifact_kind="safe_metadata_evidence",
        relative_path="bundle/../../escape.json",
        content_bytes=b'{"unsafe":true}',
        mime_type="application/json",
        is_raw_evidence=True,
        is_derived=False,
    )

    with pytest.raises(ValueError):
        materialize_metadata_probe_assets(
            artifacts_root=tmp_path,
            capture_id="capture-1",
            assets=[asset],
        )

    assert not outside_target.exists()
    assert not capture_root.exists()
