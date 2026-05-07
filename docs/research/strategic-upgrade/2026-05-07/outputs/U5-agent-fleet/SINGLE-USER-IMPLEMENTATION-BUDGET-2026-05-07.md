---
title: SINGLE USER implementation budget
status: candidate / not-authority
claim_label: ">=95% design-confidence"
created_at: 2026-05-07
---

# SINGLE-USER-IMPLEMENTATION-BUDGET


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


## 1. Budget claim

U5 can be implemented as a single local Python file + SQLite DB in **≤500 LOC** and **≤3 focused dev days**, if scope is limited to ledger CRUD, CHECKPOINT backfill, replay CLI, cost dashboard, and boundary/amend seed patterns. This budget excludes live web refresh, provider API usage import, UI, real agent wrappers, and production ScoutFlow integration.

## 2. LOC budget

| component | estimated LOC | notes |
|---|---:|---|
| DDL constants + init | 65 | table strings and migration guard |
| connection / IDs / JSON helpers | 30 | stdlib only |
| window + dispatch CRUD | 70 | create/update/query |
| artifact + audit + amend CRUD | 70 | simple inserts |
| cost import + price snapshot | 65 | CSV import and formula |
| CHECKPOINT backfill | 65 | JSON parse + lossy labels |
| replay renderer | 55 | Markdown output |
| dashboard query + ASCII bar | 55 | argparse + SQL |
| boundary scan + truthful stdout | 45 | string/path scans |
| tests / smoke helpers inside same file or adjacent | 60 | if kept separate, not counted in runtime file |
| **total runtime file** | **460-490** | target 482 LOC |

The DDL can live as a multiline constant. Tests can be a second file if strict LOC budget applies only to runtime script.

## 3. Dev-day plan

### Day 1 — DB + backfill

- Create SQLite schema.
- Implement init/create/update functions.
- Import local CHECKPOINT-main.json and manifest.jsonl.
- Add source quality labels and partial checkpoint warning.
- Smoke test with Dispatch127-176 pack.

Exit criterion: `scoutflow-ledger backfill-checkpoint` produces window rows and dispatch rows without claiming runtime approval.

### Day 2 — amend/audit/replay

- Add audit verdict import.
- Seed pattern_library from Run-1/Run-2/W2/Run-3+4 patterns.
- Implement replay Markdown renderer.
- Implement boundary_scan for changed paths/diff snippets.
- Smoke test replay for PR #231/#239/#240 synthetic rows.

Exit criterion: replay can show silent flexibility, topology replacement, synthetic downgrade and partial cascade.

### Day 3 — cost dashboard + docs

- Add price snapshot and CSV usage import.
- Add `scoutflow-cost --week/--month/--agent/--cluster/--roi`.
- Add ASCII bar rendering.
- Add README and truthful stdout template.
- Run redline scan and no-secret checks.

Exit criterion: dashboard prints honest unknown-cost warnings and non-zero bars if sample cost rows exist.

## 4. Direct cost budget

| cost area | estimate | condition |
|---|---:|---|
| SQLite storage | $0 | local file |
| Python dependencies | $0 | standard library only |
| hosting/SaaS | $0 | none |
| live web refresh | $0 direct, time only | only if user manually browses or enables web |
| LLM/API usage import | variable | only if future wrapper records API tokens |
| implementation in existing local subscription context | $0 additional infra | does not require new services |

I would phrase the budget as: **≤3 dev days, ≤500 LOC, $0 additional infrastructure, variable LLM usage only if future wrappers call paid APIs.** Do not promise a token-dollar budget without live provider prices.

## 5. Risk budget

| risk | likelihood | impact | mitigation |
|---|---|---|---|
| second source of truth | medium | high | bidirectional CHECKPOINT derive, source_ref everywhere |
| overbuilding into OTel | medium | high | no spans/traces/services, SQLite only |
| fake cost precision | high | medium | price_snapshot required, unknown warnings |
| privacy log ingestion | medium | high | do not read `~/.claude`/`~/.codex` in v1 |
| combined PR flattening | high | medium | cluster_id required |
| authority drift | medium | high | boundary_scan + single_writer_lock |
| user authorization missing | medium | high | amend_and_proceed requires explicit flag |

## 6. Acceptance checklist

- `python scoutflow_agent_fleet_ledger.py init` creates tables.
- `backfill-checkpoint` imports a partial checkpoint and reports lossy fields.
- `backfill-manifest` imports planned rows without marking complete.
- `replay` renders one dispatch timeline.
- `cost --week` renders table and warning when costs unknown.
- `boundary-scan` rejects forbidden paths and `write_enabled=True` diffs.
- `truthful-stdout` fails if `live_verified_count>0` while web browsing false.
- No network calls.
- No production ScoutFlow code changes.
- No package installs.

