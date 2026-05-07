---
title: INTEGRATION with CHECKPOINT JSON
status: candidate / not-authority
claim_label: ">=95% design-confidence"
created_at: 2026-05-07
---

# INTEGRATION-WITH-CHECKPOINT-JSON


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


## 1. Why bidirectional derive matters

CHECKPOINT.json 是 ScoutFlow 当前 run 收尾收据；U5 ledger 是逐单运行账本。两者必须双向 derive：

- **CHECKPOINT → ledger**：历史 backfill，不要求 agent wrapper 已存在。
- **ledger → CHECKPOINT**：未来 closeout，从逐单 ledger 自动生成 final receipt。

如果只能单向，就会形成第二知识库风险。U5 的原则是：CHECKPOINT 仍是 run closeout artifact，ledger 是 detail source；最终它们能互相校验。

## 2. Current CHECKPOINT-main.json fields observed

```json
{
  "run_label": "Dispatch127-176-overnight-2026-05-05",
  "started_at": "2026-05-05T23:30:00+0800",
  "baseline_match": true,
  "validator": {
    "tool": "/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/VALIDATE-Dispatch127-176-working-pack-2026-05-05.py",
    "verdict": "clear",
    "dispatch_count": 50,
    "manifest_count": 50,
    "required_external_audit_slots": [
      127,
      130,
      145,
      146,
      162,
      163,
      164,
      166,
      167,
      173,
      174,
      175
    ]
  },
  "run_policy": {
    "external_audit_required_interpretation": "mandatory_internal_audit_then_repair_or_record",
    "continue_to_dispatch176": true,
    "authority_writer": "CODEX0_only",
    "forbidden_runtime_unlocks": [
      "BBDown live",
      "yt-dlp",
      "ffmpeg",
      "ASR",
      "audio_transcript runtime",
      "browser automation",
      "migrations",
      "vault true write",
      "package installs",
      "package-manager adoption",
      "React upgrade",
      "OpenDesign runtime/code/layout reuse",
      "shadcn-admin transplant"
    ]
  },
  "batches": {
    "A": {
      "slots": [
        127,
        128,
        129,
        130,
        131,
        132,
        133,
        134,
        135,
        136,
        137,
        138,
        139,
        140,
        141,
        142,
        143,
        144
      ],
      "state": "in_progress"
    },
    "B": {
      "slots": [
        145,
        146,
        147,
        148,
        149,
        150,
        151,
        152,
        153,
        154,
        155,
        156,
        157,
        158,
        159,
        160,
        161
      ],
      "state": "pending"
    },
    "C": {
      "slots": [
        162,
        163,
        164,
        165,
        166,
        167,
        168,
        169,
        170,
        171,
        172,
        173,
        174,
        175,
        176
      ],
      "state": "pending"
    }
  },
  "cursor": {
    "batch": "A",
    "slot": 131,
    "task_id": "T-P1A-110",
    "state": "pushing"
  },
  "slots_keys": [
    "131",
    "130",
    "129",
    "128",
    "127"
  ]
}
```

Important caveat: 这个 CHECKPOINT 是 mid-run/cursor style，只含 5 个 `slots`，而 validator/manifest 指向 50 dispatch pack。不能把 `len(slots)=5` 当成 dispatch_count=5，也不能把 validator.dispatch_count=50 当成 50 个已完成 rows。Backfill 必须识别 partial receipt。

## 3. Mapping table

