from __future__ import annotations

from importlib import import_module
from typing import Any

from scoutflow_api.vault.schemas import (
    VaultCommitCandidateV1,
    VaultCommitDryRun,
    VaultFrontmatter,
    VaultPreviewDraft,
    VaultWriterPolicy,
)
from scoutflow_api.vault.writer import (
    DEFAULT_FRONTMATTER_STATUS,
    DEFAULT_FRONTMATTER_TAGS,
    RAW_FRONTMATTER_MODE,
    SCOUTFLOW_VAULT_ROOT_ENV,
    VAULT_INBOX_DIR,
    VaultWriterError,
    build_writer_policy,
    resolve_required_vault_root,
)


_LAZY_EXPORTS = {
    "build_commit_candidate_from_preview": ("scoutflow_api.vault.commit", "build_commit_candidate_from_preview"),
    "build_commit_dry_run": ("scoutflow_api.vault.commit", "build_commit_dry_run"),
    "build_frontmatter": ("scoutflow_api.vault.frontmatter", "build_frontmatter"),
    "build_preview_markdown": ("scoutflow_api.vault.renderer", "build_preview_markdown"),
    "build_secret_scan_report": ("scoutflow_api.vault.secret_scan", "build_secret_scan_report"),
    "resolve_inbox_target_path": ("scoutflow_api.vault.path_policy", "resolve_inbox_target_path"),
}


def __getattr__(name: str) -> Any:
    if name not in _LAZY_EXPORTS:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    module_name, attr_name = _LAZY_EXPORTS[name]
    module = import_module(module_name)
    value = getattr(module, attr_name)
    globals()[name] = value
    return value


__all__ = [
    "DEFAULT_FRONTMATTER_STATUS",
    "DEFAULT_FRONTMATTER_TAGS",
    "RAW_FRONTMATTER_MODE",
    "SCOUTFLOW_VAULT_ROOT_ENV",
    "VAULT_INBOX_DIR",
    "VaultCommitCandidateV1",
    "VaultCommitDryRun",
    "VaultFrontmatter",
    "VaultPreviewDraft",
    "VaultWriterError",
    "VaultWriterPolicy",
    "build_commit_candidate_from_preview",
    "build_commit_dry_run",
    "build_frontmatter",
    "build_preview_markdown",
    "build_secret_scan_report",
    "build_writer_policy",
    "resolve_inbox_target_path",
    "resolve_required_vault_root",
]
