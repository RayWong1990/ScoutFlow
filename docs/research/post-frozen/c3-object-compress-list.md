---
title: C3 object compress list
status: candidate / research / not-authority
created_at: 2026-05-06
related_dispatch: PF-C3-03
---

# C3 object compress list

## scope

- This list marks which `131-144` objects should survive only as appendix, matrix row, or overflow reference.
- Compression is not deletion. It removes standalone object pressure while retaining useful evidence.

## compress_targets

| object | source_task | current_problem | compress_to | keep_boundary |
|---|---|---|---|---|
| `hypothesis_comparison_ux` | `T-P1A-133` | reads like a separate product lane | appendix under topic-card-lite | no separate execution claim |
| `visual_reporting_candidate` | `T-P1A-135` | proof packaging and product surface are mixed | one section inside proof packet | no visual terminal verdict |
| `step3_commander_prompt_note` | `T-P1A-137` | process note occupies object slot | supporting prompt appendix | no authority or mainline gate |
| `cloud_resume_rules` | `T-P1A-138` | handoff note competes with core surfaces | packaging appendix | cloud prompt remains helper only |
| `vault_dry_run_continuation` | `T-P1A-143` | dry-run looks equal to preview proof | subsection inside preview contract | dry-run is not true write |
| `five_gate_ci_note` | `T-P1A-144` | blocked automation reads like proof | future gate row in overflow map | no browser automation approval |

## compress_by_theme

| theme | rows | action |
|---|---|---|
| `scoring_and_explanation` | `T-P1A-133` | collapse into one appendix near topic-card-lite |
| `process_and_handoff` | `T-P1A-137` + `T-P1A-138` | move to runbook / prompt support area |
| `preview_support` | `T-P1A-135` + `T-P1A-143` + `T-P1A-144` | keep as support notes, not peer-level objects |

## verdict

- Compression should happen before any new object naming round.
- `T-PASS` here only confirms a compression map exists and blocked claims stay blocked.
