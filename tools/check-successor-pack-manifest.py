#!/usr/bin/env python3
"""Validate successor-pack dispatch metadata shape for post-frozen packs."""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PACK_ROOT = ROOT / "docs" / "research" / "post-frozen" / "80-pack-source" / "02_task_packs"
DISPATCH_FILES = sorted(PACK_ROOT.glob("**/dispatches/*.md"))
EXPECTED_COUNT = 80

REQUIRED_FRONTMATTER_KEYS = [
    "cluster",
    "proof_kind",
    "open_after_state",
    "human_gate",
]

REQUIRED_SECTION_PREFIXES = [
    "## 0",
    "## 2",
    "## 4",
    "## 8",
]


def split_frontmatter(text: str) -> tuple[str, str]:
    marker = "```yaml\n"
    if marker not in text:
        raise ValueError("missing yaml code fence")
    _, rest = text.split(marker, 1)
    if "\n```" not in rest:
        raise ValueError("missing closing yaml code fence")
    frontmatter, body = rest.split("\n```", 1)
    return frontmatter, body


def validate_dispatch(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")

    try:
        frontmatter, body = split_frontmatter(text)
    except ValueError as exc:
        return [f"{path}: {exc}"]

    is_deprecated = re.search(
        r"^status:\s+deprecated_by_PF_META_01", frontmatter, re.MULTILINE
    )

    if not is_deprecated:
        for key in REQUIRED_FRONTMATTER_KEYS:
            if not re.search(rf"^{re.escape(key)}:\s+\S+", frontmatter, re.MULTILINE):
                errors.append(f"{path}: missing frontmatter key `{key}`")

    for prefix in REQUIRED_SECTION_PREFIXES:
        if prefix not in body:
            errors.append(f"{path}: missing section prefix `{prefix}`")

    blocked_claim_markers = [
        "no_true_vault_write",
        "no_runtime_approval",
        "Inherits `_PACK-DEFAULTS.md`",
        "## 6. Blocked claims that remain blocked",
        "## 0/5/6/7/9/10/11. Shared clauses",
    ]
    if not any(marker in body for marker in blocked_claim_markers):
        errors.append(f"{path}: missing blocked-claims marker or shared-clause inheritance note")

    return errors


def main() -> int:
    errors: list[str] = []

    if len(DISPATCH_FILES) != EXPECTED_COUNT:
        errors.append(
            f"dispatch count mismatch: expected {EXPECTED_COUNT}, got {len(DISPATCH_FILES)}"
        )

    for path in DISPATCH_FILES:
        errors.extend(validate_dispatch(path))

    if errors:
        for error in errors:
            print(error)
        return 1

    print(f"OK: validated {len(DISPATCH_FILES)} dispatch files under {PACK_ROOT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
