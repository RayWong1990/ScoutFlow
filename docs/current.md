# Current
## 当前状态
- Phase / Step：`1A` / `B2_PREFLIGHT_CLOSED / B2_COMMANDER_READY`
- 主任务：`T-P1A-105` 已完成 commander-mode dispatch template extension + local `plan/` gitignore；PR #93 已由 T-P1A-103 supersede，PR #93 不得原样合并
- 工作模式：Active product lane max=`3`，Authority writer max=`1`；Active count=`0/3`，Review count=`0`；Authority writer count=`0/1`
- 当前结论：Wave 2 closed；Wave 3A closeout 已在 PR #67 记录完成；Wave 3B 的 bridge SPEC、H5 design package、vault SPEC、repo 外 prototype pointer、adapt decision table 已全部 landed（live PR `#70/#71/#72/#73/#74`）；Wave 4 B1 PR body/diff layer `verdict=clear`；Wave 4 B1 RAW control-plane 已由 `/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/REPAIR-Wave4-B1-control-plane-and-B2-preflight-2026-05-05.md` 和 `T-P1A-103` 修复；T-P1A-104 新增 tracked hash manifest `docs/research/repairs/t-p1a-104-control-plane-hash-manifest-2026-05-05.md` 供外审复核 RAW 文件 hash；T-P1A-105 将 commander-mode header fields 固化到 `docs/dispatch-template.md`，并把 `plan/` 定义为 gitignored local handoff workspace；PRD-v2.1 + SRD-v3 H5/Bridge 作为 B2 planning/contract addenda 通过 `user_override_for_B2_preflight` promoted；当前生效基线仍是 `Active product lane max=3` + `Authority writer max=1`

## 当前允许
- Wave 3B 已 closed；后续只允许 review / audit / report sync，不允许继续把 Wave 3B artifact 当作未落地 backlog 重跑
- `docs/research/shoulders/clone-plan-2026-05-05.md` 与 `docs/research/shoulders/referencerepo-index-2026-05-05.md` 继续保留为历史真相源；`referencerepo/**` 仍永远 local-only
- `plan/` 是 gitignored local handoff workspace，不是 authority surface，不进入 tracked truth
- B2 preflight 已关闭；B2 execution 可以进入 commander prompt 准备，但仍需按 normal validation 执行，不得把 preflight closure 当作 runtime/frontend/migration approval
- PRD-v2.1 + SRD-v3 H5/Bridge promoted addenda 仅作为 B2 planning/contract baseline；walking skeleton、visual gate、Bridge/VaultWriter runtime、vault commit 均仍需未来证据
- 外审可用 `docs/research/repairs/t-p1a-104-control-plane-hash-manifest-2026-05-05.md` 对本机 RAW 修复包做 hash/size/structure 复核；该 manifest 不复制 RAW 文件正文或 credential material

## 当前禁止
- `services/api/migrations/**` FORBIDDEN — migration dry-run plan / schema 变更 / migration 实施均需另立 dispatch + user 显式授权 + 单独 PR + 外审
- `audio_transcript` runtime blocked
- BBDown live / yt-dlp / ffmpeg / ASR / browser automation blocked
- `subprocess.run` 不得在 orchestrator 出现（19 tripwire test 已就位）
- 不创建或修改 `workers/`、`apps/`、`packages/`；`services/**` 仅任务明确授权时可动
- 不触碰 `data/`、`referencerepo/`、凭据、raw cookie/token、raw stdout/stderr
- 不把 research note、draft spec、chat summary 写成 final authority；不启动 Phase 2-4 runtime
- `PlatformResult` enum / `WorkerReceipt` schema / Trust Trace DTO 未经新 dispatch + 外审不得改动
- 不因 `user_override_for_B2_preflight` 推断 walking skeleton 已发生；不因 B2 preflight closure 解禁 frontend implementation、runtime、migration、vault commit、BBDown live、ffmpeg、ASR 或 browser automation

## 下一步
- 当前 next gate：B2 commander prompt；只允许基于修复后的 RAW control-plane package、T-P1A-104 hash manifest 与当前 authority state 编排下一批 bounded dispatch
- authority writer 当前空闲 `0/1`；后续并行 lane 仍受 `docs/specs/parallel-execution-protocol.md` 约束
- 任何 code-bearing migration / runtime / worker / frontend 启动都必须新 dispatch + 外审
