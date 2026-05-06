---
title: Run-N Commander Template Rules — §4 Enforcement
status: candidate / commander_template_rules / not-authority
created_at: 2026-05-06
applies_to: Run-2 onward (and any future post-frozen multi-dispatch run)
upstream_audit: docs/research/post-frozen/runs/RUN-1-AMENDMENT-LEDGER-2026-05-06.md
---

# Why this exists

Run-1 三个 dispatch 同型越 §4 allowed_paths（PF-LP-01 / PF-LP-02 / PF-LP-13）。这不是个例，是 contract enforcement 缺位的 systemic 问题：当 proof requirement（如 `>=20` line excerpt）与 §4 allowed_paths 冲突时，Codex 默认扩 path 而非停下来 amend。本规则文件锁住未来 Run-N 的 stop-line。

# Three hard rules（任一违反即 dispatch reject）

## Rule 1 — §4 是窄合同

dispatch §4 `files_to_create` / `files_to_modify` 是穷举清单，不是示例。任何不在清单内的文件修改都算 `scope_deviation_flag=yes`。

## Rule 2 — Proof-requires-production-expansion -> STOP

若执行过程中发现 proof requirement（assertion bar / line count bar / coverage bar）必须修改 §4 外的 production code 才能满足：

1. `STOP`，不许扩张 §4，不许 slot-local self-recovery 跨 production 边界。
2. 在 worktree 写 truth-conflict 文件：`docs/research/post-frozen/runs/RUN-{N}-truth-conflict-{date}.md`
3. truth-conflict 必须列出：dispatch §4 allowed paths、proof requirement、实际需要的扩展 paths、推荐 amendment 文本。
4. 提交 truth-conflict 到 dispatch 自己的 worktree branch，不 push 到 main。
5. 在 PR comment 或 commander stdout 报告：`STOP: proof_requires_production_expansion / truth_conflict_at <path>`
6. 等用户裁决：`approve_amendment` / `descope_proof_bar` / `defer_to_next_run` / `roll_back`
7. 没有用户 verdict 之前，不许继续 merge。

## Rule 3 — §4 外修改必须 declared

哪怕只是 test helper de-dup / `tests/conftest.py` plumbing / fixture sync，只要文件不在 §4 清单内：

- 在 PR body 单独一节 `Scope Deviations`
- 必须列：`file_path` / `change_nature` / `coverage_impact` / `new_contract_introduced`
- `scope_deviation_flag: yes` 自动触发独立审，不得静默掩埋在 RUN report 里
- 任一独立审 reject，不 auto-merge

# Truth-conflict 文件模板

```markdown
---
title: Run-{N} Truth Conflict — {dispatch_id} proof_vs_§4
status: candidate / truth_conflict / not-authority
created_at: {date}
dispatch_id: {dispatch_id}
stop_verdict: blocked_on_truth_conflict
---

## §4 allowed_paths
- {list}

## Proof requirement
- {assertion / line count / coverage bar}

## What proof actually requires
- {production paths needed}

## Recommended amendment
- {dispatch §4 patch text}

## Awaiting user verdict
- [ ] approve_amendment
- [ ] descope_proof_bar
- [ ] defer_to_next_run
- [ ] roll_back

stop_verdict: blocked_on_truth_conflict / awaiting_user
```

# 适用范围

- 所有 post-frozen Run-N（Run-2、Run-3 ...）
- 所有 80-pack cluster dispatch（PF-LP-* / PF-C0-* / PF-O1-* / PF-META-* ...）
- 所有 high-blast 与 normal-blast dispatch（不区分）

# 与现有 _PACK-DEFAULTS / _SHARED-STOP-LINES 关系

- 本文件不修改 `_PACK-DEFAULTS` / `_SHARED-STOP-LINES`（authority-adjacent，本 PR 不碰）
- 本文件作为 `candidate / commander_template_rules / not-authority` 独立存在
- 下一次 `_PACK-DEFAULTS` authority 升级窗口可考虑把 Rule 1/2/3 promote 为 authority-locked

# Forward path

- Run-2 commander prompt 必须在顶部 reference 本文件
- 任何未引用本文件规则的 commander prompt 都是 invalid，不许执行