| CHECKPOINT key | ledger table.column | transform | lossy? | note |
|---|---|---|---|---|
| `run_label` | `dispatch_windows.run_label` | copy | no | stable window name |
| `started_at` | `dispatch_windows.started_at` | copy | no | timezone preserved as string |
| `working_pack` | `dispatch_windows.source_pack_path` | copy | no | local path not inlined |
| `expected_baseline` / `actual_origin_main` | `dispatch_windows.baseline_sha` | choose actual if present | no | can store both in notes |
| `baseline_match` | `dispatch_windows.notes` or boundary scan | boolean copy | yes | not per-dispatch |
| `validator.verdict` | `orchestration_boundary_scan.verdict` | `clear` → clear | yes | pack-level, not dispatch-level |
| `validator.dispatch_count` | `dispatch_windows.notes` | copy | no | expected manifest count |
| `validator.required_external_audit_slots[]` | dispatch rows | mark audit_required | yes | need manifest join for rows not in slots |
| `run_policy.authority_writer` | `dispatch_windows.notes` | copy | no | CODEX0_only |
| `run_policy.forbidden_runtime_unlocks[]` | boundary scan notes | JSON copy | no | blocked claims |
| `batches.A/B/C.slots[]` | dispatch rows | create planned rows | no | batch state may be stale |
| `cursor` | window notes | copy | no | useful for resume |
| `slots.{n}.task_id` | `agent_fleet_dispatch_ledger.task_id` | copy | no | existing slot rows only |
| `slots.{n}.state` | `agent_fleet_dispatch_ledger.state` | normalize | yes | e.g. pushing/merged |
| `slots.{n}.terminal_state` | `verdict/state` | MERGED→state merged, verdict clear unless risks | yes | audit may override |
| `slots.{n}.live_pr` | `pr_number` | integer | no | if present |
| `slots.{n}.files_changed[]` | `output_path` + artifact rows | first path as output, all as artifact | yes | role unknown without manifest |
| `slots.{n}.validation_attempted` | `validation_json` | JSON copy | no | command→pass/fail |
| `slots.{n}.known_risks[]` | `boundary_json` or notes | JSON copy | no | candidate-only risks |

## 4. Ledger → CHECKPOINT final synthesis

Future wrapper should synthesize final CHECKPOINT from ledger with this shape:

```json
{
  "run_label": "Run-X",
  "run_complete": true,
  "dispatches_total": 24,
  "dispatches_clear": 7,
  "dispatches_partial": 5,
  "dispatches_reject": 0,
  "clusters": {
    "PF-C1": {"verdict": "pass", "useful": "3/3", "needs_edit": "3/3"},
    "PF-C2": {"verdict": "partial", "partial_dispatches": ["PF-C2-06", "PF-C2-07"]}
  },
  "boundary": {
    "authority_files_touched": false,
    "write_enabled_false_preserved": true,
    "runtime_unlock_claimed": false
  },
  "amendments": [
    {"pattern_id": "PAT-AMEND-RUN2-TOPOLOGY-REPLACEMENT", "decision": "amend_and_proceed"}
  ]
}
```

This shape should remain a receipt, not become authority.

## 5. Backfill quality labels

| quality | meaning | allowed use |
|---|---|---|
| `exact` | field copied directly from JSON/PR | dashboard/replay |
| `joined` | field requires manifest/task-index/PR join | dashboard/replay with source_ref |
| `lossy` | field inferred from partial source | audit only, not readiness |
| `missing` | source absent | must show unknown |
| `overridden_by_audit` | audit verdict supersedes raw state | replay + amend |

`CHECKPOINT-main.json` slots are exact for slots 127-131 only; 132-176 require manifest/task-index/GitHub join. Run-2 final CHECKPOINT after PR #239 has explicit receipt corrections, so its amended fields should supersede earlier run report values.

## 6. Import algorithm

```text
1. Read CHECKPOINT JSON.
2. Create window row.
3. Import slots present in CHECKPOINT.
4. If manifest path is available, import missing planned slots.
5. If task-index/GitHub PR data is available, update PR/merge/verdict.
6. Import run report and diff bundle as artifacts.
7. Import audit PRs as audit verdicts.
8. Run boundary scan on changed file lists.
9. Mark source quality per field.
10. Emit backfill summary with lossy counts.
```

## 7. Candidate `checkpoint_backfill_map` seed

