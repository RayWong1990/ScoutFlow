# PRD — ChatGPT 与本地 Agent 协作机制

> 目标路径：`example/PRD-chatgpt-local-agent-collaboration-v0.1-2026-05-03.md`  
> 文档类型：Product Requirements Document（PRD）  
> 版本：v0.1 Draft  
> 日期：2026-05-03  
> 适用项目：ScoutFlow / 采集线  
> 范围：GitHub-as-Queue Harness；ChatGPT Web 与本地 Codex / Local Agent 协作  
> 写入边界：仅 `example/`；不触碰产品代码；不修改 authority docs

---

## 0. 一句话定义

本 PRD 定义一套 **ChatGPT Web 负责派发、审计、解释；本地 Agent 负责稳定写入、执行、验证；GitHub 负责队列、事件日志、PR 审计与合并凭证** 的协作机制。

核心原则：

```text
Web ChatGPT = Planner / Dispatcher / Auditor
Local Agent = Writer / Worker / Validator
GitHub Issue = Task Queue
GitHub Issue Comment = Event Log
GitHub Branch = Isolated Workspace
GitHub PR = Review Artifact
GitHub Actions = Validation Proof
Human = Final Gate
```

---

## 1. 背景与问题

### 1.1 已验证事实

当前 ScoutFlow 项目已经验证过以下基础能力：

1. GitHub Issue 可以承载结构化任务消息。
2. GitHub Issue Comment 可以承载 append-only 事件流。
3. 本地 Codex / runner 可以领取、执行并回写事件。
4. 重复执行时可以识别 `already_completed`，具备基础幂等能力。
5. Web ChatGPT 可以读取 GitHub 真源，并给出审计、任务拆解和下一步 prompt。
6. GitHub Connector 在部分会话中可直接通过 API 创建文件、提交 commit、创建 issue / PR。

### 1.2 需要解决的问题

过去协作链路里的不稳定点集中在：

| 问题 | 具体表现 | 影响 |
|---|---|---|
| Web ChatGPT 写入能力不稳定 | 不同会话工具暴露不一致；有时能写，有时只能读 | 不能把 Web ChatGPT 当唯一稳定 writer |
| 本地 agent 状态不可见 | 本地执行中断后，聊天里看不到事实进度 | 用户无法判断任务是否完成 |
| 多 agent 写入冲突 | 多个 agent 同时修改 authority 文件 | 容易覆盖、漂移、失真 |
| 任务重复执行 | 同一 issue 被重复领取 / 重复创建 PR | 增加清理成本 |
| 审计依赖口述 | 聊天摘要替代 GitHub 真源 | 无法追踪 commit / diff / CI |
| 直接执行外部命令风险 | Issue body 中携带任意 shell | 安全边界失控 |

### 1.3 本 PRD 的定位

本 PRD 不是 ScoutFlow 产品功能 PRD，而是 **agent 协作 harness PRD**。它定义最小可执行协作协议，用来支撑后续 ScoutFlow 的多 agent 工程流程。

---

## 2. 目标与非目标

### 2.1 目标

本阶段目标：

1. 在 `example/` 内沉淀 ChatGPT 与本地 Agent 协作机制文档。
2. 明确 Web ChatGPT、本地 Codex、本地 runner、sidecar agent、人类 gate 的职责边界。
3. 定义 GitHub Issue Queue + Comment Event Log + Branch + PR + Actions 的对象模型。
4. 定义最小状态机、幂等规则、claim / lease 规则和安全 guardrails。
5. 为后续 `T-P0-005 GitHub Queue Harness Hardening` 提供需求依据。
6. 不进入产品代码；不新增真实 `codex exec` 自动执行能力。

### 2.2 非目标

本阶段明确不做：

- 不接真实 `codex exec` 自动执行。
- 不创建 daemon / long-running worker。
- 不把 Issue body 当 shell 脚本执行。
- 不允许 Web ChatGPT 作为唯一稳定主写入器。
- 不修改 `apps/`、`services/`、`workers/`、`packages/`、`data/`、`referencerepo/` 等产品或数据路径。
- 不修改 `docs/current.md`、`docs/task-index.md` 等 authority docs，除非后续单独 task 明确授权。
- 不引入外部 SaaS 队列。

