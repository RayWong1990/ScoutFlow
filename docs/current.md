# Current
## 当前状态
- Phase / Step：`1A` / `Wave 3B open`
- 主任务：`T-P1A-043` 已完成 Wave 3B ledger open；next gate = `T-P1A-044 / PR #69`
- 工作模式：Active product lane max=`3`，Authority writer max=`1`；Active count=`0/3`，Review count=`0`；Authority writer count=`0/1`
- 当前结论：Wave 2 closed；Wave 3A closeout 已在 PR #67 记录完成；Wave 3B ledger 已打开并写入 clone plan / referencerepo tracked mirror；本波 clone/probe 计划锁定 4 个优先 clone 目标（`iFurySt/RedNote-MCP`、`ShellyDeng08/rednote-analyzer-mcp`、`satnaing/shadcn-admin`、`yt-dlp/yt-dlp`），保留 `Nemo2011/bilibili-api` 与 `Kiranism/tanstack-start-dashboard` 作为 reserve；`docs/shoulders-index.md` 已从 closeout 态推进到 `3 locked / 5 scanning / 11 discovered`；当前生效基线仍是 `Active product lane max=3` + `Authority writer max=1`；Wave 3B 仍不解禁任何 runtime、migration、或 Phase 2+ 实施

## 当前允许
- Wave 3B 当前已允许 `T-P1A-044 ~ T-P1A-050`（PR #69-#75）按既定串行门推进：`probe -> bridge SPEC -> design brief -> vault SPEC -> repo 外 prototype -> adapt decision -> closeout`
- `docs/research/shoulders/clone-plan-2026-05-05.md` 与 `docs/research/shoulders/referencerepo-index-2026-05-05.md` 是当前 Wave 3B clone/probe 真相源；`referencerepo/**` 仍永远 local-only
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
- 当前 next gate：`T-P1A-044 / PR #69`，主题为 Shoulders Probe Reports（单 PR 最多 4 个 shoulder）；仅放行 probe/report 层，不放行 runtime / migration / Phase 2+ 实施
- authority writer 当前空闲 `0/1`；后续并行 lane 仍受 `docs/specs/parallel-execution-protocol.md` 约束
- 任何 code-bearing migration / runtime / worker / frontend 启动都必须新 dispatch + 外审
