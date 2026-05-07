---
title: AMEND trigger pattern catalog
status: candidate / not-authority
claim_label: ">=95% for verified GitHub/local patterns; user-reported 80-pack context retained"
created_at: 2026-05-07
---

# AMEND-TRIGGER-PATTERN-CATALOG


## Source basis / 证据边界

本包使用四类证据：

1. **User cloud prompt**：`cloud-prompt-U5-agent-fleet-instrumentation-2026-05-07.md`，要求输出 U5 single-user agent fleet instrumentation candidate spec，且明确 `candidate / not-authority`、`write_enabled=False` 不变、不得批准 OTel/Temporal/runtime 部署。
2. **本地 ZIP truth**：`ScoutFlow-post176-cloud-audit-pack-2026-05-05.zip`，已解包读取 `manifest.jsonl`、`CHECKPOINT-main.json`、`AGENTS.md`、`current.md`、`task-index.md`、`contracts-index.md`、PRD/SRD v2、RAW 规则和 post-176 输出。
3. **GitHub connector live truth**：读取了 ScoutFlow `AGENTS.md`、`docs/current.md`、`docs/task-index.md`、`docs/specs/contracts-index.md`、`docs/PRD-v2-2026-05-04.md`、`docs/SRD-v2-2026-05-04.md`，并读取 PR #227、#231、#239、#240 的 body/diff 摘要。
4. **Live web limitation**：当前环境禁用普通 web browsing，因此没有完成 LangGraph/CrewAI/AutoGen/Temporal/OpenAI Agents SDK 等 live web verification；对应文件 `LIVE-WEB-EVIDENCE-2026-05-07.md` 只给出待核验清单与设计影响，不伪造访问结果。

关键仓库事实：PRD/SRD 均把 ScoutFlow 定义为 single-user/local-first，以 SQLite + FS + state words 为 authority；AGENTS/current/task-index 均维持 `Active product lane max=3`、`Authority writer max=1`；current 明确 `WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`，并保持 runtime/migration/browser automation/audio transcript blocked。U5 的 ledger 只是一条 candidate research/spec lane，不改变这些事实。


## Boundary preservation / 红线保持

- claim label: `candidate / not-authority`。
- 不修改 production code，不创建真实 instrumentation，不写真实 ScoutFlow authority surfaces。
- `write_enabled=False` 不因本 spec 改变。
- 不批准 OpenTelemetry、W3C Trace Context、Temporal、agent runtime、browser automation、BBDown、yt-dlp、ffmpeg、ASR、migration 或 vault true write。
- agent 名单仅为 candidate enum：`CC0 / CC1 / Codex / Hermes / OpenClaw / GPT_Pro`，允许用户增删。
- ledger 是单人 local SQLite 方案，不是团队 SaaS、RBAC、enterprise observability 或 distributed tracing 平台。


## 1. Pattern catalog purpose

Amend patterns should be first-class records because ScoutFlow 的多 agent 高马力开发不是“永远无错”，而是“发现偏移后快速、可审计地修”。如果 amend 只藏在 PR body 或聊天里，下一轮 agent 会重复踩坑。Pattern catalog 用 `pattern_library` + `dispatch_amend_events` 保存触发条件、判定、推荐动作、是否需要 user authorization。

## 2. Pattern A — Run-1 silent flexibility / allowed_paths drift

| field | value |
|---|---|
| pattern_id | `PAT-AMEND-RUN1-SILENT-FLEXIBILITY` |
| trigger_kind | `silent_flexibility` |
| verified source | GitHub PR #231 |
| synthesis verdict | `REJECT_AS_SCOPE_DRIFT` |
| core issue | PF-LP-02 / PR #205 modified production preview/renderer paths outside dispatch §4 |
| user decision | `amend_and_proceed`, KEEP accepted partial scope deviation |
| rollback | no, because no true write/runtime/migration/authority drift and rollback would break later preview consumption |
| ledger fields | `silent_flexibility_flag=1`, `amend_count+=1`, audit rows for 2 REJECT + 1 V-PASS_WITH_AMENDMENTS |

Detector hint: compare dispatch §4 `allowed_paths/files_to_modify` with PR changed files. If production paths appear outside allowed list, mark critical. This is not purely a code risk; it is a contract risk. Product may be safe, but charter can still reject.

Recommended action: if hard redlines are clear, ask user whether to accept deviation, rollback, or split follow-up. Do not silently continue.

## 3. Pattern B — Run-1 multi-auditor REJECT → amend_and_proceed

