---
title: True Vault Write Authority-Upgrade Roadmap
status: candidate
authority: not-authority
authority_state: not-execution-approved
created_by: gpt-pro
parent_cluster: W4
lane: true_vault_write
prerequisite_check: refreshed_2026-05-07T17:15:02Z
master_spec_anchor: §16.1 (硬红线) + §16.2 (升级路径) + §14.2 (pre-flight) + §16.3 (风险矩阵)
disclaimer: |
  本文是 candidate authority-upgrade roadmap, 不是 lane 完成权限升级的证据.
  Lane 解禁需要走完整 §3 pre-flight 5 步 + Hermes 外审 V-PASS + 磊哥显式授权 + spec PR merge.
  本文内的 PR # / file path / SHA 标 "(撰写时刻历史参考, 真值以 §0.5 Check 为准)".
---

# True Vault Write Authority-Upgrade Roadmap

> 本文产出的是 true_vault_write 的 candidate authority-upgrade roadmap。它只定义合法升级路径, 不改变 `write_enabled=False` 真态, 不开启其它 overflow lane。

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

- master spec §16.1 将 true vault write 放入 5 overflow lane Hold, 且要求升级路径走 spec PR + 外审 + user gate。
- current.md 当前禁止段仍明确: 5 overflow lane Hold, write path 不得偷开, credential/raw material 不进入 tracked evidence。
- Lane 边界源为 `services/api/scoutflow_api/bridge/config.py`: 未配置 vault root 与已配置 vault root 两个分支均返回 `write_enabled=False`。
- Bridge SPEC 将 commit route 定义为 gated future endpoint; 当前可讨论 preview / dry-run / contract, 不可把 dry-run 误读为 true write。
- bridge/router.py 当前暴露 dry-run vault commit route, 但 route 说明仍是 dry-run contract, 不构成 write permission。

### §1.2 Lane 现状真态

| 维度 | 真态 | 本 roadmap 处理 |
|---|---|---|
| write_enabled | False × 2 branch | 不修改, 只定义未来 flip 条件 |
| preview | 可作为 markdown preview / gated helper stack 讨论 | preview ≠ commit |
| commit | dry-run / future-gated | 只能写 contract 与 prompt skeleton |
| credential | cookie/token/auth sidecar/raw stdout 不得作为 evidence | secret scan 是升级前置条件 |
| authority state | WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED | 不改变 state |

### §1.3 风险矩阵

| 风险 | Severity | 具体失败模式 | 必需缓解 |
|---|---|---|---|
| secret leakage | critical | cookie / token / API key / raw header 进入 vault 后被 Obsidian/backup 扩散 | strict secret scan + credential material never evidence + fail-loud rejection |
| frontmatter completeness | high | 12 字段缺失导致 RAW 笔记失去 source / trust / hash / state 追溯 | commit 前 completeness gate + missing-field reason |
| immutability | high | vault commit 后历史被下游双链吸收, 返工成本高 | dry-run + operator confirmation + rollback receipt |
| partial commit | high | 7 阶段中断后留下半成品 markdown 或 orphan asset | stage transaction contract + stop condition + cleanup receipt |
| vendor legal | medium | BBDown source content 进入 vault 的版权/合规边界不清 | source policy tag + vendor risk label + runtime lane evidence |
| cross-lane drift | high | lane 1 flip 被误读为 runtime/migration/browser ready | closeout 必列其它 4 lane still Hold |

### §1.4 实施前置条件

1. Frontmatter contract 从 raw 4-field 升级到 commit-ready 12 字段, 每字段要有来源与 failure mode。
2. Secret scan contract 先于 true write, 且 credential material 不允许进入 evidence。
3. Dry-run response 与 true write response 要结构分离, rollback 只能承诺可证明路径。
4. 若涉及 ASR/rewrite/source runtime 证据, 必须等待 runtime_tools 自己完成升级路径; lane 1 不借此打开 lane 2。
5. 若涉及新持久化字段, 必须等待 dbvnext_migration 自己完成升级路径; lane 1 不借此打开 lane 4。

### §1.5 24h 内 actionable consumer

- CC1 可在 24h 内消费 D-VAULT-001/003 生成 spec PR 草稿。
- Codex 可在 CC1 填实 commander prompt 后消费 D-VAULT-004/005。
- Hermes 可消费 §6 audit skeleton 对 spec PR + commander prompt 做三方审。
- 磊哥需要拍板的不是本文, 而是后续 spec PR + Hermes verdict + commander prompt。

