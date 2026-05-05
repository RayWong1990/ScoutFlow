---
title: ScoutFlow XHS RedNote Winner Probe Batch 1
date: 2026-05-05
type: shoulder-probe-batch
status: candidate / research-only / not-authority / not-runtime-approval
wave: 3B
related_task: T-P1A-051
---

# ScoutFlow XHS RedNote Winner Probe Batch 1

## Scope

- This dispatch narrows the Wave 3B shoulder probe surface to the two XHS winners already selected in the earlier scan lane.
- All clone evidence remains local-only; tracked repo output is limited to this report.
- This report does not approve runtime, login bootstrap, browser automation capture, or any write/publish behavior.

## Inputs

- The scan lane already locked two XHS winners for `clone_to_reference -> probe` and rejected broader write-heavy candidates ([docs/research/shoulders/xhs-rednote-mcp-scan-2026-05-04.md:L23-L33](docs/research/shoulders/xhs-rednote-mcp-scan-2026-05-04.md), [docs/research/shoulders/xhs-rednote-mcp-scan-2026-05-04.md:L35-L71](docs/research/shoulders/xhs-rednote-mcp-scan-2026-05-04.md)).
- The Wave 3B clone plan reserved exactly two XHS slots and kept them in the first cap-4 probe batch ([docs/research/shoulders/clone-plan-2026-05-05.md:L22-L31](docs/research/shoulders/clone-plan-2026-05-05.md)).
- The tracked mirror records both local-only shallow clones and their `cloned_at_commit` hashes ([docs/research/shoulders/referencerepo-index-2026-05-05.md:L15-L20](docs/research/shoulders/referencerepo-index-2026-05-05.md)).
- The earlier batch probe already surfaced the strongest read-path and auth-boundary evidence for both repos ([docs/research/shoulders/shoulders-probe-batch-1-2026-05-05.md:L37-L67](docs/research/shoulders/shoulders-probe-batch-1-2026-05-05.md)).

## Batch verdict

| shoulder | decision | integration proposal | confidence | next_action |
|---|---|---|---:|---|
| `REDNOTE-XHS / iFurySt/RedNote-MCP` | continue | `reference_only -> deeper auth/output probe` | 0.84 | keep as primary read-path baseline |
| `REDNOTE-XHS / ShellyDeng08/rednote-analyzer-mcp` | continue with caution | `reference_only -> isolate read-path from analysis/generation` | 0.79 | keep as Python-native contrast |

## Probe findings

### shoulder REDNOTE-XHS / iFurySt/RedNote-MCP

Decision: keep this repo as the primary XHS read-path reference, but hold it at `reference_only` until a later lane proves ScoutFlow can tolerate its login and cookie persistence boundary.

Why:

- The scan lane selected it as the strongest narrow MCP-first XHS winner because the repo stayed focused on read-path access rather than operator-side publish behavior ([docs/research/shoulders/xhs-rednote-mcp-scan-2026-05-04.md:L27-L33](docs/research/shoulders/xhs-rednote-mcp-scan-2026-05-04.md), [docs/research/shoulders/xhs-rednote-mcp-scan-2026-05-04.md:L37-L50](docs/research/shoulders/xhs-rednote-mcp-scan-2026-05-04.md)).
- The tracked mirror confirms the local-only probe used the planned clone at `referencerepo/xhs/rednote-mcp-ifuryst/` with commit `74bf739a3db5` ([docs/research/shoulders/referencerepo-index-2026-05-05.md:L17-L18](docs/research/shoulders/referencerepo-index-2026-05-05.md)).
- The local README explicitly bootstraps login and persists cookies to `~/.mcp/rednote/cookies.json`, which is workable for a local MCP tool but not a boundary ScoutFlow should silently inherit ([referencerepo/xhs/rednote-mcp-ifuryst/README.md:L25-L26](referencerepo/xhs/rednote-mcp-ifuryst/README.md), [referencerepo/xhs/rednote-mcp-ifuryst/README.md:L67-L72](referencerepo/xhs/rednote-mcp-ifuryst/README.md)).
- The package manifest shows a concrete Node/TypeScript MCP surface with Playwright, Commander, Winston, and Zod, so the repo is credible as a tool-contract donor even though it is still browser-driven ([referencerepo/xhs/rednote-mcp-ifuryst/package.json:L7-L15](referencerepo/xhs/rednote-mcp-ifuryst/package.json:L7-L15), [referencerepo/xhs/rednote-mcp-ifuryst/package.json:L22-L33](referencerepo/xhs/rednote-mcp-ifuryst/package.json:L22-L33), [referencerepo/xhs/rednote-mcp-ifuryst/package.json:L52-L56](referencerepo/xhs/rednote-mcp-ifuryst/package.json:L52-L56)).
- The CLI registers search/content/comments tools and the auth manager hardcodes `~/.mcp/rednote/`, so the repo gives ScoutFlow a real read-path/output shape while simultaneously exposing the auth isolation work that still needs to be solved ([referencerepo/xhs/rednote-mcp-ifuryst/src/cli.ts:L35-L52](referencerepo/xhs/rednote-mcp-ifuryst/src/cli.ts:L35-L52), [referencerepo/xhs/rednote-mcp-ifuryst/src/cli.ts:L61-L79](referencerepo/xhs/rednote-mcp-ifuryst/src/cli.ts:L61-L79), [referencerepo/xhs/rednote-mcp-ifuryst/src/auth/authManager.ts:L23-L43](referencerepo/xhs/rednote-mcp-ifuryst/src/auth/authManager.ts:L23-L43)).

