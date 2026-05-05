---
title: STEP2 Prep Checklist
status: candidate
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
migration_approval: not-approved
created_at: 2026-05-05
scope: STEP2 preparation for post-Batch2 Cloud ChatGPT Pro draft and later STEP3 cold-start commander prompt
related_spec: docs/research/repairs/dispatch127-176-pack-design-v3-2026-05-05.md
---

# STEP2 Prep Checklist

> State: candidate / not authority / not execution approval / not runtime approval / not migration approval.
> This file is an execution checklist, not another large design spec.
> Current node assumption: Wave B Batch2 / Dispatch91-110 is still running, observed around Dispatch98. Cloud Draft Gate is expected after Batch2 terminal plus about one hour of audit/repair. Execution Gate remains later, after Dispatch125 terminal and final readback repair.

## 0. STEP2 Purpose

STEP2 is not just environment preparation.

STEP2 has two jobs:

1. Prepare the local execution base so STEP3 will not stall on mechanical issues.
2. Prepare the GitHub-visible input set so Cloud ChatGPT Pro can actually read the canonical materials through GitHub.

The main GitHub visibility rule is simple:

- Anything only in a dirty worktree, untracked file, or local-only branch is invisible to Cloud ChatGPT Pro.
- Anything the cloud must read must be available on `origin/main`.
- Therefore STEP2 must explicitly manage which candidate artifacts are merged, which are archived to raw, and which remain local-only.

## 1. Canonical Inputs and Version Policy

Use these rules throughout STEP2:

- Canonical spec for cloud consumption: `dispatch127-176-pack-design-v3-2026-05-05.md`
- Non-canonical older drafts: `dispatch127-176-pack-design-2026-05-05.md` and `dispatch127-176-pack-design-v2-2026-05-05.md`
- V1/V2 should not be merged to `origin/main`
- V1/V2 should be archived to raw trail storage, not left as repo noise
- STEP2 checklist itself should be merged to `origin/main` if Cloud ChatGPT Pro needs to reference it

Archive target for V1/V2:

`~/workspace/raw/05-Projects/ScoutFlow/dispatches/archive/v1-v2-spec-trail-2026-05-05/`

## 2. Completion Definition

STEP2 is complete only when all of the following are true:

- STEP2A is complete
- Batch2 terminal state exists and STEP2B is complete
- Cloud ChatGPT Pro can access the canonical input set on `origin/main`
- `T-P1A-105` visibility is consistent
- `V3` is the only spec-level canonical design document for cloud use
- `BACKBONE-TAXONOMY.md` and `READBACK-MANIFEST.md` are merged and readable through GitHub
- STEP3 prompt author has a clean input package with tier labels

## 2.1 Execution Metadata Fields

Each checklist item carries these execution fields:

| Field | Allowed values |
|---|---|
| `execution_mode` | `main_window_sequential` / `subagent_parallel` / `wait_then_main` / `wait_then_subagent` |
| `blocking_dependency` | checklist item IDs and/or external waits such as `Batch2_terminal` / `branch_protection_user_merge` |
| `codex_can_autorun` | `yes` / `yes_unless_branch_protection` / `yes_after_preflight_resolution` / `no_platform_gate` |

## 3. STEP2A Now

Target: do these now, before Batch2 terminal.

Estimated wall time: about 2-4 hours depending `T-P1A-105` cleanup and GitHub merge latency.

### [x] 2A-1a T-P1A-105 verification closure

- execution_mode: `main_window_sequential`
- blocking_dependency: `none`
- codex_can_autorun: `yes`
- Owner: Codex
- Estimated time: 10-20 min
- Prerequisite: none
- Scope:
  - `docs/dispatch-template.md`
  - `docs/specs/parallel-execution-protocol.md`
  - any other tracked files tied to local `T-P1A-105` changes
- Current observed reality:
  - `origin/main` already contains commit `70e5815` with subject `T-P1A-105 codify commander template and ignore plan (#96)`
- Required action:
  - verify repo reality now matches that merged state
  - confirm no residual mixed state remains between authority docs, tracked files, and local worktree
- Success condition:
  - no mixed state where `task-index/current` implies done but tracked files or local worktree disagree with `origin/main`

### [x] 2A-1b `plan/` gitignore decision

- execution_mode: `main_window_sequential`
- blocking_dependency: `2A-1a`
- codex_can_autorun: `yes`
- Owner: Codex
- Estimated time: 10-15 min
- Prerequisite: 2A-1a
- Decision required:
  - confirm whether `plan/` remains gitignored local workspace only
  - confirm no tracked prompt/input artifact that Cloud ChatGPT Pro needs is stored only under `plan/`
- Success condition:
  - no STEP2/STEP3 dependency relies on `.gitignore`d-only files

