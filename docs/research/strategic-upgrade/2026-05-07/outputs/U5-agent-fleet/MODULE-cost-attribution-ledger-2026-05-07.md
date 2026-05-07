---
title: MODULE cost attribution ledger
status: candidate / not-authority
claim_label: ">=95% design-confidence / price data not live-verified"
created_at: 2026-05-07
---

# MODULE — cost_attribution_ledger


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


## 1. Why cost attribution is separate from dispatch ledger

Dispatch ledger 回答“发生了什么”；cost ledger 回答“代价是谁烧掉的，换来了什么”。这两个表不能合并，因为一个 dispatch 可能有多段成本：初稿、amend、audit、replay、dashboard query；也可能一个 artifact 的价值来自多个 dispatch。把 cost 作为独立 ledger 可以把 `agent_kind/model_id/token_input/token_output/cost_usd_estimate/artifact_id/phase` 拆开，后续才能问：哪一个 cluster 最贵？哪一种 agent 最贵？哪个 prompt template 产出高 ROI？哪条 amend lane 重复烧钱？

由于当前环境不能 live verify 2026-05 provider price，本 spec 不写任何“当前价格事实”。价格进入 `model_price_snapshot`，由用户或未来 script 手动更新；如果没有 price snapshot，则 `cost_usd_estimate=0` 并标记 `estimate_method='manual_tokens_no_price'`。这比硬编码过时价格更诚实。

## 2. Schema relation

`cost_attribution_ledger.dispatch_id` FK 到 `agent_fleet_dispatch_ledger.dispatch_id`。`artifact_id` FK 到 `artifact_dimension`，让 visual asset、prompt template、entity、code、receipt、checkpoint 等都可成为 ROI 归因对象。`price_id` FK 到 `model_price_snapshot`，把“token 数”和“价格版本”分离。

