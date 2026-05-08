---
title: W3E 80-pack Residual First Cluster Starter Pack
status: candidate
authority: not-authority
created_by: gpt-pro
parent_cluster: W5
created_at: 2026-05-08
disclaimer: "W3E cluster 推荐基于 master spec §13.1 W3E 行 + 80-pack 04-first-packs-to-open.md live candidate 顺序 + PF-C0-O1 PACK-INDEX live R-version status; 不构成 execution approval"
inputs:
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/research/post-frozen/80-pack-source/01_route_decision/04-first-packs-to-open.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/research/post-frozen/80-pack-source/02_task_packs/PF-C0-O1-successor-entry-pack/PACK-INDEX.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/research/post-frozen/80-pack-source/02_task_packs/PF-C0-O1-successor-entry-pack/PACK-README.md
  - https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/research/post-frozen/PF-C4-01-codex-commander-prompt-2026-05-07.md
真态_anchor:
  current_main: c802de4
  active_lane: 0/3
  authority_writer: 0/1
  pf_c0_o1_task_count: 12
  pf_c0_o1_live_active_r_versions: [PF-C0-01R, PF-C0-MERGED-03+04, PF-C0-06R, PF-O1-01R]
---

# §0 边界声明 + 4 status 词

本文是 **candidate starter pack**，不是 commander prompt final，也不是 execution approval。它只回答：W3E 第一 cluster 推荐哪个、为什么、如何拆 5-10 dispatch。🚦

硬边界：

- 不重开 Dispatch126-176；它们是 frozen historical assets/evidence。
- 不打开 overflow/reservoir tasks，除非服务 live gate。
- 不执行 deprecated task；deprecated task 只能作为 reference language extraction。
- 不写 authority files，不改 runtime/migration/browser/vault gates。

# §1 W3E 在 master spec §13.1 的位置

原 W3E 语义：`80-pack 余量 cluster (PF-C0 / O1 / C3 等)`；输入来自 U9 dispatch-catalog + Codex multi-PR；各 cluster 独立，不阻塞 W2C/W4F。  
4-agent v3 分工：

| Agent | W3E role | 输出 |
|---|---|---|
| GPT Pro | spec / cross-cluster handoff / starter pack | 本文 |
| CC1 | U9/80-pack 选 cluster + commander prompt + audit | final commander |
| Codex | 通宵 multi-PR / dispatch execution | receipt + CHECKPOINT |
| Hermes | external audit | cross-cluster consistency verdict |
| 战友 | 拍板第一 cluster | A/B/C route decision |

# §2 5 candidate cluster 真态盘点

| Order | Pack | Dispatch count | Suggested open | Why | W5 verdict |
|---:|---|---:|---:|---|---|

| 1 | `PF-C0-O1-successor-entry-pack` | 12 | 3-4 | Thin successor entry + overflow day-zero guard | highest-entry-gate |
| 2 | `PF-localhost-preview-pack` | 18 | 8-13 | localhost paste/click/markdown/copy/download proof | direct product proof but larger scope |
| 3 | `PF-C1-proof-pair-pack` | 12 | 4-6 | real URL usefulness proof pair | good after entry gate |
| 4 | `PF-C2-raw-handoff-pack` | 12 | 4-6 | not-second-inbox RAW handoff proof | depends on handoff clarity |
| 5 | `PF-C4-controlled-hardening-pack` | 8 | 3-5 | hardening only after proof or strong partial | not first unless proof exists |

补充：PF-C3-minimal-object-compression-pack 在 master spec W3E example 中出现，且 prompt 提到 §15.2 P2 leaning PF-C3；但 `04-first-packs-to-open.md` live 顺序未把 PF-C3 放入前 5。这个冲突必须显式给战友拍板。

# §3 推荐第 1 个 W3E cluster

## §3.1 推荐 cluster: PF-C0-O1-successor-entry-pack

**推荐路径**: 先开 `PF-C0-O1-successor-entry-pack`，但只开 5-7 张精选 cards，不把 12 个任务全开。

理由：

