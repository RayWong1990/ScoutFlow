# Visual Regression Reporting 2026-05-05

> Status: candidate / reporting-only / not visual approval / not runtime approval
> Task: `T-P1A-099`
> Scope: summarize the current visual-regression baseline after slots `T-P1A-096` to `T-P1A-098`

## Current Baseline

- `tests/visual/five_gate_checklist.md` is tracked and CI-checked.
- `.github/workflows/h5-five-gate.yml` runs checklist structure validation plus `pytest tests/e2e -q`.
- `apps/capture-station/playwright.config.ts` exists as a static harness surface.
- `tests/visual/h5_visual_smoke.spec.ts` exists as a smoke spec that only runs when `CAPTURE_STATION_BASE_URL` is provided.

## What Is Verified Today

- Python baseline:
  - `python tools/check-docs-redlines.py`
  - `python tools/check-secrets-redlines.py`
  - `python -m pytest tests/api tests/contracts tests/e2e -q`
- Node baseline:
  - `npm test`
  - `npm run build`
  - `npm run lint`
  - `npm run typecheck`
- CI surfaces:
  - `docs-smoke`
  - `api-contract-tests`
  - `capture-station-node`
  - `five-gate-checklist`
  - `e2e-placeholder-baseline`

## What Is Not Verified Yet

- No screenshot bundle has been generated in this batch.
- No Playwright smoke has been executed in this batch.
- No browser automation run has been used as merge evidence in this batch.
- No human visual gate verdict has been recorded in authority docs.

## Reporting Rule

For future visual-touchpoint slots, the report should separate:

1. static readiness
2. automated execution evidence
3. screenshot evidence
4. human visual verdict

Do not collapse these into a single "pass".

## Suggested Reporting Shape

Use the repo-relative `tests/visual/reporting.md` as the lightweight template.