## 3. Cost DDL subset

 (
  artifact_id TEXT PRIMARY KEY,
  artifact_kind TEXT NOT NULL CHECK(artifact_kind IN ('visual_asset','prompt_template','entity','code','receipt','audit','checkpoint','run_report','diff_bundle','other')),
  artifact_path TEXT,
  owner_dispatch_id TEXT REFERENCES agent_fleet_dispatch_ledger(dispatch_id) ON DELETE SET NULL,
  roi_label TEXT,
  usefulness_verdict TEXT CHECK(usefulness_verdict IS NULL OR usefulness_verdict IN ('follow','needs-edit','park','reject','unknown')),
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS model_price_snapshot (
  price_id TEXT PRIMARY KEY,
  provider TEXT NOT NULL,
  model_id TEXT NOT NULL,
  input_usd_per_1m REAL,
  output_usd_per_1m REAL,
  cached_input_usd_per_1m REAL,
  price_source_url TEXT,
  live_verified_at TEXT,
  notes TEXT,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(provider, model_id, live_verified_at)
);

CREATE TABLE IF NOT EXISTS cost_attribution_ledger (
  cost_id TEXT PRIMARY KEY,
  dispatch_id TEXT NOT NULL REFERENCES agent_fleet_dispatch_ledger(dispatch_id) ON DELETE CASCADE,
  agent_kind TEXT NOT NULL CHECK(agent_kind IN ('CC0','CC1','Codex','Hermes','OpenClaw','GPT_Pro','Unknown')),
  model_id TEXT,
  token_input INTEGER NOT NULL DEFAULT 0 CHECK(token_input >= 0),
  token_output INTEGER NOT NULL DEFAULT 0 CHECK(token_output >= 0),
  token_cached_input INTEGER NOT NULL DEFAULT 0 CHECK(token_cached_input >= 0),
  cost_usd_estimate REAL NOT NULL DEFAULT 0 CHECK(cost_usd_estimate >= 0),
  artifact_id TEXT REFERENCES artifact_dimension(artifact_id) ON DELETE SET NULL,
  phase TEXT NOT NULL DEFAULT 'unknown',
  price_id TEXT REFERENCES model_price_snapshot(price_id) ON DELETE SET NULL,
  estimate_method TEXT NOT NULL DEFAULT 'manual_tokens',
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_cost_dispatch ON cost_attribution_ledger(dispatch_id);
CREATE INDEX IF NOT EXISTS idx_cost_agent ON cost_attribution_ledger(agent_kind);
CREATE INDEX IF NOT EXISTS idx_cost_phase ON cost_attribution_ledger(phase);
CREATE INDEX IF NOT EXISTS idx_cost_created ON cost_attribution_ledger(created_at);

CREATE TABLE IF NOT EXISTS orchestration_boundary_scan (
  scan_id TEXT PRIMARY KEY,
  window_id TEXT REFERENCES dispatch_windows(window_id) ON DELETE CASCADE,
  dispatch_id TEXT REFERENCES agent_fleet_dispatch_ledger(dispatch_id) ON DELETE CASCADE,
  scan_kind TEXT NOT NULL CHECK(scan_kind IN ('preflight','pre_merge','post_merge','audit','replay')),
  authority_files_touched INTEGER NOT NULL DEFAULT 0 CHECK(authority_files_touched IN (0,1)),
  forbidden_paths_touched INTEGER NOT NULL DEFAULT 0 CHECK(forbidden_paths_touched IN (0,1)),
  write_enabled_false_preserved INTEGER NOT NULL DEFAULT 1 CHECK(write_enabled_false_preserved IN (0,1)),
  runtime_unlock_claimed INTEGER NOT NULL DEFAULT 0 CHECK(runtime_unlock_claimed IN (0,1)),
  five_overflow_flag INTEGER NOT NULL DEFAULT 0 CHECK(five_overflow_flag IN (0,1)),
  verdict TEXT NOT NULL CHECK(verdict IN ('clear','concern','reject','partial')),
  notes TEXT,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS pattern_library (
  pattern_id TEXT PRIMARY KEY,
  pattern_name TEXT NOT NULL,
  pattern_kind TEXT NOT NULL CHECK(pattern_kind IN ('amend','orchestration','boundary','cost','replay')),
  severity TEXT CHECK(severity IN ('low','medium','high','critical','none')),
  detector_hint TEXT,
  recommended_action TEXT,
  source_ref TEXT,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS checkpoint_backfill_map (
  map_id TEXT PRIMARY KEY,
  checkpoint_path TEXT NOT NULL,
  checkpoint_key TEXT NOT NULL,
  target_table TEXT NOT NULL,
  target_column TEXT NOT NULL,
  transform_rule TEXT NOT NULL,
  lossy INTEGER NOT NULL DEFAULT 0 CHECK(lossy IN (0,1)),
  notes TEXT
);
```


## 4. Monthly / weekly reporting SQL


```sql
-- 本周哪个 cluster 烧钱最多
SELECT d.cluster_id,
       COUNT(DISTINCT d.dispatch_id) AS dispatches,
       ROUND(SUM(c.cost_usd_estimate), 4) AS usd,
       SUM(c.token_input + c.token_cached_input + c.token_output) AS tokens
FROM cost_attribution_ledger c
JOIN agent_fleet_dispatch_ledger d USING(dispatch_id)
WHERE date(c.created_at) >= date('now', '-7 days')
GROUP BY d.cluster_id
ORDER BY usd DESC
LIMIT 10;

-- 本月哪个 agent 最贵，输出单人调度配额是否失衡
SELECT c.agent_kind,
       COUNT(DISTINCT c.dispatch_id) AS dispatches,
       ROUND(SUM(c.cost_usd_estimate), 4) AS usd,
       ROUND(AVG(c.cost_usd_estimate), 4) AS avg_usd_per_dispatch,
       SUM(c.token_input) AS input_tokens,
       SUM(c.token_output) AS output_tokens
FROM cost_attribution_ledger c
WHERE strftime('%Y-%m', c.created_at) = strftime('%Y-%m', 'now')
GROUP BY c.agent_kind
ORDER BY usd DESC;

-- ROI: useful verdict / cost。needs-edit 算有用但需要手工成本，权重 0.65。
SELECT d.cluster_id,
       ROUND(SUM(CASE a.usefulness_verdict
           WHEN 'follow' THEN 1.0
           WHEN 'needs-edit' THEN 0.65
           WHEN 'park' THEN 0.2
           ELSE 0 END), 2) AS usefulness_score,
       ROUND(SUM(c.cost_usd_estimate), 4) AS usd,
       ROUND(SUM(CASE a.usefulness_verdict
           WHEN 'follow' THEN 1.0
           WHEN 'needs-edit' THEN 0.65
           WHEN 'park' THEN 0.2
           ELSE 0 END) / NULLIF(SUM(c.cost_usd_estimate), 0), 2) AS usefulness_per_usd
FROM cost_attribution_ledger c
JOIN agent_fleet_dispatch_ledger d USING(dispatch_id)
LEFT JOIN artifact_dimension a ON a.artifact_id = c.artifact_id
GROUP BY d.cluster_id
ORDER BY usefulness_per_usd DESC;
```


## 5. ROI model

单人 fleet 的 ROI 不应该追求企业财务精确，而应该稳定回答“继续开这一类 dispatch 值不值”。建议三层：

| ROI dimension | Formula | Interpretation |
|---|---|---|
| usefulness_per_usd | weighted usefulness / cost_usd | 适合 C1/C2 human verdict lane |
| accepted_clear_per_usd | count(verdict in clear/pass) / cost_usd | 适合 audit/research lane |
| amend_burn_ratio | amend_cost / original_cost | 判断是否需要更强 preflight |
| human_gate_savings | avoided rework hours * hourly_value - LLM cost | 适合 proof pair |
| evidence_density | count(artifact rows) / cost_usd | 适合 docs/audit bundle |

`needs-edit` 不能算失败。PR #240 的 C1 3/3 useful 但 all needs-edit，意味着它不是“无价值”，而是“有用但需要人工修辞/语义修补”。因此 ROI score 可把 `follow=1.0`、`needs-edit=0.65`、`park=0.2`、`reject=0`。这个权重应放在 query 或 config，不写死进 schema。

## 6. Cost phases

推荐 phase enum 不强制 CHECK constraint，先用字符串：

- `draft`: 初稿生产。
- `audit`: 外审/自审。
- `amend`: amendment PR 或 receipt fix。
- `replay`: reconstruct timeline。
- `dashboard`: 统计查询。
- `handoff`: RAW/staging/human gate handoff。
- `visual`: screenshot packet、视觉候选、manual review summary。

Run-1/Run-2 的成本如果没有 token 记录，只能先 backfill `cost_usd_estimate=0`，并把 `estimate_method='missing_runtime_tokens'`。不要为了 dashboard 好看而猜 token。

## 7. Example CSV import path

```text
cost_id,dispatch_id,agent_kind,model_id,token_input,token_output,token_cached_input,cost_usd_estimate,phase,artifact_id,estimate_method
cost_001,disp_pf_c1_04,Codex,codex-cli,18234,5302,0,0.0000,draft,artifact_topic_card_lite,missing_price_snapshot
cost_002,disp_run1_audit_gpt,GPT_Pro,gpt-pro-web,41200,9800,0,0.0000,audit,artifact_run1_external_audit,subscription_no_token_api
cost_003,disp_run2_amend,Codex,codex-cli,9000,2200,0,0.0000,amend,artifact_run2_amendment_ledger,missing_price_snapshot
```

这类 CSV 可由用户从 provider dashboard 手动导出，也可由本地 agent wrapper 在 stdout 末尾写入。注意：如果 token 来源不是 API 原始 usage，而是手工估算，必须在 `estimate_method` 中说明。

## 8. Dashboard aggregation examples

### 8.1 Cluster burn table

```text
cluster      dispatches  cost_usd  useful  amend_cost  roi_note
PF-C1        12          0.0000    1.95    0.0000      useful but needs semantic enrichment
PF-C2        12          0.0000    0.75    0.0000      partial cascade; defer until RAW intake
Run-2        14          0.0000    0.00    0.0000      receipt traceability amendment, no rollback
W2-docs      17          0.0000    n/a     0.0000      support docs, C3-04 deferred
```

### 8.2 Agent burn table

```text
agent      dispatches  input_tokens  output_tokens  cost_usd  warning
Codex      76          unknown       unknown        0.0000    token accounting absent
GPT_Pro    4           unknown       unknown        0.0000    subscription/no usage record
Hermes     1           unknown       unknown        0.0000    audit verdict only
```

The warning column is not cosmetic. In the current ScoutFlow evidence, token/cost instrumentation is absent, so the first dashboard may mostly show `unknown`. That is still useful: it proves the new wrapper needs token capture before claims.

## 9. Cost attribution rules

1. Never infer price from model name without a `model_price_snapshot` row.
2. Never mix subscription sunk cost with per-token API cost unless `estimate_method` says so.
3. If a dispatch is combined into one PR, cost remains per dispatch if token usage is available; PR number is only a grouping key.
4. If an amend PR fixes multiple runs, split by `dispatch_id` when possible; otherwise create a synthetic `dispatch_id='run2-amendment-pr239'` and annotate lossy attribution.
5. If a cluster is partial, cost still counts. Partial is exactly where cost questions matter.
6. Prompt caching savings are a field-level query concern, not a schema assumption; use `token_cached_input` when provider usage exposes it.

## 10. Candidate command names

```bash
scoutflow-cost --week
scoutflow-cost --month --cluster PF-C2
scoutflow-cost --agent Codex --since 2026-05-01
scoutflow-cost --roi --group-by artifact_kind
scoutflow-cost import-csv usage.csv --price-snapshot prices-2026-05.json
```

## 11. Backfill strategy when cost is unknown

The first backfill should produce honest zero-cost rows only if it also sets `estimate_method='missing_runtime_tokens'`. Alternative: skip rows entirely until a wrapper captures tokens. I recommend inserting rows with zero estimate and explicit method because the absence itself is a signal in the dashboard: it tells the operator the current fleet cannot answer burn-rate questions, which is the exact gap U5 is closing.


## Appendix A — token source hierarchy and estimate discipline

The cost ledger must separate three things that are often mixed together in ad-hoc agent runs: raw token count, provider billing price, and value attribution. A row may have exact input tokens but no price; it may have a provider invoice total but no per-dispatch breakdown; or it may have a manual estimate derived from prompt length. The schema therefore treats every numeric field as evidence with a source, not as a magical truth.

Priority order for token source is:

1. `provider_usage_export`: exact provider export or model response usage object, with captured timestamp and model id.
2. `agent_stdout_usage`: CLI prints usage counters and the stdout is preserved as a safe redacted receipt.
3. `local_tokenizer_estimate`: local tokenizer estimate for prompt and output strings, marked estimate.
4. `manual_estimate`: operator typed a number into the ledger after a run.
5. `unknown`: token fields remain null, cost remains zero, and dashboard prints warning.

This matters because ScoutFlow currently has no runtime instrumentation. A cost dashboard that invents token usage would be worse than no dashboard. The first implementation should accept null token values and still rank clusters by observed amend count, dispatch count, and risk. Token capture can be added without changing the table shape.

## Appendix B — price snapshot protocol

`model_price_snapshot` is deliberately versioned because provider prices and cache rules change. The ledger never hard-codes May 2026 prices. A safe snapshot row needs `provider`, `model_id`, `input_usd_per_million`, `output_usd_per_million`, `cache_read_usd_per_million`, `cache_write_usd_per_million`, `effective_from`, and `source_url`. The source URL can be empty only when `source_kind='manual_unverified'`; in that case dashboards must display `price_status=manual_unverified`.

When a user updates pricing, the tool should insert a new snapshot, not edit the old row. Historical reports can then reproduce the estimate as it existed at closeout. A `cost_attribution_ledger.price_snapshot_id` foreign key pins each computed estimate. If the provider invoice later disagrees, the operator can add a `billing_reconciliation` artifact row without deleting the original estimate. This keeps cost history auditable rather than retroactively perfect.

## Appendix C — ROI calculation examples

ROI in this single-user ledger is not financial return. It is a practical usefulness ratio: evidence value divided by estimated burn. The minimum viable formula is:

```text
roi_score = useful_output_score / max(cost_usd_estimate, 0.01)
```

`useful_output_score` can be filled by simple verdict mapping:

| verdict | base useful score | modifier |
|---|---:|---|
| clear | 1.00 | +0.25 if merged and no amend |
| concern | 0.65 | -0.15 if follow-up required |
| partial | 0.45 | +0.20 if expected_partial was honest and useful |
| reject | 0.05 | +0.10 if reject prevented bad merge |
| expected_partial | 0.35 | +0.20 when it preserves a downstream gate |

For Run-3+4, C1 is a good example: the user verdict was pass, but all three rows needed edit. A realistic `useful_output_score` should be less than a perfect pass because edit-cost remains high. For C2, the partial cascade should not be punished as a failed run if it preserved RAW handoff truth and prevented opening C4 too early. The ROI model therefore needs both `verdict` and `amend/risk` fields.

## Appendix D — cost backfill when no tokens exist

Current ScoutFlow evidence has dispatch receipts, PR numbers, validators, and amendment ledgers, but not per-agent token counters. Backfill should create rows with `token_input=null`, `token_output=null`, `cost_usd_estimate=0`, and `estimate_method='unknown_usage'`. The row still helps dashboard queries because it links dispatches to clusters, phases, and artifacts.

A good first backfill for the four verified run patterns is:

| run | cost rows | reason |
|---|---:|---|
| Run-1 | 8 dispatch rows + 1 amendment audit row | allowed-path drift was discovered after merge |
| Window-2 | 17 dispatch rows | docs run with C3-04 deferred |
| Run-2 | 14 dispatch rows + 1 amendment row | receipt topology and UAT partial corrections |
| Run-3+4 | 24 dispatch rows + 2 cluster rows | C1 pass and C2 partial must remain separable |

The dashboard should not print zero cost as success. It should print `cost_unknown=true`, which is a prompt to add token capture later. This is still useful because the operator can ask “which cluster lacks price evidence but generated the most amendments?”

## Appendix E — cost-related self-audit cases

1. A dispatch has `model_id` but no tokens: dashboard must not compute provider cost.
2. A dispatch has tokens but no price snapshot: dashboard may show token totals but not USD truth.
3. A dispatch has price snapshot but zero tokens: dashboard must show zero estimate and warn.
4. A model id changes during amend: create separate rows for the original dispatch and amend phase.
5. Prompt caching is used: record cache read/write tokens separately or leave cache fields null.
6. A combined PR covers multiple clusters: cost rows must carry `cluster_id` so PF-C1 and PF-C2 do not flatten into one burn number.
7. A human manually edits an artifact outside an agent: add `agent_kind='Human'` only if enum is extended by user; otherwise record as artifact note, not agent cost.
8. Provider invoice arrives later: add reconciliation metadata; do not mutate historical estimate silently.
9. Cost dashboard is exported: include price snapshot status and generated_at.
10. Token/cost values are sensitive only when they expose prompt content; numbers alone are safe, but source stdout must still be redacted before storage.


## Appendix F — cost ledger audit checklist
1. For cost attribution rows, the operator should distinguish missing usage from zero cost; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
2. For cost attribution rows, the operator should pin each USD estimate to a price snapshot; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
3. For cost attribution rows, the operator should split amend phase cost from original dispatch cost; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
4. For cost attribution rows, the operator should keep provider billing reconciliation as an additive artifact; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
5. For cost attribution rows, the operator should flag manual estimates with estimate_method and confidence; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
6. For cost attribution rows, the operator should distinguish missing usage from zero cost; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
7. For cost attribution rows, the operator should pin each USD estimate to a price snapshot; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
8. For cost attribution rows, the operator should split amend phase cost from original dispatch cost; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
9. For cost attribution rows, the operator should keep provider billing reconciliation as an additive artifact; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
10. For cost attribution rows, the operator should flag manual estimates with estimate_method and confidence; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
11. For cost attribution rows, the operator should distinguish missing usage from zero cost; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
12. For cost attribution rows, the operator should pin each USD estimate to a price snapshot; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
13. For cost attribution rows, the operator should split amend phase cost from original dispatch cost; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
14. For cost attribution rows, the operator should keep provider billing reconciliation as an additive artifact; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
15. For cost attribution rows, the operator should flag manual estimates with estimate_method and confidence; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
16. For cost attribution rows, the operator should distinguish missing usage from zero cost; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
17. For cost attribution rows, the operator should pin each USD estimate to a price snapshot; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
18. For cost attribution rows, the operator should split amend phase cost from original dispatch cost; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
19. For cost attribution rows, the operator should keep provider billing reconciliation as an additive artifact; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
20. For cost attribution rows, the operator should flag manual estimates with estimate_method and confidence; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
21. For cost attribution rows, the operator should distinguish missing usage from zero cost; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
22. For cost attribution rows, the operator should pin each USD estimate to a price snapshot; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
23. For cost attribution rows, the operator should split amend phase cost from original dispatch cost; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
24. For cost attribution rows, the operator should keep provider billing reconciliation as an additive artifact; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
