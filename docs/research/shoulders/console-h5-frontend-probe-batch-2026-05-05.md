---
title: ScoutFlow Console and H5 Frontend Shoulder Probe Batch
date: 2026-05-05
type: shoulder-probe-batch
status: candidate / research-only / not-authority / not-runtime-approval / not-frontend-implementation-approval
wave: 3B
related_task: T-P1A-053
---

# ScoutFlow Console and H5 Frontend Shoulder Probe Batch

## Scope

- This dispatch narrows the console/H5 shoulder lane to the strongest local-only browser donor plus its immediate carry-forward into the H5 design package.
- The goal is to sharpen reference and prototype input, not to approve frontend code.
- The route decision stays open: `do not pre-lock React Router 6`, and do not silently turn the station into a SaaS admin shell.

## Inputs

- The scan lane already locked three H5 constraints: `no SSR requirement`, `no Electron`, and `no admin-dashboard template lock-in`, while selecting `satnaing/shadcn-admin` as the strongest single clone candidate ([docs/research/shoulders/console-reference-scan-2026-05-04.md:L20-L33](docs/research/shoulders/console-reference-scan-2026-05-04.md), [docs/research/shoulders/console-reference-scan-2026-05-04.md:L44-L63](docs/research/shoulders/console-reference-scan-2026-05-04.md)).
- The earlier Wave 3B probe recorded `satnaing/shadcn-admin` as the primary local-only console clone and captured its app-shell evidence ([docs/research/shoulders/shoulders-probe-batch-1-2026-05-05.md:L69-L83](docs/research/shoulders/shoulders-probe-batch-1-2026-05-05.md)).
- The adapt decision table made `satnaing/shadcn-admin` the only `adapt` shoulder in the batch and explicitly limited that carry-forward to layout/system patterns ([docs/research/shoulders/adapt-decision-table-2026-05-05.md:L38-L45](docs/research/shoulders/adapt-decision-table-2026-05-05.md), [docs/research/shoulders/adapt-decision-table-2026-05-05.md:L64-L78](docs/research/shoulders/adapt-decision-table-2026-05-05.md)).
- The OpenDesign probe and H5 design brief already define the target operator surface as a four-panel workstation rather than a generic dashboard ([docs/research/prototypes/h5-opendesign-probe-2026-05-04.md:L73-L83](docs/research/prototypes/h5-opendesign-probe-2026-05-04.md), [docs/research/prototypes/h5-opendesign-probe-2026-05-04.md:L123-L147](docs/research/prototypes/h5-opendesign-probe-2026-05-04.md), [docs/visual/h5-capture-station/design-brief.md:L35-L45](docs/visual/h5-capture-station/design-brief.md), [docs/visual/h5-capture-station/design-brief.md:L61-L81](docs/visual/h5-capture-station/design-brief.md)).

## Batch verdict

| shoulder | decision | integration proposal | confidence | next_action |
|---|---|---|---:|---|
| `CONSOLE-CLI / satnaing/shadcn-admin` | continue | `adapt panel/layout/system patterns only` | 0.82 | keep as primary browser-H5 donor |

## Probe findings

### shoulder CONSOLE-CLI / satnaing/shadcn-admin

Decision: keep `satnaing/shadcn-admin` as the primary browser-H5 donor, but adapt only panel/layout/data-shell patterns and not its sidebar-first admin information architecture.

Why:

- The scan lane already judged it the best single local-only browser donor because it stays on `Vite + TanStack Router + TanStack Query + React Hook Form + Lucide + Zustand` without pulling ScoutFlow into a Next.js or Electron shell ([docs/research/shoulders/console-reference-scan-2026-05-04.md:L29-L33](docs/research/shoulders/console-reference-scan-2026-05-04.md), [docs/research/shoulders/console-reference-scan-2026-05-04.md:L214-L220](docs/research/shoulders/console-reference-scan-2026-05-04.md)).
- The earlier local-only probe showed the repo explicitly positions itself as a Shadcn + Vite admin dashboard UI and confirms the exact app-shell stack ScoutFlow wants to borrow, not clone wholesale ([docs/research/shoulders/shoulders-probe-batch-1-2026-05-05.md:L71-L78](docs/research/shoulders/shoulders-probe-batch-1-2026-05-05.md)).
- The adapt decision table is already conservative: this is the only shoulder promoted to `adapt`, and even then only for panel zoning, query/router shell patterns, and component discipline ([docs/research/shoulders/adapt-decision-table-2026-05-05.md:L42-L45](docs/research/shoulders/adapt-decision-table-2026-05-05.md), [docs/research/shoulders/adapt-decision-table-2026-05-05.md:L66-L78](docs/research/shoulders/adapt-decision-table-2026-05-05.md)).
- The OpenDesign probe and H5 design brief keep the target surface anchored in a four-panel operator workstation, which means the donor is useful only when filtered through that narrower visual/product posture ([docs/research/prototypes/h5-opendesign-probe-2026-05-04.md:L77-L83](docs/research/prototypes/h5-opendesign-probe-2026-05-04.md), [docs/research/prototypes/h5-opendesign-probe-2026-05-04.md:L127-L145](docs/research/prototypes/h5-opendesign-probe-2026-05-04.md), [docs/visual/h5-capture-station/design-brief.md:L12-L19](docs/visual/h5-capture-station/design-brief.md), [docs/visual/h5-capture-station/design-brief.md:L37-L60](docs/visual/h5-capture-station/design-brief.md)).

Carry-forward:

- keep `satnaing/shadcn-admin` as the primary local-only console clone
- adapt panel zoning, component discipline, and data-shell patterns only
- do not inherit sidebar-first dashboard IA, auth shell assumptions, or template chrome
- keep route choice open; do not pre-lock React Router 6

## Reserve note

- `Kiranism/tanstack-start-dashboard` stays reserve-only for router/query/form comparison rather than becoming the primary donor ([docs/research/shoulders/console-reference-scan-2026-05-04.md:L31-L33](docs/research/shoulders/console-reference-scan-2026-05-04.md), [docs/research/shoulders/adapt-decision-table-2026-05-05.md:L76-L78](docs/research/shoulders/adapt-decision-table-2026-05-05.md)).

## Result

This batch keeps the console/H5 conclusion tight:

- `satnaing/shadcn-admin` is the main donor
- the H5 station remains a four-panel operator surface
- route choice stays deferred
- no frontend implementation approval is implied
