from __future__ import annotations

import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]
API_ROOT = ROOT / "services" / "api"
if str(API_ROOT) not in sys.path:
    sys.path.insert(0, str(API_ROOT))


def test_vault_package_exports_scaffold_contract() -> None:
    from scoutflow_api.vault import __all__

    expected = {
        "SCOUTFLOW_VAULT_ROOT_ENV",
        "VAULT_INBOX_DIR",
        "RAW_FRONTMATTER_MODE",
        "DEFAULT_FRONTMATTER_TAGS",
        "DEFAULT_FRONTMATTER_STATUS",
        "VaultCommitCandidateV1",
        "VaultWriterError",
        "VaultWriterPolicy",
        "VaultFrontmatter",
        "VaultPreviewDraft",
        "VaultCommitDryRun",
        "build_commit_candidate_from_preview",
        "build_writer_policy",
        "resolve_required_vault_root",
        "resolve_inbox_target_path",
        "build_frontmatter",
        "build_preview_markdown",
        "build_secret_scan_report",
        "build_commit_dry_run",
    }

    assert expected.issubset(set(__all__))


def test_writer_policy_defaults_to_dry_run_and_inbox_only(tmp_path: Path) -> None:
    from scoutflow_api.vault import (
        DEFAULT_FRONTMATTER_STATUS,
        DEFAULT_FRONTMATTER_TAGS,
        RAW_FRONTMATTER_MODE,
        SCOUTFLOW_VAULT_ROOT_ENV,
        VAULT_INBOX_DIR,
        build_writer_policy,
    )

    policy = build_writer_policy({SCOUTFLOW_VAULT_ROOT_ENV: str(tmp_path / "vault")})

    assert policy.vault_root == str(tmp_path / "vault")
    assert policy.inbox_dir == "00-Inbox"
    assert policy.frontmatter_mode == "raw_4_field"
    assert policy.dry_run is True
    assert policy.write_enabled is False
    assert VAULT_INBOX_DIR == "00-Inbox"
    assert RAW_FRONTMATTER_MODE == "raw_4_field"
    assert DEFAULT_FRONTMATTER_TAGS == "调研/ScoutFlow采集"
    assert DEFAULT_FRONTMATTER_STATUS == "pending"


def test_writer_root_is_fail_loud_when_env_missing() -> None:
    from scoutflow_api.bridge.schemas import BridgeErrorCode
    from scoutflow_api.vault import resolve_required_vault_root
    from scoutflow_api.vault.writer import VaultWriterError

    with pytest.raises(VaultWriterError) as excinfo:
        resolve_required_vault_root({})

    assert excinfo.value.code is BridgeErrorCode.vault_root_unset
    assert "SCOUTFLOW_VAULT_ROOT" in excinfo.value.message


def test_scaffold_models_lock_frontmatter_and_commit_defaults() -> None:
    from scoutflow_api.vault import VaultFrontmatter, VaultPreviewDraft
    from scoutflow_api.vault.commit import build_commit_dry_run_from_preview

    frontmatter = VaultFrontmatter(
        title="ScoutFlow BV1xx411c7mD",
        date="2026-05-05",
        tags="调研/ScoutFlow采集",
        status="pending",
    )
    preview = VaultPreviewDraft(
        capture_id="cap_123",
        target_path="/tmp/scoutflow-vault/00-Inbox/scoutflow-cap_123-bv1xx411c7md.md",
        frontmatter=frontmatter,
        body_markdown="# ScoutFlow BV1xx411c7mD",
    )
    commit = build_commit_dry_run_from_preview(preview)

    assert preview.frontmatter.status == "pending"
    assert preview.warnings == []
    assert commit.dry_run is True
    assert commit.committed is False
    assert commit.write_enabled is False
    assert commit.candidate.spec_version == "VaultCommitCandidateV1"
