---
title: True Vault Write Authority-Upgrade Roadmap
status: candidate
authority: not-authority
authority_state: not-execution-approved
created_by: gpt-pro
parent_cluster: W4
lane: true_vault_write
prerequisite_check: refreshed_2026-05-08_live_check
master_spec_anchor: §16.1 (硬红线) + §16.2 (升级路径) + §14.2 (pre-flight) + §16.3 (风险矩阵)
disclaimer: |
  本文是 candidate authority-upgrade roadmap, 不是 lane 完成权限升级的证据.
  Lane 解禁需要走完整 §3 pre-flight 5 步 + Hermes 外审 V-PASS + 磊哥显式授权 + spec PR merge.
  本文内的 PR # / file path / SHA 标 "(撰写时刻历史参考, 真值以 §0.5 Check 为准)".
---

# True Vault Write Authority-Upgrade Roadmap

> 本文产出的是 true_vault_write 的 candidate authority-upgrade roadmap。它只定义合法升级路径, 不改变 `write_enabled=False` 真态, 不开启其它 overflow lane。

## §0.5 Prerequisite Check

> refreshed_at: `2026-05-08 live check in worktree`. 本段是本文件的真态读回锚, 任一后续 agent 接收本文时必须再次刷新, 不得把本文数值当永久 authority。

| Check | 刷新真态 | Drift / 处理 |
|---|---|---|
| 1 — `origin/main` | `45e88d45342ba6f6036e68695ca56d09deaaf06d`; message=`Merge pull request #257 from RayWong1990/codex/w4-b-step0-convergence` | 本文一切 PR / SHA 历史叙述以此 live truth 为准。更老的 `6dd27d7` / `c802de4` / `02ccbdc` 均仅作历史参考。 |
| 2 — docs redline | `python tools/check-docs-redlines.py` passed | 说明本窗允许路径、authority trio 禁区、lane file write-set 当前都未破。 |
| 3 — secrets redline | `python tools/check-secrets-redlines.py` passed | 说明 tracked 文本面暂无明显 credential pattern; 这不等于 lane 1 secret scan 已完成。 |
| 4 — current/task state | `docs/current.md` 与 `docs/task-index.md` 仍显示 Active `0/3`、Authority writer `0/1`、state=`WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED` | state 与 lane Hold 真态一致; 但 `docs/current.md` main anchor 仍落后于 live `origin/main`, 本文不写 authority 修复。 |
| 5 — bridge config | `services/api/scoutflow_api/bridge/config.py` 两个分支都返回 `write_enabled=False`; `frontmatter_mode="raw_4_field"` | 这是当前最硬的 lane 1 不变量; spec PR 只能围绕它收紧未来 contract。 |
| 6 — vault helper stack | `bridge/schemas.py` 只暴露 4 字段 `BridgeFrontmatter`; `BridgeVaultCommitResponse` 只有 dry-run 形状; `bridge/vault_commit.py` 固定返回 `committed=False`, `dry_run=True`, `write_enabled=False` | 现有 helper stack 仍是 preview / dry-run continuity, 不是 production writer。 |
| 7 — vault spec baseline | `services/api/scoutflow_api/vault/SPEC.md` 仍明确 raw 4-field frontmatter、`00-Inbox` containment、`write_disabled` error namespace | 12-field、secret scan、rollback 仍属未来 spec 必补项, 不能误写成现状已具备。 |

**读回证据包**: `git rev-parse origin/main`, `git log -1 --oneline origin/main`, `python tools/check-docs-redlines.py`, `python tools/check-secrets-redlines.py`, `services/api/scoutflow_api/bridge/config.py`, `services/api/scoutflow_api/bridge/schemas.py`, `services/api/scoutflow_api/bridge/vault_commit.py`, `services/api/scoutflow_api/vault/SPEC.md`, `services/api/scoutflow_api/vault/frontmatter.py`, `services/api/scoutflow_api/vault/commit.py`。

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

### §1.4A 现有 helper stack 真边界

- `BridgeVaultConfigResponse` 当前只允许 `frontmatter_mode="raw_4_field"`, 且 `write_enabled=False` 是字面硬约束, 不是运行时可协商状态。
- `BridgeFrontmatter` / `VaultFrontmatter` 当前只有 `title/date/tags/status` 四字段; 其它八个 commit-ready 槽位在本 PR 里只能定义 contract role, 不能伪装成现有 schema。
- `BridgeVaultPreviewResponse` 是 preview contract; `BridgeVaultCommitResponse` 只是 dry-run gate contract。两者都不携带真实 durable write receipt。
- `vault/commit.py` 当前只能从 preview 派生 `target_path` 和 dry-run ledger markdown, 没有原子写入、manifest 持久化、rollback receipt 或成功 commit code path。
- 因此 lane 1 本轮只能把「未来 true write 必须额外满足什么」写实, 不能把 preview helper 扩写为生产 writer 已存在。

### §1.4B 12-field commit-ready role contract

> 最终字段名允许留给后续 promoted path 对齐; 本 PR 锁的是 12 个 role slot, 不是强造今日代码字段名。

