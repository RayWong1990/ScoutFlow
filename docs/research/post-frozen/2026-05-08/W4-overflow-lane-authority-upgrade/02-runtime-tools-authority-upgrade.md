---
title: Runtime Tools Authority-Upgrade Spec Candidate
status: candidate
authority: not-authority
authority_state: not-execution-approved
created_by: gpt-pro
parent_cluster: W4
lane: runtime_tools
prerequisite_check: refreshed_2026-05-08T09:24:02Z
master_spec_anchor: §16.1 (硬红线) + §16.2 (升级路径) + §14.2 (pre-flight) + §16.3 (风险矩阵)
disclaimer: |
  本文是 candidate authority-upgrade roadmap, 不是 lane 完成权限升级的证据.
  Lane 解禁需要走完整 §3 pre-flight 5 步 + Hermes 外审 V-PASS + 磊哥显式授权 + spec PR merge.
  本文内的 PR # / file path / SHA 标 "(撰写时刻历史参考, 真值以 §0.5 Check 为准)".
---

# Runtime Tools Authority-Upgrade Spec Candidate

> 本文产出的是 runtime_tools 的 candidate spec PR 输入，不是 runtime unlock 证据。它不运行 BBDown / yt-dlp / ffmpeg / ASR, 也不把 bounded evidence 解释成 live runtime gate。

## §0.5 Prerequisite Check

> refreshed_at: `2026-05-08T09:24:02Z`. 本段是本文件的真态读回锚, 任一后续 agent 接收本文时必须再次刷新, 不得把本文数值当永久 authority。

| Check | 刷新真态 | Drift / 处理 |
|---|---|---|
| 1 — main HEAD | `45e88d45342ba6f6036e68695ca56d09deaaf06d`; message=`Merge pull request #257 from RayWong1990/codex/w4-b-step0-convergence` | 与提示词里 `c802de4` / `4792b0f` 叙述存在 chronological drift; 本文引用 main HEAD 时以 Check 1 为准。PR #257 及更早 PR #245/#247/#248 均标注「撰写时刻历史参考, 真值以 §0.5 Check 为准」。 |
| 2 — current.md | Active product lane `0/3`; Authority writer `0/1`; state=`WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`; 5 overflow lane Hold 仍列明。 | current.md body 仍写 `c802de4` 作为 main anchor，且 live main 已前进到 `45e88d4`; authority-body drift 存在，但本 lane 不负责修 authority trio。 |
| 3 — task-index.md | Active `0/3`; Review `0`; Authority writer `0/1`; Phase=`Phase 1A — WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`。 | 与提示词一致。 |
| 4 — decision-log.md | tail 可见最新 authority entry 仍聚焦 W2C closeout；未覆盖 PR #257 merge state。 | 本 lane 记录 live drift, 不代写 authority repair；若后续引用 decision-log 最新 merge 状态, 需再做 authority refresh。 |
| 5 — memory INDEX | `batch_count: 17`; Lessons 7 / Feedback 5 / Patterns 5; 重点含 L-RUNTIME-APPROVAL-DRIFT, L-MIGRATION-DRIFT, L-OVEROBJECTIFICATION, P-PROOF-PAIR-CANARY, P-OVERFLOW-NOT-BLOCKER。 | 与提示词一致。 |
| 6 — bridge config | vault true-write flag 在未配置 vault root 分支与已配置 vault root 分支均保持 false。 | 与提示词一致; 本文不改变该 invariant。 |
| B-lane sanity | `bridge/router.py` 当前暴露 bridge health / vault config / vault preview / vault commit dry-run 4 个 route decorator; migrations baseline 仅 001/002; capture-station package 未见 Playwright / Selenium dependency。 | 提示词里「5 routes」按历史参考处理, 真值以 router 文件为准。 |

**读回证据 URL 包**: main commit API, `docs/current.md`, `docs/task-index.md`, `docs/decision-log.md`, `docs/memory/INDEX.md`, `services/api/scoutflow_api/bridge/config.py`, `services/api/scoutflow_api/bridge/router.py`, `services/api/migrations/001_phase1a_capture_creation.sql`, `services/api/migrations/002_phase1a_jobs_receipt.sql`, `apps/capture-station/package.json`。

