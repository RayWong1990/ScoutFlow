# ScoutFlow AGENTS

> 适用范围：ScoutFlow 项目根目录下的所有 agent 会话。当前阶段已合并 `T-P1A-001` 的 API-side metadata-only baseline、`T-P1A-002` 的 receipt/ledger baseline、`T-P1A-004` 的安全基线，以及 PR `#10` 的 `T-P1A-003` BBDown research note、PR `#14` 的 `T-P1A-006` BBDown adapter draft spec、PR `#15` 的 `T-P1A-007` Explore URL UX research note、PR `#17` 的 `T-P1A-008` BBDown sanitized fixture parser、PR `#19` 的 `T-P1A-009` BBDown local runtime spike report、PR `#20` 的 `T-P1A-009` close hardening、PR `#23` 的 `T-P1A-010A` BBDown tool preflight package、PR `#22` 的 `T-P1A-010B` injected-runner info adapter shell、PR `#24` 的 `T-P1A-010C` PRD/SRD amendment repair pack。Wave 1 当前为 `closed`，Active count=`0/3`，Review count=`0`。`T-P1A-011` 的 `BBDown` tool preflight compatibility repair 已完成；`T-P1A-011B` manual-auth QR local-only gate 已完成；`T-P1A-011C` auth-present metadata probe 已完成；`T-P1A-011D` second retro triage、`T-P1A-011E` minimal retro skeleton、`T-P1A-011F` patched Dispatch `08/09` prompt report、`T-P1A-011G` sidecar review 已完成；`T-P1A-012` metadata receipt wiring、`T-P1A-012R` receipt-wiring retro、`T-P1A-013` Trust Trace API surface、`T-P1A-013A` receipt/trust-trace audit hardening 也已完成。当前结论是：`011C` 的 auth-present metadata evidence 已可安全桥接进既有 `/jobs/{job_id}/complete` / `artifact_assets` baseline，并且 generic receipt API 现在只接受当前 phase 明确允许的 success evidence；`GET /captures/{capture_id}/trust-trace` 继续保持分层 safe trace；repo 内 `BBDown.data` / `qrcode.png` 仍禁止。PR `#22` 的 no-auth `-info` adapter shell 不是 live runtime proof；PRD/SRD v1.2 amendment 仍是 `candidate / draft / not final authority / not runtime approval`。不允许自动执行新的 `BBDown -info`、media download、ffmpeg、ASR、workers、frontend、浏览器自动化、`audio_transcript` 或 Phase 2-4 runtime。

## 1. 进入项目先读

1. `docs/current.md`
2. `docs/task-index.md`
3. `docs/specs/contracts-index.md`
4. `docs/plans/step0-execution-plan.md`
5. 与当前任务直接相关的 PRD / SRD / amendment

## 2. 当前阶段

- 当前 Phase：`Phase 1A`
- 当前 Step：`T-P1A-013A receipt / trust trace audit hardening done`
- 当前活动任务：`T-P1A-013A`（done；当前无 active product task）；Active count=`0/3`，Review count=`0`
- 当前候选基准：`docs/PRD-v1-2026-05-02.md`、`docs/PRD-v1.1-amendment-2026-05-02.md`、`docs/SRD-v1-2026-05-02.md`、`docs/SRD-v1.1-amendment-2026-05-03.md`、`docs/current.md`、`docs/task-index.md`、`docs/specs/*.md`
- 当前只做：等待 user 是否授权新的 lane；`T-P1A-011H` candidate-only legal/vendor notes 与任何 frontend mode 仍需显式授权；不从聊天摘要自动启动新任务
- 当前不做：workers、frontend、真实下载、真实 BBDown 执行、真实 `BBDown -info`、QR/manual auth、yt-dlp / ffmpeg runtime、ASR、浏览器自动化、`audio_transcript`、Phase 2-4 runtime
- 当前状态：`T-P1A-013A=done`; `T-P1A-013=done`; `T-P1A-012R=done`; `T-P1A-012=done`; `T-P1A-011G=done`; `T-P1A-011F=done`; `T-P1A-011E=done`; `T-P1A-011D=done`; `T-P1A-011C=done`; `T-P1A-011B=done`; `T-P1A-011=done`；历史：`T-P1A-001` 已通过 PR `#7` 合并入 `main`，含义仅为 `metadata_only API-side capture creation baseline merged`；`T-P1A-002` 已通过 PR `#9` 合并入 `main`；`T-P1A-004` 已通过 PR `#8` 合并入 `main`；`T-P1A-003` 已通过 PR `#10` 合并入 `main`，含义仅为 `docs/research/** research note merged`；`T-P1A-006` 已通过 PR `#14` 合并入 `main`，含义仅为 `docs/specs/bbdown-adapter-contract-draft.md` draft spec merged；`T-P1A-007` 已通过 PR `#15` 合并入 `main`，含义仅为 `docs/research/**` Explore UX decision pack merged；`T-P1A-008` 已通过 PR `#17` 合并入 `main`，含义仅为 `fixture-only parser / classifier baseline merged`；`T-P1A-009` 已通过 PR `#19` 合并入 `main`，含义仅为 `report-only runtime spike merged`；`T-P1A-010A` / `T-P1A-010B` / `T-P1A-010C` 已通过 PR `#23` / `#22` / `#24` 合并入 `main`，含义仅为 Wave 1 package merged。

## 3. 当前红线

- 不修改 `data/`
- 不修改 `referencerepo/`
- 不在项目根建立重治理目录
- `recommendation / keyword / RAW gap` 不直接创建 capture
- `POST /captures/discover` 当前语义是 `capture 创建入口（capture creation entrypoint）`，不是 source discovery
- `audio_transcript` runtime 仍 blocked，不进入当前 active tasks
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
- `docs/retro/**`
- `AGENTS.md`
- `README.md`
- 已合入主线的 `docs/specs/bbdown-adapter-contract-draft.md`、`docs/research/**`、`docs/PRD-v1.2-amendment-2026-05-03.md`、`docs/SRD-v1.2-amendment-2026-05-03.md` 当前只作 reference / candidate；如需继续修改，必须等待新任务显式授权

## 5. 当前禁止路径

- `apps/`
- `workers/`
- `packages/`
- `data/`
- `referencerepo/`
- `candidates/`
- `dispatches/`
- `audits/`
- `services/**`（除后续 `docs/task-index.md` Active 表再次明确授权外）
- `tests/**`（除后续 `docs/task-index.md` Active 表再次明确授权外）

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
