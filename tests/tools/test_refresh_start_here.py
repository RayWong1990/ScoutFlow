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


def test_pr_number_for_commit_uses_squash_commit_override() -> None:
    assert refresh_start_here.pr_number_for_commit("5902ecf", "governance: repair memory taxonomy and W2C truth guards") == 261


def test_parse_pr_number_supports_github_merge_commit_subject() -> None:
    assert refresh_start_here.parse_pr_number("Merge pull request #273 from owner/branch") == 273


def test_resolve_target_ref_keeps_check_main_mode_on_origin_main_with_explicit_head_ref() -> None:
    assert (
        refresh_start_here.resolve_target_ref(explicit_ref="HEAD", branch_name="codex/fix-branch", check_mode=True)
        == "origin/main"
    )


def test_resolve_target_ref_can_render_explicit_head_ref_in_head_check_mode() -> None:
    assert (
        refresh_start_here.resolve_target_ref(
            explicit_ref="HEAD",
            branch_name="codex/fix-branch",
            check_mode=True,
            check_anchor_mode="head",
        )
        == "HEAD"
    )


def test_resolve_target_ref_prefers_explicit_merge_ref_in_head_check_mode() -> None:
    assert (
        refresh_start_here.resolve_target_ref(
            explicit_ref="refs/pull/261/merge",
            branch_name="codex/fix-branch",
            check_mode=True,
            check_anchor_mode="head",
        )
        == "refs/pull/261/merge"
    )


def test_resolve_target_ref_uses_origin_main_by_default() -> None:
    assert refresh_start_here.resolve_target_ref(explicit_ref=None, branch_name="main", check_mode=False) == "origin/main"


