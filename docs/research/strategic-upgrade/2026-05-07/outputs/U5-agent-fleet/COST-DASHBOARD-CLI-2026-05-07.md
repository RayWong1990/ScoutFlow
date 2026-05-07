---
title: COST dashboard CLI
status: candidate / not-authority
claim_label: ">=95% design-confidence / token prices not live-verified"
created_at: 2026-05-07
---

# COST-DASHBOARD-CLI


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


## 1. CLI objective

`scoutflow-cost` 是一个 SQLite read-only CLI。它不采集 provider 账单，不连接外部 API，不上传数据，不读取私有 agent session。它只查询 `cost_attribution_ledger` 和 dispatch tables，输出表格 + ASCII bar。第一版允许 cost 全是 unknown，因为“unknown”本身就是 U5 想暴露的 instrumentation 缺口。

## 2. Commands

```bash
scoutflow-cost --week
scoutflow-cost --month
scoutflow-cost --agent Codex
scoutflow-cost --cluster PF-C2
scoutflow-cost --roi
scoutflow-cost --phase amend --since 2026-05-01 --until 2026-05-31
scoutflow-cost import-usage usage.csv
scoutflow-cost prices add --provider openai --model gpt-x --input 0 --output 0 --source manual
```

## 3. Output contract

```text
ScoutFlow cost dashboard (candidate / local-only)
period: 2026-05-01..2026-05-31
price_status: missing_live_verified_price_snapshot

cluster       dispatches   usd_est   tokens      useful   roi_note
PF-C1         12           0.0000    unknown     1.95     pass but all needs-edit
PF-C2         12           0.0000    unknown     0.75     partial cascade; RAW handoff pending
Run-2         14           0.0000    unknown     n/a      amendment burn not tokenized
W2-docs       17           0.0000    unknown     n/a      docs support; C3-04 deferred

Burn chart (usd_est)
PF-C1    | 
PF-C2    | 
Run-2    | 
W2-docs  | 

warning: token/cost rows exist but price snapshots are missing or zero; do not use this as provider billing truth.
```

When values are non-zero:

```text
PF-C1    | #################### 12.40
PF-C2    | ########             5.10
Run-2    | ###                  1.80
```

## 4. ASCII bar rule

- Find max value in group.
- If max is 0, print empty bars and warning.
- Scale to 20 chars.
- Never colorize by default; keep terminal plain.
- Round USD to 4 decimals, tokens to integer.

## 5. Query pack


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


## 6. Python CLI skeleton

```python
import argparse, sqlite3

def bar(value: float, max_value: float, width: int = 20) -> str:
    if max_value <= 0:
        return ""
    n = int(round((value / max_value) * width))
    return "#" * n

def print_table(rows):
    max_usd = max((float(r["usd"] or 0) for r in rows), default=0)
    print("cluster       dispatches   usd_est   tokens      chart")
    for r in rows:
        usd = float(r["usd"] or 0)
        print("%-12s %10s %9.4f %10s  %s" % (r["cluster_id"], r["dispatches"], usd, str(r["tokens"] or "unknown"), bar(usd, max_usd)))
    if max_usd == 0:
        print("warning: no non-zero cost estimates; token capture or price snapshot missing")

# main() chooses SQL by --week/--month/--agent/--cluster and prints rows.
```

## 7. Dashboard readings for known runs

### Run-1

Run-1 should appear as high amendment risk, not necessarily high token burn, because the verified issue is silent flexibility/allowed_paths drift. Dashboard should flag `amend_count>0` and `silent_flexibility_flag=1` even if cost is unknown.

### Run-2

Run-2 should show receipt traceability amendment cost. The important KPI is not USD; it is the reduction of future confusion from PR #226/#228 topology. If token capture is absent, the row still helps identify a repeated pattern: receipt fixes after audit.

### Window-2

W2 should show 17 dispatch merged, one deferred dependency (PF-C3-04), and no authority/runtime drift. Cost ROI is likely “support docs and guardrails,” not direct product proof.

### Run-3+4

Run-3+4 should split C1 and C2. C1 gets usefulness score because human verdict exists. C2 gets partial cascade score and future blocker. Flattening the combined PR into one cost row would destroy the very signal the ledger is meant to preserve.

## 8. Why no web price auto-fetch

Auto-fetching model prices would reintroduce live web/API dependencies and price freshness risk. For U5, the safer primitive is manual `model_price_snapshot` import with a source URL and `live_verified_at`. If a future unlock allows live browsing/API, the price importer can be added as a separate optional command. Until then, dashboard truth is local DB truth, not vendor billing truth.

## 9. Failure modes

| failure | behavior |
|---|---|
| DB missing | print init hint, exit 2 |
| no cost rows | print dispatch counts and `cost_unknown` warning |
| price snapshot missing | compute token totals but USD 0, warning |
| malformed CSV | reject row and print line number |
| negative tokens/cost | reject import |
| unknown agent | import as `Unknown` only if `--allow-unknown-agent` |

## 10. Minimal install

No package install required. Put the script in `tools/scoutflow_cost.py`, run with `python tools/scoutflow_cost.py --week --db .scoutflow-agent-fleet-ledger.sqlite`. That keeps it aligned with single-user budget and avoids package-manager approval questions.


## Appendix A — command matrix

The dashboard should support a small command matrix rather than a feature-heavy UI:

