# Parallel Execution Protocol

> 当前状态：`candidate baseline`
> 适用阶段：`Phase 0` 与 `Phase 1A` 准备阶段
> 本协议不等于批准 `Phase 1A` 产品代码实现。

## A. 目的

- 降低 user 在多个工具之间复制粘贴、人工转述和重复审计的成本。
- 用 GitHub commit / PR diff / workflow run 作为跨工具审计真源。
- 允许并行审读、研究、验证和 patch 建议，但保护 authority 文件不被多窗口互相覆盖。

## B. 核心原则

- `Single Writer`：每个任务只能有一个主写入窗口。
- `Multi Reviewer`：其他窗口可读、审、测试、研究、给 patch 建议。
- `GitHub as Audit Source`：commit / PR diff / workflow run 优先于聊天摘要。
- `Ledger First`：`docs/task-index.md` 与 `docs/current.md` 是任务状态 authority。
- `No Sidecar Authority Writes`：`OpenClaw` / `Hermes` / `Claude` sidecar 不直接写 authority，除非任务明确授权。
- `Branch Before Parallel`：进入多窗口并行后优先使用 `task/*` branch 或 PR，不直接 push `main`。
- `Human Gate`：user 保留合并、推进、越界判断权。

## C. 工具分工

| 工具 | 当前职责 | 默认边界 |
|---|---|---|
| `Codex Desktop` | 主写入者 / repo writer / commit owner，可调 subagent | 最终单点 commit；不得把 sidecar 输出原样当事实 |
| `Codex subagent` | 并行 code / doc scan、lint、diff review、风险列举 | 不独立写回 `docs/task-index.md` / `docs/current.md` |
| `网页版 GPT Pro` | GitHub 外部审计、prompt architect、PR / commit reviewer | 不直接改 repo |
| `Claude Code / VSCode` | 文档审读、IA / UX 评论、局部文案、contract 校对 | 不主导代码主线 |
| `OpenClaw / GLM` | 次级 research、竞品 / 资料 / 风险 note、反驳审读 | 默认 read-only |
| `Hermes Agent / Kimi` | 调度设计参考、长上下文归纳、任务拆解建议 | 默认 read-only |
| `user` | 选择任务、审批范围、处理合并、判断是否进入下一阶段 | 保留最终 gate |

## D. 并行模式

| 模式 | 说明 | 适用边界 |
|---|---|---|
| 串行模式 | 一个主 agent 执行，其他工具不参与 | 小范围文档或验证任务 |
| 单主多审模式 | 一个主写入，多个 sidecar 输出建议 | 默认推荐模式 |
| 多分支并行模式 | 多个 `task/*` 分支并行 | 不得改同一 authority 文件，除非事先约定 merge order |
| 审计模式 | 所有工具只读 GitHub commit / PR / run | 输出审计意见，不写回 repo |

## E. 文件写入规则

- `docs/current.md` 与 `docs/task-index.md` 只能由主写入窗口更新。
- `docs/decision-log.md` 只记录 user 已拍板或任务闭合的事实。
- `docs/specs/*` 可由主写入窗口合并 sidecar 建议。
- sidecar 输出若要落地，优先进入 `docs/research/`，再由主写入窗口择要合并。
- 不创建顶层 `candidates/`、`dispatches/`、`audits/`。
- 不写 API / worker / Console 产品代码。

## F. 派单模板

### 主写入 agent

```md
Task ID:
Mode:
Owner:
Allowed Paths:
Forbidden Paths:
Sidecar Roles:
Validation:
Commit / PR Rules:
Stop-the-line:
```

### Sidecar

```md
Read-only scope:
Questions:
Output format:
No write-back:
No authority mutation:
```

## G. Stop-the-line

- 多个 agent 同时改 `docs/current.md` 或 `docs/task-index.md`。
- sidecar 直接改 authority 文件。
- PR / branch 与 `main` 漂移且未 rebase。
- 任务范围外写产品代码。
- 外部研究被直接写成主线事实。
- 出现凭据、token、raw response 泄露。

## H. 当前状态

- 当前为 `candidate baseline`。
- 适用于 `Phase 0` 与 `Phase 1A` 准备阶段。
- 不等于批准 `Phase 1A` 产品代码实现。
