---
title: Master Spec vNext Rebase Plan
status: candidate north-star
authority: not-authority
created_by: gpt-pro
parent_cluster: W1-master-spec-rebase
created_at: 2026-05-08
sibling_deliverables:
  - 01-pr243-to-pr245-lineage-delta-atlas.md
  - 03-master-spec-vnext-draft-section-by-section.md
purpose: 章节级 replacement / amend / deprecate plan for master spec vNext
disclaimer: PR # / SHA / merge UTC / Active / write_enabled 数字均为本次核验时刻参考；真值以 §0 Prerequisite Receipts 为准
prerequisite_check: refreshed
write_enabled: false
authority_files_writable: false
not_implementation: true
not_authority: true
not_runtime_approval: true
not_migration_approval: true
not_browser_automation_approval: true
not_true_vault_write_approval: true
5_overflow_lane_hold:
  - true_vault_write
  - runtime_tools
  - browser_automation
  - dbvnext_migration
  - full_signal_workbench
4_status_words_only:
  - current authority
  - promoted addendum
  - candidate north-star
  - reference storage
---

# Master Spec vNext Rebase Plan

> 本计划把 D1 的 lineage atlas 转成可执行 rebase strategy。它不是 PR diff，也不是 authority writer dispatch；它是给 CC0/CC1 后续接手 vNext 的章节级计划。

---

## §0 Prerequisite Receipt Link

