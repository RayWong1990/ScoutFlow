# Parallel Execution Protocol

> 当前状态：`Phase 0 / Phase 1A baseline`; Active product lane max=`3`; Authority writer max=`1`。
> 本协议允许并行研究 / 审读 / 验证，但保护 authority 文件不被多窗口覆盖。

## A. 目的

- 用 GitHub commit / PR diff / workflow run 作为跨工具审计真源。
- 允许并行审读、研究、验证和 patch 建议。
- 把 state drift 防线放在 authority writer 与 same-file conflict domain 上，而不是阻止所有并行 lane。

## B. 核心原则（修订）

- `Active product lane max = 3`
- `Active lane max = 3` — compatibility alias for promote / audit gate checks
- `Authority writer max = 1` — 永远只有一个窗口写 `docs/current.md` / `docs/task-index.md` / `docs/decision-log.md`
- `Single Writer` — `Authority writer max = 1` 的短名；用于兼容既有审计和 PR 模板措辞
- `Same file group writer max = 1` — 同 conflict domain 单写者
- `Review / audit / research lanes do not count as product active lanes` — 除非写 authority
- `GitHub as Audit Source` — 高风险或 material task 以 commit / PR diff / workflow run 为事实源
- `Ledger First` — 任务状态先写 `docs/task-index.md`，再写 `docs/current.md`
- `No Sidecar Authority Writes` — sidecar 不直接写 authority，除非任务明确授权
- `Branch Before Parallel` — 多窗口并行优先使用 `task/*` branch 或 PR
- `Human Gate` — user 保留合并、推进、越界判断权

## C. 工具分工

| 工具 | 当前职责 | 默认边界 |
|---|---|---|
| `Codex Desktop` | 主写入者 / repo writer / commit owner | 最终单点 commit；不把 sidecar 输出原样当事实 |
| `Codex subagent` | code / doc scan、lint、diff review、风险列举 | 不独立写回 authority |
| `GPT Pro` | GitHub 外部审计、PR / commit reviewer | 不直接改 repo |
| `Claude Code / VSCode` | IA / UX 评论、局部文案、contract 校对 | 默认 read-only |
| `OpenClaw / Hermes` | research、反驳审读、长上下文归纳 | 默认 read-only |
| `user` | 选择任务、审批范围、处理合并 | 保留最终 gate |

## D. 并行模式

| 模式 | 说明 | 适用边界 |
|---|---|---|
| 串行模式 | 一个主 agent 执行 | 小范围文档或验证任务 |
| 单主多审模式 | 一个 authority writer，多个 sidecar review / audit / research lane | 默认推荐模式；review lane 不计入 product lane |
| 多分支并行模式 | 多个 `task/*` 分支并行 | Active product lane max=3；same file group writer max=1 |
| 审计模式 | 所有工具只读 GitHub commit / PR / run | 输出审计意见，不写回 repo |

## E. 文件写入规则

- `docs/current.md`、`docs/task-index.md`、`docs/decision-log.md` 只能由当前 authority writer 更新。
- `docs/specs/*` 可由当前主写入窗口合并 sidecar 建议。
- Sidecar 输出若要落地，优先进入 `docs/research/`，再由主写入窗口择要合并。
- 不创建顶层 `candidates/`、`dispatches/`、`audits/`。
- 不写 API / worker / frontend runtime，除非任务明确授权。

## F. 派单模板

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

## G. Stop-the-line

- 多个 agent 同时改 `docs/current.md`、`docs/task-index.md` 或 `docs/decision-log.md`。
- Sidecar 直接改 authority 文件。
- PR / branch 与 `main` 漂移且未 rebase。
- 任务范围外写产品代码或 runtime。
- 外部研究被直接写成主线事实。
- 出现凭据、token、raw response 泄露。

## H. GitHub 外部审计

- 高风险或 material task 必须提供 PR diff / workflow run / local validation 摘要。
- `GPT Pro` 外审只输出审计意见或下一轮任务输入；不直接改 repo。
- 小 docs-only 任务可由 user 选择轻量审计，但不得绕过 authority writer。
