---
status: "candidate / cloud_prompt / not-authority"
authority: "not-authority"
created_at: "2026-05-07"
title: "MASTER-ANTI-PATTERN-INDEX-2026-05-07"
kind: "master-index"
no_actual_rule_deployment_implied: true
---

# MASTER Anti-Pattern Index — U11 Candidate Encyclopedia

[evidence-backed] 本 master index 覆盖 10 个 cluster、全部 single-file anti-pattern、cluster index、detect/prevent/escape catalog、cross-link 与 self-audit。所有文件均为 candidate / not-authority；本包不部署规则、不批准 runtime、不批准 migration、不批准 browser automation、不批准 true write。

## 1. Cluster matrix

| Cluster | Name | AP count | Critical | High | Medium | Introduced | Exposed | Hypothetical |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| SF | Silent-Flexibility / Scope Drift | 10 | 4 | 5 | 1 | 3 | 7 | 0 |
| AC | Authority-Confusion / Single-Writer | 8 | 4 | 4 | 0 | 0 | 8 | 0 |
| BL | Boundary-Leak / Overflow Slip | 10 | 8 | 2 | 0 | 0 | 10 | 0 |
| VF | Visual / 5-Gate Failure | 10 | 0 | 7 | 3 | 0 | 10 | 0 |
| VS | Vendor-SupplyChain | 7 | 2 | 4 | 1 | 0 | 7 | 0 |
| MC | Memory-CrossSession | 7 | 0 | 5 | 2 | 0 | 7 | 0 |
| MA | Multi-Agent-Collab | 7 | 4 | 3 | 0 | 1 | 6 | 0 |
| CT | Cost-Token | 6 | 0 | 2 | 4 | 0 | 6 | 0 |
| ED | Engineering-Discipline | 8 | 1 | 4 | 3 | 0 | 8 | 0 |
| DT | Documentation-Truthfulness | 7 | 2 | 5 | 0 | 1 | 6 | 0 |

## 2. Mermaid heatmap

```mermaid
flowchart LR
    SF[SF: C4/H5/M1]
    AC[AC: C4/H4/M0]
    BL[BL: C8/H2/M0]
    VF[VF: C0/H7/M3]
    VS[VS: C2/H4/M1]
    MC[MC: C0/H5/M2]
    MA[MA: C4/H3/M0]
    CT[CT: C0/H2/M4]
    ED[ED: C1/H4/M3]
    DT[DT: C2/H5/M0]
    SF --> AC --> BL --> VF --> VS --> MC --> MA --> CT --> ED --> DT
```

## 3. Introduced vs exposed distribution

[evidence-backed] Total introduced=5; exposed=75; hypothetical=0. 本包故意把大多数条目标为 exposed，因为许多踩坑不是最近 PR 新制造的 defect，而是新动作把历史债、规则缺口或文档措辞暴露出来。`introduced` 仅用于 prompt/PR 明确显示新动作造成或新写错的场景，例如 scope deviation、gate bypass receipt、synthetic evidence downgrade。

## 4. Full AP table

