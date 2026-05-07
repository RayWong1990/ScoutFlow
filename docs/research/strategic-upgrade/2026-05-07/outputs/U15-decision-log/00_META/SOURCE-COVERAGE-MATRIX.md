---
title: Source Coverage Matrix
status: candidate / not-authority
authority: not-authority
---

# Source Coverage Matrix

| Source family | Loaded in this delivery | Evidence use | Gap policy |
|---|---:|---|---|
| GitHub PR metadata #161-#240 | yes | primary PR existence, title, body summary, merged_at, merged state | PR #229 excluded because it was closed but not merged |
| GitHub PR detail #231/#239/#240 | yes | high-confidence amendment and run closeout cards | used as anchor PRs for amendment trail |
| GitHub PR metadata early #1 | yes | bootstrap decision card to reach 80 merged PRs | body-level details thin |
| Local Post176 cloud audit pack | yes | Wave 4-5 / Dispatch127-176 / post-dispatch context | used as supporting source, not full canonical truth |
| docs/decision-log.md live file | not fully loaded in this artifact build | boundary reference only | atlas does not modify or replace canonical decision log |
| PRD/SRD amendment directories live | partially represented by local Post176 pack | legacy and amendment context | not treated as exhaustive |
| U10 runbook registry | not loaded | cross-link target blocked | no runbook IDs invented |
| U11 anti-pattern registry | not loaded | cross-link target blocked | no AP-X-XX IDs invented |
| ContentFlow L1 source | not loaded | legacy patterns marked candidate | legacy docs are not counted as ScoutFlow PR cards |

## Gate result

This package is a **candidate atlas delivery**, not canonical repository state. It is intentionally useful before perfect completeness: real PR numbers are used, missing registries are made explicit, and unverifiable U11 anti-pattern links are not fabricated.
