---
title: Near-term execution matrix
status: candidate / research / not-authority
execution_approval: not-approved
runtime_approval: not-approved
created_at: 2026-05-06
related_dispatch: PF-C0-06R
---

# Near-term execution matrix

## scope

- This matrix classifies all 80 authored dispatch files from `docs/research/post-frozen/80-pack-source/02_task_packs/`.
- `near_term` is intentionally capped at `21` rows, which stays inside the dispatch target range `20-30`.
- Classification principle:
  - current near-term mainline = successor entry + localhost preview chain
  - repaired R/merged forms are called out in `reason`
  - superseded rows stay visible instead of being silently dropped
  - downstream proof, RAW handoff, controlled hardening, and global support remain outside the current near-term budget

## summary

| bucket | count | note |
|---|---:|---|
| `near_term_run1` | 8 | current 8-dispatch Run-1 |
| `near_term_run2` | 13 | remaining localhost preview chain after Run-1 |
| `superseded_by_pf_meta_01` | 8 | original authored rows folded into repaired successors |
| `reservoir_after_preview_only_localhost_ready` | 12 | `PF-C1` cluster |
| `reservoir_after_c1_go_no_go` | 11 | `PF-C2` rows before true-write future gate |
| `future_true_write_overflow` | 1 | `PF-C2-12` |
| `reservoir_after_c1_c2_artifact_reality` | 6 | `PF-C3` cluster |
| `reservoir_after_localhost_proof_and_visual_gate` | 8 | `PF-C4` cluster |
| `later_authority_closeout_after_human_approval` | 1 | `PF-LP-18` |
| `permanent_overflow_support` | 12 | `PF-GLOBAL` cluster |

## matrix