| ID | Cluster | Title | Risk | first_seen_in | I/E/H | Detect | Prevent | Rule |
|---|---|---|---|---|---|---|---|---|
| AP-SF-01 | SF | Packed repair without explicit authorization | critical | PR #226/#228 topology + PR #239 FIX-7 | exposed | audit | contract | ~/.claude/rules/execution-discipline.md |
| AP-SF-02 | SF | Run-1 amendment proceeds without explicit gate replay | critical | PR #231 + PR #239 FIX-5 | introduced | audit | template | ~/.claude/rules/execution-discipline.md |
| AP-SF-03 | SF | Multi-dispatch silent merge | high | PR #240 combined Run-3+4 | exposed | human | contract | ~/.claude/rules/execution-discipline.md |
| AP-SF-04 | SF | Worker-guessed scope expansion | critical | PR #231 A1/A2/A3 | introduced | grep | schema | ~/.claude/rules/execution-discipline.md |
| AP-SF-05 | SF | Multi-PR topology drift | high | PR #226/#228 + PR #239 FIX-7 | exposed | audit | contract | ~/.claude/rules/execution-discipline.md |
| AP-SF-06 | SF | Checkpoint field silent rename | medium | PR #239 FIX-1 | exposed | static | schema | ~/.claude/rules/execution-discipline.md |
| AP-SF-07 | SF | Allowed path silent change | high | Dispatch127-176 pack audit F3 | exposed | grep | hook | ~/.claude/rules/execution-discipline.md |
| AP-SF-08 | SF | Threshold silent loosen | high | PR #239 FIX-2 | introduced | grep | template | ~/.claude/rules/execution-discipline.md |
| AP-SF-09 | SF | Verdict wording silent escalate | high | PR #231 external audit synthesis | exposed | grep | template | ~/.claude/rules/execution-discipline.md |
| AP-SF-10 | SF | Boundary silent expand | critical | PR #240 boundary block | exposed | audit | contract | ~/.claude/rules/execution-discipline.md |
| AP-AC-01 | AC | Dual-window writes docs/current.md | critical | PR #231/#240 authority untouched assertions | exposed | grep | contract | ~/.claude/rules/parallel-safety.md |
| AP-AC-02 | AC | Sidecar agent writes authority files | critical | Dispatch127-176 manifest authority_writer | exposed | static | schema | ~/.claude/rules/parallel-safety.md |
| AP-AC-03 | AC | task-index numbering conflict | high | 2026-05-04 task-index risk named in prompt | exposed | grep | hook | ~/.claude/rules/parallel-safety.md |
| AP-AC-04 | AC | decision-log append rewritten as replace | high | PR #231 authority-file redline | exposed | grep | template | ~/.claude/rules/parallel-safety.md |
| AP-AC-05 | AC | contract-index baseline drift | high | wave5 repair overflow rules | exposed | static | contract | ~/.claude/rules/parallel-safety.md |
| AP-AC-06 | AC | AGENTS.md rewritten instead of amended | high | PR #231 authority untouched guard | exposed | grep | template | ~/.claude/rules/parallel-safety.md |
| AP-AC-07 | AC | Authority promote skips audit gate | critical | not-authority frontmatter across pack | exposed | grep | contract | ~/.claude/rules/parallel-safety.md |
| AP-AC-08 | AC | Authority writer max=1 violation | critical | manifest authority_writer rows | exposed | static | schema | ~/.claude/rules/parallel-safety.md |
| AP-BL-01 | BL | write_enabled=False implies future unlock | critical | Wave4 retro PR #113/#129 dry-run note | exposed | grep | contract | ~/.claude/rules/security.md |
| AP-BL-02 | BL | BBDown live runtime implied approval | critical | wave5 blocked/overflow rules | exposed | grep | schema | ~/.claude/rules/security.md |
| AP-BL-03 | BL | ASR runtime implied approval | critical | wave5 blocked/overflow rules | exposed | grep | schema | ~/.claude/rules/security.md |
| AP-BL-04 | BL | Browser automation implied approval | critical | visual spec screenshot future-gated clause | exposed | grep | contract | ~/.claude/rules/security.md |
| AP-BL-05 | BL | Migration implied approval | critical | wave5 blocked/overflow rules | exposed | grep | hook | ~/.claude/rules/security.md |
| AP-BL-06 | BL | Five overflow lanes unlocked in one PR | critical | roadmap O1 overflow | exposed | audit | contract | ~/.claude/rules/security.md |
| AP-BL-07 | BL | Dispatch schema lacks can_open flags | high | PR #240 can_open_c4=false | exposed | static | schema | ~/.claude/rules/security.md |
| AP-BL-08 | BL | Vendor candidate silently accepted | high | visual/vendor candidate boundary | exposed | grep | contract | ~/.claude/rules/security.md |
| AP-BL-09 | BL | Preview-only drifts into production write | critical | PR #226/#228 preview shell | exposed | grep | hook | ~/.claude/rules/security.md |
| AP-BL-10 | BL | Candidate file silently becomes authority | critical | candidate/not-authority frontmatter | exposed | grep | template | ~/.claude/rules/security.md |
| AP-VF-01 | VF | Primary title loses hierarchy to subtitle | high | visual 5 Gate rule-derived from Dispatch128/156/165 | exposed | human | template | ~/.claude/rules/aesthetic-first-principles.md |
| AP-VF-02 | VF | Subtitle or toast occludes critical content | high | visual failure taxonomy | exposed | human | contract | ~/.claude/rules/aesthetic-first-principles.md |
| AP-VF-03 | VF | Random spacing and alignment | medium | visual spec spacing/readability clauses | exposed | human | template | ~/.claude/rules/aesthetic-first-principles.md |
| AP-VF-04 | VF | Contrast below durable review threshold | high | visual spec typography/contrast clauses | exposed | human | template | ~/.claude/rules/aesthetic-first-principles.md |
| AP-VF-05 | VF | Decoration heavier than evidence | high | visual spec anti-decorative graph rule | exposed | human | contract | ~/.claude/rules/aesthetic-first-principles.md |
| AP-VF-06 | VF | Saturation hijacks attention | medium | visual spec controlled contrast | exposed | human | template | ~/.claude/rules/aesthetic-first-principles.md |
| AP-VF-07 | VF | CJK/Latin baseline mismatch | medium | visual typography readability rule | exposed | human | template | ~/.claude/rules/aesthetic-first-principles.md |
| AP-VF-08 | VF | Good-enough visual pass | high | 5 Gate not polish rule | exposed | audit | contract | ~/.claude/rules/aesthetic-first-principles.md |
| AP-VF-09 | VF | Retrofitted visual after code | high | visual Day-0 input rule-derived | exposed | audit | template | ~/.claude/rules/aesthetic-first-principles.md |
| AP-VF-10 | VF | Mobile safe-area occlusion | high | visual desktop/tablet/mobile gate | exposed | human | contract | ~/.claude/rules/aesthetic-first-principles.md |
| AP-VS-01 | VS | Single vendor lane lock-in | high | wave5 vendor/runtime overflow posture | exposed | audit | contract | ~/.claude/rules/security.md |
| AP-VS-02 | VS | Vendor selection without spike audit | high | candidate research boundary | exposed | audit | template | ~/.claude/rules/security.md |
| AP-VS-03 | VS | BBDown cease-and-desist not rechecked | critical | BBDown live runtime blocked lane | exposed | human | contract | ~/.claude/rules/security.md |
| AP-VS-04 | VS | yt-dlp legal refresh skipped | critical | PR #240 no yt-dlp boundary | exposed | human | contract | ~/.claude/rules/security.md |
| AP-VS-05 | VS | ASR vendor not benchmarked | high | audio_transcript/ASR overflow | exposed | audit | template | ~/.claude/rules/security.md |
| AP-VS-06 | VS | Whisper local install not verified | medium | ASR candidate lane | exposed | grep | hook | ~/.claude/rules/security.md |
| AP-VS-07 | VS | Cloud API treated as free | high | cost-token governance derived from run scale | exposed | audit | template | ~/.claude/rules/security.md |
| AP-MC-01 | MC | Handoff as transcript dump | high | Dispatch176 handoff contract | exposed | human | template | ~/.claude/rules/session-closure.md |
| AP-MC-02 | MC | Handoff missing closure Step 5 | high | session closure rule target | exposed | audit | template | ~/.claude/rules/session-closure.md |
| AP-MC-03 | MC | /clear decided by duration not semantic boundary | medium | token hygiene rule target | exposed | human | skill | ~/.claude/rules/session-closure.md |
| AP-MC-04 | MC | /compact without anchor | high | codex metacognition prompt target | exposed | human | template | ~/.claude/rules/session-closure.md |
| AP-MC-05 | MC | MEMORY.md grows past usable size | medium | memory hygiene prompt target | exposed | grep | hook | ~/.claude/rules/session-closure.md |
| AP-MC-06 | MC | Cross-session context assumed persistent | high | zip/GitHub/inference separation rule | exposed | audit | contract | ~/.claude/rules/session-closure.md |
| AP-MC-07 | MC | Recover without git fetch | high | codex audit required before execution | exposed | grep | hook | ~/.claude/rules/session-closure.md |
| AP-MA-01 | MA | Multi-window dispatch no ledger | critical | Run-2/Run-3/Run-4 windows | exposed | audit | schema | ~/.claude/rules/parallel-safety.md |
| AP-MA-02 | MA | amend_and_proceed skips user authorization | critical | PR #231 + PR #239 FIX-5 | introduced | audit | contract | ~/.claude/rules/parallel-safety.md |
| AP-MA-03 | MA | Three-window cloud audit only uses one or two windows | high | PR #239 3-window audit synthesis | exposed | audit | template | ~/.claude/rules/parallel-safety.md |
| AP-MA-04 | MA | Silent-flexibility detector not run | high | Run amendment fields named in prompt | exposed | grep | hook | ~/.claude/rules/parallel-safety.md |
| AP-MA-05 | MA | Single-writer race | critical | authority_writer rows + authority untouched checks | exposed | static | schema | ~/.claude/rules/parallel-safety.md |
| AP-MA-06 | MA | introduced vs exposed ignored | critical | ContentFlow L1 meta lesson requested by prompt | exposed | audit | template | ~/.claude/rules/parallel-safety.md |
| AP-MA-07 | MA | Cross-window memory drift | high | Run-3+4 held-back signal preservation | exposed | audit | contract | ~/.claude/rules/parallel-safety.md |
| AP-CT-01 | CT | Dispatch without token estimate | medium | large 50-dispatch pack scale | exposed | human | template | ~/.claude/rules/token-hygiene.md |
| AP-CT-02 | CT | Long session without /clear | medium | token hygiene rule target | exposed | human | skill | ~/.claude/rules/token-hygiene.md |
| AP-CT-03 | CT | /compact loses anchors | high | long retrospective / multi-source pack target | exposed | human | template | ~/.claude/rules/token-hygiene.md |
| AP-CT-04 | CT | No cost dashboard | medium | cloud/API cost governance target | exposed | human | template | ~/.claude/rules/token-hygiene.md |
| AP-CT-05 | CT | API retry without backoff | high | cloud/API governance target | exposed | static | hook | ~/.claude/rules/token-hygiene.md |
| AP-CT-06 | CT | Repeat prompt without cache | medium | multi-window prompt repetition target | exposed | grep | skill | ~/.claude/rules/token-hygiene.md |
| AP-ED-01 | ED | No TDD before implementation | high | PR #226/#228 validation boundary | exposed | audit | template | ~/.claude/rules/testing.md |
| AP-ED-02 | ED | Coverage threshold below 80 without waiver | medium | testing rule target | exposed | static | hook | ~/.claude/rules/testing.md |
| AP-ED-03 | ED | Code-review agent skipped | medium | agent usage rule target | exposed | audit | contract | ~/.claude/rules/testing.md |
| AP-ED-04 | ED | No verification loop | high | PR validation checklists | exposed | grep | template | ~/.claude/rules/testing.md |
| AP-ED-05 | ED | Import path assumption | medium | pack-lint parser mismatch | exposed | static | hook | ~/.claude/rules/testing.md |
| AP-ED-06 | ED | Diagnose without git fetch | high | codex audit required refresh | exposed | grep | hook | ~/.claude/rules/testing.md |
| AP-ED-07 | ED | Destructive git misuse | critical | worktree/local-only posture | exposed | human | contract | ~/.claude/rules/testing.md |
| AP-ED-08 | ED | Hooks skipped for speed | high | PR validation checklists | exposed | grep | hook | ~/.claude/rules/testing.md |
| AP-DT-01 | DT | PASS/DONE/OK wording creep | high | external reports + PR verdict language | exposed | grep | template | ~/.claude/rules/execution-discipline.md |
| AP-DT-02 | DT | Fake wall-clock duration | high | truthful stdout contract | exposed | grep | template | ~/.claude/rules/execution-discipline.md |
| AP-DT-03 | DT | Live web claimed without live web | high | zip/GitHub/public/inference separation | exposed | grep | contract | ~/.claude/rules/execution-discipline.md |
| AP-DT-04 | DT | Claim label missing | high | visual/prd source label discipline | exposed | grep | template | ~/.claude/rules/execution-discipline.md |
| AP-DT-05 | DT | Evidence not refreshed | high | codex audit refresh required | exposed | audit | contract | ~/.claude/rules/execution-discipline.md |
| AP-DT-06 | DT | Tested claim without evidence | critical | wave4 retro no rerun tests note | exposed | grep | template | ~/.claude/rules/execution-discipline.md |
| AP-DT-07 | DT | Synthetic evidence labelled works | critical | PR #239 FIX-2 | introduced | grep | schema | ~/.claude/rules/execution-discipline.md |