1. live route decision 把 PF-C0-O1 排第 1，理由是 “Thin successor entry + overflow day-zero guard”。
2. PACK-README 明确它是 code-bearing localhost work 之前的 thin gate，open_after_state = live authority readback。
3. PACK-INDEX 显示 12 tasks 中只有 4 个 active R-version / high-blocker item；其余 PF-O1-02~06 多为 deprecated，应 reference-only。
4. 24h consumer 明确：CC1 final commander prompt / Codex W3E entry / Hermes overflow guard audit。
5. 它直接降低后续最大风险：把 frozen dispatch、authority readback、overflow gate、mainline-only matrix 一次锁住。

## §3.2 Leaning 冲突显化

| 来源 | Leaning | 解释 | 本文处置 |
|---|---|---|---|
| 80-pack `04-first-packs-to-open.md` | PF-C0-O1 first | successor entry + day-zero overflow guard | 本文推荐 |
| prompt/master spec 摘要 | PF-C3 leaning | “跟 PF-C4 强相关” | 作为备选 B |
| 产品 proof 直觉 | PF-localhost-preview | 直接产品闭环 proof | 作为备选 A，体量需拆 |

# §4 PF-C0-O1 cluster spec（starter draft）

## frontmatter

```yaml
---
title: PF-C0-O1 W3E First Cluster — successor entry + overflow day-zero guard
status: candidate
authority: not-authority
target_executor: Codex long-runner
expected_runtime: 4-6h
created_at: 2026-05-08
inputs:
  - docs/research/post-frozen/80-pack-source/02_task_packs/PF-C0-O1-successor-entry-pack/PACK-INDEX.md
  - docs/research/post-frozen/80-pack-source/02_task_packs/PF-C0-O1-successor-entry-pack/PACK-README.md
  - docs/current.md
  - docs/task-index.md
  - docs/memory/INDEX.md
boundary:
  no_authority_write: true
  no_runtime_unlock: true
  no_migration: true
  no_browser_automation: true
  no_true_vault_write: true
---
```

## §0 角色与上下文

Codex 是 long-runner executor；CC1 是 conductor/auditor；GPT Pro 提供 starter spec；Hermes 做 external audit；战友拍板 cluster 与 merge。

## §1 Mission

锁定 W3E successor entry：完成 live authority readback、frozen dispatch inheritance boundary、near-term mainline-only execution matrix、overflow registry v0 与 reference-only Hold appendix。该 cluster 不执行 runtime、不打开 deprecated tasks、不写 authority。

## §2 Inputs

- PACK-INDEX / PACK-README（PF-C0-O1 live true source）
- current.md / task-index.md / decision-log.md / memory INDEX（pre-flight）
- master spec §14 / §16.2（governance + legal upgrade path）
- PF-C4-01 commander prompt（schema reference）

## §3 Hard Boundaries

```yaml
write_enabled: false
authority_files_writable: false
can_open_runtime: false
can_open_migration: false
can_open_browser_automation: false
can_open_true_vault_write: false
can_reexecute_dispatch126_176: false
can_execute_deprecated_tasks: false
```

Allowed output path only:

- `docs/research/post-frozen/2026-05-08/W3E-PF-C0-O1/**`

Forbidden claim:

- runtime approved / migration approved / true vault write approved / browser automation approved / 5 overflow lane unlocked / deprecated task executed.

## §4 2-Phase 执行计划

| Phase | Dispatch cards | Goal | Gate |
|---|---|---|---|
| Phase 1 | 3 | successor entry readback + scope memo + execution matrix | all clear before overflow appendix |
| Phase 2 | 4 | overflow registry + reference-only gate extraction | no deprecated task execution |

## §5 cross-dispatch consistency contract

- Every dispatch includes current main SHA readback.
- Every dispatch states 24h consumer.
- Deprecated PF-O1 items are language sources only, never execution units.
- Frozen Dispatch126-176 are evidence, not backlog.
- If any card needs authority write, runtime, migration, or browser automation, stop and amend.

## §6 dispatch 列表表

| dispatch_id | source | class | 24h consumer | verdict target |
|---|---|---|---|---|

