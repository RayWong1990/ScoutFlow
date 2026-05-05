from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from typing import Any

from scoutflow_api.vault.renderer import build_preview_draft
from scoutflow_api.vault.schemas import VaultCommitDryRun, VaultPreviewDraft


WRITE_DISABLED_MESSAGE = "Bridge write path is not approved in the current phase."


def build_commit_dry_run_from_preview(preview: VaultPreviewDraft) -> VaultCommitDryRun:
    return VaultCommitDryRun(
        capture_id=preview.capture_id,
        target_path=preview.target_path,
    )


def build_commit_dry_run(capture: Mapping[str, Any], vault_root: str | Path) -> VaultCommitDryRun:
    preview = build_preview_draft(capture, vault_root)
    return build_commit_dry_run_from_preview(preview)


def render_commit_ledger_markdown(commit: VaultCommitDryRun) -> str:
    target_path = commit.target_path or "unset"
    return "\n".join(
        [
            "# Vault Commit Dry Run",
            "",
            f"- capture_id: `{commit.capture_id}`",
            f"- target_path: `{target_path}`",
            f"- dry_run: `{str(commit.dry_run).lower()}`",
            f"- committed: `{str(commit.committed).lower()}`",
            f"- write_enabled: `{str(commit.write_enabled).lower()}`",
            f"- gate: {WRITE_DISABLED_MESSAGE}",
        ]
    )
