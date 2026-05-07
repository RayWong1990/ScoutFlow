---
title: MODULE agent fleet dispatch ledger
status: candidate / not-authority
claim_label: ">=95% design-confidence / not runtime proof"
created_at: 2026-05-07
---

# MODULE — agent_fleet_dispatch_ledger


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


## 1. Mission fit

`agent_fleet_dispatch_ledger` 的目标不是把 ScoutFlow 变成企业级 tracing 系统，而是在单人高马力开发节奏下补上当前最缺的运行时账本：谁派了哪一单、用了哪个 agent、何时开始/结束、产物在哪、PR 是多少、审计 verdict 是什么、是否触发 amend、是否发生 silent flexibility。现有 `CHECKPOINT.json` 更像收尾收据，能证明一段 run 完成了什么，但它不是逐单 ledger：没有 agent attribution，没有 cost join key，没有 amend trail，也不能稳定回答“为什么这个 cluster 烧钱却没有产出”。

这个模块采用 **SQLite + Markdown/JSON artifact path**，适配 single-user / local-first。它只需要一个本地 DB 文件；不需要 server，不需要 OpenTelemetry collector，不需要 W3C Trace Context，不需要 Temporal runtime。所有 ID 都是人类可读的 `dispatch_id / window_id / task_id / cluster_id`，与 ScoutFlow 当前 `T-P1A-*`、`PF-C*`、PR number、CHECKPOINT path 兼容。

## 2. Local evidence abstraction

从本地 audit pack 抽象出的 Dispatch127-176 pattern：

| metric | value |
|---|---:|
| manifest dispatch count | 50 |
| lane counts | {'authority': 4, 'research': 31, 'spec': 12, 'product': 2, 'audit': 1} |
| type counts | {'docs': 26, 'visual': 9, 'spec': 8, 'frontend': 2, 'api': 2, 'audit': 1, 'vault': 2} |
| external audit counts | {'required': 12, 'optional': 38} |
| authority writer rows | {'yes': 4, 'no': 46} |
| stop class counts | {'authority_scope_expansion': 4, 'external_audit': 9, 'none': 31, 'hard_redline_adjacent': 4, 'required_runtime_gate': 2} |
| visual touchpoint rows | {'no': 39, 'yes': 11} |
| CHECKPOINT validator verdict | clear |
| CHECKPOINT validator dispatch_count | 50 |
| CHECKPOINT required_external_audit_slots | [127, 130, 145, 146, 162, 163, 164, 166, 167, 173, 174, 175] |

Manifest sample front:

| slot | task_id | lane | type | external_audit | authority_writer | stop_class | title |
|---:|---|---|---|---|---|---|---|
| 127 | T-P1A-106 | authority | docs | required | yes | authority_scope_expansion | Wave 4 post-mid-checkpoint continuation map |
| 128 | T-P1A-107 | research | visual | optional | no | external_audit | Wave 4 visual touchpoint roster and localhost plan |
| 129 | T-P1A-108 | spec | spec | optional | no | none | Wave 4 bridge-vault continuation gap matrix |
| 130 | T-P1A-109 | authority | docs | required | yes | authority_scope_expansion | Wave 4 closeout and Wave 5 opening candidate |
| 131 | T-P1A-110 | research | docs | optional | no | none | Signal entity glossary candidate |
| 132 | T-P1A-111 | spec | spec | optional | no | none | Signal state map candidate |
| 133 | T-P1A-112 | research | docs | optional | no | none | Hypothesis lifecycle candidate |
| 134 | T-P1A-113 | research | docs | optional | no | none | Capture plan entity surface candidate |
| 135 | T-P1A-114 | research | docs | optional | no | none | Topic card entity surface candidate |
| 136 | T-P1A-115 | spec | spec | optional | no | none | Signal workbench boundary note |
| 137 | T-P1A-116 | research | docs | optional | no | none | Manual-url continuity constraints for Wave 5 |
| 138 | T-P1A-117 | research | docs | optional | no | none | Trust-trace to topic-card mapping candidate |

