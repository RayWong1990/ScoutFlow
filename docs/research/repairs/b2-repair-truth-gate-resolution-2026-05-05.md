# B2 Repair Truth Gate Resolution - 2026-05-05

## Status

- state: `truth_gate_resolution`
- scope: drift assessment only
- authority: not authority / not repair implementation / not historical FIXUP
- implementation status: no app code changes, no Node run, no Python test run

## Original Authorized Baseline

- original `BASE_REF`: `3f29fe3a1853bc6c6233a71904416349f3c98292`
- original repair target: Stage A Node repair plus slot98 repair truth clarification
- degraded-run note already present:
  - `/Users/wanglei/workspace/ScoutFlow-B2-repair-stageA-slot98/docs/research/repairs/b2-repair-truth-gate-failed-2026-05-05.md`

## Current Origin Main

After `git fetch origin --prune`:

- current `origin/main`: `000caad1364e9b06c15d2f674a23dd648163206d`
- current branch in isolated worktree: `codex/b2-repair-stagea-slot98-fixup`
- working directory used:
  - `/Users/wanglei/workspace/ScoutFlow-B2-repair-stageA-slot98`

## Drift Commit List

Command:

```bash
git log --oneline --decorate --graph 3f29fe3a1853bc6c6233a71904416349f3c98292..000caad1364e9b06c15d2f674a23dd648163206d
```

Result:

```text
* 000caad (HEAD -> codex/b2-repair-stagea-slot98-fixup, origin/main, origin/HEAD, main) docs: add STEP2A evidence notes and checklist updates (#117)
* e35c878 docs: add STEP2 canonical V3 spec and checklist (#116)
```

## Drift Touched Paths Summary

Command:

```bash
git diff --name-status 3f29fe3a1853bc6c6233a71904416349f3c98292..000caad1364e9b06c15d2f674a23dd648163206d
```

Result:

```text
A docs/research/repairs/dispatch127-176-pack-design-v3-2026-05-05.md
A docs/research/repairs/step2-local-mode-and-packlint-surface-2026-05-05.md
A docs/research/repairs/step2-prep-checklist-2026-05-05.md
A docs/research/repairs/step2-runner-api-disk-budget-2026-05-05.md
A docs/research/repairs/step2-runtime-readiness-and-screenshot-note-2026-05-05.md
A docs/research/repairs/wave5-scope-and-template-extraction-2026-05-05.md
```

Per-commit path impact:

| Commit | Subject | Touched files |
|---|---|---|
| `e35c878cc5dc3c4c9d3f008c8f26290b277c9ffa` | `docs: add STEP2 canonical V3 spec and checklist (#116)` | `docs/research/repairs/dispatch127-176-pack-design-v3-2026-05-05.md`; `docs/research/repairs/step2-prep-checklist-2026-05-05.md` |
| `000caad1364e9b06c15d2f674a23dd648163206d` | `docs: add STEP2A evidence notes and checklist updates (#117)` | `docs/research/repairs/step2-local-mode-and-packlint-surface-2026-05-05.md`; `docs/research/repairs/step2-prep-checklist-2026-05-05.md`; `docs/research/repairs/step2-runner-api-disk-budget-2026-05-05.md`; `docs/research/repairs/step2-runtime-readiness-and-screenshot-note-2026-05-05.md`; `docs/research/repairs/wave5-scope-and-template-extraction-2026-05-05.md` |

## Repair-Relevant Surface Check

Checked surface:

```bash
git diff --name-status \
  3f29fe3a1853bc6c6233a71904416349f3c98292..000caad1364e9b06c15d2f674a23dd648163206d \
  -- apps/capture-station \
     tools/check-docs-redlines.py \
     AGENTS.md \
     docs/current.md \
     docs/task-index.md \
     docs/specs/contracts-index.md \
     docs/research/repairs \
     services/api/scoutflow_api/main.py
```

Observed impact:

| Surface | Touched by drift? | Impact |
|---|---:|---|
| `apps/capture-station/**` | no | No direct Stage A code drift. |
| `tools/check-docs-redlines.py` | no | No slot98 validator drift. |
| `AGENTS.md` | no | No repo instruction drift. |
| `docs/current.md` | no | No current-state authority drift. |
| `docs/task-index.md` | no | No task-index authority drift. |
| `docs/specs/contracts-index.md` | no | No promoted contract baseline drift. |
| `docs/research/repairs/**` | yes | Repair-note/reference directory changed with STEP2 / Wave5 research notes. |
| `services/api/scoutflow_api/main.py` | no | No API entrypoint drift. |

## Interpretation

The drift does not alter the Stage A frontend code, the slot98 validator, the bridge entrypoint, or authority files. It does alter `docs/research/repairs/**`, which is one of the explicit surfaces to inspect and one of the original prompt's style-reference inputs.

Therefore the drift is not enough to invalidate the repair objective, but it is enough that the original prompt should not be reused unchanged. The baseline and input-material inventory should be patched to reflect the live `000caad...` state and the newly added repair/research-note files.

## Conclusion

Conclusion: `NEEDS_PROMPT_PATCH`

Rationale:

- the drift touches a repair-reference directory: `docs/research/repairs/**`
- the touched files are bounded STEP2 / Wave5 research or checklist notes
- no direct Stage A app code changed
- no slot98 control-plane validator changed
- no authority surface changed
- no re-dispatch is required from this drift alone

## New Base Ref If Continuing

If the repair is re-authorized after patching the prompt, use:

- new `BASE_REF`: `000caad1364e9b06c15d2f674a23dd648163206d`

## Prompt Fields To Patch Before Continuing

Patch the old repair prompt at minimum:

- replace expected `BASE_REF` / `origin/main` from `3f29fe3a1853bc6c6233a71904416349f3c98292` to `000caad1364e9b06c15d2f674a23dd648163206d`
- update the truth-gate language so `000caad...` is the expected mainline SHA
- include the already-created degraded-run note as a pre-existing artifact to preserve:
  - `/Users/wanglei/workspace/ScoutFlow-B2-repair-stageA-slot98/docs/research/repairs/b2-repair-truth-gate-failed-2026-05-05.md`
- keep `docs/research/repairs/` as a style-reference directory, but account for the new STEP2 / Wave5 files now present in that directory
- keep the original hard boundary: no historical `REPORT`, `CHECKPOINT`, or `DIFF-BUNDLE` in-place rewrite

## Not Run In This Resolution Step

Per instruction, this drift-resolution step did not run:

- `npm install`
- `npm test`
- `npm run build`
- `python -m pytest`
- repair implementation
- PR creation