## §1 Lane 当前态

### §1.1 Lane forbidden 边界引用

- current.md 当前禁止段列明: BBDown live / yt-dlp / ffmpeg / ASR / browser automation blocked。
- master spec §16.1 将 runtime_tools 放入 5 overflow lane Hold, §16.2 给出合法升级路径, 不是直接禁止未来升级。
- master spec §4.3 要求 vendor diversification; BBDown 不能成为唯一长期 adapter。
- master spec §5.1 / §9.8 讨论 ASR 与 Apple Silicon 优化, 但当前仍是候选路线图层。
- current.md 还锁定 subprocess.run 不得出现在 orchestrator, runtime lane 必须把外部 process 边界写清。

### §1.2 Lane 现状真态

| 维度 | 真态 | 本 roadmap 处理 |
|---|---|---|
| BBDown live | blocked | 只写 vendor adapter / legal risk / fallback roadmap |
| yt-dlp / ffmpeg | blocked | 只写 candidate contract 与 benchmark plan |
| ASR runtime | blocked | 只写模型矩阵与 benchmark schema |
| browser automation | blocked | lane 2 不触碰 lane 3 |
| workers/packages | current 禁止创建或修改 | 本文不输出 worker/package implementation |
| package.json | React/Vite/Vitest stack; no Playwright/Selenium | 不引浏览器自动化依赖 |

### §1.3 风险矩阵

| 风险 | Severity | 具体失败模式 | 必需缓解 |
|---|---|---|---|
| vendor legal | critical | BBDown cease-and-desist 信号导致主 adapter 风险上升 | yt-dlp / alternate source fallback + legal risk register |
| runtime cost | high | ASR/ffmpeg 长视频占用 CPU/GPU/费用, 阻塞本地工作站 | cost ledger + sample budget + model routing |
| Apple Silicon 兼容 | high | x86 binary / Rosetta fallback 导致性能与稳定性不可控 | native ARM64 / Metal first + fallback 明示 |
| ASR/rewrite quality | high | 单模型误转写被 downstream rewrite/vault 放大 | A/B benchmark + human sample review + confidence gate |
| subprocess.run tripwire | critical | orchestrator 直接调用外部工具, 破坏薄 API 边界 | process sandbox spec + redaction + tripwire |
| credential leakage | critical | auth sidecar / cookie / stdout 进入 logs or docs | credential material never evidence + redaction policy |

### §1.4 实施前置条件

1. ASR 选型矩阵与 benchmark schema 先于工具安装/运行。
2. Vendor adapter contract 必须支持 fallback, 不把 BBDown 作为 single point of failure。
3. Apple Silicon acceptance 要定义 native ARM64 与 fallback policy。
4. 外部 process 只能在受控边界中描述, orchestrator 仍不可含 subprocess.run。
5. runtime evidence 不得自动推进 vault write、migration、browser automation、full signal workbench。

### §1.5 24h 内 actionable consumer

- GPT Pro/CC1 可在 24h 内把 D-RT-001/002 变成 spec PR 草稿。
- Hermes 可立即审 vendor legal + benchmark adequacy。
- Codex 只有在 commander prompt 填实并经显式授权后, 才能消费 D-RT-005。

### §1.6 本轮 spec 锁定范围

本轮只把 lane 2 压到可执行 spec PR 级, 不推进 runtime approval。本轮 spec 必须落稳以下 5 个 surface:

1. vendor / fallback contract
2. ASR benchmark protocol
3. subprocess boundary + repo-external temp-dir + redaction + `safe_stdout_excerpt`
4. minimal rewrite plugin registry
5. bounded canary closeout packet

任何超出这 5 个 surface 的结论, 若仓库内无直接证据, 一律降级为 TODO / hypothesis。

### §1.7 preferred first-pass hypotheses（非批准）

下表只定义 lane 2 本轮 candidate spec 的首轮假设写法, 不改 current authority, 不推翻 shoulders 历史证据分层:

