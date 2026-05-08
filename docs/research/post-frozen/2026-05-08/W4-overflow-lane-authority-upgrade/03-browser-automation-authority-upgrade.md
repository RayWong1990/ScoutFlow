---
title: Browser Automation Authority-Upgrade Roadmap
status: candidate
authority: not-authority
authority_state: not-execution-approved
created_by: gpt-pro
parent_cluster: W4
lane: browser_automation
prerequisite_check: refreshed_2026-05-07T17:15:02Z
master_spec_anchor: §16.1 (硬红线) + §16.2 (升级路径) + §14.2 (pre-flight) + §16.3 (风险矩阵)
disclaimer: |
  本文是 candidate authority-upgrade roadmap, 不是 lane 完成权限升级的证据.
  Lane 解禁需要走完整 §3 pre-flight 5 步 + Hermes 外审 V-PASS + 磊哥显式授权 + spec PR merge.
  本文内的 PR # / file path / SHA 标 "(撰写时刻历史参考, 真值以 §0.5 Check 为准)".
---

# Browser Automation Authority-Upgrade Roadmap

> 本文产出的是 browser_automation 的 candidate authority-upgrade roadmap。当前没有明确 use case 时, 本 lane 的第一动作必须是 use-case intake, 不是 tool-first 浏览器自动化。

## §0.5 Prerequisite Check

> refreshed_at: `2026-05-07T17:15:02Z`. 本段是本文件的真态读回锚, 任一后续 agent 接收本文时必须再次刷新, 不得把本文数值当永久 authority。

| Check | 刷新真态 | Drift / 处理 |
|---|---|---|
| 1 — main HEAD | `6dd27d74c214c3e4768196b59f986a6d226f6699`; message=`feat(memory): cross-vendor memory graph W2D land (16 instinct memory) (#245)` | 与提示词里 `c802de4` / `4792b0f` 叙述存在 chronological drift; 本文引用 main HEAD 时以 Check 1 为准。PR #245/#247/#248 均标注「撰写时刻历史参考, 真值以 §0.5 Check 为准」。 |
| 2 — current.md | Active product lane `0/3`; Authority writer `0/1`; state=`WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`; 5 overflow lane Hold 仍列明。 | current.md body 仍写 `c802de4` 作为 main anchor, 低风险 authority-body drift; 不改变 lane 边界。 |
| 3 — task-index.md | Active `0/3`; Review `0`; Authority writer `0/1`; Phase=`Phase 1A — WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`。 | 与提示词一致。 |
| 4 — decision-log.md | PR #247 metadata 明示加入 `D-017 follow-up`; 提示词历史锚点 D-016 已不是唯一候选最新。 | 本文写作时将 D-016 视为历史参考, D-017+ 由 CC0/CC1 接收时复核 decision-log tail。 |
| 5 — memory INDEX | `batch_count: 17`; Lessons 7 / Feedback 5 / Patterns 5; 重点含 L-RUNTIME-APPROVAL-DRIFT, L-MIGRATION-DRIFT, L-OVEROBJECTIFICATION, P-PROOF-PAIR-CANARY, P-OVERFLOW-NOT-BLOCKER。 | 与提示词一致。 |
| 6 — bridge config | `write_enabled=False` 在未配置 vault root 分支与已配置 vault root 分支均成立。 | 与提示词一致; 本文不改变该 invariant。 |
| B-lane sanity | `bridge/router.py` 当前暴露 bridge health / vault config / vault preview / vault commit dry-run 4 个 route decorator; migrations baseline 仅 001/002; capture-station package 未见 Playwright / Selenium dependency。 | 提示词里「5 routes」按历史参考处理, 真值以 router 文件为准。 |

**读回证据 URL 包**: main commit API, `docs/current.md`, `docs/task-index.md`, `docs/decision-log.md`, `docs/memory/INDEX.md`, `services/api/scoutflow_api/bridge/config.py`, `services/api/scoutflow_api/bridge/router.py`, `services/api/migrations/001_phase1a_capture_creation.sql`, `services/api/migrations/002_phase1a_jobs_receipt.sql`, `apps/capture-station/package.json`。

## §1 Lane 当前态

### §1.1 Lane forbidden 边界引用

