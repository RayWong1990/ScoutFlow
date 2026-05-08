---
title: W4 Lane 5 (full_signal_workbench) Patch — §0.5 B-lane sanity + §5.7 amend_trigger lane-specific
status: candidate / patch
authority: not-authority
created_by: gpt-pro
parent_cluster: W4
parent_lane: full_signal_workbench
created_at: 2026-05-08
upstream_finding: "audit catch — 5 lane §0.5 B-lane sanity / §5.7 amend_trigger paragraph clone, lane 5 缺 lane-specific verify"
disclaimer: 真态数字以 GitHub live main HEAD 为准; 撰写时刻数字仅为历史参考。
prerequisite_check: drift_detected
main_head_drift: "docs/current.md reports c802de4; GitHub chronological latest merge readback is 6dd27d7 / PR #245 W2D memory graph (撰写时刻历史参考, GitHub live 以 §0.5 Check 为准)"
active_product_count: "0/3 (refreshed at §0.5 Check)"
authority_writer_count: "0/1 (refreshed at §0.5 Check)"
wave_state: "WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED"
write_enabled: false
memory_batch_count: 17
deliverable_type: patch
target_replacement_section:
  - "§0.5 B-lane sanity row"
  - "§5.7 amend_and_proceed pattern"

---
# Lane 5 Patch — full_signal_workbench

> State: candidate / patch / not-authority / not runtime approval / not migration approval / not lane unlock.

## §0.5 Prerequisite Check

| Check | Live readback | Result |
|---|---|---|
| docs/current.md | reports `main = c802de4`, Active `0/3`, Authority writer `0/1`, `WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`, `write_enabled=False` | drift on main-head only; authority counts match |
| docs/task-index.md | Active table empty, Review empty, Backlog empty; product lane `0/3`, authority writer `0/1` | matches prompt authority state |
| docs/decision-log.md | current authority file reachable; tail is tool-truncated, but repo search confirms PR #246/D-017 references exist on main | partial tail visibility; no authority-count drift detected |
| docs/memory/INDEX.md | `batch_count: 17`, 7 lessons + 5 feedback + 5 patterns | matches prompt |
| GitHub commit chronological | latest returned commit is `6dd27d7` / PR #245 W2D memory graph, after PR #248 / PR #247 chronologically | drift vs current.md anchor `c802de4` |

**prerequisite_check = `drift_detected`**. Main-head truth in this packet is: docs authority anchor still says `c802de4`, while GitHub chronological latest merge is `6dd27d7` (撰写时刻历史参考, GitHub live 以 §0.5 Check 为准). This packet does not write authority and does not repair that drift; it only records it for Codex / CC0 intake.

## §0.5 B-lane sanity — lane-specific replacement

| Sanity item | Lane 5 live-specific check | Required readback before any lane work |
|---|---|---|
| Workbench status | full_signal_workbench is a candidate overflow lane; PRD-v3/SRD-v3 candidate shells and master spec inventory do not promote it to execution authority | Treat Lane 5 as future product suite, not current implementation backlog |
| Entity baseline | Prompt context names 4 entity baseline: signal / hypothesis / topic_card / capture in `services/api/scoutflow_api/models.py` or candidate entity docs; schema remains TBD | Codex must verify live entity source before using field names; no schema mutation in this patch |
| Dependency gate | Lane 5 depends on Lane 1 true vault write + Lane 2 runtime tools + Lane 4 migration all ready; Lane 3 browser automation is not dependency and is deferred | Strict dependency rule: Lane 1+2+4 all V-PASS or Lane 5 STOP |
| Current authority | full_signal_workbench remains one of 5 overflow Hold lanes | No “workbench ready/unlocked” claim; no active task row implied |
| RI/DTO risk | signal/hypothesis/topic_card/capture cross-links can collide with Trust Trace / WorkerReceipt / Bridge DTO if rushed | Require collision matrix before any implementation planning |
| Upgrade path | Master spec §16.2 path H is the legal route: upstream lanes ready + explicit user gate + separate PR + cross-vendor audit | Lane 5 cannot be started by enthusiasm or partial evidence |

### Lane 5 B-lane sanity verdict

Lane 5 is `candidate / strict_dependency_blocked / not execution approved`. The default is strict: Lane 1 + Lane 2 + Lane 4 must all have V-PASS evidence and explicit authority upgrade before Lane 5 can become implementation planning. Lenient mode (“some evidence or degraded start”) is rejected for this project because it reintroduces object expansion before proof.

### Suggested §1.4 trade-off replacement

`Lane 5 chooses strict dependency gating. It starts only after Lane 1 true_vault_write, Lane 2 runtime_tools, and Lane 4 dbvnext_migration are all V-PASS with explicit user approval and audit evidence. Lane 3 browser_automation is not a dependency and remains deferred. Starting Lane 5 with partial upstream evidence is a REGENERATE-level anti-pattern.`

## §5.7 amend_and_proceed — lane-specific replacement

### Amend trigger matrix

| Trigger | Lane-specific detection | Required action | Hard stop reason |
|---|---|---|---|
| Entity drift | signal / hypothesis / topic_card / capture fields, IDs, lifecycle, or ownership differ between candidate spec, models, and UI | STOP; produce entity drift matrix; do not normalize by prose | entity drift corrupts the workbench graph and downstream capture plan |
| Dependency drift | Lane 1, Lane 2, or Lane 4 evidence missing, partial, stale, or not explicitly user-approved | STOP; mark Lane 5 blocked; do not amend continue | strict dependency is the core safety rule |
| RI drift | cross-entity references cannot prove referential integrity, idempotency, or rollback path | STOP; route to Lane 4/dbvnext readiness | workbench graph without RI becomes KM drift |
| DTO collision | signal/hypothesis/capture DTO field collides with Trust Trace, WorkerReceipt, Bridge, or PlatformResult semantics | STOP; require contract redline review | DTO collision leaks product semantics into API receipts |
| Scope explosion | workbench tries to absorb rewrite pipeline, source adapter matrix, dispatch ledger, or visual DAM in one lane | STOP; split into sub-lanes | over-objectification before proof is a known project risk |
| Product closure confusion | engineering docs green but no end-to-end product proof for capture→process→vault loop | STOP; record product gap, not “done” | engineering closeout is not product closure |

### Amend rule

Lane 5 allows amend-and-proceed only for narrowing wording, dependency table correction, or adding a missing stop condition. It may not amend-through dependency drift, RI drift, DTO collision, or entity drift. If any dependency is partial, the only valid verdict is blocked/STOP.

### Receipt requirements

- Receipt path: `docs/research/post-frozen/W4/lane-5/receipts/<timestamp>-full-signal-workbench-dependency-or-entity-drift.md`.
- Required fields: dependency status for Lane 1/2/4, entity affected, DTO collision if any, RI proof status, product proof gap, reviewer needed.
- Forbidden fields: new migration SQL, runtime execution evidence, raw vault content, authority ledger edits, synthetic entity “truth” not tied to source.

## Self-flag

1. ⚠️ I applied strict dependency gating exactly because the prompt says Lane 5 is a priority but must not start on partial Lane 1 evidence.
2. ⚠️ The “4 entity baseline” requires live Codex verification before field-level implementation; this patch intentionally stays at drift/trigger level.
3. ⚠️ Lane 5 may become the biggest product suite; CC0 should consider splitting future workbench specs into entity graph, UI state, API contract, and vault integration sub-lanes.
