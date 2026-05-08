# Current

## TL;DR (5 行)

- main = `cd9d866` (PR #250 Stage0 authority refresh) ← `ec7870d` (PR #249 post-frozen W1/W1B/W2/W4/W5 candidate substrate) ← `6dd27d7` (PR #245 W2D memory graph); capture-station code baseline 仍为 `e1deda6` / PR #243 的 13 surface 静态壳 + tokens 三层 overlay
- Active product lane `1/3` / Authority writer `0/1` / `WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`
- write_enabled=False / 5 overflow lane Hold (true_vault_write / runtime_tools / browser_automation / dbvnext_migration / full_signal_workbench)
- PRD canonical = v2 + v2.1 amend (promoted); SRD canonical = v2 + v3-h5-bridge amend (promoted)
- 入口：`docs/00-START-HERE.md`; 路线图：`docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md` (candidate north-star)

## 当前状态
- Phase / Step：`1A` / `WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`
- 主任务：`T-P1A-156` 已作为当前 active product lane 打开；范围=`W2C PF-C4-02 frontend-first existing-route wiring + shared state adapter + disabled/future-gated honesty`；默认 allowed path 为 `apps/capture-station/src/**` + 选定 bridge/trust-trace test + W2C receipt，默认不改 `services/api/**`；`trust-trace/**` 在本轮只允许 readback/state shell，不允许 graph/timeline/error-path 实现；若 live contract mismatch 阻断 truthful rendering，必须拆单独 micro PR；`T-P1A-072` 继续仅作历史 authority ledger-open anchor。`Dispatch131 / T-P1A-110 ~ Dispatch172 / T-P1A-151` 已全部以 candidate docs/spec/visual/audit lanes landed；`Dispatch173 ~ Dispatch176 / T-P1A-152 ~ T-P1A-155` 已完成 Wave 5 closeout、Wave 6 candidate open 与 overflow/handoff candidate 落地；`PR #249` 已将 `docs/research/post-frozen/2026-05-08/{W1,W1B,W2,W4,W5}` candidate packs landed 到 `main`，供 W2C/W1B/W3E/W4 后续消费，但仍保持 `candidate / not-authority / not execution approval`；其中 `T-P1A-124 / T-P1A-125` 为 bounded frontend candidate surfaces，现已补齐 local frontend validation 与 bounded screenshot packet / Playwright execution evidence，但仍保持 `NOT_EXECUTION_APPROVED`，且不构成全局 visual terminal verdict、product UI approval、runtime approval、package strategy approval 或 frontend execution gate；`PR #93` 已由 `T-P1A-103` supersede，`PR #93` 不得原样合并
- 工作模式：Active product lane max=`3`，Authority writer max=`1`；Active count=`1/3`，Review count=`0`；Authority writer count=`0/1`
- 当前结论：Wave 2 closed；Wave 3A closeout 已在 PR #67 记录完成；Wave 3B 的 bridge SPEC、H5 design package、vault SPEC、repo 外 prototype pointer、adapt decision table 已全部 landed（live PR `#70/#71/#72/#73/#74`）；Wave 4 B1 control-plane repair / B2 preflight closure 已由 `T-P1A-103` + `T-P1A-104` 收口；Wave 4 Batch 3 将 vault helper stack、placeholder e2e baseline、5 Gate workflow、frontend lint/typecheck baseline、static Playwright harness、visual reporting template 全部 landed；Wave 5 candidate docs/spec/visual/audit chain（`T-P1A-110 ~ T-P1A-151`）现已 landed 并完成 closeout writeback；`PR #249` 已补齐 post-frozen `2026-05-08` 的 W1/W1B/W2/W4/W5 candidate substrate；`PR #250` 已完成 authority refresh；当前 code-bearing next gate 已显式收窄为 `T-P1A-156 / W2C` 一条 frontend-first lane，仍不构成 runtime、migration、browser automation、vault true write 或 full-signal execution approval；PRD-v2.1 + SRD-v3 H5/Bridge 继续仅作为 planning/contract addenda；当前生效基线仍是 `Active product lane max=3` + `Authority writer max=1`

## 当前允许
- Wave 3B 已 closed；后续只允许 review / audit / report sync，不允许继续把 Wave 3B artifact 当作未落地 backlog 重跑
- `T-P1A-156 / W2C` 当前可按 frontend-first 边界进入 code branch；允许 existing route 真接、shared state adapter、disabled/future-gated honesty、W2C receipt/checkpoint；默认不改 `services/api/**`
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
- `T-P1A-156 / W2C` 默认不改 `services/api/**`；若 truthful rendering 被 live contract blocker 卡住，必须 stop-the-line 并拆单独 micro PR，而不是在 W2C 主实现里顺手扩 backend
- 不因 `user_override_for_B2_preflight` 推断 walking skeleton 已发生；不因 B2 preflight closure 解禁 frontend implementation、runtime、migration、vault commit、BBDown live、ffmpeg、ASR 或 browser automation

## 下一步
- 当前 authority 已将 `Dispatch131-176 / T-P1A-110 ~ T-P1A-155` 视为已 landed 的 Wave 5 closeout + Wave 6 open/overflow/handoff chain；`PR #249` 则补齐了 `docs/research/post-frozen/2026-05-08/**` 的 candidate substrate；当前 code-bearing next gate 已显式打开为 `T-P1A-156 / W2C`，后续只允许在其 frontend-first 边界内推进
- `Dispatch175 / T-P1A-154` 与 `Dispatch176 / T-P1A-155` 已落地为 overflow / handoff candidate truth；历史 handoff 名称不构成开工许可，后续仍需新 dispatch 明确范围
- authority writer 当前空闲 `0/1`；后续并行 lane 仍受 `docs/specs/parallel-execution-protocol.md` 约束；W2C 实现阶段的 trust-trace graph/timeline/error-path 仍保留给 W1B
- 任何 code-bearing migration / runtime / worker / frontend 启动都必须新 dispatch + 外审