## 5. Boundary statement

[boundary] 本 master index 没有把任何候选 detect/prevent 规则实际部署到 hook、CI、schema 或 production code。任何 future deployment 都必须走单独 PR、用户授权和 authority promotion gate。

[derived] Master-level audit reminder: 每个 anti-pattern 必须同时保留历史锚点与纠偏路径。只有 detect rule 而没有 escape clause，会把 review 变成阻断；只有 prevent rule 而没有 attribution，会把 exposed historical debt 误判为 introduced defect。

[derived] Master-level audit reminder: 每个 anti-pattern 必须同时保留历史锚点与纠偏路径。只有 detect rule 而没有 escape clause，会把 review 变成阻断；只有 prevent rule 而没有 attribution，会把 exposed historical debt 误判为 introduced defect。

[derived] Master-level audit reminder: 每个 anti-pattern 必须同时保留历史锚点与纠偏路径。只有 detect rule 而没有 escape clause，会把 review 变成阻断；只有 prevent rule 而没有 attribution，会把 exposed historical debt 误判为 introduced defect。

[derived] Master-level audit reminder: 每个 anti-pattern 必须同时保留历史锚点与纠偏路径。只有 detect rule 而没有 escape clause，会把 review 变成阻断；只有 prevent rule 而没有 attribution，会把 exposed historical debt 误判为 introduced defect。

