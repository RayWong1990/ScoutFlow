from __future__ import annotations

from collections.abc import Mapping
from datetime import datetime
from pathlib import Path
from typing import Any

from scoutflow_api.bridge.schemas import BridgeErrorCode
from scoutflow_api.vault.frontmatter import build_frontmatter
from scoutflow_api.vault.path_policy import resolve_inbox_target_path
from scoutflow_api.vault.schemas import VaultPreviewDraft
from scoutflow_api.vault.writer import VaultWriterError


def _require_capture_field(capture: Mapping[str, Any], field_name: str) -> str:
    value = capture.get(field_name)
    if value is None:
        raise VaultWriterError(
            BridgeErrorCode.metadata_missing,
            f"capture is missing required field {field_name!r}.",
        )
    normalized = str(value).strip()
    if not normalized:
        raise VaultWriterError(
            BridgeErrorCode.metadata_missing,
            f"capture field {field_name!r} must not be empty.",
        )
    return normalized


def build_preview_title(platform_item_id: str) -> str:
    return f"ScoutFlow {platform_item_id}"


def preview_date_from_capture(created_at: str) -> str:
    try:
        normalized = created_at.replace("Z", "+00:00")
        return datetime.fromisoformat(normalized).date().isoformat()
    except ValueError as exc:
        raise VaultWriterError(
            BridgeErrorCode.frontmatter_invalid,
            "capture created_at must be a valid ISO timestamp.",
        ) from exc


def build_preview_markdown(capture_id: str, platform_item_id: str, canonical_url: str) -> str:
    title = build_preview_title(platform_item_id)
    return "\n".join(
        [
            f"# {title}",
            "",
            f"- capture_id: `{capture_id}`",
            f"- platform_item_id: `{platform_item_id}`",
            f"- canonical_url: {canonical_url}",
            "",
            "Raw markdown candidate generated from existing capture truth only.",
        ]
    )


def build_preview_draft(capture: Mapping[str, Any], vault_root: str | Path) -> VaultPreviewDraft:
    capture_id = _require_capture_field(capture, "capture_id")
    platform_item_id = _require_capture_field(capture, "platform_item_id")
    canonical_url = _require_capture_field(capture, "canonical_url")
    created_at = _require_capture_field(capture, "created_at")

    target_path = str(resolve_inbox_target_path(vault_root, capture_id, platform_item_id))
    frontmatter = build_frontmatter(
        build_preview_title(platform_item_id),
        date_value=preview_date_from_capture(created_at),
    )
    return VaultPreviewDraft(
        capture_id=capture_id,
        target_path=target_path,
        frontmatter=frontmatter,
        body_markdown=build_preview_markdown(capture_id, platform_item_id, canonical_url),
        warnings=[],
    )
