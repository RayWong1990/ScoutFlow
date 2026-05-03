# ScoutFlow CLAUDE

> 适用对象：Claude Code / VSCode 会话。当前阶段优先做中文文档审读、IA / UX 评论、局部文案修订和 contract 校对，不进入产品实现。
> 当前任务与状态以 `docs/current.md` / `docs/task-index.md` 为准，`CLAUDE.md` 不作为任务账本。

## 1. 阅读顺序

1. `docs/current.md`
2. `docs/task-index.md`
3. `docs/specs/contracts-index.md`
4. `docs/plans/step0-execution-plan.md`
5. 当前任务直接引用的 PRD / SRD / amendment

## 2. 当前职责

- 审读 PRD / SRD / amendment 的冲突项
- 只在任务明确时做文档审读、IA / UX 评论、局部文案修订、contract 校对
- 为 Codex 的后续实现提供清晰中文 contract
- 标出 Phase 2+ outline，不把它们推进当前 backlog
- 不主导代码主线
- Claude sidecar 输出默认 read-only，只作为审读意见或 patch 建议
- 若要改文件，必须在任务授权范围内，并遵守 `Single Writer`
- 当前状态仍以 `docs/current.md` / `docs/task-index.md` 为准

## 3. GitHub 外部审计工作流

当 `Claude Code / VSCode` 参与执行或审读 ScoutFlow 任务时，默认按以下链路交接：

1. 在当前允许路径内交付变更，不进入产品实现禁区。
2. 将变更 push 到 GitHub，保留 commit、分支 / PR 与 workflow run 记录。
3. user 后续贴 `commit hash + run id + 回写摘要`；若没有 CI run，标 `run id: none`。
4. 网页版 `GPT Pro` 直接读取 GitHub commit / PR diff / workflow run 做审计。
5. `GPT Pro` 审计意见不能直接改 authority；如需修订，回到 `docs/task-index.md` / `docs/current.md` 对应任务链路。

## 4. 并行执行边界

- `docs/current.md` 与 `docs/task-index.md` 只能由当前主写入窗口更新。
- Claude 可做 sidecar 审读、IA / UX 评论、局部文案建议和 contract 校对。
- Claude 输出默认不直接成为主线事实；被采纳后由主写入窗口写回。
- 需要写文件时，必须先确认任务授权、Allowed Paths、Forbidden Paths 和 branch / PR 规则。

## 5. 当前禁止

- 不写 API / worker / Console 产品代码
- 不修改或创建 `apps/`
- 不修改或创建 `services/`
- 不修改或创建 `workers/`
- 不修改或创建 `packages/`
- 不修改或创建 `data/`
- 不修改或创建 `referencerepo/`
- 不修改或创建 `candidates/`
- 不修改或创建 `dispatches/`
- 不修改或创建 `audits/`
- 不引入浏览器自动化
- 不把外部研究直接写成主线事实

## 6. 当前必须遵守

- 进入项目时必须先读 `docs/current.md` 与 `docs/task-index.md`
- 当前任务状态只以 `docs/current.md` / `docs/task-index.md` 为准
- `POST /captures/discover` 是 `capture 创建入口（capture creation entrypoint）`
- `recommendation / keyword / RAW gap` 不直接创建 capture
- 活动任务上限 `3`
- 根目录不建立重治理目录
- 发现 schema / state / FS / LP 冲突先停线

## 7. 输出要求

- 全中文
- 明确标注当前是待拍板基准，不伪装成已锁定 contract
- 引用具体文件路径
- 变更前后口径一致
- 若被授权为主写入窗口，按 `docs/task-index.md` → `docs/current.md` 顺序写回；否则只输出审读意见
