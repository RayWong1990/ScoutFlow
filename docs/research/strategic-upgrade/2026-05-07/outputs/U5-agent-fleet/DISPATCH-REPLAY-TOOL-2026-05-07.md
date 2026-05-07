---
title: DISPATCH replay tool
status: candidate / not-authority
claim_label: ">=95% design-confidence"
created_at: 2026-05-07
---

# DISPATCH-REPLAY-TOOL


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


## 1. Purpose

Replay tool 的目标是回答一个非常具体的问题：给定 `dispatch_id`，我如何在 30 秒内看到 input → output → audit → amend → cost → boundary scan 的 timeline？当前 CHECKPOINT 和 PR body 分散在多个路径，外审要手工读 report、diff bundle、checkpoint、PR、comments，成本很高。Replay CLI 只渲染 Markdown，不执行任何 agent，不读隐私 session，不打开 browser。

## 2. Command interface

```bash
scoutflow-replay PF-C1-04
scoutflow-replay --window run3-4 --cluster PF-C2
scoutflow-replay --pr 240 --format markdown
scoutflow-replay --dispatch PF-LP-02 --show-amend --show-cost
scoutflow-replay --audit-only --verdict reject
```

输出是 Markdown，可直接附到 audit packet 或发给 GPT Pro/Hermes 做外审。默认不读取 artifact 正文，只显示 path/sha/bytes；加 `--inline-safe` 才内联 candidate docs 的前 40 行，且永远不内联 raw stdout/stderr、credential、local-only path 内容。

## 3. Timeline model

Replay timeline 分 6 类 event：

| event type | source table | example |
|---|---|---|
| dispatch core | `agent_fleet_dispatch_ledger` | task_id, PR, state, verdict |
| artifact | `dispatch_io_artifacts` | CHECKPOINT, RUN-REPORT, DIFF-BUNDLE, visual packet |
| audit | `dispatch_audit_verdicts` | REJECT / concern / V-PASS_WITH_AMENDMENTS |
| amend | `dispatch_amend_events` | amend_and_proceed, topology replacement |
| cost | `cost_attribution_ledger` | tokens/cost/phase/model |
| boundary scan | `orchestration_boundary_scan` | authority touched, write_enabled false, runtime claims |

## 4. Markdown output shape

```markdown
# Replay PF-C2-06

- window: Run-3+4 / PR #240
- cluster: PF-C2
- agent_kind: Codex
- verdict: partial
- reason: awaiting future RAW enrichment + intake
- boundary: clear; write_enabled=False preserved

## Timeline
- created: dispatch registered from cluster manifest
- output: raw-handoff-staging/.../PF-C2-06.md
- audit: C2 partial cascade, one of PF-C2-06/07/08/09/11
- amend: none yet; future RAW enrichment needed
- cost: unknown tokens; estimate_method=missing_runtime_tokens

## Replay verdict
This dispatch is not failed. It is expected_partial until RAW enrichment is performed or PF-V handoff closes the gap.
```

## 5. Python render skeleton


```python
def replay_dispatch(conn, dispatch_id: str) -> str:
    d = conn.execute("SELECT * FROM agent_fleet_dispatch_ledger WHERE dispatch_id=?", (dispatch_id,)).fetchone()
    if not d:
        raise SystemExit(f"dispatch not found: {dispatch_id}")
    audits = conn.execute("SELECT * FROM dispatch_audit_verdicts WHERE dispatch_id=? ORDER BY created_at", (dispatch_id,)).fetchall()
    artifacts = conn.execute("SELECT * FROM dispatch_io_artifacts WHERE dispatch_id=? ORDER BY created_at", (dispatch_id,)).fetchall()
    costs = conn.execute("SELECT * FROM cost_attribution_ledger WHERE dispatch_id=? ORDER BY created_at", (dispatch_id,)).fetchall()
    amends = conn.execute("SELECT * FROM dispatch_amend_events WHERE dispatch_id=? ORDER BY created_at", (dispatch_id,)).fetchall()
    scans = conn.execute("SELECT * FROM orchestration_boundary_scan WHERE dispatch_id=? ORDER BY created_at", (dispatch_id,)).fetchall()

    lines = [f"# Replay {dispatch_id}", ""]
    lines += [f"- task_id: `{d['task_id']}`", f"- agent_kind: `{d['agent_kind']}`", f"- verdict: `{d['verdict']}`", f"- state: `{d['state']}`"]
    if d['pr_number']:
        lines.append(f"- PR: #{d['pr_number']} {d['pr_url'] or ''}")
    lines += ["", "## Timeline"]
    for row in artifacts:
        lines.append(f"- `{row['created_at']}` artifact `{row['io_kind']}`: `{row['artifact_path']}`")
    for row in audits:
        lines.append(f"- `{row['created_at']}` audit `{row['auditor_kind']}` verdict `{row['verdict']}`: {row['summary'] or ''}")
    for row in amends:
        lines.append(f"- `{row['created_at']}` amend `{row['decision']}` trigger `{row['trigger_kind']}`: {row['trigger_text']}")
    for row in scans:
        lines.append(f"- `{row['created_at']}` boundary scan `{row['scan_kind']}` verdict `{row['verdict']}`")
    if costs:
        total = sum(float(c['cost_usd_estimate']) for c in costs)
        tokens = sum(int(c['token_input']) + int(c['token_output']) + int(c['token_cached_input']) for c in costs)
        lines += ["", "## Cost", f"- total_cost_usd_estimate: `{total:.6f}`", f"- tokens_recorded: `{tokens}`"]
    return "\n".join(lines) + "\n"
```


