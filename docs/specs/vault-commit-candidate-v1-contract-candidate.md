# VaultCommitCandidateV1 Contract Candidate

> status: candidate / not-authority / not true-write approval
> lane: `T-P1A-162`
> scope: true_vault_write gate-readiness only

## Purpose

`VaultCommitCandidateV1` defines the dry-run payload that future true write must reuse without mutation when P3B is explicitly opened. This contract does not flip `write_enabled`, does not perform durable write, and does not claim true write approval.

## State Machine

1. `preview_rendered`
2. `candidate_gate_ready`
3. `explicit_true_write_gate_open`
4. `durable_write_completed`

Only `preview_rendered -> candidate_gate_ready` is in scope for this lane. The remaining transitions stay blocked.

## 12 Required Roles

| Role | Meaning | Required gate |
|---|---|---|
| `title_role` | one-line title | non-empty, no newline injection |
| `date_role` | capture date | `YYYY-MM-DD` |
| `tags_role` | minimal tag set | deterministic and safe |
| `status_role` | candidate state | pending or equivalent candidate wording only |
| `capture_id_role` | ScoutFlow capture identity | unique and traceable |
| `platform_item_id_role` | platform identity | present or explicit missing reason |
| `canonical_url_role` | source URL | secret/signed-param scan pass |
| `source_mode_role` | metadata/runtime/placeholder truth | must reveal blocked runtime if any |
| `evidence_provenance_role` | source/runtime/transcript/rewrite provenance | no fabricated proof |
| `trust_trace_role` | Trust Trace identity | present or held truthfully |
| `content_hash_role` | rendered markdown hash | deterministic and reproducible |
| `commit_audit_role` | operator gate + scan + rollback receipt | required before future true write |

Any missing role blocks future true-write readiness.

## Secret Scan

Surfaces:

- `frontmatter_candidate`
- `markdown_body`
- `canonical_url`
- `trust_trace_notes`
- `rewrite_output`
- `transcript_handoff`
- `receipt_manifest_material`

Blocking categories:

- `cookie`
- `token`
- `api_key`
- `authorization_header`
- `signed_media_url`
- `raw_stdout_stderr`
- `auth_sidecar`
- `browser_profile_path`
- `local_credential_path`

The contract may record category and location class only. It must not echo secret values.

## Path Containment

All future write candidates must resolve under:

`"${SCOUTFLOW_VAULT_ROOT}/00-Inbox/"`

Reject:

- `..` escapes
- absolute paths outside the inbox
- hidden second inboxes
- unsafe title-derived path fragments
- silent duplicates without explicit conflict handling

## Atomic Write Preconditions

Future true write requires:

1. completeness pass
2. secret scan pass
3. path containment pass
4. collision/idempotency decision
5. render hash pass
6. operator explicit gate
7. atomic write plan
8. receipt + rollback plan

Dry-run payload may show these conditions, but `ready_for_true_write` remains `false` until the explicit user gate exists.

## Rollback Receipt Contract

Required fields:

- `target_path`
- `pre_write_state`
- `post_write_hash`
- `cleanup_action`
- `human_review_flag`
- `downstream_sync_caveat`

Forbidden claims:

- `rollback always restores vault history`
- `禁止: true write approved`
- `write_enabled flipped`
- `config-only flip without evidence`

## Dry-Run Surface Split

| Surface | Allowed | Forbidden |
|---|---|---|
| `preview` | render target path and markdown preview | claim durable write |
| `dry_run_commit` | prove negative gate shape only | claim almost-commit success |
| `future_true_write` | requires separate user gate plus same-payload conditions | config-only flip without evidence |

## Future P3B Same-Payload Gate

P3B stays blocked until all are true:

1. `P3A preview V-PASS`
2. same manual URL
3. same source receipt or same blocked-source truth
4. same transcript handoff or same blocked transcript truth
5. same rewrite payload
6. same preview hash
7. explicit user true-write gate

## Boundary

This candidate defines gate-readiness material only. It does not flip `write_enabled`, does not perform durable vault write, does not approve true write, does not run runtime/source tools, and does not imply DB migration approval.
