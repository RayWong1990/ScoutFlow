---
title: Full Signal Workbench Authority-Upgrade Roadmap
status: candidate
authority: not-authority
authority_state: not-execution-approved
created_by: gpt-pro
parent_cluster: W4
lane: full_signal_workbench
prerequisite_check: refreshed_2026-05-07T17:15:02Z
master_spec_anchor: §16.1 (硬红线) + §16.2 (升级路径) + §14.2 (pre-flight) + §16.3 (风险矩阵)
disclaimer: |
  本文是 candidate authority-upgrade roadmap, 不是 lane 完成权限升级的证据.
  Lane 解禁需要走完整 §3 pre-flight 5 步 + Hermes 外审 V-PASS + 磊哥显式授权 + spec PR merge.
  本文内的 PR # / file path / SHA 标 "(撰写时刻历史参考, 真值以 §0.5 Check 为准)".
---

# Full Signal Workbench Authority-Upgrade Roadmap

> 本文产出的是 full_signal_workbench 的 candidate authority-upgrade roadmap。它是 5 lane 中依赖最重的终极 lane, 不应早于 lane 1 + lane 2 + lane 4 的 readiness evidence。

## §0.5 Prerequisite Check

> refreshed_at: `2026-05-07T17:15:02Z`. 本段是本文件的真态读回锚, 任一后续 agent 接收本文时必须再次刷新, 不得把本文数值当永久 authority。

| Check | 刷新真态 | Drift / 处理 |
|---|---|---|
| 1 — main HEAD | `6dd27d74c214c3e4768196b59f986a6d226f6699`; message=`feat(memory): cross-vendor memory graph W2D land (16 instinct memory) (#245)` | 与提示词里 `c802de4` / `4792b0f` 叙述存在 chronological drift; 本文引用 main HEAD 时以 Check 1 为准。PR #245/#247/#248 均标注「撰写时刻历史参考, 真值以 §0.5 Check 为准」。 |
| 2 — current.md | Active product lane `0/3`; Authority writer `0/1`; state=`WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`; 5 overflow lane Hold 仍列明。 | current.md body 仍写 `c802de4` 作为 main anchor, 低风险 authority-body drift; 不改变 lane 边界。 |
| 3 — task-index.md | Active `0/3`; Review `0`; Authority writer `0/1`; Phase=`Phase 1A — WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`。 | 与提示词一致。 |
| 4 — decision-log.md | PR #247 metadata 明示加入 `D-017 follow-up`; 提示词历史锚点 D-016 已不是唯一候选最新。 | 本文写作时将 D-016 视为历史参考, D-017+ 由 CC0/CC1 接收时复核 decision-log tail。 |
| 5 — memory INDEX | `batch_count: 17`; Lessons 7 / Feedback 5 / Patterns 5; 重点含 L-RUNTIME-APPROVAL-DRIFT, L-MIGRATION-DRIFT, L-OVEROBJECTIFICATION, P-PROOF-PAIR-CANARY, P-OVERFLOW-NOT-BLOCKER。 | 与提示词一致。 |
| 6 — bridge config | `write_enabled=False` 在未配置 vault root 分支与已配置 vault root 分支均成立。 | 与提示词一致; 本文不改变该 invariant。 |
| B-lane sanity | `bridge/router.py` 当前暴露 bridge health / vault config / vault preview / vault commit dry-run 4 个 route decorator; migrations baseline 仅 001/002; capture-station package 未见 Playwright / Selenium dependency。 | 提示词里「5 routes」按历史参考处理, 真值以 router 文件为准。 |

**读回证据 URL 包**: main commit API, `docs/current.md`, `docs/task-index.md`, `docs/decision-log.md`, `docs/memory/INDEX.md`, `services/api/scoutflow_api/bridge/config.py`, `services/api/scoutflow_api/bridge/router.py`, `services/api/migrations/001_phase1a_capture_creation.sql`, `services/api/migrations/002_phase1a_jobs_receipt.sql`, `apps/capture-station/package.json`。

