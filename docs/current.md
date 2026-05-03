# Current

## 当前状态

- Phase：`0`
- Step：`Step0`
- 主任务：`T-P0-001`
- 工作模式：GitHub bootstrap + 根轻配置 + 入口文档
- 当前任务状态：`review`
- 当前结论：`不进入产品代码`

## 当前允许

- `.gitignore`
- `.env.example`
- `.vscode/`
- `.github/`
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

> 上述候选基准已获 user 批准，可作为 `T-P0-001` 的仓库初始化基线；这不等于批准开始产品代码实现。

## 当前任务

- `T-P0-001`：Git 初始化、GitHub 私有仓库、根轻配置、入口文档补齐，当前已完成并进入 `review`

## 下一步候选

- `T-P0-002`：`backlog`，`decision-log / locked-principles / project-context` 深化
- `T-P0-003`：`backlog`，目录骨架 + 文档 lint stub

## 阻塞

- `T-P0-002` 与 `T-P0-003` 仍待 user 选择，不自动进入下一任务
