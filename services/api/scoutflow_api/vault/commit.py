from __future__ import annotations

import hashlib
from collections.abc import Mapping
from pathlib import Path
from typing import Any

from scoutflow_api.vault.frontmatter import frontmatter_as_markdown
from scoutflow_api.vault.renderer import build_preview_draft
from scoutflow_api.vault.schemas import (
    VaultAtomicWritePreconditions,
    VaultCommitCandidateV1,
    VaultCommitDryRun,
    VaultCommitRole,
    VaultCommitRoleStatus,
    VaultDryRunSurfacePolicy,
    VaultFutureSamePayloadGate,
    VaultPathContainmentReport,
    VaultPreviewDraft,
    VaultRollbackReceiptContract,
)
from scoutflow_api.vault.secret_scan import build_secret_scan_report
from scoutflow_api.vault.path_policy import resolve_inbox_root


WRITE_DISABLED_MESSAGE = "Bridge write path is not approved in the current phase."


def build_commit_dry_run_from_preview(preview: VaultPreviewDraft) -> VaultCommitDryRun:
    return VaultCommitDryRun(
        capture_id=preview.capture_id,
        target_path=preview.target_path,
        candidate=build_commit_candidate_from_preview(
            preview,
            {
                "capture_id": preview.capture_id,
                "platform_item_id": preview.frontmatter.title.replace("ScoutFlow ", "", 1),
                "canonical_url": _extract_markdown_capture_line(preview.body_markdown, "canonical_url"),
                "source_kind": _extract_markdown_capture_line(preview.body_markdown, "source_kind").strip("`"),
                "capture_mode": _extract_markdown_capture_line(preview.body_markdown, "capture_mode").strip("`"),
            },
        ),
    )


def build_commit_dry_run(capture: Mapping[str, Any], vault_root: str | Path) -> VaultCommitDryRun:
    preview = build_preview_draft(capture, vault_root)
    return VaultCommitDryRun(
        capture_id=preview.capture_id,
        target_path=preview.target_path,
        candidate=build_commit_candidate_from_preview(preview, capture),
    )


