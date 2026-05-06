---
title: DIFF BUNDLE Run2
status: candidate / audit-bundle / not-authority
created_at: 2026-05-06
run_id: RUN-2-CODEX0-RESUME-2026-05-06
---

# DIFF BUNDLE Run2

## cross_pr_consistency

| area | PRs | consistency verdict |
|---|---|---|
| `localhost preview shell chain` | `#207`, `#216`, `#226`, `#228`, `#230` | create-capture -> URL submit -> preview shell -> preview panel -> runbook chain is internally coherent after the repair PR |
| `forensic truth closure` | `#232`, `#233`, `#234` | each verdict stayed evidence-backed and did not reopen product code or backfill silent scope notes |
| `synthetic UAT evidence` | `#235`, `#236` | synthetic run uses active probes plus JSDOM tests, keeps preview-only wording, and does not claim browser execution |
| `authority-safe closeout` | `#237` | closeout stayed inside `docs/research/post-frozen/**` and preserved `NOT_EXECUTION_APPROVED` |

## merged_outputs

- `#207` adds the capture-station `createCapture` client surface.
- `#216` wires the URL bar submit flow.
- `#226` and `#228` land the preview shell, preview panel, placeholder guard, and the packed repair chain.
- `#230` adds the localhost preview dev runbook used as the UAT-1 procedural baseline.
- `#232/#233/#234` convert the ambiguous `LP-09/10/14` gap into explicit `COVERED_BY_228` forensic truth.
- `#235` lands the synthetic UAT-1 evidence note.
- `#236` reads that synthetic loop back as `works` without promoting it to runtime approval.
- `#237` closes the chain with an authority-safe note and no authority writeback.

## high_blast_readback

| item | readback |
|---|---|
| `PF-LP-08` | preview panel behavior remains anchored to `#228`; synthetic UAT confirms the preview endpoint returns real markdown and the panel contract stayed aligned |
| `PF-LP-15` | e2e placeholder baseline guard remains merged under `#228`; later forensic and synthetic docs did not weaken that guard |

## notable_non_findings

- No resume PR touched `docs/current.md`, `docs/task-index.md`, `docs/decision-log.md`, `docs/specs/contracts-index.md`, or `AGENTS.md`.
- No resume PR touched `services/api/migrations/**`, `workers/**`, `packages/**`, `data/**`, or `referencerepo/**`.
- No resume PR claimed runtime approval, browser automation approval, migration approval, or true vault write.

## residual_risk

| risk | why it remains | current containment |
|---|---|---|
| `synthetic UAT is not human visual proof` | copy/download were classified from JSDOM tests rather than a real browser click | evidence file and readback both say `synthetic_partial` / preview-only |
| `packed PR #228 remains a historical compression point` | five localhost preview dispatches still share one repair PR | R1 forensic docs explicitly map LP-09/10/14 to `#228` instead of silently assuming coverage |
| `authority promotion risk` | later readers might overread localhost proof into runtime approval | LP-17 and LP-18 repeat `works but not runtime approval` and `read-only authority reference` |

## audit_ready_paths

- `docs/research/post-frozen/runs/RUN-2-CODEX0-REPORT-2026-05-06.md`
- `docs/research/post-frozen/runs/DIFF-BUNDLE-Run2-2026-05-06.md`
- `docs/research/post-frozen/runs/CHECKPOINT-Run2-final.json`