---

## 3. 用户与角色

### 3.1 用户

本 PRD 的唯一最终用户是 ScoutFlow 项目所有者本人。用户承担最终 gate：授权、合并、废弃、回滚、进入下一阶段。

### 3.2 角色分工

| 角色 | 定位 | 允许做 | 默认禁止 |
|---|---|---|---|
| User | Final Gate | 拍板、授权、合并、关闭任务 | 无 |
| Web ChatGPT | Planner / Dispatcher / Auditor | 读 GitHub 真源、生成任务 JSON、审计 PR、输出修复 prompt | 作为唯一稳定主 writer |
| Local Codex | Main Writer | 修改文件、运行测试、提交 commit、创建 PR、回写事件 | 绕过 issue / PR / validation |
| Local Runner / Harness | Queue Worker | 领取任务、校验 schema、生成 Codex prompt、执行白名单流程 | 执行 Issue 中的任意 shell |
| Claude / OpenClaw / Hermes / Kimi | Sidecar Reviewer | 研究、反驳、总结、patch suggestion、issue comment | 直接修改 authority docs |
| GitHub | Audit Source / Message Bus | 保存 issue、comment、branch、PR、CI 结果 | 替代人类决策 |

---

## 4. 核心协作架构

### 4.1 总体架构

```text
┌──────────────────────────────────────────────┐
│ User / Final Gate                             │
│ approve / merge / abort / escalate            │
└──────────────────────────────────────────────┘
                    │
                    ▼
┌──────────────────────────────────────────────┐
│ Web ChatGPT                                   │
│ plan / dispatch / audit / explain             │
└──────────────────────────────────────────────┘
                    │ GitHub API / Connector
                    ▼
┌──────────────────────────────────────────────┐
│ GitHub                                        │
│ issue queue / comment log / branch / PR / CI  │
└──────────────────────────────────────────────┘
                    │ poll / claim / push
                    ▼
┌──────────────────────────────────────────────┐
│ Local Harness + Codex                         │
│ validate / write / test / commit / report     │
└──────────────────────────────────────────────┘
```

### 4.2 为什么 GitHub 作为消息总线

GitHub 不是传统意义的队列系统，但非常适合当前阶段：

- 权限已经打通。
- Issue / Comment / PR / Commit 天然可审计。
- 每个动作都有时间戳、操作者、URL 和历史记录。
- 可以天然承载人类 review gate。
- 可以用 label、assignee、state、comment marker 表达任务状态。
- 不需要额外部署 Redis / RabbitMQ / Temporal / n8n。

### 4.3 为什么不让 Web ChatGPT 直接长期写代码

即使某些会话可以通过 GitHub Connector 写入文件，也不应把 Web ChatGPT 设计成唯一 writer：

1. 工具暴露不稳定：不同会话、不同连接状态下，写工具可能不可用。
2. 执行环境不可控：无法稳定运行 repo 内测试、lint、build。
3. 上下文易漂移：聊天摘要不等于 GitHub 真源。
4. 并发风险高：多个会话同时写 main 容易造成污染。

因此稳定路径是：

```text
Web ChatGPT 负责决策、派单、审计；
Local Codex / Local Harness 负责执行、验证、提交；
GitHub 保存事实；
User 最终拍板。
```

---

## 5. 对象模型

### 5.1 GitHub Issue = Task Queue Item

每个任务用一个 GitHub Issue 表示，Issue body 采用结构化 YAML / JSON block。

建议字段：

```yaml
task_id: T-P0-005
title: GitHub Queue Harness Hardening
priority: P0
status: queued
scope:
  allowed_paths:
    - scripts/github-queue/**
    - docs/prompts/**
  forbidden_paths:
    - apps/**
    - services/**
    - workers/**
    - packages/**
    - data/**
    - referencerepo/**
actor_policy:
  primary_writer: local-codex
  auditor: web-chatgpt
  final_gate: user
validation:
  required:
    - npm run docs:check
    - unit tests for parser/idempotency
outputs:
  - branch
  - pr
  - audit note
```

Issue 标签建议：

