---
title: DIFF BUNDLE Run1
status: candidate / external_audit_packet / not-authority
created_at: 2026-05-06
run_id: Run-1-CODEX0-2026-05-06
---

# DIFF BUNDLE — Run1

## audit_scope

- Target: PR `#199` -> `#206`
- Purpose: give GPT Pro / Hermes / Claude a compact cross-PR consistency packet
- Non-goals:
  - no claim of runtime approval
  - no claim of true vault write approval
  - no authority-file verdict

## pr_bundle

| PR | dispatch | files_changed | cross-PR role |
|---|---|---|---|
| `#199` | `PF-C0-01R` | `docs/research/post-frozen/live-authority-readback-after-pr194.md` | resets live truth boundary after PR193/194 |
| `#200` | `PF-O1-01R` | `docs/research/post-frozen/overflow-registry-v0.md` | names the five blocked lanes that must stay out of mainline |
| `#201` | `PF-LP-03` | `docs/research/post-frozen/vault-preview-env-contract-2026-05-06.md` | defines env semantics before localhost preview work |
| `#202` | `PF-C0-MERGED-03+04` | `docs/research/post-frozen/successor-entry-and-preview-scope-2026-05-06.md` | locks PF routing, preview-only pass bar, and naming reset |
| `#203` | `PF-C0-06R` | `docs/research/post-frozen/near-term-execution-matrix-2026-05-06.md` | fixes the 80-row classification and near-term budget |
| `#204` | `PF-LP-01` | `services/api/scoutflow_api/main.py`, `bridge/{schemas,vault_commit}.py`, `tests/api/test_main_app_routers.py`, 5 bridge contract tests | turns bridge routes into real app paths without unlocking write |
| `#205` | `PF-LP-02` | `tests/api/test_bridge_vault_preview_smoke.py`, `bridge/vault_preview.py`, `vault/renderer.py`, renderer/e2e fixture sync | makes preview smoke and 20+ line preview draft real |
| `#206` | `PF-LP-13` | `tests/conftest.py`, `tests/contracts/test_bridge_openapi_golden_contract.py`, `tests/contracts/golden/bridge-openapi-2026-05-06.json` | locks OpenAPI shape and runtime false-write invariants |

## cross_pr_invariants

### invariant_1_preview_only

- PRs `#201` -> `#206` consistently keep the localhost line preview-only.
- No PR introduces a real commit/write path.
- `write_enabled=false` stays explicit in docs, runtime responses, and golden contract.

### invariant_2_frozen_history_not_reopened

- PRs `#199`, `#202`, and `#203` consistently treat Dispatch126-176 as evidence only.
- No PR restarts linear `Dispatch177+` sequencing.
- The successor route is PF-cluster-driven, not frozen-number-driven.

### invariant_3_authority_surfaces_untouched

- None of PR `#199` -> `#206` modify:
  - `docs/current.md`
  - `docs/task-index.md`
  - `docs/decision-log.md`
  - `AGENTS.md`

### invariant_4_bridge_route_truth_progression

- `#204` makes bridge routes reachable on the real app.
- `#205` adds smoke coverage and expands preview draft shape enough to make excerpt-based proof meaningful.
- `#206` locks the mounted route and schema subset so later drift is detectable.

## review_prompts

### reviewer_focus_1

- Confirm no PR in the bundle implies true vault write or runtime approval through wording, schema shape, or tests.

### reviewer_focus_2

- Confirm `#205` preview-draft expansion remains bounded to preview-only semantics and does not smuggle in authority or RAW handoff claims.

### reviewer_focus_3

- Confirm `#206` golden subset is tight enough to catch drift but narrow enough to avoid noisy false failures.

## ready_state

- ready_for_external_audit: `yes`
- suggested order:
  1. read `#199` + `#200` for boundary and overflow truth
  2. read `#204` + `#205` for runtime-facing code changes
  3. read `#206` for final schema/golden lock

