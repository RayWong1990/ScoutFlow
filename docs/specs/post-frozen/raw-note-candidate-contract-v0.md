---
title: RAW Note Candidate Contract v0
status: candidate / contract / not-authority
created_at: 2026-05-06
related_dispatch: PF-C2-01
---

# RAW Note Candidate Contract v0

## Purpose

Define the smallest note shape that ScoutFlow can hand to RAW without changing RAW taxonomy or pretending a true vault write already exists.

## Frontmatter

RAW handoff candidates stay at four fields:

```yaml
title: <string>
date: <YYYY-MM-DD>
tags: <string>
status: pending
```

## Body Sections

The note body must stay inside these sections:

1. `## Source Snapshot`
2. `## Topic Card Lite`
3. `## Preview Boundary`
4. `## Transfer Note`

## Boundary

- ScoutFlow owns generation of the candidate note body.
- RAW owns actual intake, consumption, compile, and script expansion.
- This contract does not create a second SoR and does not approve writing into `~/workspace/raw/`.