## §1 Lane 当前态

### §1.1 Lane forbidden 边界引用

- master spec §16.1 将 full_signal_workbench 列入 5 overflow lane Hold。
- master spec §10.6 讨论 signal / hypothesis / topic_card 算法层, 但当前只有 IA candidate 与 placeholder contract, 无 runtime workbench。
- task-index Done rows 显示 T-P1A-130/131/132/133/134 等为 candidate-only docs/spec/visual surface, not runtime。
- memory L-OVEROBJECTIFICATION 与 P-PROOF-PAIR-CANARY 对本 lane 直接适用: 先 proof, 后 object。
- full_signal_workbench 依赖 true_vault_write / runtime_tools / dbvnext_migration, 不能绕过前置 lane。

### §1.2 Lane 现状真态

| 维度 | 真态 | 本 roadmap 处理 |
|---|---|---|
| signal/hypothesis/topic_card | IA candidate / glossary / UX candidate | 只作为 contract input |
| runtime workbench | no runtime approval | 不启动 runtime |
| vault write dependency | lane 1 still Hold | D-SW-002 验证 |
| ASR/source runtime dependency | lane 2 still Hold | D-SW-002 验证 |
| DB migration dependency | lane 4 still Hold | D-SW-002 验证 |
| proof-pair | 需要 1 signal + 1 hypothesis + 1 topic_card canary | D-SW-003 |

### §1.3 风险矩阵

| 风险 | Severity | 具体失败模式 | 必需缓解 |
|---|---|---|---|
| 依赖 lane 1+2+4 | critical | vault/runtime/migration 未 ready 时启动 full workbench | dependency matrix + no-go gate |
| IA → runtime 跨语义 | high | IA candidate 被误写成 runtime implementation | candidate disclaimer + commander gate |
| over-objectification | high | proof 未成立就扩张 entity graph | proof-pair canary first |
| proof-pair-canary | high | 无 1/1/1 闭环就做批量 workbench | minimal canary + evidence chain |
| 跨 entity 一致性 | high | signal/hypothesis/topic_card schema 不一致 | entity contract + RI with lane 4 |
| UX generic admin drift | medium | workbench 变成普通后台/KM 图谱 | operator workstation UX lock |
| visual terminal drift | medium | automation/CI 替代战友视觉判断 | 5 Gate human review retained |

### §1.4 实施前置条件

1. Lane 1 true_vault_write 至少有 frontmatter/commit evidence 或明确降级策略。
2. Lane 2 runtime_tools 至少有 source/ASR evidence 或明确 manual metadata fallback。
3. Lane 4 dbvnext_migration 至少有 entity/RI readiness 或明确 no-migration canary。
4. D-SW-003 proof-pair-canary 先于任何 full workbench runtime。
5. UX 必须保持 operator workstation, 不引 generic admin/dashboard。

### §1.5 24h 内 actionable consumer

- CC1 可在 24h 内消费 D-SW-001/002 做 entity + dependency spec。
- Hermes 可审 dependency gate 与 over-objectification risk。
- Codex 只有在 lane 1/2/4 verdict 与 proof-pair ready 后消费 D-SW-004。

## §2 升级路径

### §2.1 推荐路径

推荐路径: entity contract → lane dependency matrix → proof-pair canary → UX lock → Hermes → explicit user gate → bounded runtime workbench。

1. D-SW-001 先统一 signal/hypothesis/topic_card contract。
2. D-SW-002 阻止 lane 5 绕过 lane 1/2/4。
3. D-SW-003 用 1/1/1 canary 证明 proof loop。
4. D-SW-005 把 UX 气质与 5 Gate 锁住。
5. 只有 1-4 完成后, D-SW-004 才能变成 commander prompt。

### §2.2 路径理由

full_signal_workbench 是系统性 lane, 不是单页面功能。它会同时触碰 source evidence、runtime artifact、entity schema、vault write、trust trace、operator UX。任何一个前置 lane 未 ready, 都会把 candidate IA 误变成虚假 runtime。

