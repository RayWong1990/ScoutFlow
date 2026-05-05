---
title: ScoutFlow Frontend Reference Clone Local-only Mirror
date: 2026-05-05
type: shoulder-clone-mirror
status: candidate / research-only / tracked-mirror-only / not-runtime-approval / not-frontend-implementation-approval
wave: 3B
related_task: T-P1A-061
---

# ScoutFlow Frontend Reference Clone Local-only Mirror

## Scope

- This dispatch binds the frontend canonical local-only alias to the real donor clone already verified in Wave 3B.
- The result is a metadata bridge only: it does not approve app scaffolding, router choice, or any `apps/**` implementation.
- `referencerepo/**` stays untracked.

## Inputs

- The console/H5 probe batch already locked `satnaing/shadcn-admin` as the strongest browser-H5 donor while explicitly limiting carry-forward to panel/layout/system patterns ([docs/research/shoulders/console-h5-frontend-probe-batch-2026-05-05.md:L21-L29](docs/research/shoulders/console-h5-frontend-probe-batch-2026-05-05.md), [docs/research/shoulders/console-h5-frontend-probe-batch-2026-05-05.md:L33-L50](docs/research/shoulders/console-h5-frontend-probe-batch-2026-05-05.md)).
- The adapt decision table made it the only `adapt` shoulder in the batch and kept that decision narrow ([docs/research/shoulders/adapt-decision-table-2026-05-05.md:L38-L45](docs/research/shoulders/adapt-decision-table-2026-05-05.md), [docs/research/shoulders/adapt-decision-table-2026-05-05.md:L64-L78](docs/research/shoulders/adapt-decision-table-2026-05-05.md)).
- Dispatch 84 recorded the naming drift between the canonical alias family and the live donor repo name ([docs/research/shoulders/referencerepo-structure-plan-2026-05-05.md:L27-L40](docs/research/shoulders/referencerepo-structure-plan-2026-05-05.md), [docs/research/shoulders/referencerepo-index-2026-05-05.md:L14-L17](docs/research/shoulders/referencerepo-index-2026-05-05.md)).

## Mirror decision

| canonical alias | actual local path | live donor repo | metadata result |
|---|---|---|---|
| `KIRANISM-SHADCN-STARTER` | `/Users/wanglei/workspace/scoutflow-T-P1A-044/referencerepo/console/shadcn-admin` | `satnaing/shadcn-admin` | `_SCOUTFLOW_META.local.md` created |

## Why the canonical alias differs from the real donor name

- The local clone that actually exists is `satnaing/shadcn-admin`, not a `Kiranism` repo. That donor already cleared the Wave 3B evidence bar as the best browser-H5 layout/system reference ([docs/research/shoulders/console-h5-frontend-probe-batch-2026-05-05.md:L33-L50](docs/research/shoulders/console-h5-frontend-probe-batch-2026-05-05.md)).
- The lifecycle handbook and later dispatch pack still refer to the frontend canonical bucket as a `KIRANISM-*` alias family, so the mirror layer has to carry both truths at once instead of forcing a fake rename.
- The tracked index now records the exact source path, commit `a6352e7df0de`, and size `4.0M`, which is comfortably inside the `<100MB` shoulder budget ([docs/research/shoulders/referencerepo-index-2026-05-05.md:L16-L17](docs/research/shoulders/referencerepo-index-2026-05-05.md)).

## Local-only metadata truth

The local-only file created by this dispatch is:

- `referencerepo/frontend/KIRANISM-SHADCN-STARTER/_SCOUTFLOW_META.local.md`

It records:

- `canonical_alias = KIRANISM-SHADCN-STARTER`
- the real source path under `.../referencerepo/console/shadcn-admin`
- `tracked_in_git = false`
- a note that the canonical alias is a mirror compatibility name, not the upstream repo name

## Result

Dispatch 86 keeps the frontend mirror truthful:

- the real donor remains `satnaing/shadcn-admin`
- the canonical alias exists only to stabilize the local-only mirror contract
- the donor stays layout/system reference only
- no frontend implementation approval is implied