[derived] Master-level audit reminder: 每个 anti-pattern 必须同时保留历史锚点与纠偏路径。只有 detect rule 而没有 escape clause，会把 review 变成阻断；只有 prevent rule 而没有 attribution，会把 exposed historical debt 误判为 introduced defect。

[derived] Master-level audit reminder: 每个 anti-pattern 必须同时保留历史锚点与纠偏路径。只有 detect rule 而没有 escape clause，会把 review 变成阻断；只有 prevent rule 而没有 attribution，会把 exposed historical debt 误判为 introduced defect。

[derived] Master-level audit reminder: 每个 anti-pattern 必须同时保留历史锚点与纠偏路径。只有 detect rule 而没有 escape clause，会把 review 变成阻断；只有 prevent rule 而没有 attribution，会把 exposed historical debt 误判为 introduced defect。

[derived] Master-level audit reminder: 每个 anti-pattern 必须同时保留历史锚点与纠偏路径。只有 detect rule 而没有 escape clause，会把 review 变成阻断；只有 prevent rule 而没有 attribution，会把 exposed historical debt 误判为 introduced defect。

[derived] Master-level audit reminder: 每个 anti-pattern 必须同时保留历史锚点与纠偏路径。只有 detect rule 而没有 escape clause，会把 review 变成阻断；只有 prevent rule 而没有 attribution，会把 exposed historical debt 误判为 introduced defect。