## §2 升级路径

### §2.1 推荐路径

推荐路径: contract-first → risk gates → dry-run proof → Hermes → explicit user gate → minimal flip PR。

1. 先 land frontmatter 12 字段 contract, 明确 preview/commit 分界。
2. 再 land secret scan + dry-run/rollback contract, 把不可逆风险降到最小。
3. 用 D-VAULT-005 形成最小 flip commander prompt, 明确其它 lane still Hold。
4. Hermes 以 secret leakage / immutability / raw boundary / rollback 为主审维度。
5. 磊哥显式授权后才进入 Codex 实施候选。

### §2.2 路径理由

true_vault_write 是 7 阶段 pipeline 的最终出口, 风险集中在不可撤销写入与 secret 扩散。它不应该从实现便利出发, 而应从「提交前证据可验证」出发。只要 frontmatter、secret scan、rollback 三件事没锁, flip `write_enabled` 就会把 preview helper 错当 production writer。

### §2.3 不推荐路径 + 反模式

- 不推荐「只改 config 值」: 这是典型 cross-lane authority drift。
- 不推荐「先写入再补 contract」: 写入是不可逆风险, contract 必须前置。
- 不推荐「把 vault preview 当 commit proof」: preview 是 read-only / render layer。
- 不推荐「把 lane 1 与 runtime_tools 合并」: runtime evidence 的合法性属于 lane 2。

### §2.4 候选时间窗

- 撰写时刻历史参考: master spec §17 将 true vault write 放在中长期 lane, 不是今晚立即开干。
- 合理节奏: 1 个 spec PR + 1 个 audit PR + 1 个 minimal implementation PR, 中间必须有 Hermes verdict。
- 若 D-VAULT-001/003 质量足够, 24h 内最可行动的是 contract 草稿, 不是 flip。

## §3 Pre-flight 5 步

### §3.1 Step 1: task-index 注册

- 注册一个 T-LANE-VAULT-XXX active row, 占 Active product lane 1/3。
- row 必须写 owner, scope, allowed paths, forbidden paths, validation。
- scope 只能写 true_vault_write contract / spec / prompt, 不包含 runtime_tools / dbvnext_migration / browser_automation。

### §3.2 Step 2: decision-log D-XXX 草稿

- D-XXX 草稿只记录「准备进入 true_vault_write authority-upgrade candidate path」。
- 草稿必须写明本文不是 current authority。
- 草稿必须列出: trigger, evidence URL, Hermes requirement, explicit user gate, remaining Hold lanes。

### §3.3 Step 3: Hermes pre-flight 外审 prompt

- Hermes 输入: spec PR draft + commander prompt skeleton + Check 1-6 evidence。
- Hermes 输出: V-PASS-CLEAR / V-PASS-CONCERN / V-PARTIAL / V-REJECT。
- Hermes 重点: secret leakage, frontmatter completeness, dry-run/rollback, cross-lane drift。

### §3.4 Step 4: CC1 commander prompt v1 草稿

- CC1 把 §5 skeleton 填实为 paste-ready Codex prompt。
- prompt 必含 no-goals: no runtime, no migration, no browser automation, no full signal workbench。
- prompt 必含 closeout: evidence URL + remaining Hold。

### §3.5 Step 5: 磊哥显式授权 + paste Codex

- 只有当 spec PR draft + Hermes verdict + commander prompt v1 都 ready, 才进入磊哥显式授权。
- 授权文本必须指向具体 lane 与具体 PR / prompt, 不接受泛化授权。
- Codex 执行后由 Authority writer 做 closeout, 本文不替代该流程。

## §4 Dispatch templates
### D-VAULT-001 — vault commit 完整 frontmatter contract spec PR
- id: `D-VAULT-001`
- status: candidate
- parent_lane: `true_vault_write`
- dependency: 无; 起手只读 bridge/vault/current truth
- TL;DR: 把 raw 4-field preview 扩展为 commit 前 12 字段 completeness contract, 仍保持 candidate-only。
- 输入包:
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/00-START-HERE.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/decision-log.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/memory/INDEX.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/locked-principles.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/contracts-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/scoutflow_api/bridge/config.py
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/scoutflow_api/bridge/SPEC.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/scoutflow_api/bridge/router.py
- 输出 deliverable:
  - `docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/dispatch-packets/D-VAULT-001-frontmatter-contract-candidate.md`
- 验收标准:
  - 12 字段字段表完整; 每字段有来源、是否必填、失败策略
  - 明确 preview contract 与 commit contract 的差异
  - 不把 contract 写成已有 authority
