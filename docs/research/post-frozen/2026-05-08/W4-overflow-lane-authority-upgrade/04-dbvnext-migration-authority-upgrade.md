---
title: DB vNext Migration Authority-Upgrade Roadmap
status: candidate
authority: not-authority
authority_state: not-execution-approved
created_by: gpt-pro
parent_cluster: W4
lane: dbvnext_migration
prerequisite_check: refreshed_2026-05-07T17:15:02Z
master_spec_anchor: §16.1 (硬红线) + §16.2 (升级路径) + §14.2 (pre-flight) + §16.3 (风险矩阵)
disclaimer: |
  本文是 candidate authority-upgrade roadmap, 不是 lane 完成权限升级的证据.
  Lane 解禁需要走完整 §3 pre-flight 5 步 + Hermes 外审 V-PASS + 磊哥显式授权 + spec PR merge.
  本文内的 PR # / file path / SHA 标 "(撰写时刻历史参考, 真值以 §0.5 Check 为准)".
---

# DB vNext Migration Authority-Upgrade Roadmap

> 本文产出的是 dbvnext_migration 的 candidate authority-upgrade roadmap。它不输出 migration SQL, 不改变 `services/api/migrations/**` 当前 forbidden state。

## §0.5 Prerequisite Check

> refreshed_at: `2026-05-08T09:24:11Z`. 本段是本文件的真态读回锚, 任一后续 agent 接收本文时必须再次刷新, 不得把本文数值当永久 authority。

| Check | 刷新真态 | Drift / 处理 |
|---|---|---|
| 1 — main HEAD | `45e88d45342ba6f6036e68695ca56d09deaaf06d`; message=`Merge pull request #257 from RayWong1990/codex/w4-b-step0-convergence` | 本文引用 main HEAD 时以 `45e88d4` 为准；更早 prerequisite truth 只保留为历史背景, 不再作为 live anchor。 |
| 2 — current.md | Active product lane `0/3`; Authority writer `0/1`; state=`WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`; 5 overflow lane Hold 仍列明。 | `docs/current.md` TL;DR 主锚仍停在 `e18d45a`; lane 边界与计数未漂移，但 main-head 叙述尚未追到 `45e88d4`。 |
| 3 — task-index.md | Active `0/3`; Review `0`; Authority writer `0/1`; Phase=`Phase 1A — WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`。 | 与提示词一致。 |
| 4 — decision-log.md | 顶部 authority rebase 记录仍锚在 `origin/main = e18d45a` / PR #254；PR #247 metadata 明示加入 `D-017 follow-up`。 | 决策条目仍可用，但 main-head 叙述尚未追到 `45e88d4`。 |
| 5 — memory INDEX | `batch_count: 17`; Lessons 7 / Feedback 5 / Patterns 5; 重点含 L-RUNTIME-APPROVAL-DRIFT, L-MIGRATION-DRIFT, L-OVEROBJECTIFICATION, P-PROOF-PAIR-CANARY, P-OVERFLOW-NOT-BLOCKER。 | 与提示词一致。 |
| 6 — bridge config | `write_enabled=False` 在未配置 vault root 分支与已配置 vault root 分支均成立。 | 与提示词一致; 本文不改变该 invariant。 |
| 7 — START-HERE | `docs/00-START-HERE.md` 已由 `python tools/refresh-start-here.py` 刷到 `last_refreshed_from_main_sha: 45e88d4`; auto anchor chain = `45e88d4 ← 3cbe79e ← ca8593a`。 | START-HERE 已进入 `45e88d4` 语境；authority trio 其余文件仍各自保留历史锚点。 |
| B-lane sanity | `bridge/router.py` 当前暴露 bridge health / vault config / vault preview / vault commit dry-run 4 个 route decorator; migrations baseline 仅 001/002; capture-station package 未见 Playwright / Selenium dependency。 | 提示词里「5 routes」按历史参考处理, 真值以 router 文件为准。 |

