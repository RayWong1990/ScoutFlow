---
title: W1B Codex Commander Prompt Skeleton — Long Runner 通宵实施
status: candidate / commander_prompt_skeleton
authority: not-authority
created_by: gpt-pro (skeleton 模板, CC1 后续填充 + 战友拍板 paste)
parent_cluster: W1B
parent_dispatch_pack: 02-w1b-dispatch-pack.md
target_executor: Codex (Long Runner Coder, 本地 worktree)
expected_runtime: 5-7h Codex 通宵
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

# W1B Codex Commander Prompt Skeleton

> Paste-time skeleton for Codex. CC1/战友 should fill exact branch name, receipts folder, and any latest authority drift before sending. Codex implements only after W1B is properly gated.

## §0 Codex role and context

You are Codex, ScoutFlow’s Long Runner Coder in the 4-agent v3 system. You run local git/shell work for bounded implementation, receipts, checkpoint, PR, and validation. GPT Pro produced candidate spec/dispatch docs; CC0/CC1 and Hermes provide audit layers; user V-PASS is the final gate.

User interruptions must stop the run. Write a user-interrupt receipt with current phase, dispatch ID, touched files, validation status, and pending decision; then wait for the next instruction.

## §0.5 Prerequisite Check — Codex must run before work

Read and record live values from:

1. `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md`
2. `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md`
3. `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/decision-log.md`
4. `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/memory/INDEX.md`

Expected baseline from GPT Pro handoff:

- authority anchor reports `c802de4`/PR #247 while recent commit search showed `6dd27d7`/PR #245.
- Active `0/3`, Authority writer `0/1`, W1B not registered.
- PR #122/#243/#245/#246/#247/#248 were verified merged during prompt production.

If any value drifts, use live truth in receipts and write: “撰写时刻 2026-05-08 历史参考; GitHub live 以 main HEAD 为准”. Do not proceed if W1B lane registration is required but missing.

## §1 Mission

Implement W1B PF-C4-EXT 3 TODO for Trust Trace:

- `PF-C4-EXT-graph`: default self-rolled; conditional `npm d3` only after D-W1B-006 user gate and Hermes pass.
- `PF-C4-EXT-timeline`: self-rolled CSS Variables + RAF/evidence focus.
- `PF-C4-EXT-error-path`: self-rolled path backtrace + breadcrumb/highlight.

Do not implement citation chain. Do not change runtime, migration, vault true write, browser automation, or authority state except via separately issued authority-writer dispatch.

## §2 Inputs — must read in order

1. `01-w1b-cluster-spec.md`
2. `02-w1b-dispatch-pack.md`
3. v1 ledger: `docs/research/repairs/opendesign-reuse-strategy-candidate-2026-05-05.md`
4. master spec: `docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md` §7.1, §13, §15.2, §16
5. PR #243 baseline files: `TrustTrace.tsx`, `TrustTrace.module.css`, capture-station `package.json`, `tokens.css`
6. PF-V `LESSONS-LEARNED.md`, especially token discipline and one-shot placeholder honesty
7. Hermes V-PASS or V-PASS-WITH-CONCERN receipt if path-B is considered

## §3 Hard Boundaries

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

### Allowed paths for implementation work

- `apps/capture-station/src/features/trust-trace/**`
- `apps/capture-station/src/features/trust-trace/components/**`
- `apps/capture-station/src/features/trust-trace/__tests__/**`
- `docs/research/post-frozen/W1B/receipts/**`
- `docs/research/post-frozen/W1B/PF-C4-EXT-CHECKPOINT.json`
- `docs/research/post-frozen/W1B/PF-C4-EXT-lane-closeout-2026-05-08.md`

### Forbidden paths

- Authority files unless a separate authority-writer dispatch is explicitly issued.
- PRD/SRD promoted docs, top-level agent files, historical run ledgers, historical external-audit reports.
- `services/api/migrations/**`, `workers/**`, `packages/**`, `data/**`, `referencerepo/**`, `~/workspace/raw/**`.

### Forbidden assertion pattern

Do not assert that dependencies, runtime, migration, browser automation, raw vault writes, overflow lanes, PRD/SRD promotion, OpenDesign runtime use, or donor transplant have been accepted/unlocked/promoted. Use negative boundary language only.

## REGENERATE Anti-pattern Gate — package / transplant / runtime boundary

These are hard REGENERATE signals for any downstream draft, dispatch, or PR body generated from this file:

9. REGENERATE: 引整套 vendored UI 进 `apps/capture-station` — shadcn / Radix / TanStack / React Flow / Zustand / Lucide / styled-components / @emotion / Mantine / Ant Design / Chakra UI / @mui 等 UI/styling 全家桶不得进入 dependency surface。
10. REGENERATE: transplant donor files — 不复制 OpenDesign / shadcn-admin 整套源码、IA、layout primitives、class names、package assumptions 进 `apps/capture-station`。
11. REGENERATE: React 18 → 19 upgrade — v1-D6 仅允许 later spike candidate，本 W1B v2 不做版本升级。
12. REGENERATE: Tailwind / shadcn / Panda package install — v1-D5 保持 future strategy candidate only；本 v2 只讨论 graph single-point slot。
13. REGENERATE: Hex hardcoding — 除 `tokens.css` / density / type-weight token files 外，组件与 dispatch 不写硬编码色值。
14. REGENERATE: runtime lane 偷开 — BBDown live / yt-dlp / ffmpeg / ASR / browser automation / migration runtime 均不得因 W1B 启动而解禁。
15. REGENERATE: 把 D 路径误读成“禁止外引” — D 路径是单点引一个 graph lib 的候选升级路径；它不是整套 vendored UI，也不是默认外引许可。

