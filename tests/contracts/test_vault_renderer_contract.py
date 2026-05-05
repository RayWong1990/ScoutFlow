from __future__ import annotations

import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]
API_ROOT = ROOT / "services" / "api"
if str(API_ROOT) not in sys.path:
    sys.path.insert(0, str(API_ROOT))


def test_build_preview_draft_uses_capture_truth_and_created_at_date(tmp_path: Path) -> None:
    from scoutflow_api.vault.renderer import build_preview_draft

    draft = build_preview_draft(
        {
            "capture_id": "cap_123",
            "platform_item_id": "BV1xx411c7mD",
            "canonical_url": "https://www.bilibili.com/video/BV1xx411c7mD",
            "created_at": "2026-05-05T08:30:00+00:00",
        },
        tmp_path / "vault",
    )

    assert draft.capture_id == "cap_123"
    assert draft.target_path.endswith("/00-Inbox/scoutflow-cap_123-bv1xx411c7md.md")
    assert draft.frontmatter.date == "2026-05-05"
    assert "canonical_url" in draft.body_markdown


def test_build_preview_draft_rejects_missing_capture_fields(tmp_path: Path) -> None:
    from scoutflow_api.bridge.schemas import BridgeErrorCode
    from scoutflow_api.vault.renderer import build_preview_draft
    from scoutflow_api.vault.writer import VaultWriterError

    with pytest.raises(VaultWriterError) as excinfo:
        build_preview_draft(
            {
                "capture_id": "cap_123",
                "platform_item_id": "BV1xx411c7mD",
                "created_at": "2026-05-05T08:30:00+00:00",
            },
            tmp_path / "vault",
        )

    assert excinfo.value.code is BridgeErrorCode.metadata_missing


def test_build_preview_draft_rejects_bad_created_at(tmp_path: Path) -> None:
    from scoutflow_api.bridge.schemas import BridgeErrorCode
    from scoutflow_api.vault.renderer import build_preview_draft
    from scoutflow_api.vault.writer import VaultWriterError

    with pytest.raises(VaultWriterError) as excinfo:
        build_preview_draft(
            {
                "capture_id": "cap_123",
                "platform_item_id": "BV1xx411c7mD",
                "canonical_url": "https://www.bilibili.com/video/BV1xx411c7mD",
                "created_at": "2026/05/05",
            },
            tmp_path / "vault",
        )

    assert excinfo.value.code is BridgeErrorCode.frontmatter_invalid


def test_build_preview_markdown_matches_existing_bridge_wording() -> None:
    from scoutflow_api.vault.renderer import build_preview_markdown

    body = build_preview_markdown(
        "cap_123",
        "BV1xx411c7mD",
        "https://www.bilibili.com/video/BV1xx411c7mD",
    )

    assert body == "\n".join(
        [
            "# ScoutFlow BV1xx411c7mD",
            "",
            "- capture_id: `cap_123`",
            "- platform_item_id: `BV1xx411c7mD`",
            "- canonical_url: https://www.bilibili.com/video/BV1xx411c7mD",
            "",
            "Raw markdown candidate generated from existing capture truth only.",
        ]
    )