**读回证据 URL 包**: main commit API, `docs/current.md`, `docs/task-index.md`, `docs/decision-log.md`, `docs/memory/INDEX.md`, `services/api/scoutflow_api/bridge/config.py`, `services/api/scoutflow_api/bridge/router.py`, `services/api/migrations/001_phase1a_capture_creation.sql`, `services/api/migrations/002_phase1a_jobs_receipt.sql`, `apps/capture-station/package.json`。

## §1 Lane 当前态

### §1.1 Lane forbidden 边界引用

- current.md 当前禁止段明示 `services/api/migrations/**` FORBIDDEN: migration dry-run plan / schema 变更 / migration 实施均需另立 dispatch + user gate + 单独 PR + 外审。
- baseline migrations 当前只有 001 capture creation 与 002 jobs receipt, 这是现有 Phase 1A minimal schema。
- master spec §16.1 锁 PlatformResult enum / WorkerReceipt schema / Trust Trace DTO 未经新 dispatch + 外审不得改动。
- docs/SRD-amendments/db-vnext-srd-v3-candidate 仍是 candidate-only, not promoted DB authority。
- memory L-MIGRATION-DRIFT 直接适用: schema/migration 不能随 frontend/spec PR 偷渡。

### §1.2 Lane 现状真态

| 维度 | 真态 | 本 roadmap 处理 |
|---|---|---|
| migrations baseline | 001/002 only | 只作为 RI 起点 |
| adopted path | `services/api/scoutflow_api/storage.py::_init_schema()` 按文件名顺序加载 `services/api/migrations/*.sql` | 记录现行 manual SQL + storage.py loader, 不在本文扩写 SQL |
| toolchain status | repo 内当前无 `alembic*` 实体文件 | Alembic 只保留为 deferred candidate / historical suggestion, 不是本轮 adopted path |
| migration permission | forbidden | 不写真 SQL / 不改 schema |
| db-vnext SRD | candidate-only | 不当 promoted authority |
| locked shapes | PlatformResult / WorkerReceipt / Trust Trace DTO | D-MIG-003 保护 |
| environment | dev/prod truth 未在 prompt 中完整给出 | rollout 标 TODO |

### §1.2.1 双口径裁决

1. 当前 adopted path 只有 manual SQL + `storage.py` loader: live 基线是 `services/api/migrations/001_phase1a_capture_creation.sql`、`002_phase1a_jobs_receipt.sql`，由 `services/api/scoutflow_api/storage.py::_init_schema()` 顺序执行。
2. Alembic 在本轮只允许作为 deferred candidate / historical suggestion 被记录，不能再写成 lane 4 spec 的必须前置，也不能写成 adopted path。
3. 真 migration SQL、toolchain 选型、以及任何 schema execution 仍留给后续单独 migration PR；本文件只把 spec PR 的前置条件压实。

### §1.3 风险矩阵

| 风险 | Severity | 具体失败模式 | 必需缓解 |
|---|---|---|---|
| 数据丢失 | critical | migration 不可逆或 backup 不完整 | backup plan + dry-run + rollback evidence |
| 锁字段改 | critical | PlatformResult / WorkerReceipt / Trust Trace DTO shape 被顺手改 | no-touch spec lock + golden contract |
| 跨 entity RI | high | capture/job/artifact/trust/signal 关系不一致 | RI matrix + pre/post smoke |
| 部署窗口 | high | dev sqlite 与 production-like DB 风险混淆 | environment matrix + phased rollout |
| 跨 PR rollback | high | migration land 后 revert 影响数据状态 | emergency rollback plan + stop-the-line |
| authority drift | critical | db-vnext candidate 被误写成 promoted authority | explicit candidate disclaimer + decision-log gate |

### §1.4 实施前置条件

1. RI test spec 先于 migration draft。
2. Backup / dry-run / rollback plan 先于任何 migration PR。
3. Locked DTO/enum/receipt guard 先于 schema change。
4. Deployment window 要区分 dev sqlite 与 production-like environment。
5. Any migration execution 需要 Hermes V-PASS + 磊哥显式授权 + spec PR merge。

### §1.5 24h 内 actionable consumer

