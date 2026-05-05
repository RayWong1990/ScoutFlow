---
title: ScoutFlow referencerepo Size Budget Audit Mirror
date: 2026-05-05
type: shoulder-size-audit-mirror
status: candidate / research-only / tracked-audit-only / not-runtime-approval
wave: 3B
related_task: T-P1A-065
---

# ScoutFlow referencerepo Size Budget Audit Mirror

## Scope

- This dispatch records the size state of the current live local-only donor surface after Dispatch 84-89 completed.
- The audit stays mirror-only: it does not move or delete any local clone, and it does not track `referencerepo/**`.
- The purpose is to prove whether the current mirror still sits comfortably inside the `<100MB` per-donor rule and the wider local-only budget.

## Audit baseline

- audit run note: `2026-05-05T13:02:03+0800`
- per-donor hard trigger: `<100MB`
- current live donor set:
  - `REDNOTE-MCP-WINNER` primary clone
  - XHS contrast clone
  - `KIRANISM-SHADCN-STARTER` donor
  - `HERMES-KANBAN-BRIDGE` subtree donor
  - `YT-DLP` comparator donor

## Size table

| canonical alias / source | measured path | size | status |
|---|---|---:|---|
| `REDNOTE-MCP-WINNER` primary | `/Users/wanglei/workspace/scoutflow-T-P1A-044/referencerepo/xhs/rednote-mcp-ifuryst` | `516K` | within `<100MB` |
| `REDNOTE-MCP-WINNER` contrast | `/Users/wanglei/workspace/scoutflow-T-P1A-044/referencerepo/xhs/rednote-analyzer-mcp` | `864K` | within `<100MB` |
| `KIRANISM-SHADCN-STARTER` | `/Users/wanglei/workspace/scoutflow-T-P1A-044/referencerepo/console/shadcn-admin` | `4.0M` (`4132K`) | within `<100MB` |
| `HERMES-KANBAN-BRIDGE` | `/Users/wanglei/workspace/hermes-agent/plugins/kanban` | `160K` | within `<100MB` |
| `YT-DLP` | `/Users/wanglei/workspace/scoutflow-T-P1A-044/referencerepo/bilibili/yt-dlp` | `18M` (`18812K`) | within `<100MB` |

Aggregate total:

- `24068K` across the current live donor set
- approximately `23.5M` total

## Interpretation

- Every currently mirrored donor is well below the `<100MB` per-donor trigger.
- The aggregate live donor set is small enough that there is no immediate pressure to archive or trim the current Wave 3B mirror.
- `YT-DLP` is the largest live donor by a wide margin, so if ScoutFlow ever adds more comparator or frontend clones, that lane should be watched first.
- `HERMES-KANBAN-BRIDGE` stays cheap only because the mirror points to the bridge-specific subtree instead of the whole `hermes-agent` host workspace.

## Carry-forward rule

- Keep the current `<100MB` donor trigger unchanged.
- Re-run this audit whenever a new live donor is added or an existing donor is re-cloned at a materially larger size.
- If any donor crosses `<100MB`, do not silently keep it in the mirror; reopen the fork/sync policy candidate first.

## Result

Dispatch 90 closes the mirror lane with a clean budget verdict:

- all live donors are within `<100MB`
- total live donor footprint is about `23.5M`
- no immediate archive action is needed
- the size trigger remains a real gate, not a decorative note