| Slot | 当前来源 | true-write 前必须满足 | 缺失时动作 |
|---|---|---|---|
| 1. `title` | 现有 `BridgeFrontmatter.title` | 保持单行、非空、可读 | block true-write; preview 可继续 |
| 2. `date` | 现有 `BridgeFrontmatter.date` | `YYYY-MM-DD` 且来源可追溯 | block true-write |
| 3. `tags` | 现有 `BridgeFrontmatter.tags` | 保持单值 contract 或明确未来升级策略 | block true-write |
| 4. `status` | 现有 `BridgeFrontmatter.status`=`pending` | 若未来变更, 必须由 lane 1 spec 显式声明 | block true-write |
| 5. `capture_id_role` | `capture.capture_id` | 能唯一回指 ScoutFlow capture ledger | block true-write |
| 6. `platform_item_id_role` | `capture.platform_item_id` | 能回指平台对象 | block true-write |
| 7. `canonical_url_role` | `capture.canonical_url` | 先过 secret scan / signed-query scan | block true-write |
| 8. `source_mode_role` | `source_kind` + `capture_mode` | 标清 evidence 来自 metadata_only / runtime / placeholder | block true-write |
| 9. `evidence_provenance_role` | 未来 runtime / transcript / rewrite receipt; 当前可为空占位 | runtime lane 未解禁时必须显式 `hold/placeholder`, 不得伪造通过 | block true-write |
| 10. `trust_trace_role` | 未来 trust-trace readback | 可为空占位, 但必须显式标 `hold` | block true-write |
| 11. `content_hash_role` | 未来 rendered markdown / manifest hash | 必须可复核, 不能只靠 chat 口头声称 | block true-write |
| 12. `commit_audit_role` | 未来 operator confirmation + scan verdict + rollback receipt | 必须能证明写前 gate、写后结果、失败处置 | block true-write |

### §1.4C dry-run response vs true-write response split

| Contract family | 当前 live 代码 | spec PR 必须锁定的未来要求 | 禁止漂移 |
|---|---|---|---|
| preview response | `BridgeVaultPreviewResponse` | 继续只表达 preview markdown、target path、4-field frontmatter、warnings | 不得写成 commit proof |
| commit dry-run response | `BridgeVaultCommitResponse` with `committed=false`, `dry_run=true`, `write_enabled=false`, `error.code=write_disabled` | 维持 gate-failed 语义, 作为 future true-write 前的负向证据 | 不得把 `dry_run=true` 文案改写成 almost-ready |
| future true-write response | 当前不存在 | 必须与 dry-run 分 schema family; 至少额外携带 12-field completeness verdict、secret scan verdict、content hash/manifest role、rollback receipt role、remaining Hold lanes readback | 不得复用 dry-run success wording; 不得仅靠 flip config 假装完成 |

### §1.4D secret scan contract

- 扫描面必须覆盖: frontmatter candidate 全字段、markdown body、`canonical_url`、summary/rewrite、transcript/quote excerpt、任何准备入 vault 的 receipt/manifest 片段。
- 阻断类命中至少包括: cookie、token、API key、auth header、signed query parameter、raw stdout/stderr、auth sidecar、可逆 redaction placeholder。
- 若 transcript / summary / runtime receipt 尚未产生, 只能写成 `not_present / blocked_by_lane_2`, 不能因为「暂时没有内容可扫」就偷算 scan passed。
- secret scan 输出本身也不能泄露 secret 本体; 只允许写类别、位置、是否已拒绝、是否需要人工复核。

### §1.4E atomic write + rollback contract

- future true-write 至少分 6 个 gate: completeness gate -> secret scan gate -> path containment/conflict gate -> render/hash gate -> atomic write gate -> receipt/rollback gate。
- `path_policy.py` 当前已证明 containment 只能落在 `${SCOUTFLOW_VAULT_ROOT}/00-Inbox/`; future write 也必须沿用这条边界, 不能顺手扩到别的 PARA subtree。
- `atomic write` 在本文只定义 contract intent: 不能留下半成品 markdown、orphan asset、或只写 body 没写 receipt 的中间态。
- `rollback` 在本文只允许承诺「有 receipt 支持的可证明回退路径」, 不允许写成“总能恢复历史”。若真实 vault 下游同步已吸收文件, lane 1 必须 stop-the-line 并升级为人工 cleanup gate。

### §1.4F remaining Hold lanes readback

- `runtime_tools` 仍 Hold: lane 1 不得声称 transcript、ASR、rewrite、vendor runtime evidence 已 ready。
- `dbvnext_migration` 仍 Hold: lane 1 不得把新增持久化字段写成 DB 已接好。
- `browser_automation` 与 `full_signal_workbench` 仍 Hold: lane 1 不得引用其运行证据做 unlock 证明。
- 因此 lane 1 spec PR 的合法结论只能是 contract-ready / flip-future-gated, 不能是 runtime-ready / migration-ready / full-signal-ready。

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
- lane 1 的 amend trigger 不是通用 wording 微调, 而是 6 类 stop-the-line 风险: secret leakage、frontmatter completeness drift、`write_enabled` truth drift、partial commit stage drift、credential material evidence drift、path containment uncertainty。
- 命中上述任一类时, 默认动作不是继续推进, 而是: stop -> redacted drift report -> CC0/CC1 review -> 决定 keep / rollback / defer / amend_and_proceed。
- `amend_and_proceed` 只允许用于 no-write 文档澄清, 不允许用于补 runtime proof、补 migration proof、或把 dry-run 解释成 true write。
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