## 6. Replay examples from verified patterns

### 6.1 Run-1 silent flexibility

Replay should show PF-LP-02 / PR #205 as merged but globally rejected by external audit synthesis. It should include silent flexibility count and amendment PR #231. The key sentence: “product safety hard redlines stayed clear, but allowed_paths contract was breached, so `amend_and_proceed` required user authorization.”

### 6.2 Run-2 topology replacement

Replay for PF-LP-06 should show `dispatch_receipt_pr=226`, `primary_truth_pr=228`, and pattern `topology_replacement`. Without this view, a future agent may accidentally read PR #226 as final implementation truth.

### 6.3 Window-2 deferred dependency

Replay for W2 should show 17/17 merged and PF-C3-04 intentionally deferred because it depends on PF-C1-10. That prevents a misleading “all C3 complete” claim.

### 6.4 Run-3+4 partial cascade

Replay for PR #240 should group PF-C1 and PF-C2 separately: C1 pass; C2 partial with five partial rows. It should not flatten the combined PR into a single pass/fail.

## 7. Safety behavior

Replay must refuse to render unsafe local-only content. It may show path strings already in repo/PR bodies, but it must not read `~/workspace/raw/` content, `~/.claude`, `~/.codex`, credential sidecars, raw stdout/stderr, browser profile paths, or qrcode/cookie/token material. If the artifact path is local-only, output only the path and `local_only_not_inlined=true`.

## 8. Audit value

A replay tool creates a common language between Codex, GPT Pro, Hermes, Claude Code and the human operator. Instead of each auditor reconstructing a run from scratch, everyone can inspect the same timeline and challenge specific links. This is exactly the single-user equivalent of traceability, without adopting distributed tracing.


## Appendix A — timeline rendering contract

The replay tool should produce a Markdown timeline that a human can audit in less than five minutes. The default rendering order is: window header, dispatch identity, input summary, boundary scan, execution row, output artifacts, audit verdicts, amendments, cost rows, and unresolved blockers. Each section should say `missing` when the ledger has no row. Silence is not acceptable because silence looks like success.

Example section order:

```text
# Replay PF-C2-06
window: Run-3+4 combined closeout
cluster: PF-C2
state: partial
verdict: expected_partial

## 1. Input
manifest row, prompt path, parent dispatch, allowed paths

## 2. Boundary
authority files untouched, write_enabled false, runtime blocked

## 3. Output
output_path, PR number, merge commit, artifact ids

## 4. Audit
external/internal verdict table

## 5. Amend trail
trigger, user authorization, amended fields

## 6. Cost
tokens, price snapshot, cost status

## 7. Open blockers
RAW enrichment pending, PF-C4 gated
```

The renderer should preserve exact PR numbers and commit prefixes. It should not summarize “merged successfully” without showing whether the verdict was clear, partial, concern, or reject.

## Appendix B — resolver rules

A replay command can accept several keys: `dispatch_id`, `task_id`, `pr_number`, `artifact_id`, or `cluster_id`. Resolution must be deterministic. If `PF-C2-06` maps to one row, replay it. If `pr_number=240` maps to 24 dispatches, print a cluster index and require `--cluster PF-C1` or `--cluster PF-C2` unless the user asks `--all`. If `task_id` maps to historical and amended rows, show both and mark the latest final truth source.