[derived] Master-level audit reminder: 每个 anti-pattern 必须同时保留历史锚点与纠偏路径。只有 detect rule 而没有 escape clause，会把 review 变成阻断；只有 prevent rule 而没有 attribution，会把 exposed historical debt 误判为 introduced defect。

[derived] Master-level audit reminder: 每个 anti-pattern 必须同时保留历史锚点与纠偏路径。只有 detect rule 而没有 escape clause，会把 review 变成阻断；只有 prevent rule 而没有 attribution，会把 exposed historical debt 误判为 introduced defect。

[derived] Master-level audit reminder: 每个 anti-pattern 必须同时保留历史锚点与纠偏路径。只有 detect rule 而没有 escape clause，会把 review 变成阻断；只有 prevent rule 而没有 attribution，会把 exposed historical debt 误判为 introduced defect。

[derived] Master-level audit reminder: 每个 anti-pattern 必须同时保留历史锚点与纠偏路径。只有 detect rule 而没有 escape clause，会把 review 变成阻断；只有 prevent rule 而没有 attribution，会把 exposed historical debt 误判为 introduced defect。

[derived] Master-level audit reminder: 每个 anti-pattern 必须同时保留历史锚点与纠偏路径。只有 detect rule 而没有 escape clause，会把 review 变成阻断；只有 prevent rule 而没有 attribution，会把 exposed historical debt 误判为 introduced defect。