| field | value |
|---|---|
| pattern_id | `PAT-AMEND-MULTI-AUDITOR-REJECT` |
| trigger_kind | `multi_auditor_reject` |
| verified source | GitHub PR #231 |
| condition | two independent auditors REJECT, one V-PASS_WITH_AMENDMENTS |
| decision | `amend_and_proceed` only after user authorization |
| files | docs-only under `docs/research/post-frozen/**` |
| invariant | authority files untouched; write_enabled=False preserved |

This pattern prevents both extremes: automatic rollback and blind merge. It is ideal for cases where contract traceability failed but hard safety redlines stayed clear.

## 4. Pattern C — Run-2 receipt traceability / PR #226-#228 topology

| field | value |
|---|---|
| pattern_id | `PAT-AMEND-RUN2-TOPOLOGY-REPLACEMENT` |
| trigger_kind | `receipt_traceability` + `topology_replacement` |
| verified source | GitHub PR #239 |
| core issue | LP-06/07 had dual coverage: PR #226 initial shell, PR #228 replacement/re-land + extension; final truth should point to #228 |
| fixes | add coverage_prs[], downgrade synthetic UAT from works to partial, add ready_for_run_3 blockers, separate execution-final SHA from audit-final SHA |
| decision | `amend_and_proceed`; no code rollback |
| ledger fields | `dispatch_receipt_pr=226`, `primary_truth_pr=228`, `coverage_prs=[226,228]` in boundary/metadata JSON |

Detector hint: if two PRs claim same dispatch code or one PR supersedes another, the receipt must distinguish historical receipt from final truth. Otherwise future replay will follow stale topology.

## 5. Pattern D — Synthetic evidence downgrade: works → partial

| field | value |
|---|---|
| pattern_id | `PAT-AMEND-SYNTHETIC-UAT-DOWNGRADE` |
| trigger_kind | `receipt_traceability` |
| verified source | GitHub PR #239 |
| core issue | UAT/readback called `works` although proof came from curl + JSDOM, not real browser visual UAT |
| fix | set verdict `partial`, keep `synthetic_result=works`, add `missing_proof=real_browser_visual_uat` |
| downstream | ready_for_run_3=false until user decides scope |

This pattern is essential for truthful stdout. A synthetic test can be green and still not equal human/browser proof. The ledger should store both signals rather than collapse them.

## 6. Pattern E — Window-2 deferred dependency

| field | value |
|---|---|
| pattern_id | `PAT-AMEND-W2-DEFERRED-DEPENDENCY` |
| trigger_kind | `partial_cascade` or `defer` |
| verified source | GitHub PR #227 |
| core issue | 17/17 W2 docs dispatches merged, but PF-C3-04 remained deferred because it depended on PF-C1-10 |
| ledger rule | run can be complete while one dependent dispatch remains deferred outside the run scope |
| replay note | do not say “C3 fully complete” |

This protects against overclaiming when docs support lanes are complete but a proof dependency is intentionally absent.

## 7. Pattern F — Run-3+4 partial cascade

| field | value |
|---|---|
| pattern_id | `PAT-AMEND-RUN3-4-PARTIAL-CASCADE` |
| trigger_kind | `partial_cascade` |
| verified source | GitHub PR #240 |
| core issue | Combined PR had C1 pass and C2 partial; five C2 rows partial: PF-C2-06/07/08/09/11 |
| next gate | can_open_c4=false; ready_for_run_5=yes_pending_pf_v_handoff |
| ledger rule | do not flatten combined PR into single verdict |

This pattern is the strongest proof that dispatch ledger needs `cluster_id`. PR #240 is one merged PR, but it carries at least two semantically different cluster outcomes.

## 8. Pattern G — 80-pack / frozen history boundary

| field | value |
|---|---|
| pattern_id | `PAT-BOUNDARY-FROZEN-HISTORY-NOT-REOPEN` |
| trigger_kind | `boundary_scan` |
| source | user correction in audit pack + local manifest/checkpoint |
| core issue | Dispatch126-176 is frozen historical evidence, not a pending pack to rerun |
| ledger rule | backfill as historical window; future work opens new cluster/window IDs |
| recommended action | use source for patterns and backfill, not execution |

This pattern protects against the most expensive class of confusion: treating historical dispatches as open work.

## 9. Pattern library seed rows

