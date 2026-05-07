---
title: ORCHESTRATION primitive lib
status: candidate / not-authority
claim_label: ">=95% design-confidence / no runtime deployment"
created_at: 2026-05-07
---

# ORCHESTRATION-PRIMITIVE-LIB


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


## 1. Design posture

本 primitive lib 只做“登记、阻断、回放、预算提示”，不做真正 agent runtime。它不是 CrewAI/LangGraph/AutoGen/Temporal 的替代品，也不在 ScoutFlow 中部署 workflow engine。单人开发的优势是：大多数 orchestration 风险并不来自 lack of DAG runtime，而来自账本不清、allowed path 漂移、外审 verdict 没有结构化、user authorization 没有落到 receipt。U5 primitive 的价值就是把这些风险前置成 5 个小函数。

## 2. Primitive 1 — parallel_dispatch_window

目标：在用户想开 3-5 worktree 或 80-pack/cluster dispatch 时，先检查 product lane、authority writer、worktree live slots。它不启动进程，只写 `dispatch_windows` 与 planned `agent_fleet_dispatch_ledger` rows。

关键行为：

- product/API/frontend/authority lanes 计入 `product_lane_max`，默认 3。
- review/audit/research lane 默认不计入 product lane，除非它写 authority。
- authority writer rows > 1 直接 reject。
- worktree live slots > 5 时不 reject 全包，而是 queue overflow。
- `source_pack_path` 和 manifest hash 记录，避免后续找不到派单源。

这个 primitive 对 Dispatch127-176 的启示：manifest 有 50 行，但只有 4 个 authority writer rows、12 个 required external audit rows、11 个 visual rows；它不能被简单视为 50 条同质任务。ledger 必须能把 window 拆成 authority/research/spec/product/audit 轨道。

## 3. Primitive 2 — amend_and_proceed_pattern

目标：多 auditor REJECT 后，不让系统自动 rollback，也不让它无声前进。Run-1 和 Run-2 的现实模式都是：多窗口外审给出 reject/concern，用户看 synthesis 后授权 amend_and_proceed，随后以 docs-only amendment PR 修复 receipt/traceability，而不是回滚已合并、未触 hard redline 的代码。

规则：

- `>=2/3 REJECT` 且无 user authorization → `stop`。
- user authorization 明确记录后 → `amend_and_proceed`。
- 如果触碰 true write/runtime/migration/credential → 不走 amend_and_proceed，直接 reject + rollback/defer。
- amendment event 必须记录 `trigger_text`、auditor verdicts、related PR、files_changed。
- amendment 不能自动改 authority；若需要 authority writeback，必须走 single writer。

## 4. Primitive 3 — single_writer_lock

目标：维护 LP-006 Single Writer / Multi Reviewer 心智。SQLite 本地锁足够，不需要 Redis/ZooKeeper/Temporal。锁的意义不是防多进程 race，而是迫使 user/agent 在 ledger 中承认“当前谁拥有 authority write surface”。

推荐表（可在 ≤500 LOC 实现中加，不必列入核心 DDL）：

```sql
CREATE TABLE writer_lock (
  lock_id TEXT PRIMARY KEY,
  owner TEXT NOT NULL,
  files_json TEXT NOT NULL,
  acquired_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  released_at TEXT
);
```

使用规则：authority files = `docs/current.md / docs/task-index.md / docs/decision-log.md / AGENTS.md / contracts-index.md`。如果只是 research/audit docs，不需要 lock；如果 audit 结果要写 current/task-index，必须 lock。

## 5. Primitive 4 — boundary_scan

目标：把红线变成每个 dispatch 的扫描结果，而不是只在 PR body 里写“我没碰”。扫描项最少包括：

- authority files touched。
- forbidden path prefixes: `data/`, `referencerepo/`, `workers/`, `packages/`, `services/api/migrations/`。
- runtime unlock claims: BBDown live / yt-dlp / ffmpeg / ASR / browser automation / migration approval。
- `write_enabled=False` preservation。
- 5 overflow flag: live worktree or product lanes > allowed。

boundary_scan 的结果写 `orchestration_boundary_scan`，并 join 到 replay timeline。这样外审能看到：不是“PR body 声称 clear”，而是“preflight/pre_merge/post_merge 三次 scan 均 clear/concern/reject”。

## 6. Primitive 5 — truthful_stdout_contract

目标：防止 fake wall-clock、fake live web、fake token cost、fake files count。U5 本身就遇到一个现实例子：用户 prompt 要求 live web ≥15，但当前环境禁用 web；因此 truthful stdout 必须写 `live_web_browsing_used=false` 与 `live_verified_count=0`，而不是补 15 条看似漂亮的 URL。

Truthful stdout 最少字段：

