---
title: Second Window Docs-Only Commander Prompt — PF-C3 + overflow-reservoir
status: candidate / commander-prompt / not-authority
created_at: 2026-05-06
target_writer: Codex CLI second window (parallel to Run-1/2/3, docs-only no git lock conflict)
project_root: /Users/wanglei/workspace/ScoutFlow
scope: 17 docs-only dispatch (PF-C3 5 + overflow-reservoir 12)
---

# 第二窗口 Commander Prompt — PF-C3 + overflow-reservoir docs

> 17 docs-only dispatch / 全无 frontend/backend 依赖 / 与 Run-1/2/3 主链并行跑 / ~50 min unattended。
> 路径只动 `docs/research/post-frozen/**`，不冲突主链 git lock。
> 跳过 PF-C3-04（依赖 PF-C1-10，留到 Run-3 后单独跑）。

---

```
<<<COMMANDER PROMPT BEGIN>>>

你是 ScoutFlow Codex0 第二窗口写者，执行 docs-only 后台跑：把 17 个 docs-only dispatch 跑完，与主窗口 Run-1/2/3 并行不冲突。

## 项目身份
- repo: /Users/wanglei/workspace/ScoutFlow
- live status: WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED
- 你与主窗口 Codex0 并行跑，但仅写 `docs/research/post-frozen/**`，不动 services/apps/workers/packages/data
- 主窗口写产品代码 + authority-adjacent docs，你只写 candidate-only docs，git lock 不冲突

## 范围（17 dispatch / 全 docs-only / 全无主链依赖）

PF-C3 minimal object compression（5 个，跳过 C3-04）：
- PF-C3-01 131-144 object inventory
- PF-C3-02 keep list（依赖 C3-01）
- PF-C3-03 compress list（依赖 C3-01）
- PF-C3-05 anti-objectification language patch（依赖 C3-02 + C3-03）
- PF-C3-06 c3 compression closeout（依赖 C3-05）

overflow-reservoir-or-later-packs（12 个，全 deps:none）：
- PF-GLOBAL-01 ~ PF-GLOBAL-12

## 不停歇协议
- unattended，全 docs-only，pass bar = redlines + secrets + git diff --check + dispatch §8 满足
- 每个 dispatch 写到 `docs/research/post-frozen/**` 路径（按 dispatch §4 allowed_paths）
- auto-commit + push + PR + auto-merge on `mergeStateStatus=CLEAN`
- 每 PR 5 checks 全绿后 merge，不等 user
- per-PR pause 仅当 frontmatter 含 `external_audit: required`（17 个都没有）

## Subagent 自由调度
- PF-C3 内部依赖链 (01 → 02/03 → 05 → 06) 串行
- overflow-reservoir 12 个全独立，可 5-6 路并行（不同 worktree）
- subagent read-only audit 与主写并行，你说了算
- 开足马力

## Cold-start 必跑
1. `git fetch origin --prune` + `git rev-parse origin/main`
2. 确认主窗口 Run-N 正在跑（`ls /Users/wanglei/workspace/ScoutFlow-W*` 看 worktree）
3. 选不冲突的 worktree 命名（如 `ScoutFlow-W2-docs-XX`）
4. `cat docs/research/post-frozen/80-pack-source/02_task_packs/_PACK-DEFAULTS.md`
5. 抽样 cat 一个 dispatch（如 PF-GLOBAL-01）确认 §4/§8 可执行

## 严守边界（与主窗口同）
- 只写 `docs/research/post-frozen/**`（含 evidence/ 子目录、80-pack-source/ 内 candidate 文档）
- 不写 docs/current.md / AGENTS.md / docs/task-index.md / docs/decision-log.md
- 不写 services/ apps/ workers/ packages/ data/ referencerepo/
- 不解禁任何 forbidden lane
- Dispatch126-176 frozen，只引用为 evidence

## 中断处理
- slot-local retry 自己修
- 与主窗口 git push race condition（rare） → rebase 后重试
- control-plane interruption（gh pr create 异常）→ 自己接得住，参 LESSONS §6.1

## 末尾产出
完成 17 dispatch 全 merged 后，写：
1. `docs/research/post-frozen/runs/RUN-W2-CODEX0-DOCS-REPORT-2026-05-06.md`（17 dispatch receipt）
2. `docs/research/post-frozen/runs/DIFF-BUNDLE-W2-Docs-2026-05-06.md`（17 PR 跨 PR 一致性，给末尾 final 外审用）
3. `docs/research/post-frozen/runs/CHECKPOINT-W2-final.json`

stdout 末尾输出：
```
COMMANDER WINDOW-2 DOCS COMPLETE
final_origin_main: <sha>
prs_merged: [17 PR numbers]
pf_c3_done: 5/5 (C3-04 deferred, depends PF-C1-10)
overflow_reservoir_done: 12/12
interruption_count: {slot_local: N, control_plane: N, ledger: N, race_with_main: N}
report_path: <path>
diff_bundle_path: <path>
ready_for_final_audit_bundle: yes
```

## 一句话目标
跑 17 docs-only 不影响主链，开足并行马力，跑完出 receipt + DIFF-BUNDLE。

开始动笔。

<<<COMMANDER PROMPT END>>>
```

---

## 派单顺序

第二窗口启动时机：**Run-1 V-PASS 后立即**（与 Run-2 同时启）。

```bash
# 在第二个 Codex CLI 窗口（cd 到 ScoutFlow 项目根，独立 worktree）
cat /Users/wanglei/workspace/ScoutFlow/docs/research/post-frozen/window2-docs-commander-prompt-2026-05-06.md
# 复制 <<<BEGIN>>>...<<<END>>> 内容粘进去
```

## 与主窗口的关系

| 时段 | 主窗口（Codex0） | 第二窗口（Codex0-W2） |
|---|---|---|
| 17:30-18:20 | Run-2 frontend 14 dispatch | 第二窗口 17 docs |
| 18:20+ | Run-3 / Run-4 / Run-5 | (已完成，等 final DIFF-BUNDLE 收口) |

**git lock 不冲突**：主窗口写 services/apps，第二窗口只写 docs/research/post-frozen/。
**PR 编号不冲突**：GitHub 自动递增。

## PF-C3-04 单独处理

C3-04 capture-plan-lite appendix 依赖 PF-C1-10（Run-3 内 dispatch）。Run-3 完成后，单独起一个 micro commander 跑 C3-04 (~3 min)：

```text
单 dispatch 跑：PF-C3-04，依赖 PF-C1-10 已 land。按 dispatch §1/§4/§8/§12 走，docs-only，redlines + secrets + git diff --check 过即可 push + auto-merge。完成后 stdout 报 PR 号。
```