| `PF-C0-O1-P1-01-successor-entry-readback` | `PF-C0-01R` | candidate dispatch card | CC1 + Codex / W3E entry / authority readback card | clear/partial/reject |
| `PF-C0-O1-P1-02-successor-scope-memo` | `PF-C0-MERGED-03+04` | candidate dispatch card | CC1 / W3E cluster prompt / scope memo | clear/partial/reject |
| `PF-C0-O1-P1-03-mainline-execution-matrix` | `PF-C0-06R` | candidate dispatch card | Codex / W3E dispatch queue / matrix card | clear/partial/reject |
| `PF-C0-O1-P2-01-overflow-registry-v0` | `PF-O1-01R` | candidate dispatch card | CC1 + Hermes / overflow audit / registry card | clear/partial/reject |
| `PF-C0-O1-P2-02-true-vault-gate-reference` | `PF-O1-02 reference-only` | candidate dispatch card | CC1 / W6J prep / true-write gate memo | clear/partial/reject |
| `PF-C0-O1-P2-03-runtime-tools-gate-reference` | `PF-O1-03 reference-only` | candidate dispatch card | Hermes / W4F prep audit / runtime gate memo | clear/partial/reject |
| `PF-C0-O1-P2-04-db-browser-signal-hold-merge` | `PF-O1-04/05/06 reference-only` | candidate dispatch card | Codex / W3E closeout / overflow appendix | clear/partial/reject |

## §7 dispatch 通用 schema

每张卡使用 Deliverable 2 的 9 段：dispatch_id / mission / input / output / steps / verification / verdict / boundary / amend_trigger + self-verification。

## §8 amend_and_proceed pattern

- 自主 amend 上限：1 次。
- runtime/migration/authority/browser/vault 触发：不得自主 amend，必须 stop + receipt。
- deprecated task execution 触发：立即 revert + kill receipt。

## §9 lane closeout

输出：

- `PF-C0-O1-cluster-closeout-2026-05-08.md`
- `PF-C0-O1-CHECKPOINT.json`
- `PF-C0-O1-dispatch-verdict-table.md`

Closeout 必含：dispatch verdict、boundary preservation、deprecated-task handling、overflow Hold state、next cluster recommendation。

## §10 self-verification

- [ ] current main readback correct。
- [ ] Active product lane / Authority writer readback correct。
- [ ] 7 dispatch cards 全含 24h consumer。
- [ ] 不执行 deprecated tasks。
- [ ] 不写 authority files。
- [ ] 5 overflow lanes 仍 Hold。
- [ ] Self-flag 填写。

# §5 7 dispatch cards 启动包


## 1. `PF-C0-O1-P1-01-successor-entry-readback`

### 1. mission
Live authority readback after PR #247 / current c802de4, replacing stale PR194 wording with live anchor.

### 2. input
- `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/research/post-frozen/80-pack-source/02_task_packs/PF-C0-O1-successor-entry-pack/PACK-INDEX.md`
- `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/research/post-frozen/80-pack-source/02_task_packs/PF-C0-O1-successor-entry-pack/PACK-README.md`
- `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md`
- `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md`

### 3. output
- `docs/research/post-frozen/2026-05-08/W3E-PF-C0-O1/01-successor-entry-readback.md`

### 4. steps
1. Read PACK-INDEX row `PF-C0-01R` and classify active / deprecated / reference-only.
2. Read current/task-index anchors and write the observed SHA/lane state into the card.
3. Draft the bounded memo/table for this dispatch only.
4. Mark any stale PR194/Dispatch126-176 wording as historical reference, not live execution anchor.
5. Write verification notes and self-flag.

### 5. verification
- pre-flight: `current.md` main must equal live readback; Active product lane must not be silently consumed.
- post-execution: output file has status candidate / not-authority; no forbidden claim; no authority write path.
- quality: source row status handled correctly; deprecated/reference-only status not erased.

### 6. verdict
- expected: `clear` if memo is bounded and boundary-preserving.
- `partial` if latest decision-log D-ID cannot be extracted.
- `reject` if it executes deprecated tasks or claims Hold lane unlocked.

### 7. boundary
- allowed: candidate memo under W3E-PF-C0-O1 research folder.
- forbidden: authority write, runtime execution, migration, browser automation, true vault write, deprecated-task execution.
- forbidden claim: `runtime approved`, `migration approved`, `5 overflow lane unlocked`.

### 8. amend_trigger
- silent_flexibility: any expansion beyond `PF-C0-01R` scope → stop + amend receipt.
- runtime/migration/authority trigger → stop; cannot self-approve.
- stale live anchor trigger → replace with current readback and self-flag.

### 9. self-verification
- [ ] 24h consumer: CC1 + Codex / W3E entry / authority readback card
- [ ] source row status preserved。
- [ ] no implementation code body。
- [ ] no local shell assumption in cloud spec。


