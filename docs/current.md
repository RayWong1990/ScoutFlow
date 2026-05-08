# Current

## TL;DR (5 行)

- main = `5902ecf` (PR #261 W4 closeout + truth repairs) ← `5777389` (PR #259 lane 4 manual-SQL candidate landed) ← `beb0fef` (PR #258 lane 2 runtime_tools candidate landed) ← `1fa0e9a` (PR #260 lane 1 true_vault_write candidate landed) ← `45e88d4` (PR #257 W4 Step0 convergence landed); capture-station code baseline 仍为 `d0dcbfe` / PR #255 的 W2C truthful runtime surfaces + 5 态状态机 + W1B Trust Trace graph/timeline/error-path bounded lanes
- Active product lane `0/3` / Authority writer `0/1` / `WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`
- write_enabled=False / 5 overflow lane Hold (true_vault_write / runtime_tools / browser_automation / dbvnext_migration / full_signal_workbench)
- PRD canonical = v2 + v2.1 amend (promoted); SRD canonical = v2 + v3-h5-bridge amend (promoted)
- 入口：`docs/00-START-HERE.md`; 路线图：`docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md` + `docs/BATCH-TRANSCRIPTION-MASTER-ROADMAP-2026-05-08.md`（均为 candidate north-star；前者管长期 north-star，后者管批量化转写 program）

## 当前状态
- Phase / Step：`1A` / `WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`
- 主任务：当前没有已打开的 code-bearing next gate。`T-P1A-156 / W2C` 已通过 `PR #253 / cf283f9` 完成 Layer C closeout；`T-P1A-157 / W1B PF-C4-EXT trust-trace bounded lanes` 已于 `PR #255 / d0dcbfe` landed 并闭合；`PR #254 / e18d45a` 仅补 `W3E PF-C0-O1` docs-only candidate starter cluster，不占 active product slot；`PR #257 / 45e88d4` 与 `PR #260/#258/#259` 已把 W4 Step0 + lane 1/2/4 candidate spec family 落到 `main`；`PR #261 / 5902ecf` 已完成 W4 closeout truth repair：`docs/memory/**` taxonomy 回退为 reference storage、W2C stale refresh guard、vault write default-blocked、status taxonomy guard、START-HERE ref-aware check attempt、以及 PR245 / PR247-249 / PR254 / PR255 / PR257 errata。PR261 自身仍暴露 CI START-HERE freshness failed、START-HERE/current anchor 未锚到 PR261 merge truth、PR body validation 与 CI readback 不一致，因此本 PR262 只做 final consistency closeout + W1B UI truth guard，不留下新的 active lane。`Dispatch131 / T-P1A-110 ~ Dispatch172 / T-P1A-151` 已全部以 candidate docs/spec/visual/audit lanes landed；`Dispatch173 ~ Dispatch176 / T-P1A-152 ~ T-P1A-155` 已完成 Wave 5 closeout、Wave 6 candidate open 与 overflow/handoff candidate 落地；`PR #249` 已将 `docs/research/post-frozen/2026-05-08/{W1,W1B,W2,W4,W5}` candidate packs landed 到 `main`，供 W2C/W1B/W3E/W4 后续消费，但仍保持 `candidate / not-authority / not execution approval`；其中 `T-P1A-124 / T-P1A-125` 为 bounded frontend candidate surfaces，现已补齐 local frontend validation 与 bounded screenshot packet / Playwright execution evidence，但仍保持 `NOT_EXECUTION_APPROVED`，且不构成全局 visual terminal verdict、product UI approval、runtime approval、package strategy approval 或 frontend execution gate；`PR #93` 已由 `T-P1A-103` supersede，`PR #93` 不得原样合并
- 工作模式：Active product lane max=`3`，Authority writer max=`1`；Active count=`0/3`，Review count=`0`；Authority writer count=`0/1`
- 当前结论：Wave 2 closed；Wave 3A closeout 已在 PR #67 记录完成；Wave 3B 的 bridge SPEC、H5 design package、vault SPEC、repo 外 prototype pointer、adapt decision table 已全部 landed（live PR `#70/#71/#72/#73/#74`）；Wave 4 B1 control-plane repair / B2 preflight closure 已由 `T-P1A-103` + `T-P1A-104` 收口；Wave 4 Batch 3 将 vault helper stack、placeholder e2e baseline、5 Gate workflow、frontend lint/typecheck baseline、static Playwright harness、visual reporting template 全部 landed；Wave 5 candidate docs/spec/visual/audit chain（`T-P1A-110 ~ T-P1A-151`）现已 landed 并完成 closeout writeback；`PR #249` 已补齐 post-frozen `2026-05-08` 的 W1/W1B/W2/W4/W5 candidate substrate；`PR #257/#260/#258/#259` 已把 Step0 + lane 1/2/4 candidate north-star family 吸收进 live main；`PR #261 / T-P1A-158` 又把 W2C runtime stale refresh 回写风险、vault write 默认乐观态、START-HERE PR-check ref 语义、status taxonomy guard 和 `docs/memory/**` authority taxonomy 全部压回 truthful guardrail，但其 validation/anchor closeout 不 clean，本 PR262 记录 erratum 并收口。5 overflow lane 继续 Hold，仍不构成 runtime、migration、browser automation、vault true write 或 full-signal execution approval；`docs/research/repairs/pr245-memory-authority-taxonomy-erratum-2026-05-08.md`、`docs/research/repairs/pr247-pr249-start-here-validation-erratum-2026-05-08.md`、`docs/research/repairs/pr254-start-here-authority-touch-erratum-2026-05-08.md`、`docs/research/repairs/pr255-authority-writeback-erratum-2026-05-08.md` 与 `docs/research/repairs/pr257-start-here-boundary-erratum-2026-05-08.md` 已补齐审计轨迹；PR255 的 W1B UI truth bug 在本 PR262 作为 bounded frontend truth repair 修复，不打开新的 active product lane。当前生效基线仍是 `Active product lane max=3` + `Authority writer max=1`

## 当前允许
- Wave 3B 已 closed；后续只允许 review / audit / report sync，不允许继续把 Wave 3B artifact 当作未落地 backlog 重跑
- 当前没有已打开的 code-bearing capture-station lane；`T-P1A-158` 已作为一次性 bounded repair 在 `PR #261` 内收口，任何后续 capture-station 改动仍必须由新 dispatch + 新 Active row + 外审重新开口
- `docs/research/shoulders/clone-plan-2026-05-05.md` 与 `docs/research/shoulders/referencerepo-index-2026-05-05.md` 继续保留为历史真相源；`referencerepo/**` 仍永远 local-only
- `plan/` 是 gitignored local handoff workspace，不是 authority surface，不进入 tracked truth
- B2 preflight 已关闭；B2 execution 可以进入 commander prompt 准备，但仍需按 normal validation 执行，不得把 preflight closure 当作 runtime/frontend/migration approval
- Wave 4 closeout wording已记录；Wave 6 已完成 candidate open + overflow/handoff docs 收口；任何后续动作仍需从当前 authority 和新 dispatch 出发
- `docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/{00,01,02,04}*.md` 现已形成 landed candidate north-star family；可作为 lane 1/2/4 后续 dispatch、audit、promotion gate 输入，但不构成 lane 解禁
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
- `T-P1A-156 / W2C`、`T-P1A-157 / W1B PF-C4-EXT` 与 `T-P1A-158 / W2C runtime truth repair` 均已闭合；任何新的 capture-station 改动 / 任何 services/api 改动仍需新 dispatch + 新 Active row + 外审
- `PR #255` 的 ErrorPathLane / GraphLane / `audio_transcript` 相关真值问题只能在本 PR262 这种 bounded repair PR 内修复；不得把该修复解释成 backend DTO/schema/runtime 解禁
- 不因 `user_override_for_B2_preflight` 推断 walking skeleton 已发生；不因 B2 preflight closure 解禁 frontend implementation、runtime、migration、vault commit、BBDown live、ffmpeg、ASR 或 browser automation

## 下一步
- 当前 authority 已将 `Dispatch131-176 / T-P1A-110 ~ T-P1A-155` 视为已 landed 的 Wave 5 closeout + Wave 6 open/overflow/handoff chain；`PR #249` 补齐了 `docs/research/post-frozen/2026-05-08/**` 的 candidate substrate；`PR #253/#254/#255/#257/#260/#258/#259/#261` 已写回为 live merged truth；本 PR262 只收口 PR226-PR261 consistency gaps 与 W1B UI truth guard，当前没有 active code-bearing lane
- `Dispatch175 / T-P1A-154` 与 `Dispatch176 / T-P1A-155` 已落地为 overflow / handoff candidate truth；历史 handoff 名称不构成开工许可，后续仍需新 dispatch 明确范围
- authority writer 当前空闲 `0/1`；后续并行 lane 仍受 `docs/specs/parallel-execution-protocol.md` 约束；W3E PF-C0-O1 继续保持 docs-only candidate lane；W4 Step0 + lane 1/2/4 已完成 spec family closeout，但 5 overflow lane 仍全部 Hold
- 任何 code-bearing migration / runtime / worker / frontend 启动都必须新 dispatch + 外审
