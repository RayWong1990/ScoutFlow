# Current
## 当前状态
- Phase / Step：`1A` / `WAVE_5_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`
- 主任务：无 active product task；last authority writeback 从 `T-P1A-072` 进展到 post-mid-checkpoint continuation closeout truth；`T-P1A-073 ~ T-P1A-099` 已通过 Wave 4 Batch 2 + Batch 3 live PR chain 落地并闭环；`Dispatch128 / T-P1A-107` 与 `Dispatch129 / T-P1A-108` 已将视觉触点 roster 与 bridge-vault continuation gap matrix 写成 repo-visible candidate surfaces；`T-P1A-109` 已把 Wave 4 closeout 和 Wave 5 candidate opening 写回 authority；当前仍未打开新的 code-bearing next gate；`PR #93` 已由 `T-P1A-103` supersede，`PR #93` 不得原样合并
- 工作模式：Active product lane max=`3`，Authority writer max=`1`；Active count=`0/3`，Review count=`0`；Authority writer count=`0/1`
- 当前结论：Wave 2 closed；Wave 3A closeout 已在 PR #67 记录完成；Wave 3B 的 bridge SPEC、H5 design package、vault SPEC、repo 外 prototype pointer、adapt decision table 已全部 landed（live PR `#70/#71/#72/#73/#74`）；Wave 4 B1 control-plane repair / B2 preflight closure 已由 `T-P1A-103` + `T-P1A-104` 收口；Wave 4 Batch 3 将 vault helper stack、placeholder e2e baseline、5 Gate workflow、frontend lint/typecheck baseline、static Playwright harness、visual reporting template 全部 landed；Wave 4 closeout wording现已记录，Wave 5 进入 candidate docs/spec lane；但当前仍无 screenshot evidence、无本轮 Playwright execution evidence、无人类视觉终判；PRD-v2.1 + SRD-v3 H5/Bridge 继续仅作为 planning/contract addenda；当前生效基线仍是 `Active product lane max=3` + `Authority writer max=1`

## 当前允许
- Wave 3B 已 closed；后续只允许 review / audit / report sync，不允许继续把 Wave 3B artifact 当作未落地 backlog 重跑
- `docs/research/shoulders/clone-plan-2026-05-05.md` 与 `docs/research/shoulders/referencerepo-index-2026-05-05.md` 继续保留为历史真相源；`referencerepo/**` 仍永远 local-only
- `plan/` 是 gitignored local handoff workspace，不是 authority surface，不进入 tracked truth
- B2 preflight 已关闭；B2 execution 可以进入 commander prompt 准备，但仍需按 normal validation 执行，不得把 preflight closure 当作 runtime/frontend/migration approval
- Wave 4 closeout wording已记录；后续 continuation 进入 `Wave 5 candidate` docs/spec lane，仍需从当前 authority 和新 dispatch 出发
- `docs/research/wave5/**`、`docs/specs/wave5/**`、`docs/visual/h5-capture-station/wave4-final/**`、`docs/visual/h5-capture-station/wave5/**` 当前只允许作为 candidate docs/spec/visual surfaces 演进，不构成 runtime / migration / frontend implementation / browser automation / package approval
- PRD-v2.1 + SRD-v3 H5/Bridge promoted addenda 仅作为 B2 planning/contract baseline；walking skeleton、visual gate、Bridge/VaultWriter runtime、vault commit 均仍需未来证据
- `PR127 / T-P1A-101` 仍只保留为历史 handoff 命名；当前 continuation 以 `Dispatch131-144 / T-P1A-110 ~ T-P1A-123` 的 Wave 5 candidate docs/spec chain 为主，不自动提升为 active gate
- 外审可用 `docs/research/repairs/t-p1a-104-control-plane-hash-manifest-2026-05-05.md` 对本机 RAW 修复包做 hash/size/structure 复核；该 manifest 不复制 RAW 文件正文或 credential material

## 当前禁止
- `services/api/migrations/**` FORBIDDEN — migration dry-run plan / schema 变更 / migration 实施均需另立 dispatch + user 显式授权 + 单独 PR + 外审
- `audio_transcript` runtime blocked
- BBDown live / yt-dlp / ffmpeg / ASR / browser automation blocked
- `subprocess.run` 不得在 orchestrator 出现（19 tripwire test 已就位）
- 不创建或修改 `workers/`、`packages/`；`apps/**`、`services/**` 仅当前 dispatch 明确授权路径时可动
- 不触碰 `data/`、`referencerepo/`、凭据、raw cookie/token、raw stdout/stderr
- 不把 research note、draft spec、chat summary 写成 final authority；不启动 Phase 2-4 runtime
- `PlatformResult` enum / `WorkerReceipt` schema / Trust Trace DTO 未经新 dispatch + 外审不得改动
- 不因 `user_override_for_B2_preflight` 推断 walking skeleton 已发生；不因 B2 preflight closure 解禁 frontend implementation、runtime、migration、vault commit、BBDown live、ffmpeg、ASR 或 browser automation

## 下一步
- 当前 authority 已登记 `Dispatch131-144 / T-P1A-110 ~ T-P1A-123` 作为 Wave 5 candidate docs/spec continuation chain；但仍没有已打开的 code-bearing next gate
- 后续 bounded app rows 与更晚 authority rows仍需使用 dispatch slot + task ID 执行，并保留 scoped validation / internal audit；历史 handoff 名称不构成开工许可
- authority writer 当前空闲 `0/1`；后续并行 lane 仍受 `docs/specs/parallel-execution-protocol.md` 约束
- 任何 code-bearing migration / runtime / worker / frontend 启动都必须新 dispatch + 外审
