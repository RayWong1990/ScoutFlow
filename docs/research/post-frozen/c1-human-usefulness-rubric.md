---
title: PF-C1 Human Usefulness Rubric
status: candidate / rubric / not-authority
created_at: 2026-05-06
related_dispatch: PF-C1-06
human_gate: usefulness_verdict
---

# PF-C1 Human Usefulness Rubric

## Purpose

Give `C1-08` a stable, low-friction rubric so the user can judge whether each topic-card-lite preview is worth follow-up without drifting into a full design critique or final product verdict.

## Per-URL Verdict Set

| Verdict | Meaning | Counts as useful | Typical reason |
| --- | --- | --- | --- |
| `follow` | Strong enough to carry into the next lane with light clarification only | yes | The card preserves the source value and the preview shape feels directly actionable. |
| `needs-edit` | Worth keeping, but wording or field emphasis needs manual correction | yes | The source is useful, but the card over-objectifies, misses context, or needs better emphasis. |
| `park` | Not wrong enough to reject, but not worth taking forward now | no | The card is structurally fine but weak in information density or downstream value. |
| `reject` | Misleading, over-claims, or too costly to fix | no | The card shape harms trust more than it helps review speed. |

## One-Line Reason Rule

Each URL verdict must carry one short reason line that answers one of these:

- what made it worth following
- what made it too costly to edit
- where the card over-objectified the source
- where the preview preserved evidence but still failed usefulness

## C1 Rollup Rule

- `2/3` or `3/3` useful (`follow` or `needs-edit`) => `pass`
- `1/3` useful => `partial`
- `0/3` useful => `fail`

## Boundary

- This rubric does not approve C2 automatically.
- C2 may open only if the same human gate explicitly says `c2_go_no_go=yes`.
- This rubric does not replace visual review, RAW intake, or script-seed acceptance.
