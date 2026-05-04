# Current
## 当前状态
- Phase / Step：`1A` / `Wave 2 — T-P1A-019 done; T-P1A-020 next executable`
- 主任务：T-P1A-020 Trust Trace / Explore contract hardening（next executable lane）
- 工作模式：Active product lane max=`3`，Authority writer max=`1`；Active count=`1/3`，Review count=`0`
- 当前结论：T-P1A-019 已 merged（PR #44, commit `44e87a1`，含 audit-fix commit `6dead72` 修复 provenance gate + failure receipt path）；T-P1A-020 仍在 Active；研究 lane 021/022/023/024/025 均已 merged，其中 022/023/024/025 已作为 frozen research 收口进 task-index Done；`PRD-v2-2026-05-04.md` / `SRD-v2-2026-05-04.md` 仍为 base authority；`audio_transcript` runtime 仍 blocked。
## 当前允许
- T-P1A-020 现可启动（019 已完成 orchestration 层）。Allowed Paths：`tests/api/test_capture_trust_trace.py`、`tests/contracts/test_trust_trace_contract.py`（新建可）。
- 研究 lane 021/022/023/024/025 已 merged；其中 022/023/024/025 可作为 Stage 2 amendment 的 stable research inputs 引用，均非 authority，非 runtime approval。
## 当前禁止
- **`migrations/**` FORBIDDEN** — 任何 lane 不得动；schema 变更需另立 dispatch + user 显式授权 + 单独 PR + 外审。
- **`audio_transcript` runtime blocked** — `audio_transcript` capture mode 不被 `metadata-fetch/jobs` 路径接受；不启用 `audio_transcript` 任何 runtime 路径。
- **BBDown live runtime blocked** — orchestrator 是 dry-run / injected-runner only；`subprocess.run` / 真实 BBDown / yt-dlp / ffmpeg / ASR / browser automation 全部不许走，任何引入新 runtime 均需另立 dispatch + user 显式授权 + 外审。
- T-P1A-020 lane 期间 `storage.py` / `captures.py` / `jobs.py` / `main.py` 仅 read-only（018 contract frozen）。
- T-P1A-020 不得写 `external_tools/**`、`orchestration/**`、`metadata_probe_receipt_bridge.py`（owned by T-P1A-019，contract frozen until 020 完成 contract hardening）。
- 不创建或修改 `workers/`、`apps/`、`packages/`；`services/**` 仅任务明确授权时可动。
- 不触碰 `data/`、`referencerepo/`、凭据、raw cookie/token、raw stdout/stderr。
- 不把 research note、draft spec、chat summary 写成 final authority；不启动 Phase 2-4 runtime。
- `PlatformResult` enum / `WorkerReceipt` schema / Trust Trace data shape 未经新 dispatch + 外审不得改动。
## 下一步
- Start T-P1A-020（Trust Trace / Explore contract hardening；写新 contract test 文件，不动 18/19 owned 文件）。参见 `docs/task-index.md` Wave 2 Conflict Domain。
- 020 完成后 Wave 2 product lanes 全部归档，可考虑开 Wave 3（如 BBDown live bounded probe T-P1A-021A）但需新 dispatch + user 显式授权。
