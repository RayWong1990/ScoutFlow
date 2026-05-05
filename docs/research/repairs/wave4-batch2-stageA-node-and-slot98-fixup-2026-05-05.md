# Wave 4 Batch2 Stage A Node And Slot98 Fixup - 2026-05-05

## Status

repair note / evidence-backed / not authority / historical follow-up

This note records a follow-up repair for Stage A Node validation and a slot98 control-plane clarification. It does not replace the historical Batch2 report, checkpoint, diff bundle, or task authority surfaces.

## Scope

- Covers Stage A Node repair for `apps/capture-station`.
- Covers slot98 repair truth clarification for original dispatch scope vs b2v4 working-pack scope.
- Does not cover Batch3, bridge wire-in, vault runtime, authority state changes, Wave5 execution, or migration approval.

## Batch Baseline

- Original audit baseline: `3f29fe3a1853bc6c6233a71904416349f3c98292`
- Current repair baseline: `fae0bdbbcb063f609c55f910240e397749520336`
- Drift resolution: dynamic mainline drift reviewed; repair-relevant code and authority surfaces unchanged.
- Drift reviewed from original audit baseline to current repair baseline:
  - `e35c878` - docs: add STEP2 canonical V3 spec and checklist (#116)
  - `000caad` - docs: add STEP2A evidence notes and checklist updates (#117)
  - `1a29a1c` - docs: add STEP2B handoff package and close checklist
  - `fae0bdb` - Merge pull request #118 from RayWong1990/task/step2b-handoff-package
- Path drift reviewed: only `docs/research/repairs/**` changed. No drift touched `apps/capture-station/**`, `tools/check-docs-redlines.py`, `AGENTS.md`, `docs/current.md`, `docs/task-index.md`, `docs/specs/contracts-index.md`, or `services/api/scoutflow_api/main.py`.

## Original Audit Findings Addressed

- F-01: `LiveMetadataPanel` test / implementation drift.
- F-02: `FourPanelShell` glob included `*.test.tsx` files in the production module graph.
- F-03: slot98 repair statement under-described the actual repair scope.

## Before Fix Evidence

| Plane | Command | Result |
|---|---|---|
| Python docs | `python tools/check-docs-redlines.py` | passed |
| Python secrets | `python tools/check-secrets-redlines.py` | passed |
| Python API/contracts | `python -m pytest tests/api tests/contracts -q` | `162 passed` |
| Python bridge contracts | `python -m pytest tests/contracts -q -k bridge` | `28 passed, 88 deselected` |
| Node install | `npm install --no-package-lock` | installed `175` packages; no package lock created |
| Node tests | `npm test || true` | `1 failed / 7 tests`; `LiveMetadataPanel.test.tsx` could not find `audio_transcript` |
| Node build | `npm run build || true` | build completed, but production assets included test chunks and Vitest runtime chunk |
| Asset pollution | `find dist/assets -maxdepth 1 -type f \| rg '\.test-\|(^\|/)vi\.'` | found `LiveMetadataPanel.test-*.js`, `CaptureScopePanel.test-*.js`, `TrustTraceGraph.test-*.js`, `UrlBar.test-*.js`, and `vi.*.js` |

## Code Changes

- `apps/capture-station/src/layout/FourPanelShell.tsx`
  - Changed `import.meta.glob<PanelModule>("../features/**/*.tsx")` to a Vite array glob with a negative pattern: `["../features/**/*.tsx", "!../features/**/*.test.tsx"]`.
  - This preserves the existing panel-spec-driven lazy mounting model and only narrows the production module graph boundary.
- `apps/capture-station/src/features/live-metadata/LiveMetadataPanel.tsx`
  - Changed the metadata row label from `Audio transcript` to `audio_transcript`.
  - Rationale: this row is a controlled state/field surface, not only a human-readable decoration. `CaptureScopePanel` and `TrustTraceGraph` already use `audio_transcript` when expressing the blocked lane, so this panel now follows the same canonical state word.
- `apps/capture-station/src/features/live-metadata/LiveMetadataPanel.test.tsx`
  - Read and validated; no code change needed. The existing assertion already represented the canonical state word.

## After Fix Validation

| Plane | Command | Result |
|---|---|---|
| Node tests | `npm test` | `6 passed` test files / `7 passed` tests |
| Node build | `npm run build` | build completed; `37` modules transformed |
| Asset list | `find dist/assets -maxdepth 1 -type f \| sort` | only runtime panel and app chunks remained |
| Asset pollution grep | `find dist/assets -maxdepth 1 -type f \| rg '\.test-\|(^\|/)vi\.' && exit 1 || true` | no matches |
| Python docs | `python tools/check-docs-redlines.py` | passed |
| Python secrets | `python tools/check-secrets-redlines.py` | passed |
| Python API/contracts | `python -m pytest tests/api tests/contracts -q` | `162 passed` |
| Python bridge contracts | `python -m pytest tests/contracts -q -k bridge` | `28 passed, 88 deselected` |
| Diff check | `git diff --check` | passed |

## slot98 Repair Truth Clarification

Original PR98 dispatch allowed paths:

- `apps/capture-station/package.json`
- `apps/capture-station/vite.config.ts`
- `apps/capture-station/src/main.tsx`
- `apps/capture-station/src/App.tsx`

b2v4 PR98 dispatch allowed paths:

- `apps/capture-station/index.html`
- `apps/capture-station/package.json`
- `apps/capture-station/vite.config.ts`
- `apps/capture-station/src/main.tsx`
- `apps/capture-station/src/App.tsx`
- `tools/check-docs-redlines.py`

The two added b2v4 scope items were:

- `apps/capture-station/index.html`
- `tools/check-docs-redlines.py`

The original Batch2 report said the repair scope was limited to authorizing `apps/capture-station/index.html`. That statement was incomplete because the b2v4 working pack also authorized `tools/check-docs-redlines.py`, and merge commit `4a35105ab78ee8880644b9bec01860db11fb6b0d` modified `tools/check-docs-redlines.py`.

Observed merge commit touched files for slot98:

- `apps/capture-station/index.html`
- `apps/capture-station/package.json`
- `apps/capture-station/src/App.tsx`
- `apps/capture-station/src/main.tsx`
- `apps/capture-station/vite.config.ts`
- `tools/check-docs-redlines.py`

## Historical Interpretation Boundary

- The original Batch2 report is not rewritten in place.
- This note is a later repair and clarification note.
- Clean code after this repair does not mean the original batch had already proven Node validation.
- Stage A Node validation was rerun in this follow-up repair, not assumed from the original batch.
- The docs-only mainline drift through `fae0bdbbcb063f609c55f910240e397749520336` is not interpreted as a Stage A code change.

## Remaining Non-Blocking Risks

- This repair does not evaluate or implement bridge runtime wiring.
- This repair does not change the authority task ledger or allocate a new `T-P1A` task id.
- This repair does not validate visual design acceptance beyond Node test/build and production bundle cleanliness.

## Files Touched

- `apps/capture-station/src/layout/FourPanelShell.tsx`
- `apps/capture-station/src/features/live-metadata/LiveMetadataPanel.tsx`
- `docs/research/repairs/wave4-batch2-stageA-node-and-slot98-fixup-2026-05-05.md`
- `/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/FIXUP-Wave4-Batch2-v4-StageA-node-and-slot98-2026-05-05.md`

## Validation Commands

```bash
git fetch origin --prune
git log --oneline 3f29fe3a1853bc6c6233a71904416349f3c98292..fae0bdbbcb063f609c55f910240e397749520336
git diff --name-status 3f29fe3a1853bc6c6233a71904416349f3c98292..fae0bdbbcb063f609c55f910240e397749520336 -- apps/capture-station tools/check-docs-redlines.py AGENTS.md docs/current.md docs/task-index.md docs/specs/contracts-index.md services/api/scoutflow_api/main.py docs/research/repairs
python tools/check-docs-redlines.py
python tools/check-secrets-redlines.py
python -m pytest tests/api tests/contracts -q
python -m pytest tests/contracts -q -k bridge
cd apps/capture-station
npm install --no-package-lock
npm test
npm run build
find dist/assets -maxdepth 1 -type f | sort
find dist/assets -maxdepth 1 -type f | rg '\.test-|(^|/)vi\.' && exit 1 || true
cd ../..
git diff --check
```

## Conclusion

scoped_repair_evidence_clear on `BASE_REF=fae0bdbbcb063f609c55f910240e397749520336`.

The Stage A Node blocker is repaired on the current repair baseline, and the slot98 control-plane interpretation is narrowed by this follow-up evidence note without rewriting historical Batch2 artifacts.
