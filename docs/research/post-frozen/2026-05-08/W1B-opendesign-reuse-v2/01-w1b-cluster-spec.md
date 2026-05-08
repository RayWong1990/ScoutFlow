---
title: W1B OpenDesign Reuse v2 Cluster Spec — Single-Point Upgrade Path + Hermes Pre-Audit
status: candidate
authority: not-authority
created_by: gpt-pro (one-shot 60min thinking, 2026-05-08)
parent_cluster: W1B (PF-C4-EXT 3 TODO 自写 — PF-C4-EXT-graph / timeline hover / error-path highlight)
parent_spec_v1: docs/research/repairs/opendesign-reuse-strategy-candidate-2026-05-05.md (PR #122 merged 2026-05-05)
delta_target: v1 D1-D15 + E1-E6 (do not rewrite; add v2-D16+ / v2-E7+ only)
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

# W1B OpenDesign Reuse v2 Cluster Spec

> This is a candidate spec for W1B only. It is not an authority writeback, not implementation, not runtime enablement, not migration enablement, not a package decision, and not a promotion of PRD/SRD.  
> Namespace rule: use `v1-D3` for the reuse-ledger donor split, `PF-C4-EXT-graph` for the Trust Trace graph submodule, and `npm d3` for the optional single-point graph library.

## §0.5 Prerequisite Check — refreshed before output

| Check | Live readback | W1B effect |
|---|---|---|
| Check 1 — current state | `docs/00-START-HERE.md` and `docs/current.md` authority anchor report `main=c802de4` / PR #247; commit search shows latest commit `6dd27d7` / PR #245. Active product lane `0/3`; Authority writer `0/1`; state `WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`; write_enabled=false. | Treat as split-truth drift. W1B files must carry the historical-reference disclaimer and must not hard-code a single promoted main fact beyond readback evidence. |
| Check 2 — task-index | Active table empty; no W1B Active row registered. | W1B spec/dispatch remains candidate until an authority-writer dispatch registers lane. |
| Check 3 — decision/PR chain | PR #122, #243, #245, #246, #247, #248 verified merged. No W1B upgrade PR detected. | OpenDesign v1 is landed as candidate input; W1B v2 is new candidate delta only. |
| Check 4 — memory | `docs/memory/INDEX.md` reports batch_count=17 cross-vendor memory. The prompt’s 7 inline codex-metacognition instincts are treated as hard local input plus PR246 sediment context. | Keep file-count, candidate-vs-authority, 24h consumer, master-spec scan, U mapping, cross-vendor audit, and PR-verify instincts in all handoffs. |

## §1 Mission & Scope

W1B upgrades the OpenDesign reuse strategy from v1 to v2 **only to support the PF-C4-EXT Trust Trace 3 TODO cluster**: `PF-C4-EXT-graph`, `PF-C4-EXT-timeline`, and `PF-C4-EXT-error-path`.

The goal is narrow: decide how to handle a possible graph-library single-point upgrade without reopening the entire frontend reuse policy. W1B v2 does not rewrite v1, does not approve donor transplant, does not promote package strategy globally, and does not change the `apps/capture-station` visual stack by itself.

The 24h actionable consumer is Codex: the dispatch pack gives Codex a concrete gate for self-rolled graph work first, then a conditional fallback to one graph dependency if the self-rolled path fails under bounded criteria.

## §2 v1 Ledger Recap — one-page summary, not a rewrite

| v1 key | Summary | W1B v2 posture |
|---|---|---|
| v1-D1 | OpenDesign role = visual proof source / design-language donor / visual vocabulary candidate. | Unchanged; OpenDesign remains reference-only. |
| v1-D2 | Cloud entry layer = local candidate doc + lightweight handoff amend. | Unchanged; GPT Pro produces candidate docs only. |
| v1-D3 | Donor split = shadcn-admin owns structure, OpenDesign owns visual mood. | Unchanged; do not confuse with PF-C4-EXT-graph. |
| v1-D4 | Reuse level = OpenDesign reference, shadcn-admin adapt, transplant rejected by default. | Unchanged; v2 does not unlock transplant. |
| v1-D5 | Package/styling = future strategy candidate only. | Extended narrowly by v2-D16~D21 for a graph-lib single-point slot. |
| v1-D6 | React posture = current React 18 alignment. | Unchanged; no React upgrade in W1B. |
| v1-D7 | STEP3 prompt hard clause. | Historical / obsolete for W1B except as style precedent. |
| v1-D8 | Visual slot influence constrains existing H5/visual rows. | Unchanged; W1B affects Trust Trace only. |
| v1-D9 | Reject list is full and has no Cloud carve-out. | Unchanged; copied into W1B gates. |
| v1-D10 | Amend target limited to the handoff packet. | Historical; W1B uses a new 4-file candidate output folder. |
| v1-D11 | Claim labeling = canonical fact / inference / tentative candidate. | Unchanged; W1B uses explicit candidate labels. |
| v1-D12 | Unused numbering slot. | Remains unused; W1B starts at v2-D16. |
| v1-D13 | H5 layer ownership = L1 internal / L2 shadcn-admin / L3 OpenDesign. | Unchanged; graph UX belongs to ScoutFlow Trust Trace, not donor IA. |
| v1-D13a | Layer notation is prose-only. | Unchanged; no schema field. |
| v1-D13b | L1 source mention anchors internal H5 IA. | Unchanged. |
| v1-D14 | Visual review acceptance for apps/H5 touchpoints. | Extended by W1B to require evidence for graph/timeline/error-path rendering. |
| v1-D15 | Prompt-ready policy block allowed as candidate. | Unchanged; W1B emits prompt skeletons. |
| v1-E1 | Zero-install styling = CSS Variables + CSS Modules + container queries + safe motion. | Default path for all three PF-C4-EXT TODO. |
| v1-E2 | Donor freeze = shadcn-admin frozen commit. | Unchanged. |
| v1-E3 | L2/L3 collision resolved via CSS Variables, no fork/transplant. | Unchanged. |
| v1-E4 | Visual mode = Tech Utility / operator workstation + reduced-density + reduced-motion. | Unchanged; W1B must preserve operator workstation tone. |
| v1-E5 | Visual evidence expected for visual touchpoints. | Extended by v2-E7 evidence receipt. |
| v1-E6 | Token consumption = CSS Variables primary, TS mirror secondary. | Unchanged; no hardcoded visual constants. |

Locked boundary recap:

- OpenDesign remains visual reference, not code/package/runtime source.
- shadcn-admin remains adapt-only structural reference, frozen to the known reference commit.
- Transplant remains rejected by default.
- React stays aligned with the current React 18 app surface.
- The current capture-station package surface is minimal: React / React DOM only at runtime.

## §3 v2 Delta — D Path Single-Point Upgrade Candidates

### §3.1 D path definition

D path means: a future implementation lane may propose **one graph-library single-point upgrade** for `PF-C4-EXT-graph` if the default self-rolled path fails under bounded evidence. It is the master-spec §16.2 graph-lib escape hatch, not a general package lane.

D path does not apply to timeline hover or error-path unless a later spec explicitly proves those submodules cannot be handled with CSS Variables, RAF, and native React state.

### §3.2 Candidate single-point upgrade list

| Candidate | Target TODO | Lib posture | ROI | Risk | Hermes review need | W1B v2 decision |
|---|---|---|---|---|---|---|
| A | PF-C4-EXT-graph | self-rolled CSS + SVG + React state | High: zero new dependency, maximum boundary safety | Medium: force layout math can expand | LOW | Default path. |
| B | PF-C4-EXT-graph | `npm d3` single-point graph/math library | High: battle-tested force simulation primitives | Medium: new dependency and tree-shaking proof required | HIGH | Conditional fallback only. |
| C | PF-C4-EXT-graph | cytoscape single-point graph package | Medium: graph-specialized | High: heavier runtime surface / bundle-size risk | HIGH | Not recommended unless d3 fails. |
| D | PF-C4-EXT-graph | vis-network single-point graph package | Medium | High: maintenance / bundle-shape concern | HIGH | Not recommended for W1B. |
| E | PF-C4-EXT-timeline | self-rolled CSS Variables + RAF | High | Low | LOW | Default and only path for W1B. |
| F | PF-C4-EXT-error-path | self-rolled path backtrace + breadcrumb state | High | Low | LOW | Default and only path for W1B. |

<!-- TODO: cytoscape vs npm d3 vs vis-network ROI table is best-effort here; leave package freshness, ESM export shape, and actual bundle delta to CC0/CC1 live verification. -->

### §3.3 Recommendation

Recommended path for W1B:

1. Run a bounded **self-rolled spike** for `PF-C4-EXT-graph` first.
2. Use `npm d3` only if the spike records a concern such as uncontrolled implementation size or <30fps browser behavior under the fixture graph.
3. Keep `PF-C4-EXT-timeline` and `PF-C4-EXT-error-path` self-rolled.
4. Never bring in a full UI/styling framework, graph framework bundle, or donor source tree to solve this cluster.

<!-- TODO: bundle size budget 50kB gzip is a candidate threshold; CC0/CC1 should measure current capture-station baseline before enforcing it as a hard merge gate. -->

## §4 v2 Decision Ledger — delta only

| v2 key | Decision | Locked choice | Boundary |
|---|---|---|---|
| v2-D16 | Single-point upgrade scope | At most one graph library, and only for `PF-C4-EXT-graph`. | It must not spread to the other 13 surfaces or timeline/error-path. |
| v2-D17 | Self-rolled fallback-first posture | Default is self-rolled. Single-point path opens only after a 5h bounded spike yields `concern` or `partial` with evidence. | Codex cannot choose the fallback alone; user V-PASS gate required. |
| v2-D18 | Hermes external audit | Any single-point dependency path needs Hermes V-PASS or V-PASS-WITH-CONCERN before local implementation proceeds. | Hermes is advisory; user gate remains final. |
| v2-D19 | Bundle budget | Candidate budget: new graph lib delta ≤ 50kB gzip. | Threshold is candidate; must be measured before use. |
| v2-D20 | Tree-shaking enforce | Candidate lib must expose ESM tree-shakable imports and evidence must show only needed modules bundled. | Excludes libraries with opaque monolithic bundle behavior. |
| v2-D21 | Transplant posture | v1-D4 transplant rejection remains locked. | No donor files, no OpenDesign code, no shadcn-admin implementation files. |
| v2-D22 | Trust Trace scope containment | W1B may touch Trust Trace feature and local receipts only. | No authority docs, migrations, workers, packages workspace, data, raw vault, or reference clone. |
| v2-D23 | Citation-chain deferral | Citation chain remains outside W1B. | W1B replaces 3 placeholders, not all Trust Trace future work. |
| v2-E7 | Single-point evidence receipt | Required evidence: before/after bundle size, ESM/tree-shaking proof, Hermes receipt, and user gate receipt. | Missing any item → fallback to self-rolled or stop. |
| v2-E8 | Revert/fallback path | If single-point path fails audit or size budget, revert to self-rolled and record concern. | Do not escalate to multiple libraries. |
| v2-E9 | Visual/render evidence | W1B closeout includes screenshot or local browser visual note if browser execution is permitted by current gate; otherwise explicit blocked note. | No pretending visual terminal review happened. |

## §5 v1 → v2 Delta Diff Summary

| v1 Decision | v2 Status | Delta |
|---|---|---|
| v1-D1 OpenDesign role | unchanged | Reference-only visual source. |
| v1-D2 cloud entry | unchanged | Candidate docs only. |
| v1-D3 donor split | unchanged | shadcn-admin structure / OpenDesign visual mood; distinct from graph module. |
| v1-D4 reuse level transplant | unchanged | Rejected by default. |
| v1-D5 package strategy | EXTENDED | v2-D16~D21 add one graph-lib single-point slot. |
| v1-D6 React posture | unchanged | React 18 alignment. |
| v1-D7 STEP3 prompt | historical | Not a W1B authority source. |
| v1-D13 H5 layer ownership | unchanged | L1/L2/L3 split preserved. |
| v1-E1 zero-install styling | unchanged | Default self-rolled path. |
| v1-E5 visual evidence | EXTENDED | v2-E7/v2-E9 add graph-path evidence receipt. |
| v1-E6 token consumption | unchanged | CSS Variables primary. |

## §6 Hard Boundaries

```yaml
write_enabled: false
authority_files_writable: false
not_implementation: true
not_authority: true
not_runtime_approval: true
not_migration_approval: true
not_package_approval: true

5_overflow_lane_hold:
  - true_vault_write
  - runtime_tools
  - browser_automation
  - dbvnext_migration
  - full_signal_workbench

4_status_words_only:
  - current authority
  - promoted addendum
  - candidate north-star
  - reference storage

3_reuse_levels:
  - reference (cite/observe only, no code/package/IA reuse)
  - adapt (translate patterns into ScoutFlow-native docs/specs/tasks)
  - transplant (direct copy/near-copy; rejected by default)
```

### Allowed output paths for these four candidate deliverables

- `docs/research/post-frozen/2026-05-08/W1B-opendesign-reuse-v2/01-w1b-cluster-spec.md`
- `docs/research/post-frozen/2026-05-08/W1B-opendesign-reuse-v2/02-w1b-dispatch-pack.md`
- `docs/research/post-frozen/2026-05-08/W1B-opendesign-reuse-v2/03-w1b-codex-commander-prompt-skeleton.md`
- `docs/research/post-frozen/2026-05-08/W1B-opendesign-reuse-v2/04-w1b-hermes-audit-prompt-skeleton.md`

### Forbidden write domains for W1B derived work

- Authority files unless a separate authority-writer dispatch exists.
- PRD/SRD promoted files.
- Historical run ledgers and historical external-audit reports.
- `services/api/migrations/**`, `workers/**`, `packages/**`, `data/**`.
- `~/workspace/raw/**` and `referencerepo/open-design/**`.

## REGENERATE Anti-pattern Gate — package / transplant / runtime boundary

These are hard REGENERATE signals for any downstream draft, dispatch, or PR body generated from this file:

9. REGENERATE: 引整套 vendored UI 进 `apps/capture-station` — shadcn / Radix / TanStack / React Flow / Zustand / Lucide / styled-components / @emotion / Mantine / Ant Design / Chakra UI / @mui 等 UI/styling 全家桶不得进入 dependency surface。
10. REGENERATE: transplant donor files — 不复制 OpenDesign / shadcn-admin 整套源码、IA、layout primitives、class names、package assumptions 进 `apps/capture-station`。
11. REGENERATE: React 18 → 19 upgrade — v1-D6 仅允许 later spike candidate，本 W1B v2 不做版本升级。
12. REGENERATE: Tailwind / shadcn / Panda package install — v1-D5 保持 future strategy candidate only；本 v2 只讨论 graph single-point slot。
13. REGENERATE: Hex hardcoding — 除 `tokens.css` / density / type-weight token files 外，组件与 dispatch 不写硬编码色值。
14. REGENERATE: runtime lane 偷开 — BBDown live / yt-dlp / ffmpeg / ASR / browser automation / migration runtime 均不得因 W1B 启动而解禁。
15. REGENERATE: 把 D 路径误读成“禁止外引” — D 路径是单点引一个 graph lib 的候选升级路径；它不是整套 vendored UI，也不是默认外引许可。

## §7 Hermes External Review Hand-off

Hermes should audit these five items before W1B single-point path is used:

1. Single-point boundary: at most one graph lib; scoped only to Trust Trace graph.
2. No vendored framework drift: no shadcn/Radix/TanStack/React Flow/Zustand/Lucide/styling package family.
3. v1→v2 delta correctness: v2-D16~D23 and v2-E7~E9 extend v1-D5 only; no v1 rewrite.
4. Evidence sufficiency: bundle delta, tree-shaking proof, local build, and receipt trail.
5. Authority safety: candidate status, no W1B authority row claim, no overflow lane change.

Verdict scale:

| Verdict | Meaning | W1B action |
|---|---|---|
| V-PASS | No blocking issue. | Proceed with current gate plan. |
| V-PASS-WITH-CONCERN | Minor concern only. | Proceed if user accepts concern. |
| V-CONCERN | 1-2 material concerns. | Amend candidate docs or choose self-rolled. |
| V-REJECT | Any hard boundary issue. | Kill path and wait for user decision. |

## §8 Self-verification Checklist

| Item | Result |
|---|---|
| 4 deliverables self-contained | PASS |
| Frontmatter candidate + not-authority | PASS |
| §0.5 prerequisite check embedded | PASS |
| v1 ledger not rewritten | PASS |
| v2 starts at D16/E7 | PASS |
| D path treated as legal single-point candidate, not global package lane | PASS |
| Transplant rejection preserved | PASS |
| 5 overflow lane Hold preserved | PASS |
| Truth disclaimer embedded | PASS |
| TODO placeholders present | PASS |
| Authority files absent from write list | PASS |
| Namespace disambiguation present | PASS |


## §9 W1B Implementation Handoff Schema

Downstream Codex receipts should preserve this handoff schema so CC0/CC1/Hermes can audit without reading code first.

| Field | Required value | Notes |
|---|---|---|
| `lane_id` | `W1B-PF-C4-EXT` | Must match dispatch pack. |
| `path` | `path-A-self-rolled` / `path-B-npm-d3` / `kill` | Derived only from D-W1B-006. |
| `graph_result` | `clear` / `concern` / `partial` / `reject` | Separate from timeline/error-path. |
| `timeline_result` | `clear` / `concern` / `partial` / `reject` | Self-rolled only. |
| `error_path_result` | `clear` / `concern` / `partial` / `reject` | Self-rolled only. |
| `package_diff` | `none` or `d3-only` | Anything else is hard concern. |
| `bundle_delta_kb_gzip` | measured number or `not-measured-with-reason` | No fabricated numbers. |
| `tree_shaking_evidence` | path to note or `not-applicable-self-rolled` | Required for path-B. |
| `hermes_receipt` | path or `not-applicable-self-rolled` | Required for path-B. |
| `user_gate_receipt` | path | Required for path-B and PR merge. |
| `authority_files_touched` | `no` or explicit authority dispatch ID | Default should be no. |
| `overflow_lanes_changed` | `no` | Any other value is kill. |

## §10 Path A/B State Machine

```text
start
  -> run D-W1B-005 self-rolled graph spike
    -> verdict=clear
      -> path-A self-rolled graph
      -> implement timeline self-rolled
      -> implement error-path self-rolled
      -> validation + closeout
    -> verdict=concern|partial
      -> D-W1B-006 user decision gate
        -> user selects path-A anyway
          -> self-rolled with concern receipt
        -> user selects path-B
          -> require Hermes V-PASS/V-PASS-WITH-CONCERN
          -> run d3-only bundle/tree-shaking preflight
            -> preflight clear
              -> implement graph with d3-only scope
            -> preflight concern|reject
              -> fallback self-rolled or kill
    -> verdict=reject
      -> kill receipt + user decision
```

State-machine invariants:

1. No path can skip D-W1B-005.
2. Path-B cannot skip D-W1B-006.
3. Path-B cannot proceed without external audit receipt.
4. Timeline and error-path never inherit package-path rights from graph.
5. Citation chain remains future work even if all 3 W1B TODO pass.

## §11 Acceptance Criteria for Candidate Promotion to Implementation Prompt

This v2 spec may be used as the basis for Codex implementation only when:

- the four W1B markdown deliverables exist under the allowed candidate path;
- each file frontmatter remains candidate / not-authority;
- Hermes has returned V-PASS or V-PASS-WITH-CONCERN, or the user explicitly chooses to proceed without Hermes for path-A only;
- W1B Active row is registered if current governance requires it;
- no authority writer is occupied by another lane;
- `apps/capture-station/package.json` still has no graph dependency unless path-B preflight is active;
- the user has selected PR strategy A or B;
- CC0/CC1 has checked that no forbidden path appears in the planned diff.

This spec must not be used to justify unrelated frontend work. PF-C4-02 true-data wiring, citation-chain, thumbnails, runtime adapters, ASR, rewrite pipeline, source matrix, and vault commit remain separate waves or lanes.

## §12 TODO Placeholder Policy

W1B can replace three Trust Trace placeholders:

| Placeholder | Expected W1B result | Honest fallback |
|---|---|---|
| `data-todo=trust-trace-graph` | graph component with fixture-backed nodes/edges | keep placeholder with concern receipt if graph fails |
| `data-todo=trust-trace-timeline` | timeline hover/focus component | keep placeholder if evidence focus requires unavailable data |
| `data-todo=trust-trace-error-path` | path backtrace + breadcrumb/highlight | keep placeholder if graph dependency is unresolved |

W1B must not mark citation chain, live runtime, or raw-vault commit as complete. If a placeholder remains, it must include a clear TODO note and a receipt explaining why the work is deferred.

## §13 Package Surface Guardrail

The current capture-station runtime dependency surface is React + React DOM. The single-point graph slot may add only one graph library, and only after the gate sequence. Any package diff must be justified in a receipt with:

- exact package name;
- exact version installed locally;
- before/after bundle-size measurement;
- reason self-rolled path failed or was rejected;
- tree-shaking evidence;
- rollback instructions;
- user gate reference.

Do not turn that receipt into a global package strategy. It is a W1B Trust Trace exception candidate, not a reusable rule for other surfaces.

## §14 Source Evidence Snapshot

| Evidence | Readback used in this spec |
|---|---|
| START-HERE/current authority anchor | main anchor `c802de4` / PR #247; Active 0/3; Authority writer 0/1; WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED. |
| Recent commit search | latest commit-search hit `6dd27d7` / PR #245 memory graph. |
| v1 ledger | PR #122 merged; v1 D1-D15 + E1-E6 remain base ledger. |
| PR #243 baseline | TrustTrace.tsx still contains graph/timeline/error-path TODO placeholders. |
| package surface | capture-station dependencies are React and React DOM; no graph library in current package.json. |
| tokens source | token file owns color values; component specs should reference variables. |
| memory INDEX | 17 cross-vendor memory items present; prompt inline 7 instincts are additional pasted hard input. |

## §15 Self-flag

- ⚠️ Bundle budget `≤50kB gzip` is a candidate threshold; CC0/CC1 should measure current capture-station baseline before enforcing it.
- ⚠️ `npm d3` tree-shaking quality depends on exact import style and bundler output; this spec cannot prove bundle shape without local build evidence.
- ⚠️ The live repo has split-truth between authority anchor (`c802de4`) and recent commit search (`6dd27d7`); downstream closeout should refresh authority anchors before W1B registration.
- ⚠️ The prompt’s inline 7 codex-metacognition instincts are not fully enumerated in `docs/memory/INDEX.md`; this spec treats them as hard pasted input plus PR246 sediment.