- current.md 当前禁止段列明 browser automation blocked。
- master spec §16.1 锁定视觉终判由战友浏览器 review 拍板, 自动化截图不是 V-PASS。
- master spec §16.2 对 browser_automation 的升级路径要求明确 use case; 当前无 use case, 所以不能空头升级。
- capture-station package.json 当前没有 Playwright / Selenium dependency; 这是真态边界证据。
- 5 Gate aesthetic checklist 是人工视觉硬门, automation 只能辅助 smoke / evidence packet。

### §1.2 Lane 现状真态

| 维度 | 真态 | 本 roadmap 处理 |
|---|---|---|
| Playwright/Selenium dependency | no runtime dependency in package.json | 不添加依赖, 只定义升级路线 |
| use case | 当前提示词未给明确用例 | D-BA-001 必须先收敛 use case |
| visual terminal verdict | 仍由战友亲眼 V-PASS | automation 不替代 |
| motion boundary | motion 不得渗透 wiki/reading surface | D-BA-004 单独管 |
| subprocess boundary | 与 runtime_tools 一样需要 tripwire | 只定义边界, 不运行 |

### §1.3 风险矩阵

| 风险 | Severity | 具体失败模式 | 必需缓解 |
|---|---|---|---|
| 视觉终判信任 | critical | screenshot / CI pass 被误读为战友 V-PASS | human verdict invariant + evidence label |
| runtime cost | medium | headless browser 占资源, CI flake 高 | use case gating + bounded smoke |
| Motion 渗透 | high | automation 为了截图引入 motion lib / reading surface 动效 | motion boundary spec + no new UI lib |
| 5 Gate 自动化局限 | high | 自动评分替代审美判断 | 5 Gate human lock |
| subprocess.run tripwire | high | browser launch 被塞进不合适 orchestrator | automation runner boundary + tripwire |
| credential/browser profile | critical | 使用本地 profile 或 auth state 产生隐性 credential risk | no browser profile / no credential material |

### §1.4 实施前置条件

1. 必须有具体 use case: 目标 surface、需要验证的用户行为、为什么普通 unit/contract test 不够。
2. 必须明示 automation 输出是辅助 evidence, 不替代 V-PASS。
3. 必须证明不会引入 motion 渗透、generic admin drift 或外部 UI lib。
4. 必须不触碰 runtime_tools: browser automation 不得顺手做 scraping/download。
5. 必须不触碰 true_vault_write/dbvnext_migration。

### §1.5 24h 内 actionable consumer

- CC1 可在 24h 内把 D-BA-001 写成 use-case intake spec。
- Hermes 可审 D-BA-002/003 中的 human verdict invariant。
- Codex 仅在具体 use case 与 commander prompt 齐备后消费 D-BA-005。

## §2 升级路径

### §2.1 推荐路径

推荐路径: use-case intake → automation boundary → human V-PASS lock → motion guard → Hermes → explicit user gate。

1. 无 use case 不启动。
2. 有 use case 后, 只允许 e2e smoke / evidence packet, 不允许替代视觉终判。
3. 5 Gate 人工判断必须在 spec PR 里锁死。
4. Hermes 重点审 use case 是否具体、automation 与视觉验收是否混淆。

### §2.2 路径理由

browser_automation 的危险不是工具本身, 而是它很容易把「看起来跑过」误写成「视觉已过」。ScoutFlow 强视觉是一级轴, automation 只能帮助捕获重复性证据, 不能替代战友对视觉层级、空间、遮挡、字体、重量的判断。

### §2.3 不推荐路径 + 反模式

- 不推荐「先装 Playwright 再找用途」: 这会制造无 consumer 的 spec。
- 不推荐「用 screenshot diff 做审美判断」: diff 只能发现变化, 不能判断美感。
- 不推荐「browser automation 兼做 source scraping」: 那会越界到 runtime_tools。
- 不推荐「把 CI pass 当 product UI green light」: CI 不是 human V-PASS。

### §2.4 候选时间窗

- 撰写时刻历史参考: master spec §17 将 browser automation 放在中长期, 且要求 use case 前置。
- 24h 内最可行动: D-BA-001 use case intake, 而不是任何工具安装。
- 若无 use case, 本 lane 应保持 Hold, 让 lane 1/4/5 优先。

## §3 Pre-flight 5 步

### §3.1 Step 1: task-index 注册

