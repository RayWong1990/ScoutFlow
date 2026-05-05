---
title: ScoutFlow Hermes Kanban Bridge Probe Report
date: 2026-05-05
type: shoulder-probe-batch
status: candidate / research-only / not-authority / not-runtime-approval
wave: 3B
related_task: T-P1A-055
---

# ScoutFlow Hermes Kanban Bridge Probe Report

## Scope

- This dispatch probes exactly one shoulder and extracts only three narrow ideas: execution-plane separation, durable dispatcher/state handling, and file-or-db-as-source-of-truth operating style.
- The report does not approve a second authority service, does not open a new bridge daemon inside ScoutFlow, and does not treat `localhost:27124` as an implementation commitment.
- All conclusions stay at `reference_only`.

## Inputs

- The baseline roadmap names `Hermes Kanban Bridge` as a Wave 3B/4 reference shoulder and explicitly frames it as a `port 27124` pattern reference rather than a promoted runtime surface ([docs/architecture/baseline-roadmap-after-pr54-candidate-2026-05-04.md:L279-L285](docs/architecture/baseline-roadmap-after-pr54-candidate-2026-05-04.md), [docs/architecture/baseline-roadmap-after-pr54-candidate-2026-05-04.md:L319-L328](docs/architecture/baseline-roadmap-after-pr54-candidate-2026-05-04.md), [docs/architecture/baseline-roadmap-after-pr54-candidate-2026-05-04.md:L359-L367](docs/architecture/baseline-roadmap-after-pr54-candidate-2026-05-04.md)).
- The shoulders lifecycle handbook already places `HERMES-KANBAN-BRIDGE` under the `frontend/` local-only reference tree and defines the exact carry-forward ScoutFlow cares about: `port 27124` plus `file-as-source-of-truth REST API` ([docs/architecture/shoulders-lifecycle-handbook-candidate-2026-05-04.md:L436-L440](docs/architecture/shoulders-lifecycle-handbook-candidate-2026-05-04.md), [docs/architecture/shoulders-lifecycle-handbook-candidate-2026-05-04.md:L470-L503](docs/architecture/shoulders-lifecycle-handbook-candidate-2026-05-04.md), [docs/architecture/shoulders-lifecycle-handbook-candidate-2026-05-04.md:L505-L533](docs/architecture/shoulders-lifecycle-handbook-candidate-2026-05-04.md)).
- The acceptance review already corrected one major risk: ScoutFlow must not implement a second `Bridge on localhost:27124`; any bridge capability has to stay inside the existing API authority surface ([docs/research/opus-v3-acceptance-prd-srd-amendment-roadmap-review-2026-05-04.md:L83-L85](docs/research/opus-v3-acceptance-prd-srd-amendment-roadmap-review-2026-05-04.md)).
- The local Hermes Kanban design spec describes a durable SQLite-backed board, a dumb dispatcher with atomic claims, and an execution-plane-only design; the local systemd unit shows the current standalone daemon shape is deprecated in favor of gateway-hosted dispatch ([../../hermes-agent/docs/hermes-kanban-v1-spec.pdf:L14-L28](../../hermes-agent/docs/hermes-kanban-v1-spec.pdf), [../../hermes-agent/docs/hermes-kanban-v1-spec.pdf:L447-L459](../../hermes-agent/docs/hermes-kanban-v1-spec.pdf), [../../hermes-agent/docs/hermes-kanban-v1-spec.pdf:L730-L743](../../hermes-agent/docs/hermes-kanban-v1-spec.pdf), [../../hermes-agent/plugins/kanban/systemd/hermes-kanban-dispatcher.service:L1-L14](../../hermes-agent/plugins/kanban/systemd/hermes-kanban-dispatcher.service), [../../hermes-agent/plugins/kanban/systemd/hermes-kanban-dispatcher.service:L21-L29](../../hermes-agent/plugins/kanban/systemd/hermes-kanban-dispatcher.service)).

## Batch verdict

| shoulder | decision | integration proposal | confidence | next_action |
|---|---|---|---:|---|
| `HERMES-KANBAN-BRIDGE` | continue | `reference_only -> extract execution-plane patterns only` | 0.72 | keep as local bridge-pattern donor, not a runtime blueprint |

## Probe findings

### shoulder HERMES-KANBAN-BRIDGE

Decision: keep Hermes Kanban Bridge as a `reference_only` shoulder for execution-plane and dispatcher patterns, but do not inherit it as a standalone ScoutFlow bridge service.

Why:

- ScoutFlow's own planning docs already constrain the shoulder to a narrow reference role: local-only, size-bounded, and focused on `port 27124` plus `file-as-source-of-truth` patterns rather than Kanban product logic ([docs/architecture/shoulders-lifecycle-handbook-candidate-2026-05-04.md:L436-L440](docs/architecture/shoulders-lifecycle-handbook-candidate-2026-05-04.md), [docs/architecture/shoulders-lifecycle-handbook-candidate-2026-05-04.md:L489-L503](docs/architecture/shoulders-lifecycle-handbook-candidate-2026-05-04.md), [docs/architecture/shoulders-lifecycle-handbook-candidate-2026-05-04.md:L520-L533](docs/architecture/shoulders-lifecycle-handbook-candidate-2026-05-04.md)).
- The local Hermes Kanban design spec is valuable because it stays in the execution plane: durable SQLite-backed board, dumb dispatcher with atomic claims, and a first-class orchestrator profile that acts as dispatcher rather than worker ([../../hermes-agent/docs/hermes-kanban-v1-spec.pdf:L14-L28](../../hermes-agent/docs/hermes-kanban-v1-spec.pdf), [../../hermes-agent/docs/hermes-kanban-v1-spec.pdf:L447-L459](../../hermes-agent/docs/hermes-kanban-v1-spec.pdf), [../../hermes-agent/docs/hermes-kanban-v1-spec.pdf:L730-L743](../../hermes-agent/docs/hermes-kanban-v1-spec.pdf)).
- The current local service artifact is itself a warning label: the standalone dispatcher is deprecated, the gateway now hosts dispatch by default, and running two dispatchers against the same `kanban.db` is explicitly unsupported ([../../hermes-agent/plugins/kanban/systemd/hermes-kanban-dispatcher.service:L1-L14](../../hermes-agent/plugins/kanban/systemd/hermes-kanban-dispatcher.service), [../../hermes-agent/plugins/kanban/systemd/hermes-kanban-dispatcher.service:L17-L29](../../hermes-agent/plugins/kanban/systemd/hermes-kanban-dispatcher.service)).
- That warning lines up with ScoutFlow's own architecture correction: the bridge cannot become a second authority on `localhost:27124`; it has to remain a capability inside the existing API/state machine surface ([docs/research/opus-v3-acceptance-prd-srd-amendment-roadmap-review-2026-05-04.md:L83-L85](docs/research/opus-v3-acceptance-prd-srd-amendment-roadmap-review-2026-05-04.md), [docs/architecture/baseline-roadmap-after-pr54-candidate-2026-05-04.md:L341-L355](docs/architecture/baseline-roadmap-after-pr54-candidate-2026-05-04.md)).

Carry-forward:

- borrow execution-plane separation, durable dispatcher/state ideas, and orchestrator-not-worker discipline
- keep any future ScoutFlow bridge inside the existing API authority surface
- do not promote `localhost:27124` from reference pattern to implementation commitment
- do not inherit Kanban business logic or standalone daemon topology

## Result

This batch keeps the Hermes shoulder conclusion honest:

- it is a good execution-plane reference
- it is not a ScoutFlow runtime blueprint
- the highest-signal lesson is boundary discipline, not daemon cloning
