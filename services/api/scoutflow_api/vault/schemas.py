from __future__ import annotations

from enum import StrEnum
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class VaultFrontmatter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str = Field(min_length=1)
    date: str = Field(min_length=1)
    tags: str = Field(min_length=1)
    status: Literal["pending"]


class VaultWriterPolicy(BaseModel):
    model_config = ConfigDict(extra="forbid")

    vault_root: str = Field(min_length=1)
    inbox_dir: Literal["00-Inbox"] = "00-Inbox"
    frontmatter_mode: Literal["raw_4_field"] = "raw_4_field"
    dry_run: bool = True
    write_enabled: bool = False


class VaultPreviewDraft(BaseModel):
    model_config = ConfigDict(extra="forbid")

    capture_id: str = Field(min_length=1)
    target_path: str = Field(min_length=1)
    frontmatter: VaultFrontmatter
    body_markdown: str = Field(min_length=1)
    warnings: list[str] = Field(default_factory=list)


class VaultCommitDryRun(BaseModel):
    model_config = ConfigDict(extra="forbid")

    capture_id: str = Field(min_length=1)
    target_path: str | None = None
    dry_run: bool = True
    committed: bool = False
    write_enabled: bool = False
    candidate: "VaultCommitCandidateV1"


class VaultCommitRoleStatus(StrEnum):
    satisfied = "satisfied"
    held_truthfully = "held_truthfully"


class VaultCommitRole(BaseModel):
    model_config = ConfigDict(extra="forbid")

    role: Literal[
        "title_role",
        "date_role",
        "tags_role",
        "status_role",
        "capture_id_role",
        "platform_item_id_role",
        "canonical_url_role",
        "source_mode_role",
        "evidence_provenance_role",
        "trust_trace_role",
        "content_hash_role",
        "commit_audit_role",
    ]
    value: str = Field(min_length=1)
    required_gate: str = Field(min_length=1)
    status: VaultCommitRoleStatus
    ready_for_true_write: bool = True


class VaultSecretScanPattern(StrEnum):
    cookie = "cookie"
    token = "token"
    api_key = "api_key"
    authorization_header = "authorization_header"
    signed_media_url = "signed_media_url"
    raw_stdout_stderr = "raw_stdout_stderr"
    auth_sidecar = "auth_sidecar"
    browser_profile_path = "browser_profile_path"
    local_credential_path = "local_credential_path"


class VaultSecretScanMatch(BaseModel):
    model_config = ConfigDict(extra="forbid")

    category: VaultSecretScanPattern
    surface: Literal[
        "frontmatter_candidate",
        "markdown_body",
        "canonical_url",
        "trust_trace_notes",
        "rewrite_output",
        "transcript_handoff",
        "receipt_manifest_material",
    ]
    location_class: str = Field(min_length=1)


class VaultSecretScanReport(BaseModel):
    model_config = ConfigDict(extra="forbid")

    surfaces_checked: list[
        Literal[
            "frontmatter_candidate",
            "markdown_body",
            "canonical_url",
            "trust_trace_notes",
            "rewrite_output",
            "transcript_handoff",
            "receipt_manifest_material",
        ]
    ] = Field(min_length=7)
    blocking_categories: list[VaultSecretScanPattern] = Field(min_length=9)
    blocked: bool = False
    matches: list[VaultSecretScanMatch] = Field(default_factory=list)


class VaultPathContainmentReport(BaseModel):
    model_config = ConfigDict(extra="forbid")

    allowed_root: str = Field(min_length=1)
    target_path: str = Field(min_length=1)
    path_fragment_safe: bool
    contained_within_allowed_root: bool
    duplicate_conflict_policy: Literal["compare_or_conflict_before_true_write"]


class VaultAtomicWritePreconditions(BaseModel):
    model_config = ConfigDict(extra="forbid")

    completeness_pass: bool
    secret_scan_pass: bool
    path_containment_pass: bool
    collision_idempotency_decision: Literal["pending_true_write_gate"]
    render_hash_pass: bool
    operator_explicit_gate: bool
    atomic_write_plan_defined: bool
    receipt_rollback_plan_defined: bool
    ready_for_true_write: bool
    blocked_by: list[str] = Field(default_factory=list)


class VaultRollbackReceiptContract(BaseModel):
    model_config = ConfigDict(extra="forbid")

    rollback_receipt_available: bool
    required_fields: list[
        Literal[
            "target_path",
            "pre_write_state",
            "post_write_hash",
            "cleanup_action",
            "human_review_flag",
            "downstream_sync_caveat",
        ]
    ] = Field(min_length=6, max_length=6)
    forbidden_claims: list[str] = Field(min_length=4)


class VaultDryRunSurfacePolicy(BaseModel):
    model_config = ConfigDict(extra="forbid")

    surface: Literal["preview", "dry_run_commit", "future_true_write"]
    allowed: str = Field(min_length=1)
    forbidden: str = Field(min_length=1)


class VaultFutureSamePayloadGate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    p3b_state: Literal["blocked_pending_explicit_true_write_gate"] = "blocked_pending_explicit_true_write_gate"
    conditions: list[
        Literal[
            "p3a_preview_v_pass",
            "same_manual_url",
            "same_source_receipt_or_same_blocked_source_truth",
            "same_transcript_handoff_or_same_blocked_transcript_truth",
            "same_rewrite_payload",
            "same_preview_hash",
            "explicit_user_true_write_gate",
        ]
    ] = Field(min_length=7, max_length=7)


class VaultCommitCandidateV1(BaseModel):
    model_config = ConfigDict(extra="forbid")

    spec_version: Literal["VaultCommitCandidateV1"] = "VaultCommitCandidateV1"
    roles: list[VaultCommitRole] = Field(min_length=12, max_length=12)
    secret_scan: VaultSecretScanReport
    path_containment: VaultPathContainmentReport
    atomic_write_preconditions: VaultAtomicWritePreconditions
    rollback_receipt_contract: VaultRollbackReceiptContract
    surface_policies: list[VaultDryRunSurfacePolicy] = Field(min_length=3, max_length=3)
    future_same_payload_gate: VaultFutureSamePayloadGate
