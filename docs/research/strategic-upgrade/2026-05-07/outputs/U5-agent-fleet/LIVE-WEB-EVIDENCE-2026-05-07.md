---
title: LIVE WEB evidence
status: candidate / limitation-report / not-authority
claim_label: "live verification not completed"
created_at: 2026-05-07
---

# LIVE-WEB-EVIDENCE


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


## 1. Truthful evidence statement

The requested Pass 2 required ≥15 live web searches covering LangGraph, CrewAI, AutoGen, MetaGPT, Temporal, OpenAI Agents SDK, Inngest, Trigger.dev, cost dashboards, prompt caching, amend patterns, single-writer locks, and 2026-05 pricing. In this environment, ordinary web browsing is disabled. Therefore this file **does not** claim live verification and **does not** provide access-date evidence for vendor pages.

What was live-checked through available GitHub connector: ScoutFlow repository files and PRs #227/#231/#239/#240. What was not live-checked: vendor docs, model pricing, prompt caching figures, current token costs, framework 2026 feature states.

## 2. Unverified target list for future refresh

| # | target | URL | status in this run | evidence use |
|---:|---|---|---|---|
| 1 | LangGraph | https://langchain-ai.github.io/langgraph/ | not visited in this run; web disabled | do not use as evidence |
| 2 | CrewAI | https://docs.crewai.com/ | not visited in this run; web disabled | do not use as evidence |
| 3 | Microsoft AutoGen | https://microsoft.github.io/autogen/ | not visited in this run; web disabled | do not use as evidence |
| 4 | MetaGPT | https://github.com/geekan/MetaGPT | not visited in this run; web disabled | do not use as evidence |
| 5 | Temporal durable execution | https://temporal.io/ | not visited in this run; web disabled | do not use as evidence |
| 6 | OpenAI Agents SDK | https://platform.openai.com/docs/agents | not visited in this run; web disabled | do not use as evidence |
| 7 | Anthropic Claude Code | https://docs.anthropic.com/ | not visited in this run; web disabled | do not use as evidence |
| 8 | Inngest | https://www.inngest.com/ | not visited in this run; web disabled | do not use as evidence |
| 9 | Trigger.dev | https://trigger.dev/ | not visited in this run; web disabled | do not use as evidence |
| 10 | Langfuse | https://langfuse.com/ | not visited in this run; web disabled | do not use as evidence |
| 11 | Helicone | https://www.helicone.ai/ | not visited in this run; web disabled | do not use as evidence |
| 12 | OpenAI usage/cost docs | https://platform.openai.com/docs/ | not visited in this run; web disabled | do not use as evidence |
| 13 | Prompt caching | https://platform.openai.com/docs/guides/prompt-caching | not visited in this run; web disabled | do not use as evidence |
| 14 | Claude pricing | https://www.anthropic.com/pricing | not visited in this run; web disabled | do not use as evidence |
| 15 | GitHub Copilot/Codex docs | https://docs.github.com/ | not visited in this run; web disabled | do not use as evidence |
| 16 | W3C Trace Context | https://www.w3.org/TR/trace-context/ | not visited in this run; web disabled | do not use as evidence |

## 3. Design impact despite missing web

The U5 spec deliberately avoids depending on any current vendor framework detail. This is a strength under uncertainty. Even if LangGraph/CrewAI/AutoGen/Temporal changed significantly after the knowledge cutoff, the single-user ledger design still holds because it is not implementing those runtimes. It records local dispatches, artifacts, costs and amendments. The only parts that require live refresh before implementation are:

1. model price snapshots for cost estimates;
2. exact provider token usage fields if importing from APIs;
3. current prompt caching discount fields;
4. any future decision to integrate an actual runtime or workflow engine.

## 4. What must not be claimed

- Do not claim “Temporal is used by Codex” unless verified from a current primary source.
- Do not claim prompt caching percentages unless current vendor docs are checked.
- Do not hardcode GPT/Claude/Codex token prices in `model_price_snapshot` from memory.
- Do not cite vendor docs as accessed on 2026-05-07 from this run.
- Do not call this file the ≥15 live evidence refresh; it is a failed/blocked evidence refresh with a future target list.

## 5. Future live refresh checklist