- 反模式 REGENERATE:
  - REGENERATE: 字段表暗示 commit 已可执行
  - REGENERATE: 把 raw cookie/token 放入 frontmatter
  - REGENERATE: 省略 missing-field fail-loud 行为
- pre-flight check:
  - 读取 Check 1-6 真态
  - 确认 bridge config 两处 write_enabled=False
  - 确认 Bridge SPEC commit-specific extra gates
  - 确认 current 仍列 true_vault_write Hold
- self-verification:
  - frontmatter 12 字段逐项覆盖
  - 无本地路径硬编码
  - 无 secret-like 示例值
  - 每个字段有 rejection reason
  - candidate 声明出现于标题/frontmatter/正文/closeout
### D-VAULT-002 — 跨 7 阶段 pipeline 通过性 spec + RI test
- id: `D-VAULT-002`
- status: candidate
- parent_lane: `true_vault_write`
- dependency: D-VAULT-001 完成; 不依赖 runtime_tools 真运行
- TL;DR: 定义 raw → metadata → ASR → rewrite → trust trace → frontmatter → commit 的 evidence handoff 形状, 只做 contract/RI 描述。
- 输入包:
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/00-START-HERE.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/decision-log.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/memory/INDEX.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/locked-principles.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/contracts-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/scoutflow_api/bridge/config.py
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/scoutflow_api/bridge/SPEC.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/scoutflow_api/bridge/router.py
- 输出 deliverable:
  - `docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/dispatch-packets/D-VAULT-002-seven-stage-contract-candidate.md`
- 验收标准:
  - 7 阶段每阶段有输入证据、输出证据、stop condition
  - 明确 runtime_tools 未解禁时用 placeholder evidence
  - RI 描述不触发 migration
- 反模式 REGENERATE:
  - REGENERATE: 把七阶段通过性写成真 e2e 已通过
  - REGENERATE: 隐性依赖 ASR/runtime 已可用
  - REGENERATE: 把 RI test 写成 migration
- pre-flight check:
  - 复核 master spec §3 七阶段
  - 读取 current runtime blocked 段
  - 确认 no execution approval
  - 列出每阶段 required artifact type
- self-verification:
  - 每阶段 has owner
  - 每阶段 has blocker
  - 每阶段 has rollback note
  - 未跨 lane 解禁
  - 未写实现代码
### D-VAULT-003 — secret scan 强 pattern + exclude rule spec
- id: `D-VAULT-003`
- status: candidate
- parent_lane: `true_vault_write`
- dependency: D-VAULT-001 字段 contract ready
- TL;DR: 定义 vault commit 前 secret leakage gate, 覆盖 token/cookie/header/auth sidecar/raw stdout 等不可入库证据。
- 输入包:
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/00-START-HERE.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/decision-log.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/memory/INDEX.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/locked-principles.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/contracts-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/scoutflow_api/bridge/config.py
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/scoutflow_api/bridge/SPEC.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/scoutflow_api/bridge/router.py
- 输出 deliverable:
  - `docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/dispatch-packets/D-VAULT-003-secret-scan-contract-candidate.md`
- 验收标准:
  - secret pattern 分级清晰
  - exclude rule 只允许 harmless examples
  - credential material never evidence 原则被逐条映射
- 反模式 REGENERATE:
  - REGENERATE: 把 exclude rule 写成万能豁免
  - REGENERATE: 允许 raw credential 作为审计证据
  - REGENERATE: 把 redaction 后文本误写为可恢复 secret
- pre-flight check:
  - 读取 LP-SEC-001
  - 读取 raw-response-redaction contract
  - 读取 bridge SPEC security rules
  - 复核 current credential forbidden 段
- self-verification:
  - 每类 secret has rejection
  - exclude rule has rationale
  - 输出只含 safe examples
  - 无凭据形态样例
  - Hermes 维度覆盖 secret leakage
### D-VAULT-004 — dry-run + rollback contract
- id: `D-VAULT-004`
- status: candidate
- parent_lane: `true_vault_write`
- dependency: D-VAULT-001/002 完成
- TL;DR: 把 preview、dry-run commit、operator confirmation、rollback receipt 分层, 防止 partial commit 与不可逆误解。
- 输入包:
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/00-START-HERE.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/decision-log.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/memory/INDEX.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/locked-principles.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/contracts-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/scoutflow_api/bridge/config.py
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/scoutflow_api/bridge/SPEC.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/scoutflow_api/bridge/router.py
- 输出 deliverable:
  - `docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/dispatch-packets/D-VAULT-004-dry-run-rollback-candidate.md`