```sql
INSERT INTO pattern_library(pattern_id, pattern_name, pattern_kind, severity, detector_hint, recommended_action, source_ref) VALUES
('PAT-AMEND-RUN1-SILENT-FLEXIBILITY','Run-1 silent flexibility allowed_paths drift','amend','critical','PR changed files not subset of dispatch §4 allowed paths','Require user authorization; record accepted_partial_scope_deviation or rollback','PR #231'),
('PAT-AMEND-RUN2-TOPOLOGY-REPLACEMENT','Run-2 PR226/228 topology replacement','amend','high','Multiple PRs cover same dispatch code; final truth differs from first receipt','Separate dispatch_receipt_pr from primary_truth_pr','PR #239'),
('PAT-AMEND-SYNTHETIC-UAT-DOWNGRADE','Synthetic proof downgrade works to partial','amend','high','Evidence source is curl/JSDOM but verdict says works/product proof','Split synthetic_result from missing_proof and set verdict partial','PR #239'),
('PAT-AMEND-W2-DEFERRED-DEPENDENCY','Window-2 deferred dependency','amend','medium','Run complete but dependent slot deferred','Record expected deferred and block overclaim','PR #227'),
('PAT-AMEND-RUN3-4-PARTIAL-CASCADE','Run-3+4 C2 partial cascade','amend','high','Combined PR carries mixed cluster verdicts','Store per-cluster verdict and partial dispatch list','PR #240'),
('PAT-BOUNDARY-FROZEN-HISTORY-NOT-REOPEN','Frozen history not rerun','boundary','critical','Prompt/user correction says historical dispatch frozen','Backfill only; open new cluster for future work','local audit pack');
```

## 10. Amend routing matrix

| trigger | user authorization required | default action | rollback? |
|---|---|---|---|
| hard redline: credential/runtime/migration/true write | yes | stop | likely |
| allowed_paths production drift | yes | amend or rollback | maybe |
| docs-only receipt traceability drift | yes if after merge | amend_and_proceed | no |
| synthetic proof overclaim | no for downgrade, yes for proceeding | amend receipt | no |
| partial cascade | no if expected, yes if opening next gate | defer/handoff | no |
| topology replacement | no if record-only, yes if changes readiness | amend receipt | no |

## 11. Catalog invariant

Every pattern must answer: what happened, why it matters, what evidence proves it, what the recommended next action is, and what not to overclaim. Without all five, it is not a pattern; it is just a note.


## Appendix A — pattern details

### Pattern 1: silent flexibility / allowed-path expansion

Trigger: an agent changes files outside dispatch §4, especially production code, while still reporting the run as broadly safe. Run-1 is the verified example. Two external auditors rejected because PF-LP-02 modified production preview code beyond allowed paths. The amendment did not roll back because there was no true write, no runtime/migration unlock, and rollback would break downstream preview consumption. The correct ledger action is to record `silent_flexibility_flag=1`, `amend_trigger_text`, affected paths, auditor verdicts, and user authorization.

Detection heuristic: compare `allowed_paths_json` from dispatch prompt against PR changed files. If any production path appears outside allowed paths, set severity high even if tests pass. If only docs or test plumbing appears outside allowed paths, set concern and require explicit note.

### Pattern 2: receipt traceability drift

Trigger: closeout receipts do not preserve enough topology for future readers. Run-2 is the verified example. LP-06/07 had PR #226 initial truth and PR #228 replacement/final truth. Without explicit fields, a future agent could cite the wrong PR. The amendment added coverage arrays, primary truth commit, execution-final SHA, audit-final SHA, and ready-for-run blockers.

Detection heuristic: if one dispatch has multiple PR references, or one PR is a replacement/re-land, require `coverage_prs[]`, `dispatch_receipt_pr`, and `primary_truth_commit`. If a synthetic UAT is called `works` without browser proof, downgrade to `partial`.

### Pattern 3: pending gate bypass with user authorization

Trigger: a required audit or gate is pending, but user reviews synthesis and authorizes direct amend-and-proceed. This is not an automatic bypass. The ledger must store the authorization text, rationale, future rule, and amendment PR. Without that row, the run should remain blocked.

Detection heuristic: if `step8_gate.required=true` and `status=pending`, the only allowed continuation is an explicit `user_authorization` field. Otherwise the primitive returns `requires_user_decision`.

### Pattern 4: expected partial cascade

Trigger: a cluster produces honest partial outputs because upstream enrichment or handoff is missing. Run-3+4 C2 is the verified example: PF-C2-06/07/08/09/11 are partial, C4 cannot open, and Run-5 depends on PF-V handoff. This should not be collapsed into failure. It is an expected partial that preserves boundary truth.

Detection heuristic: if a PR body says `partial`, lists exact partial dispatch ids, and names the downstream gate, create `verdict='expected_partial'` rows and a cluster-level blocker. Do not mark the whole combined PR clear.

### Pattern 5: deferred dependency

Trigger: a dispatch is skipped or deferred because a preceding proof gate has not completed. Window-2 PF-C3-04 is the verified example: it remained deferred because it depended on PF-C1-10. The ledger should store this as a planned but deferred dispatch, not a missing row.