- ⚠️ Check 1: refreshed — authority-doc anchor from `docs/current.md` / `docs/00-START-HERE.md` is `c802de4` (PR #247 closeout), while PR lineage confirms PR #245 merged later as `6dd27d7` at `2026-05-07T16:07:19Z`; this pack treats PR #245 as lineage head and flags authority anchor stale.
- ✅ Check 2: clean — live lane counters remain Active product lane `0/3`, Review `0`, Authority writer `0/1`, state `WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`; no code-bearing next gate is open.
- ⚠️ Check 3: refreshed — decision-log contains PR #244 baseline consolidation entry and PR #246 closeout `D-017 follow-up`; PR #245 / #248 did not add decision-log patches in the fetched PR file patches, so D2/D3 mark closeout trail as incomplete rather than inventing entries.
- ⚠️ Check 4: refreshed — `docs/memory/INDEX.md` says `batch_count: 17` and lists 7 lessons + 5 feedback + 5 patterns; `docs/memory/README.md` still says first batch 16, so INDEX is treated as truth and README as stale wording.
- ✅ Boundary check: bridge config still returns `write_enabled=False`; 5 overflow lane all stay Hold; no runtime, migration, browser automation, true vault write, or full signal workbench unlock is implied.

**Plan posture**: `prerequisite_check=refreshed`; authority anchor stale 被纳入计划，不强行清洗。

---

## §1 Mission

产出 master spec vNext 的 rebase plan，明确哪些章节替换、哪些章节只 amend、哪些章节不动，并给出 CC0 后续接管流程。

### §1.1 Deliverables relation

| Deliverable | Role | Output |
|---|---|---|
| D1 | facts | lineage + delta + drift |
| D2 | plan | section-by-section rebase plan |
| D3 | draft | key replacement/amend sections |

### §1.2 Non-goals

- 不写 implementation code
- 不改 authority files
- 不升正式 PRD/SRD base
- 不解禁 runtime/migration/browser/true vault write
- 不合并 3 份 deliverable
- 不把 candidate north-star 改成 current authority

---

## §2 Replacement Principles

| Principle | Application |
|---|---|
| Preserve north-star | §1 vision / 7 stages / 4-layer posture remain stable. |
| Replace truth snapshot | §2 must move from PR #243 baseline to PR #245 lineage head baseline. |
| Amend status, not authority | Status stays candidate north-star; no promoted base claim. |
| Mark drift explicitly | authority-doc anchor stale and memory README stale must be visible. |
| Separate implementation from planning | W2C/W1B ready does not mean implemented. |
| Cross-vendor before risky gates | Same-family audit is not sufficient for strong gate decisions. |

---

## §3 Section Plan Table

| § | 当前内容简述 | 替换 / amend / keep | rebase 后建议 | D3 引用 |
|---|---|---|---|---|
| §0 | Why This Spec | amend | 补 PR #244/#245/#246/#247/#248 后的“现在没做”收窄；保留 north-star 目的。 | D1 §3 / D3 §0 |
| §1 | Vision | keep | 北极星不动：单人 prosumer 操作员工作站。 | D2 §2 |
| §2 | PR #243 Baseline 真态盘点 | replace | 替换为 PR #245 lineage head baseline 真态盘点，含 PR #243→#245 六 PR 链。 | D3 §2-NEW |
| §3 | 采集线 7 阶段全貌 | keep | 架构性段落不受 PR #245 影响。 | D2 §3 |
| §4 | Source Adapter Matrix | keep | 仍是 0 实施 candidate；5 overflow lane Hold 不变。 | D2 §3 |
| §5 | Audio-to-Text | keep | 仍是 future candidate；不解禁 runtime_tools。 | D2 §3 |
| §6 | Rewrite | keep | 大 narrative 与 model router spec 未受 PR #245 影响。 | D2 §3 |
| §7 | Trust Trace | keep | graph/timeline/error-path/citation 仍 candidate；PR #243 TODO 不被 PR #245 覆盖。 | D2 §3 |
| §8 | Capture Station UX 第二波 | amend | 给 13 surface mapping 增加 PR #243 land status；§8.2-§8.5 保持 0 实施 candidate；新增 §8.6。 | D3 §8-AMEND |
| §9 | 横切 system 模块 | amend | §9.3 memory 起点改 17；§9.13 U→§9.x map 已由 PR #246 补。 | D1 §3 / D2 §3 |
| §10 | 算法层 | keep | PR #245 只是 memory graph land，不改变算法 inventory。 | D2 §3 |
| §11 | UX | keep | 仍是 candidate UX/visual 第二波输入。 | D2 §3 |
| §12 | Memory | amend | 升级路线起点改 17；README stale 另列 TODO。 | D3 §14.6 |
| §13 | Wave Routing | replace | 重排 W1A/W2D/W6K 为 landed，W2C/W1B ready，5 overflow Hold。 | D3 §13-NEW |
| §14 | Pre-flight Governance | replace | 集成 Step 0 prerequisite check、PR #246/#247/#248 closeout harness、4-agent v3 SOP。 | D3 §14-NEW |
| §15 | 依赖图 + 优先级 | amend | §15.1 保持；§15.2 标 W1A/W2D/W6K done，W2C next P0。 | D2 §5 |
| §16 | 风险 + 边界守护 | amend | §16.1 保持硬红线；§16.2 替换为升级路径 vNext。 | D3 §16.2-NEW |
| §17 | 时间预算 | amend | 短期预算收窄；中长期不动。 | D2 §3 |
| §18 | Next Action Checklist | amend | 今晚/一周内状态更新；W6K refresh sprint 已部分落地。 | D2 §3 |
| §19 | 引用 | amend | 补 PR #244-#248 + docs/memory + PR246 closeout receipts。 | D2 §3 |

### §3.1 Replace sections

- **§2**: replace because truth snapshot obsolete after PR #244/#246/#247/#248/#245.
- **§13**: replace because wave statuses are materially changed.
- **§14**: replace because governance harness and Step 0 drift check changed operating model.
- **§16.2**: replace because upgrade paths require cross-vendor audit posture.

### §3.2 Amend sections

- **§0**: amend because now-done list must shrink.
- **§8**: amend because static shell land tag and W2C readiness need update.
- **§9**: amend because memory graph starts at 17 and U→§9.x map exists.
- **§12**: amend because memory growth route starts from 17, not 0.
- **§15.2**: amend because priority list must mark W1A/W2D/W6K done.
- **§18**: amend because checklist must reflect done/partial-done state.
- **§19**: amend because reference table must add PR #244-#248 and docs/memory.

### §3.3 Keep sections

- **§1**: keep, with no structural rewrite required.
- **§3**: keep, with no structural rewrite required.
- **§4**: keep, with no structural rewrite required.
- **§5**: keep, with no structural rewrite required.
- **§6**: keep, with no structural rewrite required.
- **§7**: keep, with no structural rewrite required.
- **§10**: keep, with no structural rewrite required.
- **§11**: keep, with no structural rewrite required.
- **§15.1**: keep, with no structural rewrite required.
- **§17.2**: keep, with no structural rewrite required.
- **§17.3**: keep, with no structural rewrite required.

---

## §4 ToC Recommendation

**Recommendation: do not reorder the existing ToC.**

Reasoning:

- The master spec is a strategic map; renumbering would break existing citations.
- Step 0 prerequisite check can live inside §14.2 instead of becoming a new top-level section.
- PR lineage history can be referenced in §2-NEW and §19 rather than adding a separate history chapter.
- D3 is not a paste-ready full master spec; it provides replacement sections only.

Suggested ToC handling:

| ToC item | Treatment |
|---|---|
| §0-§19 | preserve order |
| §14.2 | insert Step 0 prerequisite check substep |
| §19.3 | append PR #244-#248 reference rows |
| Appendix | optional future PR lineage appendix if CC0 wants full history |

---

## §5 Priority Rebase Map

| Priority | Item | State | Action |
|---|---|---|---|
| P0 | W2C PF-C4-02 real data wiring | ready | read §2-NEW, §8-AMEND, §13-NEW, §14-NEW before dispatch |
| P0 | authority closeout refresh | needed | current/START-HERE anchor stale after PR #245; separate authority writer dispatch |
| P1 | W1B graph/timeline/error-path | ready gated | requires OpenDesign reuse upgrade path and no external visual library drift |
| P1 | memory README stale fix | small follow-up | align README 16 → 17 wording |
| P2 | W3E remaining clusters | pending | split by cluster; avoid 80-pack giant PR |
| Hold | runtime/ASR/source expansion | blocked | requires authority upgrade path |

---

## §6 Impact Analysis

### §6.1 Directly affected dispatch/spec inputs

| Lane | Required read | Why |
|---|---|---|
| W2C | Must read §2-NEW + §8-AMEND + §13.1-NEW + §14.2 Step 0 | prevents over-engineering already-landed parts and catches authority drift |
| W1B | Must read §16.2-NEW | graph/timeline/error-path remain implementation work but upgrade gates must be explicit |
| W3E | Must read §13.3-NEW | governance harness and closeout order already changed |
| W6K | Must read §14.6 | memory graph truth is 17 and README wording is stale |

### §6.2 Indirectly affected

- README / START-HERE navigation references may need authority closeout refresh after PR #245.
- contracts-index remains stable but can cite docs/memory as current authority when future contracts use memory items.
- locked-principles remains valid; no LP rewrite required.
- PRD/SRD candidate thin shells remain candidate and must not be promoted through this plan.

### §6.3 Not affected

- 4 status words
- 5 overflow Hold list
- capture-station PR #243 physical implementation baseline
- PRD-v2 and promoted PRD-v2.1 addendum
- SRD-v2 and promoted h5-bridge addendum
- immutable ledger receipts

---

## §7 CC0/CC1 Rebase Flow

| Step | Action | Guard |
|---|---|---|
| Step 1 | CC0 receives D1+D2+D3 | read D1 §0 before any edit |
| Step 2 | External audit prompt | ask Hermes to check D2 table for missing stale sections |
| Step 3 | Double-review draft | CC0 + CC1 review D3 section draft against master spec |
| Step 4 | Human V-PASS | browser-read PR diff and ensure candidate posture remains |
| Step 5 | Single PR | merge only after authority writer slot is available and boundaries pass |
| Step 6 | Post-flight | run refresh flow and update closeout receipts if authority dispatch was opened |

---

## §8 Acceptance Checklist

- [x] D1/D2/D3 frontmatter present and consistent.
- [x] D1 chronological PR order is #243 → #244 → #246 → #247 → #248 → #245.
- [x] D2 section plan contains all §0-§19 rows.
- [x] D3 includes §2-NEW / §8-AMEND / §13-NEW / §14-NEW / §16.2-NEW.
- [x] Authority-doc anchor drift is visible in all three files.
- [x] Memory 17 vs README 16 drift is visible.
- [x] No local-only path is cited.
- [x] No implementation code appears.
- [x] 5 overflow lanes remain Hold.
- [x] Self-flag exists in each file.

---

## §9 Self-flag

- ⚠️ D2 assumes CC0 will decide whether authority closeout refresh for PR #245 is a separate prerequisite PR or bundled with master spec vNext; this plan recommends separate authority writer dispatch if live authority drift must be corrected first.
- ⚠️ §13.3 governance harness path details are summarized from PR metadata/patches, not a full manual read of every retrospective line.
- ⚠️ The optional PR lineage appendix is deferred to CC0; this plan avoids ToC renumbering to protect citations.

> **File path**: `docs/research/post-frozen/2026-05-08/W1-master-spec-rebase/02-master-spec-vnext-rebase-plan.md`
> **Status**: candidate / rebase-plan / not-authority