| Label | 含义 |
|---|---|
| `queue:ready` | 可领取 |
| `queue:claimed` | 已领取 |
| `queue:running` | 执行中 |
| `queue:blocked` | 阻塞 |
| `queue:done` | 已完成 |
| `agent:codex` | 由本地 Codex 执行 |
| `audit:requested` | 等待 ChatGPT / Codex 审计 |
| `scope:docs-only` | 仅文档 |

### 5.2 Issue Comment = Event Log

Issue comment 是 append-only 事件流，不应频繁编辑旧 comment。

事件 marker：

```text
<!-- scoutflow:event:v1 -->
```

事件示例：

```json
{
  "event": "claimed",
  "task_id": "T-P0-005",
  "agent": "local-codex",
  "run_id": "2026-05-03T08-10-00Z-local-codex",
  "lease_until": "2026-05-03T09:10:00Z",
  "base_branch": "main",
  "target_branch": "task/T-P0-005-github-queue-hardening"
}
```

### 5.3 Branch = Isolated Workspace

分支命名：

```text
task/<task-id>-<slug>
```

示例：

```text
task/T-P0-005-github-queue-hardening
task/T-P0-006-local-harness-skeleton
```

规则：

- 每个任务一个主分支。
- 同一任务重复执行时优先复用原分支。
- 不允许直接开发到 `main`，除非用户明确要求 docs-only smoke / example smoke。
- task 分支合并后可保留到阶段末，再批量清理。

### 5.4 Pull Request = Review Artifact

PR 是审计单元，不只是合并入口。

PR body 必须包含：

```markdown
## Task
- Issue: #<id>
- Task ID: T-P0-005

## Scope
- Allowed paths:
- Modified paths:

## Changes
- ...

## Validation
- [ ] docs check
- [ ] unit tests
- [ ] manual verification

## Risk
- ...

## Agent Notes
- Writer:
- Auditor:
- Known limitations:
```

### 5.5 GitHub Actions = Validation Proof

CI 不应只作为“能不能合并”的判断，还应成为审计证据。

最低要求：

- docs-only task 至少跑 markdown / link / repository hygiene check。
- code task 至少跑 lint + unit test + type check。
- worker / harness task 必须包含 golden case。

---

## 6. 状态机

### 6.1 最小状态

```text
queued
  ↓
claimed
  ↓
running
  ↓
completed
  ↓
audit_requested
  ↓
audited
  ↓
merged / rejected / followup_required
```

### 6.2 状态说明

| 状态 | 说明 | 允许转移 |
|---|---|---|
| `queued` | 任务已创建，等待领取 | claimed / cancelled |
| `claimed` | 某 agent 获得 lease | running / expired / released |
| `running` | 本地执行中 | completed / blocked / failed |
| `completed` | 本地已完成提交或 PR | audit_requested |
| `audit_requested` | 等待审计 | audited / followup_required |
| `audited` | 审计完成 | merged / rejected / followup_required |
| `merged` | PR 已合并或 main 已更新 | closed |
| `rejected` | 任务不采纳 | closed |
| `followup_required` | 需要补丁或新任务 | queued / closed |

### 6.3 Claim / Lease 规则

为了避免多 agent 抢同一个任务，采用 lease：

```json
{
  "event": "claimed",
  "agent": "local-codex",
  "run_id": "uuid-or-timestamp",
  "lease_until": "2026-05-03T09:10:00Z"
}
```

规则：

1. 只有 `queue:ready` 或 lease 过期的任务可领取。
2. 领取后必须写入 `claimed` event。
3. 默认 lease 建议 60 分钟。
4. 执行超过 lease 需续租 comment。
5. 其他 agent 看到有效 lease 必须跳过。
6. 如果任务已出现 `completed` event，重复 runner 必须返回 `already_completed`。

### 6.4 幂等规则

幂等检查顺序：

```text
1. 读取 issue comments
2. 查找最新 scoutflow:event:v1
3. 如果存在 completed / merged → 不重复执行
4. 如果存在 active claimed lease → 不抢占
5. 如果 branch 已存在 → 复用 branch，禁止创建同名冲突分支
6. 如果 PR 已存在 → 更新原 PR，不新建重复 PR
```

