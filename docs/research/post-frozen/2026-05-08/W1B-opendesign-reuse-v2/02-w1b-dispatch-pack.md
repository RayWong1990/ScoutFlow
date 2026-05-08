---
title: W1B Dispatch Pack — OpenDesign Reuse v2 Land + PF-C4-EXT 3 TODO Implementation
status: candidate
authority: not-authority
created_by: gpt-pro (one-shot 60min thinking, 2026-05-08)
parent_cluster: W1B
parent_spec: 01-w1b-cluster-spec.md
target_executor: Codex (Long Runner Coder, 本地 worktree 通宵 5-7h)
total_dispatch: 15
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

# W1B Dispatch Pack

> Candidate dispatch pack only. It gives CC0/CC1/Codex a concrete plan; it does not register a lane, does not modify authority, and does not execute implementation in this document.

## §0.5 Refreshed state summary

- Current authority docs report Active product lane `0/3`, Authority writer `0/1`, and `WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`.
- `task-index.md` Active table is empty; W1B is not currently registered as an Active row.
- Verified PR readback: PR #122 OpenDesign v1, PR #243 PF-C4-01 baseline, PR #245 memory graph, PR #246 governance harness, PR #247 closeout, PR #248 cleanup all merged.
- Split-truth note: authority anchor says `c802de4`/PR #247; commit search says latest commit `6dd27d7`/PR #245. Treat both as evidence until authority refresh closes the lag.

## §1 Dispatch phases

| Phase | Dispatch IDs | Purpose | Gate |
|---|---|---|---|
| Phase 1 — v2 docs land | D-W1B-001~004 | preflight, Hermes pre-review, candidate-doc PR, optional W1B Active row registration | candidate-doc PR + optional authority-writer gate |
| Phase 2 — graph path decision | D-W1B-005~007 | self-rolled spike, decision gate, conditional d3 preflight | user V-PASS before path-B |
| Phase 3 — 3 TODO implementation | D-W1B-008~013 | graph, timeline, error-path, integration, full validation | local validation truthful green/concern |
| Phase 4 — closeout | D-W1B-014~015 | receipt, checkpoint, PR, audit, merge path | CC audit + user V-PASS |

## §2 File-count and estimate discipline

Any downstream estimate such as “~N files touched” must run `find <dir> -type f | wc -l` before appearing in a receipt or PR body. Directory count, glob count, and memory estimates are not acceptable as evidence.

## §3 Dispatch cards


### D-W1B-001: v2 cluster spec pre-flight check

**Mission**: Refresh authority state and lane safety before any W1B doc or implementation action.

```yaml
input:
  - GitHub raw `docs/current.md`
  - GitHub raw `docs/task-index.md`
  - GitHub raw `docs/decision-log.md`
  - GitHub raw `docs/memory/INDEX.md`
  - recent PR/commit readback for #122/#243/#245/#246/#247/#248
output:
  - receipt: `docs/research/post-frozen/2026-05-08/W1B-opendesign-reuse-v2/receipts/preflight-<timestamp>.md`
verification:
  - Active product lane and Authority writer counts recorded
  - W1B Active row presence/absence recorded
  - drift between authority anchor and actual latest commit recorded
  - PR state/mergedAt verified for cited PRs
verdict:
  - clear / concern (<reason>) / partial (<reason>) / reject (<reason>)
boundary:
  - Do not edit authority docs from this dispatch
  - If current/task-index/decision-log disagree, report split-truth instead of choosing silently
amend_trigger:
  - drift found and not explained
  - W1B already active in task-index
  - Authority writer occupied
self_verification:
  - frontmatter candidate/not-authority confirmed
  - no authority write in planned output
  - no runtime/migration/raw-vault/browser lane change
  - no hardcoded visual constants outside token files
  - TODO placeholder honesty preserved when implementation is deferred
```

### D-W1B-002: v2 cluster spec Hermes pre-review request