- CC1 可在 24h 内消费 D-MIG-001/002/003 起草 spec PR。
- Hermes 可审 backup completeness + RI + locked fields。
- Codex 不能从本文直接写 migration; 只有 commander prompt 填实且授权后才可进入候选实施。

## §2 升级路径

### §2.1 推荐路径

推荐路径: RI spec → backup/rollback spec → locked DTO guard → migration spec PR skeleton → Hermes → explicit user gate → separate migration PR skeleton → phased rollout。

1. D-MIG-001 定义 RI matrix, 不写 SQL。
2. D-MIG-002 定义 backup/dry-run/rollback evidence。
3. D-MIG-003 锁住 PlatformResult / WorkerReceipt / Trust Trace DTO。
4. D-MIG-004 只在 1-3 完成后形成 lane 4 spec PR skeleton, 并写明 adopted path = manual SQL + `storage.py` loader。
5. D-MIG-004 不把 Alembic 当必须前置; 若后续有人主张引入 Alembic, 只能作为 deferred candidate 单独论证。
6. D-MIG-005/006 负责 rollout 风险控制与 closeout evidence, 防止 dev pass 泛化。

### §2.2 路径理由

dbvnext_migration 是数据完整性 lane, 风险不可通过「快改快回」解决。只要 migration 改变持久化层, revert 就不等于数据恢复。因此必须先把 backup、RI、locked fields、deployment window 写成硬条件。

### §2.3 不推荐路径 + 反模式

- 不推荐「schema 草案直接进 migration file」: candidate spec 不等于 execution permission。
- 不推荐「顺手改 enum/DTO」: 这是跨 contract drift。
- 不推荐「dev sqlite 成功即宣称 rollout 结束」: 环境层风险未覆盖。
- 不推荐「forward-only 无 rollback」: 即使 forward-only, emergency path 仍要写。

### §2.4 候选时间窗

- 撰写时刻历史参考: dbvnext_migration 属于中长期高风险 lane。
- 24h 内最可行动: RI + backup + lock spec, 不是 migration。
- 1 周内可行动: Hermes review + migration commander prompt skeleton。

## §3 Pre-flight 5 步

### §3.1 Step 1: task-index 注册

- 注册 T-LANE-MIG-XXX, 占 Active product lane 1/3。
- scope 必须包含 backup/RI/locked fields; allowed paths 起初应为 research/spec candidate, not migration path。
- validation 必须列 pre/post RI 与 rollback evidence。

### §3.2 Step 2: decision-log D-XXX 草稿

- 草稿必须明确 dbvnext_migration 只是 candidate upgrade path。
- 草稿必须写 no SQL / no execution until explicit user gate。
- 草稿必须列 environment unknowns 与 backup requirement。

### §3.3 Step 3: Hermes pre-flight 外审 prompt

- Hermes 审 backup plan, RI, locked fields, rollback realism, deployment window。
- Any critical gap = V-REJECT。
- V-PARTIAL 以上必须修订后才能给 Codex。

### §3.4 Step 4: CC1 commander prompt v1 草稿

- prompt 必须拆分: spec/audit, migration draft, dry-run evidence, rollout, closeout。
- prompt 必须包含 amend_and_proceed trigger: schema drift, RI fail, rollback uncertainty, DTO collision。
- prompt 不得包含真 migration SQL。

### §3.5 Step 5: 磊哥显式授权 + paste Codex

- 授权必须指明 exact migration scope 与 backup evidence。
- 无 backup evidence 不执行。
- Codex closeout 必须列 data integrity evidence 与 rollback status。

## §4 Dispatch templates
### D-MIG-001 — schema 完整 RI test spec
- id: `D-MIG-001`
- status: candidate
- parent_lane: `dbvnext_migration`
- dependency: 无; spec-only
- TL;DR: 定义 capture/job/artifact/trust/signal 等跨 entity referential integrity acceptance, 不写真 migration。
- 输入包:
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/00-START-HERE.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/decision-log.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/memory/INDEX.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/locked-principles.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/contracts-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/migrations/001_phase1a_capture_creation.sql
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/migrations/002_phase1a_jobs_receipt.sql
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/SRD-amendments/db-vnext-srd-v3-candidate-2026-05-04.md
- 输出 deliverable:
  - `docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/dispatch-packets/D-MIG-001-ri-test-spec-candidate.md`