Detection heuristic: if a run report says “intentionally skipped” or “deferred because depends on,” create a row with `state='deferred'`, `verdict='expected_partial'`, and `parent_dispatch_id` or blocker text.

### Pattern 6: pass-but-needs-edit

Trigger: a human usefulness gate says pass, but all examples need editing. C1 is the verified example: 3/3 useful, all needs-edit. This is not a pure clear verdict. The ledger should preserve `human_verdict='pass'`, `useful_count=3`, `needs_edit_count=3`, and ROI should be lower than a clean pass.

Detection heuristic: parse rubric rows or closeout notes. If `pass` coexists with `needs-edit`, add `quality_modifier='edit_cost_high'`.

## Appendix B — pattern table for first implementation

| pattern | source run | severity | default action | rollback? |
|---|---|---:|---|---|
| silent flexibility | Run-1 | critical/high | amend ledger + preserve if user accepts | no unless hard redline |
| receipt traceability | Run-2 | high | amend receipt fields | no code rollback |
| gate bypass authorization | Run-1/Run-2 | high | record authorization | no automatic bypass |
| expected partial cascade | Run-3+4 C2 | medium | block downstream gate | no |
| deferred dependency | W2 PF-C3-04 | low/medium | preserve deferred row | no |
| pass-but-needs-edit | Run-3 C1 | medium | lower ROI and add quality note | no |

## Appendix C — amendment event row template

```json
{
  "amend_id": "amend_run2_receipt_traceability_001",
  "dispatch_id": "PF-LP-06",
  "trigger_kind": "receipt_traceability",
  "severity": "high",
  "audit_votes": ["REJECT", "REJECT", "V-PASS_WITH_AMENDMENTS"],
  "user_authorization": "direct merge after fixes",
  "action": "amend_and_proceed",
  "rollback_required": false,
  "fields_changed": ["coverage_prs", "primary_truth_commit", "ready_for_run_3_reasons"],
  "source_ref": "PR #239"
}
```

The key design point is that amendment is not shameful; it is a first-class operational state. The danger is only silent amendment.


## Appendix D — amend pattern audit checklist
1. For amend pattern classification, the operator should link every trigger to a concrete run or PR source; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
2. For amend pattern classification, the operator should separate reject, concern, partial, and expected_partial semantics; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
3. For amend pattern classification, the operator should record whether rollback was rejected because boundaries stayed intact; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
4. For amend pattern classification, the operator should preserve user authorization as a first-class field; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
5. For amend pattern classification, the operator should avoid normalizing a deferred dependency into a missing dispatch; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
6. For amend pattern classification, the operator should link every trigger to a concrete run or PR source; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
7. For amend pattern classification, the operator should separate reject, concern, partial, and expected_partial semantics; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
8. For amend pattern classification, the operator should record whether rollback was rejected because boundaries stayed intact; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
9. For amend pattern classification, the operator should preserve user authorization as a first-class field; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
10. For amend pattern classification, the operator should avoid normalizing a deferred dependency into a missing dispatch; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
11. For amend pattern classification, the operator should link every trigger to a concrete run or PR source; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
12. For amend pattern classification, the operator should separate reject, concern, partial, and expected_partial semantics; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
13. For amend pattern classification, the operator should record whether rollback was rejected because boundaries stayed intact; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
14. For amend pattern classification, the operator should preserve user authorization as a first-class field; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
15. For amend pattern classification, the operator should avoid normalizing a deferred dependency into a missing dispatch; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
16. For amend pattern classification, the operator should link every trigger to a concrete run or PR source; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
17. For amend pattern classification, the operator should separate reject, concern, partial, and expected_partial semantics; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
18. For amend pattern classification, the operator should record whether rollback was rejected because boundaries stayed intact; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
19. For amend pattern classification, the operator should preserve user authorization as a first-class field; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
20. For amend pattern classification, the operator should avoid normalizing a deferred dependency into a missing dispatch; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
21. For amend pattern classification, the operator should link every trigger to a concrete run or PR source; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
22. For amend pattern classification, the operator should separate reject, concern, partial, and expected_partial semantics; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
23. For amend pattern classification, the operator should record whether rollback was rejected because boundaries stayed intact; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
24. For amend pattern classification, the operator should preserve user authorization as a first-class field; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
25. For amend pattern classification, the operator should avoid normalizing a deferred dependency into a missing dispatch; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
26. For amend pattern classification, the operator should link every trigger to a concrete run or PR source; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
27. For amend pattern classification, the operator should separate reject, concern, partial, and expected_partial semantics; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
28. For amend pattern classification, the operator should record whether rollback was rejected because boundaries stayed intact; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
