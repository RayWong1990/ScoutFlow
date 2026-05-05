---
title: ScoutFlow referencerepo Local-only Structure and Clone Plan Mirror
date: 2026-05-05
type: shoulder-clone-plan-mirror
status: candidate / research-only / tracked-mirror-only / not-runtime-approval
wave: 3B
related_task: T-P1A-059
---

# ScoutFlow referencerepo Local-only Structure and Clone Plan Mirror

## Scope

- This dispatch mirrors the actual local-only clone surface into tracked docs so Wave 4 Batch 1 can resume from Dispatch 84 without inventing missing `referencerepo/**` truth.
- No tracked clone, runtime, frontend, bridge service, or authority file is changed here.
- `referencerepo/**` remains local-only. The execution-surface truth lives in `referencerepo/_INDEX.local.md`, while tracked output stays under `docs/research/shoulders/`.

## Inputs

- The Wave 3B clone plan already defined the first cap-4 clone queue and the reserve rows that should stay deferred ([docs/research/shoulders/clone-plan-2026-05-05.md:L12-L22](docs/research/shoulders/clone-plan-2026-05-05.md), [docs/research/shoulders/clone-plan-2026-05-05.md:L24-L31](docs/research/shoulders/clone-plan-2026-05-05.md)).
- The existing tracked mirror already records the four live local-only clones plus two reserve rows ([docs/research/shoulders/referencerepo-index-2026-05-05.md:L12-L19](docs/research/shoulders/referencerepo-index-2026-05-05.md)).
- The shoulders lifecycle handbook locked the long-lived local-only layout, including `_INDEX.local.md`, `_SCOUTFLOW_META.local.md`, and the `<100MB` per-clone budget ([docs/architecture/shoulders-lifecycle-handbook-candidate-2026-05-04.md:L420-L456](docs/architecture/shoulders-lifecycle-handbook-candidate-2026-05-04.md), [docs/architecture/shoulders-lifecycle-handbook-candidate-2026-05-04.md:L458-L503](docs/architecture/shoulders-lifecycle-handbook-candidate-2026-05-04.md)).
- Dispatch 83 closed with the Wave 3B synthesis already landed on `main`, so the only honest next step here is local-only mirror repair, not another probe wave ([docs/research/shoulders/wave-3b-probe-synthesis-2026-05-05.md:L10-L29](docs/research/shoulders/wave-3b-probe-synthesis-2026-05-05.md)).

## Observed local-only surface

Execution on 2026-05-05 verified the legacy clone surface at:

- `/Users/wanglei/workspace/scoutflow-T-P1A-044/referencerepo`

Observed live clone directories:

| lane | source absolute path | upstream | commit | size | current state |
|---|---|---|---|---:|---|
| XHS primary | `/Users/wanglei/workspace/scoutflow-T-P1A-044/referencerepo/xhs/rednote-mcp-ifuryst` | `iFurySt/RedNote-MCP` | `74bf739a3db5` | `516K` | present |
| XHS contrast | `/Users/wanglei/workspace/scoutflow-T-P1A-044/referencerepo/xhs/rednote-analyzer-mcp` | `ShellyDeng08/rednote-analyzer-mcp` | `b82eafc3ee94` | `864K` | present |
| Frontend donor | `/Users/wanglei/workspace/scoutflow-T-P1A-044/referencerepo/console/shadcn-admin` | `satnaing/shadcn-admin` | `a6352e7df0de` | `4.0M` | present |
| Bilibili comparator | `/Users/wanglei/workspace/scoutflow-T-P1A-044/referencerepo/bilibili/yt-dlp` | `yt-dlp/yt-dlp` | `35684c1171dd` | `18M` | present |

## Naming drift and canonical mirror mapping

The local-only truth is currently split across two naming systems:

1. The legacy clone worktree keeps source-shaped paths such as `xhs/rednote-mcp-ifuryst` and `console/shadcn-admin`.
2. The lifecycle handbook and later Wave 4 dispatches expect canonical local-only aliases such as `capture/REDNOTE-MCP-WINNER` and `frontend/KIRANISM-SHADCN-STARTER`.

Dispatch 84 keeps both truths without faking new clones:

| observed source path | canonical local-only alias | mirror intent |
|---|---|---|
| `xhs/rednote-mcp-ifuryst` | `capture/REDNOTE-MCP-WINNER` | primary XHS read-path winner |
| `xhs/rednote-analyzer-mcp` | `capture/REDNOTE-MCP-WINNER` | supporting contrast source; stays indexed even though the canonical alias is shared |
| `console/shadcn-admin` | `frontend/KIRANISM-SHADCN-STARTER` | canonical alias absorbs naming drift from the live donor repo |
| `bilibili/yt-dlp` | `capture/YT-DLP` | canonical alias matches live comparator role |

## Structure decision

- Create `referencerepo/_INDEX.local.md` inside the B1 execution worktree as the local-only execution-surface index.
- Do not copy or move any real clone directory during this dispatch.
- Keep tracked truth in `docs/research/shoulders/referencerepo-index-2026-05-05.md`.
- Let later dispatches create the minimal `_SCOUTFLOW_META.local.md` files only when each canonical alias has a real source path behind it.

## Bridge note

- No bridge clone existed under the legacy `scoutflow-T-P1A-044/referencerepo` surface.
- Dispatch 87 must therefore verify its bridge donor from a separate real workspace surface instead of inventing a fake `referencerepo/frontend/HERMES-KANBAN-BRIDGE` clone.
- Dispatch 84 does not promote any bridge source yet; it only leaves the structure open for that later evidence-backed mapping.

## Result

Dispatch 84 resolves the structure-level blocker honestly:

- the four live legacy clones are real
- their canonical alias mapping is now explicit
- `_INDEX.local.md` becomes the local-only execution-surface truth
- later mirror dispatches can proceed one alias at a time without tracking `referencerepo/**`
