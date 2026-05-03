# Current

## 当前状态

- Phase：`1A`
- Step：`T-P1A-006 / T-P1A-007 active`
- 主任务：`T-P1A-006`、`T-P1A-007`
- 工作模式：PR `#10` 已合并为 `docs/research/**` research note；`T-P1A-005` 人审同步处于 review branch 写回；后续 `T-P1A-006` / `T-P1A-007` 可并行，但仍遵守 `Single Writer / Multi Reviewer`
- 当前任务状态：`T-P1A-006=active`; `T-P1A-007=active`; `T-P1A-005=review`; `T-P1A-003=done`; `T-P1A-008=backlog/gated`; `T-P1A-009=backlog/gated`
- 当前结论：`main` 当前已合入 `T-P1A-001` metadata-only API-side baseline、`T-P1A-002` receipt / artifact ledger baseline、`T-P1A-004` text redaction / secret scan safety baseline，并已通过 PR `#10` 合入 `T-P1A-003` BBDown research note。`T-P1A-003` merge commit=`8328c567e26db118ad456b29f8616066174b3568`，head=`42baf4165d7bf9022a9e8742d989a7428ae3ee4b`，PR head GitHub run=`25278481839`，main merge GitHub run=`25280084928`，`docs-smoke=success` / `api-contract-tests=success`。`T-P1A-003` 仍只是 research note，不是 authority，不是 implementation approval。当前 Active count=`2/3`；当前不创建 workers，不调用 BBDown / yt-dlp / ffmpeg / ASR，不启用 `audio_transcript` runtime，不进入 Phase 2-4。

## 当前允许

- `T-P1A-006`：从 PR `#10` research note 提炼 `docs/specs/bbdown-adapter-contract-draft.md`；必须标记 `draft / not final authority / not runtime approval`
- `T-P1A-007`：与 user 做 Explore URL 粘贴 / 风险提示 / receipt 状态展示脑暴；只允许形成 discussion / research / draft notes，不写 frontend
- authority 同步文件：`docs/task-index.md`、`docs/current.md`、`docs/decision-log.md`、`docs/specs/contracts-index.md`
- 入口同步文件：`AGENTS.md`、`README.md`，仅在状态口径需要时修改

## 当前禁止

- `apps/`
- `workers/`
- `packages/`
- `data/`
- `referencerepo/`
- `candidates/`
- `dispatches/`
- `audits/`
- `audio_transcript` runtime
- 真下载 / ASR / BBDown / yt-dlp / ffmpeg runtime
- 浏览器自动化
- Phase 2-4 真实逻辑
- 把 BBDown research note 直接写成 final authority
- 把用户“隐私合规风险低”解释为可以提交 cookie / token / secret

## 当前候选基准

- `T-P1A-001` = `metadata_only API-side capture creation baseline merged`
- `T-P1A-002` = `API-side receipt ingestion and artifact ledger mapping merged baseline`
- `T-P1A-004` = `redaction / secret scan / CI hardening merged baseline`
- `T-P1A-003` = `BBDown public-source research note merged as reference only`
- `docs/specs/bbdown-adapter-contract-draft.md` = `T-P1A-006` 可提炼的 draft spec；未写入前不是 authority；写入后仍必须是 `draft / not final authority / not runtime approval`
- `POST /captures/discover` = `capture 创建入口（capture creation entrypoint）`
- `POST /jobs/{job_id}/complete` = `worker receipt API-side validation and ledger entrypoint`; 当前只接收已存在 job 的 receipt，不创建 worker queue runtime
- `recommendation / keyword / RAW gap` 不直接创建 capture
- 活动任务上限 `3`；当前 Active count=`2/3`
- 项目根不建立重治理目录

> `T-P1A-001` / `T-P1A-002` / `T-P1A-004` 的合并只表示对应 API-side 和安全基线进入 `main`；`T-P1A-003` 的合并只表示 research note 进入 `docs/research/**`。这些都不等于批准 broader Phase 1A runtime、workers、frontend、`audio_transcript` 或 Phase 2-4 产品代码。

## 当前任务

- `T-P1A-006`：BBDown adapter contract draft；状态 `active`；从 merged PR `#10` research note 提炼 draft spec，不实现或调用 runtime capture
- `T-P1A-007`：Explore URL UX / risk / receipt status brainstorm；状态 `active`；与 user 交互式脑暴，不写 frontend 代码
- `T-P1A-008`：BBDown sanitized fixture parser；状态 `backlog/gated`；前置为 `T-P1A-006` draft spec 合并；只用脱敏 fixture，不运行 BBDown
- `T-P1A-009`：BBDown local runtime spike；状态 `backlog/gated`；前置为 `T-P1A-006` + `T-P1A-008` + user 再次明确批准；不得下载媒体，不跑 ASR
- `T-P1A-003`：BBDown tool-surface research note；状态 `done`；已通过 PR `#10` 合并入 `main`，只作为 research note
- `T-P1A-002`：API jobs / receipt / artifact ledger foundation；状态 `done`；已通过 PR `#9` 合并入 `main`
- `T-P1A-004`：Redaction / secret scan / CI hardening；状态 `done`；已通过 PR `#8` 合并入 `main`
- `T-P1A-001`：Bilibili `manual_url` quick_capture metadata contract；状态 `done`；已通过 PR `#7` 合并入 `main`

## 下一步候选

- 并行执行 `T-P1A-006` 与 `T-P1A-007`
- `T-P1A-006` 只产 `bbdown-adapter-contract-draft.md`
- `T-P1A-007` 只产 Explore URL UX / risk / receipt 状态展示的脑暴记录或候选说明
- `T-P1A-008` 必须等 `T-P1A-006` draft spec 合并后再开
- `T-P1A-009` 必须等 `T-P1A-006` + `T-P1A-008` 完成后，并由 user 再次明确批准 runtime spike 后再开

## 阻塞

- 不允许让 `recommendation / keyword / RAW gap` 直接创建 capture
- 不允许把 `/captures/discover` 语义写成 source discovery / search / recommendation discovery
- 不允许把 BBDown research note、draft spec、或“后续希望复用 BBDown”解释为 runtime approval