| code | cluster | priority | open_after_state | status | reason |
|---|---|---|---|---|---|
| `PF-C0-01` | `PF-C0/PF-O1` | `blocker` | `live_authority_readback_after_PR194` | `near_term_run1` | in the current successor-entry/preview Run-1 chain. Active repaired form is PF-C0-01R. |
| `PF-C0-02` | `PF-C0/PF-O1` | `deprecated` | `live_authority_readback_after_PR194` | `superseded_by_pf_meta_01` | frozen boundary is now inherited from _PACK-DEFAULTS §0; no standalone dispatch is needed |
| `PF-C0-03` | `PF-C0/PF-O1` | `high` | `live_authority_readback_after_PR194` | `near_term_run1` | in the current successor-entry/preview Run-1 chain. Active repaired form is PF-C0-MERGED-03+04. |
| `PF-C0-04` | `PF-C0/PF-O1` | `deprecated` | `live_authority_readback_after_PR194` | `superseded_by_pf_meta_01` | preview-only scope merged into successor entry and preview-only scope memo |
| `PF-C0-05` | `PF-C0/PF-O1` | `deprecated` | `live_authority_readback_after_PR194` | `superseded_by_pf_meta_01` | dispatch naming reset belongs inside the successor entry memo |
| `PF-C0-06` | `PF-C0/PF-O1` | `high` | `live_authority_readback_after_PR194` | `near_term_run1` | in the current successor-entry/preview Run-1 chain. Active repaired form is PF-C0-06R. |
| `PF-C1-01` | `PF-C1` | `medium` | `preview_only_localhost_ready` | `reservoir_after_preview_only_localhost_ready` | next proof-pair cluster; kept outside the current near-term budget until localhost preview proof is real. |
| `PF-C1-02` | `PF-C1` | `medium` | `preview_only_localhost_ready` | `reservoir_after_preview_only_localhost_ready` | next proof-pair cluster; kept outside the current near-term budget until localhost preview proof is real. |
| `PF-C1-03` | `PF-C1` | `medium` | `preview_only_localhost_ready` | `reservoir_after_preview_only_localhost_ready` | next proof-pair cluster; kept outside the current near-term budget until localhost preview proof is real. |
| `PF-C1-04` | `PF-C1` | `medium` | `preview_only_localhost_ready` | `reservoir_after_preview_only_localhost_ready` | next proof-pair cluster; kept outside the current near-term budget until localhost preview proof is real. |
| `PF-C1-05` | `PF-C1` | `medium` | `preview_only_localhost_ready` | `reservoir_after_preview_only_localhost_ready` | next proof-pair cluster; kept outside the current near-term budget until localhost preview proof is real. |
| `PF-C1-06` | `PF-C1` | `medium` | `preview_only_localhost_ready` | `reservoir_after_preview_only_localhost_ready` | next proof-pair cluster; kept outside the current near-term budget until localhost preview proof is real. |
| `PF-C1-07` | `PF-C1` | `medium` | `preview_only_localhost_ready` | `reservoir_after_preview_only_localhost_ready` | next proof-pair cluster; kept outside the current near-term budget until localhost preview proof is real. |
| `PF-C1-08` | `PF-C1` | `medium` | `preview_only_localhost_ready` | `reservoir_after_preview_only_localhost_ready` | next proof-pair cluster; kept outside the current near-term budget until localhost preview proof is real. |
| `PF-C1-09` | `PF-C1` | `medium` | `preview_only_localhost_ready` | `reservoir_after_preview_only_localhost_ready` | next proof-pair cluster; kept outside the current near-term budget until localhost preview proof is real. |
| `PF-C1-10` | `PF-C1` | `medium` | `preview_only_localhost_ready` | `reservoir_after_preview_only_localhost_ready` | next proof-pair cluster; kept outside the current near-term budget until localhost preview proof is real. |
| `PF-C1-11` | `PF-C1` | `medium` | `preview_only_localhost_ready` | `reservoir_after_preview_only_localhost_ready` | next proof-pair cluster; kept outside the current near-term budget until localhost preview proof is real. |
| `PF-C1-12` | `PF-C1` | `medium` | `preview_only_localhost_ready` | `reservoir_after_preview_only_localhost_ready` | next proof-pair cluster; kept outside the current near-term budget until localhost preview proof is real. |
| `PF-C2-01` | `PF-C2` | `medium` | `c1_partial_or_pass` | `reservoir_after_c1_go_no_go` | RAW handoff cluster stays downstream of C1 usefulness/go-no-go and out of the current preview-only line. |
| `PF-C2-02` | `PF-C2` | `medium` | `c1_partial_or_pass` | `reservoir_after_c1_go_no_go` | RAW handoff cluster stays downstream of C1 usefulness/go-no-go and out of the current preview-only line. |
| `PF-C2-03` | `PF-C2` | `medium` | `c1_partial_or_pass` | `reservoir_after_c1_go_no_go` | RAW handoff cluster stays downstream of C1 usefulness/go-no-go and out of the current preview-only line. |
| `PF-C2-04` | `PF-C2` | `medium` | `c1_partial_or_pass` | `reservoir_after_c1_go_no_go` | RAW handoff cluster stays downstream of C1 usefulness/go-no-go and out of the current preview-only line. |
| `PF-C2-05` | `PF-C2` | `medium` | `c1_partial_or_pass` | `reservoir_after_c1_go_no_go` | RAW handoff cluster stays downstream of C1 usefulness/go-no-go and out of the current preview-only line. |
| `PF-C2-06` | `PF-C2` | `medium` | `c1_partial_or_pass` | `reservoir_after_c1_go_no_go` | RAW handoff cluster stays downstream of C1 usefulness/go-no-go and out of the current preview-only line. |
| `PF-C2-07` | `PF-C2` | `medium` | `c1_partial_or_pass` | `reservoir_after_c1_go_no_go` | RAW handoff cluster stays downstream of C1 usefulness/go-no-go and out of the current preview-only line. |
| `PF-C2-08` | `PF-C2` | `medium` | `c1_partial_or_pass` | `reservoir_after_c1_go_no_go` | RAW handoff cluster stays downstream of C1 usefulness/go-no-go and out of the current preview-only line. |
| `PF-C2-09` | `PF-C2` | `medium` | `c1_partial_or_pass` | `reservoir_after_c1_go_no_go` | RAW handoff cluster stays downstream of C1 usefulness/go-no-go and out of the current preview-only line. |
| `PF-C2-10` | `PF-C2` | `medium` | `c1_partial_or_pass` | `reservoir_after_c1_go_no_go` | RAW handoff cluster stays downstream of C1 usefulness/go-no-go and out of the current preview-only line. |
| `PF-C2-11` | `PF-C2` | `medium` | `c1_partial_or_pass` | `reservoir_after_c1_go_no_go` | RAW handoff cluster stays downstream of C1 usefulness/go-no-go and out of the current preview-only line. |
| `PF-C2-12` | `PF-C2` | `medium` | `c1_partial_or_pass` | `future_true_write_overflow` | explicit future true-write gate; cannot enter near-term mainline before RAW proof and human approval. |
| `PF-C3-01` | `PF-C3` | `reservoir` | `parallel_prep_after_successor_entry` | `reservoir_after_c1_c2_artifact_reality` | compression/object-control work needs real proof artifacts first; do not pre-open it from candidate docs alone. |
| `PF-C3-02` | `PF-C3` | `reservoir` | `parallel_prep_after_successor_entry` | `reservoir_after_c1_c2_artifact_reality` | compression/object-control work needs real proof artifacts first; do not pre-open it from candidate docs alone. |
| `PF-C3-03` | `PF-C3` | `reservoir` | `parallel_prep_after_successor_entry` | `reservoir_after_c1_c2_artifact_reality` | compression/object-control work needs real proof artifacts first; do not pre-open it from candidate docs alone. |
| `PF-C3-04` | `PF-C3` | `reservoir` | `parallel_prep_after_successor_entry` | `reservoir_after_c1_c2_artifact_reality` | compression/object-control work needs real proof artifacts first; do not pre-open it from candidate docs alone. |
| `PF-C3-05` | `PF-C3` | `reservoir` | `parallel_prep_after_successor_entry` | `reservoir_after_c1_c2_artifact_reality` | compression/object-control work needs real proof artifacts first; do not pre-open it from candidate docs alone. |
| `PF-C3-06` | `PF-C3` | `reservoir` | `parallel_prep_after_successor_entry` | `reservoir_after_c1_c2_artifact_reality` | compression/object-control work needs real proof artifacts first; do not pre-open it from candidate docs alone. |
| `PF-C4-01` | `PF-C4` | `reservoir` | `c1_c2_pass_or_strong_partial` | `reservoir_after_localhost_proof_and_visual_gate` | controlled hardening belongs after localhost proof and visual/human gates, not before. |
| `PF-C4-02` | `PF-C4` | `reservoir` | `c1_c2_pass_or_strong_partial` | `reservoir_after_localhost_proof_and_visual_gate` | controlled hardening belongs after localhost proof and visual/human gates, not before. |
| `PF-C4-03` | `PF-C4` | `reservoir` | `c1_c2_pass_or_strong_partial` | `reservoir_after_localhost_proof_and_visual_gate` | controlled hardening belongs after localhost proof and visual/human gates, not before. |
| `PF-C4-04` | `PF-C4` | `reservoir` | `c1_c2_pass_or_strong_partial` | `reservoir_after_localhost_proof_and_visual_gate` | controlled hardening belongs after localhost proof and visual/human gates, not before. |
| `PF-C4-05` | `PF-C4` | `reservoir` | `c1_c2_pass_or_strong_partial` | `reservoir_after_localhost_proof_and_visual_gate` | controlled hardening belongs after localhost proof and visual/human gates, not before. |
| `PF-C4-06` | `PF-C4` | `reservoir` | `c1_c2_pass_or_strong_partial` | `reservoir_after_localhost_proof_and_visual_gate` | controlled hardening belongs after localhost proof and visual/human gates, not before. |
| `PF-C4-07` | `PF-C4` | `reservoir` | `c1_c2_pass_or_strong_partial` | `reservoir_after_localhost_proof_and_visual_gate` | controlled hardening belongs after localhost proof and visual/human gates, not before. |
| `PF-C4-08` | `PF-C4` | `reservoir` | `c1_c2_pass_or_strong_partial` | `reservoir_after_localhost_proof_and_visual_gate` | controlled hardening belongs after localhost proof and visual/human gates, not before. |
| `PF-GLOBAL-01` | `PF-overflow/global-reservoir` | `permanent_overflow` | `never_auto_open` | `permanent_overflow_support` | cross-pack support or permanent overflow artifact; not part of the current 20-30 mainline budget. |
| `PF-GLOBAL-02` | `PF-overflow/global-reservoir` | `permanent_overflow` | `never_auto_open` | `permanent_overflow_support` | cross-pack support or permanent overflow artifact; not part of the current 20-30 mainline budget. |
| `PF-GLOBAL-03` | `PF-overflow/global-reservoir` | `permanent_overflow` | `never_auto_open` | `permanent_overflow_support` | cross-pack support or permanent overflow artifact; not part of the current 20-30 mainline budget. |
| `PF-GLOBAL-04` | `PF-overflow/global-reservoir` | `permanent_overflow` | `never_auto_open` | `permanent_overflow_support` | cross-pack support or permanent overflow artifact; not part of the current 20-30 mainline budget. |
| `PF-GLOBAL-05` | `PF-overflow/global-reservoir` | `permanent_overflow` | `never_auto_open` | `permanent_overflow_support` | cross-pack support or permanent overflow artifact; not part of the current 20-30 mainline budget. |
| `PF-GLOBAL-06` | `PF-overflow/global-reservoir` | `permanent_overflow` | `never_auto_open` | `permanent_overflow_support` | cross-pack support or permanent overflow artifact; not part of the current 20-30 mainline budget. |
| `PF-GLOBAL-07` | `PF-overflow/global-reservoir` | `permanent_overflow` | `never_auto_open` | `permanent_overflow_support` | cross-pack support or permanent overflow artifact; not part of the current 20-30 mainline budget. |
| `PF-GLOBAL-08` | `PF-overflow/global-reservoir` | `permanent_overflow` | `never_auto_open` | `permanent_overflow_support` | cross-pack support or permanent overflow artifact; not part of the current 20-30 mainline budget. |
| `PF-GLOBAL-09` | `PF-overflow/global-reservoir` | `permanent_overflow` | `never_auto_open` | `permanent_overflow_support` | cross-pack support or permanent overflow artifact; not part of the current 20-30 mainline budget. |
| `PF-GLOBAL-10` | `PF-overflow/global-reservoir` | `permanent_overflow` | `never_auto_open` | `permanent_overflow_support` | cross-pack support or permanent overflow artifact; not part of the current 20-30 mainline budget. |
| `PF-GLOBAL-11` | `PF-overflow/global-reservoir` | `permanent_overflow` | `never_auto_open` | `permanent_overflow_support` | cross-pack support or permanent overflow artifact; not part of the current 20-30 mainline budget. |
| `PF-GLOBAL-12` | `PF-overflow/global-reservoir` | `permanent_overflow` | `never_auto_open` | `permanent_overflow_support` | cross-pack support or permanent overflow artifact; not part of the current 20-30 mainline budget. |
| `PF-LP-01` | `PF-localhost-preview` | `blocker` | `successor_entry_ready` | `near_term_run1` | in the current successor-entry/preview Run-1 chain. |
| `PF-LP-02` | `PF-localhost-preview` | `blocker` | `successor_entry_ready` | `near_term_run1` | in the current successor-entry/preview Run-1 chain. |
| `PF-LP-03` | `PF-localhost-preview` | `high` | `successor_entry_ready` | `near_term_run1` | in the current successor-entry/preview Run-1 chain. |
| `PF-LP-04` | `PF-localhost-preview` | `blocker` | `successor_entry_ready` | `near_term_run2` | part of the remaining localhost preview chain after Run-1, still inside the 20-30 near-term budget. |
| `PF-LP-05` | `PF-localhost-preview` | `blocker` | `successor_entry_ready` | `near_term_run2` | part of the remaining localhost preview chain after Run-1, still inside the 20-30 near-term budget. |
| `PF-LP-06` | `PF-localhost-preview` | `high` | `successor_entry_ready` | `near_term_run2` | part of the remaining localhost preview chain after Run-1, still inside the 20-30 near-term budget. |
| `PF-LP-07` | `PF-localhost-preview` | `high` | `successor_entry_ready` | `near_term_run2` | part of the remaining localhost preview chain after Run-1, still inside the 20-30 near-term budget. |
| `PF-LP-08` | `PF-localhost-preview` | `high` | `successor_entry_ready` | `near_term_run2` | part of the remaining localhost preview chain after Run-1, still inside the 20-30 near-term budget. |
| `PF-LP-09` | `PF-localhost-preview` | `high` | `successor_entry_ready` | `near_term_run2` | part of the remaining localhost preview chain after Run-1, still inside the 20-30 near-term budget. |
| `PF-LP-10` | `PF-localhost-preview` | `high` | `successor_entry_ready` | `near_term_run2` | part of the remaining localhost preview chain after Run-1, still inside the 20-30 near-term budget. |
| `PF-LP-11` | `PF-localhost-preview` | `medium` | `successor_entry_ready` | `near_term_run2` | part of the remaining localhost preview chain after Run-1, still inside the 20-30 near-term budget. |
| `PF-LP-12` | `PF-localhost-preview` | `medium` | `successor_entry_ready` | `near_term_run2` | still near-term, but explicitly deferred to Run-2 until PF-LP-04 lands and the frontend chain exists. |
| `PF-LP-13` | `PF-localhost-preview` | `high` | `successor_entry_ready` | `near_term_run1` | in the current successor-entry/preview Run-1 chain. |
| `PF-LP-14` | `PF-localhost-preview` | `reservoir` | `successor_entry_ready` | `near_term_run2` | part of the remaining localhost preview chain after Run-1, still inside the 20-30 near-term budget. |
| `PF-LP-15` | `PF-localhost-preview` | `reservoir` | `successor_entry_ready` | `near_term_run2` | part of the remaining localhost preview chain after Run-1, still inside the 20-30 near-term budget. |
| `PF-LP-16` | `PF-localhost-preview` | `reservoir` | `successor_entry_ready` | `near_term_run2` | part of the remaining localhost preview chain after Run-1, still inside the 20-30 near-term budget. |
| `PF-LP-17` | `PF-localhost-preview` | `reservoir` | `successor_entry_ready` | `near_term_run2` | part of the remaining localhost preview chain after Run-1, still inside the 20-30 near-term budget. |
| `PF-LP-18` | `PF-localhost-preview` | `reservoir` | `successor_entry_ready` | `later_authority_closeout_after_human_approval` | touches authority surfaces only after preview-loop readback and explicit human approval. |
| `PF-O1-01` | `PF-C0/PF-O1` | `blocker` | `live_authority_readback_after_PR194` | `near_term_run1` | in the current successor-entry/preview Run-1 chain. Active repaired form is PF-O1-01R. |
| `PF-O1-02` | `PF-C0/PF-O1` | `deprecated` | `live_authority_readback_after_PR194` | `superseded_by_pf_meta_01` | true vault write is represented as row 1 in the overflow registry |
| `PF-O1-03` | `PF-C0/PF-O1` | `deprecated` | `live_authority_readback_after_PR194` | `superseded_by_pf_meta_01` | runtime tools are represented as row 2 in the overflow registry |
| `PF-O1-04` | `PF-C0/PF-O1` | `deprecated` | `live_authority_readback_after_PR194` | `superseded_by_pf_meta_01` | browser automation is represented as row 3 in the overflow registry |
| `PF-O1-05` | `PF-C0/PF-O1` | `deprecated` | `live_authority_readback_after_PR194` | `superseded_by_pf_meta_01` | DBvNext and migration are represented as row 4 in the overflow registry |
| `PF-O1-06` | `PF-C0/PF-O1` | `deprecated` | `live_authority_readback_after_PR194` | `superseded_by_pf_meta_01` | full Signal Workbench is represented as row 5 in the overflow registry |