## 2. `PF-C0-O1-P1-02-successor-scope-memo`

### 1. mission
Successor entry + preview-only scope memo; locks frozen 126-176 as evidence, not execution backlog.

### 2. input
- `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/research/post-frozen/80-pack-source/02_task_packs/PF-C0-O1-successor-entry-pack/PACK-INDEX.md`
- `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/research/post-frozen/80-pack-source/02_task_packs/PF-C0-O1-successor-entry-pack/PACK-README.md`
- `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md`
- `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md`

### 3. output
- `docs/research/post-frozen/2026-05-08/W3E-PF-C0-O1/02-successor-scope-memo.md`

### 4. steps
1. Read PACK-INDEX row `PF-C0-MERGED-03+04` and classify active / deprecated / reference-only.
2. Read current/task-index anchors and write the observed SHA/lane state into the card.
3. Draft the bounded memo/table for this dispatch only.
4. Mark any stale PR194/Dispatch126-176 wording as historical reference, not live execution anchor.
5. Write verification notes and self-flag.

### 5. verification
- pre-flight: `current.md` main must equal live readback; Active product lane must not be silently consumed.
- post-execution: output file has status candidate / not-authority; no forbidden claim; no authority write path.
- quality: source row status handled correctly; deprecated/reference-only status not erased.

### 6. verdict
- expected: `clear` if memo is bounded and boundary-preserving.
- `partial` if latest decision-log D-ID cannot be extracted.
- `reject` if it executes deprecated tasks or claims Hold lane unlocked.

### 7. boundary
- allowed: candidate memo under W3E-PF-C0-O1 research folder.
- forbidden: authority write, runtime execution, migration, browser automation, true vault write, deprecated-task execution.
- forbidden claim: `runtime approved`, `migration approved`, `5 overflow lane unlocked`.

### 8. amend_trigger
- silent_flexibility: any expansion beyond `PF-C0-MERGED-03+04` scope → stop + amend receipt.
- runtime/migration/authority trigger → stop; cannot self-approve.
- stale live anchor trigger → replace with current readback and self-flag.

### 9. self-verification
- [ ] 24h consumer: CC1 / W3E cluster prompt / scope memo
- [ ] source row status preserved。
- [ ] no implementation code body。
- [ ] no local shell assumption in cloud spec。


## 3. `PF-C0-O1-P1-03-mainline-execution-matrix`

### 1. mission
Near-term 20-30 mainline-only execution matrix; no overflow/reservoir task unless live gate.

### 2. input
- `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/research/post-frozen/80-pack-source/02_task_packs/PF-C0-O1-successor-entry-pack/PACK-INDEX.md`
- `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/research/post-frozen/80-pack-source/02_task_packs/PF-C0-O1-successor-entry-pack/PACK-README.md`
- `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md`
- `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md`

### 3. output
- `docs/research/post-frozen/2026-05-08/W3E-PF-C0-O1/03-mainline-execution-matrix.md`

### 4. steps
1. Read PACK-INDEX row `PF-C0-06R` and classify active / deprecated / reference-only.
2. Read current/task-index anchors and write the observed SHA/lane state into the card.
3. Draft the bounded memo/table for this dispatch only.
4. Mark any stale PR194/Dispatch126-176 wording as historical reference, not live execution anchor.
5. Write verification notes and self-flag.

### 5. verification
- pre-flight: `current.md` main must equal live readback; Active product lane must not be silently consumed.
- post-execution: output file has status candidate / not-authority; no forbidden claim; no authority write path.
- quality: source row status handled correctly; deprecated/reference-only status not erased.

### 6. verdict
- expected: `clear` if memo is bounded and boundary-preserving.
- `partial` if latest decision-log D-ID cannot be extracted.
- `reject` if it executes deprecated tasks or claims Hold lane unlocked.

### 7. boundary
- allowed: candidate memo under W3E-PF-C0-O1 research folder.
- forbidden: authority write, runtime execution, migration, browser automation, true vault write, deprecated-task execution.
- forbidden claim: `runtime approved`, `migration approved`, `5 overflow lane unlocked`.

### 8. amend_trigger
- silent_flexibility: any expansion beyond `PF-C0-06R` scope → stop + amend receipt.
- runtime/migration/authority trigger → stop; cannot self-approve.
- stale live anchor trigger → replace with current readback and self-flag.