Carry-forward:

- Keep this repo as the primary XHS read-path baseline.
- Future work should stay on output normalization and auth isolation, not on publish/write surface expansion.

### shoulder REDNOTE-XHS / ShellyDeng08/rednote-analyzer-mcp

Decision: keep this repo as the Python-native contrast shoulder, but split its read-path value from the broader analysis/generation posture before any adaptation talk.

Why:

- The scan lane selected it as the second XHS winner because it matches ScoutFlow's Python bias better than the TypeScript repo while remaining MIT-licensed and actively packaged ([docs/research/shoulders/xhs-rednote-mcp-scan-2026-05-04.md:L27-L33](docs/research/shoulders/xhs-rednote-mcp-scan-2026-05-04.md), [docs/research/shoulders/xhs-rednote-mcp-scan-2026-05-04.md:L52-L71](docs/research/shoulders/xhs-rednote-mcp-scan-2026-05-04.md)).
- The tracked mirror records the local-only clone at `referencerepo/xhs/rednote-analyzer-mcp/` with commit `b82eafc3ee94` ([docs/research/shoulders/referencerepo-index-2026-05-05.md:L17-L19](docs/research/shoulders/referencerepo-index-2026-05-05.md)).
- The README and `pyproject.toml` clearly position the repo as an MCP server for search, analysis, and generation, which is broader than ScoutFlow's current capture boundary and therefore must be narrowed on intake ([referencerepo/xhs/rednote-analyzer-mcp/README.md:L1-L13](referencerepo/xhs/rednote-analyzer-mcp/README.md:L1-L13), [referencerepo/xhs/rednote-analyzer-mcp/pyproject.toml:L1-L10](referencerepo/xhs/rednote-analyzer-mcp/pyproject.toml:L1-L10), [referencerepo/xhs/rednote-analyzer-mcp/pyproject.toml:L52-L67](referencerepo/xhs/rednote-analyzer-mcp/pyproject.toml:L52-L67)).
- The server keeps a module-level singleton adapter and supports both `mock` and `playwright`, which is useful for teasing apart contract-first read-path testing from live browser work later ([referencerepo/xhs/rednote-analyzer-mcp/src/rednote_analyzer_mcp/server.py:L20-L33](referencerepo/xhs/rednote-analyzer-mcp/src/rednote_analyzer_mcp/server.py:L20-L33), [referencerepo/xhs/rednote-analyzer-mcp/src/rednote_analyzer_mcp/server.py:L36-L63](referencerepo/xhs/rednote-analyzer-mcp/src/rednote_analyzer_mcp/server.py:L36-L63)).
- The Playwright adapter stores cookies under `~/.rednote-mcp/cookies.json` and adds request pacing, which is operationally mature but still too broad to inherit into current ScoutFlow runtime assumptions ([referencerepo/xhs/rednote-analyzer-mcp/src/rednote_analyzer_mcp/adapters/playwright.py:L42-L49](referencerepo/xhs/rednote-analyzer-mcp/src/rednote_analyzer_mcp/adapters/playwright.py:L42-L49), [referencerepo/xhs/rednote-analyzer-mcp/src/rednote_analyzer_mcp/adapters/playwright.py:L55-L57](referencerepo/xhs/rednote-analyzer-mcp/src/rednote_analyzer_mcp/adapters/playwright.py:L55-L57)).

Carry-forward:

- Keep this repo as the Python-native contrast shoulder.
- Later XHS adapter work should judge only discovery/note-detail/comment surfaces and leave analysis/generation out of the first implementation lane.

## Result

This batch stays inside the narrowest truthful conclusion:

- two XHS winners remain valid
- both stay `reference_only`
- neither repo currently clears ScoutFlow's auth/runtime boundary
- the next useful step is deeper output-shape and auth-isolation probing, not implementation
