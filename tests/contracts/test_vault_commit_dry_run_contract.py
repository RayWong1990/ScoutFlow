from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
API_ROOT = ROOT / "services" / "api"
if str(API_ROOT) not in sys.path:
    sys.path.insert(0, str(API_ROOT))


def test_build_commit_dry_run_from_preview_stays_write_disabled() -> None:
    from scoutflow_api.vault.commit import build_commit_dry_run_from_preview
    from scoutflow_api.vault.schemas import VaultFrontmatter, VaultPreviewDraft

    preview = VaultPreviewDraft(
        capture_id="cap_123",
        target_path="/tmp/scoutflow-vault/00-Inbox/scoutflow-cap_123-bv1xx411c7md.md",
        frontmatter=VaultFrontmatter(
            title="ScoutFlow BV1xx411c7mD",
            date="2026-05-05",
            tags="调研/ScoutFlow采集",
            status="pending",
        ),
        body_markdown="# ScoutFlow BV1xx411c7mD",
    )
    commit = build_commit_dry_run_from_preview(preview)

    assert commit.capture_id == "cap_123"
    assert commit.target_path == preview.target_path
    assert commit.dry_run is True
    assert commit.committed is False
    assert commit.write_enabled is False
    assert commit.candidate.spec_version == "VaultCommitCandidateV1"
    assert len(commit.candidate.roles) == 12


def test_build_commit_dry_run_reuses_preview_target_path(tmp_path: Path) -> None:
    from scoutflow_api.vault.commit import build_commit_dry_run

    commit = build_commit_dry_run(
        {
            "capture_id": "cap_123",
            "platform_item_id": "BV1xx411c7mD",
            "canonical_url": "https://www.bilibili.com/video/BV1xx411c7mD",
            "created_at": "2026-05-05T08:30:00+00:00",
        },
        tmp_path / "vault",
    )

    assert commit.target_path == str(tmp_path / "vault" / "00-Inbox" / "scoutflow-cap_123-bv1xx411c7md.md")
    assert commit.write_enabled is False
    assert commit.candidate.path_containment.contained_within_allowed_root is True


def test_render_commit_ledger_markdown_matches_gate_message(tmp_path: Path) -> None:
    from scoutflow_api.vault.commit import WRITE_DISABLED_MESSAGE, build_commit_dry_run, render_commit_ledger_markdown

    commit = build_commit_dry_run(
        {
            "capture_id": "cap_123",
            "platform_item_id": "BV1xx411c7mD",
            "canonical_url": "https://www.bilibili.com/video/BV1xx411c7mD",
            "created_at": "2026-05-05T08:30:00+00:00",
        },
        tmp_path / "vault",
    )
    markdown = render_commit_ledger_markdown(commit)

    assert WRITE_DISABLED_MESSAGE in markdown
    assert "- dry_run: `true`" in markdown
    assert "- committed: `false`" in markdown
    assert "- candidate_spec: `VaultCommitCandidateV1`" in markdown
