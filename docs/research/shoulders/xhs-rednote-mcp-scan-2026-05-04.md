---
title: ScoutFlow XHS / RedNote MCP Shoulder Scan
status: candidate / research-only / not-authority / not-runtime-approval
date: 2026-05-04
task: T-P1A-037
dispatch_pr_slot: PR #62
backbone_source: docs/research/pr55-pr74-worklist-candidate-2026-05-04.md §7
---

# ScoutFlow XHS / RedNote MCP Shoulder Scan

## Scope

- Stage: `scan` only, not `clone`, not `probe`, not runtime approval.
- Allowed output only: `docs/research/shoulders/xhs-rednote-mcp-scan-2026-05-04.md`
- `docs/shoulders-index.md` intentionally not updated in this PR.
- scan stage does not require file:line citations; probe stage later requires >=3 file:line evidence per selected repo.

## Method

This pass used live GitHub surface evidence only: repo landing page, default branch / HEAD recency, README, manifest, and one core file path or module path. No `referencerepo/` clone was performed. Maintenance recency is treated as a scoring factor, not a hard threshold.

## Short Verdict

| Candidate | Decision | Integration Proposal | Confidence | Notes |
|---|---|---|---:|---|
| `iFurySt/RedNote-MCP` | `winner` | `clone_to_reference -> probe` | 0.84 | Most adopted read-focused MCP baseline; MIT; clear TS layout |
| `ShellyDeng08/rednote-analyzer-mcp` | `winner` | `clone_to_reference -> probe` | 0.81 | Python-native, recent, modular tool layout, MIT |
| `TimeCyber/mcp-xiaohongshu` | `defer` | `reference_only` | 0.67 | Fork of iFury with publish/write surface added; useful contrast but wider blast radius |
| `MrMao007/RedNote-MCP-Plus` | `defer` | `reference_only` | 0.63 | Python package and richer tool set, but write/interaction scope is too broad for first probe |
| `yangsijie666/xiaohongshu-crawler` | `defer` | `reference_only until license clarified` | 0.72 | Strong crawler + MCP shape, but license signal is unclear on repo surface |
| `MilesCool/rednote-mcp` | `drop` | `drop` | 0.58 | Tiny history, low ecosystem proof, and repo/package license signal diverges |
| `cloudy-sfu/MCP-rednote-assistant` | `drop` | `drop` | 0.76 | GPL-3.0 plus cookie-export/manual flow misaligns with ScoutFlow baseline |

## Winner Recommendation

### Winner A: `iFurySt/RedNote-MCP`

Why it wins:

- highest ecosystem validation in this batch (`~1k` stars on repo surface)
- narrow read-path positioning: search, note detail, comments, login bootstrap
- clear MCP packaging (`package.json`, `src/index.ts`, `src/cli.ts`, tool modules)
- MIT license keeps later adaptation space open

Wave 3B probe focus:

- tool contract shape in `src/tools/rednoteTools.ts`
- cookie persistence and auth boundary in `src/auth/authManager.ts`
- whether read-path output can map cleanly into ScoutFlow typed capture metadata without carrying publish/write scope

### Winner B: `ShellyDeng08/rednote-analyzer-mcp`

Why it wins:

- Python-first implementation fits ScoutFlow's current repo language better
- very recent activity signal
- modular split between adapters, models, prompts, and tools
- explicit PyPI/distribution posture suggests better packaging discipline than one-off scripts

Wave 3B probe focus:

- `src/rednote_analyzer_mcp/server.py` tool registration and transport shape
- `src/rednote_analyzer_mcp/adapters/playwright.py` browser boundary
- whether `analysis` / `generation` layers can be separated from the pure read-path ScoutFlow actually needs

## Drop / Defer Summary

- Drop now: `MilesCool/rednote-mcp`, `cloudy-sfu/MCP-rednote-assistant`
- Defer now: `TimeCyber/mcp-xiaohongshu`, `MrMao007/RedNote-MCP-Plus`, `yangsijie666/xiaohongshu-crawler`
- Reserve note: `yangsijie666/xiaohongshu-crawler` is technically interesting enough for a later probe if license posture becomes explicit and the project needs a crawler-heavy route rather than a narrower MCP reference.

