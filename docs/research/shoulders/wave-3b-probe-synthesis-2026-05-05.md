---
title: ScoutFlow Wave 3B Probe Synthesis
date: 2026-05-05
type: synthesis-report
status: candidate / research-only / not-authority / not-runtime-approval
wave: 3B
related_task: T-P1A-058
---

# ScoutFlow Wave 3B Probe Synthesis

## Scope

- This dispatch synthesizes the tracked outputs from Dispatch 76-82 only.
- It does not reopen Wave 4, does not rewrite authority surfaces, and does not convert any research result into runtime approval.
- The goal is to separate what is now `reference_only`, what is `adapt`, and what is `contract-ready but still gated`.

## Input set

- XHS pair narrowed to two `reference_only` winners with unresolved auth/runtime boundary ([docs/research/shoulders/xhs-rednote-winner-probe-batch-1-2026-05-05.md:L25-L30](docs/research/shoulders/xhs-rednote-winner-probe-batch-1-2026-05-05.md), [docs/research/shoulders/xhs-rednote-winner-probe-batch-1-2026-05-05.md:L68-L75](docs/research/shoulders/xhs-rednote-winner-probe-batch-1-2026-05-05.md)).
- Bilibili comparator lane narrowed to live `yt-dlp` plus reserve-only `Nemo2011` ([docs/research/shoulders/bilibili-comparator-probe-batch-2026-05-05.md:L25-L29](docs/research/shoulders/bilibili-comparator-probe-batch-2026-05-05.md), [docs/research/shoulders/bilibili-comparator-probe-batch-2026-05-05.md:L50-L61](docs/research/shoulders/bilibili-comparator-probe-batch-2026-05-05.md)).
- Console/H5 lane narrowed to `satnaing/shadcn-admin` as the only `adapt` donor while route choice stays open ([docs/research/shoulders/console-h5-frontend-probe-batch-2026-05-05.md:L25-L29](docs/research/shoulders/console-h5-frontend-probe-batch-2026-05-05.md), [docs/research/shoulders/console-h5-frontend-probe-batch-2026-05-05.md:L44-L62](docs/research/shoulders/console-h5-frontend-probe-batch-2026-05-05.md)).
- Vault lane locked `00-Inbox + raw 4-field + fail-loud env` as the carry-forward contract while keeping runtime gated ([docs/research/shoulders/obsidian-vault-probe-batch-2026-05-05.md:L25-L29](docs/research/shoulders/obsidian-vault-probe-batch-2026-05-05.md), [docs/research/shoulders/obsidian-vault-probe-batch-2026-05-05.md:L44-L57](docs/research/shoulders/obsidian-vault-probe-batch-2026-05-05.md)).
- Hermes lane stayed `reference_only` and explicitly rejected a second bridge authority or daemon cloning ([docs/research/shoulders/hermes-kanban-bridge-probe-report-2026-05-05.md:L25-L29](docs/research/shoulders/hermes-kanban-bridge-probe-report-2026-05-05.md), [docs/research/shoulders/hermes-kanban-bridge-probe-report-2026-05-05.md:L44-L57](docs/research/shoulders/hermes-kanban-bridge-probe-report-2026-05-05.md)).
- PR Factory lane stayed `reference_only` and limited its value to dry-run-first local-only orchestration ([docs/research/shoulders/pr-factory-orchestration-probe-batch-2026-05-05.md:L25-L29](docs/research/shoulders/pr-factory-orchestration-probe-batch-2026-05-05.md), [docs/research/shoulders/pr-factory-orchestration-probe-batch-2026-05-05.md:L44-L57](docs/research/shoulders/pr-factory-orchestration-probe-batch-2026-05-05.md)).
- OpenDesign v0.3 now has code-level repo-external mock evidence and five-gate pass status ([docs/research/prototypes/opendesign-v0.3-deep-visual-probe-2026-05-05.md:L25-L29](docs/research/prototypes/opendesign-v0.3-deep-visual-probe-2026-05-05.md), [docs/research/prototypes/opendesign-v0.3-deep-visual-probe-2026-05-05.md:L44-L57](docs/research/prototypes/opendesign-v0.3-deep-visual-probe-2026-05-05.md)).
- The older decision table is still directionally valid but is now superseded by the narrower per-dispatch outputs above ([docs/research/shoulders/adapt-decision-table-2026-05-05.md:L40-L45](docs/research/shoulders/adapt-decision-table-2026-05-05.md), [docs/research/shoulders/adapt-decision-table-2026-05-05.md:L96-L105](docs/research/shoulders/adapt-decision-table-2026-05-05.md)).

## Synthesis verdict

| lane | current class | conclusion | carry-forward |
|---|---|---|---|
| XHS | `reference_only` | two winners valid, auth boundary unresolved | deeper output-shape + auth-isolation probe |
| Bilibili comparator | `reference_only` | `yt-dlp` live, `Nemo2011` reserve-only | use for ceiling/drift explanation, not replacement |
| Console/H5 | `adapt` | `satnaing/shadcn-admin` is the only donor worth adapting | adapt layout/system patterns only |
| Vault / PARA | `contract-ready but gated` | `00-Inbox + raw 4-field + fail-loud env` is stable | use as future bridge/vault contract input |
| Hermes bridge | `reference_only` | borrow execution-plane discipline, reject second authority | keep inside existing API surface |
| PR Factory | `reference_only` | helper is valuable, but only as local-only orchestration tool | keep dry-run and containment hard |
| OpenDesign v0.3 | `reference_only prototype` | mock now proves the visual contract in code | keep repo-external mock as strongest visual evidence |

## Calls

1. `reference_only` shoulders:
   - both XHS winners
   - `yt-dlp`
   - Hermes Kanban Bridge
   - PR Factory helper

2. `adapt` shoulder:
   - `satnaing/shadcn-admin` only

3. `contract-ready but still gated` surfaces:
   - `00-Inbox + raw 4-field + fail-loud env`
   - OpenDesign/H5 visual contract

4. explicit non-calls:
   - no XHS runtime approval
   - no Bilibili comparator replacement
   - no second bridge authority
   - no tracked frontend implementation
   - no vault runtime approval

## Open risks

- The upcoming mirror dispatches still carry naming drift against some live local-only paths, especially after the narrower 76-82 outputs.
- `Nemo2011` remains reserve-only; any later policy or mirror doc must not describe it as a live clone result without new evidence.
- The H5 lane is visually stronger now, but route choice and tracked app implementation are still separate gates.

## Result

Wave 3B now has a cleaner handoff shape than the older one-shot decision table:

- what stays `reference_only` is explicit
- what is safe to `adapt` is singular and bounded
- what is contract-ready is named, but still gated
