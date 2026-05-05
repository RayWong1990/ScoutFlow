from __future__ import annotations

from datetime import date

from scoutflow_api.bridge.schemas import BridgeErrorCode
from scoutflow_api.vault.schemas import VaultFrontmatter
from scoutflow_api.vault.writer import DEFAULT_FRONTMATTER_STATUS, DEFAULT_FRONTMATTER_TAGS, VaultWriterError


def _ensure_single_line(value: str, field_name: str) -> str:
    normalized = value.strip()
    if not normalized or "\n" in normalized or "\r" in normalized:
        raise VaultWriterError(
            BridgeErrorCode.frontmatter_invalid,
            f"{field_name} must be a single-line non-empty string.",
        )
    return normalized


def build_frontmatter(
    title: str,
    *,
    date_value: str,
    tags: str = DEFAULT_FRONTMATTER_TAGS,
    status: str = DEFAULT_FRONTMATTER_STATUS,
) -> VaultFrontmatter:
    clean_title = _ensure_single_line(title, "title")
    clean_tags = _ensure_single_line(tags, "tags")
    clean_status = _ensure_single_line(status, "status")

    try:
        normalized_date = date.fromisoformat(date_value).isoformat()
    except ValueError as exc:
        raise VaultWriterError(
            BridgeErrorCode.frontmatter_invalid,
            "date must use YYYY-MM-DD format.",
        ) from exc

    if clean_status != DEFAULT_FRONTMATTER_STATUS:
        raise VaultWriterError(
            BridgeErrorCode.frontmatter_invalid,
            f"status must stay {DEFAULT_FRONTMATTER_STATUS!r} in the raw 4-field contract.",
        )

    return VaultFrontmatter(
        title=clean_title,
        date=normalized_date,
        tags=clean_tags,
        status=clean_status,
    )


def frontmatter_as_markdown(frontmatter: VaultFrontmatter) -> str:
    return "\n".join(
        [
            "---",
            f'title: "{frontmatter.title}"',
            f"date: {frontmatter.date}",
            f"tags: {frontmatter.tags}",
            f"status: {frontmatter.status}",
            "---",
        ]
    )