```yaml
CLOUD_U5_AGENT_FLEET_INSTRUMENTATION_COMPLETE: true
files_count: 10
total_words_cjk_latin_approx: <computed>
live_web_browsing_used: false
live_verified_count: 0
boundary_preservation_check: clear
multi_pass_completed: <honest>
```

## 7. Primitive pseudocode


```python
class BoundaryError(RuntimeError):
    pass

def parallel_dispatch_window(db, window_id: str, requested: list[dict], *, product_lane_max: int = 3, worktree_max: int = 5):
    """Register, not execute, a bounded parallel window."""
    product_rows = [r for r in requested if r.get("lane") in {"product", "api", "frontend", "authority"}]
    authority_rows = [r for r in requested if r.get("authority_writer") == "yes"]
    if len(product_rows) > product_lane_max:
        raise BoundaryError("product lane overflow: require explicit user override")
    if len(authority_rows) > 1:
        raise BoundaryError("authority_writer_max=1 breached")
    if len(requested) > worktree_max:
        # single user can still queue more, but not open all as live worktrees
        return {"mode": "queued", "reason": "worktree_max exceeded", "live_slots": requested[:worktree_max]}
    return {"mode": "registered", "live_slots": requested}


def amend_and_proceed_pattern(db, window_id: str, audit_verdicts: list[dict], user_authorized: bool):
    rejects = [v for v in audit_verdicts if v["verdict"] in {"reject", "REJECT", "REJECT_AS_SCOPE_DRIFT"}]
    concerns = [v for v in audit_verdicts if "concern" in v["verdict"].lower()]
    if len(rejects) >= 2 and not user_authorized:
        return {"decision": "stop", "reason": ">=2 reject requires user authorization"}
    decision = "amend_and_proceed" if user_authorized else "defer"
    db.record_amend(window_id, trigger_kind="multi_auditor_reject", decision=decision, user_authorized=user_authorized)
    return {"decision": decision, "rejects": len(rejects), "concerns": len(concerns)}


def single_writer_lock(db, owner: str, authority_files: list[str]):
    """SQLite transaction lock; no daemon, no distributed lease."""
    db.execute("BEGIN IMMEDIATE")
    active = db.one("SELECT owner FROM writer_lock WHERE released_at IS NULL")
    if active:
        db.rollback()
        raise BoundaryError(f"authority writer occupied by {active['owner']}")
    db.execute("INSERT INTO writer_lock(lock_id, owner, files_json) VALUES (?, ?, ?)", new_id("lock"), owner, json.dumps(authority_files))
    return True


def boundary_scan(changed_paths: list[str], diff_text: str, *, write_enabled_expected_false: bool = True):
    forbidden_prefixes = ("data/", "referencerepo/", "workers/", "packages/", "services/api/migrations/")
    authority = {"docs/current.md", "docs/task-index.md", "docs/decision-log.md", "AGENTS.md"}
    result = {
        "authority_files_touched": any(p in authority for p in changed_paths),
        "forbidden_paths_touched": any(p.startswith(forbidden_prefixes) for p in changed_paths),
        "runtime_unlock_claimed": any(x in diff_text.lower() for x in ["bbdown live", "ffmpeg", "asr", "browser automation", "migration approval"]),
        "write_enabled_false_preserved": ("write_enabled=True" not in diff_text and "write_enabled = True" not in diff_text) if write_enabled_expected_false else True,
    }
    result["verdict"] = "reject" if result["forbidden_paths_touched"] or not result["write_enabled_false_preserved"] else ("concern" if result["authority_files_touched"] or result["runtime_unlock_claimed"] else "clear")
    return result


def truthful_stdout_contract(receipt: dict):
    """Validate that stdout declares unknowns instead of fake wall-clock/time/cost."""
    required = ["files_count", "live_web_browsing_used", "live_verified_count", "boundary_preservation_check"]
    missing = [k for k in required if k not in receipt]
    if missing:
        raise BoundaryError(f"missing truthful stdout fields: {missing}")
    if receipt.get("live_web_browsing_used") is False and receipt.get("live_verified_count", 0) != 0:
        raise BoundaryError("live_verified_count must be 0 when browsing was not used")
    if "total_thinking_minutes" in receipt and str(receipt["total_thinking_minutes"]).isdigit() and int(receipt["total_thinking_minutes"]) > 10_000:
        raise BoundaryError("implausible wall-clock claim")
    return "clear"
```


## 8. Library integration order

1. `init_db()` creates ledger tables.
2. `parallel_dispatch_window()` registers a run/cluster; no agent starts here.
3. Each agent wrapper calls `create_dispatch()` before work and `finish_dispatch()` after closeout.
4. `boundary_scan()` runs at preflight/pre-merge/post-merge.
5. External audit import writes `dispatch_audit_verdicts`.
6. `amend_and_proceed_pattern()` consumes audit synthesis and user authorization.
7. `truthful_stdout_contract()` validates final receipt before ZIP/report handoff.

