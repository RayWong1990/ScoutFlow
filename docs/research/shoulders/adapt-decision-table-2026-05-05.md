---
title: ScoutFlow Shoulders Adapt Decision Table
date: 2026-05-05
status: candidate / decision-only / not-runtime-approval
related_task: T-P1A-049
---

# ScoutFlow Shoulders Adapt Decision Table

## 1. Scope

This document converts Wave 3B probe results plus the repo-external H5 mock into a bounded decision candidate. It does not approve implementation. It only decides which shoulders move forward as `adapt`, `fork`, `reference_only`, or `drop`.

## 2. Inputs

Inputs used:

- `docs/research/shoulders/shoulders-probe-batch-1-2026-05-05.md`
- `docs/research/h5-prototype-mock-pointer-2026-05-05.md`
- `docs/visual/h5-capture-station/design-brief.md`
- `docs/visual/h5-capture-station/trust-trace-graph-spec.md`

## 3. Decision rubric

Mode meanings in this PR:

- `adapt`: borrow patterns into a future ScoutFlow implementation
- `fork`: maintain a long-lived local fork with active upstream sync
- `reference_only`: keep as a design/probe/reference source without direct implementation commitment
- `drop`: stop carrying the shoulder forward

Current bias:

- prefer `reference_only` unless the probe clearly exposed a narrow, high-value pattern worth copying
- avoid `fork` unless local divergence is already justified
- use `drop` only when the shoulder adds cost without signal

## 4. Decision table

| Shoulder | Decision | Why now | Carry-forward |
|---|---|---|---|
| `REDNOTE-XHS / iFurySt/RedNote-MCP` | `reference_only` | read-path is useful, but cookie/login boundary is too opinionated | keep as XHS read-path reference |
| `REDNOTE-XHS / ShellyDeng08/rednote-analyzer-mcp` | `reference_only` | Python-native stack is useful, but generation/analysis scope is too broad | keep as Python contrast repo |
| `CONSOLE-CLI / satnaing/shadcn-admin` | `adapt` | layout/system patterns fit the H5 mock and design package best | adapt panel/layout/data-shell ideas only |
| `BILIBILI-COMPARATOR / yt-dlp` | `reference_only` | strongest comparator for page/subtitle/chapter/comment ceiling, but not the main runtime route | keep as comparator ceiling reference |

## 5. REDNOTE-XHS call

The XHS pair remains `reference_only`.

Reason:

- both probes exposed useful read-path structure
- neither one fits ScoutFlow's current runtime and auth boundary directly
- the project still needs a later, narrower adapter decision before any implementation work

Carry-forward:

- keep `iFurySt/RedNote-MCP` as the first read-path reference
- keep `ShellyDeng08/rednote-analyzer-mcp` as Python-native contrast
- no `fork`
- no `drop`

## 6. CONSOLE-CLI call

`satnaing/shadcn-admin` becomes the only `adapt` decision in this batch.

Reason:

- the H5 mock and design package already lean on the same browser-H5 stack cues
- the probe proved strong panel/layout/data-shell value
- we only want to adapt layout/system patterns, not clone the full admin IA

Carry-forward:

- adapt panel zoning, query/router shell patterns, and component discipline
- do not adapt sidebar-first dashboard IA
- keep `Kiranism/tanstack-start-dashboard` as reserve-only

## 7. BILIBILI-COMPARATOR call

`yt-dlp` remains `reference_only`.

Reason:

- it is excellent as a comparator ceiling for fields and multi-part behavior
- ScoutFlow already has `BBDown` as the locked primary route
- the current need is comparison and drift explanation, not runtime replacement

Carry-forward:

- keep `Nemo2011/bilibili-api` reserve-only
- no `fork`
- no `drop`

## 8. Wave 4 carry-forward

Wave 4 should consume this table conservatively:

- `adapt`: `satnaing/shadcn-admin` panel/layout/system patterns
- `reference_only`: both XHS repos and `yt-dlp`
- `fork`: none approved
- `drop`: none triggered in this batch

Wave 4 remains candidate-only until PR75 closeout says otherwise.