- 注册 T-LANE-BA-XXX, 占 Active product lane 1/3。
- scope 必须写明 use case ID; 若没有 use case ID, 不得注册 implementation task。
- validation 必含 human V-PASS invariant。

### §3.2 Step 2: decision-log D-XXX 草稿

- 草稿说明 browser_automation 只进入 use-case gated candidate path。
- 草稿必须写: automation evidence auxiliary, human visual terminal verdict retained。
- 草稿必须列 no-goals: no scraping/runtime, no vault write, no migration。

### §3.3 Step 3: Hermes pre-flight 外审 prompt

- Hermes 审 use case 具体性、visual verdict 混淆、motion 渗透、credential/browser profile risk。
- 若 Hermes 判 use case vague, verdict 应为 V-PARTIAL 或 V-REJECT。

### §3.4 Step 4: CC1 commander prompt v1 草稿

- prompt 必须引用 use case ID 与 target surface。
- prompt 必须说明 screenshot evidence 的用途与限制。
- prompt 不得暗示 automation 替代战友亲眼审。

### §3.5 Step 5: 磊哥显式授权 + paste Codex

- 磊哥授权必须指向一个具体 use case。
- 若授权只是「打开浏览器自动化」而无 use case, 应回到 D-BA-001。
- Codex closeout 必须标 human verdict 是否发生; 若未发生, 不得写 terminal visual verdict。

## §4 Dispatch templates
### D-BA-001 — use case 必填 spec
- id: `D-BA-001`
- status: candidate
- parent_lane: `browser_automation`
- dependency: 无; 当前缺明确 use case
- TL;DR: 在没有具体 use case 前, 只允许定义 use-case intake schema, 不允许空头打开 Playwright/Selenium。
- 输入包:
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/00-START-HERE.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/decision-log.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/memory/INDEX.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/locked-principles.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/contracts-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/apps/capture-station/package.json
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/visual/h5-capture-station/wave4-final/wave4-visual-touchpoint-roster-and-localhost-plan-candidate-2026-05-05.md
- 输出 deliverable:
  - `docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/dispatch-packets/D-BA-001-use-case-intake-candidate.md`
- 验收标准:
  - use case schema 含 target surface / risk / human verdict role
  - 明确无 use case = stop
  - 不选择工具栈
- 反模式 REGENERATE:
  - REGENERATE: 空头写 browser automation general enablement
  - REGENERATE: 把 visual terminal verdict 自动化
  - REGENERATE: 未列 human reviewer
- pre-flight check:
  - 读取 current browser blocked
  - 读取 package dependency truth
  - 读取 master spec §16.1 visual rules
  - 确认 no use case evidence
- self-verification:
  - use case fields complete
  - stop condition present
  - no dependency install
  - human V-PASS invariant present
  - candidate label intact
### D-BA-002 — Playwright 边界 spec
- id: `D-BA-002`
- status: candidate
- parent_lane: `browser_automation`
- dependency: D-BA-001 有具体 use case 后
- TL;DR: 定义 browser automation 只用于 e2e smoke / screenshot evidence packet, 不替代人工视觉终判。
- 输入包:
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/00-START-HERE.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/decision-log.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/memory/INDEX.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/locked-principles.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/contracts-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/apps/capture-station/package.json
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/visual/h5-capture-station/wave4-final/wave4-visual-touchpoint-roster-and-localhost-plan-candidate-2026-05-05.md
- 输出 deliverable:
  - `docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/dispatch-packets/D-BA-002-playwright-boundary-candidate.md`
- 验收标准:
  - e2e smoke vs visual verdict 分界清楚
  - screenshot evidence 只作辅助
  - no browser profile/credential
- 反模式 REGENERATE:
  - REGENERATE: 把截图当 V-PASS
  - REGENERATE: 把 automation 扩展到 scraping/runtime_tools
  - REGENERATE: 引入 browser profile
- pre-flight check:
  - 复核 use case
  - 读取 5 Gate visual rules
  - 确认 package no Playwright
  - 列 automation side effects
- self-verification:
  - boundary table present
  - human verdict retained
  - no credential/browser profile
  - no motion leak
  - candidate label intact
