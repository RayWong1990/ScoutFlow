---
title: ScoutFlow Wave 3B Shoulders Clone Plan
date: 2026-05-05
status: candidate / planning-only / not-authority / not-runtime-approval
wave: 3B
related_task: T-P1A-043
---

# ScoutFlow Wave 3B Shoulders Clone Plan

> 本计划只定义 Wave 3B 的 local-only clone/probe 顺序，不构成 runtime、dependency、frontend、或 adapter 实施批准。
>
> `referencerepo/** is local-only`。本文件只是 tracked 计划面，真实 clone 结果以后由 `docs/research/shoulders/referencerepo-index-2026-05-05.md` 作为 tracked mirror 记录。

## 1. 计划原则

1. 单 PR probe 上限仍是 `4 shoulders / PR`。
2. 先 clone，再 probe；clone 不等于集成。
3. repo-local tracked diff 不允许出现 `referencerepo/**`。
4. reserve 候选不在本 PR 执行 clone，只记录顺位。

## 2. Clone Queue

| slot | shoulder_row | repo | purpose | planned_local_path | PR69 role | status |
|---|---|---|---|---|---|---|
| 1 | `REDNOTE-XHS` | `iFurySt/RedNote-MCP` | read-path MCP baseline | `referencerepo/xhs/rednote-mcp-ifuryst/` | probe | planned |
| 2 | `REDNOTE-XHS` | `ShellyDeng08/rednote-analyzer-mcp` | Python-native XHS analyzer contrast | `referencerepo/xhs/rednote-analyzer-mcp/` | probe | planned |
| 3 | `CONSOLE-CLI` | `satnaing/shadcn-admin` | browser H5 clone winner | `referencerepo/console/shadcn-admin/` | probe | planned |
| 4 | `BILIBILI-COMPARATOR` | `yt-dlp/yt-dlp` | low-risk comparator family | `referencerepo/bilibili/yt-dlp/` | probe | planned |
| 5 | `BILIBILI-COMPARATOR` | `Nemo2011/bilibili-api` | GPL comparator reserve | `referencerepo/bilibili/nemo2011-bilibili-api/` | reserve | reserve |
| 6 | `CONSOLE-CLI` | `Kiranism/tanstack-start-dashboard` | router/data-stack reserve | `referencerepo/console/tanstack-start-dashboard/` | reserve | reserve |

## 3. Why These Six

- `REDNOTE-XHS`: PR #65 已明确锁定双 winner，所以直接双 clone，避免 probe 时再回到 scan。
- `CONSOLE-CLI`: 只选 `satnaing/shadcn-admin` 做主 clone，`Kiranism/tanstack-start-dashboard` 留给 router/data-stack 对比。
- `BILIBILI-COMPARATOR`: 主 clone 用 `yt-dlp/yt-dlp`，`Nemo2011/bilibili-api` 保持 reserve，防止 PR #69 立刻吃掉第五个 shoulder。

## 4. Gate

- PR #69 只 probe 前 4 个 planned clones。
- reserve 项只有在 PR #69 证明需要第二批 comparator / dashboard 对比时才升级。
- `referencerepo/** is local-only` 再次成立；本 PR 不执行任何 tracked clone。
