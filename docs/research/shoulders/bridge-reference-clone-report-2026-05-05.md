---
title: ScoutFlow Bridge Reference Clone Local-only Mirror
date: 2026-05-05
type: shoulder-clone-mirror
status: candidate / research-only / tracked-mirror-only / not-runtime-approval
wave: 3B
related_task: T-P1A-062
---

# ScoutFlow Bridge Reference Clone Local-only Mirror

## Scope

- This dispatch resolves the bridge evidence question that blocked the earlier Batch 1 run.
- The goal is not to pretend there is a neat standalone `HERMES-KANBAN-BRIDGE` repo under `referencerepo/`; the goal is to prove whether a real local bridge donor surface exists anywhere in the workspace.
- The result remains `reference_only` and does not approve a second ScoutFlow bridge daemon or any `services/**` implementation.

## Inputs

- The earlier Hermes bridge probe already concluded that ScoutFlow only wants execution-plane and dispatcher patterns from this shoulder, not a second authority service ([docs/research/shoulders/hermes-kanban-bridge-probe-report-2026-05-05.md:L18-L29](docs/research/shoulders/hermes-kanban-bridge-probe-report-2026-05-05.md), [docs/research/shoulders/hermes-kanban-bridge-probe-report-2026-05-05.md:L33-L51](docs/research/shoulders/hermes-kanban-bridge-probe-report-2026-05-05.md)).
- Dispatch 84 explicitly left bridge unresolved because no bridge source existed under the legacy `scoutflow-T-P1A-044/referencerepo` clone surface ([docs/research/shoulders/referencerepo-structure-plan-2026-05-05.md:L42-L54](docs/research/shoulders/referencerepo-structure-plan-2026-05-05.md)).
- The user then pointed out a live machine-level Hermes surface under `~/.hermes`, which matches the earlier probe's claim that Hermes is actively used on this machine.

## Verified bridge donor surface

The real bridge donor surface is not a standalone clone in `workspace/*/referencerepo`. It is a live local Hermes workspace plus its runtime state:

| evidence role | verified path | proof |
|---|---|---|
| host repo root | `/Users/wanglei/workspace/hermes-agent` | README identifies the repo as `Hermes Agent` and documents gateway-backed usage (`/Users/wanglei/workspace/hermes-agent/README.md:L5-L21`, `/Users/wanglei/workspace/hermes-agent/README.md:L71-L83`) |
| bridge-specific source subtree | `/Users/wanglei/workspace/hermes-agent/plugins/kanban` | Kanban dashboard manifest and plugin API prove a bridge-like surface exists under this subtree (`/Users/wanglei/workspace/hermes-agent/plugins/kanban/dashboard/manifest.json:L2-L13`, `/Users/wanglei/workspace/hermes-agent/plugins/kanban/dashboard/plugin_api.py:L1-L24`) |
| runtime deprecation boundary | `/Users/wanglei/workspace/hermes-agent/plugins/kanban/systemd/hermes-kanban-dispatcher.service` | service file says standalone dispatcher is deprecated and gateway-hosted dispatch is the default (`/Users/wanglei/workspace/hermes-agent/plugins/kanban/systemd/hermes-kanban-dispatcher.service:L1-L24`) |
| live runtime truth | `/Users/wanglei/.hermes/config.yaml` and `/Users/wanglei/.hermes/gateway.pid` | local config keeps `kanban.dispatch_in_gateway: true`, and the running gateway process points back to `hermes_agent/hermes_cli/main.py gateway run` (`/Users/wanglei/.hermes/config.yaml:L363-L365`, `/Users/wanglei/.hermes/gateway.pid:L1-L1`) |

## Mirror decision

| canonical alias | actual local path | size | metadata result | note |
|---|---|---:|---|---|
| `HERMES-KANBAN-BRIDGE` | `/Users/wanglei/workspace/hermes-agent/plugins/kanban` | `160K` | `_SCOUTFLOW_META.local.md` created | bridge-specific subtree inside an actively used Hermes workspace |

## Why Dispatch 87 can proceed

- A real local donor surface exists. It is just not laid out as a standalone mirror repo under `referencerepo/`.
- The bridge-specific subtree is small enough to fit the `<100MB` mirror rule, while the machine-level runtime evidence under `~/.hermes` proves this is not a dead or hypothetical checkout.
- The service and config evidence agree with the earlier ScoutFlow bridge probe: the useful pattern is gateway-hosted dispatch and thin API/web bridge behavior, not a second daemon inside ScoutFlow.

## What this dispatch does not claim

- It does not claim `plugins/kanban` is a standalone GitHub repo.
- It does not claim ScoutFlow should clone the whole `hermes-agent` monorepo into its own `referencerepo/`.
- It does not approve `localhost:27124`, `services/**`, or runtime bridge code.

## Result

Dispatch 87 clears the evidence gate honestly:

- a real bridge donor surface exists on this machine
- the local-only canonical alias points to the bridge-specific subtree, not a fake standalone repo
- runtime evidence from `~/.hermes` confirms the donor is actively used
- the bridge lane may continue as `reference_only`