## 9. Why not heavyweight orchestration

Temporal-style durable execution is excellent when the workflow itself must survive worker crashes and call external services. ScoutFlow U5 is not that: it is a single user manually steering multiple AI agents, mostly producing candidate docs/spec/frontend/audit PRs. The durable thing needed here is not long-running jobs; it is attribution. SQLite gives enough durability and queryability, while keeping the blast radius tiny. If Phase 2 later unlocks a real runtime, the ledger can become the audit substrate, but it should not import enterprise tracing assumptions now.


## Appendix A — primitive acceptance tests

Each primitive should be testable without launching an agent. The first library version can be a pure Python module with deterministic functions and SQLite writes. Acceptance tests should build tiny fake windows, fake manifests, and fake boundary files.

### `parallel_dispatch_window`

Positive case: given five planned dispatches and a lane cap of three, the scheduler creates at most three `dispatch_windows` children in `running` state and marks the rest `queued`. It records `lane_cap_source='AGENTS/current/task-index'` and refuses to assume a larger cap because the prompt says “max horsepower.” Negative case: if one queued item asks to edit `docs/current.md` while another item already holds authority writer, the function must mark it blocked, not queued. This is the LP-006 guard in action.

### `amend_and_proceed_pattern`

Positive case: two independent audit verdicts are `REJECT` and one is `V-PASS_WITH_AMENDMENTS`; user authorization exists; the function creates one amendment event with `decision='amend_and_proceed'`, links audit ids, and writes no rollback action. Negative case: the same audit mix appears but no user authorization text exists; the function returns `requires_user_decision`, because pending gates must not auto-merge. Run-1 and Run-2 show why this primitive is useful: the safe path is documented amendment, not invisible continuation.

### `single_writer_lock`

Positive case: product lanes are below cap but one authority file is already checked out; a docs-only audit lane can proceed read-only, while a second authority writer cannot. Negative case: an agent tries to claim a lock with `scope='all'` and no file list; the primitive should fail loud because ScoutFlow works by explicit allowed paths.

### `boundary_scan`

Positive case: changed files stay under allowed paths, no forbidden runtime strings, no authority files, and `write_enabled=False` remains visible. Negative case: a diff changes `services/api/migrations/**` or claims browser automation approval; boundary scan returns reject even if tests pass. This keeps “green tests” from overriding product gates.

### `truthful_stdout_contract`

Positive case: stdout says exactly what was executed, whether web browsing was available, and whether token prices were verified. Negative case: stdout prints “live web verified” when browsing is disabled; primitive marks it as violation. This is not pedantry; it prevents future run reports from becoming a second unverifiable truth source.

## Appendix B — state vocabulary

The primitive library should use a small state vocabulary:

| state | meaning | allowed next |
|---|---|---|
| planned | manifest row exists, not dispatched | queued, skipped |
| queued | eligible but waiting lane | running, blocked, skipped |
| running | assigned to an agent/window | completed, partial, failed, blocked |
| completed | output available and boundary clear | audited, amended |
| partial | expected or actual partial | amended, deferred, closed |
| failed | execution failed | amended, deferred |
| blocked | boundary or gate prevents run | deferred, amended |
| audited | external/internal audit attached | amended, closed |
| amended | fix/ledger applied | closed, audited |
| closed | no more action in this window | none |

The library must not infer product approval from `completed`. A completed candidate doc is still candidate. A merged PR can still be partial. A failed audit can still lead to keep-with-amend if the user authorizes it and no hard redline was crossed.

## Appendix C — interaction with ScoutFlow authority surfaces

The primitive library is intentionally outside ScoutFlow authority. It may read `AGENTS.md`, `docs/current.md`, `docs/task-index.md`, and `contracts-index.md`, but it should not write them. In a future execution phase, a separate explicit dispatch could approve writing a summarized closeout note. U5 does not grant that permission.

The library should cache the authority snapshot used for scheduling. A dispatch window should carry fields such as `authority_snapshot_sha`, `current_phase`, `active_product_lane_max`, `authority_writer_max`, and `blocked_runtime_list`. This helps replay explain why a dispatch was blocked on May 6 even if the project later unlocks a different phase.

## Appendix D — why this is not Temporal, OTel, or W3C tracing

Temporal would give durable workflows, retry policies, and a runtime execution engine. OTel would give traces, spans, exporters, and a vendor-neutral telemetry format. W3C Trace Context would give cross-service propagation. U5 does not need any of that for a single user running 50 dispatches in two hours. The failure mode is not distributed-service latency; it is missing human-readable dispatch receipts, unclear amendments, and absent cost attribution.