### D-BA-003 — 5 Gate 人工 V-PASS 不被替代 spec lock
- id: `D-BA-003`
- status: candidate
- parent_lane: `browser_automation`
- dependency: D-BA-001
- TL;DR: 把视觉层级、空间对齐、遮挡安全、字体可读、视觉重量的人工 gate 固化为 automation 不可替代项。
- 输入包:
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/00-START-HERE.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/decision-log.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/memory/INDEX.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/locked-principles.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/contracts-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/apps/capture-station/package.json
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/visual/h5-capture-station/wave4-final/wave4-visual-touchpoint-roster-and-localhost-plan-candidate-2026-05-05.md
- 输出 deliverable:
  - `docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/dispatch-packets/D-BA-003-five-gate-human-lock-candidate.md`
- 验收标准:
  - 5 Gate 每项有人工 reviewer 字段
  - automation evidence 标 auxiliary
  - V-PASS 只由战友浏览器 review 拍板
- 反模式 REGENERATE:
  - REGENERATE: 自动评分替代审美判断
  - REGENERATE: 省略遮挡安全
  - REGENERATE: 把 CI pass 当 visual pass
- pre-flight check:
  - 读取 START-HERE visual redlines
  - 读取 memory F-STRONG-VISUAL-FIRST-CLASS
  - 读取 visual roster candidate
  - 确认 no terminal verdict
- self-verification:
  - 5 Gate complete
  - human role explicit
  - CI/automation not final
  - no generic admin drift
  - candidate label intact
### D-BA-004 — Motion 渗透防护 spec
- id: `D-BA-004`
- status: candidate
- parent_lane: `browser_automation`
- dependency: D-BA-002/003
- TL;DR: 限制 browser automation 与 motion evidence 的用途, 防止 motion 渗透到 wiki/reading surface 或审美决策。
- 输入包:
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/00-START-HERE.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/decision-log.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/memory/INDEX.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/locked-principles.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/contracts-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/apps/capture-station/package.json
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/visual/h5-capture-station/wave4-final/wave4-visual-touchpoint-roster-and-localhost-plan-candidate-2026-05-05.md
- 输出 deliverable:
  - `docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/dispatch-packets/D-BA-004-motion-boundary-candidate.md`
- 验收标准:
  - motion allowed/forbidden surfaces 明确
  - automation 不引入新 animation dependency
  - reading surface no motion drift
- 反模式 REGENERATE:
  - REGENERATE: 把 motion 当 polish 无边界扩张
  - REGENERATE: 引入 generic animation lib
  - REGENERATE: automation 默认录制/回放成为 verdict
- pre-flight check:
  - 读取 master spec motion redline
  - 读取 package dependencies
  - 确认 no new UI lib
  - 列 surface classes
- self-verification:
  - surface matrix complete
  - motion no-goals present
  - no dependency addition
  - V-PASS human retained
  - candidate label intact
### D-BA-005 — browser_automation authority 升级 PR + commander prompt
- id: `D-BA-005`
- status: candidate
- parent_lane: `browser_automation`
- dependency: D-BA-001~004 + Hermes V-PASS
- TL;DR: 只有明确 use case 与 human verdict invariant 齐备后, 起草 minimal automation PR skeleton。
- 输入包:
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/00-START-HERE.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/decision-log.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/memory/INDEX.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/locked-principles.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/contracts-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/apps/capture-station/package.json
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/visual/h5-capture-station/wave4-final/wave4-visual-touchpoint-roster-and-localhost-plan-candidate-2026-05-05.md
- 输出 deliverable:
  - `docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/dispatch-packets/D-BA-005-authority-upgrade-skeleton-candidate.md`
- 验收标准:
  - prompt 含 use case ID
  - no runtime_tools / no migration / no vault write
  - visual terminal verdict retained
- 反模式 REGENERATE:
  - REGENERATE: 无 use case 也启动
  - REGENERATE: 混入 runtime scraping
  - REGENERATE: 省略 human V-PASS
- pre-flight check:
  - 刷新 Check 1-6
  - 确认 use case doc exists
  - 确认 Hermes verdict
  - 确认 Active slot
- self-verification:
  - use case linked
  - scope minimal
  - side effects bounded
  - remaining Hold listed
  - candidate label intact