### 9. self-verification
- [ ] 24h consumer: Codex / W3E dispatch queue / matrix card
- [ ] source row status preserved。
- [ ] no implementation code body。
- [ ] no local shell assumption in cloud spec。


## 4. `PF-C0-O1-P2-01-overflow-registry-v0`

### 1. mission
Overflow registry v0; records Hold state and blocks accidental unlock claims.

### 2. input
- `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/research/post-frozen/80-pack-source/02_task_packs/PF-C0-O1-successor-entry-pack/PACK-INDEX.md`
- `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/research/post-frozen/80-pack-source/02_task_packs/PF-C0-O1-successor-entry-pack/PACK-README.md`
- `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md`
- `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md`

### 3. output
- `docs/research/post-frozen/2026-05-08/W3E-PF-C0-O1/04-overflow-registry-v0.md`

### 4. steps
1. Read PACK-INDEX row `PF-O1-01R` and classify active / deprecated / reference-only.
2. Read current/task-index anchors and write the observed SHA/lane state into the card.
3. Draft the bounded memo/table for this dispatch only.
4. Mark any stale PR194/Dispatch126-176 wording as historical reference, not live execution anchor.
5. Write verification notes and self-flag.

### 5. verification
- pre-flight: `current.md` main must equal live readback; Active product lane must not be silently consumed.
- post-execution: output file has status candidate / not-authority; no forbidden claim; no authority write path.
- quality: source row status handled correctly; deprecated/reference-only status not erased.

### 6. verdict
- expected: `clear` if memo is bounded and boundary-preserving.
- `partial` if latest decision-log D-ID cannot be extracted.
- `reject` if it executes deprecated tasks or claims Hold lane unlocked.

### 7. boundary
- allowed: candidate memo under W3E-PF-C0-O1 research folder.
- forbidden: authority write, runtime execution, migration, browser automation, true vault write, deprecated-task execution.
- forbidden claim: `runtime approved`, `migration approved`, `5 overflow lane unlocked`.

### 8. amend_trigger
- silent_flexibility: any expansion beyond `PF-O1-01R` scope → stop + amend receipt.
- runtime/migration/authority trigger → stop; cannot self-approve.
- stale live anchor trigger → replace with current readback and self-flag.

### 9. self-verification
- [ ] 24h consumer: CC1 + Hermes / overflow audit / registry card
- [ ] source row status preserved。
- [ ] no implementation code body。
- [ ] no local shell assumption in cloud spec。


## 5. `PF-C0-O1-P2-02-true-vault-gate-reference`

### 1. mission
Extract true_vault_write gate language from deprecated task as reference only; do not execute deprecated task.

### 2. input
- `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/research/post-frozen/80-pack-source/02_task_packs/PF-C0-O1-successor-entry-pack/PACK-INDEX.md`
- `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/research/post-frozen/80-pack-source/02_task_packs/PF-C0-O1-successor-entry-pack/PACK-README.md`
- `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md`
- `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md`

### 3. output
- `docs/research/post-frozen/2026-05-08/W3E-PF-C0-O1/05-true-vault-gate-reference.md`

### 4. steps
1. Read PACK-INDEX row `PF-O1-02 reference-only` and classify active / deprecated / reference-only.
2. Read current/task-index anchors and write the observed SHA/lane state into the card.
3. Draft the bounded memo/table for this dispatch only.
4. Mark any stale PR194/Dispatch126-176 wording as historical reference, not live execution anchor.
5. Write verification notes and self-flag.

### 5. verification
- pre-flight: `current.md` main must equal live readback; Active product lane must not be silently consumed.
- post-execution: output file has status candidate / not-authority; no forbidden claim; no authority write path.
- quality: source row status handled correctly; deprecated/reference-only status not erased.

### 6. verdict
- expected: `clear` if memo is bounded and boundary-preserving.
- `partial` if latest decision-log D-ID cannot be extracted.
- `reject` if it executes deprecated tasks or claims Hold lane unlocked.

### 7. boundary
- allowed: candidate memo under W3E-PF-C0-O1 research folder.
- forbidden: authority write, runtime execution, migration, browser automation, true vault write, deprecated-task execution.
- forbidden claim: `runtime approved`, `migration approved`, `5 overflow lane unlocked`.