### [x] 2A-1c local tools/tests cleanup + `ff-only` sync

- execution_mode: `main_window_sequential`
- blocking_dependency: `2A-1a`
- codex_can_autorun: `yes`
- Owner: Codex
- Estimated time: 15-30 min
- Prerequisite: 2A-1a
- Scope:
  - local pack-lint related stray edits
  - stale worktrees/branches if they interfere with clean readback
  - sync local mainline view against `origin/main`
- Success condition:
  - repo state is understandable
  - no misleading stale local branch state contaminates readback

### [x] 2A-2 Codex local mode verification

- execution_mode: `subagent_parallel`
- blocking_dependency: `2A-1c`
- codex_can_autorun: `yes`
- Owner: Codex
- Estimated time: 5-10 min
- Prerequisite: none
- Verify:
  - later commander execution must run in local mode
  - remote compact must not be on the critical path
- Suggested proof:
  - record the local-mode invocation pattern to be used for STEP3
- Success condition:
  - STEP3 prompt author has an exact local-mode run assumption

### [x] 2A-3 `pack_lint v2.5` upgrade surface note

- execution_mode: `subagent_parallel`
- blocking_dependency: `2A-1c`
- codex_can_autorun: `yes`
- Owner: Codex
- Estimated time: 20-30 min
- Prerequisite: none
- Important boundary:
  - define upgrade scope now
  - do not implement it inside STEP2
- Minimum note must cover:
  - dual mode validation for `manifest.jsonl` and full `dispatch.md`
  - frontmatter/schema checks
  - handoff chain validation
  - stop-class detectability
  - no live PR number hardcode
- Success condition:
  - this can later become an early Dispatch127 item without re-thinking scope

### [x] 2A-4 raw runs directory scaffold

- execution_mode: `subagent_parallel`
- blocking_dependency: `2A-1c`
- codex_can_autorun: `yes`
- Owner: Codex
- Estimated time: 10-15 min
- Prerequisite: none
- Prepare path conventions for:
  - `runs/Dispatch127-176-<timestamp>/`
  - `screenshots/`
  - `cloud-drafts/`
  - `audit/`
- Success condition:
  - STEP3 prompt author can reference stable output locations

### [x] 2A-5 Playwright / screenshot / localhost readiness note

- execution_mode: `subagent_parallel`
- blocking_dependency: `2A-1c`
- codex_can_autorun: `yes`
- Owner: Codex
- Estimated time: 20-30 min
- Prerequisite: none
- Clarify:
  - what can be prepared now
  - what cannot be actually exercised until scaffold/frontend exists
- Must distinguish:
  - pre-existing screenshot/audit pipeline readiness
  - future `pnpm dev` / localhost entry once frontend exists
- Success condition:
  - no false assumption that visual automation is fully runnable now if product code is not present yet

### [x] 2A-6 GitHub plan / runner / API / disk verification

- execution_mode: `subagent_parallel`
- blocking_dependency: `2A-1c`
- codex_can_autorun: `yes`
- Owner: Codex
- Estimated time: 15-25 min
- Prerequisite: none
- Verify:
  - GitHub Actions concurrent runner limit
  - GitHub API rate budget assumptions
  - worktree disk budget
  - local machine tolerance for staged `10 -> 20` pool rollout
- Record operating rule:
  - if runner capacity behaves like free plan `5`, later pool cap should be `10-12`
  - if Pro/team capacity supports it, keep target `20`
- Success condition:
  - STEP3 prompt author knows whether `20` remains realistic or must be capped

### [x] 2A-7 GitHub access prep

- execution_mode: `main_window_sequential`
- blocking_dependency: `2A-1a 2A-8 branch_protection_user_merge`
- codex_can_autorun: `yes_unless_branch_protection`
- Owner: Codex
- Estimated time: 30-60 min
- Prerequisite: 2A-1a, 2A-8
- Required GitHub-visible merges:
  - `dispatch127-176-pack-design-v3-2026-05-05.md`
  - `step2-prep-checklist-2026-05-05.md`
- Explicit non-merge:
  - V1
  - V2
- Success condition:
  - Cloud ChatGPT Pro can read the canonical spec and the STEP2 checklist from `origin/main`

### [x] 2A-8 repo state cleanup

- execution_mode: `main_window_sequential`
- blocking_dependency: `2A-1c`
- codex_can_autorun: `yes`
- Owner: Codex
- Estimated time: 20-30 min
- Prerequisite: 2A-1a
- Actions:
  - archive V1/V2 to raw trail path
  - keep V3 as canonical repo candidate
  - ensure no unrelated dirty files remain in the way
- Preferred archival policy:
  - move V1/V2 to `~/workspace/raw/05-Projects/ScoutFlow/dispatches/archive/v1-v2-spec-trail-2026-05-05/`
