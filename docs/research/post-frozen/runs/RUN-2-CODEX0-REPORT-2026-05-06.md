---
title: RUN-2 CODEX0 report
status: candidate / run-report / not-authority
created_at: 2026-05-06
run_id: RUN-2-CODEX0-RESUME-2026-05-06
baseline_origin_main: f7d6c5c383fe36ed18c6ad981692cec363de3b72
final_origin_main: 7d41e5dc34601a9fd23a819ab9bddc895765ba60
---

# RUN-2 CODEX0 report

## summary

- Scope executed: `PF-LP-04/05/06/07/08/09/10/11/12/14/15/16/17/18`
- Resume starting truth: `origin/main=f7d6c5c383fe36ed18c6ad981692cec363de3b72`, with `#207/#216/#226/#228/#230` already merged
- Resume result: all remaining dispatches completed, R1 forensic truth landed, synthetic UAT-1 evidence landed, and preview-only closeout stayed non-authority
- Resume-phase write surface (after `#230`) stayed inside `docs/research/post-frozen/**`. Full Run-2 changed `apps/capture-station/**`, `tests/e2e/**`, `docs/research/repairs/**`, and `docs/research/post-frozen/**` as listed in the `dispatch_receipts` table below.

## forensic_verdicts

| dispatch | verdict | source PR | source merge commit | note |
|---|---|---:|---|---|
| `PF-LP-09` | `COVERED_BY_228` | `#233` | `b4fc8b5` | copy action already implemented and test-covered under `#228` |
| `PF-LP-10` | `COVERED_BY_228` | `#232` | `9512f9e` | download action already implemented and test-covered under `#228` |
| `PF-LP-14` | `COVERED_BY_228` | `#234` | `2445761` | `api-client.test.ts` already covered by `#228` |

## dispatch_receipts

| code | PR | merge_commit | output | verdict |
|---|---:|---|---|---|
| `PF-LP-04` | `#207` | `f84e75d` | `apps/capture-station/src/lib/api-client.ts` | `T-PASS` |
| `PF-LP-05` | `#216` | `5886187` | `apps/capture-station/src/features/url-bar/UrlBar.tsx` | `T-PASS` |
| `PF-LP-06` | `#226`, `#228` | `04a25c3`, `bd1f382` | `apps/capture-station/src/layout/FourPanelShell.tsx` | `T-PASS` |
| `PF-LP-07` | `#226`, `#228` | `04a25c3`, `bd1f382` | `apps/capture-station/src/layout/FourPanelShell.tsx` | `T-PASS` |
| `PF-LP-08` | `#228` | `bd1f382` | `apps/capture-station/src/features/vault-preview/VaultPreviewPanel.tsx` | `T-PASS` |
| `PF-LP-09` | `#233` | `b4fc8b5` | `docs/research/post-frozen/runs/RUN-2-LP-09-coverage-evidence-2026-05-06.md` | `COVERED_BY_228` |
| `PF-LP-10` | `#232` | `9512f9e` | `docs/research/post-frozen/runs/RUN-2-LP-10-coverage-evidence-2026-05-06.md` | `COVERED_BY_228` |
| `PF-LP-11` | `#228` | `bd1f382` | `apps/capture-station/src/features/vault-preview/VaultPreviewPanel.tsx` | `T-PASS` |
| `PF-LP-12` | `#230` | `f7d6c5c` | `docs/research/post-frozen/localhost-preview-dev-runbook-2026-05-06.md` | `T-PASS` |
| `PF-LP-14` | `#234` | `2445761` | `docs/research/post-frozen/runs/RUN-2-LP-14-coverage-evidence-2026-05-06.md` | `COVERED_BY_228` |
| `PF-LP-15` | `#228` | `bd1f382` | `tests/e2e/test_h5_bridge_preview_placeholder.py` | `T-PASS` |
| `PF-LP-16` | `#235` | `91a2dea` | `docs/research/post-frozen/evidence/PF-LP-16-manual-localhost-run-2026-05-06.md` | `partial` |
| `PF-LP-17` | `#236` | `0109a5a` | `docs/research/post-frozen/preview-only-localhost-loop-readback.md` | `partial` |
| `PF-LP-18` | `#237` | `7d41e5d` | `docs/research/post-frozen/preview-only-closeout-authority-safe-note-2026-05-06.md` | `partial` |

## synthetic_uat_1

- evidence path: `docs/research/post-frozen/evidence/PF-LP-16-manual-localhost-run-2026-05-06.md`
- input URL kept with original query string:
  `https://www.bilibili.com/video/BV1WQ9YBNEk6/?spm_id_from=333.1387.homepage.video_card.click&vd_source=4be6ac946264764a925966c890c00b25`
- canonical BV path note:
  `https://www.bilibili.com/video/BV1WQ9YBNEk6`
- synthetic probe result:
  - `capture_id=01KQYEXWJYZ9X8FW7TGD1QW0XP`
  - preview markdown lines=`23`
  - first lines=`# ScoutFlow BV1WQ9YBNEk6`, blank line, `## Capture`
  - `pnpm test -- VaultPreviewPanel UrlBar` passed `22/22`
- classification:
  - `copy_action=success`
  - `download_action=success`
  - `verdict=partial`
  - `synthetic_result=works`
  - `missing_proof=real_browser_visual_uat`

## validation

- Runtime probes:
  - `curl -s http://127.0.0.1:8000/healthz | grep ok`
  - `POST /captures/discover`
  - `GET /captures/{capture_id}/vault-preview`
- Frontend test probe:
  - `pnpm test -- VaultPreviewPanel UrlBar`
- Branch-level checks on each docs PR:
  - `python tools/check-docs-redlines.py`
  - `python tools/check-secrets-redlines.py`
  - `git diff --check`

## interruption_log

| class | count | note |
|---|---:|---|
| `slot_local` | `1` | one malformed `curl -> python` pipeline was retried to recover exact markdown line counts |
| `control_plane` | `2` | one `git worktree add` config-lock collision; one `gh pr merge --delete-branch` local-branch deletion collision caused by live worktrees |
| `ledger` | `0` | no post-merge receipt rebuild was needed |

## boundary_verdict

- `blocked_claims_intact=true`
- `authority_files_touched=false`
- `runtime_unlock_claimed=false`
- `migration_unlock_claimed=false`
- `browser_automation_unlock_claimed=false`
- `true_vault_write_claimed=false`

## follow_up

- External audit inputs for Run-2 are now complete:
  - `docs/research/post-frozen/runs/RUN-2-CODEX0-REPORT-2026-05-06.md`
  - `docs/research/post-frozen/runs/DIFF-BUNDLE-Run2-2026-05-06.md`
  - `docs/research/post-frozen/runs/CHECKPOINT-Run2-final.json`

## ready_for_run_3

- ready_for_run_3: no
- blocking_reasons:
  - LP-18 closeout intentionally stopped short of authority writeback (`docs/research/post-frozen/preview-only-closeout-authority-safe-note-2026-05-06.md`)
  - real_browser_visual_uat_not_run (synthetic UAT-1 only; user authorized partial-evidence mode)
  - human_decision_pending: whether real-browser UAT + authority writeback are prerequisites for Run-3
- amendment_status: receipt_traceability_amended_2026-05-06
- gate: pending_user_decision_on_run_3_scope