### 8. amend_trigger
- silent_flexibility: any expansion beyond `PF-O1-02 reference-only` scope → stop + amend receipt.
- runtime/migration/authority trigger → stop; cannot self-approve.
- stale live anchor trigger → replace with current readback and self-flag.

### 9. self-verification
- [ ] 24h consumer: CC1 / W6J prep / true-write gate memo
- [ ] source row status preserved。
- [ ] no implementation code body。
- [ ] no local shell assumption in cloud spec。


## 6. `PF-C0-O1-P2-03-runtime-tools-gate-reference`

### 1. mission
Extract runtime_tools gate language from deprecated task as reference only; no BBDown/yt-dlp/ffmpeg/ASR execution.

### 2. input
- `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/research/post-frozen/80-pack-source/02_task_packs/PF-C0-O1-successor-entry-pack/PACK-INDEX.md`
- `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/research/post-frozen/80-pack-source/02_task_packs/PF-C0-O1-successor-entry-pack/PACK-README.md`
- `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md`
- `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md`

### 3. output
- `docs/research/post-frozen/2026-05-08/W3E-PF-C0-O1/06-runtime-tools-gate-reference.md`

### 4. steps
1. Read PACK-INDEX row `PF-O1-03 reference-only` and classify active / deprecated / reference-only.
2. Read current/task-index anchors and write the observed SHA/lane state into the card.
3. Draft the bounded memo/table for this dispatch only.
4. Mark any stale PR194/Dispatch126-176 wording as historical reference, not live execution anchor.
5. Write verification notes and self-flag.

### 5. verification
- pre-flight: `current.md` main must equal live readback; Active product lane must not be silently consumed.
- post-execution: output file has status candidate / not-authority; no forbidden claim; no authority write path.
- quality: source row status handled correctly; deprecated/reference-only status not erased.

### 6. verdict
- expected: `clear` if memo is bounded and boundary-preserving.
- `partial` if latest decision-log D-ID cannot be extracted.
- `reject` if it executes deprecated tasks or claims Hold lane unlocked.

### 7. boundary
- allowed: candidate memo under W3E-PF-C0-O1 research folder.
- forbidden: authority write, runtime execution, migration, browser automation, true vault write, deprecated-task execution.
- forbidden claim: `runtime approved`, `migration approved`, `5 overflow lane unlocked`.

### 8. amend_trigger
- silent_flexibility: any expansion beyond `PF-O1-03 reference-only` scope → stop + amend receipt.
- runtime/migration/authority trigger → stop; cannot self-approve.
- stale live anchor trigger → replace with current readback and self-flag.

### 9. self-verification
- [ ] 24h consumer: Hermes / W4F prep audit / runtime gate memo
- [ ] source row status preserved。
- [ ] no implementation code body。
- [ ] no local shell assumption in cloud spec。


## 7. `PF-C0-O1-P2-04-db-browser-signal-hold-merge`

### 1. mission
Merge browser_automation / dbvnext_migration / full_signal_workbench Hold wording into one guard appendix.

### 2. input
- `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/research/post-frozen/80-pack-source/02_task_packs/PF-C0-O1-successor-entry-pack/PACK-INDEX.md`
- `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/research/post-frozen/80-pack-source/02_task_packs/PF-C0-O1-successor-entry-pack/PACK-README.md`
- `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md`
- `https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md`

### 3. output
- `docs/research/post-frozen/2026-05-08/W3E-PF-C0-O1/07-overflow-hold-appendix.md`

### 4. steps
1. Read PACK-INDEX row `PF-O1-04/05/06 reference-only` and classify active / deprecated / reference-only.
2. Read current/task-index anchors and write the observed SHA/lane state into the card.
3. Draft the bounded memo/table for this dispatch only.
4. Mark any stale PR194/Dispatch126-176 wording as historical reference, not live execution anchor.
5. Write verification notes and self-flag.

### 5. verification
- pre-flight: `current.md` main must equal live readback; Active product lane must not be silently consumed.
- post-execution: output file has status candidate / not-authority; no forbidden claim; no authority write path.
- quality: source row status handled correctly; deprecated/reference-only status not erased.

### 6. verdict
- expected: `clear` if memo is bounded and boundary-preserving.
- `partial` if latest decision-log D-ID cannot be extracted.
- `reject` if it executes deprecated tasks or claims Hold lane unlocked.