| Surface | preferred first-pass hypothesis | 当前证据分层 | 必须保留的 gate |
|---|---|---|---|
| source adapter | `yt-dlp primary / BBDown fallback` | shoulders 里 `yt-dlp` 仍是 comparator / reference_only 证据, repo 内现成 BBDown contract / preflight / parser 只证明可写 contract, 不证明 live route | legal refresh receipt + bounded canary receipt + explicit runtime approval |
| ASR | `Whisper.cpp Metal primary / FunASR fallback` | U14 `A01` / `H02` 只提供 candidate recipe 与 benchmark contract, 未提供本机 benchmark 实测 | benchmark receipt + quality review + cost ledger + explicit runtime approval |

解释:

- `yt-dlp primary / BBDown fallback` 是本轮 spec 用来防 single-source failure 的 preferred first-pass hypothesis, 不是对当前 shoulders/reference_only 分层的 authority rewrite。
- `Whisper.cpp Metal primary / FunASR fallback` 是本轮 spec 用来组织 benchmark 与 fallback ladder 的 preferred first-pass hypothesis, 不是默认批准路线。
- 若 live legal refresh 或 benchmark receipt 与本假设冲突, 以后者为准, 立即回退到 `candidate / hypothesis`。

### §1.8 最小 spec contract 读回

| Contract surface | 本轮必须写清 | 证据锚点 |
|---|---|---|
| vendor / fallback | priority、fallback trigger、single-source stop-line、legal refresh | `docs/specs/bbdown-adapter-contract-draft.md`, `docs/specs/platform-adapter-risk-contract.md`, shoulders/U2 |
| ASR benchmark | fixture manifest、metric schema、model/package/hash、人工复核字段 | U14 `H02`, `A01` |
| process sandbox | command array、repo-external temp-dir、redaction、`safe_stdout_excerpt`、no raw stdout/stderr receipt | `bbdown_info_adapter.py`, `bbdown_info_parser.py`, `dry_run_metadata.py` |
| rewrite registry | 仅保留最小 style registry / output schema / fallback note, 不扩成 rewrite implementation | master spec §6.2-§6.4 |
| canary closeout | bounded sub-lane、benchmark receipt、cost ledger、legal refresh、remaining Hold | U2 fail modes, U11 truthful stdout contract |

### §1.9 Transcript handoff 最小字段

本 subsection 只定义 lane 2 向 rewrite / trust-trace / downstream review 交接时的最小 transcript handoff shape。它是 `candidate handoff`, 不是 runtime approval，也不是 transcript 质量已通过的声明。

| Field | 必须性 | 用途 |
|---|---|---|
| `transcript_text` | required | 下游 rewrite / review 的文本主体；不得替代原始音频证据 |
| `language_detected` | required | 标记主语种或 mixed-language 结果，支撑模型/route 回放 |
| `duration_seconds` | required | 对齐音频时长、benchmark 和 closeout 样本说明 |
| `asr_engine` | required | 记录引擎族，如 `whisper.cpp-metal` / `funasr`；用于 fallback 与 drift 定位 |
| `asr_model_sha256` | required | 记录模型身份，而不是只写模型名 |
| `extraction_seed` | required | 记录音频提取/切分入口的稳定种子或 deterministic run id |
| `trust_trace_id` | required | 让 transcript handoff 能被 trust-trace / receipt 链路追溯 |
| `source_url` | required | 保留来源 URL，避免 transcript 脱离 source context |
| `capture_date` | required | 标记采集日期，避免 later replay 把旧 transcript 当新样本 |

规则:

- 这 9 项是最小 handoff surface，不等于完整 transcript schema。
- handoff packet 可以附带额外字段，但不得省略这 9 项。
- 若其中任一字段缺失，本 lane 只能写 `handoff_incomplete` / `candidate`, 不得把 transcript 交接描述成 ready-for-rewrite。
- `transcript_text` 可以进入 handoff；raw stdout/stderr、cookie、token、auth sidecar、未脱敏 URL 参数不得进入 handoff。

## §2 升级路径

### §2.1 推荐路径

推荐路径: hypothesis freeze + vendor diversification + ASR benchmark + Apple Silicon acceptance + sandbox spec → Hermes → explicit user gate → bounded runtime canary。