- 验收标准:
  - RI matrix 覆盖现有 captures/jobs/artifact_assets/job_events
  - 未来 signal/hypothesis/topic_card 仅以 candidate field table 出现
  - 无 CREATE/ALTER SQL
- 反模式 REGENERATE:
  - REGENERATE: 输出真 SQL
  - REGENERATE: 把 db-vnext candidate 当 promoted authority
  - REGENERATE: 改 PlatformResult/WorkerReceipt/DTO
- pre-flight check:
  - 读取 current migrations forbidden
  - 读取 baseline migration 001/002
  - 读取 L-MIGRATION-DRIFT
  - 确认 no active product lane collision
- self-verification:
  - no SQL statements
  - RI matrix complete
  - locked fields protected
  - candidate label present
  - Hermes dimensions mapped
### D-MIG-002 — backup plan + dry-run + rollback path spec
- id: `D-MIG-002`
- status: candidate
- parent_lane: `dbvnext_migration`
- dependency: D-MIG-001 draft
- TL;DR: 定义 migration 前 backup, dry-run evidence, emergency rollback, forward-only caveat。
- 输入包:
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/00-START-HERE.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/decision-log.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/memory/INDEX.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/locked-principles.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/contracts-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/migrations/001_phase1a_capture_creation.sql
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/migrations/002_phase1a_jobs_receipt.sql
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/SRD-amendments/db-vnext-srd-v3-candidate-2026-05-04.md
- 输出 deliverable:
  - `docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/dispatch-packets/D-MIG-002-backup-rollback-candidate.md`
- 验收标准:
  - backup evidence schema 清楚
  - dry-run 与 production window 分离
  - rollback realism 标 caveat
- 反模式 REGENERATE:
  - REGENERATE: 无 backup plan 就迁移
  - REGENERATE: 宣称 forward-only 可无 rollback
  - REGENERATE: 混淆 dev sqlite 与 prod db
- pre-flight check:
  - 读取 master spec §16.2 row dbvnext
  - 读取 current forbidden
  - 列 environment matrix
  - 确认 no SQL output
- self-verification:
  - backup checklist present
  - dry-run evidence fields present
  - rollback caveats present
  - deployment window present
  - candidate label intact
### D-MIG-003 — PlatformResult / WorkerReceipt / Trust Trace DTO 不动 spec lock
- id: `D-MIG-003`
- status: candidate
- parent_lane: `dbvnext_migration`
- dependency: D-MIG-001
- TL;DR: 把三个锁字段/shape 列为 migration hard no-touch, 除非另立 dispatch + 外审。
- 输入包:
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/00-START-HERE.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/decision-log.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/memory/INDEX.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/locked-principles.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/contracts-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/migrations/001_phase1a_capture_creation.sql
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/migrations/002_phase1a_jobs_receipt.sql
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/SRD-amendments/db-vnext-srd-v3-candidate-2026-05-04.md
- 输出 deliverable:
  - `docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/dispatch-packets/D-MIG-003-locked-dto-guard-candidate.md`
- 验收标准:
  - 三类 lock 有当前来源与 no-touch rationale
  - 任何 change request 需独立 path
  - tests/golden contract 描述清楚
- 反模式 REGENERATE:
  - REGENERATE: migration 顺手改 enum/receipt/DTO
  - REGENERATE: 把 field rename 写成 cleanup
  - REGENERATE: 缺少 golden evidence
- pre-flight check:
  - 读取 current locked fields
  - 读取 contracts-index Receipt/Platform
  - 读取 memory L-MIGRATION-DRIFT
  - 确认 no implementation
- self-verification:
  - lock table complete
  - change request path present
  - no schema mutation
  - Hermes can audit
  - candidate label intact
