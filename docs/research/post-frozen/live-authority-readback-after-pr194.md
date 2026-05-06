---
title: Live authority readback after PR194
status: candidate / research / not-authority
execution_approval: not-approved
runtime_approval: not-approved
created_at: 2026-05-06
related_dispatch: PF-C0-01R
---

# Live authority readback after PR194

## source_boundary

- This note is a post-frozen readback for successor-entry work only.
- Dispatch126-176 remain frozen historical assets/evidence; they are not reopened, reordered, or re-executed here.
- Truth classes are intentionally separated:
  - zip-derived input truth
  - PR192-era candidate readback
  - PR193/PR194 merged GitHub fact
  - current repo seam truth on `origin/main`

## live_truth_table

| claim | source_class | evidence_path_or_sha | verdict |
|---|---|---|---|
| Uploaded post-frozen corpus exists as an 80-dispatch candidate pack and is input material, not authority. | zip_derived_input | `docs/research/post-frozen/80-pack-source/` + `docs/research/post-frozen/claude-deep-review-2026-05-06.md` | `candidate_input_only` |
| PR192 landed the STEP3 cold-start handoff packet contract, but it is historical candidate/handoff truth, not the current execution gate by itself. | PR192_era_readback | PR `#192` merge `0eb29eb39eea8b13403d8008932f348b5e6acd9b` + `docs/task-index.md` row `T-P1A-155` | `historical_candidate_truth` |
| PR193 already closed Batch ABC authority sync, so pre-PR193 readbacks that still treat earlier batch state as current are superseded. | live_github_fact | PR `#193` merge `4d35e643f528ac7b7b37847111c8eefd8753766f` + `docs/current.md` current Wave 6 state | `authority_supersedes_old_readback` |
| PR194 added STEP0 authoring templates as reference surfaces for successor work; they are authoring aids, not execution approval, runtime approval, or mainline proof. | live_github_fact | PR `#194` merge `b260d13a1d8b67f66207223a4f90918059570a60` + `docs/research/web-gpt-step0/**` | `reference_only_not_execution_gate` |
| Current localhost code seams still match a successor-entry posture: `create_app()` does not mount `bridge_router`; bridge modules/config/spec exist; H5 API client exposes bridge reads but not `createCapture`; write stays disabled. | live_repo_code | `services/api/scoutflow_api/main.py`, `services/api/scoutflow_api/bridge/config.py`, `services/api/scoutflow_api/bridge/router.py`, `apps/capture-station/src/lib/api-client.ts` | `successor_entry_ready` |

## conflict_verdict

- Current live truth supports the successor path `PF-C0/O1 -> PF-LP -> PF-C1 -> PF-C2 -> PF-C4`, not automatic `Dispatch177+` continuation.
- PR193/PR194 are the live GitHub boundary that newer successor work must read from before drafting next mainline tasks.
- The current localhost seam is still preview-only and write-disabled:
  - `services/api/scoutflow_api/main.py` has not yet mounted `bridge_router`
  - `services/api/scoutflow_api/bridge/config.py` keeps `write_enabled=False`
  - `apps/capture-station/src/lib/api-client.ts` still lacks `createCapture(canonicalUrl)`
- Result: successor-entry docs can proceed; code-bearing localhost preview work still needs explicit PF-LP execution to turn seams into reachable routes and a usable preview loop.
