from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
API_ROOT = ROOT / "services" / "api"
FIXTURE_PATH = ROOT / "tests" / "fixtures" / "walking_skeleton" / "placeholder_metadata.json"
if str(API_ROOT) not in sys.path:
    sys.path.insert(0, str(API_ROOT))


def _load_fixture() -> dict[str, str]:
    return json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))


def test_placeholder_fixture_is_safe_input_for_vault_preview(tmp_path: Path) -> None:
    from scoutflow_api.vault.renderer import build_preview_draft

    fixture = _load_fixture()
    draft = build_preview_draft(fixture, tmp_path / "vault")

    assert draft.capture_id == fixture["capture_id"]
    assert draft.frontmatter.date == "2026-05-05"
    assert draft.target_path.endswith("/00-Inbox/scoutflow-cap_placeholder-bv1placeholder.md")
    assert "Raw markdown candidate generated from existing capture truth only." in draft.body_markdown


def test_placeholder_fixture_omits_runtime_and_raw_output_fields() -> None:
    fixture = _load_fixture()
    forbidden_keys = {
        "stdout_text",
        "stderr_text",
        "audio_transcript",
        "download_url",
        "media_path",
        "ffmpeg_log",
    }

    assert fixture["source_kind"] == "manual_url"
    assert fixture["capture_mode"] == "metadata_only"
    assert fixture["status"] == "metadata_fetched"
    assert fixture["frontmatter_mode"] == "raw_4_field"
    assert forbidden_keys.isdisjoint(fixture)