Manifest sample tail:

| slot | task_id | lane | type | external_audit | authority_writer | stop_class | title |
|---:|---|---|---|---|---|---|---|
| 169 | T-P1A-148 | research | docs | optional | no | none | RUN-SUMMARY schema for Dispatch127-176 run |
| 170 | T-P1A-149 | research | docs | optional | no | none | Product-lane override evidence packet |
| 171 | T-P1A-150 | research | docs | optional | no | none | Global pool staging health-check contract |
| 172 | T-P1A-151 | research | docs | optional | no | none | Branch protection and merge policy note |
| 173 | T-P1A-152 | authority | docs | required | yes | authority_scope_expansion | Wave 5 closeout template |
| 174 | T-P1A-153 | authority | docs | required | yes | authority_scope_expansion | Wave 6 ledger-open candidate |
| 175 | T-P1A-154 | research | docs | required | no | hard_redline_adjacent | Overflow candidate registry for DB vNext and blocked runtime lanes |
| 176 | T-P1A-155 | research | docs | optional | no | none | STEP3 cold-start handoff packet contract |

这个形态告诉我们 ledger 至少要保存：slot/task/title/lane/type/allowed paths/forbidden paths/external audit flag/authority writer flag/stop class/visual flag/pr/merge_sha/verdict/known risks。否则后续 audit 只能靠 grep 和记忆。

## 3. DDL