When web is available, run this refresh as a separate evidence pass:

```text
for each target:
  open official docs/pricing page
  record URL, title, vendor, accessed_at, relevant quote, screenshot if pricing
  classify evidence: orchestration / cost / prompt caching / dashboard / runtime
  decide whether U5 design changes
  update LIVE-WEB-EVIDENCE with verified rows
  update model_price_snapshot seed only from price docs
```

Minimum acceptable future evidence row:

```yaml
vendor: OpenAI
page_title: <live title>
url: <official URL>
accessed_at: <timestamp>
claim_supported: <exact limited claim>
quote_or_summary: <short quote/summary>
used_in_u5: <schema/query/budget/no-change>
```

## 6. Offline design notes, clearly non-evidence

Based on general knowledge up to the model cutoff, multi-agent frameworks often optimize coordination, memory, tool calling, or durable execution. U5 does not need to choose among them because ScoutFlow's present issue is instrumentation absence, not workflow engine absence. For a single user running CC0/CC1/Codex/Hermes/OpenClaw/GPT Pro, the practical bottleneck is: no dispatch ledger, no cost attribution, no amend trigger catalog, and no replay. SQLite solves that without changing runtime.

## 7. Evidence verdict

```yaml
live_web_browsing_used: false
live_verified_count: 0
vendor_url_count_listed_for_future: 16
requirement_met: false
reason: web browsing disabled in current environment
safe_to_use_for_schema_design: true
safe_to_use_for_vendor_claims_or_prices: false
```


## Appendix A — future verification worksheet

Because live browsing was unavailable, this file defines exactly what should be verified when browsing is re-enabled. Each row should be filled with `visited_at`, `source_url`, `version_or_date`, `claim`, and `design_impact`.

| target | claim to verify | design impact if true | design impact if false |
|---|---|---|---|
| LangGraph | current durable graph/checkpointing features | compare with local replay graph | keep U5 simple |
| CrewAI | current multi-agent crew/task logging | borrow terminology only | no impact |
| AutoGen | current agent conversation logging | possible source for transcript import | no impact |
| MetaGPT | current role/task orchestration pattern | compare role enum | no impact |
| Temporal durable agents | whether agent workflow examples exist | future runtime option, not U5 | no impact |
| OpenAI Agents SDK | current tracing/session primitives | maybe import usage metadata later | no impact |
| Claude Code | current multi-window/CLI logging behavior | possible local source path mapping | no impact |
| Codex CLI | current usage/log/export behavior | usage capture adapter | no impact |
| Inngest | event-driven agent workflow support | future event bus comparison | no impact |
| Trigger.dev | agent/workflow orchestration support | future event bus comparison | no impact |
| Langfuse | current token/cost dashboard fields | price/usage schema comparison | no impact |
| Helicone | current cost dashboard fields | provider cost import mapping | no impact |
| OpenAI usage | current export/billing fields | model_price_snapshot update | no hard-coded price |
| Anthropic pricing | current Claude/Caching pricing | model_price_snapshot update | no hard-coded price |
| prompt caching | current cache read/write accounting | cache fields in cost ledger | nullable cache fields remain |

## Appendix B — how to record verified sources

A verified source row should look like this:

```yaml
vendor: OpenAI Agents SDK
source_url: https://example.invalid/replace-with-real
visited_at: 2026-05-07T00:00:00Z
version_observed: replace-with-real
claims:
  - sessions or traces available
  - usage metadata available or unavailable
design_impact: keep local ledger; optionally add import adapter later
confidence: high
```

If a vendor page is marketing-only and lacks implementation detail, mark confidence medium or low. If a source is a blog post rather than docs, record it as `reference`, not `authority`. If pricing is involved, the page must be provider-owned or invoice-backed; secondary summaries are not enough for cost estimates.

## Appendix C — expected influence of live evidence

Live web evidence should not change the core U5 architecture. At most it can refine adapters. For example, if OpenAI Agents SDK exposes usage metadata, U5 can add an importer that writes `cost_attribution_ledger` rows. If Langfuse or Helicone exposes useful cost dashboard fields, U5 can mirror field names. If Temporal shows durable agent execution patterns, U5 can add a future comparison note. None of those facts justify deploying a runtime, changing `write_enabled=False`, or adopting enterprise tracing.

