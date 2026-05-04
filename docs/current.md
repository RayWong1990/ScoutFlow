# Current
## 当前状态
- Phase / Step：`1A` / `Wave 3A closed`
- 主任务：`T-P1A-042` 已完成 closeout；next gate = `Wave 3B ledger open / PR #68`（Wave 3B gate=`GO`，待 PR68 正式开账）
- 工作模式：Active product lane max=`3`，Authority writer max=`1`；Active count=`0/3`，Review count=`0`；Authority writer count=`0/1`
- 当前结论：Wave 2 closed；Wave 3 reference docs landed（PR #55 / T-P1A-030, merge `395a7e6`）；Wave 3A 的 ADR / PRD candidate / SRD candidate / PR Factory protocol candidate / repo 外 OpenDesign probe / 四个 shoulder scan / PR Factory tooling helper 已全部落地（live PR `#57/#58/#64/#59/#62/#65/#60/#61/#63/#66`）；`docs/specs/parallel-execution-protocol.md` 已同步 `Codex Commander Fan-out` 实战硬化，但当前生效基线仍是 `Active product lane max=3` + `Authority writer max=1`；Wave 3A 仍不解禁任何 runtime；不修改 `PRD-v2-2026-05-04.md` / `SRD-v2-2026-05-04.md` base authority；SRD-v3 remains candidate-only；`docs/shoulders-index.md` 已完成 scan-closeout 同步（3 locked / 4 scanning / 12 discovered）

## 当前允许
- `PR #68` 可打开 Wave 3B ledger，并创建 shoulders clone plan / referencerepo tracked mirror；在此之前 PR69+ 不得开跑
- `docs/shoulders-index.md` 的下一轮状态推进必须基于已落地 scan artifact 或后续 clone/probe/decision artifact；PR67 仅完成 Wave 3A closeout 同步
- `docs/specs/parallel-execution-protocol.md` 已纳入 `Codex Commander Fan-out` 模式，但仅作为流程硬化；不代表 product lane 上限提升或 authority 多写者放行

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
- 当前 next gate：`Wave 3B ledger open / PR #68`，主题为 ledger open + shoulders clone plan；仅放行 ledger / clone-plan 层，不放行 runtime / migration / Phase 2+ 实施
- authority writer 当前空闲 `0/1`；后续并行 lane 仍受 `docs/specs/parallel-execution-protocol.md` 约束
- 任何 code-bearing migration / runtime / worker / frontend 启动都必须新 dispatch + 外审