**Mission**: Paste deliverable 04 to Hermes with 01 and 02 inline, then collect independent verdict before package-path fallback is used.

```yaml
input:
  - 01 cluster spec
  - 02 dispatch pack
  - 04 Hermes prompt skeleton
  - master spec §7.1/§13/§15.2/§16 raw URL
  - v1 ledger raw URL
output:
  - receipt: `docs/research/post-frozen/2026-05-08/W1B-opendesign-reuse-v2/receipts/hermes-audit-<timestamp>.md`
verification:
  - Hermes verdict is V-PASS or V-PASS-WITH-CONCERN for proceeding
  - V-CONCERN produces amend list
  - V-REJECT stops single-point path
verdict:
  - clear / concern (<reason>) / partial (<reason>) / reject (<reason>)
boundary:
  - Hermes is advisory; user gate remains final
  - Do not start single-point fallback after V-REJECT
amend_trigger:
  - Hermes reports any hard-boundary ambiguity
  - Hermes cannot verify bundle budget
  - Hermes requests current GitHub readback not provided
self_verification:
  - frontmatter candidate/not-authority confirmed
  - no authority write in planned output
  - no runtime/migration/raw-vault/browser lane change
  - no hardcoded visual constants outside token files
  - TODO placeholder honesty preserved when implementation is deferred
```

### D-W1B-003: v2 candidate-doc PR

**Mission**: CC0 commits the four W1B candidate markdown files as reference/candidate documentation only.

```yaml
input:
  - 4 markdown deliverables
  - Hermes receipt if available
  - preflight receipt
output:
  - branch: `cc0/w1b-opendesign-reuse-v2-2026-05-08`
  - 4 files under `docs/research/post-frozen/2026-05-08/W1B-opendesign-reuse-v2/`
  - PR body with candidate-only boundary
verification:
  - diff only contains intended docs path
  - frontmatter status stays candidate
  - no implementation code
  - docs redline and secrets redline pass
verdict:
  - clear / concern (<reason>) / partial (<reason>) / reject (<reason>)
boundary:
  - Do not write PRD/SRD/current/task-index/decision-log from this dispatch
  - Do not claim promotion
amend_trigger:
  - diff includes app code
  - status word drift
  - authority path appears in write diff
self_verification:
  - frontmatter candidate/not-authority confirmed
  - no authority write in planned output
  - no runtime/migration/raw-vault/browser lane change
  - no hardcoded visual constants outside token files
  - TODO placeholder honesty preserved when implementation is deferred
```

### D-W1B-004: optional W1B Active row registration by Authority writer

**Mission**: Register W1B as an Active product lane only after candidate-doc PR lands and user explicitly opens W1B.

```yaml
input:
  - merged candidate-doc PR
  - docs/task-index.md
  - docs/current.md
  - docs/decision-log.md
output:
  - one authority-writer PR that registers W1B Active row and updates current state
verification:
  - Active product count ≤ 3
  - Authority writer count ≤ 1
  - W1B allowed paths and validation clear
  - START-HERE refresh if required
verdict:
  - clear / concern (<reason>) / partial (<reason>) / reject (<reason>)
boundary:
  - This is the only card in this pack that may touch authority files, and only after explicit authority-writer dispatch
  - No parallel authority writer
amend_trigger:
  - authority writer already occupied
  - W1B code work starts before registration
  - no validation plan
self_verification:
  - frontmatter candidate/not-authority confirmed
  - no authority write in planned output
  - no runtime/migration/raw-vault/browser lane change
  - no hardcoded visual constants outside token files
  - TODO placeholder honesty preserved when implementation is deferred
```

### D-W1B-005: PF-C4-EXT-graph self-rolled spike

**Mission**: Give Codex a 5h bounded attempt to implement the Trust Trace graph with CSS/SVG/React state and no new dependency.