def test_render_anchor_block_uses_live_values() -> None:
    context = refresh_start_here.RefreshContext(
        target_ref="origin/main",
        commits=[
            refresh_start_here.GitCommit("e207664", "docs: baseline (#244)", 244),
            refresh_start_here.GitCommit("e1deda6", "feat: shell (#243)", 243),
            refresh_start_here.GitCommit("00917fe", "feat: closeout (#242)", 242),
        ],
        current_pr_number=244,
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
        target_ref="origin/main",
        commits=[
            refresh_start_here.GitCommit("300abcd", "docs: refresh (#300)", 300),
            refresh_start_here.GitCommit("244abcd", "docs: baseline (#244)", 244),
            refresh_start_here.GitCommit("243abcd", "feat: shell (#243)", 243),
        ],
        current_pr_number=300,
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


def test_default_refresh_uses_origin_main_and_writes_main_fields() -> None:
    assert refresh_start_here.resolve_target_ref(explicit_ref=None, branch_name="feature", check_mode=False) == "origin/main"

    source = """---
title: Demo
status: current authority
last_updated: 2026-05-06
refresh_interval_pr: 50
next_forced_refresh_pr: 300
last_refreshed_from_main_pr: 259
last_refreshed_from_main_sha: 5777389
---

## §1 当前真态锚点

<!-- START_HERE_AUTO_ANCHORS_BEGIN -->
old
<!-- START_HERE_AUTO_ANCHORS_END -->
"""
    context = refresh_start_here.RefreshContext(
        target_ref="origin/main",
        commits=[
            refresh_start_here.GitCommit("5902ecf", "governance: repair memory taxonomy and W2C truth guards", 261),
            refresh_start_here.GitCommit("b1b2350", "docs(governance): close W4 tier4 merge and errata", None),
            refresh_start_here.GitCommit("5777389", "W4-E: lock lane 4 DB vNext spec to manual SQL path (#259)", 259),
        ],
        current_pr_number=261,
        checkpoint_dispatch_total=38,
        strategic_markdown_count="895",
        strategic_word_count="1,479,998",
        refresh_interval_pr=50,
        next_forced_refresh_pr=300,
        last_updated="2026-05-08",
    )

    refreshed = refresh_start_here.refresh_text(source, context)

    assert "last_refreshed_from_main_pr: 261" in refreshed
    assert "last_refreshed_from_main_sha: 5902ecf" in refreshed
    assert "| main content anchor | `5902ecf` (PR #261) ← `b1b2350` ← `5777389` (PR #259) |" in refreshed


def test_refresh_text_keeps_main_frontmatter_when_rendering_head_truth() -> None:
    source = """---
title: Demo
status: current authority
last_updated: 2026-05-06
refresh_interval_pr: 50
next_forced_refresh_pr: 300
last_refreshed_from_main_pr: 259
last_refreshed_from_main_sha: 5777389
---

## §1 当前真态锚点

<!-- START_HERE_AUTO_ANCHORS_BEGIN -->
old
<!-- START_HERE_AUTO_ANCHORS_END -->
"""
    context = refresh_start_here.RefreshContext(
        target_ref="HEAD",
        commits=[
            refresh_start_here.GitCommit("b594375", "docs(governance): close W4 tier4 merge and errata", None),
            refresh_start_here.GitCommit("5777389", "W4-E: lock lane 4 DB vNext spec to manual SQL path (#259)", 259),
            refresh_start_here.GitCommit("beb0fef", "W4-C: harden lane 2 runtime tools spec candidate (#258)", 258),
        ],
        current_pr_number=259,
        checkpoint_dispatch_total=38,
        strategic_markdown_count="895",
        strategic_word_count="1,479,998",
        refresh_interval_pr=50,
        next_forced_refresh_pr=300,
        last_updated="2026-05-08",
    )

    refreshed = refresh_start_here.refresh_text(source, context, update_main_frontmatter=False)

    assert "last_refreshed_from_main_pr: 259" in refreshed
    assert "last_refreshed_from_main_sha: 5777389" in refreshed
    assert "| checked-out content anchor | `b594375` ← `5777389` (PR #259) ← `beb0fef` (PR #258) |" in refreshed


def test_pr_synthetic_ref_check_mode_main_does_not_force_checked_out_head_label() -> None:
    assert (
        refresh_start_here.resolve_target_ref(
            explicit_ref="HEAD",
            branch_name="codex/pr262-consistency-closeout-full-repair",
            check_mode=True,
            check_anchor_mode="main",
        )
        == "origin/main"
    )


def test_render_ref_label_keeps_first_parent_as_main_content_anchor() -> None:
    assert refresh_start_here.render_ref_label("origin/main^1") == "main content anchor"


def test_refresh_text_uses_latest_merge_pr_with_stable_content_anchor() -> None:
    source = """---
title: Demo
status: current authority
last_updated: 2026-05-06
refresh_interval_pr: 50
next_forced_refresh_pr: 300
last_refreshed_from_main_pr: 272
last_refreshed_from_main_sha: 7790c36
---

## §1 当前真态锚点

<!-- START_HERE_AUTO_ANCHORS_BEGIN -->
old
<!-- START_HERE_AUTO_ANCHORS_END -->
"""
    context = refresh_start_here.RefreshContext(
        target_ref="origin/main",
        commits=[
            refresh_start_here.GitCommit("086083b", "docs(start-here): fix overflow hold summary and refresh anchor", None),
            refresh_start_here.GitCommit("7790c36", "docs(governance): promote T-P1A-160 after Lane D merge", None),
            refresh_start_here.GitCommit("e588e96", "docs(repair): add lane-d PF-V scope note for PR271", None),
        ],
        current_pr_number=273,
        checkpoint_dispatch_total=38,
        strategic_markdown_count="895",
        strategic_word_count="1,479,998",
        refresh_interval_pr=50,
        next_forced_refresh_pr=300,
        last_updated="2026-05-08",
    )

    refreshed = refresh_start_here.refresh_text(source, context)

    assert "last_refreshed_from_main_pr: 273" in refreshed
    assert "last_refreshed_from_main_sha: 086083b" in refreshed
    assert "| main content anchor | `086083b` ← `7790c36` ← `e588e96` |" in refreshed
