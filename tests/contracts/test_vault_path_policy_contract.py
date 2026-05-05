from __future__ import annotations

import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]
API_ROOT = ROOT / "services" / "api"
if str(API_ROOT) not in sys.path:
    sys.path.insert(0, str(API_ROOT))


def test_slugify_title_normalizes_preview_filename_fragment() -> None:
    from scoutflow_api.vault.path_policy import slugify_title

    assert slugify_title("ScoutFlow BV1xx411c7mD") == "scoutflow-bv1xx411c7md"
    assert slugify_title("  ") == "capture"


def test_resolve_inbox_target_path_stays_under_00_inbox(tmp_path: Path) -> None:
    from scoutflow_api.vault.path_policy import resolve_inbox_root, resolve_inbox_target_path

    vault_root = tmp_path / "vault"
    target = resolve_inbox_target_path(vault_root, "cap_123", "ScoutFlow BV1xx411c7mD")

    assert target == resolve_inbox_root(vault_root) / "scoutflow-cap_123-scoutflow-bv1xx411c7md.md"
    assert target.parts[-2] == "00-Inbox"


def test_resolve_inbox_target_path_blocks_capture_id_escape(tmp_path: Path) -> None:
    from scoutflow_api.bridge.schemas import BridgeErrorCode
    from scoutflow_api.vault.path_policy import resolve_inbox_target_path
    from scoutflow_api.vault.writer import VaultWriterError

    with pytest.raises(VaultWriterError) as excinfo:
        resolve_inbox_target_path(tmp_path / "vault", "../cap_123", "title")

    assert excinfo.value.code is BridgeErrorCode.path_escape_blocked


def test_resolve_inbox_target_path_blocks_resolved_escape(tmp_path: Path) -> None:
    from scoutflow_api.bridge.schemas import BridgeErrorCode
    from scoutflow_api.vault.path_policy import resolve_inbox_target_path
    from scoutflow_api.vault.writer import VaultWriterError

    with pytest.raises(VaultWriterError) as excinfo:
        resolve_inbox_target_path(
            tmp_path / "vault",
            "cap_123",
            "../../outside",
            slug_is_normalized=True,
        )

    assert excinfo.value.code is BridgeErrorCode.path_escape_blocked
