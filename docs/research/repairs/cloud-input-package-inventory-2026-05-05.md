---
title: Cloud Input Package Inventory
status: candidate
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
created_at: 2026-05-05
scope: STEP2 item 2B-2 cloud package inventory with tier and visibility state
---

# Cloud Input Package Inventory

> State: candidate / not authority / not execution approval.

## 1. Inventory Rule

Every input is classified by:

- `tier`: `canonical` / `context` / `optional` / `forbidden`
- `visibility_state`: `origin/main` / `candidate branch` / `local only`

## 2. Inventory Table

| Tier | Visibility | File | Use |
|---|---|---|---|
| `canonical` | `origin/main` | `docs/research/repairs/dispatch127-176-pack-design-v3-2026-05-05.md` | main design contract |
| `canonical` | `origin/main` | `docs/research/repairs/step2-prep-checklist-2026-05-05.md` | STEP2 execution contract |
| `canonical` | `origin/main` | `docs/research/repairs/wave5-scope-and-template-extraction-2026-05-05.md` | Wave 5 anchor pool + batch1 template extraction |
| `canonical` | `candidate branch` | `docs/research/repairs/batch2-audit-summary-2026-05-05.md` | current fact-layer summary |
| `canonical` | `candidate branch` | `docs/research/repairs/readback-manifest-2026-05-05.md` | repo/readback truth layer |
| `canonical` | `candidate branch` | `docs/research/repairs/backbone-taxonomy-2026-05-05.md` | final 50-slot backbone input contract |
| `canonical` | `origin/main` | `docs/PRD-v2-2026-05-04.md` | base product anchor |
| `canonical` | `origin/main` | `docs/SRD-v2-2026-05-04.md` | base engineering anchor |
| `canonical` | `origin/main` | `docs/PRD-amendments/prd-v2.1-strong-visual-h5-para-pr-factory-candidate-2026-05-04.md` | candidate addendum promoted for B2 planning/contract baseline via `T-P1A-103`, not globally promoted base authority |
| `canonical` | `origin/main` | `docs/SRD-amendments/h5-bridge-para-vault-srd-v3-candidate-2026-05-04.md` | candidate addendum promoted for B2 planning/contract baseline via `T-P1A-103`, not globally promoted base authority |
| `canonical` | `origin/main` | `docs/SRD-amendments/db-vnext-srd-v3-candidate-2026-05-04.md` | candidate-only DB context; use cautiously as non-default anchor |
| `context` | `origin/main` | `docs/current.md` | current authority state |
| `context` | `origin/main` | `docs/task-index.md` | task/state support |
| `context` | `origin/main` | `docs/decision-log.md` | decision support |
| `context` | `origin/main` | `docs/specs/contracts-index.md` | contract support |
| `context` | `origin/main` | `docs/shoulders-index.md` | shoulders/reference state |
| `context` | `origin/main` | `docs/dispatch-template.md` | dispatch writing shape |
| `context` | `local only` | `/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/packs/ScoutFlow-PR76-PR125-dispatch-pack-2026-05-05-b2v4/scoutflow-doc3-amend-pr76-pr125-worklist-2026-05-05.md` | batch1 structural template |
| `context` | `local only` | `/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/REPORT-Wave4-Batch2-v4-Dispatch91-110-CODEX0-2026-05-05.md` | full Batch2 raw report |
| `optional` | `origin/main` | `docs/research/repairs/step2-local-mode-and-packlint-surface-2026-05-05.md` | local mode and lint background |
| `optional` | `origin/main` | `docs/research/repairs/step2-runtime-readiness-and-screenshot-note-2026-05-05.md` | runtime/readiness context |
| `optional` | `origin/main` | `docs/research/repairs/step2-runner-api-disk-budget-2026-05-05.md` | staged-pool caveat |
| `optional` | `local only` | `/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/archive/v1-v2-spec-trail-2026-05-05/dispatch127-176-pack-design-2026-05-05.md` | historical candidate trail |
| `optional` | `local only` | `/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/archive/v1-v2-spec-trail-2026-05-05/dispatch127-176-pack-design-v2-2026-05-05.md` | historical candidate trail |
| `forbidden` | `local only` | `.env`, raw credentials, cookie/token material, raw stdout containing secrets | never expose to cloud |
| `forbidden` | `origin/main` | `migrations/**` as actionable cloud input | keep out of cloud prompt |

## 3. Packaging Guidance

- prefer canonical files first
- use context files only when they add current truth or structural template value
- summarize very large local-only context rather than pasting it inline
- never treat `candidate branch` rows as already cloud-readable until merged

## 4. Current Status

At first write time:

- enough canonical/context material already exists to start Cloud Draft Gate once `backbone-taxonomy` and `readback-manifest` are merged
- local-only batch1 worklist remains a useful template source but should be summarized rather than dumped verbatim
- rows marked `candidate branch` are expected to move to `origin/main` through the current STEP2B merge PR before STEP2 is declared fully closed
