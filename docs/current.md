# Current
## 当前状态
- Phase / Step：`1A` / `T-P1A-015 PRD/SRD promote to v2`
- 主任务：`T-P1A-015`；当前任务状态：`done`（local complete；GPT Pro external audit + PR merge pending）
- 工作模式：Active product lane max=`3`，Authority writer max=`1`；Active count=`0/3`，Review count=`0`
- 当前结论：`PRD-v2-2026-05-04.md` 与 `SRD-v2-2026-05-04.md` 已生成；旧 PRD/SRD/amendment 已归档到 `docs/archive/`；forward authority 引用已切 v2；未改 runtime、schema、receipt schema、PlatformResult enum、Trust Trace DTO；`audio_transcript` runtime 仍 blocked。
## 当前允许
- 当前无 active product task；如需继续，只允许 `T-P1A-015` close sync 或 user 显式授权的新 lane。
- `T-P1A-016` 仍需 user gate。
- 后续新 amendment 以 v2 base 为起点，不再叠在 v1 上。
- 新 lane 必须先写 `docs/task-index.md`，并明确 owner、scope、allowed paths、validation。
## 当前禁止
- 不创建或修改 `workers/`、`apps/`、`packages/`；`services/**` 仅任务明确授权时可动。
- 不触碰 `data/`、`referencerepo/`、凭据、raw cookie/token。
- 不运行 BBDown / yt-dlp / ffmpeg / ASR / browser automation，不启用 `audio_transcript` runtime。
- 不把 research note、draft spec、chat summary 写成 final authority；不启动 Phase 2-4 runtime。
## 下一步
- 先做 `T-P1A-015` 的 GPT Pro 外审与 PR merge。
- `T-P1A-016` 仍待单独授权；其他 runtime lane 也仍需新 gate。