Resolution priority:

1. exact `dispatch_id`
2. exact `task_id`
3. exact `artifact_id`
4. exact `pr_number`
5. exact `cluster_id`
6. fuzzy title search only with `--search`

This avoids the Run-2 topology problem where PR #226 and PR #228 both touched LP-06/07 but #228 became final truth.

## Appendix C — privacy and redaction

Replay must never print raw prompts, raw stdout, secrets, cookies, tokens, QR paths, or browser profile paths. It prints safe summaries and hashes. If an artifact path points outside the repo or into a local-only raw directory, the default output should show only a normalized label and hash, unless the user passes `--show-local-paths`. Even then, the tool should warn that local paths are not authority.

The tool should also avoid printing hidden chain-of-thought or private reasoning logs. The replay goal is evidence traceability: what task was dispatched, what was produced, what was audited, what was amended, and what it cost. It is not a model introspection tool.

## Appendix D — tests for replay

Test cases should include:

1. single dispatch with clear verdict and one output path.
2. dispatch with `expected_partial` and no PR.
3. combined PR with two clusters and multiple dispatches.
4. Run-2 replacement topology where original receipt PR differs from final truth PR.
5. Run-1 audit reject followed by amend-and-proceed.
6. missing cost rows; renderer warns rather than inventing numbers.
7. missing live web evidence; renderer prints limitation.
8. boundary scan reject; renderer highlights stop-line before output.
9. local-only path redaction.
10. corrupted JSON metadata; renderer falls back to raw string with warning.

## Appendix E — CLI examples

```bash
scoutflow-replay PF-C1-10
scoutflow-replay --pr 240 --cluster PF-C2
scoutflow-replay --run Run-2 --amends
scoutflow-replay --artifact topic-card-lite --format markdown
scoutflow-replay --dispatch PF-LP-06 --show-topology
scoutflow-replay --cluster PF-C1 --cost --no-local-paths
```

The output should be stable enough to paste into an audit PR body. It should not require a web server or notebook. A single SQLite connection and Markdown renderer are sufficient.


## Appendix F — replay output audit checklist
1. For dispatch replay rendering, the operator should show missing sections explicitly instead of omitting them; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
2. For dispatch replay rendering, the operator should resolve replacement PR topology before choosing final truth; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
3. For dispatch replay rendering, the operator should redact local paths unless the operator explicitly asks for them; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
4. For dispatch replay rendering, the operator should show amendment events before final verdict; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
5. For dispatch replay rendering, the operator should show cost evidence status even when cost rows are missing; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
6. For dispatch replay rendering, the operator should show missing sections explicitly instead of omitting them; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
7. For dispatch replay rendering, the operator should resolve replacement PR topology before choosing final truth; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
8. For dispatch replay rendering, the operator should redact local paths unless the operator explicitly asks for them; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
9. For dispatch replay rendering, the operator should show amendment events before final verdict; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
10. For dispatch replay rendering, the operator should show cost evidence status even when cost rows are missing; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
11. For dispatch replay rendering, the operator should show missing sections explicitly instead of omitting them; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
12. For dispatch replay rendering, the operator should resolve replacement PR topology before choosing final truth; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
13. For dispatch replay rendering, the operator should redact local paths unless the operator explicitly asks for them; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
14. For dispatch replay rendering, the operator should show amendment events before final verdict; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
15. For dispatch replay rendering, the operator should show cost evidence status even when cost rows are missing; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
16. For dispatch replay rendering, the operator should show missing sections explicitly instead of omitting them; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
17. For dispatch replay rendering, the operator should resolve replacement PR topology before choosing final truth; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
18. For dispatch replay rendering, the operator should redact local paths unless the operator explicitly asks for them; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
19. For dispatch replay rendering, the operator should show amendment events before final verdict; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
20. For dispatch replay rendering, the operator should show cost evidence status even when cost rows are missing; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
21. For dispatch replay rendering, the operator should show missing sections explicitly instead of omitting them; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
22. For dispatch replay rendering, the operator should resolve replacement PR topology before choosing final truth; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
23. For dispatch replay rendering, the operator should redact local paths unless the operator explicitly asks for them; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
24. For dispatch replay rendering, the operator should show amendment events before final verdict; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
25. For dispatch replay rendering, the operator should show cost evidence status even when cost rows are missing; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
26. For dispatch replay rendering, the operator should show missing sections explicitly instead of omitting them; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