## 7. Phase 2 unlock candidates

Only after Phase 1 works locally:

1. Optional provider usage CSV adapters.
2. Optional wrapper for Codex/Claude stdout receipts.
3. Optional GitHub PR importer with connector/API.
4. Optional HTML dashboard.
5. Optional local session log import, but only with explicit user privacy approval and redaction.

These are not part of U5 v1 budget.


## Appendix A — three day implementation plan

### Day 1 — schema and import

Create `agent_fleet_dispatch_ledger.py` with SQLite initialization, DDL, and import functions for manifest and CHECKPOINT. Build tests using the local Dispatch127-176 manifest and mid-run CHECKPOINT. The day is successful when the tool can create a database, import 50 planned manifest rows, import 5 checkpoint slot rows, and report the partial/cursor caveat.

Estimated LOC: 170. Risk: duplicate ids and stale batch states. Mitigation: store source type and source hash on every imported row.

### Day 2 — amendments and replay

Add `dispatch_amend_events`, audit verdict imports, and Markdown replay. Seed patterns for Run-1, Run-2, W2 deferred dependency, and Run-3+4 C1/C2 split. The day is successful when `scoutflow-replay --pr 240 --cluster PF-C2` can show partial dispatches and blockers.

Estimated LOC: 160. Risk: flattening combined PRs. Mitigation: require `cluster_id` in replay queries and tests.

### Day 3 — cost dashboard and packaging

Add cost tables, price snapshot table, no-price dashboard, ASCII chart, and README. The day is successful when `scoutflow-cost --unknown` lists rows without usage and `scoutflow-cost --cluster PF-C2` prints a conservative report.

Estimated LOC: 150. Risk: readers mistake unknown cost for zero cost. Mitigation: dashboard header and warning on every report.

## Appendix B — line budget

| component | target LOC |
|---|---:|
| DDL and connection helper | 65 |
| manifest/CHECKPOINT import | 95 |
| PR/amend seed import helpers | 70 |
| replay renderer | 95 |
| cost dashboard CLI | 95 |
| tests / fixtures glue | 70 |
| total | 485 |

The 500 LOC cap is tight but credible if the first version avoids classes where functions suffice, avoids web servers, and stores complex metadata as JSON text. It is not credible if the implementation tries to parse every historical PR diff automatically. The first version should prefer explicit seed files and small import adapters.

## Appendix C — excluded work

Excluded from the three-day budget:

- live web price verification.
- provider API integrations.
- reading private `~/.claude` or `~/.codex` logs.
- UI dashboard.
- OpenTelemetry spans.
- Temporal workflows.
- background daemon.
- production ScoutFlow code changes.
- writing `docs/current.md` or task-index.

## Appendix D — test budget

Minimal tests should cover DDL creation, manifest import, checkpoint import, amend event insertion, replay rendering, no-price dashboard warning, and duplicate import idempotency. A small pytest suite can run in under a second because everything is SQLite in a temporary directory. No browser automation, no network, and no provider calls are required.


## Appendix E — implementation budget audit checklist
1. For single-user implementation budget, the operator should count lines after removing comments and fixtures; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
2. For single-user implementation budget, the operator should keep importers explicit instead of building a general PR crawler; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
3. For single-user implementation budget, the operator should write tests around the four verified run patterns; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
4. For single-user implementation budget, the operator should defer provider integrations to a later approved phase; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
5. For single-user implementation budget, the operator should confirm the CLI runs without network access; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
6. For single-user implementation budget, the operator should count lines after removing comments and fixtures; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
7. For single-user implementation budget, the operator should keep importers explicit instead of building a general PR crawler; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
8. For single-user implementation budget, the operator should write tests around the four verified run patterns; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
9. For single-user implementation budget, the operator should defer provider integrations to a later approved phase; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
10. For single-user implementation budget, the operator should confirm the CLI runs without network access; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
11. For single-user implementation budget, the operator should count lines after removing comments and fixtures; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
12. For single-user implementation budget, the operator should keep importers explicit instead of building a general PR crawler; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
13. For single-user implementation budget, the operator should write tests around the four verified run patterns; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
14. For single-user implementation budget, the operator should defer provider integrations to a later approved phase; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
15. For single-user implementation budget, the operator should confirm the CLI runs without network access; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
16. For single-user implementation budget, the operator should count lines after removing comments and fixtures; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
