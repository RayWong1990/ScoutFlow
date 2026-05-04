# Current
## 当前状态
- Phase / Step：`1A` / `T-P1A-014 lean constraints cleanup v2`
- 主任务：`T-P1A-014`；当前任务状态：`done`（local complete；仍需 GPT Pro 外审与 PR merge 才能进入 main）
- 工作模式：Active product lane max=`3`，Authority writer max=`1`；Active count=`0/3`，Review count=`0`
- 当前结论：入口文档已减重，contracts-index=8 group，locked principles=4 hard LP；未改 runtime、schema、receipt schema、PlatformResult enum、Trust Trace DTO；`audio_transcript` runtime 仍 blocked。
## 当前允许
- 当前只允许 `T-P1A-014` 的 GitHub 外审、PR 修订与 merge 决策。
- `T-P1A-015` / `T-P1A-016` 在 `T-P1A-014` merged 到 `main` 前不得启动。
- 新 lane 必须先写 `docs/task-index.md`，并明确 owner、scope、allowed paths、validation。
## 当前禁止
- 不创建或修改 `workers/`、`apps/`、`packages/`；`services/**` 仅任务明确授权时可动。
- 不触碰 `data/`、`referencerepo/`、凭据、raw cookie/token。
- 不运行 BBDown / yt-dlp / ffmpeg / ASR / browser automation，不启用 `audio_transcript` runtime。
- 不把 research note、draft spec、chat summary 写成 final authority；不启动 Phase 2-4 runtime。
## 下一步
- GPT Pro 外审输入：PR diff、retro drop list、boundary grep 输出、onboarding readiness 表。
- 外审通过并 merge 后，user 再决定是否授权 `T-P1A-015` 或 `T-P1A-016`。
