---
title: ScoutFlow H5 Capture Station Design Package
date: 2026-05-05
status: candidate / design-only / not-frontend-implementation-approval
related_task: T-P1A-046
---

# ScoutFlow H5 Capture Station Design Package

This folder defines the Wave 3B design package for the future browser H5 capture surface.

Scope of this package:

- lock the 4-panel information architecture
- lock the trust-trace graph visual semantics
- lock the 5 Gate design audit checklist

Out of scope:

- no `apps/**`
- no frontend implementation
- no route wiring
- no runtime approval

Files:

- `design-brief.md`: operator-facing layout, tone, and state presentation
- `trust-trace-graph-spec.md`: trust-trace graph node/edge and visual encoding rules
- `five-gate-checklist.md`: hard visual audit gate for later stills/pages

Design position:

- browser H5 workstation, not desktop shell
- strong visual operator surface, not admin dashboard template
- metadata and state clarity first, decoration second

Carry-forward:

- `services/api/scoutflow_api/bridge/SPEC.md` locks the route-group boundary
- this package locks how that future data should be seen, not how it is coded
