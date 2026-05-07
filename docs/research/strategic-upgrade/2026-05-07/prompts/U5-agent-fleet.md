---
title: Cloud Prompt — U5 Agent Fleet Instrumentation (多 AI agent 派单台账 + 成本归因)
status: candidate / cloud_prompt / not-authority
authority: not-authority
created_at: 2026-05-07
target_window: GPT Pro web 浏览模式
new_lane: yes
---

# Cloud Prompt — U5 Agent Fleet Instrumentation

## §1 Mission

ScoutFlow 用户在 max horsepower 模式跑 multi-AI agent fleet (CC0 / CC1 / Codex / Hermes / OpenClaw), 实测 ~50 dispatch / 2h 节奏。**当前完全无运行时 instrumentation**: CHECKPOINT.json 仅是收尾收据, 没有派单 ledger / 成本归因 / agent 表现追踪 / amend 触发分析。

本任务: 写 single-user agent fleet instrumentation 完整 candidate spec — `agent_fleet_dispatch_ledger` + `cost_attribution_ledger` + multi-agent orchestration primitives — 单人量级 (≤500 行 Python + SQLite), **不是企业 OpenTelemetry W3C Trace Context 重型方案**。

## §2 Inputs

1. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/EXTERNAL-AUDIT-REPORT-2026-05-07.md (Run-3+4 audit)
2. Run-1 / Run-2 / Window-2 / Run-3+4 CHECKPOINT JSON (4 run 收尾收据 schema 已有)
3. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/PRD-v2-2026-05-04.md (LP-006 Single Writer)
4. https://github.com/RayWong1990/ScoutFlow/blob/main/AGENTS.md (multi-agent 协作纪律)
5. 用户实际 4 run pattern: 80-pack dispatch + 7 cluster + amend_and_proceed
6. **Live web** 真实 search multi-agent orchestration 2026

## §3 Multi-pass Work Plan (≥10 pass, ≥120 min)

1. **Pass 1**: 读 4 run CHECKPOINT JSON + EXTERNAL-AUDIT 8 章 + AGENTS.md 协作纪律, 抽象现 dispatch 节奏
2. **Pass 2 — Live web**: 真实 search ≥15: LangGraph / CrewAI / AutoGen / MetaGPT / Temporal Agent / OpenAI Agents SDK / Inngest / Trigger.dev / dispatch ledger 模式 / 单创作者 cost dashboard / Claude Code 多窗口协作 / Codex parallel
3. **Pass 3 — agent_fleet_dispatch_ledger schema**: SQLite 表 (dispatch_id / window_id / agent_kind ∈ {CC0/CC1/Codex/Hermes/OpenClaw/GPT_Pro} / model_id / task_id (cluster.dispatch e.g. PF-C2-06) / parent_dispatch_id / start_at / end_at / verdict ∈ {clear/concern/reject/partial/expected_partial} / amend_count / amend_trigger_text / output_path / pr_number / silent_flexibility_flag), 与 CHECKPOINT.json 双向 derive
4. **Pass 4 — cost_attribution_ledger schema**: SQLite 表 (cost_id / dispatch_id FK / agent_kind / token_input / token_output / model_id / cost_usd_estimate / artifact_id (visual_asset / prompt_template / entity / code FK) / phase / created_at), 月报 query (这周/月哪条 cluster 烧钱最多, 哪 agent 最贵, ROI 哪个)
5. **Pass 5 — Orchestration primitive lib**: 抽象 5 primitive: `parallel_dispatch_window` (3-5 worktree) / `amend_and_proceed_pattern` (multi-auditor REJECT → user 授权 amend → 直 merge) / `single_writer_lock` (LP-006) / `boundary_scan` (write_enabled / 5 overflow / authority files) / `truthful_stdout_contract` (无伪造 wall-clock)
6. **Pass 6 — Replay tool**: 给定 dispatch_id 重建 input/output/audit/amend trail 的 timeline view (markdown 渲染)
7. **Pass 7 — Cost dashboard**: 简易 CLI script `scoutflow-cost --week / --month / --agent / --cluster`, 输出表格 + 简易 ASCII bar chart
8. **Pass 8 — Amend trigger pattern catalog**: 提取 4 run 实际 amend trigger (Run-1 silent flexibility / Run-2 PR226-228 packed repair / Run-3+4 partial cascade), 写成 amend_pattern 库, 与 pattern_library FK
9. **Pass 9 — Self-audit ≥15**
10. **Pass 10**: README + truthful stdout

## §4 Hard Boundaries

