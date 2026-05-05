---
title: ScoutFlow XHS Reference Clone Local-only Mirror
date: 2026-05-05
type: shoulder-clone-mirror
status: candidate / research-only / tracked-mirror-only / not-runtime-approval
wave: 3B
related_task: T-P1A-060
---

# ScoutFlow XHS Reference Clone Local-only Mirror

## Scope

- This dispatch mirrors the canonical local-only XHS donor mapping into tracked docs after Dispatch 84 repaired the structure layer.
- The work creates one local-only metadata file for the canonical alias `REDNOTE-MCP-WINNER` and leaves all runtime, login, and browser-driven behavior blocked.
- No tracked `referencerepo/**` path is introduced.

## Inputs

- The XHS winner probe already separated the primary read-path winner from the Python-native contrast shoulder ([docs/research/shoulders/xhs-rednote-winner-probe-batch-1-2026-05-05.md:L21-L29](docs/research/shoulders/xhs-rednote-winner-probe-batch-1-2026-05-05.md), [docs/research/shoulders/xhs-rednote-winner-probe-batch-1-2026-05-05.md:L33-L71](docs/research/shoulders/xhs-rednote-winner-probe-batch-1-2026-05-05.md), [docs/research/shoulders/xhs-rednote-winner-probe-batch-1-2026-05-05.md:L73-L95](docs/research/shoulders/xhs-rednote-winner-probe-batch-1-2026-05-05.md)).
- Dispatch 84 made the naming drift explicit and recorded that both live XHS clones currently map into the same canonical alias family ([docs/research/shoulders/referencerepo-structure-plan-2026-05-05.md:L27-L40](docs/research/shoulders/referencerepo-structure-plan-2026-05-05.md), [docs/research/shoulders/referencerepo-index-2026-05-05.md:L12-L20](docs/research/shoulders/referencerepo-index-2026-05-05.md)).
- The verified local source paths remain `/Users/wanglei/workspace/scoutflow-T-P1A-044/referencerepo/xhs/rednote-mcp-ifuryst` and `/Users/wanglei/workspace/scoutflow-T-P1A-044/referencerepo/xhs/rednote-analyzer-mcp`.

## Mirror decision

| canonical alias | actual local path | role | metadata result |
|---|---|---|---|
| `REDNOTE-MCP-WINNER` | `/Users/wanglei/workspace/scoutflow-T-P1A-044/referencerepo/xhs/rednote-mcp-ifuryst` | primary XHS winner | `_SCOUTFLOW_META.local.md` created |
| `REDNOTE-MCP-WINNER` support row | `/Users/wanglei/workspace/scoutflow-T-P1A-044/referencerepo/xhs/rednote-analyzer-mcp` | supporting contrast source | indexed only; no second canonical meta file |

## Why the canonical meta points to `rednote-mcp-ifuryst`

- The Wave 3B XHS probe already treated `iFurySt/RedNote-MCP` as the primary read-path baseline and kept `rednote-analyzer-mcp` as the Python-native contrast shoulder rather than the first implementation donor ([docs/research/shoulders/xhs-rednote-winner-probe-batch-1-2026-05-05.md:L35-L52](docs/research/shoulders/xhs-rednote-winner-probe-batch-1-2026-05-05.md), [docs/research/shoulders/xhs-rednote-winner-probe-batch-1-2026-05-05.md:L73-L88](docs/research/shoulders/xhs-rednote-winner-probe-batch-1-2026-05-05.md)).
- The tracked mirror confirms the primary clone commit is `74bf739a3db5`, while the contrast clone remains a separate real source with commit `b82eafc3ee94` ([docs/research/shoulders/referencerepo-index-2026-05-05.md:L14-L15](docs/research/shoulders/referencerepo-index-2026-05-05.md)).
- Using one canonical metadata file for the primary donor keeps the local-only alias truthful without pretending the two XHS repos are interchangeable.

## Local-only metadata truth

The local-only file created by this dispatch is:

- `referencerepo/capture/REDNOTE-MCP-WINNER/_SCOUTFLOW_META.local.md`

It records:

- `canonical_alias = REDNOTE-MCP-WINNER`
- the actual live source path under `scoutflow-T-P1A-044/referencerepo/xhs/rednote-mcp-ifuryst`
- `tracked_in_git = false`
- notes pointing to the second real XHS clone as supporting contrast evidence rather than a second canonical winner

## Result

Dispatch 85 keeps the XHS mirror honest:

- the canonical alias now resolves to one real primary donor
- the second XHS repo remains visible as supporting evidence
- no tracked `referencerepo/**` path appears
- runtime and auth boundaries remain unchanged