## Candidate Verdicts

### 1. `iFurySt/RedNote-MCP`

- URL: `https://github.com/iFurySt/RedNote-MCP`
- Last commit: `74bf739a3db5` on `main` (`2025-05-11T12:30:29Z`)
- Stars / forks / issues: about `1k` / `171` / `17`
- License: `MIT`
- README summary: positions itself as a RedNote MCP service for content access, with login bootstrap, keyword search, note URL access, and comment access. README explicitly requires Playwright install and stores cookies under `~/.mcp/rednote/cookies.json`.
- manifest: root `package.json`; npm-oriented package with `dist/index.js`, CLI entry, build/test scripts, and MCP SDK dependency.
- one core file path: `src/tools/rednoteTools.ts`
- decision: `winner`
- integration proposal: `clone_to_reference -> probe`
- confidence: `0.84`
- blockers:
  - Node + Playwright runtime instead of Python
  - cookie persistence path and login bootstrap need boundary review before any runtime discussion
  - no proof yet that returned payloads match ScoutFlow capture fields cleanly
- next action: deep probe tool contracts, auth boundary, and output shape

### 2. `MilesCool/rednote-mcp`

- URL: `https://github.com/MilesCool/rednote-mcp`
- Last commit: `9d51cc3ed03a` on `master` (`2025-06-26T10:37:44Z`)
- Stars / forks / issues: about `24` / `5` / `1`
- License: repo surface shows `MIT` file, but package manifest says `"license": "ISC"`
- README summary: focuses on search/retrieve for Xiaohongshu with Playwright, MCP SDK, parallel processing, and Zod validation.
- manifest: root `package.json`; minimal TS package with `dist/index.js`, Playwright, MCP SDK, and Zod.
- one core file path: `src/index.ts`
- decision: `drop`
- integration proposal: `drop`
- confidence: `0.58`
- blockers:
  - only `5` commits on repo surface, so maintenance proof is thin
  - license signal diverges between repo file and manifest
  - repo shape is small enough that it adds limited reference value beyond larger neighbors
- next action: none unless later evidence shows materially better output schema discipline than the winners

### 3. `TimeCyber/mcp-xiaohongshu`

- URL: `https://github.com/TimeCyber/mcp-xiaohongshu`
- Last commit: `cbf77d2e9299` on `main` (`2025-06-04T03:37:56Z`)
- Stars / forks / issues: about `12` / `3` / `0`
- License: `MIT`
- README summary: forked from `iFurySt/RedNote-MCP`, but expands from read-only access into publish flow, image upload, privacy settings, and broader interaction.
- manifest: root `package.json`; packaged CLI/server with MCP SDK plus broader dependency surface and release files.
- one core file path: `src/index.ts`
- decision: `defer`
- integration proposal: `reference_only`
- confidence: `0.67`
- blockers:
  - write/publish features broaden the account-risk surface immediately
  - overlap with upstream iFury means probe value is lower unless ScoutFlow explicitly wants publish paths
  - fork status means later maintenance may trail or diverge unpredictably
- next action: only probe if the team later wants a read+publish comparison against the narrower iFury baseline

### 4. `ShellyDeng08/rednote-analyzer-mcp`

- URL: `https://github.com/ShellyDeng08/rednote-analyzer-mcp`
- Last commit: `b82eafc3ee94` on `master` (`2026-03-17T22:36:15Z`)
- Stars / forks / issues: about `6` / `2` / `0`
- License: `MIT`
- README summary: presents itself as an MCP server for search, analysis, and content generation, with bilingual docs, PyPI packaging, and explicit AI-workflow positioning.
- manifest: root `pyproject.toml`; Python `>=3.11`, MIT, structured keywords, and package name `rednote-analyzer-mcp`.
- one core file path: `src/rednote_analyzer_mcp/server.py`
- decision: `winner`
- integration proposal: `clone_to_reference -> probe`
- confidence: `0.81`
- blockers:
  - analysis/generation scope may be wider than ScoutFlow's immediate read-path needs
  - Playwright adapter still implies browser/login complexity
  - low star count means adoption proof is lighter than iFury