### §2.3 不推荐路径 + 反模式

- 不推荐「先做 workbench UI」: 容易变成 generic admin 且没有 proof。
- 不推荐「先建完整 entity DB」: 违反 objects-after-proof。
- 不推荐「跳过 lane 1/2/4」: 会把终极 lane 变成绕开红线的入口。
- 不推荐「批量信号/假设」: 先做 1/1/1 canary。

### §2.4 候选时间窗

- 撰写时刻历史参考: full_signal_workbench 应在 lane 1/2/4 ready 后启动, 合理为 1-3 月级别。
- 24h 内最可行动: D-SW-001 entity contract + D-SW-002 dependency matrix。
- 若 lane 1/2/4 未 ready, D-SW-004 必须保持 candidate skeleton。

## §3 Pre-flight 5 步

### §3.1 Step 1: task-index 注册

- 注册 T-LANE-SW-XXX, 占 Active product lane 1/3。
- scope 必须写 dependency gate: lane 1/2/4 readiness 或 explicit downgrade。
- allowed paths 初期只应为 research/spec/visual candidate, not migration/runtime/vault write。

### §3.2 Step 2: decision-log D-XXX 草稿

- 草稿说明 full_signal_workbench 进入 candidate upgrade path, 不是 runtime gate。
- 草稿必须列 lane 1/2/4 dependency status。
- 草稿必须写 proof-pair-canary requirement。

### §3.3 Step 3: Hermes pre-flight 外审 prompt

- Hermes 审 dependency completeness、proof-pair adequacy、over-objectification、UX drift、entity consistency。
- 若缺 lane dependency verdict, Hermes 应 V-PARTIAL 或 V-REJECT。

### §3.4 Step 4: CC1 commander prompt v1 草稿

- prompt 必须先跑 dependency check, 再跑 canary, 最后才 workbench。
- prompt 必须 no-goals: no unapproved runtime, no migration, no vault true write。
- prompt 必须把 operator UX 与 5 Gate 人工审列为 hard boundary。

### §3.5 Step 5: 磊哥显式授权 + paste Codex

- 授权必须指明 lane 1/2/4 readiness evidence 与 canary scope。
- 若选择降级策略, 授权必须显式写出降级边界。
- Codex closeout 必须把 proof-pair 与 full pipeline evidence 分开。

## §4 Dispatch templates
### D-SW-001 — signal / hypothesis / topic_card entity contract spec
- id: `D-SW-001`
- status: candidate
- parent_lane: `full_signal_workbench`
- dependency: 无; spec-only
- TL;DR: 统一 signal、hypothesis、topic_card 三 entity 的 input/output/status/trust relation, 不启动 runtime。
- 输入包:
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/00-START-HERE.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/decision-log.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/memory/INDEX.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/locked-principles.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/contracts-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/wave5/signal-workbench-boundary-note-candidate-2026-05-05.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/wave5/signal-entity-glossary-candidate-2026-05-05.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/wave5/hypothesis-lifecycle-candidate-2026-05-05.md
- 输出 deliverable:
  - `docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/dispatch-packets/D-SW-001-entity-contract-candidate.md`
- 验收标准:
  - 三 entity 字段表完整
  - cross §5.4/6.4/7.2/12.1 一致性映射
  - 明确 IA candidate → runtime gap
- 反模式 REGENERATE:
  - REGENERATE: 把 entity contract 写成 DB schema authority
  - REGENERATE: 跳过 proof-pair canary
  - REGENERATE: 引 generic KM graph
- pre-flight check:
  - 读取 wave5 candidate docs
  - 读取 memory L-OVEROBJECTIFICATION
  - 读取 current no runtime
  - 确认 lane 1/2/4 dependency
- self-verification:
  - entity table complete
  - runtime gap explicit
  - no migration
  - proof dependency present
  - candidate label intact