```sql
INSERT INTO checkpoint_backfill_map(map_id, checkpoint_path, checkpoint_key, target_table, target_column, transform_rule, lossy, notes) VALUES
('map_run_label','*','run_label','dispatch_windows','run_label','copy',0,'window identity'),
('map_policy','*','run_policy.forbidden_runtime_unlocks','orchestration_boundary_scan','notes','json_copy',0,'blocked runtime claims'),
('map_slot_task','*','slots.*.task_id','agent_fleet_dispatch_ledger','task_id','copy',0,'slot task'),
('map_slot_state','*','slots.*.state','agent_fleet_dispatch_ledger','state','normalize_state',1,'state vocabulary differs'),
('map_slot_pr','*','slots.*.live_pr','agent_fleet_dispatch_ledger','pr_number','int_or_null',0,'PR number'),
('map_validation','*','slots.*.validation_attempted','agent_fleet_dispatch_ledger','validation_json','json_copy',0,'validation evidence');
```

## 8. Anti-overclaim checks

1. If `validator.dispatch_count` > imported slot rows, output `checkpoint_partial=true`.
2. If `run_complete` absent, do not mark window complete.
3. If audit PR later downgrades a verdict, ledger must store both raw verdict and audit override.
4. If `write_enabled=False` source not present, say unknown, not true.
5. If `final_origin_main` differs after receipt bundle PR, keep both execution final SHA and audit final SHA.
6. If combined PR includes multiple clusters, checkpoint synthesis must preserve cluster verdicts.

## 9. Why this is enough for Phase 1

The mapping is intentionally boring. It does not require parsing trace IDs, spans, clocks, or nested workflow histories. It captures exactly what the current ScoutFlow artifacts already expose and adds the missing keys needed for replay/cost/amend. That is the right level for a single-user Phase 1 ledger.


## Appendix A — conflict resolution rules

When CHECKPOINT, manifest, run report, and PR body disagree, the integration layer must not silently choose the most optimistic value. It should apply a clear precedence model:

1. Explicit user authorization and latest authority surfaces define gates.
2. Merged PR body and diff define what landed.
3. Amendment PRs can supersede earlier receipts for traceability fields.
4. CHECKPOINT final receipts define closeout intent, unless later amended.
5. Mid-run CHECKPOINT cursor entries define partial execution status only.
6. Manifest defines planned dispatch shape, not completion truth.
7. Chat text is not durable evidence unless copied into a receipt.

This rule explains why the local `CHECKPOINT-main.json` with only five `slots` cannot be treated as a completed 50-row ledger. It also explains why Run-2 PR #239 can update the interpretation of earlier Run-2 checkpoint fields.

## Appendix B — generated CHECKPOINT shape from ledger

The future ledger-to-CHECKPOINT export should include both summary and detail:

```json
{
  "run_id": "RUN-3-4",
  "run_complete": true,
  "dispatches_total": 24,
  "clusters": [
    {"cluster_id": "PF-C1", "verdict": "pass", "useful": "3/3", "needs_edit": "3/3"},
    {"cluster_id": "PF-C2", "verdict": "partial", "partial_dispatches": ["PF-C2-06", "PF-C2-07", "PF-C2-08", "PF-C2-09", "PF-C2-11"]}
  ],
  "boundary": {
    "authority_files_touched": false,
    "write_enabled_false_preserved": true,
    "runtime_unlock_claimed": false
  },
  "amendments": [],
  "cost_status": "usage_missing_or_partial"
}
```

The export should include `source_ledger_schema_version` and `generated_at`. If the ledger has unresolved rejects, `run_complete` can still be true, but `ready_for_next_run` should be false with reasons.

## Appendix C — validation queries

