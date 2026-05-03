# ScoutFlow AGENTS

> 适用范围：ScoutFlow 项目根目录下的所有 agent 会话。当前阶段已合并 `T-P1A-001` 的 API-side metadata-only baseline、`T-P1A-002` 的 receipt/ledger baseline、`T-P1A-004` 的安全基线，以及 PR `#10` 的 `T-P1A-003` BBDown research note、PR `#14` 的 `T-P1A-006` BBDown adapter draft spec、PR `#15` 的 `T-P1A-007` Explore URL UX research note。当前 `T-P1A-008` 已由 Dispatch 3 显式打开为 `active`，仅允许 sanitized fixture parser；`T-P1A-009` 仍为 `backlog/gated`。仍不允许 workers、frontend、浏览器自动化或 Phase 2-4 runtime。

## 1. 进入项目先读

1. `docs/current.md`
2. `docs/task-index.md`
3. `docs/specs/contracts-index.md`
4. `docs/plans/step0-execution-plan.md`
5. 与当前任务直接相关的 PRD / SRD / amendment

## 2. 当前阶段

- 当前 Phase：`Phase 1A`
- 当前 Step：`T-P1A-008 active / T-P1A-009 gated`
- 当前活动任务：`T-P1A-008` BBDown sanitized fixture parser；fixture-only，不运行 BBDown，不访问真实 Bilibili URL；`T-P1A-009` local runtime spike 仍为 gated backlog
- 当前候选基准：`docs/PRD-v1-2026-05-02.md`、`docs/PRD-v1.1-amendment-2026-05-02.md`、`docs/SRD-v1-2026-05-02.md`、`docs/SRD-v1.1-amendment-2026-05-03.md`、`docs/current.md`、`docs/task-index.md`、`docs/specs/*.md`
- 当前只做：`T-P1A-008` allowed paths 内的脱敏 fixture parser / classifier 与任务账本同步；不自动批准新 runtime
- 当前不做：workers、frontend、真实下载、ASR、BBDown / yt-dlp / ffmpeg runtime、浏览器自动化、Phase 2-4 runtime
- 当前状态：`active`；历史：`T-P1A-001` 已通过 PR `#7` 合并入 `main`，含义仅为 `metadata_only API-side capture creation baseline merged`；`T-P1A-002` 已通过 PR `#9` 合并入 `main`；`T-P1A-004` 已通过 PR `#8` 合并入 `main`；`T-P1A-003` 已通过 PR `#10` 合并入 `main`，含义仅为 `docs/research/** research note merged`；`T-P1A-006` 已通过 PR `#14` 合并入 `main`，含义仅为 `docs/specs/bbdown-adapter-contract-draft.md` draft spec merged；`T-P1A-007` 已通过 PR `#15` 合并入 `main`，含义仅为 `docs/research/**` Explore URL UX decision pack merged；当前只允许 `T-P1A-008` 受控 fixture-only 产品代码

## 3. 当前红线

- 不修改 `data/`
- 不修改 `referencerepo/`
- 不在项目根建立重治理目录
- `recommendation / keyword / RAW gap` 不直接创建 capture
- `POST /captures/discover` 当前语义是 `capture 创建入口（capture creation entrypoint）`，不是 source discovery
- `audio_transcript` runtime 不进入当前 active tasks
- 不创建或修改 `workers/`
- 不创建或修改 `apps/`
- Phase 2-4 只作参考 outline，不进入当前实现任务
- BBDown research note / draft spec 不得被当作 runtime approval
- cookie / token / secret 不得进入 Git、PR、CI、logs 或 tracked artifacts

## 4. 当前允许路径

- `docs/current.md`
- `docs/task-index.md`
- `docs/decision-log.md`
- `docs/specs/contracts-index.md`
- `AGENTS.md`
- `README.md`
- `services/api/scoutflow_api/external_tools/**`
- `tests/contracts/**`
- `tests/fixtures/bbdown/**`
- 已合入主线的 `docs/specs/bbdown-adapter-contract-draft.md` 与 `docs/research/**` 当前只作 reference；如需继续修改，必须等待新任务显式授权

## 5. 当前禁止路径

- `apps/`
- `workers/`
- `packages/`
- `data/`
- `referencerepo/`
- `candidates/`
- `dispatches/`
- `audits/`
- `services/**` 中除 `services/api/scoutflow_api/external_tools/**` 外的路径
- `tests/**` 中除 `tests/contracts/**` 与 `tests/fixtures/bbdown/**` 外的路径

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
| `Codex Desktop` | 任务账本、主写入、commit owner；未来新任务仍需显式授权 | 不写 workers / frontend；不让 subagent 独立写 authority |
| `Codex subagent` | code/doc scan、lint、diff review、风险列举 | 不独立写回 `docs/current.md` / `docs/task-index.md` |
| `Claude Code / VSCode` | 文档审读、IA/UX 评论、局部文案修订、contract 校对 | 不主导当前代码主线；默认 sidecar read-only |
| `ChatGPT Pro` | GitHub 外部审计、prompt 派单、PR/commit review | 不直接改 repo；不绕过任务账本 |
| `OpenClaw / GLM` | 次级 research / scout note、反驳审读 | 默认 read-only；不直写 authority |
| `Hermes Agent / Kimi` | 未来调度与信号源设计参考、长上下文归纳 | 默认 read-only；当前不抢跑推荐采集 |

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