- candidate / not-authority
- write_enabled=False 不变 (本 lane 不解禁)
- 不批准实际部署 OpenTelemetry / Temporal / 任何 agent runtime
- ledger 仅 spec, 不实际 instrument 真实 agent (留待 Phase 2 unlock)
- 不修改 production code
- agent 名单仅 candidate (CC0/CC1/Codex/Hermes/OpenClaw/GPT_Pro), 用户可增删

## §5 Live Web Evidence Refresh

≥15 真实 search:
- LangGraph 2026 / CrewAI 2026 / AutoGen 2026 / MetaGPT 2026
- Temporal durable agent execution 2026 (OpenAI Codex 用)
- OpenAI Agents SDK / Anthropic Computer Use / Claude Code multi-window
- Inngest / Trigger.dev event-driven agent
- 单创作者 cost dashboard 2026 (Helicone / Langfuse / Helicone Cost / OpenAI usage)
- Prompt Caching (80% latency / 90% token saving)
- amend_and_proceed pattern (人工干预 + 自动重派)
- single-writer lock pattern
- Claude / GPT / Codex token cost 2026-05 当前价格

## §6 Cross-local Search

- `~/.claude/projects/` 历史 session JSONL (CC 多窗口 dispatch 数据源)
- `~/.codex/` Codex CLI 配置 + log
- `~/.claude/skills/` orchestration / brainstorm-five-lens skill
- ScoutFlow 4 run CHECKPOINT JSON 全文
- ContentFlow L1 retrospective (1749 行) — multi-agent 协作模式沉淀
- `~/.claude/rules/agents.md` Agent 使用门槛 / 并行限制

## §7 Output Deliverables

ZIP filename: `cloud-output-U5-agent-fleet-instrumentation-2026-05-07.zip`
File count: **10**

| # | File | min 字 | claim label |
|---|---|---:|---|
| 1 | MODULE-agent-fleet-dispatch-ledger-2026-05-07.md | 3000 (SQLite DDL + Python CRUD + 4 run backfill 计划) | ≥95% |
| 2 | MODULE-cost-attribution-ledger-2026-05-07.md | 2800 (SQLite DDL + 月报 query + ROI 计算) | ≥95% |
| 3 | ORCHESTRATION-PRIMITIVE-LIB-2026-05-07.md | 3000 (5 primitive Python pseudocode) | ≥95% |
| 4 | DISPATCH-REPLAY-TOOL-2026-05-07.md | 2000 (replay CLI + markdown timeline) | ≥95% |
| 5 | COST-DASHBOARD-CLI-2026-05-07.md | 2000 (CLI spec + ASCII chart 示例) | ≥95% |
| 6 | AMEND-TRIGGER-PATTERN-CATALOG-2026-05-07.md | 2500 (4 run 实际 amend 抽样) | ≥95% |
| 7 | INTEGRATION-WITH-CHECKPOINT-JSON-2026-05-07.md | 2000 (4 run CHECKPOINT.json 双向 derive 规则) | ≥95% |
| 8 | LIVE-WEB-EVIDENCE-2026-05-07.md | 2500 (≥15 vendor URL + 访问日期) | ≥95% |
| 9 | SINGLE-USER-IMPLEMENTATION-BUDGET-2026-05-07.md | 1500 (≤500 行 Python / ≤3 天 / ≤$X) | ≥95% |
| 10 | README-deliverable-index-2026-05-07.md | 1200 | 100% |

总字数 ≥**22000**

## §8 Self-audit (≥15)

- 是否漂移成企业 OTel / W3C Trace Context
- single-user vs team agent fleet
- ledger schema 是否真能从 CHECKPOINT.json derive
- cost dashboard 数字是否真按 token 计算
- amend pattern 是否真用 4 run 实例
- live web URL 真访问
- 与 U4 (visual asset) / U6/U7/U8 是否冲突
- replay 工具是否真单人量级 (vs 重型 distributed tracing)

## §9 Truthful Stdout Contract

```yaml
CLOUD_U5_AGENT_FLEET_INSTRUMENTATION_COMPLETE: true
zip_filename: cloud-output-U5-agent-fleet-instrumentation-2026-05-07.zip
files_count: 10
total_words_cjk_latin_approx: <真实>
total_thinking_minutes: <真实>
live_web_browsing_used: <true|false>
live_verified_count: <真实>
modules_specced: 5
sqlite_ddl_tables_count: <真实>
orchestration_primitives_count: 5
amend_patterns_extracted_from_4_runs: <真实>
single_user_budget_loc: <真实>
single_user_budget_dev_days: <真实>
multi_pass_completed: <真实/10>
self_audit_findings: <真实>
boundary_preservation_check: clear
ready_for_user_audit: yes
```

## §10 ZIP Filename

`cloud-output-U5-agent-fleet-instrumentation-2026-05-07.zip`