---

## 7. 安全边界

### 7.1 禁止把 Issue 当 shell

Issue body 中可以描述任务，但不允许直接包含“可执行 shell 即真源”。

禁止：

```yaml
run: rm -rf data && npm install && curl ...
```

允许：

```yaml
intent: add parser golden tests
allowed_commands:
  - npm run test:queue
  - npm run docs:check
```

本地 harness 必须把命令映射到白名单，而不是执行任意字符串。

### 7.2 路径白名单

初始阶段只允许：

```text
example/**
docs/prompts/**
docs/audits/**
docs/dispatch/**
scripts/github-queue/**
.github/workflows/docs-check.yml
```

默认禁止：

```text
apps/**
services/**
workers/**
packages/**
data/**
referencerepo/**
.env
*.key
*.pem
```

### 7.3 Secret Redaction

任何 issue/comment/PR body 写入前必须检查：

- `OPENAI_API_KEY`
- `ANTHROPIC_API_KEY`
- `GITHUB_TOKEN`
- `GH_TOKEN`
- `sk-`
- `ghp_`
- `github_pat_`
- 私钥块：`BEGIN PRIVATE KEY`

命中时必须 reject 或 redact。

### 7.4 Authority Docs 保护

以下文件视作 authority docs，默认禁止 agent 直接改：

```text
docs/current.md
docs/task-index.md
docs/decisions.md
docs/SRD-*.md
docs/PRD-*.md
AGENTS.md
```

如需修改，必须单独任务、单独 PR、单独审计。

---

## 8. Web ChatGPT 工作流

### 8.1 派单流程

```text
User 提出目标
  ↓
Web ChatGPT 读取 GitHub 真源
  ↓
生成任务拆解 / Prompt Dispatch
  ↓
创建或建议创建 GitHub Issue
  ↓
本地 Agent 领取任务
```

Web ChatGPT 输出任务时必须包含：

- task id
- goal
- scope
- allowed paths
- forbidden paths
- acceptance criteria
- validation command
- expected deliverables
- rollback notes

### 8.2 审计流程

```text
Local Agent 提交 PR
  ↓
Web ChatGPT 读取 PR diff / commits / CI
  ↓
输出 audit report
  ↓
若可接受：建议 merge
  ↓
若不可接受：输出修复 prompt
```

审计报告必须包含：

- 结论：approve / request changes / block
- 风险等级：P0 / P1 / P2 / P3
- 证据：commit、changed files、CI 状态
- 问题清单：按严重度排序
- 修复建议：可直接交给 Codex 的 prompt

---

## 9. Local Agent / Harness 工作流

### 9.1 领取任务

```text
poll queue:ready issues
  ↓
read latest event comments
  ↓
check lease and completed state
  ↓
append claimed event
  ↓
create/reuse task branch
```

### 9.2 执行任务

```text
validate scope
  ↓
generate codex prompt
  ↓
apply changes
  ↓
run validation
  ↓
commit
  ↓
push branch
  ↓
create/update PR
  ↓
append completed event
```

### 9.3 回写事件

完成事件示例：

```json
{
  "event": "completed",
  "task_id": "T-P0-005",
  "agent": "local-codex",
  "branch": "task/T-P0-005-github-queue-hardening",
  "commit": "<sha>",
  "pr": 12,
  "validation": {
    "docs_check": "passed",
    "unit_tests": "passed"
  },
  "notes": "No product code touched."
}
```

---

## 10. MVP 需求

### 10.1 功能需求

| ID | 功能 | 描述 | 优先级 |
|---|---|---|---|
| F-001 | Issue schema parser | 解析任务 issue 中的结构化字段 | P0 |
| F-002 | Event log reader | 读取 issue comments 并识别最新状态 | P0 |
| F-003 | Claim / lease | 支持领取、续租、过期判断 | P0 |
| F-004 | Idempotency guard | 避免重复执行已完成任务 | P0 |
| F-005 | Scope validator | 检查变更路径是否越权 | P0 |
| F-006 | Branch manager | 创建 / 复用 task branch | P1 |
| F-007 | PR manager | 创建 / 更新 PR | P1 |
| F-008 | Validation runner | 执行白名单测试命令 | P1 |
| F-009 | Audit summary generator | 生成给 Web ChatGPT 的审计摘要 | P2 |