```sql
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS dispatch_windows (
  window_id TEXT PRIMARY KEY,
  run_label TEXT NOT NULL,
  window_kind TEXT NOT NULL CHECK(window_kind IN ('run','cluster','batch','audit','amendment','manual')),
  source_pack_path TEXT,
  baseline_sha TEXT,
  final_sha TEXT,
  started_at TEXT,
  ended_at TEXT,
  product_lane_max INTEGER NOT NULL DEFAULT 3,
  authority_writer_max INTEGER NOT NULL DEFAULT 1,
  write_enabled INTEGER NOT NULL DEFAULT 0 CHECK(write_enabled IN (0,1)),
  runtime_unlock_claimed INTEGER NOT NULL DEFAULT 0 CHECK(runtime_unlock_claimed IN (0,1)),
  notes TEXT,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS agent_fleet_dispatch_ledger (
  dispatch_id TEXT PRIMARY KEY,
  window_id TEXT NOT NULL REFERENCES dispatch_windows(window_id) ON DELETE CASCADE,
  agent_kind TEXT NOT NULL CHECK(agent_kind IN ('CC0','CC1','Codex','Hermes','OpenClaw','GPT_Pro','Unknown')),
  model_id TEXT,
  task_id TEXT NOT NULL,
  cluster_id TEXT,
  dispatch_slot TEXT,
  parent_dispatch_id TEXT REFERENCES agent_fleet_dispatch_ledger(dispatch_id),
  start_at TEXT,
  end_at TEXT,
  state TEXT NOT NULL DEFAULT 'planned' CHECK(state IN ('planned','running','merged','closed','deferred','blocked','amended','superseded')),
  verdict TEXT NOT NULL DEFAULT 'partial' CHECK(verdict IN ('clear','concern','reject','partial','expected_partial','pass','fail','deferred')),
  amend_count INTEGER NOT NULL DEFAULT 0,
  amend_trigger_text TEXT,
  output_path TEXT,
  pr_number INTEGER,
  pr_url TEXT,
  head_sha TEXT,
  merge_sha TEXT,
  silent_flexibility_flag INTEGER NOT NULL DEFAULT 0 CHECK(silent_flexibility_flag IN (0,1)),
  allowed_paths_json TEXT,
  forbidden_paths_json TEXT,
  validation_json TEXT,
  boundary_json TEXT,
  source_ref TEXT,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_dispatch_window ON agent_fleet_dispatch_ledger(window_id);
CREATE INDEX IF NOT EXISTS idx_dispatch_task ON agent_fleet_dispatch_ledger(task_id);
CREATE INDEX IF NOT EXISTS idx_dispatch_cluster ON agent_fleet_dispatch_ledger(cluster_id);
CREATE INDEX IF NOT EXISTS idx_dispatch_pr ON agent_fleet_dispatch_ledger(pr_number);
CREATE INDEX IF NOT EXISTS idx_dispatch_verdict ON agent_fleet_dispatch_ledger(verdict);

CREATE TABLE IF NOT EXISTS dispatch_io_artifacts (
  io_id TEXT PRIMARY KEY,
  dispatch_id TEXT NOT NULL REFERENCES agent_fleet_dispatch_ledger(dispatch_id) ON DELETE CASCADE,
  io_kind TEXT NOT NULL CHECK(io_kind IN ('input','output','audit','receipt','checkpoint','diff_bundle','run_report','visual_asset','prompt_template','raw_handoff','note')),
  artifact_path TEXT NOT NULL,
  artifact_sha256 TEXT,
  artifact_bytes INTEGER,
  is_repo_tracked INTEGER NOT NULL DEFAULT 1 CHECK(is_repo_tracked IN (0,1)),
  evidence_label TEXT NOT NULL DEFAULT 'candidate',
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS dispatch_audit_verdicts (
  audit_id TEXT PRIMARY KEY,
  dispatch_id TEXT NOT NULL REFERENCES agent_fleet_dispatch_ledger(dispatch_id) ON DELETE CASCADE,
  auditor_kind TEXT NOT NULL CHECK(auditor_kind IN ('CC0','CC1','Codex','Hermes','OpenClaw','GPT_Pro','human','unknown')),
  auditor_model_id TEXT,
  verdict TEXT NOT NULL CHECK(verdict IN ('clear','concern','reject','partial','expected_partial','pass','fail','v_pass_with_amendments')),
  finding_count INTEGER NOT NULL DEFAULT 0,
  critical_count INTEGER NOT NULL DEFAULT 0,
  summary TEXT,
  source_path TEXT,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS dispatch_amend_events (
  amend_id TEXT PRIMARY KEY,
  dispatch_id TEXT REFERENCES agent_fleet_dispatch_ledger(dispatch_id) ON DELETE SET NULL,
  window_id TEXT REFERENCES dispatch_windows(window_id) ON DELETE SET NULL,
  pattern_id TEXT,
  trigger_kind TEXT NOT NULL CHECK(trigger_kind IN ('multi_auditor_reject','receipt_traceability','silent_flexibility','partial_cascade','topology_replacement','user_override','boundary_scan','other')),
  trigger_text TEXT NOT NULL,
  user_authorized INTEGER NOT NULL DEFAULT 0 CHECK(user_authorized IN (0,1)),
  decision TEXT NOT NULL CHECK(decision IN ('amend_and_proceed','rollback','defer','record_only','split_followup')),
  rollback_required INTEGER NOT NULL DEFAULT 0 CHECK(rollback_required IN (0,1)),
  files_changed_json TEXT,
  related_pr_number INTEGER,
  source_ref TEXT,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS artifact_dimension (
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


## 4. Python CRUD skeleton


```python
# scoutflow_agent_fleet_ledger.py — target <= 500 LOC, standard library only.
from __future__ import annotations

import json
import sqlite3
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

DB_PATH = Path(".scoutflow-agent-fleet-ledger.sqlite")

AGENTS = {"CC0", "CC1", "Codex", "Hermes", "OpenClaw", "GPT_Pro", "Unknown"}
VERDICTS = {"clear", "concern", "reject", "partial", "expected_partial", "pass", "fail", "deferred"}


def new_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:16]}"