```yaml
input:
  - TrustTrace.tsx placeholder `data-todo=trust-trace-graph`
  - TrustTrace.module.css
  - tokens.css
  - v2 cluster spec §3/§4
output:
  - `apps/capture-station/src/features/trust-trace/components/Graph.*` or equivalent local feature component
  - receipt recording complexity, performance, and verdict
verification:
  - typecheck/lint/test/build green
  - no dependency change
  - fixture graph renders without console errors
  - performance target: 30fps+ on bounded fixture if browser check is allowed
verdict:
  - clear / concern (<reason>) / partial (<reason>) / reject (<reason>)
boundary:
  - No npm graph lib
  - No external donor source
  - No app-wide architecture rewrite
  - No citation-chain scope expansion
amend_trigger:
  - 5h exceeded
  - graph math expands beyond bounded surface
  - performance <30fps
  - typecheck/build red
self_verification:
  - frontmatter candidate/not-authority confirmed
  - no authority write in planned output
  - no runtime/migration/raw-vault/browser lane change
  - no hardcoded visual constants outside token files
  - TODO placeholder honesty preserved when implementation is deferred
```

### D-W1B-006: single-point upgrade decision gate

**Mission**: Choose path-A self-rolled or path-B conditional `npm d3` fallback based on D-W1B-005 evidence and user V-PASS.

```yaml
input:
  - D-W1B-005 receipt
  - Hermes audit receipt
  - bundle baseline if available
output:
  - decision receipt: path-A self-rolled / path-B npm-d3 / kill
verification:
  - decision cites actual evidence
  - user V-PASS recorded before path-B
  - Hermes V-PASS or V-PASS-WITH-CONCERN present for path-B
verdict:
  - clear / concern (<reason>) / partial (<reason>) / reject (<reason>)
boundary:
  - Codex cannot self-authorize path-B
  - At most one graph lib
  - No multiple-lib comparison install spree
amend_trigger:
  - missing user gate
  - Hermes V-CONCERN unresolved
  - self-rolled evidence inconclusive
self_verification:
  - frontmatter candidate/not-authority confirmed
  - no authority write in planned output
  - no runtime/migration/raw-vault/browser lane change
  - no hardcoded visual constants outside token files
  - TODO placeholder honesty preserved when implementation is deferred
```

### D-W1B-007: path-B only — npm d3 preflight and evidence

**Mission**: Only if D-W1B-006 selects path-B, prepare the single-point d3 evidence trail before implementation proceeds.

```yaml
input:
  - path-B decision receipt
  - capture-station package.json
  - bundler output before baseline
  - v2-D19/v2-D20 criteria
output:
  - package diff limited to d3 dependency
  - bundle before/after evidence
  - tree-shaking note
  - fallback note if budget fails
verification:
  - bundle delta ≤ candidate 50kB gzip or concern recorded
  - ESM import style documented
  - pnpm build green
  - no second graph lib
verdict:
  - clear / concern (<reason>) / partial (<reason>) / reject (<reason>)
boundary:
  - This card is conditional only
  - No UI/styling package
  - No global package policy extension
amend_trigger:
  - bundle budget exceeded
  - tree-shaking not demonstrable
  - build red
  - second package proposed
self_verification:
  - frontmatter candidate/not-authority confirmed
  - no authority write in planned output
  - no runtime/migration/raw-vault/browser lane change
  - no hardcoded visual constants outside token files
  - TODO placeholder honesty preserved when implementation is deferred
```

### D-W1B-008: PF-C4-EXT-graph implementation

**Mission**: Replace the graph placeholder using either path-A self-rolled or path-B d3, based on the decision receipt.

```yaml
input:
  - D-W1B-006 decision receipt
  - D-W1B-005 or D-W1B-007 evidence
  - Trust Trace fixtures
output:
  - Trust Trace graph component integrated
  - graph placeholder removed or downgraded to honest fallback note
  - tests for graph render and selected-state behavior
verification:
  - typecheck/lint/test/build green
  - token usage clear
  - graph renders fixture nodes/edges
  - no citation-chain work
verdict:
  - clear / concern (<reason>) / partial (<reason>) / reject (<reason>)
boundary:
  - Scope is Trust Trace graph only
  - Path-B dependency use limited to graph module
  - No donor transplant
amend_trigger:
  - implementation requires second dependency
  - visual constants not tokenized
  - fixture cannot render
self_verification:
  - frontmatter candidate/not-authority confirmed
  - no authority write in planned output
  - no runtime/migration/raw-vault/browser lane change
  - no hardcoded visual constants outside token files
  - TODO placeholder honesty preserved when implementation is deferred
```

