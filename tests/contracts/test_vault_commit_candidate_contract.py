from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
API_ROOT = ROOT / "services" / "api"
if str(API_ROOT) not in sys.path:
    sys.path.insert(0, str(API_ROOT))


def test_vault_commit_candidate_v1_locks_12_roles_and_negative_gate_shape(tmp_path: Path) -> None:
    from scoutflow_api.vault.commit import build_commit_dry_run

    fixture_path = ROOT / "tests" / "fixtures" / "vault_commit_candidate" / "expected_roles.json"
    expected_roles = json.loads(fixture_path.read_text(encoding="utf-8"))["roles"]

    commit = build_commit_dry_run(
        {
            "capture_id": "cap_123",
            "platform_item_id": "BV1xx411c7mD",
            "canonical_url": "https://www.bilibili.com/video/BV1xx411c7mD",
            "created_at": "2026-05-08T12:30:00+00:00",
            "source_kind": "manual_url",
            "capture_mode": "metadata_only",
        },
        tmp_path / "vault",
    )

    candidate = commit.candidate
    assert candidate.spec_version == "VaultCommitCandidateV1"
    assert [role.role for role in candidate.roles] == expected_roles
    assert candidate.roles[9].status.value == "held_truthfully"
    assert len(candidate.roles[10].value) == 64
    assert candidate.secret_scan.blocked is False
    assert candidate.secret_scan.matches == []
    assert len(candidate.secret_scan.surfaces_checked) == 7
    assert len(candidate.secret_scan.blocking_categories) == 9
    assert candidate.path_containment.allowed_root.endswith("/00-Inbox")
    assert candidate.path_containment.contained_within_allowed_root is True
    assert candidate.path_containment.duplicate_conflict_policy == "compare_or_conflict_before_true_write"
    assert candidate.atomic_write_preconditions.completeness_pass is True
    assert candidate.atomic_write_preconditions.operator_explicit_gate is False
    assert candidate.atomic_write_preconditions.ready_for_true_write is False
    assert "operator_explicit_gate_missing" in candidate.atomic_write_preconditions.blocked_by
    assert candidate.rollback_receipt_contract.rollback_receipt_available is True
    assert len(candidate.rollback_receipt_contract.required_fields) == 6
    assert len(candidate.rollback_receipt_contract.forbidden_claims) == 4
    assert [item.surface for item in candidate.surface_policies] == [
        "preview",
        "dry_run_commit",
        "future_true_write",
    ]
    assert candidate.future_same_payload_gate.p3b_state == "blocked_pending_explicit_true_write_gate"
    assert len(candidate.future_same_payload_gate.conditions) == 7