1. 先冻结 preferred first-pass hypotheses, 但同时写明它们只是 hypothesis, 不得写成已批准默认路线。
2. 再做模型/adapter 选择与 legal refresh / benchmark receipt 模板, 避免先接工具再补安全边界。
3. 再做 subprocess sandbox, 明确 repo-external temp-dir、stdout/stderr redaction、`safe_stdout_excerpt` 与 failure classification。
4. 然后用小样本 canary 验证: source metadata, audio extraction, ASR, cost, redaction。
5. closeout 时只说 canary evidence, 不泛化成全 runtime 体系完成。

### §2.2 路径理由

runtime_tools 是成本、legal、安全、质量风险叠加的 lane。它不是单个工具开关, 而是 source adapter + media processing + ASR + cost ledger + process boundary 的组合。先跑工具会制造无法审计的本地 side effect; 先建 schema 与 benchmark 能降低漂移。

### §2.3 不推荐路径 + 反模式

- 不推荐「直接跑 BBDown live」: vendor/legal/credential/evidence 都未闭环。
- 不推荐「只接 yt-dlp 就宣称 diversification 完成」: fallback strategy 还要覆盖 source capability 与 failure mode。
- 不推荐「用单条 ASR 样本选型」: 中文/英文/长短音频差异很大。
- 不推荐「让 browser automation 跟 runtime_tools 一起走」: Playwright/Selenium 属于 lane 3。

### §2.4 候选时间窗

- 撰写时刻历史参考: master spec §17 把 runtime_tools 放入中期 lane, 通常应先 spec/audit, 再 canary。
- 24h 内最可行动: D-RT-001 ASR matrix + D-RT-002 vendor adapter spec。
- 1 周内可行动: D-RT-004 sandbox spec + Hermes review。

## §3 Pre-flight 5 步

### §3.1 Step 1: task-index 注册

- 注册 T-LANE-RT-XXX, 占 Active product lane 1/3。
- scope 只含 runtime_tools spec / benchmark / sandbox; explicitly not browser automation, not migration, not vault true write。
- validation 必含 benchmark evidence 与 redaction evidence 字段。

### §3.2 Step 2: decision-log D-XXX 草稿

- 决策草稿写明 runtime_tools 进入 candidate upgrade path, 不构成 runtime execution gate。
- 必列 vendor diversification 与 subprocess sandbox 两个强制前置。
- 必列 cost ledger 与 Apple Silicon acceptance。

### §3.3 Step 3: Hermes pre-flight 外审 prompt

- Hermes 审 vendor legal、benchmark design、Apple Silicon、sandbox、credential redaction。
- Verdict V-PARTIAL 以上风险必须修订后才能进入 Codex。
- Hermes 不替代磊哥显式授权。

### §3.4 Step 4: CC1 commander prompt v1 草稿

- prompt 必须分 spec / canary / closeout phases。
- prompt 不得包含本地运行命令; 由 Codex 后续在授权上下文中设计可验证步骤。
- prompt 必须写 no-goals: no browser automation, no migration, no true vault write。

### §3.5 Step 5: 磊哥显式授权 + paste Codex

- 授权范围必须指明工具、样本、side effect、evidence path、stop condition。
- 未授权不得运行 live media/download/ASR。
- closeout 必须把 canary evidence 与 broader runtime readiness 分开。

## §4 Dispatch templates
### D-RT-001 — ASR 选型矩阵 spec PR
- id: `D-RT-001`
- status: candidate
- parent_lane: `runtime_tools`
- dependency: 无; 先做 spec/audit
- TL;DR: 建立以 `Whisper.cpp Metal primary / FunASR fallback` 为 preferred first-pass hypothesis 的 benchmark schema; 其他模型只作 comparator 候选, 不运行 live runtime。
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
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/bbdown-adapter-contract-draft.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/platform-adapter-risk-contract.md
- 输出 deliverable:
  - `docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/dispatch-packets/D-RT-001-asr-matrix-candidate.md`
- 验收标准:
  - 模型矩阵含 quality、rtf、timestamp drift、成本、Apple Silicon、privacy、fallback trigger
  - benchmark evidence 字段定义清楚, 且不填伪实测值
  - `Whisper.cpp Metal primary / FunASR fallback` 只以 hypothesis 口径出现
  - 不写真实执行命令
