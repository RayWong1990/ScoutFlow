# ScoutFlow Step0 执行计划

> 执行说明：本计划供 `Codex Desktop`、`Claude Code / VSCode`、`OpenClaw`、`Hermes CLI` 读取。执行时必须遵守 `AGENTS.md`、`docs/current.md`、`docs/task-index.md`。步骤中的 checkbox 仅用于计划跟踪。
> 本文件是执行计划模板，不是完成记录。`- [ ]` 仅表示计划步骤，不代表本次审计修复未完成。

**Goal:** 在不写产品代码的前提下，收敛 ScoutFlow 的 Step0 入口文档、任务账本和开工安全 contract，让 Phase 0 / Phase 1A 具备可执行的文档真源。

**Architecture:** 本计划先把 PRD / SRD / 组织草案压缩成一层更窄的执行面：`current / task-index / AGENTS / CLAUDE + SRD amendment + contract pack`。ScoutFlow 当前还不是 git 仓库，因此 `T-P0-000` 只写文档；`git init`、根轻配置、目录骨架和后续 worktree 纪律由 `T-P0-001` 之后接手。

**Tech Stack:** Markdown、`rg`、`apply_patch`、PRD/SRD 文档对照、轻量 shell 验证

---

## 文件结构

- 创建 `AGENTS.md`：项目根的通用 agent 入口
- 创建 `CLAUDE.md`：Claude Code / VSCode 会话入口
- 创建 `docs/current.md`：当前活状态、允许区、禁止区、下一步
- 创建 `docs/task-index.md`：共享薄账本，Active 上限 `3`
- 创建 `docs/SRD-v1.1-amendment-2026-05-03.md`：A001-A015 开工安全补丁
- 创建 `docs/specs/contracts-index.md`：待拍板候选基准总索引
- 创建 `docs/specs/worker-receipt-contract.md`：Phase 1A 报账与台账协议
- 创建 `docs/specs/platform-adapter-risk-contract.md`：平台失败 typed contract
- 创建 `docs/specs/raw-response-redaction.md`：raw response 脱敏与凭据安全
- 创建 `docs/plans/step0-execution-plan.md`：本计划自身

## 执行说明

- 当前任务只写文档，不写 API / worker / Console
- 当前任务不修改 `data/` 与 `referencerepo/`
- 当前任务不创建项目根重治理目录
- 当前任务结束时不执行代码级验证；只做文档一致性与边界验证
- 当前仓库尚未 `git init`，因此本任务不做 commit；首个 checkpoint 由 `T-P0-001` 负责

### Task 1: 入口文档与任务账本

**Files:**
- Create: `AGENTS.md`
- Create: `CLAUDE.md`
- Create: `docs/current.md`
- Create: `docs/task-index.md`

- [ ] **Step 1: 写 `AGENTS.md`，锁阅读顺序、红线、允许路径和停线条件**

```md
# ScoutFlow AGENTS

## 进入项目先读
1. docs/current.md
2. docs/task-index.md
3. docs/specs/contracts-index.md
4. docs/plans/step0-execution-plan.md

## 当前阶段
- Phase 0 / Step0
- 当前只做文档与 contract
- Phase 2-4 只作参考 outline

## 当前红线
- 不改 data/
- 不改 referencerepo/
- recommendation / keyword / RAW gap 不直接创建 capture
- /captures/discover 是 capture 创建入口（capture creation entrypoint）
```

- [ ] **Step 2: 写 `CLAUDE.md`，给 Claude Code / VSCode 一个更窄的文档职责入口**

```md
# ScoutFlow CLAUDE

## 当前职责
- 文档审读
- SRD / PRD 冲突识别
- contract 校对

## 当前禁止
- 不写 API / worker / Console
- 不做浏览器自动化
```

- [ ] **Step 3: 写 `docs/current.md`，把当前 Phase、允许区、禁止区和下一步收紧到一页**

```md
# Current

## 当前状态
- Phase: 0
- Step: Step0
- 主任务: T-P0-000

## 当前允许
- docs/
- AGENTS.md
- CLAUDE.md

## 当前禁止
- apps/
- services/
- workers/
- packages/
- data/
- referencerepo/
```

