# ScoutFlow

ScoutFlow 是一个面向个人研究工作流的 authority-first 内容采集、转写、规整与证据账本工作台。

## 当前阶段

- 当前阶段：`Phase 0 / Step0`
- 当前任务与状态：以 `docs/current.md` 为准
- 当前焦点：文档、contract、红线 lint stub
- 当前不做：API / worker / Console 产品代码

## 当前基调

- `authority-first`：SQLite、FS layout、state words 是后续实现的约束中心
- `/captures/discover` 是 `capture 创建入口（capture creation entrypoint）`
- `recommendation / keyword / RAW gap` 当前不得直接创建 capture
- Phase 2-4 当前只作参考 outline

## 阅读顺序

1. `AGENTS.md`
2. `docs/current.md`
3. `docs/task-index.md`
4. `docs/specs/contracts-index.md`
5. `docs/SRD-v1.1-amendment-2026-05-03.md`

## 仓库边界

- `data/` 不进 git
- `referencerepo/` 不进 git
- 不建立 `candidates/`、`dispatches/`、`audits/` 顶层目录

## GitHub 外部审计工作流

ScoutFlow 当前把 GitHub 记录作为跨工具审计真源：

1. `Codex Desktop` / `Claude Code` / `Hermes Agent` / `OpenClaw` 等工具按任务边界交付变更。
2. 执行工具 push 到 GitHub，保留 commit / PR / workflow run。
3. user 贴 `commit hash + run id + 回写摘要`；无 CI run 时写 `run id: none`。
4. 网页版 `GPT Pro` 直接从 GitHub 的 commit / PR diff / workflow run 审计。
5. 审计意见回到任务账本和当前状态文档，不以聊天摘要替代仓库事实。

任务状态以 `docs/current.md` 与 `docs/task-index.md` 为准；并行执行协议见 `docs/specs/parallel-execution-protocol.md`。

## 当前范围

- Step0 文档与 contract 已形成候选实现基准
- 当前 Git bootstrap 不等于批准开始产品代码
