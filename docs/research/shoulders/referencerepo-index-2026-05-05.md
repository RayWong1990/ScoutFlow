---
title: ScoutFlow referencerepo index tracked mirror
date: 2026-05-05
status: candidate / tracked-mirror-only / local-only-truth-mirrored
wave: 3B
related_task: T-P1A-044
---

# ScoutFlow referencerepo index tracked mirror

> 本文件是 `referencerepo/**` 的 tracked mirror，不是磁盘真相源。
>
> 2026-05-05 Dispatch 84 续跑时，镜像真相源明确为：
> `/Users/wanglei/workspace/scoutflow-T-P1A-044/referencerepo`
>
> 当前 live rows 只记录真实存在的 local-only clone；reserve rows 继续保留为计划项，不假装已经 clone。

| shoulder_id | category | canonical_local_alias | source_absolute_path | planned_local_path | upstream | license | cloned_at_commit | size | metadata_local_state | tracked mirror note |
|---|---|---|---|---|---|---|---|---:|---|---|
| `rednote-mcp-ifuryst` | `xhs` | `capture/REDNOTE-MCP-WINNER` | `/Users/wanglei/workspace/scoutflow-T-P1A-044/referencerepo/xhs/rednote-mcp-ifuryst` | `referencerepo/xhs/rednote-mcp-ifuryst/` | `iFurySt/RedNote-MCP` | `MIT` | `74bf739a3db5` | `516K` | `dispatch84_index_created; canonical meta pending` | primary XHS winner; tracked mirror for local-only clone + probe |
| `rednote-analyzer-mcp` | `xhs` | `capture/REDNOTE-MCP-WINNER` | `/Users/wanglei/workspace/scoutflow-T-P1A-044/referencerepo/xhs/rednote-analyzer-mcp` | `referencerepo/xhs/rednote-analyzer-mcp/` | `ShellyDeng08/rednote-analyzer-mcp` | `MIT` | `b82eafc3ee94` | `864K` | `dispatch84_index_created; canonical meta shared-with-primary` | secondary XHS contrast source; stays indexed even though the canonical alias is shared |
| `shadcn-admin` | `console` | `frontend/KIRANISM-SHADCN-STARTER` | `/Users/wanglei/workspace/scoutflow-T-P1A-044/referencerepo/console/shadcn-admin` | `referencerepo/console/shadcn-admin/` | `satnaing/shadcn-admin` | `MIT` | `a6352e7df0de` | `4.0M` | `dispatch84_index_created; canonical meta pending` | canonical alias intentionally differs from the live donor repo name |
| `yt-dlp` | `bilibili` | `capture/YT-DLP` | `/Users/wanglei/workspace/scoutflow-T-P1A-044/referencerepo/bilibili/yt-dlp` | `referencerepo/bilibili/yt-dlp/` | `yt-dlp/yt-dlp` | `Unlicense` | `35684c1171dd` | `18M` | `dispatch84_index_created; canonical meta pending` | live comparator clone used for Wave 3B probe |
| `nemo2011-bilibili-api` | `bilibili` | `capture/BILI-API-NEMO2011` | `not cloned` | `referencerepo/bilibili/nemo2011-bilibili-api/` | `Nemo2011/bilibili-api` | `GPL-3.0` | `pending` | `n/a` | `not_applicable` | reserve only; clone deferred after cap-4 gate |
| `tanstack-start-dashboard` | `console` | `frontend/KIRANISM-TANSTACK-START-DASHBOARD` | `not cloned` | `referencerepo/console/tanstack-start-dashboard/` | `Kiranism/tanstack-start-dashboard` | `MIT` | `pending` | `n/a` | `not_applicable` | reserve only; clone deferred after cap-4 gate |

## Dispatch 84 mirror rules

- `referencerepo/**` stays local-only and untracked.
- The B1 execution worktree now uses `referencerepo/_INDEX.local.md` as the execution-surface truth for existence checks.
- Canonical alias names may differ from live donor directory names; the tracked mirror must record both instead of forcing a rename.