- Success condition:
  - repo only carries the canonical candidate docs needed for cloud access
  - raw retains audit trail for V1/V2

### [x] 2A-9 PRD/SRD Wave 5 scope review + batch1 worklist template extraction

- execution_mode: `subagent_parallel`
- blocking_dependency: `2A-1c`
- codex_can_autorun: `yes`
- Owner: Codex
- Estimated time: 60-90 min
- Prerequisite: 2A-1 complete
- Canonical inputs:
  - [PRD-v2-2026-05-04.md](/Users/wanglei/workspace/ScoutFlow/docs/PRD-v2-2026-05-04.md)
  - [SRD-v2-2026-05-04.md](/Users/wanglei/workspace/ScoutFlow/docs/SRD-v2-2026-05-04.md)
  - [prd-v2.1-strong-visual-h5-para-pr-factory-candidate-2026-05-04.md](/Users/wanglei/workspace/ScoutFlow/docs/PRD-amendments/prd-v2.1-strong-visual-h5-para-pr-factory-candidate-2026-05-04.md)
  - [db-vnext-srd-v3-candidate-2026-05-04.md](/Users/wanglei/workspace/ScoutFlow/docs/SRD-amendments/db-vnext-srd-v3-candidate-2026-05-04.md)
  - [h5-bridge-para-vault-srd-v3-candidate-2026-05-04.md](/Users/wanglei/workspace/ScoutFlow/docs/SRD-amendments/h5-bridge-para-vault-srd-v3-candidate-2026-05-04.md)
- Context input:
  - [scoutflow-doc3-amend-pr76-pr125-worklist-2026-05-05.md](</Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/packs/ScoutFlow-PR76-PR125-dispatch-pack-2026-05-05-b2v4/scoutflow-doc3-amend-pr76-pr125-worklist-2026-05-05.md>)
- Required outputs:
  - Wave 5 PRD/SRD section index
  - batch1 worklist structure extraction
  - implemented-vs-unimplemented mapping for Dispatch127-176 continuation
- Suggested output path:
  - `docs/research/repairs/wave5-scope-and-template-extraction-2026-05-05.md`
- Success condition:
  - `BACKBONE-TAXONOMY.md` later has anchored `contract_source` candidates instead of vague theme generation
  - batch1 worklist structural template draft exists and can be reused when shaping BACKBONE

## 4. STEP2B Batch2 terminal + 1h window

Target: do these after Batch2 / Dispatch91-110 reaches terminal state.

Estimated wall time: about 1 hour if STEP2A is already clean.

### [ ] 2B-1 Batch2 one-page audit/repair summary

- execution_mode: `wait_then_main`
- blocking_dependency: `Batch2_terminal`
- codex_can_autorun: `yes_after_preflight_resolution`
- Owner: Codex
- Estimated time: 15-20 min
- Prerequisite: Batch2 terminal state
- Must summarize:
  - actual end-state
  - remaining audit notes
  - any facts Cloud ChatGPT Pro should know but should not read from long raw reports
- Success condition:
  - a short current-fact layer exists for STEP3 input packaging

### [ ] 2B-2 Cloud input package inventory with tier and visibility state

- execution_mode: `wait_then_main`
- blocking_dependency: `2B-1`
- codex_can_autorun: `yes`
- Owner: Codex
- Estimated time: 15-20 min
- Prerequisite: 2B-1
- Every item must be tagged with:
  - `tier`: canonical / context / optional / forbidden
  - `visibility_state`: `origin/main` / `candidate branch` / `local only`
- Success condition:
  - STEP3 prompt author can decide exactly what to paste/reference to Cloud ChatGPT Pro

#### Explicit tier table

| Tier | File | Use |
|---|---|---|
| `canonical` | `V3 spec` + `STEP2 checklist` + `BACKBONE-TAXONOMY.md` + `READBACK-MANIFEST.md` | main spec + input contract |
| `canonical` | `PRD-v2` + `SRD-v2` + `PRD-v2.1 amendment` + `2x SRD-v3 amendments` | business-direction anchors; candidate addenda should be labeled as promoted for B2 planning/contract baseline via `T-P1A-103`, not as globally promoted base docs |
| `context` | batch1 worklist `scoutflow-doc3-amend-pr76-pr125-worklist-2026-05-05.md` | structural template for Cloud draft |
| `context` | `docs/current.md` + `docs/task-index.md` + `docs/decision-log.md` + `docs/specs/contracts-index.md` + `docs/shoulders-index.md` | authority state |
| `context` | `docs/dispatch-template.md` | dispatch writing shape |
| `context` | Batch2 one-page audit/repair summary | freshest state layer |
| `optional` | existing dispatch `.md` samples from batch1/b2v4 | style/reference only |
| `optional` | existing runtime-log / RUN-SUMMARY samples if present | post-run format hints |
| `forbidden` | `migrations/**` / `.env` / raw credentials / raw stdout with tokens | never expose to cloud |

