---
title: ScoutFlow 批量化转写平台 Master Roadmap — 2026-05-08
status: candidate north-star
authority: not-authority
created_at: 2026-05-08
paired_with: docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md
purpose: 批量化转写平台的执行总纲; 衔接 P3 vertical slice / PF-V visual productization / runtime_tools / true_vault_write / batch friction / DB architecture
basis:
  - docs/current.md
  - docs/00-START-HERE.md
  - docs/PRD-v2-2026-05-04.md
  - docs/SRD-v2-2026-05-04.md
  - docs/PRD-amendments/prd-v2.1-strong-visual-h5-para-pr-factory-candidate-2026-05-04.md
  - docs/SRD-amendments/h5-bridge-para-vault-srd-v3-candidate-2026-05-04.md
  - docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md
  - docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/01-true-vault-write-authority-upgrade.md
  - docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/02-runtime-tools-authority-upgrade.md
  - docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/04-dbvnext-migration-authority-upgrade.md
  - docs/research/post-frozen/2026-05-08/W4-overflow-lane-authority-upgrade/05-full-signal-workbench-authority-upgrade.md
  - /Users/wanglei/Downloads/research0508/scoutflow-g1-next-historical-reuse-atlas-deep/**
  - /Users/wanglei/Downloads/research0508/scoutflow-g2-next-p3-single-item-closure-deep/**
  - /Users/wanglei/Downloads/research0508/scoutflow-g3-next-w5h-min-source-matrix-deep/**
  - /Users/wanglei/Downloads/research0508/scoutflow-g4-next-small-batch-canary-ops-deep/**
  - /Users/wanglei/Downloads/scoutflow-g5-next-wave-planning-synthesis.zip
disclaimer: |
  本文件是 candidate north-star 执行总纲，不是 current authority，不是 runtime approval，
  不是 migration approval，不是 browser automation approval，不是 true_vault_write approval。
  PR / SHA / main HEAD 仅作历史 receipts，不作本路线图主锚。主锚是 authority state、
  landed capability、5 overflow Hold、以及每轮 preflight 的 live readback。
---

# ScoutFlow 批量化转写平台 Master Roadmap — 2026-05-08

> 角色说明:
>
> - `master spec` 回答: ScoutFlow 长期北极星、11 wave、系统 inventory、长期升级路径是什么。
> - `本 roadmap` 回答: 在 2026-05-08 真态下，如何以最大马力、最高质量、最强视觉、尽快全功能、单人敏捷的方式，把“批量化转写平台”做出来。
> - 两者是配套关系，不互相替代。

## §0 当前起点

### §0.1 本轮采用的真态锚

本路线图不把 `main HEAD` 或某个 PR 号当主锚，而使用以下 4 个真态锚:

1. `docs/current.md` 当前 state = `WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`
2. `write_enabled=False` 仍为硬真相
3. 5 overflow lane Hold 仍全在:
   - `true_vault_write`
   - `runtime_tools`
   - `browser_automation`
   - `dbvnext_migration`
   - `full_signal_workbench`
4. 已 landed 能力已经足够支撑下一波:
   - `PF-V` 视觉资产 handoff
   - `PF-C4-01` 13 surface shell
   - `W2C` truthful runtime surfaces + 5 态状态机
   - `W1B` Trust Trace bounded lanes
   - `T-P1A-158` stale refresh / default-blocked vault write / START-HERE ref-aware freshness repair

### §0.2 保留不动的硬边界

以下硬边界保留，不因为追求速度而放松:

- `candidate != authority`
- `preview != write`
- `runtime != approved`
- `migration != implied`
- `proof before object`
- `no browser automation`
- `no scheduler / worker platform / DB queue in first wave`

## §1 这份路线图修正了什么

本路线图保留原有三点正确性:

1. 先用 live authority 真态开工，不从 stale checkout 或历史 prompt 开工。
2. 先做单条 proof，再做 batch，再决定是否解禁更重的 lane。
3. 接口要先收窄到可审计最小集，不能一上来把 source / ASR / rewrite / preview / write / batch 混成一团。

在此基础上，按 Opus 纠偏，做 6 个关键修正:

1. `3 URL` 只作为 `smoke batch`，不是最终 batch 验证。
2. 新增 `10 URL friction batch`，专门暴露真实批量摩擦。
3. 新增 `Lane D = PF-V visual productization`，不再让视觉只是 Lane A 的附属工作。
4. UI stack 选型提前为 candidate workstream，而不是默认永久锁死当前自绘方案。
5. `DB architecture decision` 提前，`DB migration implementation` 后置。
6. 首个 runtime canary 只战术性选择一条 source route 和一个 ASR engine，不把首次实现误写成长期战略 promotion。

## §2 Program 组织方式

### §2.1 Program-level parallelism

这份路线图按 `执行主线` 组织:

- `云端 GPT Pro`: 重型 spec、dispatch、选型 candidate、收敛长文本
- `本地 Codex 多窗口`: 实现、验证、PR、closeout
- `本地 Opus`: 高风险审计、视觉真值审计、过度 claim 审计
- `用户`: `V-PASS`、`true-write explicit gate`、`route choice gate`、`UI dependency gate`

### §2.2 与当前 active lane 上限的关系

当前 authority 仍写死:

- `Active product lane max = 3`
- `Authority writer max = 1`

因此本路线图区分两种并行:

1. `tracked code-bearing product lanes`
   - 任何时刻最多 3 条
2. `candidate / research / visual-productization / architecture workstreams`
   - 只要不写 authority、不进入 code-bearing product scope，就可以并行跑

换言之:

- Program-level 可以四轨并行
- 但 code-bearing writer 仍遵守 repo 现行上限

## §3 第一波总结构

### §3.1 四轨并行

第一波分成 4 条主线:

| Track | 名称 | 默认形态 | 目标 |
|---|---|---|---|
| A | P3 vertical slice | code-bearing product lane | 做出单条 operator flow + preview closure |
| B | runtime_tools single-route canary | code-bearing product lane | 做出单源单路单引擎 canary |
| C | true_vault_write gate + minimal flip | code-bearing product lane | 准备 same-payload minimal flip |
| D | PF-V visual productization | candidate first, code-bearing later if approved | 把 PF-V 资产产品化为最强视觉 operator workstation |

### §3.2 两个非 product candidate workstream

除了 A/B/C/D，再固定并行两份 candidate study:

1. `UI stack decision candidate`
2. `DB vNext architecture decision candidate`

这两份都不直接开 product lane，不写 schema implementation，不改 runtime truth。

## §4 Phase 0 — Live Truth Preflight

### §4.1 目标

压缩 Phase 0，只保留动态真值读取，不再把它扩成治理大 PR。

### §4.2 必读 receipts

每次新 commander run 起手必须读取:

- current authority phase
- active product lane count
- authority writer count
- 5 overflow Hold list
- `write_enabled`
- latest closeout receipts for lane 1/2/4 family
- `PR #261` merged truth
- W2C/W1B/T-P1A-158 landed capability

### §4.3 Phase 0 输出

只允许输出:

- one-page preflight receipt
- route/allowed-path confirmation
- lane slot plan
- no-go list

不允许输出:

- new governance reform
- runtime claims
- migration claims
- implicit unlock wording

## §5 Phase 1 — 四轨并行准备

### §5.1 Lane A — P3 preview vertical slice

目标: 先做出一个真实可感知的 single-item operator flow。

固定 scope:

- `1 URL`
- `manual_url`
- `metadata readback`
- `Trust Trace visible`
- `Vault Preview visible`
- `Topic Card Lite/Vault visible`
- `RewriteOutputV1 preview`
- `human V-PASS`

固定不做:

- no source runtime unlock
- no true write
- no batch
- no DB migration
- no browser automation

Lane A 只负责:

- operator flow
- state truth
- preview closure
- surface readability

Lane A 不负责:

- 完整视觉系统建设
- source route实现策略
- true-write flip

### §5.2 Lane B — runtime_tools single-route canary

目标: 把 runtime_tools 从 candidate 推到一次受控 canary，但不写成 runtime approval。

固定策略:

- source family: `Bilibili only`
- live route first choice: `yt-dlp metadata-first`
- fallback/comparator: `BBDown`
- 这次 route 选择是 tactical first-canary choice，不是长期 source strategy promotion

固定 ASR:

- first engine: `Whisper.cpp Metal`
- `FunASR` 仅保留 fallback candidate，不进入首个 live canary 实现

固定边界:

- repo-external temp dir
- `safe_stdout_excerpt` + manifest only
- no raw stdout/stderr tracked
- no vault true write
- no browser automation
- no dual-route live run

### §5.3 Lane C — true_vault_write gate first, flip later

目标: 先把 gate 做完整，再等 `P3A V-PASS` 后对同 payload 做 minimal flip。

Phase 1 只做 gate readiness:

- 12-role completeness contract
- secret scan gate
- path containment gate
- atomic write precondition
- receipt/rollback evidence contract

Phase 1 禁止:

- source runtime
- ASR runtime
- batch logic
- migration
- DTO/schema drift
- frontend 顺手大改

### §5.4 Lane D — PF-V visual productization

目标: 不让 PF-V 停留在 reference asset，而是产品化为 operator workstation 视觉系统。

第一阶段默认是 `candidate / visual-productization / not-authority`，内容包括:

- PF-V asset mapping
- panel/component target map
- state visual grammar
- UI stack option comparison
- dependency risk table
- which assets enter runtime vs remain reference-only

若后续进入 code-bearing:

- 必须新 dispatch
- 必须声明 allowed paths
- 必须确认是否占 product lane slot
- 不得混入 source/runtime/true-write PR

### §5.5 Phase 1 并行 companion studies

#### A. UI stack decision candidate

必须回答:

1. 现有 self-rolled CSS/TSX 是否已经形成视觉瓶颈
2. 是否值得引入 `shadcn` / `Tailwind` / `Radix` / `React Flow` / graph lib
3. 最小可接受引入点是什么
4. 哪些 PF-V asset 必须产品化，哪些只保留 reference
5. 若引 dependency，如何严格隔离在 Lane D，不污染 A/B/C

默认结论前提:

- 首波默认继续 self-rolled
- 但不再把 “永不引新 UI stack” 当先验真理

#### B. DB vNext architecture decision candidate

只做决策，不做 migration implementation。

必须回答:

1. `10 / 100 / 1000` item 下的主要瓶颈分别是什么
2. 哪些数据必须持久化进 DB
3. 哪些只保留 receipt files
4. SQLite 当前 path 还能撑多久
5. 何时才触发 Lane 4 implementation
6. 不做 DB vNext 的最大代价是什么

必须比较:

- current SQLite path
- SQLite + manual SQL migration
- SQLite + backup strategy
- DuckDB analytics mirror
- future Postgres option

## §6 Phase 2 — Single-item closure

### §6.1 P3A — Preview-only closure

`P3A` 是第一道真正的 product proof。

Clear 条件:

- URL present
- source receipt present
- `TranscriptHandoffV1` present，或明确写成 blocked
- `RewriteOutputV1` present
- vault preview hash present
- Trust Trace visible
- human `V-PASS`
- remaining Holds listed

不允许:

- 把 preview 写成 closure
- 把 preview 写成 write
- 把 blocked state 写成 success

### §6.2 P3B — Same-payload minimal true-write canary

`P3B` 只允许在 `P3A clear` 后启动。

固定前置:

- same URL
- same source receipt
- same transcript handoff
- same rewrite payload
- same preview hash
- user explicit true-write gate

Clear 条件:

- 12-role completeness pass
- secret scan pass
- path containment pass
- atomic write pass
- hash pass
- rollback/cleanup receipt pass

## §7 Phase 3 — 3 URL smoke batch

### §7.1 目标

验证 batch machinery 不崩，不把 `3 URL` 假装成最终批量能力证明。

### §7.2 固定参数

- `3 URLs`
- `<=2 logical in-flight slots`
- `preview-only` first
- `same 3 URLs true-write` second

### §7.3 交付物

- per-item receipt
- final state per item
- dedupe result
- lightweight cost row
- one-page batch closeout
- remaining Holds

## §8 Phase 3.5 — 10 URL friction batch

### §8.1 为什么必须有 10 URL

`3 URL` 只能发现:

- 单条流程可否重复
- preview/write boundary 是否能守住
- final state 能否写清

`10 URL` 才有机会暴露:

- dedupe 真价值
- rate/runtime drift
- ASR 耗时分布
- rewrite 质量/成本波动
- vault note naming collision
- operator 连续处理负担
- batch closeout 信息噪音

### §8.2 固定参数

- `10 URLs`
- `2-3 logical slots`
- no scheduler
- no worker architecture
- no DB queue

### §8.3 分两段

- `Batch 10A`: 10 URL preview-only friction
- `Batch 10B`: same 10 URL true-write friction

`10B` 进入条件:

- `P3B clear`
- `Batch 3A` clear or partial-with-known-reason
- `Batch 10A` closeout complete

### §8.4 必观察摩擦

- dedupe/idempotency
- source failure spread
- ASR time distribution
- rewrite quality drift
- vault naming/path collisions
- operator fatigue
- receipt readability
- closeout noise level

## §9 Phase 4 — 扩展判断

以下都 clear 后，才进入正式扩展判断:

- `P3A clear`
- `P3B clear`
- `Batch 3` closeout complete
- `Batch 10` friction report complete

扩展顺序固定为:

1. `W4G` rewrite fullization
2. `W5H` source matrix expansion
3. `W5I` comments / nested comments
4. `Lane 4` DB vNext implementation
5. `Lane 5` full signal workbench

其中:

- `DB vNext` 只有在 batch friction 明确暴露 DB 痛点后才进 implementation
- `Lane 5` 只有在 proof-pair canary 与 lane 1/2/4 dependency verdict 齐备后才启动

## §10 最小接口集

### §10.1 SourceAdapterV1

首波只需要最小 source seam，不造平台。

最小职责:

- `probe_metadata`
- `fetch_media`
- `extract_audio`
- `classify_failure`
- `emit_source_receipt`

### §10.2 TranscriptHandoffV1

9 个 required fields:

1. `transcript_text`
2. `language_detected`
3. `duration_seconds`
4. `asr_engine`
5. `asr_model_sha256`
6. `extraction_seed`
7. `trust_trace_id`
8. `source_url`
9. `capture_date`

缺任一字段时只能写:

- `candidate`
- `handoff_incomplete`

不得写成 ready-for-rewrite。

### §10.3 RewriteOutputV1

首波唯一 active rewrite style:

```text
style_id = obsidian_capture_note_v1
```

固定输出 sections:

1. Title
2. Source summary
3. Key points
4. Transcript-backed details
5. Trust / evidence notes
6. Follow-up questions or open uncertainties

### §10.4 VaultCommitCandidateV1

最小要求:

- 12 role slots
- preview/commit split
- secret scan verdict
- path verdict
- output hash
- rollback receipt

### §10.5 ItemRunManifestV1 / BatchRunManifestV1

只服务:

- item identity
- claim state
- final state
- evidence links
- cost row

不服务:

- scheduler
- worker orchestration
- queue backend

## §11 Multi-agent 分工

### §11.1 GPT Pro

固定负责:

- Lane D visual productization candidate
- UI stack decision candidate
- DB architecture decision candidate
- runtime_tools canary prompt refine
- batch friction closeout template

### §11.2 Codex

固定负责:

- Lane A P3 preview vertical slice
- Lane B runtime single-route canary
- Lane C true-write gate + minimal flip
- Lane D code-bearing visual productization (仅在获准后)

### §11.3 Opus

固定负责:

- boundary audit
- overclaim audit
- visual truth audit
- DB architecture critique

### §11.4 User

固定 gate:

- human `V-PASS`
- true-write explicit gate
- first source route tactical choice
- UI dependency gate

## §12 验收与 stop-line

### §12.1 通过条件

- single-item preview 必须 clear
- single-item true write 必须 clear
- 3 URL smoke batch 至少得到 truthful closeout
- 10 URL friction batch 必须得到 friction report
- 所有 closeout 必须列 remaining Holds
- 所有视觉 claim 必须经过人工 V-PASS

### §12.2 永久 stop-line

出现以下任一项立即停线:

- candidate 文档被写成 authority
- preview 被写成 commit success
- bounded canary 被写成 runtime-ready/full-platform-ready
- source/ASR/true-write/migration/browser 自动被顺手打开
- raw stdout/stderr、cookie、token、signed params 进入 tracked evidence
- Lane 5 在 lane 1/2/4 未 ready 时偷开
- UI stack dependency 混入 source/runtime/write PR

## §13 一句话总路线

ScoutFlow 下一波应以 `P3 single-item preview workstation` 为产品主线，以 `runtime_tools 单路 canary` 和 `true_vault_write gate` 为并行辅线，同时新增 `PF-V visual productization Lane D`；`3 URL` 只作 smoke，随后必须跑 `10 URL friction batch`；`DB migration` 实现后置，但 `DB architecture decision` 必须提前锁定。

## §14 和 master spec 的配套读法

新 session 的推荐读法:

1. `docs/current.md`
2. `docs/00-START-HERE.md`
3. `docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md`
4. `docs/BATCH-TRANSCRIPTION-MASTER-ROADMAP-2026-05-08.md`

解释:

- `master spec` 看大局、inventory、长期 wave、升级路径
- `0508 roadmap` 看下一波 program、lane 拆分、batch 节奏、视觉与 DB 修正

这份 roadmap 默认作为后续 `P3 / runtime_tools / true_vault_write / batch friction / PF-V productization` 的 companion document 使用。
