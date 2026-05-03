# ScoutFlow CLAUDE

> 适用对象：Claude Code / VSCode 会话。当前阶段优先做中文文档、SRD 修订、IA 审读和 contract 校对，不进入产品实现。

## 1. 阅读顺序

1. `docs/current.md`
2. `docs/task-index.md`
3. `docs/specs/contracts-index.md`
4. `docs/plans/step0-execution-plan.md`
5. 当前任务直接引用的 PRD / SRD / amendment

## 2. 当前职责

- 审读 PRD / SRD / amendment 的冲突项
- 只在任务明确时修改 `docs/`、`AGENTS.md`、`CLAUDE.md`
- 为 Codex 的后续实现提供清晰中文 contract
- 标出 Phase 2+ outline，不把它们推进当前 backlog

## 3. 当前禁止

- 不写 API / worker / Console 产品代码
- 不修改 `data/`
- 不修改 `referencerepo/`
- 不引入浏览器自动化
- 不把外部研究直接写成主线事实

## 4. 当前必须遵守

- `POST /captures/discover` 是 `capture 创建入口（capture creation entrypoint）`
- `recommendation / keyword / RAW gap` 不直接创建 capture
- 活动任务上限 `3`
- 根目录不建立重治理目录
- 发现 schema / state / FS / LP 冲突先停线

## 5. 输出要求

- 全中文
- 明确标注当前是待拍板基准，不伪装成已锁定 contract
- 引用具体文件路径
- 变更前后口径一致
- 写回 `docs/task-index.md` 与 `docs/current.md`