### 10.2 非功能需求

| 类别 | 要求 |
|---|---|
| 可审计性 | 所有关键动作必须落 GitHub comment / commit / PR |
| 可回放 | 同一 issue 可重新读取并恢复状态 |
| 幂等性 | 重跑不应制造重复 PR / 重复 commit |
| 可中断 | 本地 runner 中断后可由 lease 过期恢复 |
| 最小权限 | 默认 docs-only；产品代码需单独授权 |
| 可解释 | 每个 PR body 必须写清楚任务来源、范围、验证 |

---

## 11. 验收标准

### 11.1 文档级验收

本 PRD 文件满足：

- 位于 `example/` 目录。
- 不修改产品代码。
- 明确 Web ChatGPT 与本地 Agent 的职责边界。
- 明确 GitHub Issue Queue / Comment Event Log / Branch / PR / CI 模型。
- 明确 claim / lease / idempotency / security guardrails。

### 11.2 后续工程验收

`T-P0-005` 之后的最小工程验收建议：

1. 创建一个 docs-only task issue。
2. 本地 harness 能读取 issue 并 claim。
3. 重复运行时不会重复 claim。
4. 本地 harness 能生成 task branch。
5. 本地 harness 能创建 PR。
6. PR body 包含 validation summary。
7. Web ChatGPT 能读取 PR 并产出 audit report。
8. 任务完成后 issue comment 中存在 `completed` event。
9. 再次运行返回 `already_completed`。

---

## 12. 后续路线

### 12.1 T-P0-005 — GitHub Queue Harness Hardening

目标：把当前 smoke 脚本升级为可靠 harness。

建议范围：

```text
scripts/github-queue/**
docs/prompts/**
docs/audits/**
example/**
```

重点：

- schema parser
- event parser
- lease handling
- idempotency
- redaction
- golden cases

### 12.2 T-P0-006 — Local Agent Execution Skeleton

目标：定义本地 agent 如何安全调用 Codex，但不接无限制自动执行。

重点：

- prompt file generation
- command allowlist
- dry-run mode
- output capture
- validation summary

### 12.3 T-P0-007 — PR Audit Protocol

目标：标准化 Web ChatGPT / Codex 对 PR 的审计报告格式。

重点：

- PR changed files checklist
- authority docs checklist
- branch hygiene checklist
- validation proof checklist
- merge / reject / followup 三态结论

---

## 13. 关键设计原则

1. **GitHub 真源优先**：聊天摘要只能辅助，不能替代 issue / commit / PR / CI。
2. **Web 规划，本地执行**：Web ChatGPT 优先做 planner / auditor，本地 agent 优先做 writer / validator。
3. **所有执行都要可审计**：没有 comment / commit / PR 记录的动作，不视作事实完成。
4. **默认 docs-only**：产品代码、authority docs、数据目录必须单独授权。
5. **重复运行必须安全**：幂等比速度重要。
6. **Issue 是任务，不是 shell**：任务描述可以结构化，但不能直接作为命令执行。
7. **人类最终拍板**：任何 agent 都不能替代用户做最终合并、废弃、回滚决策。

---

## 14. 当前结论

ScoutFlow 当前最适合采用以下协作范式：

```text
User 提目标
  ↓
Web ChatGPT 生成 PRD / prompt / audit checklist
  ↓
GitHub Issue 保存任务
  ↓
Local Agent claim + execute + validate
  ↓
GitHub PR 保存 diff 和 CI
  ↓
Web ChatGPT 审计
  ↓
User 决定 merge / followup / reject
```

这套范式可以把 ChatGPT 网页版的不稳定写入能力，转换成一个更稳的工程协作系统：**能写时可直接写小范围 docs；正式开发仍走本地 Agent + PR + CI。**

---

## 15. 变更记录

| 日期 | 版本 | 变更 |
|---|---|---|
| 2026-05-03 | v0.1 | 初版：定义 ChatGPT Web 与本地 Agent 协作机制、GitHub-as-Queue、状态机、边界与验收标准 |
