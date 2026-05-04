# Current
## 当前状态
- Phase / Step：`1A` / `Wave 3A open`
- 主任务：T-P1A-031（PR #56）— Wave 3A ledger open + shoulders-index
- 工作模式：Active product lane max=`3`，Authority writer max=`1`；Active count=`0/3`，Review count=`0`；本 PR 占 authority writer `1/1`，merge 后归 `0/1`
- 当前结论：Wave 2 closed；Wave 3 reference docs landed（PR #55 / T-P1A-030, merge `395a7e6`）；Wave 3A open（PR #56 / T-P1A-031），范围为顺延后 PR56-PR67（12 PR，T-P1A-031 ~ T-P1A-042）；Wave 3A 不解禁任何 runtime；不修改 `PRD-v2-2026-05-04.md` / `SRD-v2-2026-05-04.md` base authority；SRD-v3 remains candidate-only；`docs/shoulders-index.md` 已就位（19 entries；3 locked / 16 discovered；transition rule per errata P1-10）

## 当前允许
- Wave 3A 12 PR 范围（顺延后 PR56-PR67）：T-P1A-031 ledger open；T-P1A-032 ADR-001 Obsidian PARA Lock；T-P1A-033 PRD v2.1 Strong Visual H5 candidate；T-P1A-034 SRD v3 H5 Bridge PARA vault candidate；T-P1A-035 Parallel Execution Protocol PR factory candidate；T-P1A-036 OpenDesign H5 visual probe（repo 外）；T-P1A-037 ~ T-P1A-040 四个 shoulder scan；T-P1A-041 PR factory V1 tooling plan + scripts；T-P1A-042 Wave 3A closeout
- `docs/shoulders-index.md` 后续可被 PR62-65 scan 与 PR68-73 probe/decide read/write；任何 status 提升必须有对应 scan/probe/decision artifact
- 任何 Wave 3A 内 PR 启动都需 user 显式授权 + decision-log 单独 entry

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
- PR56 merge 后 authority writer 归 `0/1`，释放 Wave 3A 后续并行 lane
- 建议下一个 user gate：T-P1A-032 ADR-001 Obsidian PARA Lock（PR #57，顺延后，原 doc3 §2），优先锁定 vault 边界且无 product-code path dependency
- 任何 code-bearing migration / runtime / worker / frontend 启动都必须新 dispatch + 外审
