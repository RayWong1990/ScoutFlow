---
title: PR247-PR249 START-HERE validation erratum
status: reference storage
type: erratum
created_at: 2026-05-08
related_prs: [247, 248, 249]
---

# PR247-PR249 START-HERE validation erratum

## Scope

This note corrects the validation trail for PR #247, PR #248, and PR #249. It does not roll back their landed docs payload.

## What the PR trail said

Those PRs recorded `python tools/refresh-start-here.py --check` as a passing validation step.

## Live fact

In PR workflow context, `refresh-start-here.py --check` was reading `origin/main` instead of the checked-out PR truth, so docs-check could fail on START-HERE freshness even when the branch itself was internally consistent.

## Repair landed here

- `tools/refresh-start-here.py` now resolves its git ref explicitly
- `--check` uses checked-out `HEAD` by default
- non-main local refresh defaults to `HEAD`
- local main refresh keeps `origin/main`

## Correction effect

- PR #247 / #248 / #249 must not be cited as clean CI precedent for START-HERE freshness
- the candidate-only / runtime-locked boundaries of those PRs remain unchanged
- this repair fixes tool truthfulness, not the substantive candidate docs they landed

## Source

- `https://github.com/RayWong1990/ScoutFlow/pull/247`
- `https://github.com/RayWong1990/ScoutFlow/pull/248`
- `https://github.com/RayWong1990/ScoutFlow/pull/249`
- `tools/refresh-start-here.py`
- `.github/workflows/docs-check.yml`