- next action: probe its adapter/tool split and assess whether read-only extraction can be isolated cleanly

### 5. `cloudy-sfu/MCP-rednote-assistant`

- URL: `https://github.com/cloudy-sfu/MCP-rednote-assistant`
- Last commit: `1befa1c44b3a` on `main` (`2026-04-26T13:29:20Z`)
- Stars / forks / issues: about `4` / `1` / `0`
- License: `GPL-3.0`
- README summary: describes a RedNote assistant/server that collects data from Xiaohongshu, with a manual cookie-export flow and Windows-focused installation notes.
- manifest: root `requirements.txt`; dependency list includes `mcp`, `httpx`, `pydantic`, `pandas`, and scraping-related packages, but no stronger packaging metadata surfaced in root.
- one core file path: `server.py`
- decision: `drop`
- integration proposal: `drop`
- confidence: `0.76`
- blockers:
  - `GPL-3.0` is a material downstream constraint for any adaptation path
  - manual cookie-export workflow is operationally weaker than the other candidates
  - flatter script layout gives less reusable contract structure than the modular winners
- next action: none

### 6. `MrMao007/RedNote-MCP-Plus`

- URL: `https://github.com/MrMao007/RedNote-MCP-Plus`
- Last commit: `351d4a7e3b6a` on `main` (`2026-02-09T08:45:14Z`)
- Stars / forks / issues: about `5` / `0` / `0`
- License: `MIT`
- README summary: explicitly markets a broader tool suite, including publish, like, favorite, comment, follow, search, and dump-style data access.
- manifest: root `pyproject.toml` plus `requirements.txt`; Python package `rednote_mcp_plus` with console script and `mcp[cli]`.
- one core file path: `src/rednote_mcp_plus/server.py`
- decision: `defer`
- integration proposal: `reference_only`
- confidence: `0.63`
- blockers:
  - tool surface is much broader than the minimal read-path ScoutFlow should study first
  - includes account-interaction and publish actions that are outside current runtime authority
  - low adoption signal makes it weaker than the narrower winners
- next action: keep as a later reference if ScoutFlow ever studies operator-side write tools

### 7. `yangsijie666/xiaohongshu-crawler`

- URL: `https://github.com/yangsijie666/xiaohongshu-crawler`
- Last commit: `59abbe2b6fda` on `master` (`2026-02-28T10:34:43Z`)
- Stars / forks / issues: about `7` / `3` / `0`
- License: no explicit root `LICENSE` file was visible in the scanned repo surface; treat as unresolved until clarified
- README summary: frames itself as a full Xiaohongshu crawler plus MCP service, with Playwright, stealth layers, multiple transports, JSON/Excel output, and broad note/comment collection.
- manifest: root `pyproject.toml`; Python `>=3.10`, `mcp[cli]`, `playwright`, `playwright-stealth`, `browserforge`, `starlette`, `uvicorn`.
- one core file path: `mcp_server.py`
- decision: `defer`
- integration proposal: `reference_only until license clarified`
- confidence: `0.72`
- blockers:
  - no explicit repo-surface license is a real gate for adaptation
  - crawler/stealth/export surface is significantly larger than ScoutFlow's current scan objective
  - anti-detection/runtime concerns risk dragging the next probe into blocked runtime territory too early
- next action: only promote to probe if license is clarified and the team explicitly wants a crawler-heavy shoulder rather than an MCP-first shoulder

## Recommended Wave 3B Probe Order

1. `iFurySt/RedNote-MCP`
2. `ShellyDeng08/rednote-analyzer-mcp`
3. `yangsijie666/xiaohongshu-crawler` only as reserve, after license clarification

## Final Scan Verdict

Two repos are strong enough for `clone_to_reference -> probe`, three are better kept as `reference_only` for now, and two should be dropped from the active shoulder queue. The main split is simple: ScoutFlow should study one narrower MCP-first baseline and one Python-native structured baseline before touching crawler-heavy or publish-heavy variants.
