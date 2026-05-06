---
title: ScoutFlow and RAW SoR Handoff Matrix
status: candidate / handoff-matrix / not-authority
created_at: 2026-05-06
related_dispatch: PF-C2-10
---

# ScoutFlow and RAW SoR Handoff Matrix

| Domain | Owner | Current state | Boundary |
| --- | --- | --- | --- |
| preview artifact generation | ScoutFlow | complete for C1 three-url proof | preview-only, write-disabled |
| staged note preparation | ScoutFlow | complete for two candidate notes | repo-local staging only |
| copy into `~/workspace/raw/00-Inbox/` | User / RAW side | pending | ScoutFlow must not perform this write |
| intake verdict | RAW | pending | no dual SoR; ScoutFlow records only readback |
| script expansion | RAW | pending | ScoutFlow candidate seed does not replace RAW acceptance |

## SoR Rule

ScoutFlow owns preview and evidence preparation. RAW owns intake, compile, and downstream script acceptance. This split remains explicit until a future human-approved true-write gate exists.
