# ScoutFlow AGENTS

> 适用范围：ScoutFlow 项目根目录下的所有 agent 会话。当前阶段只允许 Step0 文档与 contract 工作，不允许开始产品实现。

## 1. 进入项目先读

1. `docs/current.md`
2. `docs/task-index.md`
3. `docs/specs/contracts-index.md`
4. `docs/plans/step0-execution-plan.md`
5. 与当前任务直接相关的 PRD / SRD / amendment

## 2. 当前阶段

- 当前 Phase：`Phase 0`
- 当前 Step：`Step0`
- 当前活动任务：`T-P0-002`（close done；等待 user 选择是否进入 Phase 1A 准备任务）
- 当前候选基准：`docs/PRD-v1-2026-05-02.md`、`docs/PRD-v1.1-amendment-2026-05-02.md`、`docs/SRD-v1-2026-05-02.md`、`docs/SRD-v1.1-amendment-2026-05-03.md`、`docs/current.md`、`docs/task-index.md`、`docs/specs/*.md`
- 当前只做：Step0 文档、contract、协作协议收口；等待下一任务
- 当前不做：API、worker、Console、真实采集、浏览器自动化
- 当前状态：`T-P0-002 done`；`T-P0-003 done`；不自动进入 Phase 1A 产品代码

## 3. 当前红线

- 不修改 `data/`
- 不修改 `referencerepo/`
- 不在项目根建立重治理目录
- `recommendation / keyword / RAW gap` 不直接创建 capture
- `POST /captures/discover` 当前语义是 `capture 创建入口（capture creation entrypoint）`，不是 source discovery
- Phase 2-4 只作参考 outline，不进入当前实现任务

## 4. 当前允许路径

- `.github/workflows/docs-check.yml`
- `.github/pull_request_template.md`
- `tools/check-docs-redlines.py`
- `docs/`
- `AGENTS.md`
- `CLAUDE.md`
- `README.md`

## 5. 当前禁止路径

- `apps/`
- `services/`
- `workers/`
- `packages/`
- `data/`
- `referencerepo/`
- `candidates/`
- `dispatches/`
- `audits/`

## 6. 写回纪律

- 任务状态变化先写 `docs/task-index.md`
- 当前焦点变化再写 `docs/current.md`
- contract 变更同步 `docs/specs/contracts-index.md`
- 发现 schema / state words / FS layout / LP 冲突时先停线，再升级任务

## 7. 停线条件

- 任一改动触碰 schema / state words / FS layout / LP 且当前任务未授权
- 提议把 Phase 2-4 的真实逻辑塞进当前任务
- 提议让 `recommendation / keyword / RAW gap` 直接创建 capture
- raw response、日志或报账结构里出现凭据
- 任何实现试图把 worker 旁路写入 authority

## 8. 当前工具分工

| 工具 | 当前职责 | 当前不应做 |
|---|---|---|
| `Codex Desktop` | Step0 文档、contract、任务账本、主写入、commit owner | 当前任务中不写产品代码；不让 subagent 独立写 authority |
| `Codex subagent` | code/doc scan、lint、diff review、风险列举 | 不独立写回 `docs/current.md` / `docs/task-index.md` |
| `Claude Code / VSCode` | 文档审读、IA/UX 评论、局部文案修订、contract 校对 | 不主导当前代码主线；默认 sidecar read-only |
| `ChatGPT Pro` | GitHub 外部审计、prompt 派单、PR/commit review | 不直接改 repo；不绕过任务账本 |
| `OpenClaw / GLM` | 次级 research / scout note、反驳审读 | 默认 read-only；不直写 authority |
| `Hermes Agent / Kimi` | 未来调度与信号源设计参考、长上下文归纳 | 默认 read-only；Phase 1A 不抢跑推荐采集 |

## 9. 并行执行协议

当前多工具协作遵守 `docs/specs/parallel-execution-protocol.md`：

- `Single Writer`：同一任务只能有一个主写入窗口。
- `Multi Reviewer`：其他窗口只做 read-only review / research / patch suggestion。
- `GitHub external audit source`：跨工具审计以 commit / PR diff / workflow run 为事实源，不以聊天摘要替代仓库事实。
- `Branch / PR preferred`：并行任务优先使用 `task/*` branch 或 PR，不直接 push `main`。
- `docs/current.md` 与 `docs/task-index.md` 只能由主写入 agent 修改。
- 网页版 `GPT Pro` 不直接改 repo，只审计 commit / PR / workflow run。
- `OpenClaw` / `Hermes` / `Claude` 默认不直写 authority，除非任务明确授权且遵守 `Single Writer`。

## 10. GitHub 外部审计工作流

当前多工具协作默认采用 GitHub 作为审计真源：

1. `Codex Desktop` / `Claude Code` / `Hermes Agent` / `OpenClaw` 等工具在授权范围内交付任务变更。
2. 执行工具将变更 push 到 GitHub，保留可审计的 commit / branch / PR / run 记录。
3. user 在后续会话贴出 `commit hash + run id + 回写摘要`；若没有 CI run，明确写 `run id: none`。
4. 网页版 `GPT Pro` 直接从 GitHub 的 commit / PR diff / workflow run 审计，不以聊天转述作为事实源。
5. `GPT Pro` 输出只作为审计意见或下一轮任务输入；不直接改主线文件，不绕过 `docs/task-index.md` 与 `docs/current.md`。

## 11. 当前输出要求

- 中文
- 引用具体文件
- 明确哪些是待拍板 contract，哪些只是 Phase 2+ outline
- 不把聊天内容当事实
