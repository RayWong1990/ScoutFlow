---
title: Final reservoir closeout map
status: candidate / research / not-authority
created_at: 2026-05-06
related_dispatch: PF-GLOBAL-12
---

# Final reservoir closeout map

## reservoir_groups

| group | rows | open_after_state | closeout_rule |
|---|---|---|---|
| `PF-C1 proof pair` | `12` | `preview_only_localhost_ready` | close only after usefulness signal exists |
| `PF-C2 RAW handoff` | `12` | `c1_partial_or_pass` | close only with RAW evidence and no true-write shortcut |
| `PF-C3 compression` | `6` | `parallel_prep_after_successor_entry` | close only after real proof artifacts exist |
| `PF-C4 hardening` | `8` | `c1_c2_pass_or_strong_partial` | close only after proof and visual gates are real |
| `PF-GLOBAL support` | `12` | `never_auto_open` | stays reservoir unless a later dispatch promotes a row |

## closeout_rules

- Reservoir rows do not become active because a similar file already exists.
- Promotion must be explicit, scoped, and tied to a fresh live baseline.
- Support files should be referenced, not recopied into authority docs.

## verdict

- `T-PASS` for final mapping only; no reservoir row is opened by this document.
