# Current
## 当前状态
- Phase / Step：`1A` / `docs baseline + dispatch template cleanup complete`
- 主任务：无 active product task；`T-P1A-015=done`，`T-P1A-016=done`
- 工作模式：Active product lane max=`3`，Authority writer max=`1`；Active count=`0/3`，Review count=`0`
- 当前结论：`PRD-v2-2026-05-04.md` 与 `SRD-v2-2026-05-04.md` 已生成并归档 v1/amendment chain；`docs/dispatch-template.md` 与 `dispatch-authoring-guide` 已建立；未改 runtime、schema、receipt schema、PlatformResult enum、Trust Trace DTO；`audio_transcript` runtime 仍 blocked。
## 当前允许
- 当前无 active product task；下一步需要 user 显式授权新 lane。
- 后续新 amendment 以 `docs/PRD-v2-2026-05-04.md` / `docs/SRD-v2-2026-05-04.md` 为起点。
- 新 dispatch 从 `T-P1A-017+` 起应引用 `docs/dispatch-template.md`。
- 新 lane 必须先写 `docs/task-index.md`，并明确 owner、scope、allowed paths、validation。
## 当前禁止
- 不创建或修改 `workers/`、`apps/`、`packages/`；`services/**` 仅任务明确授权时可动。
- 不触碰 `data/`、`referencerepo/`、凭据、raw cookie/token。
- 不运行 BBDown / yt-dlp / ffmpeg / ASR / browser automation，不启用 `audio_transcript` runtime。
- 不把 research note、draft spec、chat summary 写成 final authority；不启动 Phase 2-4 runtime。
## 下一步
- 等 user 授权新的 product lane 或 audit lane。
