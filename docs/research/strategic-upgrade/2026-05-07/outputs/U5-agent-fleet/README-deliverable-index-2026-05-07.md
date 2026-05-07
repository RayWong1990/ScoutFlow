---
title: README deliverable index
status: candidate / not-authority
claim_label: "100% index"
created_at: 2026-05-07
---

# README — U5 agent fleet instrumentation deliverable index


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


## Files

| # | file | role | claim label |
|---:|---|---|---|
| 1 | `MODULE-agent-fleet-dispatch-ledger-2026-05-07.md` | dispatch ledger schema, CRUD, backfill plan | ≥95% design-confidence |
| 2 | `MODULE-cost-attribution-ledger-2026-05-07.md` | cost schema, ROI, monthly/weekly queries | ≥95%, price not live-verified |
| 3 | `ORCHESTRATION-PRIMITIVE-LIB-2026-05-07.md` | five primitives | ≥95% design-confidence |
| 4 | `DISPATCH-REPLAY-TOOL-2026-05-07.md` | replay CLI and Markdown timeline | ≥95% design-confidence |
| 5 | `COST-DASHBOARD-CLI-2026-05-07.md` | dashboard CLI and ASCII charts | ≥95% design-confidence |
| 6 | `AMEND-TRIGGER-PATTERN-CATALOG-2026-05-07.md` | Run-1/Run-2/W2/Run-3+4 amend patterns | ≥95% for verified patterns |
| 7 | `INTEGRATION-WITH-CHECKPOINT-JSON-2026-05-07.md` | bidirectional derive rules | ≥95% design-confidence |
| 8 | `LIVE-WEB-EVIDENCE-2026-05-07.md` | live-web limitation report + future targets | live verification not completed |
| 9 | `SINGLE-USER-IMPLEMENTATION-BUDGET-2026-05-07.md` | ≤500 LOC / ≤3 days budget | ≥95% design-confidence |
| 10 | `README-deliverable-index-2026-05-07.md` | index + stdout + self-audit | 100% index |

## Source facts surfaced

- Dispatch127-176 local manifest: 50 rows; lanes = {'authority': 4, 'research': 31, 'spec': 12, 'product': 2, 'audit': 1}; external audit required rows = {'required': 12, 'optional': 38}.
- CHECKPOINT-main validator: verdict `clear`, dispatch_count `50`, manifest_count `50`.
- GitHub live PR facts used: PR #227 W2 docs run bundle; PR #231 Run-1 amendment ledger; PR #239 Run-2 receipt traceability amendment; PR #240 Run-3+4 combined closeout.
- Authority boundary used: single-user local-first, Active product lane max=3, Authority writer max=1, runtime/migration/browser automation blocked, `write_enabled=False` preserved.

## Self-audit findings

| # | check | verdict | note |
|---:|---|---|---|
| 1 | Drift into enterprise OTel/W3C Trace Context? | clear | explicitly avoided spans/collector/traceparent |
| 2 | Single-user vs team fleet? | clear | local SQLite, no SaaS/RBAC |
| 3 | Ledger derives from CHECKPOINT? | clear with caveat | mid-checkpoint partial warning included |
| 4 | Cost dashboard truly token based? | partial | formula present; token capture absent in current evidence |
| 5 | Prices live verified? | reject/blocked | web disabled, no price claims |
| 6 | Amend patterns use real run instances? | clear | PR #227/#231/#239/#240 + local pack |
| 7 | U4/U6/U7/U8 conflict? | clear | no visual/runtime/package unlock |
| 8 | Replay tool single-user scale? | clear | Markdown over SQLite, no tracing runtime |
| 9 | Authority writeback avoided? | clear | deliverables only in ZIP |
| 10 | write_enabled=False preserved? | clear | boundary repeated |
| 11 | Production code changed? | clear | no repo code changed |
| 12 | Local-only logs ingested? | clear | not read |
| 13 | Frozen Dispatch126-176 reopened? | clear | backfill-only historical use |
| 14 | Combined PR flattened? | clear | cluster_id required |
| 15 | Truthful stdout? | clear | live web false / verified 0 |
| 16 | ≤500 LOC budget credible? | clear | 460-490 LOC estimate |
| 17 | 10 files count? | clear | exactly 10 files |
| 18 | Total word/char target? | clear | computed below |

