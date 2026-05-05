---
title: ScoutFlow Shoulder Fork Sync Policy Candidate
date: 2026-05-05
type: shoulder-policy-candidate
status: candidate / research-only / tracked-policy-only / not-runtime-approval
wave: 3B
related_task: T-P1A-064
---

# ScoutFlow Shoulder Fork Sync Policy Candidate

## Scope

- This dispatch proposes how the newly repaired local-only shoulder mirror should handle sync cadence without executing any GitHub fork, clone, or automation.
- The policy stays at candidate level and only governs the current Wave 3B local-only donors.
- It does not approve repo writes outside `docs/research/shoulders/`.

## Inputs

- Dispatch 84-88 established four live canonical local-only donors plus one bridge subtree donor, all backed by real machine-local evidence.
- The lifecycle handbook already locked the structural guardrails: local-only metadata files, tracked mirror only in docs, and `<100MB` per-clone budget ([docs/architecture/shoulders-lifecycle-handbook-candidate-2026-05-04.md:L420-L456](docs/architecture/shoulders-lifecycle-handbook-candidate-2026-05-04.md), [docs/architecture/shoulders-lifecycle-handbook-candidate-2026-05-04.md:L458-L503](docs/architecture/shoulders-lifecycle-handbook-candidate-2026-05-04.md)).
- The bridge donor differs from the others because it is a subtree inside an actively used host workspace rather than a standalone clone ([docs/research/shoulders/bridge-reference-clone-report-2026-05-05.md:L20-L37](docs/research/shoulders/bridge-reference-clone-report-2026-05-05.md)).

## Policy

### 1. Base rules

- Keep every live donor under the `<100MB` local-only mirror rule.
- Default mode is `reference_only`, not fork.
- `fork` only becomes thinkable after a later dispatch explicitly requires local code divergence plus upstream resync, which none of the current donors do.
- Any sync script proposal must stay dry-run and macOS-compatible.

### 2. Donor matrix

| canonical alias | source truth | current role | fork policy | sync cadence | rationale |
|---|---|---|---|---|---|
| `REDNOTE-MCP-WINNER` | `rednote-mcp-ifuryst` primary + `rednote-analyzer-mcp` contrast | XHS read-path reference | `no fork` | `on-demand` | auth/runtime boundary is still blocked; ScoutFlow only needs periodic re-checks when XHS shape work reopens |
| `KIRANISM-SHADCN-STARTER` | `satnaing/shadcn-admin` | layout/system donor | `no fork` | `monthly` | UI donor may drift gradually, but there is no live app implementation yet |
| `HERMES-KANBAN-BRIDGE` | `hermes-agent/plugins/kanban` subtree | execution-plane reference | `no fork` | `on-demand` | donor is a subtree of an active host workspace; ScoutFlow wants patterns, not divergence |
| `YT-DLP` | `yt-dlp/yt-dlp` | Bilibili comparator donor | `no fork` | `monthly` | comparator field shape can drift with upstream extractor updates |

### 3. Explicit no-fork cases

- `REDNOTE-MCP-WINNER`: no fork because the current problem is auth/runtime boundary, not missing local features.
- `HERMES-KANBAN-BRIDGE`: no fork because the donor is already part of an actively used Hermes workspace and ScoutFlow only wants gateway/dispatcher patterns.
- `YT-DLP`: no fork because ScoutFlow uses it as a comparator ceiling, not as the locked primary runtime.

### 4. Re-evaluation triggers

Re-open this policy only if one of the following becomes true:

- a donor breaches the `<100MB` mirror budget
- ScoutFlow starts carrying local code deltas that cannot live as pure notes/specs
- a later product dispatch needs repeatable upstream diff tracking instead of one-off read-only sampling

## Result

This candidate keeps the mirror conservative:

- all current donors remain `reference_only`
- zero live donor needs a GitHub fork today
- sync cadence is bounded and explicit
- `<100MB` remains the hard local-only budget trigger