- [ ] **Step 4: 写 `docs/task-index.md`，只保留 1 条 Active 和 3 条 Pending**

```md
# ScoutFlow Task Index

## Active
- T-P0-000

## Pending
- T-P0-001
- T-P0-002
- T-P0-003
```

- [ ] **Step 5: 验证入口文档只覆盖当前范围**

Run: `rg -n "Phase 2-4|capture creation entrypoint|T-P0-000" AGENTS.md CLAUDE.md docs/current.md docs/task-index.md`

Expected: 命中当前范围说明；`docs/task-index.md` 中 Active 仅 1 条

### Task 2: SRD 开工安全补丁

**Files:**
- Create: `docs/SRD-v1.1-amendment-2026-05-03.md`

- [ ] **Step 1: 写 amendment 头部，明确“这是补充修订，不是主体重写”**

```md
# SRD v1.1 Amendment — 2026-05-03

> 本文件是对 2026-05-02 amendment 的补充修订，不是 SRD 主体重写。
> 状态：DRAFT，待 user 拍板。
```

- [ ] **Step 2: 写 A001-A008，把旧 SRD 的冲突项收口到当前执行面**

```md
## A001 Authority Chain 修订
## A002 Claude Design 移除
## A003 Task Index
## A004 capture_mode / quick_capture_preset 命名统一
## A005 source_kind 命名统一
## A006 artifact_assets 命名残留修正
## A007 NFR 分级
## A008 Tool Roster 更新
```

- [ ] **Step 3: 写 A009-A015，把 Step0 真正缺的开工安全补丁补上**

```md
## A009 Tool Roster & Research Note Protocol
## A010 Phase Scope Freeze
## A011 Definition of Ready / Done / Stop-the-line
## A012 Capture Entry API Semantics
## A013 Worker Receipt & Artifact Ledger Contract
## A014 Platform Adapter Risk Contract
## A015 Raw Response Redaction & Credential Safety
```

- [ ] **Step 4: 在 amendment 里加最小机械 patch 清单和 user 拍板列表**

```md
## 对 base SRD 的最小机械修补清单
## 当前仍需 user 拍板
```

- [ ] **Step 5: 验证 amendment 同时覆盖 A001 与 A015，且没有把 Phase 2-4 拉进当前实现任务**

Run: `rg -n "A001|A015|Phase Scope Freeze|reference outline" docs/SRD-v1.1-amendment-2026-05-03.md`

Expected: 命中 A001-A015 与范围冻结内容；只把 Phase 2-4 写成参考 outline

### Task 3: Contract 索引与报账协议

**Files:**
- Create: `docs/specs/contracts-index.md`
- Create: `docs/specs/worker-receipt-contract.md`

- [ ] **Step 1: 写 `contracts-index.md`，把待拍板候选基准与参考 outline 分开**

```md
# ScoutFlow Contracts Index

## 待拍板候选基准
- Authority Chain
- Task Index
- Tool Roster
- Phase Scope Freeze
- Capture Entry API
- Worker Receipt
- Platform Adapter Risk
- Raw Response Redaction

## 仅作参考 outline
- Phase 1B
- Phase 2
- Phase 3
- Phase 4
```

- [ ] **Step 2: 写 `worker-receipt-contract.md`，锁 receipt 顶层字段、produced_assets 字段和 API 校验规则**

```md
# Worker Receipt 与 Artifact Ledger Contract

## Receipt 顶层字段
- job_id
- capture_id
- job_type
- producer
- idempotency
- platform_result
- produced_assets
- next_status

## produced_assets 字段
- zone
- artifact_kind
- relative_path
- sha256
- bytes
- redaction_applied
```

- [ ] **Step 3: 在 `worker-receipt-contract.md` 写一个 Phase 1A 最小 JSON 示例**

```json
{
  "job_id": "01HXJOB0001",
  "capture_id": "01HXCAP0001",
  "job_type": "metadata_fetch",
  "producer": "workers.bili",
  "platform_result": "ok",
  "produced_assets": []
}
```

