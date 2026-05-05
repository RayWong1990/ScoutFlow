from __future__ import annotations

import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]
API_ROOT = ROOT / "services" / "api"
if str(API_ROOT) not in sys.path:
    sys.path.insert(0, str(API_ROOT))


def test_build_frontmatter_locks_raw_four_field_shape() -> None:
    from scoutflow_api.vault.frontmatter import build_frontmatter

    frontmatter = build_frontmatter("ScoutFlow BV1xx411c7mD", date_value="2026-05-05")

    assert frontmatter.model_dump() == {
        "title": "ScoutFlow BV1xx411c7mD",
        "date": "2026-05-05",
        "tags": "调研/ScoutFlow采集",
        "status": "pending",
    }


def test_build_frontmatter_rejects_bad_date() -> None:
    from scoutflow_api.bridge.schemas import BridgeErrorCode
    from scoutflow_api.vault.frontmatter import build_frontmatter
    from scoutflow_api.vault.writer import VaultWriterError

    with pytest.raises(VaultWriterError) as excinfo:
        build_frontmatter("ScoutFlow BV1xx411c7mD", date_value="2026/05/05")

    assert excinfo.value.code is BridgeErrorCode.frontmatter_invalid


def test_build_frontmatter_rejects_non_pending_status() -> None:
    from scoutflow_api.bridge.schemas import BridgeErrorCode
    from scoutflow_api.vault.frontmatter import build_frontmatter
    from scoutflow_api.vault.writer import VaultWriterError

    with pytest.raises(VaultWriterError) as excinfo:
        build_frontmatter("ScoutFlow BV1xx411c7mD", date_value="2026-05-05", status="ready")

    assert excinfo.value.code is BridgeErrorCode.frontmatter_invalid


def test_frontmatter_as_markdown_renders_stable_yaml_block() -> None:
    from scoutflow_api.vault.frontmatter import build_frontmatter, frontmatter_as_markdown

    frontmatter = build_frontmatter("ScoutFlow BV1xx411c7mD", date_value="2026-05-05")
    markdown = frontmatter_as_markdown(frontmatter)

    assert markdown == "\n".join(
        [
            "---",
            'title: "ScoutFlow BV1xx411c7mD"',
            "date: 2026-05-05",
            "tags: 调研/ScoutFlow采集",
            "status: pending",
            "---",
        ]
    )
