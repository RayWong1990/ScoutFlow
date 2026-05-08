# Current

## TL;DR (5 行)

- main = `3a64cb9` (PR #271 Lane D PF-V visual productization merged) ← `376ec0c` (PR #263 remediation sub-wave lane-open) ← `db80ad7` (PR #262 close PR226-PR261 consistency gaps) ← `5902ecf` (PR #261 W4 closeout + truth repairs) ← `5777389` (PR #259 lane 4 manual-SQL candidate landed); capture-station code baseline 已升到 Lane D merged truth：W2C truthful runtime surfaces + 5 态状态机 + W1B Trust Trace bounded lanes + PF-V visual state primitives (`StateBadge` / `HoldBanner` / `EvidenceTable` / lane-order tokens)
- Active product lane `3/3` / Authority writer `0/1` / `WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`
- write_enabled=False / 5 overflow lane Hold (true_vault_write / runtime_tools / browser_automation / dbvnext_migration / full_signal_workbench)
- PRD canonical = v2 + v2.1 amend (promoted); SRD canonical = v2 + v3-h5-bridge amend (promoted)
- 入口：`docs/00-START-HERE.md`; 路线图：`docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md` + `docs/BATCH-TRANSCRIPTION-MASTER-ROADMAP-2026-05-08.md`（均为 candidate north-star；前者管长期 north-star，后者管批量化转写 program）

## 当前状态
- Phase / Step：`1A` / `WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`
- 主任务：`PR #271 / 3a64cb9` 已将 `T-P1A-LANE-D-CODE-BEARING` 的 visual primitives 落到 `main`，满足本轮 Round 3 promote 前置。当前进入 `Phase 1 remediation sub-wave Round 3`：Active=`T-P1A-160`（Lane A）+ `T-P1A-161`（Lane B）+ `T-P1A-162`（Lane C）；Lane D=`done`；Review/docs-only=`Lane-D-CANDIDATE-DOCS` + `T-P1V-BAT-PREP` + `T-P1V-MANUAL-EVIDENCE` + `T-P1V-MONITOR`。本次 promote 只做 slot replacement，不新增第 4 条 active lane，也不构成 visual closeout。
- 工作模式：Active product lane max=`3`，Authority writer max=`1`；Active count=`3/3`，Review count=`4`；Authority writer count=`0/1`
- 当前结论：Lane D 已 merged 并转入 Done，Lane A 已从 Blocked promote 到 Active，当前 Active 仍严格为 `3/3`（A+B+C，slot replacement）。`write_enabled=False` 继续是硬真相；5 overflow Hold（`true_vault_write` / `runtime_tools` / `browser_automation` / `dbvnext_migration` / `full_signal_workbench`）全部不变；`master spec §13` 全 Hold 仍在；本轮仍不解禁 runtime / true write / migration / browser automation / dependency install，也不把 Opus-2 visual REJECT 写成已 closeout。

## 当前允许
- 当前允许的直接后续包括 `T-P1A-160` 的 Round 3 code-bearing 实施与其 localhost / visual audit 准备；`T-P1A-161` / `T-P1A-162` 继续保持 active；Round 3 之后仍不得跳过 Round 4/5 直接 closeout
- Wave 3B 已 closed；后续只允许 review / audit / report sync，不允许继续把 Wave 3B artifact 当作未落地 backlog 重跑
- 当前 capture-station code-bearing 允许 `T-P1A-160` 在已合入的 Lane D primitives 基础上推进 single-item preview vertical slice；`T-P1A-158` 已作为一次性 bounded repair 在 `PR #261` 内收口；任何超出 Lane A 当前 dispatch 或回头改写 Lane D owned path 的改动仍必须新 dispatch + 新 Active row + 外审
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
- `PR #255` / `PR #262` 之后，任何新的 UI / visual truth 修补都只能在当前已登记 dispatch 边界内进行；不得把视觉修补解释成 backend DTO/schema/runtime 解禁，`audio_transcript` 仍 blocked
- 不因 `user_override_for_B2_preflight` 推断 walking skeleton 已发生；不因 B2 preflight closure 解禁 frontend implementation、runtime、migration、vault commit、BBDown live、ffmpeg、ASR 或 browser automation

## 下一步
- 当前 authority 已将 `PR #271 / 3a64cb9` 视为本轮 Round 3 promote 的 live baseline；`T-P1A-160` + `T-P1A-161` + `T-P1A-162` 已注册为 active `3/3`，`T-P1A-LANE-D-CODE-BEARING` 已转入 Done；`Lane-D-CANDIDATE-DOCS` / `T-P1V-BAT-PREP` / `T-P1V-MANUAL-EVIDENCE` / `T-P1V-MONITOR` 继续作为 review/docs-only support lanes
- `Dispatch175 / T-P1A-154` 与 `Dispatch176 / T-P1A-155` 已落地为 overflow / handoff candidate truth；历史 handoff 名称不构成开工许可，后续仍需新 dispatch 明确范围
- authority writer 当前空闲 `0/1`；后续并行 lane 仍受 `docs/specs/parallel-execution-protocol.md` 约束；当前 next-step 已切到 Round 4/5/6：Lane A PR 完成后走战友 localhost `V-PASS`、再走 Opus-3 `V-PASS-CLEAR`、最后由 `PR-C` 做 closeout；W4 Step0 + lane 1/2/4 已完成 spec family closeout，但 5 overflow lane 仍全部 Hold
- 任何 code-bearing migration / runtime / worker / frontend 启动都必须新 dispatch + 外审
