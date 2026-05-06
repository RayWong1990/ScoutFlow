# Run-1 Truth Conflict

status: resolved_for_run1_continue / LP-12_deferred_to_Run-2

## source_boundary

- This note records a cold-start truth conflict for `Run-1` before any stage PR was opened.
- Truth sources used here:
  - `docs/current.md`
  - dispatch files under `docs/research/post-frozen/80-pack-source/02_task_packs/**/dispatches/`
  - current repo code in `services/api/scoutflow_api/main.py`
  - current repo code in `apps/capture-station/src/lib/api-client.ts`

## conflict_table

| item | prompt_or_dispatch_claim | live_truth | evidence_path | verdict |
|---|---|---|---|---|
| `PF-LP-12` stage placement | commander prompt puts `PF-LP-12` in Stage 1 with `依赖 = none` | dispatch file says `depends: PF-LP-01, PF-LP-04` | `docs/research/post-frozen/80-pack-source/02_task_packs/PF-localhost-preview-pack/dispatches/PF-LP-12-localhost-dev-run-instructions.md` | `conflict` |
| `PF-LP-01` dependency status | Stage 1 would require `PF-LP-01` already satisfied if `PF-LP-12` is runnable there | current `main.py` still only mounts `captures_router` and `jobs_router`; `bridge_router` is not mounted | `services/api/scoutflow_api/main.py` | `conflict` |
| `PF-LP-04` dependency status | `PF-LP-12` also depends on `PF-LP-04` | current API client exposes bridge read methods only; no `createCapture(canonicalUrl)` helper exists | `apps/capture-station/src/lib/api-client.ts` | `conflict` |
| Run-1 scope completeness | Run-1 scope includes `PF-LP-12` but does not include `PF-LP-04` | dispatch dependency graph therefore cannot be satisfied inside the declared 9-dispatch run as written | prompt stage table plus `PF-LP-04` dispatch | `conflict` |

## execution_impact

- `PF-LP-03` remains runnable after `PF-O1-01R`.
- `PF-LP-12` is not runnable at Stage 1 under dispatch truth.
- To make `PF-LP-12` runnable, one of these must be clarified by user:
  - remove `PF-LP-12` from Run-1;
  - move `PF-LP-12` after `PF-LP-01` and explicitly accept that `PF-LP-04` is out-of-run but already waived or separately satisfied;
  - add `PF-LP-04` into Run-1 and re-stage the pack.

## resolution

- user clarification: stage table is advisory, dispatch §3 dependencies are authoritative
- resolution applied on 2026-05-06:
  - `PF-LP-12` removed from Run-1
  - `PF-LP-12` deferred to Run-2 after `PF-LP-04` lands
  - Run-1 continues with 8 dispatches: `PF-C0-01R`, `PF-O1-01R`, `PF-LP-03`, `PF-C0-MERGED-03+04`, `PF-C0-06R`, `PF-LP-01`, `PF-LP-02`, `PF-LP-13`
- conflict remains historically true, but is no longer a Run-1 stop condition after user rescoping

## stop_verdict

- initial_verdict: `blocked_on_truth_conflict`
- current_verdict: `resolved_for_run1_continue`
- reason: user explicitly re-scoped Run-1 and removed the conflicting dispatch
- baseline_origin_main: `82481b197eaa420744af90427b07a5ad670d3d96`
- prs_opened: `0`
- prs_merged: `0`
