---
status: "candidate / cloud_prompt / not-authority"
authority: "not-authority"
created_at: "2026-05-07"
title: "ESCAPE-CLAUSE-CATALOG-2026-05-07"
kind: "escape-clause-catalog"
no_actual_rule_deployment_implied: true
---

# Escape Clause Catalog

[evidence-backed] Escape clause 用于已经踩坑后的纠偏，不等同于检测失败后的惩罚。U11 关注 keep、rollback、defer、amend_and_proceed、needs_user 五种路径。

## Universal escape sequence

[candidate] 1) Stop new writes. 2) Build delta table. 3) Re-label claims. 4) Classify introduced vs exposed. 5) Ask user/authority writer for keep/rollback/defer/amend. 6) Write receipt. 7) Re-open only the minimal safe continuation.

## trivial


## moderate

- [candidate] `AP-SF-03` `Multi-dispatch silent merge`: first action = freeze claim wording; second action = compare `PR #240 combined Run-3+4` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-SF-05` `Multi-PR topology drift`: first action = freeze claim wording; second action = compare `PR #226/#228 + PR #239 FIX-7` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-SF-06` `Checkpoint field silent rename`: first action = freeze claim wording; second action = compare `PR #239 FIX-1` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-SF-08` `Threshold silent loosen`: first action = freeze claim wording; second action = compare `PR #239 FIX-2` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-SF-09` `Verdict wording silent escalate`: first action = freeze claim wording; second action = compare `PR #231 external audit synthesis` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-VF-01` `Primary title loses hierarchy to subtitle`: first action = freeze claim wording; second action = compare `visual 5 Gate rule-derived from Dispatch128/156/165` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-VF-03` `Random spacing and alignment`: first action = freeze claim wording; second action = compare `visual spec spacing/readability clauses` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-VF-06` `Saturation hijacks attention`: first action = freeze claim wording; second action = compare `visual spec controlled contrast` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-VF-07` `CJK/Latin baseline mismatch`: first action = freeze claim wording; second action = compare `visual typography readability rule` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-VS-06` `Whisper local install not verified`: first action = freeze claim wording; second action = compare `ASR candidate lane` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-MC-03` `/clear decided by duration not semantic boundary`: first action = freeze claim wording; second action = compare `token hygiene rule target` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-MC-05` `MEMORY.md grows past usable size`: first action = freeze claim wording; second action = compare `memory hygiene prompt target` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-CT-01` `Dispatch without token estimate`: first action = freeze claim wording; second action = compare `large 50-dispatch pack scale` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-CT-02` `Long session without /clear`: first action = freeze claim wording; second action = compare `token hygiene rule target` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-CT-04` `No cost dashboard`: first action = freeze claim wording; second action = compare `cloud/API cost governance target` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-CT-06` `Repeat prompt without cache`: first action = freeze claim wording; second action = compare `multi-window prompt repetition target` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-ED-02` `Coverage threshold below 80 without waiver`: first action = freeze claim wording; second action = compare `testing rule target` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-ED-03` `Code-review agent skipped`: first action = freeze claim wording; second action = compare `agent usage rule target` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-ED-05` `Import path assumption`: first action = freeze claim wording; second action = compare `pack-lint parser mismatch` with actual touched files; third action = choose keep/rollback/defer/amend.

## hard

