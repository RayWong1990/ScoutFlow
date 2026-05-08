---
title: Code-bearing Conversion Gate
status: candidate / docs-only / not-authority
authority: not-authority
ingest_basis:
  - GPT Pro pack A `05-lane-d-code-bearing-dispatch-candidate.md`
  - GPT Pro pack C `Lane-D-visual-productization-candidate-handoff.md`
  - GPT Pro pack C `OPUS-AUDIT-POINTS.md`
---

# Code-bearing Conversion Gate

## Purpose

This file defines what must be true before Lane D can convert from `docs-only` to `code-bearing`. It is not itself an approval.

## Conversion Conditions

Lane D may become code-bearing only when all conditions are explicitly confirmed:

1. Product lane slot usage is confirmed.
2. Target components are named and bounded.
3. Dependency decision is explicit, with default `no install`.
4. Allowed code paths are bounded under `apps/capture-station/src/**`.
5. Validation commands are named in advance.
6. Human localhost visual review is required.
7. Opus dependency/visual audit is required before merge.

Without all seven, Lane D remains `candidate / docs-only / not-authority`.

## Allowed-path Candidate

Future code-bearing dispatches should stay bounded to:

- `apps/capture-station/src/**/*.tsx`
- `apps/capture-station/src/**/*.css`
- `apps/capture-station/src/**/*.module.css`
- `apps/capture-station/src/**/*.test.ts`
- `apps/capture-station/src/**/*.test.tsx`
- `apps/capture-station/src/assets/**`
- `apps/capture-station/src/styles/**`

Any broader path request requires a fresh dispatch review.

## Validation Baseline

```bash
pnpm --dir apps/capture-station test
pnpm --dir apps/capture-station lint
pnpm --dir apps/capture-station typecheck
pnpm --dir apps/capture-station build
python tools/check-docs-redlines.py
python tools/check-secrets-redlines.py
git diff --check
```

Optional targeted tests remain secondary to the full boundary above.

## Human Gate Wording

The human approval text must stay verbatim:

```text
Approve Lane D visual productization code-bearing PR.
No dependency adoption approved unless separately stated.
No runtime/source/true-write/migration/browser automation approval.
```

## Stop-line

Stop immediately if any of the following occurs:

- A dependency install is treated as default.
- `apps/**` edits are attempted before explicit code-bearing approval.
- Lane D scope is merged with Lane A/B/C in the same PR.
- Runtime, source, true-write, migration, or browser automation claims are implied.
- PF-V raw HTML/JSON is imported as runtime.
- Preview styling can be mistaken for committed state.
- Blocked/disabled states become visually soft enough to hide holds.
- Authority files are modified under cover of visual work.

## Opus Audit Prompt

Use the following before any Lane D code-bearing merge:

```text
You are Opus dependency and visual-productization auditor for ScoutFlow Lane D.

Input packet:
- PF-V asset map
- component target map
- state visual grammar
- dependency decision intake
- proposed code-bearing dispatch if any

Audit questions:
1. Is Lane D still docs-only unless user explicitly approved code-bearing work?
2. If code-bearing is proposed, does it name product lane slot impact?
3. Does dependency selection avoid contaminating Lane A/B/C?
4. Does it avoid dependency install by default?
5. Are state labels and blocked-state visual grammar stronger than decoration?
6. Does the proposal avoid browser automation and runtime/source/write scope?
7. Are validation and localhost review defined?

Return: V-PASS-CLEAR / V-PASS-WITH-AMENDMENTS / V-PARTIAL / V-REJECT.
Reject if dependency install is treated as automatic or if visual work hides evidence boundaries.
```

## Expected Closeout Shape

Any future Lane D code-bearing closeout should still say:

- visual productization only,
- no dependency approval unless separately granted,
- no runtime approval,
- no true-write approval,
- no migration approval,
- no browser automation approval,
- remaining holds listed explicitly.