## §4 Phase × dispatch list

| Phase | Dispatch range | Estimated work | Owner |
|---|---|---|---|
| Phase 1 | D-W1B-001~004 | preflight, Hermes pre-review, candidate-doc PR, optional authority registration | CC0/CC1 + user gate |
| Phase 2 | D-W1B-005~007 | graph self-rolled spike, decision gate, conditional d3 preflight | Codex + user gate |
| Phase 3 | D-W1B-008~013 | graph/timeline/error-path implementation, integration, validation | Codex |
| Phase 4 | D-W1B-014~015 | closeout, checkpoint, PR, audit, merge path | Codex + CC0/CC1 + user |

Do not skip D-W1B-006. Path-B is invalid without the decision receipt.

## §5 PR strategy

Default option A: one PR after all implementation and closeout receipts are complete.

Fallback option B: phased PRs only if user changes paste-time strategy.

Default branch:

- `codex/w1b-opendesign-reuse-v2-2026-05-08`
- start from `origin/main` after W1B v2 candidate docs are landed and, if required, W1B Active row exists.

## §6 amend_and_proceed pattern

Allowed autonomous amend count: 1 per W1B lane total.

Trigger examples:

- silent flexibility detected;
- validation red cannot be fixed quickly;
- self-rolled graph exceeds timebox;
- package-path evidence fails tree-shaking/bundle check;
- authority drift creates lane ambiguity.

Procedure:

1. Stop current dispatch.
2. Write amend receipt with trigger, files touched, rollback/continue recommendation, and validation status.
3. Revert unsafe diff if needed.
4. Continue only if within first autonomous amend and boundary is safe.
5. On second amend trigger, stop and wait for user.

## §7 Self-audit after each phase

Run and record:

1. Boundary: write_enabled, 5 overflow lanes, authority docs, forbidden paths.
2. Anti-pattern: UI/styling framework, donor transplant, React upgrade, hardcoded visual constants.
3. Token discipline: all visual values come from token variables or token files.
4. TODO honesty: citation-chain remains future if not implemented.
5. Evidence: validation commands, bundle delta if path-B, Hermes receipt, user gate receipt.

## §8 Truthful Stdout Contract

Write to W1B CHECKPOINT:

```yaml
lane_id: W1B-PF-C4-EXT
execution_mode: local_worktree_long_runner_codex
single_point_upgrade_path: self-rolled | npm-d3 | kill
hermes_v_pass_receipt: <path-or-none>
bundle_size_increment_kb_gzip: <actual-or-not-measured-with-reason>
pf_c4_ext_3_todo_completed: 3/3 | partial
validation:
  typecheck: pass | fail | not-run-with-reason
  lint: pass | fail | not-run-with-reason
  test: pass | fail | not-run-with-reason
  build: pass | fail | not-run-with-reason
boundary_preservation_check: clear | concern:<reason>
authority_files_untouched: confirmed | exception-with-dispatch-id
raw_vault_untouched: confirmed
overflow_lanes_unchanged: confirmed
todo_placeholders_honest: confirmed
ready_for_user_audit: yes | no_with_reason
```

Do not fabricate wall-clock, command output, screenshots, or bundle data.

## §9 Kill signals

Stop immediately and write kill receipt if any happens:

- forbidden path touched;
- runtime/ASR/download/browser/migration path opened;
- authority file changed without an explicit authority-writer dispatch;
- raw vault path touched;
- donor source copied into app;
- more than one graph dependency proposed;
- conditional `npm d3` path used before D-W1B-006 gate;
- bundle delta exceeds candidate budget and user has not accepted concern;
- test/build failure cannot be narrowed.

## §10 Codex worktree

- Branch: `codex/w1b-opendesign-reuse-v2-2026-05-08`
- Target: `main`
- PR title template: `feat(capture-station): W1B Trust Trace graph timeline error-path implementation`
- PR body must include Summary, Validation, Boundary, Path decision, Evidence receipts, Self-flag.

## §11 Paste-time alterations for user/CC1

Update only these if needed before paste:

- branch name;
- path-A vs path-B forced strategy, if user already decided;
- PR strategy A/B;
- allowed paths if authority writer dispatch is issued;
- Hermes second audit requirement.

## §12 Empty fill-in section

CC1/user may paste final live values, Hermes receipt path, and W1B Active row ID here before sending to Codex.

## Self-flag

- ⚠️ The skeleton assumes W1B candidate docs have landed before implementation; if user wants direct implementation first, §2/§5 must be altered.
- ⚠️ Bundle-size fields cannot be truthful until Codex runs a local build/analyze step.
- ⚠️ Browser visual checks depend on current runtime/browser gate; if gated, Codex must record blocked evidence, not visual pass.
- ⚠️ The split-truth main anchor should be refreshed by authority writer before any W1B closeout depends on exact HEAD wording.