- [candidate] `AP-SF-01` `Packed repair without explicit authorization`: first action = freeze claim wording; second action = compare `PR #226/#228 topology + PR #239 FIX-7` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-SF-02` `Run-1 amendment proceeds without explicit gate replay`: first action = freeze claim wording; second action = compare `PR #231 + PR #239 FIX-5` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-SF-04` `Worker-guessed scope expansion`: first action = freeze claim wording; second action = compare `PR #231 A1/A2/A3` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-SF-07` `Allowed path silent change`: first action = freeze claim wording; second action = compare `Dispatch127-176 pack audit F3` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-SF-10` `Boundary silent expand`: first action = freeze claim wording; second action = compare `PR #240 boundary block` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-AC-03` `task-index numbering conflict`: first action = freeze claim wording; second action = compare `2026-05-04 task-index risk named in prompt` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-AC-04` `decision-log append rewritten as replace`: first action = freeze claim wording; second action = compare `PR #231 authority-file redline` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-AC-05` `contract-index baseline drift`: first action = freeze claim wording; second action = compare `wave5 repair overflow rules` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-AC-06` `AGENTS.md rewritten instead of amended`: first action = freeze claim wording; second action = compare `PR #231 authority untouched guard` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-BL-07` `Dispatch schema lacks can_open flags`: first action = freeze claim wording; second action = compare `PR #240 can_open_c4=false` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-BL-08` `Vendor candidate silently accepted`: first action = freeze claim wording; second action = compare `visual/vendor candidate boundary` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-VF-02` `Subtitle or toast occludes critical content`: first action = freeze claim wording; second action = compare `visual failure taxonomy` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-VF-04` `Contrast below durable review threshold`: first action = freeze claim wording; second action = compare `visual spec typography/contrast clauses` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-VF-05` `Decoration heavier than evidence`: first action = freeze claim wording; second action = compare `visual spec anti-decorative graph rule` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-VF-08` `Good-enough visual pass`: first action = freeze claim wording; second action = compare `5 Gate not polish rule` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-VF-09` `Retrofitted visual after code`: first action = freeze claim wording; second action = compare `visual Day-0 input rule-derived` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-VF-10` `Mobile safe-area occlusion`: first action = freeze claim wording; second action = compare `visual desktop/tablet/mobile gate` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-VS-01` `Single vendor lane lock-in`: first action = freeze claim wording; second action = compare `wave5 vendor/runtime overflow posture` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-VS-02` `Vendor selection without spike audit`: first action = freeze claim wording; second action = compare `candidate research boundary` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-VS-05` `ASR vendor not benchmarked`: first action = freeze claim wording; second action = compare `audio_transcript/ASR overflow` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-VS-07` `Cloud API treated as free`: first action = freeze claim wording; second action = compare `cost-token governance derived from run scale` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-MC-01` `Handoff as transcript dump`: first action = freeze claim wording; second action = compare `Dispatch176 handoff contract` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-MC-02` `Handoff missing closure Step 5`: first action = freeze claim wording; second action = compare `session closure rule target` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-MC-04` `/compact without anchor`: first action = freeze claim wording; second action = compare `codex metacognition prompt target` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-MC-06` `Cross-session context assumed persistent`: first action = freeze claim wording; second action = compare `zip/GitHub/inference separation rule` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-MC-07` `Recover without git fetch`: first action = freeze claim wording; second action = compare `codex audit required before execution` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-MA-03` `Three-window cloud audit only uses one or two windows`: first action = freeze claim wording; second action = compare `PR #239 3-window audit synthesis` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-MA-04` `Silent-flexibility detector not run`: first action = freeze claim wording; second action = compare `Run amendment fields named in prompt` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-MA-06` `introduced vs exposed ignored`: first action = freeze claim wording; second action = compare `ContentFlow L1 meta lesson requested by prompt` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-MA-07` `Cross-window memory drift`: first action = freeze claim wording; second action = compare `Run-3+4 held-back signal preservation` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-CT-03` `/compact loses anchors`: first action = freeze claim wording; second action = compare `long retrospective / multi-source pack target` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-CT-05` `API retry without backoff`: first action = freeze claim wording; second action = compare `cloud/API governance target` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-ED-01` `No TDD before implementation`: first action = freeze claim wording; second action = compare `PR #226/#228 validation boundary` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-ED-04` `No verification loop`: first action = freeze claim wording; second action = compare `PR validation checklists` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-ED-06` `Diagnose without git fetch`: first action = freeze claim wording; second action = compare `codex audit required refresh` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-ED-08` `Hooks skipped for speed`: first action = freeze claim wording; second action = compare `PR validation checklists` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-DT-01` `PASS/DONE/OK wording creep`: first action = freeze claim wording; second action = compare `external reports + PR verdict language` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-DT-02` `Fake wall-clock duration`: first action = freeze claim wording; second action = compare `truthful stdout contract` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-DT-03` `Live web claimed without live web`: first action = freeze claim wording; second action = compare `zip/GitHub/public/inference separation` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-DT-04` `Claim label missing`: first action = freeze claim wording; second action = compare `visual/prd source label discipline` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-DT-05` `Evidence not refreshed`: first action = freeze claim wording; second action = compare `codex audit refresh required` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-DT-07` `Synthetic evidence labelled works`: first action = freeze claim wording; second action = compare `PR #239 FIX-2` with actual touched files; third action = choose keep/rollback/defer/amend.

