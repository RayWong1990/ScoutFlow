from __future__ import annotations

import re
from pathlib import Path

from scoutflow_api.bridge.error_codes import BridgeErrorCode
from scoutflow_api.vault.writer import VAULT_INBOX_DIR, VaultWriterError


SLUG_RE = re.compile(r"[^a-z0-9]+")


def slugify_title(value: str) -> str:
    lowered = value.lower()
    normalized = SLUG_RE.sub("-", lowered).strip("-")
    return normalized or "capture"


def resolve_inbox_root(vault_root: str | Path) -> Path:
    return Path(vault_root).expanduser().resolve() / VAULT_INBOX_DIR


def _assert_capture_id_safe(capture_id: str) -> None:
    if not capture_id or any(char in capture_id for char in ("/", "\\")) or ".." in capture_id:
        raise VaultWriterError(
            BridgeErrorCode.path_escape_blocked,
            "capture_id contains path-unsafe fragments.",
        )


def _assert_slug_safe(slug: str) -> None:
    if not slug or any(char in slug for char in ("/", "\\")) or ".." in slug:
        raise VaultWriterError(
            BridgeErrorCode.path_escape_blocked,
            "slug contains path-unsafe fragments.",
        )


def assert_target_within_inbox(inbox_root: Path, target_path: Path) -> Path:
    resolved_inbox = inbox_root.resolve()
    resolved_target = target_path.resolve(strict=False)
    try:
        resolved_target.relative_to(resolved_inbox)
    except ValueError as exc:
        raise VaultWriterError(
            BridgeErrorCode.path_escape_blocked,
            "Resolved target path escaped the allowed 00-Inbox subtree.",
        ) from exc
    return resolved_target


def resolve_inbox_target_path(
    vault_root: str | Path,
    capture_id: str,
    title_or_slug: str,
    *,
    slug_is_normalized: bool = False,
) -> Path:
    _assert_capture_id_safe(capture_id)
    inbox_root = resolve_inbox_root(vault_root)
    slug = title_or_slug if slug_is_normalized else slugify_title(title_or_slug)
    if slug_is_normalized:
        _assert_slug_safe(slug)
    target_path = inbox_root / f"scoutflow-{capture_id}-{slug}.md"
    return assert_target_within_inbox(inbox_root, target_path)
