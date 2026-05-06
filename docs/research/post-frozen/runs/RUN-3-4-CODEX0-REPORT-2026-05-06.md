---
title: RUN-3-4 CODEX0 Report
status: candidate / run-report / not-authority
created_at: 2026-05-06
execution_mode: local_worktree_only_until_merge
base_ref: 2dbf2c19ae7c93f626929191bc9d0d4e3979958f
worktree: /tmp/scoutflow-run3-4-1778080188
---

# RUN-3-4 CODEX0 Report

## Run Summary

- `batch_a_audit: clear`
- `batch_b_audit: clear`
- `batch_c_audit: clear`
- `c1_verdict: pass`
- `c1_useful_count: 3 of 3`
- `c2_verdict: partial`
- `c2_partial_count: 5`
- `c1_iteration_2_run: no`
- `authority_writeback: skipped_by_user_choice`
- `final_origin_main_observed: 2dbf2c19ae7c93f626929191bc9d0d4e3979958f`
- `execution_mode: local_worktree_only_until_merge`

This run intentionally held `0 commit / 0 PR / 0 merge` during execution so the honest `C2 partial` state could stay visible in one worktree until the user authorized a single-shot direct merge.

## Dispatch Receipt

| Dispatch | Outcome | Artifact |
| --- | --- | --- |
| `PF-C1-01` | pass | `docs/research/post-frozen/c1-canary-url-pack.md` |
| `PF-C1-02` | pass | `docs/specs/post-frozen/topic-card-lite-contract-v0.md` |
| `PF-C1-03` | pass | `docs/research/post-frozen/topic-card-preview-vault-historical-asset-extraction.md` |
| `PF-C1-04` | pass | `apps/capture-station/src/features/topic-card-preview/**` |
| `PF-C1-05` | pass | `apps/capture-station/src/features/topic-card-vault/**` |
| `PF-C1-06` | pass | `docs/research/post-frozen/c1-human-usefulness-rubric.md` |
| `PF-C1-07` | pass | `docs/research/post-frozen/c1-three-url-preview-proof-set.md` + `proof-artifacts/run-3-c1-07/` |
| `PF-C1-08` | pass | `docs/research/post-frozen/evidence/PF-C1-08-human-verdict-2026-05-06.md` |
| `PF-C1-09` | pass | `docs/research/post-frozen/c1-false-positive-edit-cost-log.md` |
| `PF-C1-10` | pass | `docs/research/post-frozen/c1-proof-readback.md` |
| `PF-C1-11` | skipped | `docs/research/post-frozen/c1-second-canary-iteration.md` |
| `PF-C1-12` | partial / skip | no authority writeback by explicit human choice |
| `PF-C2-01` | pass | `docs/specs/post-frozen/raw-note-candidate-contract-v0.md` |
| `PF-C2-02` | pass | `docs/research/post-frozen/raw-frontmatter-compatibility-check.md` |
| `PF-C2-03` | pass | `docs/research/post-frozen/manual-raw-handoff-runbook.md` |
| `PF-C2-04` | pass | `docs/research/post-frozen/raw-intake-acceptance-rubric.md` |
| `PF-C2-05` | pass | `docs/specs/post-frozen/script-seed-proof-contract.md` |
| `PF-C2-06` | partial | `docs/research/post-frozen/c2-two-note-manual-raw-handoff-run.md` + `raw-handoff-staging/` |
| `PF-C2-07` | partial | `docs/research/post-frozen/c2-raw-intake-readback-result.md` |
| `PF-C2-08` | partial | `docs/research/post-frozen/c2-script-seed-generation-result.md` |
| `PF-C2-09` | expected_partial | `docs/research/post-frozen/c2-second-inbox-negative-test.md` |
| `PF-C2-10` | pass_with_pending_boundary | `docs/research/post-frozen/scoutflow-raw-sor-handoff-matrix.md` |
| `PF-C2-11` | partial | `docs/research/post-frozen/c2-proof-readback.md` |
| `PF-C2-12` | pass | `docs/research/post-frozen/future-true-write-gate-draft.md` |

## Boundary Audits

### Batch A

- authority files untouched
- `topic-card-preview/**` and `topic-card-vault/**` stayed inside allowed app paths
- no true-write / runtime unlock / migration drift
- `write_enabled=False` still present twice in `services/api/scoutflow_api/bridge/config.py`

### Batch B

- `PF-C1-08` evidence is filled and aligned with downstream actions: `pass`, `c2_go_no_go=yes`, `allow_authority_writeback=no`
- no authority files were modified because C1-12 stayed skipped
- `PF-C2-01..05` all stayed candidate-only / not-authority

### Batch C

- staging remained entirely inside `docs/research/post-frozen/raw-handoff-staging/`
- no write into `~/workspace/raw/`
- no true vault write, browser automation, migrations, or blocked runtime tools
- `PF-C2-12` stayed overflow-only

## Interruptions

- `slot_local: 1`
  - initial localhost server backgrounding did not hold; reran the server in a stable foreground session and completed `PF-C1-07`
- `control_plane: 0`
- `ledger: 0`

## Ready State

- `ready_for_external_audit: yes`
- `ready_for_run_5: yes_pending_pf_v_handoff`
- `why_not_full_ready: PF-C2 remains partial until the user manually copies staged notes into RAW 00-Inbox and RAW-side intake evidence exists`
