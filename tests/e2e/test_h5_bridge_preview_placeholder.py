from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
API_ROOT = ROOT / "services" / "api"
FIXTURE_PATH = ROOT / "tests" / "fixtures" / "walking_skeleton" / "placeholder_metadata.json"
if str(API_ROOT) not in sys.path:
    sys.path.insert(0, str(API_ROOT))


def test_vault_preview_draft_contract_matches_placeholder_fixture(tmp_path: Path) -> None:
    from scoutflow_api.vault.renderer import build_preview_draft

    fixture_source = FIXTURE_PATH.read_text(encoding="utf-8")

    draft = build_preview_draft(
        {
            "capture_id": "cap_placeholder",
            "platform_item_id": "BV1PLACEHOLDER",
            "canonical_url": "https://www.bilibili.com/video/BV1PLACEHOLDER",
            "created_at": "2026-05-05T08:30:00+00:00"
        },
        tmp_path / "vault",
    )

    assert "BV1PLACEHOLDER" in fixture_source
    assert draft.target_path.endswith("/00-Inbox/scoutflow-cap_placeholder-bv1placeholder.md")
    assert draft.frontmatter.title == "ScoutFlow BV1PLACEHOLDER"
    assert draft.frontmatter.date == "2026-05-05"
    assert draft.frontmatter.status == "pending"
    assert "## Preview boundary" in draft.body_markdown
    assert "- preview_only: `true`" in draft.body_markdown
    assert "- write_enabled: `false`" in draft.body_markdown
    assert "- runtime_tools_enabled: `false`" in draft.body_markdown
    assert draft.warnings == []
