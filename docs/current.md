# Current

## 当前状态

- Phase：`0`
- Step：`Step0`
- 主任务：`T-P0-003`
- 工作模式：目录骨架 + 文档 lint stub + 入口文档同步
- 当前任务状态：`done`
- 当前结论：`不进入产品代码`

## 当前允许

- `.gitignore`
- `.env.example`
- `.vscode/`
- `.github/`
- `tools/`
- `README.md`
- `docs/`
- `AGENTS.md`
- `CLAUDE.md`

## 当前禁止

- `apps/`
- `services/`
- `workers/`
- `packages/`
- `data/`
- `referencerepo/`
- `candidates/`
- `dispatches/`
- `audits/`
- 真实采集实现
- 浏览器自动化
- Phase 2-4 真实逻辑

## 当前候选基准

- `POST /captures/discover` = `capture 创建入口（capture creation entrypoint）`
- `recommendation / keyword / RAW gap` 不直接创建 capture
- 活动任务上限 `3`
- 项目根不建立重治理目录

> 上述候选基准已获 user 批准，可作为 `Phase 0 / Phase 1A` 的候选实现基线；这不等于批准开始产品代码实现。

## 当前任务

- `T-P0-003`：目录骨架 + 文档 lint stub + 入口文档同步，当前已闭合为 `done`
- 本任务已创建最小文档红线 lint stub、接入 GitHub Actions docs-check，并同步 `README.md` / `AGENTS.md` / `CLAUDE.md` 入口口径

## 下一步候选

- `T-P0-002`：`backlog`，`decision-log / locked-principles / project-context` 深化
- 不自动进入 `Phase 1A` 产品代码

## 阻塞

- 不自动进入 `T-P0-002` 或 `Phase 1A`，等待 user 后续选择
