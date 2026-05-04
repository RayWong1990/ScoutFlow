# Current
## 当前状态
- Phase / Step：`1A` / `Wave 2 closed; Phase 2A migration prep gated`
- 主任务：无 active product task；T-P1A-020（PR #43+#49）与 T-P1A-026（PR #51）均已 merged，并由 T-P1A-027 ledger-closed
- 工作模式：Active product lane max=`3`，Authority writer max=`1`；Active count=`0/3`，Review count=`0`
- 当前结论：Wave 2 product lanes（018/019/020）全部 merged；研究 lanes（021/022/023/024/025）已 frozen 进 Done；DB vNext 进展为 research(#42) → spec design(#50) → SRD-v3 candidate amendment(#51) 三阶段（user-authorized progression），均为 candidate / 不是 promoted authority；`PRD-v2-2026-05-04.md` / `SRD-v2-2026-05-04.md` 仍为 base authority；`audio_transcript` runtime 仍 blocked；`migrations/**` 仍 FORBIDDEN
## 当前允许
- 下一步：T-P1A-028（S1）SRD-v3 candidate audit-fix（trigger + composite FK + PlatformResult CHECK + cross-capture identity + reachability vocab）— S0 与 S1 文件域零交集，可真并行
- T-P1A-028 之后：可考虑 Phase 2A migration dry-run plan dispatch（仍非 migration 实施）
- Wave 3 候选 lane（如 BBDown bounded live probe T-P1A-021A、Explore frontend skeleton、ASR eval-only gate）均为 propose-only；任何启动均需新 dispatch + user 显式授权 + decision-log 单独 entry
## 当前禁止
- `services/api/migrations/**` FORBIDDEN — S0 + S1 通过前不得动；schema 变更需另立 dispatch + user 显式授权 + 单独 PR + 外审
- `audio_transcript` runtime blocked
- BBDown live / yt-dlp / ffmpeg / ASR / browser automation blocked
- `subprocess.run` 不得在 orchestrator 出现（19 tripwire test 已就位）
- 不创建或修改 `workers/`、`apps/`、`packages/`；`services/**` 仅任务明确授权时可动
- 不触碰 `data/`、`referencerepo/`、凭据、raw cookie/token、raw stdout/stderr
- 不把 research note、draft spec、chat summary 写成 final authority；不启动 Phase 2-4 runtime
- `PlatformResult` enum / `WorkerReceipt` schema / Trust Trace DTO 未经新 dispatch + 外审不得改动
## 下一步
- 等 S1（T-P1A-028）merge；S1 完成 SRD-v3 candidate audit-fix
- S0 merge 后第三个从 main 读取状态的新执行窗口才可启动（避免 stale current.md 误导）
- S0 + S1 全 merge 后，user 显式 gate 下一阶段（Phase 2A migration dry-run plan / Wave 3 候选）