## critical

- [candidate] `AP-AC-01` `Dual-window writes docs/current.md`: first action = freeze claim wording; second action = compare `PR #231/#240 authority untouched assertions` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-AC-02` `Sidecar agent writes authority files`: first action = freeze claim wording; second action = compare `Dispatch127-176 manifest authority_writer` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-AC-07` `Authority promote skips audit gate`: first action = freeze claim wording; second action = compare `not-authority frontmatter across pack` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-AC-08` `Authority writer max=1 violation`: first action = freeze claim wording; second action = compare `manifest authority_writer rows` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-BL-01` `write_enabled=False implies future unlock`: first action = freeze claim wording; second action = compare `Wave4 retro PR #113/#129 dry-run note` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-BL-02` `BBDown live runtime implied approval`: first action = freeze claim wording; second action = compare `wave5 blocked/overflow rules` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-BL-03` `ASR runtime implied approval`: first action = freeze claim wording; second action = compare `wave5 blocked/overflow rules` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-BL-04` `Browser automation implied approval`: first action = freeze claim wording; second action = compare `visual spec screenshot future-gated clause` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-BL-05` `Migration implied approval`: first action = freeze claim wording; second action = compare `wave5 blocked/overflow rules` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-BL-06` `Five overflow lanes unlocked in one PR`: first action = freeze claim wording; second action = compare `roadmap O1 overflow` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-BL-09` `Preview-only drifts into production write`: first action = freeze claim wording; second action = compare `PR #226/#228 preview shell` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-BL-10` `Candidate file silently becomes authority`: first action = freeze claim wording; second action = compare `candidate/not-authority frontmatter` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-VS-03` `BBDown cease-and-desist not rechecked`: first action = freeze claim wording; second action = compare `BBDown live runtime blocked lane` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-VS-04` `yt-dlp legal refresh skipped`: first action = freeze claim wording; second action = compare `PR #240 no yt-dlp boundary` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-MA-01` `Multi-window dispatch no ledger`: first action = freeze claim wording; second action = compare `Run-2/Run-3/Run-4 windows` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-MA-02` `amend_and_proceed skips user authorization`: first action = freeze claim wording; second action = compare `PR #231 + PR #239 FIX-5` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-MA-05` `Single-writer race`: first action = freeze claim wording; second action = compare `authority_writer rows + authority untouched checks` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-ED-07` `Destructive git misuse`: first action = freeze claim wording; second action = compare `worktree/local-only posture` with actual touched files; third action = choose keep/rollback/defer/amend.
- [candidate] `AP-DT-06` `Tested claim without evidence`: first action = freeze claim wording; second action = compare `wave4 retro no rerun tests note` with actual touched files; third action = choose keep/rollback/defer/amend.

[derived] Escape 难度越高，越不应由执行窗口单独判断。critical 条目通常涉及 authority promotion、runtime unlock、migration、browser automation、true write 或 destructive git；这些场景需要用户授权或独立审计。

[derived] Escape 难度越高，越不应由执行窗口单独判断。critical 条目通常涉及 authority promotion、runtime unlock、migration、browser automation、true write 或 destructive git；这些场景需要用户授权或独立审计。

[derived] Escape 难度越高，越不应由执行窗口单独判断。critical 条目通常涉及 authority promotion、runtime unlock、migration、browser automation、true write 或 destructive git；这些场景需要用户授权或独立审计。

[derived] Escape 难度越高，越不应由执行窗口单独判断。critical 条目通常涉及 authority promotion、runtime unlock、migration、browser automation、true write 或 destructive git；这些场景需要用户授权或独立审计。

[derived] Escape 难度越高，越不应由执行窗口单独判断。critical 条目通常涉及 authority promotion、runtime unlock、migration、browser automation、true write 或 destructive git；这些场景需要用户授权或独立审计。