- 反模式 REGENERATE:
  - REGENERATE: 把 benchmark table 写成已实测
  - REGENERATE: 只选 BBDown/Whisper 单 vendor
  - REGENERATE: 忽略 cost ledger
- pre-flight check:
  - 读取 master spec §5.1/§9.8
  - 读取 current runtime blocked
  - 读取 U14 `H02` / `A01`
  - 读取 memory L-RUNTIME-APPROVAL-DRIFT
  - 确认 no workers/package creation
- self-verification:
  - primary/fallback/comparator 三层角色分明
  - benchmark placeholders 标 TODO
  - cost dimension present
  - Apple Silicon dimension present
  - candidate label intact
### D-RT-002 — yt-dlp / BBDown 多元化 adapter spec
- id: `D-RT-002`
- status: candidate
- parent_lane: `runtime_tools`
- dependency: D-RT-001 可并行
- TL;DR: 把 `yt-dlp primary / BBDown fallback` 写成 preferred first-pass hypothesis, 同时把 legal refresh、capability matrix、fallback trigger 写清; 不把任一路线写成当前批准默认。
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
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/bbdown-adapter-contract-draft.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/platform-adapter-risk-contract.md
- 输出 deliverable:
  - `docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/dispatch-packets/D-RT-002-vendor-adapter-candidate.md`
- 验收标准:
  - capability matrix 覆盖 B站/YouTube/抖音/XHS/Research
  - `yt-dlp primary / BBDown fallback` 只以 hypothesis 写法出现
  - BBDown cease-and-desist 风险与 `yt-dlp` legal refresh 都以 candidate risk / refresh-required 写法出现
  - fallback strategy 不绕过 user gate
- 反模式 REGENERATE:
  - REGENERATE: 声明 BBDown live 可跑
  - REGENERATE: 把 external legal fact 写成 authority policy
  - REGENERATE: fallback 触发无 evidence
- pre-flight check:
  - 读取 master spec §4.3
  - 读取 platform adapter risk contract
  - 读取 shoulders `yt-dlp` comparator / reference_only 历史口径
  - 读取 memory vendor diversification 相关条目
  - 复核 current blocked
- self-verification:
  - vendor risk labels present
  - fallback condition present
  - legal refresh receipt required
  - no live execution claim
  - no credential material
  - Hermes legal dimension present
### D-RT-003 — Apple Silicon Metal optimization spec
- id: `D-RT-003`
- status: candidate
- parent_lane: `runtime_tools`
- dependency: D-RT-001 matrix draft
- TL;DR: 围绕 native ARM64、Metal、VideoToolbox/CoreML/mlx 路线定义 performance acceptance, 但不安装/运行工具。
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
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/bbdown-adapter-contract-draft.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/platform-adapter-risk-contract.md
- 输出 deliverable:
  - `docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/dispatch-packets/D-RT-003-apple-silicon-candidate.md`
- 验收标准:
  - native ARM64 与 fallback 明确
  - performance counters 定义
  - Rosetta 2 fallback 不默认
- 反模式 REGENERATE:
  - REGENERATE: 忽略 Apple Silicon
  - REGENERATE: 把优化 spec 写成已跑 benchmark
  - REGENERATE: 引入不可审计 binary
- pre-flight check:
  - 读取 master spec U14/§9.8 anchor
  - 确认 runtime lane still Hold
  - 读取 package/dependency truth
  - 列出 benchmark TODO
- self-verification:
  - hardware assumptions 标 TODO
  - no local command
  - no install instruction
  - cost/perf tradeoff present
  - candidate label present
### D-RT-004 — subprocess.run sandbox 边界 spec
- id: `D-RT-004`
- status: candidate
- parent_lane: `runtime_tools`
- dependency: D-RT-002/003 完成
- TL;DR: 明确 orchestrator 不含 subprocess.run, 仅受控 worker/adapter boundary 可描述外部 process, 并有 tripwire。
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
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/bbdown-adapter-contract-draft.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/platform-adapter-risk-contract.md
- 输出 deliverable:
  - `docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/dispatch-packets/D-RT-004-subprocess-sandbox-candidate.md`
- 验收标准:
  - orchestrator / worker / adapter 边界清楚
  - tripwire test intent 明确
  - repo-external temp-dir + command-array rule 明确
  - `safe_stdout_excerpt` / `safe_stderr_excerpt` rule 明确
  - raw stdout/stderr 不进入 tracked evidence