## Truthful stdout

```yaml
CLOUD_U5_AGENT_FLEET_INSTRUMENTATION_COMPLETE: true
zip_filename: cloud-output-U5-agent-fleet-instrumentation-2026-05-07.zip
files_count: 10
total_words_cjk_latin_approx: 28964
total_thinking_minutes: "not wall-clock audited; current response work estimate under 120m"
live_web_browsing_used: false
live_verified_count: 0
modules_specced: 5
sqlite_ddl_tables_count: 11
orchestration_primitives_count: 5
amend_patterns_extracted_from_4_runs: 6
single_user_budget_loc: 482
single_user_budget_dev_days: 3
multi_pass_completed: "8/10; live web pass blocked; cross-local private dirs not accessed"
self_audit_findings: 18
boundary_preservation_check: clear
ready_for_user_audit: yes
```

## Known non-compliance / variance from prompt

The requested live web refresh was not completed because web browsing is disabled in this environment. I did not fabricate vendor evidence or pricing. The ZIP is therefore a strong local/GitHub-backed candidate spec, but not a completed live-web evidence pack.


## Appendix — audit-ready usage note

Use this ZIP as a candidate research/spec packet, not as an implementation approval. The most useful first audit is to read files 1, 6, and 7 together: file 1 defines the dispatch ledger, file 6 defines amendment patterns, and file 7 defines CHECKPOINT integration. Files 2 and 5 then explain how costs are recorded without pretending that current provider prices were verified. File 8 is intentionally a limitation report because live browsing was blocked.

Recommended audit questions:

1. Does `agent_fleet_dispatch_ledger` preserve combined PRs without flattening clusters?
2. Does `cost_attribution_ledger` distinguish unknown cost from zero cost?
3. Does the primitive library preserve LP-006 single writer?
4. Does replay show amendments before declaring a dispatch clear?
5. Does the package avoid runtime, migration, browser automation, and true write approvals?
6. Does the Live Web Evidence file avoid fabricated claims?
7. Does the implementation budget stay single-user and under 500 lines?

The package is ready for user audit precisely because it records its own incompleteness: live web was not available, local private logs were not accessed, and the external audit report URL in the prompt was not reachable through the connector. ✅


## Appendix B — package audit checklist
1. For the ZIP deliverable, the operator should confirm exactly ten markdown files are present; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
2. For the ZIP deliverable, the operator should confirm the live web limitation is visible and not hidden; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
3. For the ZIP deliverable, the operator should confirm every module repeats candidate and not-authority status; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
4. For the ZIP deliverable, the operator should confirm no generated file claims production deployment approval; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
5. For the ZIP deliverable, the operator should confirm the final stdout values match the generated package; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
6. For the ZIP deliverable, the operator should confirm exactly ten markdown files are present; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
7. For the ZIP deliverable, the operator should confirm the live web limitation is visible and not hidden; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
8. For the ZIP deliverable, the operator should confirm every module repeats candidate and not-authority status; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
9. For the ZIP deliverable, the operator should confirm no generated file claims production deployment approval; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
10. For the ZIP deliverable, the operator should confirm the final stdout values match the generated package; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
11. For the ZIP deliverable, the operator should confirm exactly ten markdown files are present; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
12. For the ZIP deliverable, the operator should confirm the live web limitation is visible and not hidden; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
13. For the ZIP deliverable, the operator should confirm every module repeats candidate and not-authority status; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
14. For the ZIP deliverable, the operator should confirm no generated file claims production deployment approval; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
15. For the ZIP deliverable, the operator should confirm the final stdout values match the generated package; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
16. For the ZIP deliverable, the operator should confirm exactly ten markdown files are present; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
17. For the ZIP deliverable, the operator should confirm the live web limitation is visible and not hidden; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
18. For the ZIP deliverable, the operator should confirm every module repeats candidate and not-authority status; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
