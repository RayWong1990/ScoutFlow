from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
API_ROOT = ROOT / "services" / "api"
COMPONENT_PATH = ROOT / "apps" / "capture-station" / "src" / "features" / "vault-commit" / "VaultCommitDryRunButton.tsx"
if str(API_ROOT) not in sys.path:
    sys.path.insert(0, str(API_ROOT))


def test_vault_commit_placeholder_surface_tracks_dry_run_contract(tmp_path: Path) -> None:
    from scoutflow_api.vault.commit import WRITE_DISABLED_MESSAGE, build_commit_dry_run

    component_source = COMPONENT_PATH.read_text(encoding="utf-8")
    commit = build_commit_dry_run(
        {
            "capture_id": "cap_placeholder",
            "platform_item_id": "BV1PLACEHOLDER",
            "canonical_url": "https://www.bilibili.com/video/BV1PLACEHOLDER",
            "created_at": "2026-05-05T08:30:00+00:00",
        },
        tmp_path / "vault",
    )

    assert "data-testid=\"panel-vault-commit\"" in component_source
    assert "dry-run only" in component_source
    assert "Commit to vault (disabled)" in component_source
    assert "dry_run: true" in component_source
    assert "commit.dry_run" in component_source
    assert "committed" in component_source
    assert "write_disabled" in component_source
    assert commit.dry_run is True
    assert commit.committed is False
    assert commit.write_enabled is False
    assert commit.target_path and commit.target_path.endswith("/00-Inbox/scoutflow-cap_placeholder-bv1placeholder.md")
    assert "Bridge write path is not approved in the current phase." == WRITE_DISABLED_MESSAGE
