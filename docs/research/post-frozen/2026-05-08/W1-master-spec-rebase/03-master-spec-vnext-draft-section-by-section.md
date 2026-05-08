---
title: Master Spec vNext Draft — Key Section by Section
status: candidate north-star
authority: not-authority
created_by: gpt-pro
parent_cluster: W1-master-spec-rebase
created_at: 2026-05-08
sibling_deliverables:
  - 01-pr243-to-pr245-lineage-delta-atlas.md
  - 02-master-spec-vnext-rebase-plan.md
purpose: direct draft for master spec vNext replacement/amend sections
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

# Master Spec vNext Draft — Key Section by Section

> 本 draft 提供 master spec vNext 关键 section 文案：§2-NEW、§8-AMEND、§13-NEW、§14-NEW、§16.2-NEW。它不是完整 master spec，也不是 authority writeback。CC0 可将其拆入 `docs/COLLECTION-LINE-MASTER-SPEC-2026-05-08-vNext.md` 或作为 PR draft source。

---

## §0 Draft Scope + Prerequisite Receipts

本 draft 替换或 amend PR #243 baseline master spec 的关键段落。其余 vision / 7-stage / source matrix / audio / rewrite / trust trace / algorithm / UX / dependency / long-term timing 等章节按 D2 plan 保留。

