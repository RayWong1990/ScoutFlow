from __future__ import annotations

from enum import StrEnum


class BridgeErrorCode(StrEnum):
    bridge_not_implemented = "bridge_not_implemented"
    vault_root_unset = "vault_root_unset"
    capture_not_found = "capture_not_found"
    capture_state_blocked = "capture_state_blocked"
    metadata_missing = "metadata_missing"
    frontmatter_invalid = "frontmatter_invalid"
    path_escape_blocked = "path_escape_blocked"
    write_disabled = "write_disabled"
