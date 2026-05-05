# B2 Repair Truth Gate Blocked After Prompt Patch - 2026-05-05

## Status

state=blocked_after_prompt_patch

This note records a truth-gate stop for the B2-REPAIR-01B follow-up. It is not authority, not a product task record, and not a replacement for the earlier truth-gate failed / resolution notes.

## Failure Marker

failure_marker=TG-2_BASE_REF_MISMATCH_EXTRA_COMMIT

The patched prompt expected:

```text
000caad1364e9b06c15d2f674a23dd648163206d
```

The fetched `origin/main` resolved to:

```text
fae0bdbbcb063f609c55f910240e397749520336
```

Because the patched prompt explicitly required stopping when extra commits appeared beyond the known drift set, no Stage A code repair, npm install, pytest run, commit, push, or PR creation was attempted.

## Baseline Context

- Original audit baseline: `3f29fe3a1853bc6c6233a71904416349f3c98292`
- Patched repair baseline requested by prompt: `000caad1364e9b06c15d2f674a23dd648163206d`
- Actual fetched `origin/main`: `fae0bdbbcb063f609c55f910240e397749520336`
- Worktree branch at stop: `codex/b2-repair-stagea-slot98-fixup`
- Worktree HEAD at stop: `000caad1364e9b06c15d2f674a23dd648163206d`

## Observed Commit Drift

Command:

```bash
git log --oneline --decorate --graph 3f29fe3a1853bc6c6233a71904416349f3c98292..origin/main
```

Observed:

```text
*   fae0bdb (HEAD -> main, origin/main, origin/HEAD) Merge pull request #118 from RayWong1990/task/step2b-handoff-package
|\
| * 1a29a1c docs: add STEP2B handoff package and close checklist
|/
* 000caad (codex/b2-repair-stagea-slot98-fixup) docs: add STEP2A evidence notes and checklist updates (#117)
* e35c878 docs: add STEP2 canonical V3 spec and checklist (#116)
```

The prompt allowed only the two known commits ending at `000caad...`. The additional merge commit `fae0bdb...` / PR #118 was outside the patched prompt's accepted commit set.

## Observed Path Drift

Command:

```bash
git diff --name-status \
  3f29fe3a1853bc6c6233a71904416349f3c98292..origin/main \
  -- apps/capture-station \
     tools/check-docs-redlines.py \
     AGENTS.md \
     docs/current.md \
     docs/task-index.md \
     docs/specs/contracts-index.md \
     docs/research/repairs \
     services/api/scoutflow_api/main.py
```

Observed changed paths were still limited to `docs/research/repairs/**`:

```text
A	docs/research/repairs/backbone-taxonomy-2026-05-05.md
A	docs/research/repairs/batch2-audit-summary-2026-05-05.md
A	docs/research/repairs/cloud-input-package-inventory-2026-05-05.md
A	docs/research/repairs/dispatch127-176-pack-design-v3-2026-05-05.md
A	docs/research/repairs/readback-manifest-2026-05-05.md
A	docs/research/repairs/step2-local-mode-and-packlint-surface-2026-05-05.md
A	docs/research/repairs/step2-prep-checklist-2026-05-05.md
A	docs/research/repairs/step2-runner-api-disk-budget-2026-05-05.md
A	docs/research/repairs/step2-runtime-readiness-and-screenshot-note-2026-05-05.md
A	docs/research/repairs/step3-handoff-packet-2026-05-05.md
A	docs/research/repairs/wave5-scope-and-template-extraction-2026-05-05.md
```

No drift was observed in:

- `apps/capture-station/**`
- `tools/check-docs-redlines.py`
- `AGENTS.md`
- `docs/current.md`
- `docs/task-index.md`
- `docs/specs/contracts-index.md`
- `services/api/scoutflow_api/main.py`

That path evidence suggests the new drift is likely docs/research-only, but the commit set no longer matches the patched prompt. This run therefore stops for re-authorization rather than inferring permission to continue.

## Worktree State At Stop

Command:

```bash
git status --short
git rev-parse HEAD
git rev-parse --abbrev-ref HEAD
```

Observed before writing this note:

```text
?? docs/research/repairs/b2-repair-truth-gate-failed-2026-05-05.md
?? docs/research/repairs/b2-repair-truth-gate-resolution-2026-05-05.md
000caad1364e9b06c15d2f674a23dd648163206d
codex/b2-repair-stagea-slot98-fixup
```

The two earlier truth-gate notes were preserved. This blocked note is the only new file written in response to the failed patched truth gate.

## Actions Not Taken

- Did not edit `apps/capture-station/**`.
- Did not edit `tools/check-docs-redlines.py`.
- Did not edit authority files.
- Did not run `npm install`, `npm test`, or `npm run build`.
- Did not run pytest.
- Did not write the Stage A repair evidence note.
- Did not write the RAW sibling FIXUP.
- Did not commit, push, or create a PR.

## Required Next Input

A new prompt patch is required if this repair should continue from `fae0bdbbcb063f609c55f910240e397749520336`, or from a later `origin/main` SHA after a fresh bounded drift analysis.