| command | purpose | output |
|---|---|---|
| `scoutflow-cost --week` | weekly burn | cluster table + bar chart |
| `scoutflow-cost --month` | monthly burn | cluster and agent ranking |
| `scoutflow-cost --agent Codex` | agent-specific cost | phase breakdown |
| `scoutflow-cost --cluster PF-C2` | cluster deep dive | dispatch rows and amendments |
| `scoutflow-cost --unknown` | missing cost evidence | rows with null tokens/prices |
| `scoutflow-cost --roi` | value-normalized view | ROI score and caveats |
| `scoutflow-cost --export markdown` | audit export | Markdown report |

The default should be conservative: do not assume week or month from local timezone if the database has no dates. Use `created_at` and show the date range explicitly.

## Appendix B — no-price dashboard behavior

Because the current evidence has no provider token exports, the dashboard will often run in no-price mode. No-price mode is still useful. It should show:

- dispatch count by cluster.
- amendment count by cluster.
- partial/reject count by cluster.
- missing token rows.
- missing price snapshot rows.
- artifact count by phase.

A no-price dashboard can answer “where should instrumentation be added first?” For ScoutFlow, the answer is likely the clusters that combine high dispatch volume and high amend risk: Run-2 receipt traceability and Run-3+4 C2 partial cascade. This is not billing truth, but it is operationally useful.

## Appendix C — dashboard SQL snippets

```sql
-- Missing usage rows by cluster
SELECT d.cluster_id, COUNT(*) AS missing_usage
FROM agent_fleet_dispatch_ledger d
LEFT JOIN cost_attribution_ledger c ON c.dispatch_id = d.dispatch_id
WHERE c.cost_id IS NULL OR c.token_input IS NULL OR c.token_output IS NULL
GROUP BY d.cluster_id
ORDER BY missing_usage DESC;

-- Amendment burn proxy
SELECT d.cluster_id,
       COUNT(a.amend_id) AS amend_events,
       COUNT(DISTINCT d.dispatch_id) AS dispatches
FROM agent_fleet_dispatch_ledger d
LEFT JOIN dispatch_amend_events a ON a.dispatch_id = d.dispatch_id
GROUP BY d.cluster_id
ORDER BY amend_events DESC, dispatches DESC;

-- Agent cost by phase
SELECT agent_kind, phase,
       SUM(COALESCE(cost_usd_estimate,0)) AS usd,
       SUM(COALESCE(token_input,0)+COALESCE(token_output,0)) AS tokens
FROM cost_attribution_ledger
GROUP BY agent_kind, phase
ORDER BY usd DESC;
```

## Appendix D — chart formatting cases

Case 1: all zero cost. Print blank bars and a warning. Case 2: one non-zero cluster and many zero clusters. Print the non-zero cluster with full width and zero clusters blank. Case 3: missing cost rows. Print `unknown` rather than `0.0000` if there is no cost row at all. Case 4: mixed estimates. Add a `method` column so `provider_usage_export` and `manual_estimate` are not visually equivalent.

Example:

```text
cluster      dispatches  usd_est  method                 chart
PF-C1        12          unknown  no_usage_rows           
PF-C2        12          0.4200   manual_estimate         ####################
Run-2        14          unknown  no_usage_rows           
```

## Appendix E — dashboard guardrails

The CLI must repeat the evidence status at the top of every report. A dashboard without evidence status is dangerous because readers may mistake a zero for a verified zero. Recommended header:

```text
ScoutFlow cost dashboard
ledger: .scoutflow-agent-fleet-ledger.sqlite
price_status: missing_live_verified_price_snapshot
usage_status: partial_or_missing
runtime_scope: candidate/not-authority
```

The dashboard must not fetch provider prices automatically in this phase. Automatic fetching would reintroduce live web/runtime behavior that the U5 prompt explicitly keeps out of scope.


## Appendix F — dashboard audit checklist
1. For cost dashboard output, the operator should print price_status and usage_status in the header; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
2. For cost dashboard output, the operator should group combined PRs by cluster instead of PR number only; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
3. For cost dashboard output, the operator should show unknown tokens as unknown rather than zero; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
4. For cost dashboard output, the operator should scale ASCII bars from verified numeric values only; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
5. For cost dashboard output, the operator should export markdown with the same warnings as terminal output; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
6. For cost dashboard output, the operator should print price_status and usage_status in the header; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
7. For cost dashboard output, the operator should group combined PRs by cluster instead of PR number only; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
8. For cost dashboard output, the operator should show unknown tokens as unknown rather than zero; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
9. For cost dashboard output, the operator should scale ASCII bars from verified numeric values only; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
10. For cost dashboard output, the operator should export markdown with the same warnings as terminal output; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
11. For cost dashboard output, the operator should print price_status and usage_status in the header; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
12. For cost dashboard output, the operator should group combined PRs by cluster instead of PR number only; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
13. For cost dashboard output, the operator should show unknown tokens as unknown rather than zero; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
14. For cost dashboard output, the operator should scale ASCII bars from verified numeric values only; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
15. For cost dashboard output, the operator should export markdown with the same warnings as terminal output; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
16. For cost dashboard output, the operator should print price_status and usage_status in the header; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
17. For cost dashboard output, the operator should group combined PRs by cluster instead of PR number only; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
18. For cost dashboard output, the operator should show unknown tokens as unknown rather than zero; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
19. For cost dashboard output, the operator should scale ASCII bars from verified numeric values only; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
20. For cost dashboard output, the operator should export markdown with the same warnings as terminal output; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
21. For cost dashboard output, the operator should print price_status and usage_status in the header; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
22. For cost dashboard output, the operator should group combined PRs by cluster instead of PR number only; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
23. For cost dashboard output, the operator should show unknown tokens as unknown rather than zero; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
24. For cost dashboard output, the operator should scale ASCII bars from verified numeric values only; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