### D-MIG-004 — dbvnext_migration spec PR
- id: `D-MIG-004`
- status: candidate
- parent_lane: `dbvnext_migration`
- dependency: D-MIG-001~003 + backup evidence
- TL;DR: 合成 lane 4 spec PR skeleton，明确 adopted path 仍是 manual SQL + `storage.py` loader；migration execution 仍需 user gate 与 Hermes V-PASS。
- 输入包:
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/00-START-HERE.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/decision-log.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/memory/INDEX.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/locked-principles.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/contracts-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/migrations/001_phase1a_capture_creation.sql
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/migrations/002_phase1a_jobs_receipt.sql
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/SRD-amendments/db-vnext-srd-v3-candidate-2026-05-04.md
- 输出 deliverable:
  - `docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/dispatch-packets/D-MIG-004-authority-upgrade-skeleton-candidate.md`
- 验收标准:
  - spec PR 含 backup/RI/lock fields/deployment window
  - 明确 adopted path = manual SQL + `storage.py` loader
  - 明确 Alembic = deferred candidate, not required in this round
  - 不输出 migration SQL
  - no runtime/vault/browser
- 反模式 REGENERATE:
  - REGENERATE: 把 spec PR 当 migration PR
  - REGENERATE: 把 Alembic 写成 adopted path 或必经前置
  - REGENERATE: 省略 backup evidence
  - REGENERATE: 改 locked DTO
- pre-flight check:
  - 刷新 Check 1-6
  - 确认 D-MIG-001~003 ready
  - 确认 Hermes preflight
  - 复核 `storage.py` loader + 001/002 baseline
  - 确认 Active slot
- self-verification:
  - scope lane-only
  - backup present
  - RI present
  - locked fields present
  - adopted/deferred wording explicit
  - candidate label intact
### D-MIG-005 — amend_and_proceed for migration
- id: `D-MIG-005`
- status: candidate
- parent_lane: `dbvnext_migration`
- dependency: D-MIG-004
- TL;DR: 定义 migration 发现 silent flexibility 时的立即 amend 规则, 防止带病 land。
- 输入包:
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/00-START-HERE.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/decision-log.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/memory/INDEX.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/locked-principles.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/contracts-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/migrations/001_phase1a_capture_creation.sql
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/migrations/002_phase1a_jobs_receipt.sql
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/SRD-amendments/db-vnext-srd-v3-candidate-2026-05-04.md
- 输出 deliverable:
  - `docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/dispatch-packets/D-MIG-005-amend-proceed-candidate.md`
- 验收标准:
  - silent flexibility triggers 清楚
  - amend 上限与 stop condition 清楚
  - evidence diff table 明确
- 反模式 REGENERATE:
  - REGENERATE: 发现 schema drift 仍继续
  - REGENERATE: 第三次 amend 不 stop
  - REGENERATE: 把 rollback risk 降级
- pre-flight check:
  - 读取 memory F-DIRECT-MERGE-OK
  - 读取 L-MIGRATION-DRIFT
  - 列 possible drift cases
  - 确认 no SQL output
- self-verification:
  - trigger table present
  - stop-the-line present
  - audit loop present
  - no implementation
  - candidate label intact
### D-MIG-006 — lane closeout + post-migration smoke packet
- id: `D-MIG-006`
- status: candidate
- parent_lane: `dbvnext_migration`
- dependency: D-MIG-004/005 后续
- TL;DR: 定义 migration 后 evidence packet: RI, backup, rollback, smoke, remaining Hold。
- 输入包:
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/00-START-HERE.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/decision-log.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/memory/INDEX.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/locked-principles.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/contracts-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/migrations/001_phase1a_capture_creation.sql
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/migrations/002_phase1a_jobs_receipt.sql
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/SRD-amendments/db-vnext-srd-v3-candidate-2026-05-04.md
- 输出 deliverable:
  - `docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/dispatch-packets/D-MIG-006-closeout-smoke-candidate.md`
- 验收标准:
  - post-migration smoke 只作 evidence, 不泛化 runtime
  - backup/rollback evidence linked
  - remaining Hold lanes listed
- 反模式 REGENERATE:
  - REGENERATE: closeout 漏 rollback
  - REGENERATE: 把 smoke pass 当 product closure
  - REGENERATE: 修改 authority files as deliverable