### D-W1B-009: PF-C4-EXT-timeline hover implementation

**Mission**: Replace timeline hover placeholder with CSS Variables + RAF/evidence focus behavior, no new dependency.

```yaml
input:
  - TrustTrace.tsx placeholder `data-todo=trust-trace-timeline`
  - trace fixture rows
  - tokens.css
output:
  - timeline component integrated
  - hover/focus state tests
  - receipt note for reduced-motion behavior
verification:
  - typecheck/lint/test/build green
  - keyboard-focus path exists
  - prefers-reduced-motion honored if motion is used
verdict:
  - clear / concern (<reason>) / partial (<reason>) / reject (<reason>)
boundary:
  - Self-rolled only
  - No graph-lib coupling unless reading selected graph node state
  - No runtime/browser automation unlock
amend_trigger:
  - hover requires live data not available
  - motion inaccessible
  - timeline leaks scope into citation-chain
self_verification:
  - frontmatter candidate/not-authority confirmed
  - no authority write in planned output
  - no runtime/migration/raw-vault/browser lane change
  - no hardcoded visual constants outside token files
  - TODO placeholder honesty preserved when implementation is deferred
```

### D-W1B-010: PF-C4-EXT-error-path implementation

**Mission**: Replace error-path placeholder with path backtrace, breadcrumb, and visual highlight state.

```yaml
input:
  - TrustTrace.tsx placeholder `data-todo=trust-trace-error-path`
  - graph node/edge fixture
  - traceRows fixture
output:
  - error path component/state integrated
  - breadcrumb state tests
  - receipt note on graph dependency assumptions
verification:
  - typecheck/lint/test/build green
  - error path highlights deterministic fixture
  - empty/error state honest
verdict:
  - clear / concern (<reason>) / partial (<reason>) / reject (<reason>)
boundary:
  - Self-rolled only
  - No runtime data claim
  - No citation-chain scope
amend_trigger:
  - graph implementation unavailable
  - breadcrumb state nondeterministic
  - hardcoded colors appear
self_verification:
  - frontmatter candidate/not-authority confirmed
  - no authority write in planned output
  - no runtime/migration/raw-vault/browser lane change
  - no hardcoded visual constants outside token files
  - TODO placeholder honesty preserved when implementation is deferred
```

### D-W1B-011: cross-TODO consistency check

**Mission**: Audit graph/timeline/error-path as one Trust Trace interaction grammar.

```yaml
input:
  - outputs of D-W1B-008~010
  - TrustTrace.tsx
  - tokens.css
  - component tests
output:
  - consistency receipt with token, state, accessibility, and TODO status summary
verification:
  - 3 submodules share selection grammar
  - token discipline pass
  - no L8 sync-badge leakage
  - no citation-chain false completion
verdict:
  - clear / concern (<reason>) / partial (<reason>) / reject (<reason>)
boundary:
  - Do not add new scope to make consistency pass
  - Do not rewrite shared components unrelated to Trust Trace
amend_trigger:
  - state grammar conflict
  - selection state unclear
  - TODO count dishonest
self_verification:
  - frontmatter candidate/not-authority confirmed
  - no authority write in planned output
  - no runtime/migration/raw-vault/browser lane change
  - no hardcoded visual constants outside token files
  - TODO placeholder honesty preserved when implementation is deferred
```

### D-W1B-012: TrustTrace.tsx integration and placeholder accounting

**Mission**: Integrate the three completed submodules into TrustTrace and leave citation-chain as future work if present.