- 反模式 REGENERATE:
  - REGENERATE: 在 orchestrator 放外部命令
  - REGENERATE: raw stdout/stderr 进 tracked evidence
  - REGENERATE: 省略 failure classification
- pre-flight check:
  - 读取 current tripwire 条款
  - 读取 contracts-index platform/security
  - 读取 memory L-RUNTIME-APPROVAL-DRIFT
  - 确认 no workers path creation unless future authorized
- self-verification:
  - boundary diagram text-only
  - redaction present
  - failure states present
  - temp-dir outside repo
  - command shape only, no live execution claim
  - no runtime claim
### D-RT-005 — runtime_tools authority 升级 PR + commander prompt
- id: `D-RT-005`
- status: candidate
- parent_lane: `runtime_tools`
- dependency: D-RT-001~004 + Hermes V-PASS + explicit gate
- TL;DR: 把 ASR/vendor/Apple Silicon/sandbox 四个 contract 合成 lane upgrade PR 与 Codex skeleton。
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
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/bbdown-adapter-contract-draft.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/platform-adapter-risk-contract.md
- 输出 deliverable:
  - `docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/dispatch-packets/D-RT-005-authority-upgrade-skeleton-candidate.md`
- 验收标准:
  - commander prompt 分阶段
  - no browser automation / no migration / no vault true write
  - benchmark evidence 是 gate
  - minimal rewrite plugin registry 已定义 style / output schema / fallback note, 但不进入 rewrite implementation
  - bounded canary 只覆盖一个 sub-lane 一次
- 反模式 REGENERATE:
  - REGENERATE: 合并打开 browser automation
  - REGENERATE: 把 ASR runtime 写成已授权
  - REGENERATE: 省略 cost budget
- pre-flight check:
  - 读取 Check 1-6
  - 确认 Active slot
  - 确认 Hermes verdict
  - 复核 lane 2-only scope
- self-verification:
  - scope lane-only
  - benchmark required
  - cost ledger required
  - rewrite registry minimal-only
  - closeout required
  - candidate label intact
### D-RT-006 — lane closeout + benchmark evidence packet
- id: `D-RT-006`
- status: candidate
- parent_lane: `runtime_tools`
- dependency: D-RT-005 后续
- TL;DR: 定义 closeout evidence packet, 把 vendor、ASR、Apple Silicon、sandbox、cost 证据汇总给 Authority writer。
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
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/bbdown-adapter-contract-draft.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/platform-adapter-risk-contract.md
- 输出 deliverable:
  - `docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/dispatch-packets/D-RT-006-closeout-benchmark-candidate.md`
- 验收标准:
  - benchmark evidence 不混同 claim
  - remaining Hold lanes 清楚
  - cost budget 记录
  - closeout packet 包含 legal refresh、temp-dir manifest、redaction summary、rewrite registry snapshot
  - transcript handoff snapshot 显式包含 9 个最小字段
  - 只 closeout 一个 bounded canary, 不泛化到 whole lane approved
- 反模式 REGENERATE:
  - REGENERATE: 把单样本 benchmark 泛化
  - REGENERATE: closeout 声称 full runtime done
  - REGENERATE: 漏写 vendor fallback
- pre-flight check:
  - 读取 final PR metadata
  - 读取 CI/audit evidence URL
  - 复核 current state
  - 确认 no authority write in packet