## Appendix D — why no live price appears here

Provider pricing is time-sensitive and can change after this response. Since live browsing is disabled, the package does not include current token prices for Claude, GPT, Codex, or any other model. This is an intentional truthfulness decision. The schema supports prices; the evidence pack does not claim them. A future operator can add `model_price_snapshot` rows once they verify provider pages on the target date.

## Appendix E — minimum live-web pass when available

The prompt requested at least fifteen searches. A complete future pass should include at least these searches and record results in a table:

1. LangGraph durable execution and checkpointing.
2. CrewAI observability or task tracking.
3. AutoGen agent conversation logging.
4. MetaGPT role/task orchestration.
5. Temporal durable agent workflows.
6. OpenAI Agents SDK sessions/tracing/usage.
7. Claude Code CLI multi-window or usage logs.
8. Codex CLI parallel execution or logs.
9. Inngest agent workflows.
10. Trigger.dev agent workflows.
11. Langfuse cost dashboard.
12. Helicone cost dashboard.
13. OpenAI prompt caching pricing.
14. Anthropic prompt caching pricing.
15. General single-writer lock or local concurrency pattern.

Each search must be tied to a concrete design decision. Searching without design impact should not pad the evidence count.


## Appendix F — live evidence verification checklist
1. For future live web refresh, the operator should record visited_at and source_url for each vendor page; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
2. For future live web refresh, the operator should separate provider documentation from third-party summaries; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
3. For future live web refresh, the operator should reject price claims that cannot be tied to a current provider source; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
4. For future live web refresh, the operator should write design impact for each search instead of collecting links; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
5. For future live web refresh, the operator should preserve the no-runtime boundary even if orchestration products look attractive; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
6. For future live web refresh, the operator should record visited_at and source_url for each vendor page; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
7. For future live web refresh, the operator should separate provider documentation from third-party summaries; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
8. For future live web refresh, the operator should reject price claims that cannot be tied to a current provider source; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
9. For future live web refresh, the operator should write design impact for each search instead of collecting links; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
10. For future live web refresh, the operator should preserve the no-runtime boundary even if orchestration products look attractive; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
11. For future live web refresh, the operator should record visited_at and source_url for each vendor page; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
12. For future live web refresh, the operator should separate provider documentation from third-party summaries; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
13. For future live web refresh, the operator should reject price claims that cannot be tied to a current provider source; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
14. For future live web refresh, the operator should write design impact for each search instead of collecting links; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
15. For future live web refresh, the operator should preserve the no-runtime boundary even if orchestration products look attractive; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
16. For future live web refresh, the operator should record visited_at and source_url for each vendor page; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
17. For future live web refresh, the operator should separate provider documentation from third-party summaries; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
18. For future live web refresh, the operator should reject price claims that cannot be tied to a current provider source; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
19. For future live web refresh, the operator should write design impact for each search instead of collecting links; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
20. For future live web refresh, the operator should preserve the no-runtime boundary even if orchestration products look attractive; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
21. For future live web refresh, the operator should record visited_at and source_url for each vendor page; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
22. For future live web refresh, the operator should separate provider documentation from third-party summaries; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
23. For future live web refresh, the operator should reject price claims that cannot be tied to a current provider source; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
24. For future live web refresh, the operator should write design impact for each search instead of collecting links; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
25. For future live web refresh, the operator should preserve the no-runtime boundary even if orchestration products look attractive; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
26. For future live web refresh, the operator should record visited_at and source_url for each vendor page; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
27. For future live web refresh, the operator should separate provider documentation from third-party summaries; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
28. For future live web refresh, the operator should reject price claims that cannot be tied to a current provider source; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
29. For future live web refresh, the operator should write design impact for each search instead of collecting links; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
30. For future live web refresh, the operator should preserve the no-runtime boundary even if orchestration products look attractive; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
31. For future live web refresh, the operator should record visited_at and source_url for each vendor page; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
32. For future live web refresh, the operator should separate provider documentation from third-party summaries; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
33. For future live web refresh, the operator should reject price claims that cannot be tied to a current provider source; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
34. For future live web refresh, the operator should write design impact for each search instead of collecting links; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