```yaml
input:
  - TrustTrace.tsx
  - Graph/timeline/error-path components
  - existing EvidenceTable and PanelCard components
output:
  - TrustTrace.tsx integrated surface
  - placeholder accounting receipt
  - smoke tests
verification:
  - 3 PF-C4-EXT TODO replaced or honestly marked partial
  - citation-chain remains out of scope
  - UI copy remains Chinese
verdict:
  - clear / concern (<reason>) / partial (<reason>) / reject (<reason>)
boundary:
  - No app-wide refactor
  - No live API wiring
  - No route changes
amend_trigger:
  - placeholder removal overclaims runtime
  - English UI drift
  - tests missing
self_verification:
  - frontmatter candidate/not-authority confirmed
  - no authority write in planned output
  - no runtime/migration/raw-vault/browser lane change
  - no hardcoded visual constants outside token files
  - TODO placeholder honesty preserved when implementation is deferred
```

### D-W1B-013: capture-station full validation

**Mission**: Run full local validation for capture-station and record truthfully.

```yaml
input:
  - apps/capture-station package scripts
  - repo redline tools
  - W1B receipts
output:
  - validation receipt with exact commands and results
  - failure narrow report if any step fails
verification:
  - pnpm typecheck
  - pnpm lint
  - pnpm test
  - pnpm build
  - python tools/check-docs-redlines.py
  - python tools/check-secrets-redlines.py
  - git diff --check
verdict:
  - clear / concern (<reason>) / partial (<reason>) / reject (<reason>)
boundary:
  - Do not mark green unless actually green
  - Do not skip failing test silently
  - Do not run forbidden runtime tools
amend_trigger:
  - validation red
  - environment blocker not narrowed
  - stdout contract incomplete
self_verification:
  - frontmatter candidate/not-authority confirmed
  - no authority write in planned output
  - no runtime/migration/raw-vault/browser lane change
  - no hardcoded visual constants outside token files
  - TODO placeholder honesty preserved when implementation is deferred
```

### D-W1B-014: lane closeout receipt and CHECKPOINT

**Mission**: Write W1B lane closeout narrative and structured checkpoint with path choice and evidence.

```yaml
input:
  - all D-W1B receipts
  - validation receipt
  - Hermes receipt
  - decision receipt
output:
  - `docs/research/post-frozen/W1B/receipts/PF-C4-EXT-lane-closeout-2026-05-08.md`
  - `docs/research/post-frozen/W1B/PF-C4-EXT-CHECKPOINT.json`
verification:
  - narrative ≥1500 Chinese characters
  - all 15 dispatch verdicts summarized
  - single_point_upgrade_path field present
  - bundle delta field truthful
  - boundary preservation clear/concern stated
verdict:
  - clear / concern (<reason>) / partial (<reason>) / reject (<reason>)
boundary:
  - Closeout is a receipt, not authority
  - No historical ledger modification
  - No raw vault write
amend_trigger:
  - missing dispatch verdict
  - checkpoint fields fabricated
  - boundary not checked
self_verification:
  - frontmatter candidate/not-authority confirmed
  - no authority write in planned output
  - no runtime/migration/raw-vault/browser lane change
  - no hardcoded visual constants outside token files
  - TODO placeholder honesty preserved when implementation is deferred
```

### D-W1B-015: PR open, CC audit, user V-PASS, merge path

**Mission**: Open implementation PR, run CC0/CC1 audit, and wait for user V-PASS before merge route.

```yaml
input:
  - W1B implementation diff
  - closeout receipt
  - CHECKPOINT
  - validation output
output:
  - PR targeting main
  - PR body with summary/validation/boundary
  - CC audit report or review comments
verification:
  - changed files within allowed paths
  - no authority files unless separate authority dispatch
  - CI expected checks recorded
  - user V-PASS / amend / root-cause path selected
verdict:
  - clear / concern (<reason>) / partial (<reason>) / reject (<reason>)
boundary:
  - No direct merge before user gate
  - No hidden second dependency
  - No overflow lane claim
amend_trigger:
  - CC audit concern
  - CI fail
  - user chooses amend/root-cause
  - forbidden path in diff
self_verification:
  - frontmatter candidate/not-authority confirmed
  - no authority write in planned output
  - no runtime/migration/raw-vault/browser lane change
  - no hardcoded visual constants outside token files
  - TODO placeholder honesty preserved when implementation is deferred
```