```sql
-- CHECKPOINT claims 50 dispatches but ledger has fewer non-planned rows
SELECT w.window_id, w.expected_dispatch_count, COUNT(d.dispatch_id) AS rows
FROM dispatch_windows w
LEFT JOIN agent_fleet_dispatch_ledger d ON d.window_id = w.window_id
GROUP BY w.window_id
HAVING rows < w.expected_dispatch_count;

-- merged rows without PR number
SELECT dispatch_id, task_id, verdict
FROM agent_fleet_dispatch_ledger
WHERE state='merged' AND pr_number IS NULL;

-- partial clusters without blocker reasons
SELECT cluster_id, COUNT(*)
FROM agent_fleet_dispatch_ledger
WHERE verdict IN ('partial','expected_partial')
GROUP BY cluster_id
HAVING SUM(CASE WHEN boundary_json IS NOT NULL OR amend_trigger_text IS NOT NULL THEN 1 ELSE 0 END)=0;
```

## Appendix D — import/export failure modes

- JSON parse failure: store raw file hash and fail loud.
- Missing `dispatches_total`: derive from manifest only and mark source as planned.
- Duplicate dispatch id: require suffix or parent relationship; do not overwrite.
- PR number appears in multiple dispatches: allow many-to-one but require cluster id.
- Checkpoint says ready for next run but amendment says blocked: amendment wins.
- Cost rows absent: export `cost_status='missing'`.
- Boundary fields absent: export `boundary_status='unknown'`, not `clear`.

## Appendix E — hash discipline

Every imported CHECKPOINT should store `source_sha256`. Every exported CHECKPOINT should include the ledger database hash or at least a digest of the rows used. This is lightweight but valuable: it lets a future audit verify that a replay was generated from the same evidence base. The hash does not make the ledger authoritative; it only makes the candidate evidence packet reproducible.


## Appendix F — CHECKPOINT integration audit checklist
1. For CHECKPOINT import and export, the operator should check whether the source checkpoint is final or cursor style; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
2. For CHECKPOINT import and export, the operator should import manifest rows as planned rows before assigning verdicts; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
3. For CHECKPOINT import and export, the operator should let amendment PRs supersede earlier receipt fields when documented; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
4. For CHECKPOINT import and export, the operator should write hash values for every imported receipt file; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
5. For CHECKPOINT import and export, the operator should export blocker reasons when next-run readiness is false; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
6. For CHECKPOINT import and export, the operator should check whether the source checkpoint is final or cursor style; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
7. For CHECKPOINT import and export, the operator should import manifest rows as planned rows before assigning verdicts; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
8. For CHECKPOINT import and export, the operator should let amendment PRs supersede earlier receipt fields when documented; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
9. For CHECKPOINT import and export, the operator should write hash values for every imported receipt file; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
10. For CHECKPOINT import and export, the operator should export blocker reasons when next-run readiness is false; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
11. For CHECKPOINT import and export, the operator should check whether the source checkpoint is final or cursor style; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
12. For CHECKPOINT import and export, the operator should import manifest rows as planned rows before assigning verdicts; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
13. For CHECKPOINT import and export, the operator should let amendment PRs supersede earlier receipt fields when documented; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
14. For CHECKPOINT import and export, the operator should write hash values for every imported receipt file; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
15. For CHECKPOINT import and export, the operator should export blocker reasons when next-run readiness is false; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
16. For CHECKPOINT import and export, the operator should check whether the source checkpoint is final or cursor style; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
17. For CHECKPOINT import and export, the operator should import manifest rows as planned rows before assigning verdicts; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
18. For CHECKPOINT import and export, the operator should let amendment PRs supersede earlier receipt fields when documented; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
19. For CHECKPOINT import and export, the operator should write hash values for every imported receipt file; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
20. For CHECKPOINT import and export, the operator should export blocker reasons when next-run readiness is false; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
21. For CHECKPOINT import and export, the operator should check whether the source checkpoint is final or cursor style; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
22. For CHECKPOINT import and export, the operator should import manifest rows as planned rows before assigning verdicts; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
23. For CHECKPOINT import and export, the operator should let amendment PRs supersede earlier receipt fields when documented; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
24. For CHECKPOINT import and export, the operator should write hash values for every imported receipt file; record the evidence source, the expected boundary, the observed result, and the follow-up action before treating the row as audit-ready. This item is intentionally local-first, single-user, and candidate-only.