- ⚠️ Check 1: refreshed — authority-doc anchor from `docs/current.md` / `docs/00-START-HERE.md` is `c802de4` (PR #247 closeout), while PR lineage confirms PR #245 merged later as `6dd27d7` at `2026-05-07T16:07:19Z`; this pack treats PR #245 as lineage head and flags authority anchor stale.
- ✅ Check 2: clean — live lane counters remain Active product lane `0/3`, Review `0`, Authority writer `0/1`, state `WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`; no code-bearing next gate is open.
- ⚠️ Check 3: refreshed — decision-log contains PR #244 baseline consolidation entry and PR #246 closeout `D-017 follow-up`; PR #245 / #248 did not add decision-log patches in the fetched PR file patches, so D2/D3 mark closeout trail as incomplete rather than inventing entries.
- ⚠️ Check 4: refreshed — `docs/memory/INDEX.md` says `batch_count: 17` and lists 7 lessons + 5 feedback + 5 patterns; `docs/memory/README.md` still says first batch 16, so INDEX is treated as truth and README as stale wording.
- ✅ Boundary check: bridge config still returns `write_enabled=False`; 5 overflow lane all stay Hold; no runtime, migration, browser automation, true vault write, or full signal workbench unlock is implied.

### §0.1 Replacement rule

- status remains `candidate north-star`.
- authority remains `not-authority`.
- single-user prosumer north-star unchanged.
- 4-layer architecture unchanged.
- 5 overflow lane Hold unchanged.
- PRD/SRD canonical base unchanged; U1 thin candidate shells are not formal base.
- authority-doc anchor stale is preserved as a known closeout issue, not silently fixed here.

### §0.2 Section replacement map

| Original section | Draft treatment | Reason |
|---|---|---|
| §2 PR #243 Baseline | replace with §2-NEW | truth snapshot now includes PR #244/#246/#247/#248/#245 |
| §8 Capture Station UX | amend | 13 surface static shell is landed, W2C is ready |
| §13 Wave Routing | replace | W1A/W2D/W6K state changed |
| §14 Pre-flight Governance | replace | Step 0 prerequisite check + governance harness now essential |
| §16.2 Upgrade Path | replace | cross-vendor audit requirement must be explicit |

---

# §2-NEW PR #245 Lineage Baseline 真态盘点

> Replaces original `§2 PR #243 Baseline 真态盘点`. This section uses PR #245 as lineage head and separately flags authority-doc anchor drift. All numbers are writing-time receipts, not authority by themselves.

## §2.1 Baseline summary

| Dimension | Truth | Interpretation | Source |
|---|---|---|---|
| Lineage head | `6dd27d7` / PR #245 | merged after PR #248; memory graph land | PR #245 |
| Authority-doc anchor | `c802de4` / PR #247 | current/START-HERE stale relative to PR #245 | PR #247/#248 |
| Capture-station stack | React 18.3.1 + Vite 5.4.10 + CSS Modules + token overlay | 13 surface static shell | PR #243 |
| 13 surface | landed static shell | not live data wired | PR #243 |
| 15 shared components | landed | component baseline for W2C/W1B | PR #243 |
| Token references | 375 var references | visual token density already physical | PR #243 |
| Honest TODO | thumbnail / graph / timeline hover / error path | still pending | PR #243 |
| L8 sync-badge | 3 state done | synced / pending / external-changed | PR #243 |
| Doc baseline | landed | START-HERE + master spec + thin candidate shells + storage | PR #244 |
| 16 ZIP storage | landed | reference storage | PR #244 |
| Governance harness | landed partial | START-HERE/retrospective/master spec closeout order | PR #246 |
| Layer C closeout | landed | PR #246 closeout authority writeback | PR #247 |
| Stale cleanup | landed | L-1/L-2/L-4 + stale PR #247 refresh | PR #248 |
| Memory graph | 17 items landed | docs/memory INDEX true; README stale | PR #245 |
| write boundary | `write_enabled=False` | unchanged | bridge config |
| 5 overflow lane | Hold | true_vault_write/runtime_tools/browser_automation/dbvnext_migration/full_signal_workbench | current/START-HERE |

## §2.2 Chronological lineage

| Order | PR | Merge UTC | SHA | Meaning |
|---|---|---|---|---|
| 1 | #243 | 2026-05-07T08:02:55Z | e1deda6 | PF-C4-01 capture-station physical baseline |
| 2 | #244 | 2026-05-07T11:00:52Z | e207664 | baseline navigation consolidation + master spec promotion |
| 3 | #246 | 2026-05-07T15:39:31Z | 3c01a1c | governance harness + CC1 retrospective sediment |
| 4 | #247 | 2026-05-07T15:43:19Z | c802de4 | PR #246 closeout — Layer C writeback |
| 5 | #248 | 2026-05-07T15:52:39Z | 4792b0f | stale refresh + L-1/L-2/L-4 cleanup |
| 6 | #245 | 2026-05-07T16:07:19Z | 6dd27d7 | W2D cross-vendor memory graph land |

## §2.3 Current caveats

- Do not say `main anchor is fully refreshed` until authority docs include PR #245 or a new closeout explicitly records why PR #245 did not require authority anchor movement.
- Do not treat PR #245 title stale wording as truth; use INDEX count 17 and changed files list 19.
- Do not treat PR #246 same-family Layer 1.5 audit as final cross-vendor strong gate; it is useful evidence but not a vendor-diversified gate. (Layer 1.5 = same-family double review, Layer 2 = cross-vendor; instinct §3 #16 standard naming)
- Do not treat capture-station static shell as data-wired W2C implementation.
- Do not turn candidate thin shells into canonical PRD/SRD base.

## §2.4 Baseline consequence for next work

| Lane | State | Consequence |
|---|---|---|
| W2C | ready | start from physical shell + doc baseline + governance Step 0 |
| W1B | ready gated | graph/timeline/error-path remain honest TODO; upgrade path needed for visual library choices |
| W6K | partial landed | memory graph and governance harness now need consolidation, not first land |
| Authority closeout | needed | PR #245 drift should be addressed separately if CC0 wants clean anchor |

---

# §8-AMEND Capture Station UX 第二波

> This amends the original §8. PR #243 has already landed the static shell; W2C should not rebuild shell from scratch. It should hydrate the existing shell with live data, state, and micro-interactions while keeping the write boundary disabled where required.

## §8.1-AMEND 13 surface × Bridge API mapping with land status

| Surface | Route / DTO | PR #243 land status | vNext action |
|---|---|---|---|
| 01 URL Bar | POST /captures/discover | ✅ PR #243 static shell | W2C 接真数据 + url validation |
| 02 Live Metadata | GET /captures/{id}/metadata | ✅ PR #243 static shell | W2C 读取 current capture metadata |
| 03 Capture Scope | GET /captures/{id} | ✅ PR #243 static shell | W2C 生命周期状态 + guard copy |
| 04 Trust Trace | GET /captures/{id}/trust-trace | ✅ shell / ⏳ graph TODO | W1B graph + timeline + error path |
| 05 Vault Preview | POST /bridge/vault/preview | ✅ PR #243 static shell | W2C preview data hydration |
| 06 Vault Commit | POST /bridge/vault/commit | ✅ disabled static shell | true_vault_write 升级前只保留 disabled |
| 07 Topic Card Lite | capture/topic DTO | ✅ PR #243 static shell | W2C card hydration |
| 08 Topic Card Vault | vault preview DTO | ✅ PR #243 static shell | W2C frontmatter preview data |
| 09 Signal Hypothesis | signal candidate DTO | ✅ PR #243 static shell | W3E later |
| 10 Capture Plan | capture plan DTO | ✅ PR #243 static shell | W3E later |
| 11 Density Spec | tokens/density | ✅ PR #243 static shell | no runtime dependency |
| 12 Type Spec | tokens/type | ✅ PR #243 static shell | no runtime dependency |
| 13 L8 Sync Badge | sync badge state | ✅ 3 state done | W2C promote to live state |

## §8.2 State machine — unchanged candidate

| State | Meaning | Current surface | vNext action |
|---|---|---|---|
| idle | no URL / no capture | existing shell placeholder | W2C adds live transition |
| discovering | metadata fetch in progress | static visual exists | W2C connects route |
| metadata_ready | metadata found | static visual exists | W2C populates card |
| scope_review | operator reviews capture scope | static visual exists | W2C adds guard copy |
| preview_ready | vault preview generated | static visual exists | W2C hydrates markdown/frontmatter |
| commit_disabled | true write unavailable | disabled shell exists | must remain disabled until upgrade path |
| error | safe error path | TODO for error-path visual | W1B/W2C split |

## §8.3 Micro-interactions — still candidate

- URL validation pulse should be data-driven, not decorative.
- L8 sync-badge should promote from static three-state to live state only after source truth exists.
- Timeline hover and error-path are W1B/W2C split; do not silently implement them as fake visuals.
- Vault Commit control must stay disabled and explicit about boundary until true_vault_write path is approved.
- All motion must be evidence-serving; no generic dashboard animation.

## §8.4 L8 sync-badge promotion guard

| Badge | Current | Promotion requirement |
|---|---|---|
| synced | static state exists | route/data confirms external state |
| pending | static state exists | operation in-flight state is real |
| external-changed | static state exists | external delta is verified and operator-visible |

## §8.5 Capture state machine — unchanged boundary

- capture state may display evidence but must not imply media/runtime completion.
- receipt ledger evidence may display but must not imply vault write.
- Bridge/Vault preview may display but must not imply true commit.
- browser automation remains Hold; any visual test evidence must be labeled as bounded/static unless future path upgrades it.

## §8.6-NEW Pre-W2C launch guard

- Read §2-NEW to avoid rebuilding already-landed shell.
- Read §13.1-NEW to see W2C is next P0 after W1A/W2D/W6K partial done.
- Read §14.2 Step 0 before citing PR number, SHA, lane count, memory count, or write boundary.
- Confirm authority-doc anchor drift handling before writing commander prompt.
- Confirm README memory count stale wording is not copied into W2C spec.

---

# §13-NEW Wave Routing + 4-agent v3 分工

> Replaces original §13. It updates wave status after PR #244/#246/#247/#248/#245 and makes the governance harness part of routing rather than a separate afterthought.

## §13.1-NEW Wave list

| # | Wave | Main owner | Blocker | Time | Status | Source / note |
|---|---|---|---|---|---|---|
| W1A | untracked batch land / 16 ZIP storage | CC1 | none | done | ✅ landed | PR #244 |
| W2D | U16 memory ingest | CC1 | none | 60-90min | ✅ landed | PR #245 |
| W6K | Memory + collaboration mode sediment | CC1 + audits | PR #246 follow-up | multi-step | ✅ landed partial | PR #246/#247/#248 |
| W2C | PF-C4-02 real data wiring + micro-interactions | GPT Pro spec + Codex implementation | Prereq §14 Step 0 + W2C commander | 6-8h | 🚀 ready | next P0 |
| W1B | PF-C4-EXT graph/timeline/error-path | Codex + design audit | OpenDesign reuse strategy v2 | 6-8h | 🚀 ready gated | depends upgrade |
| W3E | 80-pack remaining clusters | Codex multi-PR + CC1 audit | cluster-by-cluster | multi-day | ⏳ pending | independent |
| W4F | Phase 2 ASR spike | GPT Pro + Codex | runtime_tools authority path | multi-day | 🔒 hold | overflow |
| W4G | Phase 2 Rewrite | GPT Pro + Codex | W4F + runtime path | multi-day | 🔒 hold | overflow |
| W5H | Source matrix expansion | Codex multi-PR | runtime_tools authority path | multi-day | 🔒 hold | overflow |
| W5I | comments / nested comments subsystem | Codex + Hermes audit | W5H | multi-day | 🔒 hold | overflow |
| W6J | Vault commit true unlock | GPT Pro + Codex + CC0/CC1 + Hermes | W4F/W4G/W5H + true_vault_write path | multi-week | 🔒 hold | overflow |

### §13.1.1 Routing implications

- W1A is no longer a backlog candidate; it landed in PR #244.
- W2D is no longer pending; cross-vendor memory landed in PR #245, with README stale wording follow-up.
- W6K is partially landed through governance harness and stale cleanup; remaining work is consolidation and cross-vendor mirror, not first harness land.
- W2C becomes next P0 product lane, but it must start with Step 0 drift checks.
- W1B remains high visual value but must respect upgrade path around graph library and visual principles.
- All 5 overflow lanes stay Hold; do not batch-unlock them.

## §13.2-AMEND 4-agent v3 division matrix

| Agent | Role | Strength | Weakness / guard | Best next use |
|---|---|---|---|---|
| GPT Pro | Heavy Producer | one-shot schema/narrative/spec | No local repo operations; cannot be long runner | W2C spec, D3 vNext draft, dispatch schema |
| Codex | Long Runner Coder | local execution, sustained patches, tests, multi-PR rhythm | Narrative may need CC1/GPT Pro polish | W2C implementation, W1B self-rolled graph, W3E clusters |
| CC0 | Conductor + final authority coordinator | route, user-facing decisions, merge control | same-family self-audit not enough | V-PASS, double review, boundary adjudication |
| CC1 | Spec/audit/engineer | governance harness, retrospective, high-signal repair | long session can drift without Step 0 | PR #244/#246/#247/#248 evidence |
| Hermes | Independent external audit | vendor-diversified critique | needs precise prompt and source pack | pre-flight and upgrade-path audit |

### §13.2.1 Evidence-backed lessons

| Wave | Observed owner | Evidence | Guard |
|---|---|---|---|
| W2D | CC1 main run | PR #245 memory graph landed with Layer 2 catching H/M issues | use INDEX as truth; do not over-trust title wording |
| W6K | CC1 + closeout | PR #246/#247/#248 governance harness and cleanup | requires cross-vendor strong gate for future risky decisions |
| W1A | CC1 main run | PR #244 doc baseline and storage landed | doc consolidation does not promote candidate shells |
| W2C | GPT Pro + Codex proposed | spec one-shot + long-runner implementation is best fit | CC1/Hermes audit before code-bearing work |

## §13.3-AMEND Governance harness integration

- PR #246 added master spec §9.13 U→§9.x map and §14.4 closeout order amendments.
- PR #247 executed Layer C closeout for PR #246: task-index → current → decision-log → START-HERE refresh.
- PR #248 cleaned stale refresh state and aligned §16.1 authority file wording.
- PR #245 landed docs/memory after PR #248; therefore a future closeout refresh should reconcile authority-doc anchor drift.
- The former 5漏洞修订 remains conceptually integrated; vNext should not duplicate it as if missing.
- Cross-vendor audit should be planned before major risky gates; same-family audit can be a useful intermediate layer but not the strong gate.

### §13.3.1 Governance harness source map

| Layer | PR | Current state | vNext treatment |
|---|---|---|---|
| Layer A | PR #246 | frontmatter/anchor reduction concept landed | cite in §14 |
| Layer B | PR #246/#248 | refresh flow and checks exist | cite in post-flight |
| Layer C | PR #247 | closeout writeback order executed | hard-lock in §14.4 |
| Layer D | PR #246/#248 | forced refresh interval concept recorded | keep as governance check |
| Layer memory | PR #245 | docs/memory shared path exists | add §14.6 |

---

# §14-NEW Pre-flight Governance

> Replaces original §14. This section is the operating safety rail for every new wave. It captures hard rules from current authority, the PR #246/#247/#248 governance harness, and the PR #245 memory graph land.

## §14.1-NEW Governance hard rules

1. Any code-bearing migration, runtime, worker, or frontend implementation must start from a new dispatch and external audit.
2. Do not create or modify worker/package surfaces; app/service surfaces only when the current dispatch explicitly authorizes their paths.
3. Active product lane max remains 3; Authority writer max remains 1.
4. PlatformResult enum, WorkerReceipt schema, and Trust Trace DTO shape must not change without new dispatch and external audit.
5. Top-level governance files are not touched casually; only explicit governance dispatch may change them.
6. write_enabled remains false unless the true_vault_write upgrade path is explicitly approved.
7. 5 overflow lanes stay Hold and must not be bundled into one unlock.

## §14.2-AMEND Every wave starts with 5+1 steps

### Step 0 — Prerequisite Check (NEW)

| Substep | Action | Receipt |
|---|---|---|
| 0-A | Read current authority TL;DR | main anchor / Active / Authority writer / wave state / write boundary |
| 0-B | Read lane registry | Active count / Review count / Done rows / candidate state |
| 0-C | Read decision trail | latest relevant D entries and missing entries |
| 0-D | Read memory index | cross-vendor instinct count and relevant lessons |
| 0-E | Compare prompt-written numbers | if PR/SHA/count drift, write drift receipt before producing spec |

### Steps 1-5 — unchanged flow with stronger gates

| Step | Action | Guard |
|---|---|---|
| Step 1 | Register lane if needed | respect product lane max and avoid saturating slots |
| Step 2 | Decision entry if authority-changing | single writer only; no parallel authority edits |
| Step 3 | Hermes pre-flight external audit | vendor-diversified when risky or boundary-bearing |
| Step 4 | Commander prompt | CC1/GPT Pro spec source; explicit allowed paths and stop-line |
| Step 5 | Codex long-runner implementation | only after Step 0-4 pass; no implicit scope expansion |

## §14.3-AMEND If pre-flight fails

| Failure | Handling |
|---|---|
| lane full | wait or close an Active lane before starting |
| authority writer conflict | serialize; never parallel-write authority surfaces |
| external audit reject | repair spec and re-audit before dispatch |
| prerequisite drift | use refreshed truth; never copy stale prompt numbers |
| boundary ambiguity | write explicit candidate TODO, do not implement |
| memory conflict | prefer docs/memory INDEX and mark stale sibling wording |

## §14.4-AMEND Post-flight (V-PASS stage)

1. CC1 audit or assigned audit agent reviews actual diff against dispatch.
2. Human V-PASS reviews browser-visible or document-visible result.
3. Choose merge / amend / root-cause route based on evidence.
4. Write closeout receipt only after evidence is checked.
5. If authority writeback is in scope, use the established order: lane registry → current state → decision trail → START-HERE refresh flow.
6. If latest merged PR reaches forced refresh threshold, run W6K refresh sprint and advance threshold.
7. After PR #245-type content land, verify whether authority-doc anchor needs a closeout refresh.

## §14.5-NEW 4-agent v3 SOP

| Decision | Default | Why |
|---|---|---|
| Routing first question | Should this be GPT Pro? | Use GPT Pro for schema-heavy one-shot narrative/spec production. |
| Local sustained execution | Use Codex | Use Codex for repo operations, tests, multiple commits, long-runner implementation. |
| Conductor/auditor | Use CC0/CC1 | Use Claude Code for routing, spec review, audit, and final user-facing synthesis. |
| Independent critique | Use Hermes | Use Hermes for pre-flight or strong external audit, especially boundary-bearing tasks. |
| Double review | CC0 + CC1 | Use double Opus review for major PR/spec/prompt, but do not call it cross-vendor. |
| Strong gate | cross-vendor | Use at least one independent vendor path for high-risk/boundary decisions. |

### §14.5.1 Audit layer vocabulary

| Layer | Meaning | Allowed verdict use |
|---|---|---|
| Layer 1 | single agent self-audit | smoke only |
| Layer 1.5 | second reviewer in same family or subagent | useful catch, not strong gate (was "Layer 2" in non-canonical usage) |
| Layer 2 | cross-vendor external audit (Codex / Hermes / GPT Pro) | stronger pre-flight / risky gate (canonical naming per instinct §3 #16) |
| Layer 3 | human ultrathink final review | final merge posture |

## §14.6-NEW Memory integration

### §14.6.1 Current memory truth

| Bucket | Count | IDs |
|---|---|---|
| Lessons | 7 | L-AUTHORITY-DRIFT, L-CANDIDATE-PROMOTION, L-RUNTIME-APPROVAL-DRIFT, L-MIGRATION-DRIFT, L-PRODUCT-CLOSURE-MISTAKE, L-OVEROBJECTIFICATION, L-HANDOFF-OVERLONG |
| Feedback | 5 | F-STRONG-VISUAL-FIRST-CLASS, F-DIRECT-MERGE-OK, F-NOT-HEAVY-KM, F-SAFE-PARALLEL, F-DISPATCH-FROZEN-CORRECTION |
| Patterns | 5 | P-PROOF-PAIR-CANARY, P-OBJECTS-AFTER-PROOF, P-API-AS-WRITE-BOUNDARY, P-OVERFLOW-NOT-BLOCKER, P-DUAL-TRUTH-SEPARATION |

### §14.6.2 Required use before spec/dispatch

- Before citing state, scan L-AUTHORITY-DRIFT and L-CANDIDATE-PROMOTION.
- Before any runtime-adjacent wording, scan L-RUNTIME-APPROVAL-DRIFT.
- Before migration wording, scan L-MIGRATION-DRIFT.
- Before expanding entities, scan L-OVEROBJECTIFICATION and P-OBJECTS-AFTER-PROOF.
- Before dispatch packaging, scan F-SAFE-PARALLEL and P-OVERFLOW-NOT-BLOCKER.
- Before handoff, scan L-HANDOFF-OVERLONG.
- Before writing cross-vendor spec, cite docs/memory INDEX count 17 and flag README stale count if relevant.

### §14.6.3 Memory drift handling

| Observed drift | Truth source | Handling |
|---|---|---|
| README says 16 | INDEX says 17 | use INDEX, add README wording follow-up |
| PR title says 16 | PR body + INDEX list 17 | use file list/INDEX |
| local-only memory mentions more | docs/memory is shared path for this spec | do not cite local-only memory as authority |

## §14.7-NEW Global skill / closure rule integration

- Visual-related waves must run a 5-gate aesthetic review before final V-PASS.
- Every session closeout should leave a short executable handoff, not a transcript dump.
- These rules should be mirrored into repository-readable docs before they are cited as cross-vendor authority.
- Until mirrored, reference them as operating discipline, not as current authority documents.
- W2C and W1B should include aesthetic gate language in their commander prompts.

---

# §16.2-NEW Candidate / Authority Upgrade Path

> Replaces original §16.2. The purpose is to make every unlock path explicit, serialized, and externally audited. This section does not approve any unlock; it only describes what would be required. Same-family review can help but does not replace cross-vendor audit for risky gates.

| Unlock item | Authority path | Required steps | Audit requirement |
|---|---|---|---|
| single-point graph library choice | OpenDesign reuse strategy v2 candidate | spec PR → external audit → merge → W1B dispatch | Hermes or equivalent independent review required |
| Whisper local acceleration | runtime_tools authority upgrade | spec PR → benchmark evidence → external audit → merge | cross-vendor required; no silent runtime start |
| true vault write | true_vault_write authority upgrade | spec PR → full 7-stage pipeline evidence → external audit → double review → human V-PASS | strictest path; never bundled |
| browser automation | browser_automation authority upgrade | spec PR → explicit use case → external audit → merge | independent audit required |
| DB vNext migration | dbvnext_migration authority upgrade | spec PR → backup/rollback plan → external audit → double review → merge | migration-specific audit required |
| full signal workbench | full_signal_workbench authority upgrade | spec PR → product closure evidence → external audit → merge | cross-vendor plus human product review |

## §16.2.1 Absolute rules

- Never skip authority upgrade path and jump directly to implementation.
- Never treat same-family review as cross-vendor strong gate.
- Never bundle multiple overflow lane unlocks in one PR.
- Every upgrade path must have its own spec, audit, closeout, and human V-PASS.
- Every upgrade path must preserve existing write boundary until explicitly changed by authority.
- Candidate wording must stay visibly candidate until promotion is recorded in current authority and decision trail.

## §16.2.2 Stop-line triggers

| Trigger | Action |
|---|---|
| A prompt says a lane is already approved | verify current authority and decision trail; if absent, stop |
| A worker proposes new state/schema fields | stop unless dispatch explicitly permits |
| A visual implementation imports heavy external stack | stop and route through visual upgrade audit |
| A command would write outside preview/dry-run boundary | stop and verify true_vault_write path |
| A runtime tool is invoked | stop unless runtime_tools path is approved |
| A stale PR/SHA/count is detected | write prerequisite drift receipt before continuing |

---

# Appendix A — vNext insertion checklist

- [ ] Move §2-NEW into master spec and remove old PR #243-only table.
- [ ] Amend §8 with land-status table and §8.6 launch guard.
- [ ] Replace §13 with new wave list and 4-agent matrix.
- [ ] Replace §14 with Step 0 + 5+1 flow + memory integration.
- [ ] Replace §16.2 with serialized upgrade path table.
- [ ] Amend §15.2 priority row to mark W1A/W2D/W6K done/partial done.
- [ ] Amend §19 references to include PR #244/#245/#246/#247/#248 and docs/memory.
- [ ] Do not renumber ToC unless CC0 explicitly chooses to create a full vNext copy.

# Appendix B — Source reference rows for §19.3

| Reference | Status | Use in vNext |
|---|---|---|
| PR #243 | merged | capture-station physical baseline |
| PR #244 | merged | doc baseline + storage + status words |
| PR #246 | merged | governance harness + retrospective + §9.13 |
| PR #247 | merged | Layer C closeout for PR #246 |
| PR #248 | merged | stale cleanup + L-1/L-2/L-4 |
| PR #245 | merged after #248 | cross-vendor memory graph, lineage head |
| docs/memory/INDEX.md | current authority | memory item count and IDs |
| docs/memory/README.md | current authority but stale wording | README count follow-up |

---

# Appendix F — vNext Integration Guard Cards

> 本 appendix 是给 CC0/CC1 接管时用的 guard card。它不是新章节编号建议，只是把 D3 正文里的边界、wave、surface、memory 应用点拆成可扫读卡片，降低 rebase 时漏掉 PR #245 / PR #248 drift 的概率。

## A.1 Authority-doc anchor drift guard

- Trigger: 任何段落写 “main HEAD / latest baseline / current anchor”。
- Read source: `docs/current.md`, `docs/00-START-HERE.md`, PR lineage metadata, D1 §0 receipts。
- Draft action: 同时写出 authority-doc anchor 与 PR lineage fact，不把二者混成一个值。
- Safe wording: “authority-doc anchor still records `c802de4`; PR lineage shows PR #245 merged later as `6dd27d7`.”
- Unsafe wording: “current docs are fully refreshed after PR #245.”
- Follow-up owner: authority-writer closeout lane, not this candidate draft。

## A.2 Memory count drift guard

- Trigger: 任何段落写 “16 memory / 17 memory / U16 ingest”。
- Read source: `docs/memory/INDEX.md` count and table, plus README wording。
- Draft action: 采用 INDEX=17；README=stale follow-up。
- Safe wording: “17 table items; README count stale.”
- Unsafe wording: “the memory batch is 16.”
- Follow-up owner: W6K refresh or memory-maintenance lane。

## A.3 Status-word guard

- Trigger: 任何 frontmatter `status:` 或正文状态总结。
- Allowed set: current authority / promoted addendum / candidate north-star / reference storage。
- Draft action: master spec vNext stays candidate north-star。
- Safe wording: “candidate north-star; not authority.”
- Unsafe wording: “formal base / approved product authority / final runtime baseline.”
- Follow-up owner: PRD/SRD promotion lane only after explicit decision。

## A.4 Overflow lane guard

- Trigger: 任何涉及 vault write, runtime tools, browser automation, migration, full signal workbench 的句子。
- Draft action: 明确 Hold；只给升级路径，不给开工许可。
- Safe wording: “single dedicated authority upgrade PR per lane.”
- Unsafe wording: “bundle unlock all five lanes.”
- Follow-up owner: per-lane spec + external audit + human pass。

## A.5 Same-family audit guard

- Trigger: 任何段落写 "Layer 1.5 / Layer 2 / self-audit / double review"。
- Draft action: 明确 same-family review (Layer 1.5) is useful but not cross-vendor (Layer 2)。
- Safe wording: "double Opus (Layer 1.5) catches many issues, but strong gate still needs Layer 2 cross-vendor path."
- Unsafe wording: "double same-family review (Layer 1.5) equals Layer 2 cross-vendor audit."
- Follow-up owner: CC0 review plan。

## A.6 Candidate-source guard

- Trigger: 引用 16 ZIP / U1-U16 / post-frozen research / thin shells。
- Draft action: 标明 candidate/reference layer，不升级成 current authority。
- Safe wording: “storage or candidate input for later dispatch.”
- Unsafe wording: “source has already approved execution.”
- Follow-up owner: per-wave spec author。

## A.7 Deliverable placement guard

- Trigger: CC0 准备把 D3 移入 master spec vNext。
- Draft action: D3 是 section-by-section draft；不要直接覆盖整份 master spec unless CC0 合并 PR243 preserved sections。
- Safe wording: “replace or amend listed sections only.”
- Unsafe wording: “D3 alone is the full master spec.”
- Follow-up owner: authority writer + reviewer pair。

---

# Appendix G — Wave Start Cards (for §13.1 / §14)

## B.1 W1A — untracked batch land

- Current status: ✅ landed via PR #244 body scope。
- Primary evidence: 16 ZIP storage, START-HERE, master spec visibility, status-word lock。
- Rebase action: mark done; do not keep as pending Wave。
- Pre-flight delta: none for new execution; only future reference-storage hygiene。
- Boundary: reference storage is searchable input, not execution approval。
- Closeout risk: stale statistics must be refreshed by authority closeout, not copied blindly。

## B.2 W2D — U16 memory ingest

- Current status: ✅ landed via PR #245 lineage。
- Primary evidence: `docs/memory/INDEX.md` batch_count 17 + 19 changed files in PR #245。
- Rebase action: change §9.3 / §12.4 starting point from zero to 17。
- Pre-flight delta: future memory expansion starts from 17 table items and README stale fix。
- Boundary: memory items are current-authority instincts, not a license to rewrite other authority docs。
- Closeout risk: authority-doc anchor still stale after PR #245。

## B.3 W6K — governance and collaboration sediment

- Current status: ✅ landed across PR #246 / #247 / #248, with PR #245 memory as sibling foundation。
- Primary evidence: retrospective, handoff template, START-HERE updates, master spec patches, refresh tool fixes。
- Rebase action: rewrite §14 as pre-flight governance vNext, not as future backlog only。
- Pre-flight delta: add Step 0 prerequisite receipts before wave routing。
- Boundary: governance harness does not approve runtime or migration work。
- Closeout risk: some global-rule material remains outside repository mirror; keep as TODO, not citation source。

## B.4 W2C — PF-C4-02 true data wiring

- Current status: 🚀 ready to launch after governance rebase。
- Primary evidence: PR #243 physical capture-station shell + §8 surface mapping。
- Rebase action: keep as next P0, but require §0.5 receipts and §14 gates first。
- Pre-flight delta: use GPT Pro for schema / narrative spec, Codex for long-run implementation, CC1 for commander/audit, Hermes for external pre-flight。
- Boundary: no true vault write, no browser automation, no runtime tools unless separate upgrade path already passed。
- Closeout risk: 13 surfaces are static shell; true data wiring must not claim full product closure。

## B.5 W1B — PF-C4-EXT remaining honest TODO

- Current status: 🚀 ready, dependent on OpenDesign reuse strategy decision。
- Primary evidence: PR #243 honest TODO list: thumbnail, graph, timeline hover, error path。
- Rebase action: keep TODO as visible, not failure。
- Pre-flight delta: external audit must validate library / self-rolled strategy before any frontend implementation。
- Boundary: no new heavy UI dependency family without explicit reject-list handling。
- Closeout risk: “D3” label may be mistaken for npm package; D3 here means self-rolled graph work unless upgraded。

## B.6 W3E — 80-pack residual clusters

- Current status: ⏳ pending, cluster-specific。
- Primary evidence: U9 dispatch catalog and master spec §13 routing。
- Rebase action: keep independent; do not let it block W2C。
- Pre-flight delta: each cluster needs scope, allowed paths, validation, and closeout receipt。
- Boundary: candidate prompt catalog is not execution approval。
- Closeout risk: packed PR topology can hide scope drift; require explicit cluster ledger。

## B.7 W4F — Phase 2 ASR / runtime tools

- Current status: 🔒 Hold through runtime_tools lane。
- Primary evidence: current boundaries and §16 upgrade path。
- Rebase action: leave future candidate, not ready lane。
- Pre-flight delta: benchmark evidence + authority upgrade PR required before implementation。
- Boundary: ASR planning does not open audio runtime。
- Closeout risk: Apple Silicon optimization docs are reference input, not approval。

## B.8 W4G — Rewrite pipeline

- Current status: 🔒 Hold until upstream capture / transcript path is safe。
- Primary evidence: master spec §6 candidate pipeline and cost / style inventory。
- Rebase action: preserve design inventory; no immediate replace needed。
- Pre-flight delta: model router, style skill, cost ledger must be spec-first。
- Boundary: no vault commit side effects and no authority promotion of generated rewrites。
- Closeout risk: style library can become heavy knowledge management if proof loop not established。

## B.9 W5H — source matrix expansion

- Current status: 🔒 Hold for runtime/source tool unlock。
- Primary evidence: §4 source adapter matrix and vendor diversification risk。
- Rebase action: preserve as future source strategy。
- Pre-flight delta: each vendor needs separate risk posture and adapter contract。
- Boundary: no platform scraping/runtime execution without dedicated approval path。
- Closeout risk: single-vendor lock-in and cease-and-desist drift。

## B.10 W5I — comments / nested reply subsystem

- Current status: 🔒 Hold pending source matrix maturity。
- Primary evidence: §4.4 comments subsystem candidate design。
- Rebase action: preserve candidate algorithms and schema ideas as inventory。
- Pre-flight delta: source-vendor evidence and data-shape contract first。
- Boundary: no comment scraping execution implied。
- Closeout risk: over-objectification before proof loop。

## B.11 W6J — true vault commit

- Current status: 🔒 Hold through true_vault_write lane。
- Primary evidence: write_enabled=False and §16.2 upgrade path。
- Rebase action: keep as long-term final close loop, not near-term W2C scope。
- Pre-flight delta: full seven-stage pipeline evidence + frontmatter contract + independent audit。
- Boundary: preview / dry-run / disabled UI are not true write。
- Closeout risk: user trust damage if preview semantics drift into write semantics。

---

# Appendix C — 13 Surface Rebase Cards (for §8)

## C.1 App Shell

- Land status: ✅ static shell in PR #243。
- vNext stance: keep as foundation, not rewrite。
- W2C need: route data into global station state without expanding authority scope。
- Visual need: keep operator workstation hierarchy。
- Boundary: no package strategy escalation。

## C.2 URL Bar

- Land status: ✅ static/input surface。
- vNext stance: amend mapping with PR #243 tag。
- W2C need: connect discover flow under existing capture-scope gate。
- Visual need: risk prompt and validation feedback must be visible but not noisy。
- Boundary: recommendation or keyword signal still cannot directly create capture。

## C.3 Live Metadata

- Land status: ✅ static panel。
- vNext stance: amend with real-data pending tag。
- W2C need: metadata loading, degraded state, stale state, and source confidence display。
- Visual need: differentiate “observed” vs “predicted” fields。
- Boundary: metadata evidence is not media/runtime evidence。

## C.4 Capture Scope

- Land status: ✅ static panel。
- vNext stance: preserve capture gate as a hard UX contract。
- W2C need: scope explanation, denied path, operator override notes。
- Visual need: hard gate should feel protective, not generic admin form validation。
- Boundary: no silent expansion of capture types。

## C.5 Trust Trace

- Land status: ✅ shell with honest TODOs。
- vNext stance: keep graph/timeline/error-path as W1B or W2C-adjacent work, not pretend done。
- W2C need: receipt/evidence rows first, graph later if path approved。
- Visual need: trace must show provenance and transformation chain。
- Boundary: no Trust Trace DTO shape change without explicit dispatch。

## C.6 Vault Preview

- Land status: ✅ static preview / dry-run family foundation。
- vNext stance: keep preview as safe intermediate proof。
- W2C need: render deterministic frontmatter preview using existing bridge contract only。
- Visual need: strong label that preview is not write。
- Boundary: true vault write remains Hold。

## C.7 Vault Commit

- Land status: ✅ disabled/shell semantics。
- vNext stance: preserve disabled gate until W6J path。
- W2C need: explain blocked reason and next authority path。
- Visual need: disabled controls must still teach the pipeline。
- Boundary: no side-effecting commit。

## C.8 Topic Card Lite

- Land status: ✅ static card surface。
- vNext stance: use as proof-pair canary with preview and handoff。
- W2C need: source metadata, hypothesis hint, and evidence badge mapping。
- Visual need: card density must remain readable in mixed CJK/Latin content。
- Boundary: no heavy object graph before proof loop。

## C.9 Topic Card Vault

- Land status: ✅ bounded candidate / static shell lineage。
- vNext stance: keep as visual/storage bridge candidate。
- W2C need: clear separation between vault-ready preview and vault-write approval。
- Visual need: stronger hierarchy for title, metadata, frontmatter, evidence。
- Boundary: no write path implied。

## C.10 Signal Hypothesis

- Land status: ✅ static shell。
- vNext stance: preserve as planning/intelligence surface。
- W2C need: show confidence, rationale, and source evidence without making it a capture creator。
- Visual need: hypothesis language should be tentative and traceable。
- Boundary: hypothesis cannot bypass capture gate。

## C.11 Capture Plan

- Land status: ✅ static shell。
- vNext stance: next true workflow target after metadata and scope wiring。
- W2C need: plan states, blocked states, operator acknowledgement。
- Visual need: “plan” and “execution” must be visually separate。
- Boundary: plan existence is not runtime execution。

## C.12 Density Spec

- Land status: ✅ token/density surface。
- vNext stance: use as visual guard for all W2C amendments。
- W2C need: prevent random spacing and dashboard drift。
- Visual need: apply 5 Gate style review before UI merge。
- Boundary: visual spec does not approve new dependency family。

## C.13 Type Spec

- Land status: ✅ typography surface。
- vNext stance: keep as CJK/Latin readability anchor。
- W2C need: all evidence and status labels should remain legible under long source titles。
- Visual need: avoid all-caps generic dashboard energy。
- Boundary: no hardcoded color or font escape outside approved token layer。

---

# Appendix D — 17 Memory Application Cards (for §14.6)

## D.1 L-AUTHORITY-DRIFT

- Rule cue: candidate, research, or chat summary must not become authority by repetition。
- Apply before: any D2 replacement plan and D3 governance section。
- Rebase note: authority-doc anchor drift after PR #245 is a concrete example。
- Failure mode: closing the drift verbally but not in authority closeout。

## D.2 L-CANDIDATE-PROMOTION

- Rule cue: frontmatter status and body claim must match。
- Apply before: master spec vNext frontmatter and §0 boundary。
- Rebase note: vNext remains candidate north-star。
- Failure mode: thin shell or master spec treated as formal PRD/SRD base。

## D.3 L-RUNTIME-APPROVAL-DRIFT

- Rule cue: bounded evidence and placeholder route do not approve live runtime。
- Apply before: W4F/W5H/W2C planning。
- Rebase note: W2C cannot smuggle runtime through visual/data wiring。
- Failure mode: “observed route” wording turns into runtime unlock。

## D.4 L-MIGRATION-DRIFT

- Rule cue: schema planning needs independent migration path。
- Apply before: ASR transcript schema and DB vNext mentions。
- Rebase note: §16.2 keeps migration behind dedicated upgrade route。
- Failure mode: adding table ideas to product plan as if schema is approved。

## D.5 L-PRODUCT-CLOSURE-MISTAKE

- Rule cue: engineering closure is not product closure。
- Apply before: any “landed / done” word in §13。
- Rebase note: 13 surfaces landed as static shell, not full user loop。
- Failure mode: “PR merged” equals “operator workflow complete”。

## D.6 L-OVEROBJECTIFICATION

- Rule cue: entity graph before proof loop creates knowledge-management bloat。
- Apply before: memory graph, source matrix, comments subsystem。
- Rebase note: start from proof-pair canary and real data wiring。
- Failure mode: W3E object expansion blocks W2C loop。

## D.7 L-HANDOFF-OVERLONG

- Rule cue: concise executable handoff beats transcript dump。
- Apply before: §14 post-flight and closeout receipts。
- Rebase note: D3 itself is section draft, not raw session log。
- Failure mode: hiding decisions inside long narrative without gate cards。

## D.8 F-STRONG-VISUAL-FIRST-CLASS

- Rule cue: visual quality is a first-class product axis。
- Apply before: W2C, W1B, density/type changes。
- Rebase note: §8.6 points W2C to surface cards and 5 Gate review。
- Failure mode: data wiring passes technically but loses workstation aesthetic。

## D.9 F-DIRECT-MERGE-OK

- Rule cue: direct merge is acceptable for bounded docs-only cleanup, not cross-boundary work。
- Apply before: PR review and V-PASS planning。
- Rebase note: authority upgrades still require explicit external audit and human pass。
- Failure mode: using direct merge preference to bypass red lines。

## D.10 F-NOT-HEAVY-KM

- Rule cue: short entry + single truth beats second knowledge base。
- Apply before: memory and governance design。
- Rebase note: use `docs/memory/INDEX.md` as entry, not duplicate full atlas。
- Failure mode: creating parallel memory mirrors with conflicting counts。

## D.11 F-SAFE-PARALLEL

- Rule cue: max horsepower does not mean slot saturation。
- Apply before: W2C/W1B/W3E parallel plan。
- Rebase note: product lane count remains 0/3 now, but every new active lane still needs registry。
- Failure mode: opening three waves without clear conflict domains。

## D.12 F-DISPATCH-FROZEN-CORRECTION

- Rule cue: historical ledger is immutable; corrections append, not rewrite。
- Apply before: stale inventory and §19 references。
- Rebase note: PR #245 drift should be appended as closeout note, not retroactively hidden。
- Failure mode: editing history to make lineage look clean。

## D.13 P-PROOF-PAIR-CANARY

- Rule cue: pair a small visual proof with safe preview / handoff evidence。
- Apply before: W2C first implementation slice。
- Rebase note: Topic Card Lite + Vault Preview + handoff card are likely canary pair。
- Failure mode: jumping to full pipeline before canary proves value。

## D.14 P-OBJECTS-AFTER-PROOF

- Rule cue: object model expansion after user-visible proof。
- Apply before: entity and graph roadmaps。
- Rebase note: §9.3 starts from 17 memory items but should not force graph expansion first。
- Failure mode: building object lattice while capture loop remains static。

## D.15 P-API-AS-WRITE-BOUNDARY

- Rule cue: thin API is write boundary; UI does not create side effects directly。
- Apply before: Vault Preview / Commit / Capture Plan sections。
- Rebase note: W2C wiring must respect Bridge/Vault contracts。
- Failure mode: UI control implies write despite backend disabled state。

## D.16 P-OVERFLOW-NOT-BLOCKER

- Rule cue: Hold lanes do not block product main, but also do not open silently。
- Apply before: §13 prioritization and §16.2 upgrade table。
- Rebase note: W2C can proceed without runtime/vault unlock。
- Failure mode: claiming product blocked until all five lanes open。

## D.17 P-DUAL-TRUTH-SEPARATION

- Rule cue: storage archive, live repository fact, and local operational truth are separate。
- Apply before: D1 receipts and D2 rebase plan。
- Rebase note: authority-doc anchor and PR lineage differ; report both。
- Failure mode: flattening all truth sources into one stale number。

---

# Appendix E — TODO Placeholder Bank

> These TODOs are intentionally copy-safe for CC0/CC1 review. They preserve uncertainty without pretending authority.

- `<!-- TODO: verify whether PR #245 closeout should refresh docs/current.md and START-HERE anchor in a separate authority lane, leave to CC0 follow-up -->`
- `<!-- TODO: reconcile docs/memory README count with INDEX=17, leave to memory-maintenance follow-up -->`
- `<!-- TODO: decide whether governance harness Layer A-D needs standalone §13.4 or remains inline in §13.3, leave to CC0 review -->`
- `<!-- TODO: decide whether external audit SOP should name Hermes only or support multiple independent reviewers, leave to governance review -->`
- `<!-- TODO: decide whether W2C commander prompt should include D3 Appendix B/C cards verbatim or summarize them, leave to commander author -->`
- `<!-- TODO: verify next_forced_refresh_pr before closeout writeback, leave to authority-writer lane -->`
- `<!-- TODO: if PRD/SRD promotion occurs later, split §1-§9 absorption from §13-§18 governance manual, leave to promotion lane -->`
- `<!-- TODO: if OpenDesign strategy changes, re-evaluate W1B graph/timeline/error-path dependency stance, leave to visual architecture lane -->`
- `<!-- TODO: if cross-vendor memory mirror lands later, update §14.6 source list without citing local-only paths, leave to W6K follow-up -->`
- `<!-- TODO: if W2C lands, update §8 surface status tags from static shell to true-data-wired with evidence, leave to W2C closeout -->`

---

# Self-flag

- ⚠️ §13.3 governance harness details are summarized at layer level; CC0 should decide whether to split them into a separate §13.4 in the full vNext file.
- ⚠️ §14.7 intentionally avoids citing local-only rule paths; if CC0 wants those rules as cross-vendor authority, mirror them into repository docs first.
- ⚠️ §16.2 uses high-level audit path language; CC0 may add a dedicated SOP table if Hermes/cross-vendor process needs stricter operational wording.
- ⚠️ The authority-doc anchor drift after PR #245 is not resolved here; this draft only makes it impossible to miss.

> **File path**: `docs/research/post-frozen/2026-05-08/W1-master-spec-rebase/03-master-spec-vnext-draft-section-by-section.md`
> **Status**: candidate / vNext-section-draft / not-authority