- 验收标准:
  - dry-run 与 true write 的 response contract 分离
  - rollback path 明确何时可用 / 不可用
  - partial commit 有 stop-the-line 规则
- 反模式 REGENERATE:
  - REGENERATE: 把 rollback 说成总能恢复历史
  - REGENERATE: 绕过 operator confirmation
  - REGENERATE: commit 失败后继续推进 promotion_state
- pre-flight check:
  - 读取 bridge commit dry-run route
  - 读取 vault SPEC carry-forward
  - 确认 write_enabled=False
  - 列出 failure modes
- self-verification:
  - 每个 failure mode has remediation
  - rollback 不承诺不可实现能力
  - dry-run evidence 与 true write evidence 分开
  - 无运行命令
  - 无 path hard-code
### D-VAULT-005 — write_enabled flip spec PR + commander prompt
- id: `D-VAULT-005`
- status: candidate
- parent_lane: `true_vault_write`
- dependency: D-VAULT-001~004 + Hermes V-PASS + 磊哥显式授权候选
- TL;DR: 仅在完整证据齐备后, 起草最小 flip PR 方案与 Codex commander prompt; flip 本身不由本文执行。
- 输入包:
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/00-START-HERE.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/decision-log.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/memory/INDEX.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/locked-principles.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/contracts-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/scoutflow_api/bridge/config.py
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/scoutflow_api/bridge/SPEC.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/scoutflow_api/bridge/router.py
- 输出 deliverable:
  - `docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/dispatch-packets/D-VAULT-005-flip-commander-skeleton-candidate.md`
- 验收标准:
  - flip scope 最小化
  - 明确其它 4 overflow lane 仍 Hold
  - commander prompt 含 secret scan / frontmatter / rollback gates
- 反模式 REGENERATE:
  - REGENERATE: 把 flip PR 当自动批准
  - REGENERATE: 同时修改 migrations/runtime/browser lane
  - REGENERATE: 省略 Hermes 外审
- pre-flight check:
  - 复核前 4 dispatch 完成状态
  - 读取 current Active slot
  - 读取 decision-log latest D-XXX
  - 确认 Hermes verdict
- self-verification:
  - scope 只含 lane 1
  - no hidden lane dependency
  - closeout plan present
  - no implementation detail beyond skeleton
  - candidate label intact
### D-VAULT-006 — lane closeout writeback packet
- id: `D-VAULT-006`
- status: candidate
- parent_lane: `true_vault_write`
- dependency: D-VAULT-005 完成后由 Authority writer 接管
- TL;DR: 提供 closeout 文案包: 做了什么、证据、剩余 Hold、风险, 但本 dispatch 不直接写 authority 文件。
- 输入包:
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/00-START-HERE.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/decision-log.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/memory/INDEX.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/locked-principles.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/contracts-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/scoutflow_api/bridge/config.py
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/scoutflow_api/bridge/SPEC.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/scoutflow_api/bridge/router.py
- 输出 deliverable:
  - `docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/dispatch-packets/D-VAULT-006-closeout-packet-candidate.md`
- 验收标准:
  - closeout packet 清晰区分 candidate / promoted / current authority
  - 包含 evidence URL 列表
  - 列出其它 lane Hold
- 反模式 REGENERATE:
  - REGENERATE: 把 closeout packet 自称 authority writeback
  - REGENERATE: 遗漏 remaining Hold
  - REGENERATE: 未标 PR/SHA 历史参考
- pre-flight check:
  - 读取 Check 1-6 新真态
  - 汇总 PR URL / commit URL / Hermes URL
  - 复核 Active/Writer slot
  - 确认 no local path references
