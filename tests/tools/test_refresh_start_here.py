from __future__ import annotations

import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "tools" / "refresh-start-here.py"
SPEC = importlib.util.spec_from_file_location("refresh_start_here_for_tests", MODULE_PATH)
assert SPEC is not None
assert SPEC.loader is not None
refresh_start_here = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = refresh_start_here
SPEC.loader.exec_module(refresh_start_here)


def test_compute_next_forced_refresh_keeps_future_threshold() -> None:
    assert refresh_start_here.compute_next_forced_refresh(244, 300, 50) == 300


def test_compute_next_forced_refresh_bumps_after_threshold() -> None:
    assert refresh_start_here.compute_next_forced_refresh(300, 300, 50) == 350
    assert refresh_start_here.compute_next_forced_refresh(351, 300, 50) == 400


def test_render_anchor_block_uses_live_values() -> None:
    context = refresh_start_here.RefreshContext(
        commits=[
            refresh_start_here.GitCommit("e207664", "docs: baseline (#244)", 244),
            refresh_start_here.GitCommit("e1deda6", "feat: shell (#243)", 243),
            refresh_start_here.GitCommit("00917fe", "feat: closeout (#242)", 242),
        ],
        checkpoint_dispatch_total=38,
        strategic_markdown_count="895",
        strategic_word_count="1,479,998",
        refresh_interval_pr=50,
        next_forced_refresh_pr=300,
        last_updated="2026-05-07",
    )

    block = refresh_start_here.render_anchor_block(context)

    assert "`e207664` (PR #244) ← `e1deda6` (PR #243) ← `00917fe` (PR #242)" in block
    assert "`38`" in block
    assert "`895 markdown / 1,479,998 字`" in block


def test_refresh_text_updates_anchor_block_and_threshold() -> None:
    source = """---
title: Demo
status: current authority
last_updated: 2026-05-06
refresh_interval_pr: 50
next_forced_refresh_pr: 300
last_refreshed_from_main_pr: 243
last_refreshed_from_main_sha: e1deda6
---

## §1 当前真态锚点

<!-- START_HERE_AUTO_ANCHORS_BEGIN -->
old
<!-- START_HERE_AUTO_ANCHORS_END -->
"""
    context = refresh_start_here.RefreshContext(
        commits=[
            refresh_start_here.GitCommit("300abcd", "docs: refresh (#300)", 300),
            refresh_start_here.GitCommit("244abcd", "docs: baseline (#244)", 244),
            refresh_start_here.GitCommit("243abcd", "feat: shell (#243)", 243),
        ],
        checkpoint_dispatch_total=38,
        strategic_markdown_count="895",
        strategic_word_count="1,479,998",
        refresh_interval_pr=50,
        next_forced_refresh_pr=300,
        last_updated="2026-05-08",
    )

    refreshed = refresh_start_here.refresh_text(source, context)

    assert "next_forced_refresh_pr: 350" in refreshed
    assert "last_refreshed_from_main_pr: 300" in refreshed
    assert "last_refreshed_from_main_sha: 300abcd" in refreshed
    assert "old" not in refreshed
    assert "`300abcd` (PR #300)" in refreshed
