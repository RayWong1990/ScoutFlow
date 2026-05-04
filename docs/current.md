# Current
## 当前状态
- Phase / Step：`1A` / `Wave 2 closed; S0/S1 audit-fix merged; Phase 2A migration dry-run gated`
- 主任务：无 active product task；T-P1A-027（PR #52）与 T-P1A-028（PR #53）已 merged 并记录
- 工作模式：Active product lane max=`3`，Authority writer max=`1`；Active count=`0/3`，Review count=`0`
- 当前结论：Wave 2 product lanes（018/019/020）全部 merged；研究 lanes（021/022/023/024/025）已 frozen 进 Done；DB vNext remains candidate-only；not SRD-v3 promoted authority；not migration approval；not runtime approval；`PRD-v2-2026-05-04.md` / `SRD-v2-2026-05-04.md` 仍为 base authority；`audio_transcript` runtime 仍 blocked；`migrations/**` 仍 FORBIDDEN
## 当前允许
- 下一步可考虑 Phase 2A migration dry-run plan dispatch（仍非 migration 实施）；必须由 user 显式授权
- SRD-v3 promote 仍需单独 promotion gate；当前 SRD-v3 candidate 只是 candidate contract
- Wave 3 候选 lane（如 BBDown bounded live probe T-P1A-021A、Explore frontend skeleton、ASR eval-only gate）均为 propose-only；任何启动均需新 dispatch + user 显式授权 + decision-log 单独 entry
## 当前禁止
- `services/api/migrations/**` FORBIDDEN — migration dry-run plan / schema 变更 / migration 实施均需另立 dispatch + user 显式授权 + 单独 PR + 外审
- `audio_transcript` runtime blocked
- BBDown live / yt-dlp / ffmpeg / ASR / browser automation blocked
- `subprocess.run` 不得在 orchestrator 出现（19 tripwire test 已就位）
- 不创建或修改 `workers/`、`apps/`、`packages/`；`services/**` 仅任务明确授权时可动
- 不触碰 `data/`、`referencerepo/`、凭据、raw cookie/token、raw stdout/stderr
- 不把 research note、draft spec、chat summary 写成 final authority；不启动 Phase 2-4 runtime
- `PlatformResult` enum / `WorkerReceipt` schema / Trust Trace DTO 未经新 dispatch + 外审不得改动
## 下一步
- User 显式 gate 下一阶段：Phase 2A migration dry-run plan 或 Wave 3 候选
- 若进入 Phase 2A migration dry-run plan，只能先产出 plan / risk / validation packet；仍不得写 `services/api/migrations/**`
- 任何 code-bearing migration / runtime / worker / frontend 启动都必须新 dispatch + 外审