## §4 Conditional path matrix

| Condition | Path | Required receipt |
|---|---|---|
| D-W1B-005 self-rolled graph is clear | path-A self-rolled | self-rolled spike receipt + user acceptance |
| D-W1B-005 is concern due to bounded complexity/perf | path-B `npm d3` single-point | Hermes V-PASS/V-PASS-WITH-CONCERN + user V-PASS + bundle baseline |
| D-W1B-007 exceeds budget or cannot prove tree-shaking | fallback self-rolled or kill | bundle/tree-shaking concern receipt |
| Any forbidden path touched | kill | kill receipt + user decision |

## §5 Hard Boundaries

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

### Allowed implementation paths after W1B registration

- `apps/capture-station/src/features/trust-trace/**`
- `apps/capture-station/src/features/trust-trace/components/**`
- `apps/capture-station/src/features/trust-trace/__tests__/**`
- `docs/research/post-frozen/W1B/receipts/**`
- `docs/research/post-frozen/W1B/PF-C4-EXT-CHECKPOINT.json`

### Forbidden implementation paths

- Authority files, unless D-W1B-004 is explicitly issued as a single authority-writer dispatch.
- PRD/SRD files, top-level agent files, historical run ledgers, historical external audit reports.
- `services/api/migrations/**`, `workers/**`, `packages/**`, `data/**`, `referencerepo/**`, `~/workspace/raw/**`.

## REGENERATE Anti-pattern Gate — package / transplant / runtime boundary

These are hard REGENERATE signals for any downstream draft, dispatch, or PR body generated from this file:

9. REGENERATE: 引整套 vendored UI 进 `apps/capture-station` — shadcn / Radix / TanStack / React Flow / Zustand / Lucide / styled-components / @emotion / Mantine / Ant Design / Chakra UI / @mui 等 UI/styling 全家桶不得进入 dependency surface。
10. REGENERATE: transplant donor files — 不复制 OpenDesign / shadcn-admin 整套源码、IA、layout primitives、class names、package assumptions 进 `apps/capture-station`。
11. REGENERATE: React 18 → 19 upgrade — v1-D6 仅允许 later spike candidate，本 W1B v2 不做版本升级。
12. REGENERATE: Tailwind / shadcn / Panda package install — v1-D5 保持 future strategy candidate only；本 v2 只讨论 graph single-point slot。
13. REGENERATE: Hex hardcoding — 除 `tokens.css` / density / type-weight token files 外，组件与 dispatch 不写硬编码色值。
14. REGENERATE: runtime lane 偷开 — BBDown live / yt-dlp / ffmpeg / ASR / browser automation / migration runtime 均不得因 W1B 启动而解禁。
15. REGENERATE: 把 D 路径误读成“禁止外引” — D 路径是单点引一个 graph lib 的候选升级路径；它不是整套 vendored UI，也不是默认外引许可。

## §6 Dispatch-pack Self-flag

- ⚠️ D-W1B-005 5h timebox is a candidate tradeoff: enough to expose complexity, but CC0/CC1 may adjust if local graph fixture proves larger.
- ⚠️ D-W1B-007 uses a 50kB gzip candidate budget; exact threshold should be measured against current capture-station bundle.
- ⚠️ D-W1B-004 is optional because only an authority-writer dispatch may register W1B; this pack intentionally keeps docs land separate from lane opening.
- ⚠️ Browser visual evidence remains conditional; if browser execution is gated at runtime, receipt must say blocked instead of inventing a visual terminal verdict.
