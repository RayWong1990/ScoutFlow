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
- 当前活动任务：`T-P0-003`
- 当前候选基准：`docs/PRD-v1-2026-05-02.md`、`docs/PRD-v1.1-amendment-2026-05-02.md`、`docs/SRD-v1-2026-05-02.md`、`docs/SRD-v1.1-amendment-2026-05-03.md`、`docs/current.md`、`docs/task-index.md`、`docs/specs/*.md`
- 当前只做：目录骨架、文档 lint stub、入口文档同步
- 当前不做：API、worker、Console、真实采集、浏览器自动化
- 当前状态：`T-P0-001 已闭合；T-P0-003 已进入 review，等待外部审计`

## 3. 当前红线

- 不修改 `data/`
- 不修改 `referencerepo/`
- 不在项目根建立重治理目录
- `recommendation / keyword / RAW gap` 不直接创建 capture
- `POST /captures/discover` 当前语义是 `capture 创建入口（capture creation entrypoint）`，不是 source discovery
- Phase 2-4 只作参考 outline，不进入当前实现任务

## 4. 当前允许路径

- 项目根轻配置
- `.github/workflows/docs-check.yml`
- `tools/`
- `docs/`
- `AGENTS.md`
- `CLAUDE.md`

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
| `Codex Desktop` | Step0 文档、contract、任务账本、后续代码主执行 | 当前任务中不写产品代码 |
| `Claude Code / VSCode` | 文档审读、IA/UX 评论、局部文案修订 | 不主导当前代码主线 |
| `ChatGPT Pro` | 外部研究 note、参考资料整理 | 不直接改主线文件 |
| `OpenClaw` | 次级 research / scout note | 不直写 authority |
| `Hermes CLI` | 未来调度与信号源设计参考 | Phase 1A 不抢跑推荐采集 |

## 9. 当前输出要求

- 中文
- 引用具体文件
- 明确哪些是待拍板 contract，哪些只是 Phase 2+ outline
- 不把聊天内容当事实