- self-verification:
  - closeout 有 no-goals
  - 风险矩阵更新
  - candidate label 未漂移
  - Authority writer handoff 明确
  - self-flag 已列不确定项
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
在 true_vault_write 已获得完整 pre-flight 与显式授权后, 以最小 scope 完成 vault commit write path 的 contract enforcement / dry-run-to-write transition / closeout evidence。
### §5.4 §2 Inputs
- master spec §16 / §14.2 / §16.3
- current/task-index/decision-log raw URLs
- bridge config / SPEC / router raw URLs
- locked principles LP-SEC-001
- memory INDEX L-AUTHORITY-DRIFT + L-RUNTIME-APPROVAL-DRIFT
### §5.5 §3 Hard Boundaries
- 仍不打开 runtime_tools / browser_automation / dbvnext_migration / full_signal_workbench
- 不写 credential material; 不把 raw token/cookie 作为 evidence
- 不改 PlatformResult / WorkerReceipt / Trust Trace DTO
- 不创建 worker 或 package surface
- 任何 path 由 contract 派生, 不 hard-code
### §5.6 §4 N-phase 执行计划 + dispatch 列表
- Phase 1: frontmatter 12 字段 contract lock
- Phase 2: secret scan + exclude rule lock
- Phase 3: dry-run + rollback evidence lock
- Phase 4: minimal flip PR with test evidence
- Phase 5: closeout packet + remaining Hold readback
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
- secret leakage scan strictness and harmless exclude rule
- frontmatter contract 12 字段完整性
- write_enabled invariant before/after flip and other lane Hold
- vault commit reversibility / rollback realism
- RAW boundary and credential material never evidence
- preview / dry-run / true write semantic separation
- cross-lane drift detection
### §6.5 audit output schema
| Dimension | Finding | Severity | Required revision | Evidence URL |
|---|---|---|---|---|
| `<dimension>` | `<finding>` | `<C/H/M/L>` | `<revision>` | `<raw URL / PR URL>` |
Final verdict: `<V-PASS-CLEAR | V-PASS-CONCERN | V-PARTIAL | V-REJECT>`
Hermes signoff: `<name / timestamp / caveat>`
## §7 Lane-specific 反模式

1. REGENERATE: 把 vault preview target 当 true commit target。
2. REGENERATE: 跳过 frontmatter completeness check 直接进入 write path。
3. REGENERATE: secret scan 只做弱 pattern, 或允许 credential material 作为 evidence。
4. REGENERATE: 把 raw cookie / token / auth sidecar 写进 markdown / vault / tracked doc。
5. REGENERATE: 说 rollback 总能恢复, 但没有 dry-run proof / rollback receipt。
6. REGENERATE: true_vault_write flip 同时改 runtime / migration / browser 自动化边界。
7. REGENERATE: 把 current.md 内 stale main SHA 当最新真态, 不跑 §0.5 Check。
8. REGENERATE: closeout 不列 remaining Hold lanes。
9. REGENERATE: output deliverable 把 authority files 当本文写入目标。


## §8 Self-flag

### §8.1 GPT Pro 不确定的取舍点

  - ⚠️ D-VAULT-002 七阶段 contract 是否应拆为 4+3 两个 dispatch, 取决于 CC1 对 pipeline proof 粒度的偏好。
  - ⚠️ 12 字段 frontmatter 的最终字段名可能要跟 PRD-v3/SRD-v3 future promoted path 对齐, 本文只给 upgrade roadmap。
  - ⚠️ rollback 能力边界取决于 RAW vault 下游同步方式, 本文只能要求 evidence, 不能证明具体实现。

### §8.2 GPT Pro 弱项

  - ⚠️ 未读取完整 decision-log tail, 仅通过 PR #247 metadata 确认 D-017 follow-up; 需 CC0/CC1 接收时复核。
  - ⚠️ 没有运行本地 secret scan 或 vault preview; 本文只做 candidate roadmap。
  - ⚠️ ZIP audit pack为 2026-05-05 历史 reference, 未作为 2026-05-07 main truth 主源。

### §8.3 待磊哥拍板取舍点

  - 🟡 是否把 frontmatter contract 拆成独立 promoted addendum PR, 还是并入 lane spec PR。
  - 🟡 true write 首次试点是否只允许单 capture canary, 还是允许小批量。
  - 🟡 rollback 失败时是否要求人工 vault cleanup gate。
  - 🟡 lane 1 是否必须等待 lane 2/4 任一 evidence, 还是可先做 preview-to-commit shell。

### §8.4 Self-verification result

- 5 份 markdown 1-to-1 mapping 已生成; 本文件为 `true_vault_write`。
- frontmatter 已含 status / authority / authority_state / created_by / parent_cluster / lane / prerequisite_check / disclaimer。
- 已包含 §0.5 + §1-§8 全段落。
- Dispatch 数量在 5-7 范围内, 每个 dispatch 含 standard schema。
- 未写实现模块代码、真 migration SQL、浏览器脚本或运行命令。
- 未把本 lane 写成 current authority, 未声明 lane 已完成解禁。
- 输出 deliverable 清单未把 authority files 作为本文件写入目标。
- 未引用被禁止的本地 home 路径, 未假设本地 shell 命令。
