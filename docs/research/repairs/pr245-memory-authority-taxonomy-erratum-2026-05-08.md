---
title: PR245 memory authority taxonomy erratum
status: reference storage
type: erratum
created_at: 2026-05-08
related_pr: 245
---

# PR245 memory authority taxonomy erratum

## Scope

This note corrects PR #245's authority taxonomy only. It does not delete the cross-vendor memory pack.

## What the PR trail said

- `docs/memory/**` files were written with `status: current authority`
- `README.md` / `INDEX.md` described the memory pack as same-level with `docs/current.md` / `docs/task-index.md` / `docs/decision-log.md` / `docs/00-START-HERE.md`

## Live correction

`docs/memory/**` is an operational memory reference layer, not a current-authority write surface.

Truth after this repair:

- `docs/memory/**` frontmatter uses `status: reference storage`
- memory entries keep `cross_vendor_readers`
- memory entries now carry `memory_role: cross-vendor instinct source`
- `L-AUTHORITY-DRIFT` no longer expands current-authority surfaces to `AGENTS.md` / root `CLAUDE.md`

## Correction effect

- cross-vendor git-tracked memory stays available
- no new status word is introduced
- no authority surface is added beyond the locked four current-authority files

## Source

- `https://github.com/RayWong1990/ScoutFlow/pull/245`
- `docs/memory/README.md`
- `docs/memory/INDEX.md`
- `docs/memory/lessons/L-AUTHORITY-DRIFT.md`