### D-SW-002 — lane 1+2+4 dependency check spec
- id: `D-SW-002`
- status: candidate
- parent_lane: `full_signal_workbench`
- dependency: D-SW-001 可并行
- TL;DR: 定义 lane 5 启动前必须验证 true_vault_write/runtime_tools/dbvnext_migration 的 ready 状态, 防止终极 lane 偷跑。
- 输入包:
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/00-START-HERE.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/decision-log.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/memory/INDEX.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/locked-principles.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/contracts-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/wave5/signal-workbench-boundary-note-candidate-2026-05-05.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/wave5/signal-entity-glossary-candidate-2026-05-05.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/wave5/hypothesis-lifecycle-candidate-2026-05-05.md
- 输出 deliverable:
  - `docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/dispatch-packets/D-SW-002-dependency-check-candidate.md`
- 验收标准:
  - lane 1/2/4 dependency matrix 有 explicit verdict
  - 可接受降级策略标 TODO
  - 无 cross-lane implicit enablement
- 反模式 REGENERATE:
  - REGENERATE: lane 5 绕过 lane 1/2/4
  - REGENERATE: 把 candidate roadmap 当 ready
  - REGENERATE: 无降级策略却启动
- pre-flight check:
  - 读取 lane 1/2/4 closeout if any
  - 读取 current Hold list
  - 读取 memory P-OVERFLOW-NOT-BLOCKER
  - 确认 no hidden approval
- self-verification:
  - dependency matrix complete
  - TODO for unknowns
  - no overclaim
  - remaining Hold listed
  - candidate label intact
### D-SW-003 — proof-pair-canary 1 signal + 1 hypothesis + 1 topic_card 闭环 proof
- id: `D-SW-003`
- status: candidate
- parent_lane: `full_signal_workbench`
- dependency: D-SW-001/002
- TL;DR: 先用最小 proof-pair 验证 entity relationship 与 operator UX, 防止对象化过早。
- 输入包:
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/00-START-HERE.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/decision-log.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/memory/INDEX.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/locked-principles.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/contracts-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/wave5/signal-workbench-boundary-note-candidate-2026-05-05.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/wave5/signal-entity-glossary-candidate-2026-05-05.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/wave5/hypothesis-lifecycle-candidate-2026-05-05.md
- 输出 deliverable:
  - `docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/dispatch-packets/D-SW-003-proof-pair-canary-candidate.md`
- 验收标准:
  - 1 signal / 1 hypothesis / 1 topic_card 三件套有 evidence relation
  - proof before object 明确
  - no runtime claim
- 反模式 REGENERATE:
  - REGENERATE: 批量建 workbench 对象
  - REGENERATE: 无 canary 直接建 DB
  - REGENERATE: topic_card 无 source trace
- pre-flight check:
  - 读取 P-PROOF-PAIR-CANARY
  - 读取 L-OVEROBJECTIFICATION
  - 确认 lane dependencies
  - 定义 canary evidence
- self-verification:
  - canary minimal
  - evidence chain present
  - no DB migration
  - no runtime claim
  - candidate label intact
### D-SW-004 — full_signal_workbench runtime 升级 PR + commander prompt
- id: `D-SW-004`
- status: candidate
- parent_lane: `full_signal_workbench`
- dependency: D-SW-001~003 + lane 1/2/4 verdict
- TL;DR: 只有依赖与 canary 齐备后, 起草 runtime workbench skeleton。
- 输入包:
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/00-START-HERE.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/decision-log.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/memory/INDEX.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/locked-principles.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/contracts-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/wave5/signal-workbench-boundary-note-candidate-2026-05-05.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/wave5/signal-entity-glossary-candidate-2026-05-05.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/wave5/hypothesis-lifecycle-candidate-2026-05-05.md
- 输出 deliverable:
  - `docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/dispatch-packets/D-SW-004-runtime-upgrade-skeleton-candidate.md`
