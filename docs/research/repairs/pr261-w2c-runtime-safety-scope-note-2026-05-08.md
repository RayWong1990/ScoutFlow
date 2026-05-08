---
title: PR261 W2C runtime safety scope note
status: reference storage
type: repair-note
created_at: 2026-05-08
related_pr: 261
---

# PR261 W2C runtime safety scope note

## Allowed app paths

- `apps/capture-station/src/lib/w2c-runtime.tsx`
- `apps/capture-station/src/lib/w2c-runtime.test.tsx`

## Allowed tool paths

- `tools/refresh-start-here.py`
- `tools/check-docs-redlines.py`
- `tests/tools/test_refresh_start_here.py`
- `tests/tools/test_check_docs_redlines.py`

## Boundary

- no `services/**` changes
- no `workers/**` or `packages/**` changes
- no runtime unlock / migration unlock / browser automation unlock / vault true-write unlock
- repair target is limited to START-HERE truth probes, docs taxonomy guard, and W2C stale-response / default-blocked safety
