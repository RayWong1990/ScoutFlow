# Current

## 当前状态

- Phase：`0`
- Step：`Step0`
- 主任务：`T-P0-001`
- 工作模式：GitHub bootstrap + 根轻配置 + 入口文档
- 当前任务状态：`in_progress`
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

- `T-P0-001`：Git 初始化、GitHub 私有仓库、根轻配置、入口文档补齐

## 下一步候选

- `T-P0-002`：`backlog`，待补齐 DoR 并经 user 批准
- `T-P0-003`：`backlog`，待补齐 DoR 并经 user 批准

## 阻塞

- 若 `gh auth status` 显示未登录，需 user 本人完成 `gh auth login`