- 验收标准:
  - commander prompt 引 dependency verdict
  - proof-pair canary 作为 entry gate
  - no generic admin/dashboard UX
- 反模式 REGENERATE:
  - REGENERATE: 绕过 dependency
  - REGENERATE: 把 IA candidate 当 runtime
  - REGENERATE: 引入重 KM/workbench
- pre-flight check:
  - 刷新 Check 1-6
  - 读取 lane 1/2/4 closeout
  - 确认 Hermes verdict
  - 确认 Active slot
- self-verification:
  - dependency linked
  - canary linked
  - UX boundary present
  - no hidden migration/runtime
  - candidate label intact
### D-SW-005 — signal workbench UX 操作员气质
- id: `D-SW-005`
- status: candidate
- parent_lane: `full_signal_workbench`
- dependency: D-SW-001/003
- TL;DR: 把 workbench UX 锁定为 operator workstation, 避免 generic admin/KM dashboard。
- 输入包:
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/00-START-HERE.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/decision-log.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/memory/INDEX.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/locked-principles.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/contracts-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/wave5/signal-workbench-boundary-note-candidate-2026-05-05.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/wave5/signal-entity-glossary-candidate-2026-05-05.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/wave5/hypothesis-lifecycle-candidate-2026-05-05.md
- 输出 deliverable:
  - `docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/dispatch-packets/D-SW-005-ux-operator-candidate.md`
- 验收标准:
  - UX principles 与 master spec §11 对齐
  - 5 Gate human review retained
  - generic admin anti-patterns listed
- 反模式 REGENERATE:
  - REGENERATE: 把 signal workbench 设计成数据后台
  - REGENERATE: 忽略 visual first-class
  - REGENERATE: 自动化替代 human verdict
- pre-flight check:
  - 读取 memory F-STRONG-VISUAL-FIRST-CLASS
  - 读取 PF-C4-01 surface truth
  - 读取 visual redlines
  - 确认 browser automation not required
- self-verification:
  - operator language present
  - generic admin reject list present
  - 5 Gate present
  - no new UI dependency
  - candidate label intact
### D-SW-006 — lane closeout + 全 7 阶段闭环验收
- id: `D-SW-006`
- status: candidate
- parent_lane: `full_signal_workbench`
- dependency: D-SW-004/005 后续
- TL;DR: 定义 full_signal_workbench closeout: signal → hypothesis → topic_card → vault/trust/source 的 7 阶段 evidence readback。
- 输入包:
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/00-START-HERE.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/decision-log.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/memory/INDEX.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/locked-principles.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/contracts-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/wave5/signal-workbench-boundary-note-candidate-2026-05-05.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/wave5/signal-entity-glossary-candidate-2026-05-05.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/wave5/hypothesis-lifecycle-candidate-2026-05-05.md
- 输出 deliverable:
  - `docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/dispatch-packets/D-SW-006-closeout-seven-stage-candidate.md`
- 验收标准:
  - 7 阶段 evidence table complete
  - dependency verdict restated
  - remaining gaps listed
- 反模式 REGENERATE:
  - REGENERATE: 把 closeout 当 product complete
  - REGENERATE: 漏 lane 依赖
  - REGENERATE: 无 proof-pair
- pre-flight check:
  - 读取 final PR metadata
  - 读取 canary evidence
  - 复核 lane dependencies
  - 确认 no authority write in packet
