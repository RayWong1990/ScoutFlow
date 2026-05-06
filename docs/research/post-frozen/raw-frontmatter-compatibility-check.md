---
title: RAW Frontmatter Compatibility Check
status: candidate / compatibility-check / not-authority
created_at: 2026-05-06
related_dispatch: PF-C2-02
---

# RAW Frontmatter Compatibility Check

## Check Result

`compatible_enough_for_candidate_handoff = yes`

## What Was Checked

| Item | Result | Note |
| --- | --- | --- |
| `title` | pass | Bridge preview already emits a stable human-readable title. |
| `date` | pass | Bridge preview emits ISO date. |
| `tags` | pass | Existing preview tag string is compact and non-secret. |
| `status` | pass | `pending` matches candidate posture and does not overclaim intake completion. |

## Non-Goals

- This is not a RAW schema change.
- This is not a RAW app integration.
- This does not prove actual intake occurred.

## Compatibility Note

The candidate note can safely reuse current bridge frontmatter because the shape is small, deterministic, and already aligned with preview-only boundary language.
