---
title: Linked Anti-pattern Cross-link
status: blocked / candidate / not-authority
authority: not-authority
---

# Linked Anti-pattern Cross-link

U15 requested decision → U11 anti-pattern links. The U11 anti-pattern registry was not available in this run, so this file intentionally avoids fabricated `AP-X-XX` identifiers.

## Blocked cross-link table

| Decision area | Candidate anti-pattern concept | U11 ID status | Related PRs |
|---|---|---|---|
| Run-1 scope drift | Silent production expansion before charter wording | blocked_missing_u11_registry | #204, #205, #206, #231 |
| Synthetic evidence overclaim | `works` claim downgraded to `partial` | blocked_missing_u11_registry | #235, #236, #238, #239 |
| Replacement vs incremental topology | Later repair PR changes how earlier PRs should be read | blocked_missing_u11_registry | #226, #228, #232, #233, #234, #239 |
| Candidate/authority confusion | Candidate docs or preview proof mistaken for canonical authority | blocked_missing_u11_registry | #161-#196, #199-#203 |
| Compressed closeout smoothing | Single PR hides partial lane status | blocked_missing_u11_registry | #240 |

## Promotion rule

After the U11 registry is loaded, add only IDs that exist in that registry. Each ID should point back to the exact PR card and, ideally, to the evidence paragraph that triggered the anti-pattern mapping.