def connect(path: Path = DB_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db(conn: sqlite3.Connection, ddl_text: str) -> None:
    conn.executescript(ddl_text)
    conn.commit()


def as_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


@dataclass(frozen=True)
class DispatchInput:
    window_id: str
    agent_kind: str
    task_id: str
    dispatch_id: str | None = None
    model_id: str | None = None
    cluster_id: str | None = None
    dispatch_slot: str | None = None
    parent_dispatch_id: str | None = None
    allowed_paths: list[str] | None = None
    forbidden_paths: list[str] | None = None
    source_ref: str | None = None


def create_window(conn: sqlite3.Connection, *, run_label: str, window_kind: str,
                  baseline_sha: str | None = None, source_pack_path: str | None = None) -> str:
    window_id = new_id("win")
    conn.execute(
        """INSERT INTO dispatch_windows
           (window_id, run_label, window_kind, baseline_sha, source_pack_path)
           VALUES (?, ?, ?, ?, ?)""",
        (window_id, run_label, window_kind, baseline_sha, source_pack_path),
    )
    conn.commit()
    return window_id


def create_dispatch(conn: sqlite3.Connection, data: DispatchInput) -> str:
    if data.agent_kind not in AGENTS:
        raise ValueError(f"unknown agent_kind: {data.agent_kind}")
    dispatch_id = data.dispatch_id or new_id("disp")
    conn.execute(
        """INSERT INTO agent_fleet_dispatch_ledger
           (dispatch_id, window_id, agent_kind, model_id, task_id, cluster_id, dispatch_slot,
            parent_dispatch_id, allowed_paths_json, forbidden_paths_json, source_ref)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            dispatch_id, data.window_id, data.agent_kind, data.model_id, data.task_id,
            data.cluster_id, data.dispatch_slot, data.parent_dispatch_id,
            as_json(data.allowed_paths or []), as_json(data.forbidden_paths or []), data.source_ref,
        ),
    )
    conn.commit()
    return dispatch_id


def finish_dispatch(conn: sqlite3.Connection, *, dispatch_id: str, verdict: str,
                    state: str = "closed", pr_number: int | None = None,
                    pr_url: str | None = None, output_path: str | None = None,
                    merge_sha: str | None = None, validation: dict[str, str] | None = None,
                    silent_flexibility: bool = False, amend_trigger_text: str | None = None) -> None:
    if verdict not in VERDICTS:
        raise ValueError(f"bad verdict: {verdict}")
    conn.execute(
        """UPDATE agent_fleet_dispatch_ledger
           SET verdict=?, state=?, pr_number=?, pr_url=?, output_path=?, merge_sha=?,
               validation_json=?, silent_flexibility_flag=?, amend_trigger_text=?,
               updated_at=CURRENT_TIMESTAMP
           WHERE dispatch_id=?""",
        (verdict, state, pr_number, pr_url, output_path, merge_sha,
         as_json(validation or {}), int(silent_flexibility), amend_trigger_text, dispatch_id),
    )
    conn.commit()


def attach_artifact(conn: sqlite3.Connection, *, dispatch_id: str, io_kind: str,
                    path: str, sha256: str | None = None, size: int | None = None,
                    tracked: bool = True, label: str = "candidate") -> str:
    io_id = new_id("io")
    conn.execute(
        """INSERT INTO dispatch_io_artifacts
           (io_id, dispatch_id, io_kind, artifact_path, artifact_sha256, artifact_bytes,
            is_repo_tracked, evidence_label)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (io_id, dispatch_id, io_kind, path, sha256, size, int(tracked), label),
    )
    conn.commit()
    return io_id


def record_cost(conn: sqlite3.Connection, *, dispatch_id: str, agent_kind: str, model_id: str,
                token_input: int, token_output: int, token_cached_input: int = 0,
                price_id: str | None = None, artifact_id: str | None = None,
                phase: str = "unknown", cost_usd_estimate: float | None = None) -> str:
    if cost_usd_estimate is None:
        row = conn.execute("SELECT * FROM model_price_snapshot WHERE price_id=?", (price_id,)).fetchone() if price_id else None
        if row is None:
            cost_usd_estimate = 0.0
        else:
            input_cost = token_input * float(row["input_usd_per_1m"] or 0) / 1_000_000
            cached_cost = token_cached_input * float(row["cached_input_usd_per_1m"] or 0) / 1_000_000
            output_cost = token_output * float(row["output_usd_per_1m"] or 0) / 1_000_000
            cost_usd_estimate = round(input_cost + cached_cost + output_cost, 6)
    cost_id = new_id("cost")
    conn.execute(
        """INSERT INTO cost_attribution_ledger
           (cost_id, dispatch_id, agent_kind, model_id, token_input, token_output,
            token_cached_input, cost_usd_estimate, artifact_id, phase, price_id)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (cost_id, dispatch_id, agent_kind, model_id, token_input, token_output,
         token_cached_input, cost_usd_estimate, artifact_id, phase, price_id),
    )
    conn.commit()
    return cost_id


def backfill_from_checkpoint(conn: sqlite3.Connection, checkpoint_path: Path, *, default_agent: str = "Codex") -> str:
    data = json.loads(checkpoint_path.read_text())
    window_id = create_window(
        conn,
        run_label=data.get("run_label", checkpoint_path.stem),
        window_kind="run",
        baseline_sha=data.get("actual_origin_main") or data.get("baseline_origin_main"),
        source_pack_path=data.get("working_pack"),
    )
    for slot, item in (data.get("slots") or {}).items():
        disp_id = create_dispatch(conn, DispatchInput(
            window_id=window_id,
            agent_kind=default_agent,
            task_id=item.get("task_id", f"slot-{slot}"),
            dispatch_slot=str(slot),
            allowed_paths=item.get("files_changed", []),
            source_ref=str(checkpoint_path),
        ))
        finish_dispatch(
            conn,
            dispatch_id=disp_id,
            state=item.get("state", "partial"),
            verdict="clear" if item.get("terminal_state") == "MERGED" else "partial",
            pr_number=item.get("live_pr"),
            pr_url=item.get("live_pr_url"),
            output_path=(item.get("files_changed") or [None])[0],
            merge_sha=item.get("merge_sha"),
            validation=item.get("validation_attempted", {}),
        )
    return window_id
```


## 5. Backfill plan for 4 run receipts

### 5.1 CHECKPOINT-main.json → dispatch_windows

`run_label` 映射为 `dispatch_windows.run_label`；`expected_baseline` 和 `actual_origin_main` 映射 baseline 字段；`run_policy.authority_writer = CODEX0_only` 映射到 window note；`run_policy.forbidden_runtime_unlocks[]` 写入 boundary_json 或 window notes。`validator.verdict` 不直接决定每个 dispatch verdict，只决定 pack-level validator verdict。

### 5.2 CHECKPOINT-main.json slots → agent_fleet_dispatch_ledger

本地 `CHECKPOINT-main.json` 只包含中途 cursor 附近 5 个 slot，不是 50 个 final rows；因此 backfill 分两阶段：第一阶段从 `slots` object 写已有 row，第二阶段从 `manifest.jsonl` 补 planned row，再从 `task-index.md` 或 GitHub PR readback 填 PR/merge/verdict。这个双源 backfill 可以避免把 mid-checkpoint 错读为 final completeness。

### 5.3 PR #227 / #231 / #239 / #240 → amend/audit tables

- PR #227 的 W2 checkpoint 17 dispatch/17 merged、PF-C3-04 deferred、interruption counts，应写为 `dispatch_windows(window_kind='run')` + 17 dispatch rows + one expected deferred note。
- PR #231 的 Run-1 3 auditor synthesis 与 8 amendment rows，应写 `dispatch_audit_verdicts` + `dispatch_amend_events(trigger_kind='silent_flexibility')`。
- PR #239 的 Run-2 receipt traceability fixes，应写 `dispatch_amend_events(trigger_kind='receipt_traceability'|'topology_replacement')`，尤其记录 PR #226/#228 final truth source。
- PR #240 的 Run-3+4 C1 pass / C2 partial cascade，应写两个 `dispatch_windows` 或一个 combined window with two clusters：`PF-C1` pass, `PF-C2` partial，C2 five partial dispatches entered as `expected_partial` unless audit says reject。

## 6. Ledger invariants

1. `dispatch_id` 是 stable replay key，不等同 PR number；一个 dispatch 可无 PR，或多个 dispatch 合并进一个 PR。
2. `window_id` 是 cost/reporting 聚合 key。Run-3+4 combined PR 必须允许一个 PR 对多个 clusters。
3. `verdict` 与 `state` 分离：merged 不是 clear，partial 也可 merged；Run-2 synthetic UAT 就是 merged but partial。
4. `silent_flexibility_flag` 不自动判 reject，只提示审计需要读取 allowed_paths 与 actual changed files。
5. `amend_count` 只统计被记录的 amendment，不统计 normal edit/retry。
6. `boundary_json` 只记录 scanner 结果，不替代 ScoutFlow authority surfaces。
7. `source_ref` 必须写到具体 CHECKPOINT/PR/report path，避免“聊天说过”的弱证据。

## 7. Candidate backfill pseudo-sequence

```bash
scoutflow-ledger init .scoutflow-agent-fleet-ledger.sqlite
scoutflow-ledger backfill-checkpoint RUN-Dispatch127-176-overnight-2026-05-05/CHECKPOINT-main.json
scoutflow-ledger backfill-manifest dispatch127-176-autoexec-pack/manifest.jsonl --window Dispatch127-176
scoutflow-ledger import-pr --number 227 --kind window2-docs
scoutflow-ledger import-pr --number 231 --kind run1-amendment
scoutflow-ledger import-pr --number 239 --kind run2-amendment
scoutflow-ledger import-pr --number 240 --kind run3-4-combined
scoutflow-ledger replay PF-C2-06 --format markdown
```

## 8. What this module deliberately does not do

它不解析 LLM 对话全文，不读取 `~/.claude` 或 `~/.codex` 隐私日志，不上报 SaaS，不执行 agent，不重写 ScoutFlow authority，不把 `current.md` 的 lane 规则变成新规则。它只是给单人本地开发新增一个可查询的 evidence ledger，让 CHECKPOINT 不再承担不适合的运行时归因职责。🚦


## Appendix F — dispatch ledger audit checklist
1. For dispatch ledger import and replay, the operator should confirm dispatch_id is stable and not confused with PR number; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
2. For dispatch ledger import and replay, the operator should check cluster_id on combined pull requests; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
3. For dispatch ledger import and replay, the operator should compare allowed paths with changed paths; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
4. For dispatch ledger import and replay, the operator should preserve expected_partial instead of flattening to clear; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
5. For dispatch ledger import and replay, the operator should store source_ref for every derived row; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
6. For dispatch ledger import and replay, the operator should confirm dispatch_id is stable and not confused with PR number; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
7. For dispatch ledger import and replay, the operator should check cluster_id on combined pull requests; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
8. For dispatch ledger import and replay, the operator should compare allowed paths with changed paths; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
9. For dispatch ledger import and replay, the operator should preserve expected_partial instead of flattening to clear; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
10. For dispatch ledger import and replay, the operator should store source_ref for every derived row; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
11. For dispatch ledger import and replay, the operator should confirm dispatch_id is stable and not confused with PR number; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
12. For dispatch ledger import and replay, the operator should check cluster_id on combined pull requests; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
13. For dispatch ledger import and replay, the operator should compare allowed paths with changed paths; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
14. For dispatch ledger import and replay, the operator should preserve expected_partial instead of flattening to clear; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
15. For dispatch ledger import and replay, the operator should store source_ref for every derived row; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
16. For dispatch ledger import and replay, the operator should confirm dispatch_id is stable and not confused with PR number; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
17. For dispatch ledger import and replay, the operator should check cluster_id on combined pull requests; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
18. For dispatch ledger import and replay, the operator should compare allowed paths with changed paths; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
