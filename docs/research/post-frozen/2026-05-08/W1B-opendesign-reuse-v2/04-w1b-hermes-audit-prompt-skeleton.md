---
title: W1B Hermes External Audit Prompt Skeleton — v2 Cluster Spec + Dispatch Pack 外审
status: candidate / audit_prompt_skeleton
authority: not-authority
created_by: gpt-pro (skeleton 模板, CC1/战友填充 paste 给 Hermes web)
parent_cluster: W1B
parent_spec: 01-w1b-cluster-spec.md
parent_dispatch_pack: 02-w1b-dispatch-pack.md
target_executor: Hermes (3rd party, GPT-5 base, independent auditor)
expected_runtime: ~30-60 min Hermes thinking
disclaimer: "撰写时刻 2026-05-08 北京历史参考；GitHub live 以 main HEAD 与 authority docs readback 为准"
prerequisite_check_status: "Check 1 refreshed: START-HERE/current.md authority anchor reports main=c802de4 PR #247 while commit search shows latest commit 6dd27d7 PR #245; Active 0/3, Authority writer 0/1, WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED, write_enabled=false. Check 2 refreshed: task-index Active row empty, W1B not registered. Check 3 refreshed: PR #122/#243/#245/#246/#247/#248 merged; no W1B land detected. Check 4 refreshed: docs/memory/INDEX.md batch_count=17; prompt inline 7 codex-metacognition instincts treated as hard local input plus PR246 sediment context."
write_enabled: false
authority_files_writable: false
not_implementation: true
not_authority: true
not_runtime_approval: true
not_migration_approval: true
not_package_approval: true
---

# W1B Hermes External Audit Prompt Skeleton

> Hermes: You are the independent external auditor. Audit candidate markdown only. Do not implement, rewrite, promote, or approve runtime/package/migration/browser/raw-vault lanes.

## §0 Hermes role

You provide a third-party audit verdict for W1B OpenDesign reuse v2 candidate docs. Your review is advisory but important. User V-PASS remains the final decision gate.

## §0.5 Prerequisite Check — Hermes must run first

Read and compare live state from:

1. `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md`
2. `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md`
3. `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/decision-log.md`
4. `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/memory/INDEX.md`

GPT Pro production-time readback:

- authority anchor: `c802de4`/PR #247;
- recent commit search: `6dd27d7`/PR #245;
- Active `0/3`, Authority writer `0/1`, W1B not registered;
- PR #122/#243/#245/#246/#247/#248 verified merged;
- memory INDEX batch_count=17; prompt inline 7 instincts treated as hard pasted input.

If this has drifted, report live truth. Do not silently adopt historical numbers.

## §1 Audit scope

Audit these two primary files:

1. `01-w1b-cluster-spec.md`
2. `02-w1b-dispatch-pack.md`

Optional context:

- `03-w1b-codex-commander-prompt-skeleton.md` for implementation handoff consistency.
- This file (`04`) is the audit prompt, not an object of self-audit.

## §2 Inputs to paste inline

CC1/user should paste:

- Full text of 01 cluster spec.
- Full text of 02 dispatch pack.
- If useful: 03 Codex skeleton.
- Reference raw URLs: master spec §7.1/§13/§15.2/§16, v1 OpenDesign ledger, PR #243 baseline files, capture-station package.json, TrustTrace.tsx.

Hermes should not infer private/local files that are not pasted or accessible.

## §3 Audit Checklist

### 3.1 Single-point boundary check

Questions:

- Does v2 allow at most one graph library and only for `PF-C4-EXT-graph`?
- Does it keep timeline and error-path self-rolled?
- Does it require self-rolled attempt first?
- Does it require user gate + Hermes pass before path-B?
- Is the 50kB gzip bundle budget labeled candidate and evidence-based?
- Does tree-shaking evidence apply to the exact library/import style?

Verdict: PASS / CONCERN / REJECT.

### 3.2 Vendored UI/styling drift check

Questions:

- Do the docs avoid bringing in shadcn/Radix/TanStack/React Flow/Zustand/Lucide/styling package families?
- Do they distinguish one graph-lib single-point path from a vendored framework?
- Do they reject donor source transplant and donor IA/class-name copying?
- Do they keep OpenDesign reference-only and shadcn-admin adapt-only?