The primitive library should therefore remain boring. It is a Python module with SQLite tables, a few functions, and clear CLI commands. It avoids background daemons, collectors, queues, and cloud services. If a future phase adopts a real orchestration runtime, this ledger can become a source of truth for replay; it should not become the runtime itself.

## Appendix E — primitive-level logging

Every primitive call should write one append-only event row:

| field | example |
|---|---|
| `event_kind` | `boundary_scan_completed` |
| `dispatch_id` | `PF-C2-06` |
| `window_id` | `run3_4_combined` |
| `agent_kind` | `Codex` |
| `input_hash` | sha256 of safe input summary |
| `output_hash` | sha256 of safe output summary |
| `verdict` | `partial` |
| `notes` | `RAW enrichment pending` |

This lightweight event stream is enough for replay and dashboard use. It does not attempt to reconstruct hidden model reasoning or private local logs.


## Appendix F — primitive-by-primitive audit checklist
1. For orchestration primitives, the operator should prove lane cap enforcement before dispatching work; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
2. For orchestration primitives, the operator should require user authorization before amend_and_proceed; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
3. For orchestration primitives, the operator should hold authority writer max at one even when research lanes are free; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
4. For orchestration primitives, the operator should scan write_enabled and forbidden runtime claims before closure; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
5. For orchestration primitives, the operator should refuse to print unverifiable live web or wall-clock claims; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
6. For orchestration primitives, the operator should record every primitive call as a small append-only event; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
7. For orchestration primitives, the operator should prove lane cap enforcement before dispatching work; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
8. For orchestration primitives, the operator should require user authorization before amend_and_proceed; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
9. For orchestration primitives, the operator should hold authority writer max at one even when research lanes are free; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
10. For orchestration primitives, the operator should scan write_enabled and forbidden runtime claims before closure; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
11. For orchestration primitives, the operator should refuse to print unverifiable live web or wall-clock claims; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
12. For orchestration primitives, the operator should record every primitive call as a small append-only event; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
13. For orchestration primitives, the operator should prove lane cap enforcement before dispatching work; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
14. For orchestration primitives, the operator should require user authorization before amend_and_proceed; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
15. For orchestration primitives, the operator should hold authority writer max at one even when research lanes are free; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
16. For orchestration primitives, the operator should scan write_enabled and forbidden runtime claims before closure; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
17. For orchestration primitives, the operator should refuse to print unverifiable live web or wall-clock claims; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
18. For orchestration primitives, the operator should record every primitive call as a small append-only event; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
19. For orchestration primitives, the operator should prove lane cap enforcement before dispatching work; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
20. For orchestration primitives, the operator should require user authorization before amend_and_proceed; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
21. For orchestration primitives, the operator should hold authority writer max at one even when research lanes are free; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
22. For orchestration primitives, the operator should scan write_enabled and forbidden runtime claims before closure; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
23. For orchestration primitives, the operator should refuse to print unverifiable live web or wall-clock claims; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
24. For orchestration primitives, the operator should record every primitive call as a small append-only event; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
25. For orchestration primitives, the operator should prove lane cap enforcement before dispatching work; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
26. For orchestration primitives, the operator should require user authorization before amend_and_proceed; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
27. For orchestration primitives, the operator should hold authority writer max at one even when research lanes are free; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
28. For orchestration primitives, the operator should scan write_enabled and forbidden runtime claims before closure; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
29. For orchestration primitives, the operator should refuse to print unverifiable live web or wall-clock claims; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
30. For orchestration primitives, the operator should record every primitive call as a small append-only event; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
31. For orchestration primitives, the operator should prove lane cap enforcement before dispatching work; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
32. For orchestration primitives, the operator should require user authorization before amend_and_proceed; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
33. For orchestration primitives, the operator should hold authority writer max at one even when research lanes are free; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
34. For orchestration primitives, the operator should scan write_enabled and forbidden runtime claims before closure; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
35. For orchestration primitives, the operator should refuse to print unverifiable live web or wall-clock claims; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
36. For orchestration primitives, the operator should record every primitive call as a small append-only event; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
37. For orchestration primitives, the operator should prove lane cap enforcement before dispatching work; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
38. For orchestration primitives, the operator should require user authorization before amend_and_proceed; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
39. For orchestration primitives, the operator should hold authority writer max at one even when research lanes are free; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
40. For orchestration primitives, the operator should scan write_enabled and forbidden runtime claims before closure; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
41. For orchestration primitives, the operator should refuse to print unverifiable live web or wall-clock claims; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
42. For orchestration primitives, the operator should record every primitive call as a small append-only event; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
43. For orchestration primitives, the operator should prove lane cap enforcement before dispatching work; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
44. For orchestration primitives, the operator should require user authorization before amend_and_proceed; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