- self-verification:
  - evidence table complete
  - limitations present
  - dependencies present
  - visual status present
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
在 lane 1/2/4 dependency verdict 与 proof-pair canary 齐备后, 以 bounded scope 推进 signal / hypothesis / topic_card full workbench runtime candidate。
### §5.4 §2 Inputs
- master spec §10.6 / §11 / §16
- wave5 candidate docs
- memory L-OVEROBJECTIFICATION + P-PROOF-PAIR-CANARY
- lane 1/2/4 closeout URLs if present
- current/task-index/decision-log raw URLs
### §5.5 §3 Hard Boundaries
- lane 1/2/4 未 ready 不启动 full runtime
- 不把 IA candidate 当 runtime authority
- 不做未授权 migration / vault write / external runtime
- 先 proof-pair canary, 后对象扩张
- UX 不得变 generic admin/dashboard
### §5.6 §4 N-phase 执行计划 + dispatch 列表
- Phase 1: entity contract lock
- Phase 2: lane dependency verdict
- Phase 3: proof-pair canary
- Phase 4: operator UX lock
- Phase 5: bounded runtime candidate and closeout
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
- lane 1+2+4 dependency completeness
- proof-pair-canary existence and adequacy
- entity schema consistency across signal/hypothesis/topic_card
- over-objectification risk
- operator workstation UX vs generic admin drift
- 7-stage full pipeline evidence
- candidate vs authority wording discipline
### §6.5 audit output schema
| Dimension | Finding | Severity | Required revision | Evidence URL |
|---|---|---|---|---|
| `<dimension>` | `<finding>` | `<C/H/M/L>` | `<revision>` | `<raw URL / PR URL>` |
Final verdict: `<V-PASS-CLEAR | V-PASS-CONCERN | V-PARTIAL | V-REJECT>`
Hermes signoff: `<name / timestamp / caveat>`
## §7 Lane-specific 反模式

1. REGENERATE: lane 1/2/4 未 ready 仍启动 full workbench runtime。
2. REGENERATE: IA candidate 被写成 runtime implementation。
3. REGENERATE: 无 proof-pair canary 直接建对象体系。
4. REGENERATE: signal/hypothesis/topic_card schema 不一致。
5. REGENERATE: workbench UX 变 generic admin/dashboard。
6. REGENERATE: full_signal_workbench 隐性打开 migration 或 vault true write。
7. REGENERATE: closeout 把 engineering smoke 当 product closure。
8. REGENERATE: 5 Gate human review 被 automation/CI 替代。
9. REGENERATE: memory lesson 直接写成 current authority, 未走维护规则。


## §8 Self-flag

### §8.1 GPT Pro 不确定的取舍点

  - ⚠️ Lane 5 是否必须等待 lane 1+2+4 全部 V-PASS, 还是允许某一前置 lane 降级, 需要磊哥拍板。
  - ⚠️ Signal/hypothesis/topic_card 最终 entity shape 可能受 dbvnext_migration 约束, 本文只给 candidate contract。
  - ⚠️ proof-pair-canary 的「足够证明」标准需要 Hermes 与战友共同确定。

### §8.2 GPT Pro 弱项

  - ⚠️ 未读取全部 Wave5 candidate docs, 仅依据提示词与 contracts/task-index 锚点。
  - ⚠️ 未验证 lane 1/2/4 的未来 closeout, 因为当前均仍 Hold。
  - ⚠️ 未做 UX 视觉图, 只给 operator UX 约束。

### §8.3 待磊哥拍板取舍点

  - 🟡 Lane 5 是否等 lane 1+2+4 全 ready 后再启动。
  - 🟡 是否允许 no-migration canary 先跑 entity memory only。
  - 🟡 proof-pair-canary 的最小证据格式。
  - 🟡 full workbench 首轮 UX 是否先做 one-screen canary。

### §8.4 Self-verification result

- 5 份 markdown 1-to-1 mapping 已生成; 本文件为 `full_signal_workbench`。
- frontmatter 已含 status / authority / authority_state / created_by / parent_cluster / lane / prerequisite_check / disclaimer。
- 已包含 §0.5 + §1-§8 全段落。
- Dispatch 数量在 5-7 范围内, 每个 dispatch 含 standard schema。
- 未写实现模块代码、真 migration SQL、浏览器脚本或运行命令。
- 未把本 lane 写成 current authority, 未声明 lane 已完成解禁。
- 输出 deliverable 清单未把 authority files 作为本文件写入目标。
- 未引用被禁止的本地 home 路径, 未假设本地 shell 命令。