### 7. boundary
- allowed: candidate memo under W3E-PF-C0-O1 research folder.
- forbidden: authority write, runtime execution, migration, browser automation, true vault write, deprecated-task execution.
- forbidden claim: `runtime approved`, `migration approved`, `5 overflow lane unlocked`.

### 8. amend_trigger
- silent_flexibility: any expansion beyond `PF-O1-04/05/06 reference-only` scope → stop + amend receipt.
- runtime/migration/authority trigger → stop; cannot self-approve.
- stale live anchor trigger → replace with current readback and self-flag.

### 9. self-verification
- [ ] 24h consumer: Codex / W3E closeout / overflow appendix
- [ ] source row status preserved。
- [ ] no implementation code body。
- [ ] no local shell assumption in cloud spec。


# §6 推荐路径（战友拍板入口）

| Path | 推荐度 | 做法 | 适合情况 | 风险 |
|---|---:|---|---|---|
| A | ⭐⭐⭐⭐⭐ | 直接派 PF-C0-O1 7-card starter | 想先锁 successor/overflow 安全边界 | 产品 proof 慢一天 |
| B | ⭐⭐⭐⭐ | 先派 PF-C3 minimal object compression | 想跟 PF-C4 强相关 work 更近 | 80-pack route decision 未主推 |
| C | ⭐⭐⭐ | 先派 PF-localhost-preview，拆成 2 cluster | 想最快看到 paste/click/markdown/copy/download proof | 18 dispatch 太大，容易超一夜 |

本文推荐 **Path A**。如果战友更看重立刻 proof，可选 Path C，但建议先拆成 `localhost-preview-A` 与 `localhost-preview-B` 两个 cluster。

# §7 风险 + 备选拆解

| Risk | Why it matters | Mitigation |
|---|---|---|
| PF-C0-O1 12 tasks 只开 7 | 剩余任务可能被遗忘 | closeout 写 residual table，后续二轮再判 |
| deprecated PF-O1-02~06 被误执行 | PACK-INDEX 明确 deprecated | 本文只做 reference extraction |
| PR194 wording stale | current main 已 PR247 closeout | dispatch 1 必做 live readback |
| PF-C3 leaning 冲突 | master spec/prompt 与 80-pack route 不完全同向 | 战友拍板；本文显式呈现 |
| overflow gate 与 §16.2 重复 | 容易被认为冗余 | PF-O1 是 day-zero guard；§16.2 是未来合法升级路径 |

# §8 Self-verification Checklist

| Item | Result |
|---|---|
| frontmatter status candidate | pass |
| W3E first cluster has recommendation + alternatives | pass |
| cluster spec includes 10 sections | pass |
| 7 dispatch cards each has 9 segments | pass |
| 24h consumer present per card | pass |
| deprecated tasks treated reference-only | pass |
| no runtime/migration/browser/vault unlock | pass |
| Self-flag present | pass |

## §Self-flag

### 弱项 / 不确定

- ⚠️ PACK-INDEX live shows many PF-O1 rows deprecated; prompt suggested opening PF-O1-02/03 as dispatches. I converted them to reference-only extraction cards to avoid executing deprecated tasks.
- ⚠️ PF-C0-01R title says “after PR194”, but current live main is PR #247 closeout / `c802de4`; dispatch 1 must rewrite live anchor.
- ⚠️ PF-C3 may be strategically better if 战友 prioritizes PF-C4 adjacency over successor/overflow safety. This is a real product-management tradeoff.
- ⚠️ This starter pack does not enumerate actual `dispatches/*.md` file bodies under PF-C0-O1; final commander prompt should fetch exact files before Codex paste.

### 真态 drift

- prompt historical suggestion: PF-C0-01 after PR #247? PACK-INDEX title says PR194; live current main says PR #247 closeout. Use live current for execution anchor.
- prompt suggested 5-7 cards including PF-O1-02/03 direct; PACK-INDEX marks PF-O1-02/03 deprecated. This file treats them as reference-only.

### 待战友 / CC1 拍板取舍点

1. 是否同意 PF-C0-O1 作为 W3E 第 1 cluster。
2. 若不同意，优先 PF-C3 还是 PF-localhost-preview。
3. 是否允许 CC1 将 deprecated PF-O1 rows 的 language 抽成 reference-only appendix。