### [ ] 2B-3 `READBACK-MANIFEST.md` generation + GitHub visibility

- execution_mode: `wait_then_main`
- blocking_dependency: `2B-1 branch_protection_user_merge`
- codex_can_autorun: `yes_unless_branch_protection`
- Owner: Codex
- Estimated time: 15-20 min
- Prerequisite: 2B-1
- Rule:
  - this is not just a local note
  - it must be merged to `origin/main` if Cloud ChatGPT Pro is supposed to consume it
- Success condition:
  - cloud can read the final readback contract through GitHub

### [ ] 2B-4 handoff to STEP3 prompt author

- execution_mode: `wait_then_main`
- blocking_dependency: `2B-2 2B-3 2B-5`
- codex_can_autorun: `yes`
- Owner: Codex
- Estimated time: 10-15 min
- Prerequisite: 2B-2, 2B-3, 2B-5
- Handoff must include:
  - canonical files
  - context files
  - visibility-state notes
  - any known exclusions
  - current pool/rate-limit assumptions
- Success condition:
  - STEP3 prompt author can write a cold-start prompt without further repo archaeology

### [ ] 2B-5 `BACKBONE-TAXONOMY.md` anchored contract generation + GitHub visibility

- execution_mode: `wait_then_subagent`
- blocking_dependency: `2A-9 2B-3 Batch2_terminal`
- codex_can_autorun: `yes_after_preflight_resolution`
- Owner: Codex
- Estimated time: 90-120 min
- Prerequisite: 2A-9 complete + Batch2 terminal + `READBACK-MANIFEST.md` ready
- Contract-source rule for every entry:
  - anchor to `PRD-v2 §X.Y`
  - or `SRD-v2 §Y.Z`
  - or `PRD-v2.1 §Z`
  - or `SRD-v3 db-vnext §W`
  - or `SRD-v3 h5-bridge §V`
  - or `batch1 worklist §M/range`
  - or `inference`, which must include `inference_from + risk_flag: tentative`
- Structural guidance:
  - reuse batch1 worklist section logic where useful: overview, per-dispatch fields, file-domain matrix, errata, verdict-like constraints
- Overflow rule:
  - if a valid theme extends beyond the 50-slot budget, classify it as `overflow_candidate` for Wave 6 rather than forcing it into Dispatch127-176
- Codex validation rule:
  - every claimed `PRD/SRD §X.Y` anchor must be grep-verifiable in the referenced file
- Visibility rule:
  - `BACKBONE-TAXONOMY.md` must be merged to `origin/main`
- Success condition:
  - Cloud ChatGPT Pro receives a bounded content-origin contract instead of inventing Wave 5

## 5. Artifact Disposition Rules

### Canonical repo-tracked candidates

- `dispatch127-176-pack-design-v3-2026-05-05.md`
- `step2-prep-checklist-2026-05-05.md`
- later: `BACKBONE-TAXONOMY.md`
- later: `READBACK-MANIFEST.md`

### Raw-only archive artifacts

- `dispatch127-176-pack-design-2026-05-05.md`
- `dispatch127-176-pack-design-v2-2026-05-05.md`

Archive destination:

`~/workspace/raw/05-Projects/ScoutFlow/dispatches/archive/v1-v2-spec-trail-2026-05-05/`

### Local-only artifacts

- transient scratch notes
- temporary summaries before canonicalization
- any file under `.gitignore`d `plan/`

## 6. Suggested Execution Order

1. Finish `2A-1` through `2A-3`
2. Clean repo state and archive V1/V2 via `2A-8`
3. Run GitHub access prep via `2A-7`
4. Let Opus finish `2A-9`
5. Wait for Batch2 terminal state
6. Execute `2B-1` through `2B-5`
7. Hand everything to STEP3 prompt author

## 7. Exit Criteria

STEP2 can be called `verdict=ready_for_step3_authoring` only if:

- `T-P1A-105` is consistent
- V3 and this checklist are visible on `origin/main`
- V1/V2 are archived out of the repo working set
- Batch2 one-page summary exists
- tiered cloud input inventory exists
- `READBACK-MANIFEST.md` is visible on `origin/main`
- `BACKBONE-TAXONOMY.md` is visible on `origin/main`
- no hidden local-only dependency remains in the STEP3 cold-start path

## 8. Self-Review

- No unresolved placeholder or ambiguous completion wording should remain in this checklist.
- This checklist should remain mechanical and execution-oriented, not expand into a fourth large design spec.
- Cloud-access constraints should be explicit, not implied.
- `V3` should remain the only canonical spec-level design doc for cloud use.
