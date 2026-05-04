# Current
## 当前状态
- Phase / Step：`1A` / `Wave 2 — T-P1A-018 done; T-P1A-019 next executable`
- 主任务：T-P1A-019 metadata probe dry-run orchestrator（next executable lane）
- 工作模式：Active product lane max=`3`，Authority writer max=`1`；Active count=`2/3`，Review count=`0`
- 当前结论：T-P1A-018 已 merged（PR #39, commit `a1f965b`，含 OpenAPI UX P0/P1/P2 audit-fix）；T-P1A-019/020 仍在 Active；研究 lane 021/022/023/024/025 仍在 backlog（021 已 merged 为 research/done）；`PRD-v2-2026-05-04.md` / `SRD-v2-2026-05-04.md` 仍为 base authority；`audio_transcript` runtime 仍 blocked。
## 当前允许
- T-P1A-019 现可启动（018 已完成 storage/job 层）。Allowed Paths：`services/api/scoutflow_api/external_tools/**`、`metadata_probe_receipt_bridge.py`、`orchestration/**`（新建）。
- T-P1A-020 等 T-P1A-019 完成 orchestration 层后启动。
- 研究 lane 022/023/024/025 可继续写 `docs/research/` 研究笔记；非 authority，非 runtime approval。
## 当前禁止
- **`migrations/**` FORBIDDEN** — 任何 lane 不得动；schema 变更需另立 dispatch + user 显式授权 + 单独 PR + 外审。
- **`audio_transcript` runtime blocked** — `audio_transcript` capture mode 不被 `metadata-fetch/jobs` 路径接受；不启用 `audio_transcript` 任何 runtime 路径。
- T-P1A-019 lane 期间 `storage.py` 仅 read-only（018 已 merged，contract frozen until 020 完成 contract hardening）。
- T-P1A-019 不得写 `test_capture_trust_trace.py`（owned by T-P1A-020）。
- T-P1A-020 不得写 `external_tools/**`、`orchestration/**`、`metadata_probe_receipt_bridge.py`（owned by T-P1A-019）。
- 不创建或修改 `workers/`、`apps/`、`packages/`；`services/**` 仅任务明确授权时可动。
- 不触碰 `data/`、`referencerepo/`、凭据、raw cookie/token。
- 不运行 BBDown / yt-dlp / ffmpeg / ASR / browser automation。
- 不把 research note、draft spec、chat summary 写成 final authority；不启动 Phase 2-4 runtime。
- `PlatformResult` enum / `WorkerReceipt` schema / Trust Trace data shape 未经新 dispatch + 外审不得改动。
## 下一步
- Start T-P1A-019（metadata probe dry-run orchestrator；先建 `orchestration/` 模块 + `external_tools/` 抽象层）。参见 `docs/task-index.md` Wave 2 Conflict Domain。
- T-P1A-020 在 019 完成后启动（Trust Trace / Explore contract hardening；20 端到端测试依赖 19 orchestration）。