- self-verification:
  - evidence table complete
  - limitations present
  - remaining Hold present
  - Hermes signoff linked
  - transcript handoff 9 字段 present
  - canary scope bounded
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
在 runtime_tools 通过 spec/audit/gate 后, 按本文件定义的 preferred first-pass hypotheses, 以 bounded canary 方式验证 vendor adapter、media extraction、ASR、redaction、cost ledger、minimal rewrite registry 与 process sandbox。
### §5.4 §2 Inputs
- master spec §4.3 / §5.1 / §9.8 / §16
- current/task-index/decision-log raw URLs
- contracts-index Platform/Security groups
- memory INDEX L-RUNTIME-APPROVAL-DRIFT
- capture-station package truth for no browser automation dependency
### §5.5 §3 Hard Boundaries
- 不触碰 browser_automation lane; no Playwright/Selenium
- 不触碰 true_vault_write; no vault true commit
- 不触碰 dbvnext_migration; no migration script
- 不创建未授权 worker/package surface
- credential material never evidence; raw stdout/stderr 必须 redacted
### §5.6 §4 N-phase 执行计划 + dispatch 列表
- Phase 1: hypothesis freeze + vendor/ASR matrix contract
- Phase 2: Apple Silicon benchmark acceptance + legal refresh receipt
- Phase 3: subprocess sandbox boundary + temp-dir/redaction rules
- Phase 4: bounded runtime canary evidence
- Phase 5: closeout with limitations + remaining Hold
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
- vendor legal risk and fallback adequacy
- ASR benchmark evidence design
- Apple Silicon native ARM64 / Metal compatibility
- subprocess.run tripwire and process sandbox
- Cost / Token Budget discipline
- credential/redaction safety
- canary scope not generalized into broad runtime claim
### §6.5 audit output schema
| Dimension | Finding | Severity | Required revision | Evidence URL |
|---|---|---|---|---|
| `<dimension>` | `<finding>` | `<C/H/M/L>` | `<revision>` | `<raw URL / PR URL>` |
Final verdict: `<V-PASS-CLEAR | V-PASS-CONCERN | V-PARTIAL | V-REJECT>`
Hermes signoff: `<name / timestamp / caveat>`
## §7 Lane-specific 反模式

1. REGENERATE: 把 BBDown / yt-dlp / ffmpeg / ASR 写成当前可运行事实。
2. REGENERATE: 单 vendor 方案无 fallback, 或把 BBDown 当唯一长期路线。
3. REGENERATE: ASR benchmark 没有质量、速度、成本、Apple Silicon 四维。
4. REGENERATE: orchestrator 边界允许 subprocess.run。
5. REGENERATE: raw stdout/stderr 或 credential material 进入 tracked evidence。
6. REGENERATE: runtime_tools closeout 顺手打开 browser automation。
7. REGENERATE: 把 bounded canary 当 full pipeline production readiness。
8. REGENERATE: 忽略 cost ledger 或长视频资源开销。


## §8 Self-flag

### §8.1 GPT Pro 不确定的取舍点

  - ⚠️ ASR matrix 中 FunASR / Paraformer-large 的具体版本与 benchmark corpus 需 CC1/Codex 后续确认。
  - ⚠️ BBDown cease-and-desist 信号属于历史风险锚, 本文未做实时法律事实外查。
  - ⚠️ Apple Silicon hardware profile 未知, 需在 Codex canary 前由 owner 环境事实填实。

### §8.2 GPT Pro 弱项

  - ⚠️ 未运行任何 tool benchmark, 所有 benchmark 字段为 roadmap schema。
  - ⚠️ decision-log latest tail 需 CC0/CC1 接收时复核 D-017+。
  - ⚠️ 未穷尽 XHS / Research / PDF / Image source adapters, 仅覆盖 lane 2 核心。

### §8.3 待磊哥拍板取舍点

  - 🟡 runtime_tools 首轮 canary 选 BBDown 还是 yt-dlp。
  - 🟡 ASR first model 选 Whisper.cpp Metal 还是中文专精模型。
  - 🟡 是否要求 cost ledger 先于任何 canary。
  - 🟡 subprocess sandbox 是否必须先落单独 spec PR。

### §8.4 Self-verification result

- 5 份 markdown 1-to-1 mapping 已生成; 本文件为 `runtime_tools`。
- frontmatter 已含 status / authority / authority_state / created_by / parent_cluster / lane / prerequisite_check / disclaimer。
- 已包含 §0.5 + §1-§8 全段落。
- Dispatch 数量在 5-7 范围内, 每个 dispatch 含 standard schema。
- 未写实现模块代码、真 migration SQL、浏览器脚本或运行命令。
- 未把本 lane 写成 current authority, 未声明 lane 已完成解禁。
- 输出 deliverable 清单未把 authority files 作为本文件写入目标。
- 未引用被禁止的本地 home 路径, 未假设本地 shell 命令。
