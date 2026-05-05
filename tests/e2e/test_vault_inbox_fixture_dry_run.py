from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
API_ROOT = ROOT / "services" / "api"
EXPECTED_NOTE_PATH = ROOT / "tests" / "fixtures" / "vault_inbox" / "expected_scoutflow_note.md"
if str(API_ROOT) not in sys.path:
    sys.path.insert(0, str(API_ROOT))


def test_vault_inbox_fixture_matches_current_helper_stack(tmp_path: Path) -> None:
    from scoutflow_api.vault.commit import build_commit_dry_run
    from scoutflow_api.vault.frontmatter import frontmatter_as_markdown
    from scoutflow_api.vault.renderer import build_preview_draft

    capture = {
        "capture_id": "cap_placeholder",
        "platform_item_id": "BV1PLACEHOLDER",
        "canonical_url": "https://www.bilibili.com/video/BV1PLACEHOLDER",
        "created_at": "2026-05-05T08:30:00+00:00",
    }
    preview = build_preview_draft(capture, tmp_path / "vault")
    commit = build_commit_dry_run(capture, tmp_path / "vault")

    rendered_note = "\n".join(
        [
            frontmatter_as_markdown(preview.frontmatter),
            "",
            preview.body_markdown,
        ]
    )
    expected_note = EXPECTED_NOTE_PATH.read_text(encoding="utf-8").strip()

    assert commit.target_path == preview.target_path
    assert commit.dry_run is True
    assert commit.committed is False
    assert rendered_note.strip() == expected_note