- [ ] **Step 4: 验证 contract index 与 receipt contract 已建立交叉引用**

Run: `rg -n "Worker Receipt|artifact_assets|platform_result" docs/specs/contracts-index.md docs/specs/worker-receipt-contract.md`

Expected: 两个文件都命中相同 contract 关键词

### Task 4: 平台风险与脱敏协议

**Files:**
- Create: `docs/specs/platform-adapter-risk-contract.md`
- Create: `docs/specs/raw-response-redaction.md`

- [ ] **Step 1: 写 `platform-adapter-risk-contract.md`，把平台结果 typed 化**

```md
# Platform Adapter Risk Contract

## platform_result
- ok
- auth_required
- rate_limited
- forbidden
- not_found
- region_blocked
- vip_required
- parser_drift
- network_error
- timeout
- unavailable
- unknown_error
```

- [ ] **Step 2: 写当前允许的技术表面与当前禁止项**

```md
## 当前允许
- metadata fetch
- BBDown
- yt-dlp fallback
- ffmpeg

## 当前禁止
- 浏览器自动化
- 评论链路
- XHS / YouTube 真采集
```

- [ ] **Step 3: 写 `raw-response-redaction.md`，锁“凭据不是 evidence”**

```md
# Raw Response 脱敏与凭据安全规则

## 核心规则
- 凭据不是 evidence
- raw_api_response 必须是安全后的 response evidence

## 当前禁止保存
- Cookie
- Authorization
- Set-Cookie
- 完整 cookie jar
- 浏览器 profile
```

- [ ] **Step 4: 在 `raw-response-redaction.md` 写与 worker receipt 的联动字段**

```json
{
  "redaction_applied": true,
  "redaction_policy": "credentials-v1",
  "sensitive_fields_removed": ["headers.cookie", "headers.authorization"]
}
```

- [ ] **Step 5: 验证平台风险文档与脱敏文档都明确当前不做浏览器自动化**

Run: `rg -n "浏览器自动化|凭据不是 evidence|platform_result" docs/specs/platform-adapter-risk-contract.md docs/specs/raw-response-redaction.md`

Expected: 两个文件都命中当前边界与安全规则

### Task 5: 一致性复核与下阶段切分

**Files:**
- Modify: `docs/plans/step0-execution-plan.md`
- Review: `AGENTS.md`
- Review: `CLAUDE.md`
- Review: `docs/current.md`
- Review: `docs/task-index.md`
- Review: `docs/SRD-v1.1-amendment-2026-05-03.md`
- Review: `docs/specs/*.md`

- [ ] **Step 1: 复核所有新文档都使用中文，并且只描述当前生效范围**

Run: `rg -n "当前生效|reference outline|Phase 0|Phase 1A" AGENTS.md CLAUDE.md docs/current.md docs/task-index.md docs/SRD-v1.1-amendment-2026-05-03.md docs/specs/*.md`

Expected: 命中当前范围与 outline 区分

- [ ] **Step 2: 复核 `/captures/discover` 的语义在所有关键文件里一致**

Run: `rg -n "capture creation entrypoint" AGENTS.md docs/current.md docs/SRD-v1.1-amendment-2026-05-03.md docs/specs/contracts-index.md`

Expected: 所有关键文件都把该路由写成 capture 入口，而不是 discovery/search

- [ ] **Step 3: 复核新文档没有引入命名禁区，并且没有新增项目根重治理目录要求**

Run: `rg -n "candidates/|dispatches/|audits/" docs/plans/step0-execution-plan.md docs/SRD-v1.1-amendment-2026-05-03.md docs/task-index.md AGENTS.md CLAUDE.md`

Expected: 只在“不要建立”或“Phase 4 outline”语境中出现，不作为当前目录要求

- [ ] **Step 4: 记录 no-commit 例外，并把首个 checkpoint 交给 T-P0-001**

Run: `test -d .git && git status --short || echo "no-git-yet"`

Expected: 输出 `no-git-yet`
