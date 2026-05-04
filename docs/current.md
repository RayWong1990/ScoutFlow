# Current
## 当前状态
- Phase / Step：`1A` / `Wave 2 ledger open — T-P1A-017 PR pending merge`
- 主任务：Wave 2 product lanes registered — T-P1A-018/019/020 open；T-P1A-017 ledger-open PR open for user review
- 工作模式：Active product lane max=`3`，Authority writer max=`1`；Active count=`3/3`，Review count=`0`
- 当前结论：Wave 2 product lanes 018/019/020 registered；research backlog 021/022/023/024/025 in backlog；conflict domain table locked in task-index；`PRD-v2-2026-05-04.md` / `SRD-v2-2026-05-04.md` remain base authority；`audio_transcript` runtime still blocked。
## 当前允许
- T-P1A-018 可在 T-P1A-017 PR merge 后启动（sequencing: 018 → 019 → 020）。
- T-P1A-019 等 T-P1A-018 完成 storage/job 层后启动。
- T-P1A-020 等 T-P1A-019 完成 orchestration 层后启动。
- 研究 lane 021/022/023/024/025 可在 T-P1A-017 PR merge 后写 `docs/research/` 研究笔记；非 authority，非 runtime approval。
## 当前禁止
- T-P1A-019/020 不得写 `storage.py`/`captures.py`/`jobs.py`/`main.py`（owned by T-P1A-018）。
- T-P1A-018/020 不得写 `external_tools/**`/`orchestration/**`/`metadata_probe_receipt_bridge.py`（owned by T-P1A-019）。
- T-P1A-018/019 不得写 `test_capture_trust_trace.py`（owned by T-P1A-020）。
- 任何 lane 不得动 `migrations/**` — FORBIDDEN。
- 不创建或修改 `workers/`、`apps/`、`packages/`；`services/**` 仅任务明确授权时可动。
- 不触碰 `data/`、`referencerepo/`、凭据、raw cookie/token。
- 不运行 BBDown / yt-dlp / ffmpeg / ASR / browser automation，不启用 `audio_transcript` runtime。
- 不把 research note、draft spec、chat summary 写成 final authority；不启动 Phase 2-4 runtime。
## 下一步
- T-P1A-017 PR merge（需要 user Wave 2 lane plan 签字 + conflict domain 浏览授权，见 §4 步骤 10）。
- 签字后 T-P1A-018 可启动。