Verdict: PASS / CONCERN / REJECT.

### 3.3 v1 → v2 delta reasonableness

Questions:

- Does v2 start at v2-D16/v2-E7 and avoid rewriting v1-D1~D15/v1-E1~E6?
- Does v2 extend only v1-D5 package/styling strategy, not all frontend reuse?
- Does v1-D4 transplant rejection remain intact?
- Does v1-D6 React 18 posture remain intact?
- Does v1-D3 donor split stay distinct from `PF-C4-EXT-graph` and `npm d3`?

Verdict: PASS / CONCERN / REJECT.

### 3.4 REGENERATE anti-pattern enforce check

Questions:

- Are anti-patterns 9-15 present and actionable?
- Are Tailwind/shadcn/Panda/React upgrade/hex hardcoding/runtime-lane/migration-lane violations hard stops?
- Are TODO placeholders honest rather than disguised completion claims?
- Is file-count estimate discipline included with `find <dir> -type f | wc -l`?

Verdict: PASS / CONCERN / REJECT.

### 3.5 Authority and boundary check

Questions:

- Does every file frontmatter say candidate and not-authority?
- Is there no promotion/current-state assertion by these candidate docs?
- Are 5 overflow lanes kept on Hold?
- Are authority files absent from candidate deliverable write lists?
- Is optional authority-writer registration separated into its own dispatch?

Verdict: PASS / CONCERN / REJECT.

### Cross-cutting A — PR citation verification

Check PR #122, #243, #245, #246, #247, #248 state and mergedAt if you cite them. Report any mismatch with GPT Pro readback.

### Cross-cutting B — truth disclaimer sweep

Find all hard numbers or state claims: main SHA, PR #, active count, bundle budget, dispatch count, runtime status. Confirm they have a historical/live disclaimer or evidence trail.

## §4 Verdict scale

| Verdict | Criteria | Action |
|---|---|---|
| V-PASS | 5 checklist items + 2 cross-cutting checks pass; no material concern. | W1B docs usable. |
| V-PASS-WITH-CONCERN | All hard boundaries pass; 1-3 minor concerns. | Usable if user accepts concerns. |
| V-CONCERN | One or two material concerns without hard-boundary failure. | Amend before implementation or force self-rolled path. |
| V-REJECT | Any hard-boundary violation, multiple graph libs, transplant drift, overflow drift, status promotion, or missing anti-pattern gates. | Stop W1B path until corrected. |

## §5 Output format for Hermes report

Use this report structure:

```markdown
# Hermes Audit Report — W1B OpenDesign Reuse v2

## Verdict
V-PASS | V-PASS-WITH-CONCERN | V-CONCERN | V-REJECT

## Evidence table
| Check | Verdict | Evidence quote | Concern |
|---|---|---|---|
| 3.1 Single-point boundary | | | |
| 3.2 Vendored UI/styling drift | | | |
| 3.3 v1→v2 delta | | | |
| 3.4 REGENERATE anti-patterns | | | |
| 3.5 Authority/boundary | | | |
| Cross-cutting A PR verify | | | |
| Cross-cutting B disclaimer | | | |

## Required fixes
- ...

## Optional recommendations
- ...

## Hermes self-flag
- ...
```

## §6 Hermes non-goals

- Do not implement code.
- Do not rewrite the four markdown deliverables.
- Do not promote candidate docs to authority.
- Do not approve dependency, runtime, migration, browser automation, or raw vault changes.
- Do not choose path-A/path-B for the user; only audit whether the gate is safe.
- Do not audit unrelated ScoutFlow waves beyond evidence needed for W1B.

## Self-flag

- ⚠️ Hermes may not be able to validate bundle size without a local build artifact; mark it as evidence-required, not pass/fail by assumption.
- ⚠️ The split-truth between authority anchor and recent commit search needs live readback during Hermes audit.
- ⚠️ If 01/02 are pasted but raw GitHub references are unavailable, audit the pasted text and flag missing external evidence.
- ⚠️ A 30-60 min audit should focus on hard boundaries first; minor copy-edit issues should not dominate the verdict.