- pre-flight check:
  - 读取 final PR metadata
  - 读取 smoke/audit evidence
  - 复核 current state
  - 确认 no authority write in packet
- self-verification:
  - evidence table complete
  - limitations present
  - remaining Hold present
  - locked DTO still protected
  - self-flag present

## §5 Codex commander prompt skeleton
### §5.1 §0 Codex 角色与上下文
Codex 是 OpenAI Long Runner Coder, 接收 CC1 填实后的 commander prompt, 在单一明确 dispatch 下执行。本文只给 skeleton, 不直接启动实施。Codex 起手必须读本文件 §0.5 的刷新结果, 然后用 GitHub API / raw URL 复核 main HEAD、current/task state、lane 边界源。
### §5.2 §0.5 Prerequisite Check
- Check A: 读取 main commit API, 记录 SHA + message。
- Check B: 读取 current/task-index, 确认 Active product lane 与 Authority writer 空位。
- Check C: 读取 lane 边界源, 确认本 lane 仍处 Hold 且未被其它 lane 间接改变。
- Check D: 读取 memory INDEX, 特别是 runtime/migration/candidate/overflow 相关 instinct。
- Check E: 读取 PR #243/#244/#245/#246/#247/#248 metadata, 引 PR # 时一律标历史参考。
### §5.3 §1 Mission
在 backup/RI/locked DTO/Hermes/explicit gate 齐备后, 以分阶段方式推进 DB vNext migration candidate implementation, 严格区分 spec、dry-run、migration、rollout、closeout。
### §5.4 §2 Inputs
- master spec §5.4 / §6.4 / §7.2 / §12.1 / §16
- baseline migration 001/002 raw URLs
- current/task-index/decision-log raw URLs
- contracts-index Receipt/Platform groups
- memory L-MIGRATION-DRIFT
### §5.5 §3 Hard Boundaries
- 不输出或执行未授权 migration SQL
- 若后续进入 execution, adopted path 默认仍是 manual SQL + `storage.py` loader
- Alembic 只可作为 deferred candidate 另立评估
- 不改 PlatformResult / WorkerReceipt / Trust Trace DTO shape
- 不触碰 runtime_tools / browser_automation / true_vault_write
- 无 backup evidence 不进入 migration
- dev success 不泛化 production readiness
### §5.6 §4 N-phase 执行计划 + dispatch 列表
- Phase 1: RI matrix lock
- Phase 2: backup + rollback plan lock
- Phase 3: locked DTO guard
- Phase 4: migration PR skeleton and Hermes review
- Phase 5: phased rollout and closeout
### §5.7 §5 amend_and_proceed pattern
- silent_flexibility 触发条件: schema 字段需要新增、红线措辞产生歧义、验证证据不足、跨 lane 依赖发生 drift。
- 触发后动作: 不扩大范围; 先写 amend note; 再让 CC0/CC1 对 commander prompt 做最小修订; 仍保持本 lane 不替代其他 lane。
- 单 PR 内最多两轮 amend; 第三轮必须 stop-the-line, 由磊哥拍板是否拆 PR。
### §5.8 §6 Lane closeout 验收
- closeout packet 必须把「做了什么 / 没做什么 / 证据是什么 / 哪些 lane 仍 Hold」写清。
- Authority writer 才能执行最终 writeback; 本 skeleton 不把 authority 文件列为本文件输出 deliverable。
- closeout 后仍需 Hermes 或 CC1 复核, 防止 candidate roadmap 被误引为 current authority。
## §6 Hermes audit prompt skeleton
### §6.1 Hermes 独立外审角色
Hermes 是 3rd party independent auditor, 只对本 lane 的 spec PR、commander prompt、dispatch pack 给外审 verdict。Hermes 输出不替代磊哥显式授权, 也不把 candidate 文档提升为 authority。
### §6.2 audit scope
- 本 lane authority-upgrade spec PR 是否把 §16.1 红线、§16.2 升级路径、§14.2 pre-flight、§16.3 风险矩阵贯彻到位。
- CC1 commander prompt 是否有明确 lane scope、allowed paths、forbidden paths、validation、closeout。
- Dispatch pack 是否能在 24h 内被 Codex/CC1 消费, 且不隐性打开其它 overflow lane。
### §6.3 4 级 verdict 标准
| Verdict | 含义 | 后续动作 |
|---|---|---|
| V-PASS-CLEAR | 无 blocking / high issue | 可进入磊哥显式授权候选 |
| V-PASS-CONCERN | 有 medium 风险, 不阻塞 | 修 wording / validation 后可继续 |
| V-PARTIAL | 有 high 风险点 | land 前必须修订, 不得静默继续 |
| V-REJECT | critical 风险或边界破坏 | 阻塞 Codex 启动, 回到 spec rewrite |
### §6.4 audit dimensions
- backup plan completeness and evidence quality
- RI test coverage across entity graph
- PlatformResult / WorkerReceipt / Trust Trace DTO no-touch
- migration reversibility and emergency rollback realism
- deployment window separation: dev sqlite vs production-like
- candidate vs authority language discipline
- cross-PR rollback blast radius
### §6.5 audit output schema
| Dimension | Finding | Severity | Required revision | Evidence URL |
|---|---|---|---|---|
| `<dimension>` | `<finding>` | `<C/H/M/L>` | `<revision>` | `<raw URL / PR URL>` |
Final verdict: `<V-PASS-CLEAR | V-PASS-CONCERN | V-PARTIAL | V-REJECT>`
Hermes signoff: `<name / timestamp / caveat>`
## §7 Lane-specific 反模式

