# Current

## TL;DR (5 行)

- main = `02ccbdc` (PR #252 W2C runtime surfaces wired) ← `a15b948` (PR #251 W2C lane open) ← `cd9d866` (PR #250 Stage0 authority refresh) ← `ec7870d` (PR #249 post-frozen W1/W1B/W2/W4/W5 candidate substrate); capture-station code baseline 已升级到 `02ccbdc` / PR #252 的 13 surface 真接 + 5 态状态机 + Trust Trace data shell (graph/timeline/error-path 留 W1B)
- Active product lane `1/3` / Authority writer `0/1` / `WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`
- write_enabled=False / 5 overflow lane Hold (true_vault_write / runtime_tools / browser_automation / dbvnext_migration / full_signal_workbench)
- PRD canonical = v2 + v2.1 amend (promoted); SRD canonical = v2 + v3-h5-bridge amend (promoted)
- 入口：`docs/00-START-HERE.md`; 路线图：`docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md` (candidate north-star)

## 当前状态
- Phase / Step：`1A` / `WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`
- 主任务：`T-P1A-156 / W2C` 已闭合 (PR #252 merge commit=`02ccbdc`，2026-05-08T03:46:55Z)；当前 code-bearing next gate 已重新打开为 `T-P1A-157 / W1B PF-C4-EXT trust-trace bounded lanes`。范围=`apps/capture-station/src/features/trust-trace/**` + W1B receipts/scope note + carry-forward sync；路径选择=`path-A self-rolled only`；`d3` fallback 继续保持 `evidence + Hermes + user gate` 才可开。W3E PF-C0-O1 保持 docs-only candidate lane，不占 active product slot。`Dispatch131 / T-P1A-110 ~ Dispatch172 / T-P1A-151` 已全部以 candidate docs/spec/visual/audit lanes landed；`Dispatch173 ~ Dispatch176 / T-P1A-152 ~ T-P1A-155` 已完成 Wave 5 closeout、Wave 6 candidate open 与 overflow/handoff candidate 落地；`PR #249` 已将 `docs/research/post-frozen/2026-05-08/{W1,W1B,W2,W4,W5}` candidate packs landed 到 `main`，供 W2C/W1B/W3E/W4 后续消费，但仍保持 `candidate / not-authority / not execution approval`；其中 `T-P1A-124 / T-P1A-125` 为 bounded frontend candidate surfaces，现已补齐 local frontend validation 与 bounded screenshot packet / Playwright execution evidence，但仍保持 `NOT_EXECUTION_APPROVED`，且不构成全局 visual terminal verdict、product UI approval、runtime approval、package strategy approval 或 frontend execution gate；`PR #93` 已由 `T-P1A-103` supersede，`PR #93` 不得原样合并
- 工作模式：Active product lane max=`3`，Authority writer max=`1`；Active count=`1/3`，Review count=`0`；Authority writer count=`0/1`
- 当前结论：Wave 2 closed；Wave 3A closeout 已在 PR #67 记录完成；Wave 3B 的 bridge SPEC、H5 design package、vault SPEC、repo 外 prototype pointer、adapt decision table 已全部 landed（live PR `#70/#71/#72/#73/#74`）；Wave 4 B1 control-plane repair / B2 preflight closure 已由 `T-P1A-103` + `T-P1A-104` 收口；Wave 4 Batch 3 将 vault helper stack、placeholder e2e baseline、5 Gate workflow、frontend lint/typecheck baseline、static Playwright harness、visual reporting template 全部 landed；Wave 5 candidate docs/spec/visual/audit chain（`T-P1A-110 ~ T-P1A-151`）现已 landed 并完成 closeout writeback；`PR #249` 已补齐 post-frozen `2026-05-08` 的 W1/W1B/W2/W4/W5 candidate substrate；`PR #250` 已完成 authority refresh；`PR #252 / T-P1A-156 / W2C` 已闭合并完成 13 surface 真接 + 5 态状态机 + Trust Trace data shell，CI 4 pass + e2e-placeholder-baseline 历史 stale fail (admin override 合规)，仍不构成 runtime、migration、browser automation、vault true write 或 full-signal execution approval；PRD-v2.1 + SRD-v3 H5/Bridge 继续仅作为 planning/contract addenda；当前生效基线仍是 `Active product lane max=3` + `Authority writer max=1`

## 当前允许
- Wave 3B 已 closed；后续只允许 review / audit / report sync，不允许继续把 Wave 3B artifact 当作未落地 backlog 重跑
- `T-P1A-156 / W2C` 已 closed (PR #252 merge `02ccbdc`)；当前允许的唯一 code-bearing capture-station lane 为 `T-P1A-157 / W1B PF-C4-EXT`，路径限定在 `apps/capture-station/src/features/trust-trace/**` + W1B receipts/scope note
- `docs/research/shoulders/clone-plan-2026-05-05.md` 与 `docs/research/shoulders/referencerepo-index-2026-05-05.md` 继续保留为历史真相源；`referencerepo/**` 仍永远 local-only
- `plan/` 是 gitignored local handoff workspace，不是 authority surface，不进入 tracked truth
- B2 preflight 已关闭；B2 execution 可以进入 commander prompt 准备，但仍需按 normal validation 执行，不得把 preflight closure 当作 runtime/frontend/migration approval
- Wave 4 closeout wording已记录；Wave 6 已完成 candidate open + overflow/handoff docs 收口；任何后续动作仍需从当前 authority 和新 dispatch 出发
- `docs/research/wave5/**`、`docs/specs/wave5/**`、`docs/visual/h5-capture-station/wave4-final/**`、`docs/visual/h5-capture-station/wave5/**` 当前已形成 landed candidate surfaces；它们仍不构成 runtime / migration / frontend implementation / browser automation / package approval
- PRD-v2.1 + SRD-v3 H5/Bridge promoted addenda 仅作为 B2 planning/contract baseline；walking skeleton、visual gate、Bridge/VaultWriter runtime、vault commit 均仍需未来证据
- `PR127 / T-P1A-101` 仍只保留为历史 handoff 命名；Wave 5 / Wave 6 candidate continuation 已由 `Dispatch131-176 / T-P1A-110 ~ T-P1A-155` landed；这不自动提升为 execution gate
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
- `T-P1A-156 / W2C` 已 closed；除 `T-P1A-157 / W1B PF-C4-EXT` 已开口的信任溯源 bounded lanes 外，其他 capture-station 改动 / 任何 services/api 改动仍需新 dispatch + 新 Active row + 外审
- 不因 `user_override_for_B2_preflight` 推断 walking skeleton 已发生；不因 B2 preflight closure 解禁 frontend implementation、runtime、migration、vault commit、BBDown live、ffmpeg、ASR 或 browser automation

## 下一步
- 当前 authority 已将 `Dispatch131-176 / T-P1A-110 ~ T-P1A-155` 视为已 landed 的 Wave 5 closeout + Wave 6 open/overflow/handoff chain；`PR #249` 补齐了 `docs/research/post-frozen/2026-05-08/**` 的 candidate substrate；`PR #252 / T-P1A-156 / W2C` 已闭合并完成 13 surface 真接 + 5 态状态机 + Trust Trace data shell；当前唯一 active code-bearing lane 为 `T-P1A-157 / W1B PF-C4-EXT`
- `Dispatch175 / T-P1A-154` 与 `Dispatch176 / T-P1A-155` 已落地为 overflow / handoff candidate truth；历史 handoff 名称不构成开工许可，后续仍需新 dispatch 明确范围
- authority writer 当前空闲 `0/1`；后续并行 lane 仍受 `docs/specs/parallel-execution-protocol.md` 约束；`T-P1A-157 / W1B PF-C4-EXT` 为当前唯一 active product lane；W3E PF-C0-O1 继续保持 docs-only candidate lane；W4 5 lane authority-upgrade spec 仍是后续候选 next-wave
- 任何 code-bearing migration / runtime / worker / frontend 启动都必须新 dispatch + 外审