### D-BA-006 — lane closeout packet
- id: `D-BA-006`
- status: candidate
- parent_lane: `browser_automation`
- dependency: D-BA-005 后续
- TL;DR: 汇总 automation 作为辅助 evidence 的范围与限制, 给 Authority writer closeout 使用。
- 输入包:
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/00-START-HERE.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/decision-log.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/memory/INDEX.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/locked-principles.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/contracts-index.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/apps/capture-station/package.json
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/visual/h5-capture-station/wave4-final/wave4-visual-touchpoint-roster-and-localhost-plan-candidate-2026-05-05.md
- 输出 deliverable:
  - `docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/dispatch-packets/D-BA-006-closeout-packet-candidate.md`
- 验收标准:
  - closeout 明确 human verdict status
  - automation evidence 不泛化
  - remaining Hold lanes 清楚
- 反模式 REGENERATE:
  - REGENERATE: closeout 称 automation 替代人工
  - REGENERATE: 漏写 use case ID
  - REGENERATE: 把 screenshot packet 当 product UI approval
- pre-flight check:
  - 读取 final PR metadata
  - 读取 screenshot evidence URL if any
  - 复核 current state
  - 确认 no authority write in packet
- self-verification:
  - evidence/limitation table present
  - human verdict line present
  - no terminal visual claim
  - remaining Hold present
  - self-flag present
## §5 Codex commander prompt skeleton
### §5.1 §0 Codex 角色与上下文
Codex 是 OpenAI Long Runner Coder, 接收 CC1 填实后的 commander prompt, 在单一明确 dispatch 下执行。本文只给 skeleton, 不直接启动实施。Codex 起手必须读本文件 §0.5 的刷新结果, 然后用 GitHub API / raw URL 复核 main HEAD、current/task state、lane 边界源。
### §5.2 §0.5 Prerequisite Check
- Check A: 读取 main commit API, 记录 SHA + message。
- Check B: 读取 current/task-index, 确认 Active product lane 与 Authority writer 空位。
- Check C: 读取 lane 边界源, 确认本 lane 仍处 Hold 且未被其它 lane 间接改变。
- Check D: 读取 memory INDEX, 特别是 runtime/migration/candidate/overflow 相关 instinct。
- Check E: 读取 PR #243/#244/#245/#246/#247/#248 metadata, 引 PR # 时一律标历史参考。
### §5.3 §1 Mission
在具体 use case 与 human V-PASS invariant 齐备后, 以最小自动化 scope 采集 e2e smoke / screenshot evidence, 严格不替代人工视觉终判。
### §5.4 §2 Inputs
- master spec §16 browser automation row
- current/task-index/decision-log raw URLs
- capture-station package.json
- visual roster candidate
- memory F-STRONG-VISUAL-FIRST-CLASS
### §5.5 §3 Hard Boundaries
- 无具体 use case 不启动
- automation evidence 不等于 V-PASS
- 不触碰 runtime_tools; no scraping/download
- 不触碰 vault write / migration / full signal workbench
- no browser profile / no credential material
### §5.6 §4 N-phase 执行计划 + dispatch 列表
- Phase 1: use-case intake lock
- Phase 2: automation boundary spec
- Phase 3: 5 Gate human V-PASS lock
- Phase 4: motion boundary guard
- Phase 5: bounded evidence packet closeout
### §5.7 §5 amend_and_proceed pattern
- silent_flexibility 触发条件: schema 字段需要新增、红线措辞产生歧义、验证证据不足、跨 lane 依赖发生 drift。
- 触发后动作: 不扩大范围; 先写 amend note; 再让 CC0/CC1 对 commander prompt 做最小修订; 仍保持本 lane 不替代其他 lane。
- 单 PR 内最多两轮 amend; 第三轮必须 stop-the-line, 由磊哥拍板是否拆 PR。
### §5.8 §6 Lane closeout 验收
- closeout packet 必须把「做了什么 / 没做什么 / 证据是什么 / 哪些 lane 仍 Hold」写清。
- Authority writer 才能执行最终 writeback; 本 skeleton 不把 authority 文件列为本文件输出 deliverable。
- closeout 后仍需 Hermes 或 CC1 复核, 防止 candidate roadmap 被误引为 current authority。
## §6 Hermes audit prompt skeleton
### §6.1 Hermes 独立外审角色
Hermes 是 3rd party independent auditor, 只对本 lane 的 spec PR、commander prompt、dispatch pack 给外审 verdict。Hermes 输出不替代磊哥显式授权, 也不把 candidate 文档提升为 authority。
### §6.2 audit scope
- 本 lane authority-upgrade spec PR 是否把 §16.1 红线、§16.2 升级路径、§14.2 pre-flight、§16.3 风险矩阵贯彻到位。
- CC1 commander prompt 是否有明确 lane scope、allowed paths、forbidden paths、validation、closeout。
- Dispatch pack 是否能在 24h 内被 Codex/CC1 消费, 且不隐性打开其它 overflow lane。
### §6.3 4 级 verdict 标准
| Verdict | 含义 | 后续动作 |
|---|---|---|
| V-PASS-CLEAR | 无 blocking / high issue | 可进入磊哥显式授权候选 |
| V-PASS-CONCERN | 有 medium 风险, 不阻塞 | 修 wording / validation 后可继续 |
| V-PARTIAL | 有 high 风险点 | land 前必须修订, 不得静默继续 |
| V-REJECT | critical 风险或边界破坏 | 阻塞 Codex 启动, 回到 spec rewrite |
### §6.4 audit dimensions
- use case specificity and 24h consumer clarity
- V-PASS human visual terminal invariant
- 5 Gate human review not substituted
- Motion 渗透 redline
- e2e smoke vs visual acceptance boundary
- credential/browser profile safety
- package/dependency scope containment
### §6.5 audit output schema
| Dimension | Finding | Severity | Required revision | Evidence URL |
|---|---|---|---|---|
| `<dimension>` | `<finding>` | `<C/H/M/L>` | `<revision>` | `<raw URL / PR URL>` |
Final verdict: `<V-PASS-CLEAR | V-PASS-CONCERN | V-PARTIAL | V-REJECT>`
Hermes signoff: `<name / timestamp / caveat>`
## §7 Lane-specific 反模式