1. REGENERATE: 输出真 migration SQL 或 CREATE/ALTER 类语句。
2. REGENERATE: 把 db-vnext candidate SRD 当 promoted authority。
3. REGENERATE: 无 backup plan 仍进入 migration。
4. REGENERATE: PlatformResult / WorkerReceipt / Trust Trace DTO 被顺手改。
5. REGENERATE: dev sqlite pass 被写成 production readiness。
6. REGENERATE: migration closeout 不列 rollback status。
7. REGENERATE: schema change 随 frontend/runtime PR 偷渡。
8. REGENERATE: RI test 只覆盖单表, 不覆盖跨 entity。
9. REGENERATE: authority files 被列为本文输出 deliverable。


## §8 Self-flag

### §8.1 GPT Pro 不确定的取舍点

  - ⚠️ 环境真态未完全给出: dev sqlite 与 production-like DB 的具体差异需要后续确认。
  - ⚠️ RI matrix 最终要跟 SRD-v3 promoted path 对齐, 本文只给 upgrade roadmap。
  - ⚠️ backup/rollback 的实际机制依赖 owner 本地 DB 管理方式, 本文只定义证据要求。

### §8.2 GPT Pro 弱项

  - ⚠️ 未读取完整 SRD db-vnext candidate 内容, 只基于 contracts/current/master prompt 锚点。
  - ⚠️ 未执行任何 schema diff 或 migration dry-run。
  - ⚠️ decision-log latest tail 需 CC0/CC1 接收时复核。

### §8.3 待磊哥拍板取舍点

  - 🟡 是否先做 RI/backup spec PR, 再单独 migration PR。
  - 🟡 是否允许 forward-only migration, 以及 emergency rollback 最低标准。
  - 🟡 dev sqlite 与 production-like gate 是否都必须存在。
  - 🟡 locked DTO guard 是否进入独立 promoted addendum。

### §8.4 Self-verification result

- 5 份 markdown 1-to-1 mapping 已生成; 本文件为 `dbvnext_migration`。
- frontmatter 已含 status / authority / authority_state / created_by / parent_cluster / lane / prerequisite_check / disclaimer。
- 已包含 §0.5 + §1-§8 全段落。
- Dispatch 数量在 5-7 范围内, 每个 dispatch 含 standard schema。
- 未写实现模块代码、真 migration SQL、浏览器脚本或运行命令。
- 未把本 lane 写成 current authority, 未声明 lane 已完成解禁。
- 输出 deliverable 清单未把 authority files 作为本文件写入目标。
- 未引用被禁止的本地 home 路径, 未假设本地 shell 命令。