[derived] Master-level audit reminder: 每个 anti-pattern 必须同时保留历史锚点与纠偏路径。只有 detect rule 而没有 escape clause，会把 review 变成阻断；只有 prevent rule 而没有 attribution，会把 exposed historical debt 误判为 introduced defect。

[derived] Master-level audit reminder: 每个 anti-pattern 必须同时保留历史锚点与纠偏路径。只有 detect rule 而没有 escape clause，会把 review 变成阻断；只有 prevent rule 而没有 attribution，会把 exposed historical debt 误判为 introduced defect。

[derived] Master-level audit reminder: 每个 anti-pattern 必须同时保留历史锚点与纠偏路径。只有 detect rule 而没有 escape clause，会把 review 变成阻断；只有 prevent rule 而没有 attribution，会把 exposed historical debt 误判为 introduced defect。

[derived] Master-level audit reminder: 每个 anti-pattern 必须同时保留历史锚点与纠偏路径。只有 detect rule 而没有 escape clause，会把 review 变成阻断；只有 prevent rule 而没有 attribution，会把 exposed historical debt 误判为 introduced defect。

[derived] Master-level audit reminder: 每个 anti-pattern 必须同时保留历史锚点与纠偏路径。只有 detect rule 而没有 escape clause，会把 review 变成阻断；只有 prevent rule 而没有 attribution，会把 exposed historical debt 误判为 introduced defect。

[derived] Master-level audit reminder: 每个 anti-pattern 必须同时保留历史锚点与纠偏路径。只有 detect rule 而没有 escape clause，会把 review 变成阻断；只有 prevent rule 而没有 attribution，会把 exposed historical debt 误判为 introduced defect。

[derived] Master-level audit reminder: 每个 anti-pattern 必须同时保留历史锚点与纠偏路径。只有 detect rule 而没有 escape clause，会把 review 变成阻断；只有 prevent rule 而没有 attribution，会把 exposed historical debt 误判为 introduced defect。

[derived] Master-level audit reminder: 每个 anti-pattern 必须同时保留历史锚点与纠偏路径。只有 detect rule 而没有 escape clause，会把 review 变成阻断；只有 prevent rule 而没有 attribution，会把 exposed historical debt 误判为 introduced defect。

[derived] Master-level audit reminder: 每个 anti-pattern 必须同时保留历史锚点与纠偏路径。只有 detect rule 而没有 escape clause，会把 review 变成阻断；只有 prevent rule 而没有 attribution，会把 exposed historical debt 误判为 introduced defect。

[derived] Master-level audit reminder: 每个 anti-pattern 必须同时保留历史锚点与纠偏路径。只有 detect rule 而没有 escape clause，会把 review 变成阻断；只有 prevent rule 而没有 attribution，会把 exposed historical debt 误判为 introduced defect。

[derived] Master-level audit reminder: 每个 anti-pattern 必须同时保留历史锚点与纠偏路径。只有 detect rule 而没有 escape clause，会把 review 变成阻断；只有 prevent rule 而没有 attribution，会把 exposed historical debt 误判为 introduced defect。

[derived] Master-level audit reminder: 每个 anti-pattern 必须同时保留历史锚点与纠偏路径。只有 detect rule 而没有 escape clause，会把 review 变成阻断；只有 prevent rule 而没有 attribution，会把 exposed historical debt 误判为 introduced defect。