def build_commit_candidate_from_preview(preview: VaultPreviewDraft, capture: Mapping[str, Any]) -> VaultCommitCandidateV1:
    content_hash = hashlib.sha256(preview.body_markdown.encode("utf-8")).hexdigest()
    platform_item_id = _mapping_value(capture, "platform_item_id")
    canonical_url = _mapping_value(capture, "canonical_url")
    source_kind = _mapping_value(capture, "source_kind", default="manual_url") or "manual_url"
    capture_mode = _mapping_value(capture, "capture_mode", default="metadata_only") or "metadata_only"
    trust_trace_truth = "held:trust_trace_not_materialized_in_phase_1a"
    roles = [
        VaultCommitRole(
            role="title_role",
            value=preview.frontmatter.title,
            required_gate="non-empty, no newline injection",
            status=VaultCommitRoleStatus.satisfied,
        ),
        VaultCommitRole(
            role="date_role",
            value=preview.frontmatter.date,
            required_gate="YYYY-MM-DD or fail",
            status=VaultCommitRoleStatus.satisfied,
        ),
        VaultCommitRole(
            role="tags_role",
            value=preview.frontmatter.tags,
            required_gate="deterministic and safe",
            status=VaultCommitRoleStatus.satisfied,
        ),
        VaultCommitRole(
            role="status_role",
            value=preview.frontmatter.status,
            required_gate="candidate or pending state only",
            status=VaultCommitRoleStatus.satisfied,
        ),
        VaultCommitRole(
            role="capture_id_role",
            value=preview.capture_id,
            required_gate="unique and traceable",
            status=VaultCommitRoleStatus.satisfied,
        ),
        VaultCommitRole(
            role="platform_item_id_role",
            value=platform_item_id or "held:missing_platform_item_id_reason_required",
            required_gate="present or explicit missing reason",
            status=VaultCommitRoleStatus.satisfied if platform_item_id else VaultCommitRoleStatus.held_truthfully,
        ),
        VaultCommitRole(
            role="canonical_url_role",
            value=canonical_url or "held:missing_canonical_url_reason_required",
            required_gate="secret or signed-param scan pass",
            status=VaultCommitRoleStatus.satisfied if canonical_url else VaultCommitRoleStatus.held_truthfully,
        ),
        VaultCommitRole(
            role="source_mode_role",
            value=f"source_kind={source_kind};capture_mode={capture_mode};runtime=blocked",
            required_gate="must reveal blocked runtime if any",
            status=VaultCommitRoleStatus.satisfied,
        ),
        VaultCommitRole(
            role="evidence_provenance_role",
            value="capture_row+preview_render_only;transcript=blocked;rewrite=blocked",
            required_gate="no fabricated proof",
            status=VaultCommitRoleStatus.satisfied,
        ),
        VaultCommitRole(
            role="trust_trace_role",
            value=trust_trace_truth,
            required_gate="present or held truthfully",
            status=VaultCommitRoleStatus.held_truthfully,
        ),
        VaultCommitRole(
            role="content_hash_role",
            value=content_hash,
            required_gate="deterministic and reproducible",
            status=VaultCommitRoleStatus.satisfied,
        ),
        VaultCommitRole(
            role="commit_audit_role",
            value="operator_gate+secret_scan+rollback_receipt_required_before_true_write",
            required_gate="operator gate plus scan plus rollback receipt required before future true write",
            status=VaultCommitRoleStatus.satisfied,
        ),
    ]
    secret_scan = build_secret_scan_report(
        frontmatter_candidate=frontmatter_as_markdown(preview.frontmatter),
        markdown_body=preview.body_markdown,
        canonical_url=canonical_url,
        trust_trace_notes=trust_trace_truth,
        rewrite_output="blocked:no_rewrite_output_in_phase_1a",
        transcript_handoff="blocked:no_transcript_handoff_in_phase_1a",
        receipt_manifest_material=f"target_path={preview.target_path};content_hash={content_hash};io_logs_not_stored",
    )
    path_containment = _build_path_containment(preview.target_path)
    atomic_preconditions = _build_atomic_preconditions(secret_scan.blocked, path_containment.contained_within_allowed_root)
    return VaultCommitCandidateV1(
        roles=roles,
        secret_scan=secret_scan,
        path_containment=path_containment,
        atomic_write_preconditions=atomic_preconditions,
        rollback_receipt_contract=VaultRollbackReceiptContract(
            rollback_receipt_available=True,
            required_fields=[
                "target_path",
                "pre_write_state",
                "post_write_hash",
                "cleanup_action",
                "human_review_flag",
                "downstream_sync_caveat",
            ],
            forbidden_claims=[
                "rollback always restores vault history",
                "禁止: true write approved",
                "write_enabled flipped",
                "config-only flip without evidence",
            ],
        ),
        surface_policies=[
            VaultDryRunSurfacePolicy(
                surface="preview",
                allowed="render target path and markdown preview",
                forbidden="claim durable write",
            ),
            VaultDryRunSurfacePolicy(
                surface="dry_run_commit",
                allowed="prove negative gate shape only",
                forbidden="claim almost-commit success",
            ),
            VaultDryRunSurfacePolicy(
                surface="future_true_write",
                allowed="requires separate user gate plus same-payload condition",
                forbidden="config-only flip without evidence",
            ),
        ],
        future_same_payload_gate=VaultFutureSamePayloadGate(
            conditions=[
                "p3a_preview_v_pass",
                "same_manual_url",
                "same_source_receipt_or_same_blocked_source_truth",
                "same_transcript_handoff_or_same_blocked_transcript_truth",
                "same_rewrite_payload",
                "same_preview_hash",
                "explicit_user_true_write_gate",
            ]
        ),
    )


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
            f"- candidate_spec: `{commit.candidate.spec_version}`",
            f"- candidate_roles: `{len(commit.candidate.roles)}`",
            f"- secret_scan_blocked: `{str(commit.candidate.secret_scan.blocked).lower()}`",
            f"- future_true_write_state: `{commit.candidate.future_same_payload_gate.p3b_state}`",
            f"- gate: {WRITE_DISABLED_MESSAGE}",
        ]
    )


def _extract_markdown_capture_line(markdown: str, label: str) -> str:
    prefix = f"- {label}: "
    for line in markdown.splitlines():
        if line.startswith(prefix):
            return line[len(prefix) :].strip()
    return ""


def _build_path_containment(target_path: str) -> VaultPathContainmentReport:
    target = Path(target_path)
    inbox_root = resolve_inbox_root(target.parents[1])
    return VaultPathContainmentReport(
        allowed_root=str(inbox_root),
        target_path=target_path,
        path_fragment_safe=".." not in target_path and not target_path.startswith(".."),
        contained_within_allowed_root=str(target).startswith(str(inbox_root)),
        duplicate_conflict_policy="compare_or_conflict_before_true_write",
    )


def _build_atomic_preconditions(secret_scan_blocked: bool, path_contained: bool) -> VaultAtomicWritePreconditions:
    blocked_by = []
    if secret_scan_blocked:
        blocked_by.append("secret_scan_blocked")
    if not path_contained:
        blocked_by.append("path_containment_failed")
    blocked_by.append("operator_explicit_gate_missing")
    return VaultAtomicWritePreconditions(
        completeness_pass=True,
        secret_scan_pass=not secret_scan_blocked,
        path_containment_pass=path_contained,
        collision_idempotency_decision="pending_true_write_gate",
        render_hash_pass=True,
        operator_explicit_gate=False,
        atomic_write_plan_defined=True,
        receipt_rollback_plan_defined=True,
        ready_for_true_write=False,
        blocked_by=blocked_by,
    )


def _mapping_value(mapping: Mapping[str, Any], key: str, *, default: str = "") -> str:
    if key not in mapping:
        return default
    value = mapping[key]
    return str(value).strip()