1. REGENERATE: 无 use case 仍起草 Playwright/Selenium 实施。
2. REGENERATE: screenshot evidence 被写成 human V-PASS。
3. REGENERATE: CI pass 被写成 product UI terminal verdict。
4. REGENERATE: browser automation 顺手做 scraping/download。
5. REGENERATE: 引入 browser profile / credential state。
6. REGENERATE: motion 为了 automation 渗透 reading/wiki surface。
7. REGENERATE: 引整套 UI/animation dependency。
8. REGENERATE: output deliverable 没列 automation side effects 与 stop condition。


## §8 Self-flag

### §8.1 GPT Pro 不确定的取舍点

  - ⚠️ 当前没有明确 use case, 所以 Lane 3 最合理动作可能是继续 Hold。
  - ⚠️ 5 Gate 自动化辅助的边界需要战友审美偏好最终拍板。
  - ⚠️ 是否允许 screenshot packet 作为非 terminal evidence 进入 RAW/dispatch 存档, 需 CC0/CC1 细化。

### §8.2 GPT Pro 弱项

  - ⚠️ 未运行 browser automation, 也未检查所有 visual candidate surface。
  - ⚠️ 未读取完整 5 Gate rule 文件, 仅依据 START-HERE/master spec/memory 的公开锚点。
  - ⚠️ 没有确认未来 CI runner 是否支持 browser tooling。

### §8.3 待磊哥拍板取舍点

  - 🟡 Lane 3 是否暂缓, 等具体 use case 出现再写 spec PR。
  - 🟡 是否允许 Playwright 仅作为 CI smoke, 还是也允许本地截图 packet。
  - 🟡 human V-PASS 的记录格式是否要单独 contract。
  - 🟡 Motion guard 是否需要独立 PR。

### §8.4 Self-verification result

- 5 份 markdown 1-to-1 mapping 已生成; 本文件为 `browser_automation`。
- frontmatter 已含 status / authority / authority_state / created_by / parent_cluster / lane / prerequisite_check / disclaimer。
- 已包含 §0.5 + §1-§8 全段落。
- Dispatch 数量在 5-7 范围内, 每个 dispatch 含 standard schema。
- 未写实现模块代码、真 migration SQL、浏览器脚本或运行命令。
- 未把本 lane 写成 current authority, 未声明 lane 已完成解禁。
- 输出 deliverable 清单未把 authority files 作为本文件写入目标。
- 未引用被禁止的本地 home 路径, 未假设本地 shell 命令。
