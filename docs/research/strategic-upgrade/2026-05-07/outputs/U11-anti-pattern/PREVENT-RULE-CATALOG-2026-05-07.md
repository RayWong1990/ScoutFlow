---
status: "candidate / cloud_prompt / not-authority"
authority: "not-authority"
created_at: "2026-05-07"
title: "PREVENT-RULE-CATALOG-2026-05-07"
kind: "prevent-rule-catalog"
no_actual_rule_deployment_implied: true
---

# Prevent Rule Catalog

[evidence-backed] 本 catalog 按 schema、contract、template、hook、skill 五类组织预防规则。U11 只写 candidate spec，不修改实际 rule/hook/skill。

## schema

### AP-SF-04 — Worker-guessed scope expansion

[candidate] 预防落位：在未来 `schema` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Worker-guessed scope expansion` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-SF-06 — Checkpoint field silent rename

[candidate] 预防落位：在未来 `schema` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Checkpoint field silent rename` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-AC-02 — Sidecar agent writes authority files

[candidate] 预防落位：在未来 `schema` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Sidecar agent writes authority files` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-AC-08 — Authority writer max=1 violation

[candidate] 预防落位：在未来 `schema` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Authority writer max=1 violation` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-BL-02 — BBDown live runtime implied approval

[candidate] 预防落位：在未来 `schema` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `BBDown live runtime implied approval` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-BL-03 — ASR runtime implied approval

[candidate] 预防落位：在未来 `schema` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `ASR runtime implied approval` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-BL-07 — Dispatch schema lacks can_open flags

[candidate] 预防落位：在未来 `schema` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Dispatch schema lacks can_open flags` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-MA-01 — Multi-window dispatch no ledger

[candidate] 预防落位：在未来 `schema` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Multi-window dispatch no ledger` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-MA-05 — Single-writer race

[candidate] 预防落位：在未来 `schema` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Single-writer race` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-DT-07 — Synthetic evidence labelled works

[candidate] 预防落位：在未来 `schema` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Synthetic evidence labelled works` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

## contract

### AP-SF-01 — Packed repair without explicit authorization

[candidate] 预防落位：在未来 `contract` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Packed repair without explicit authorization` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-SF-03 — Multi-dispatch silent merge

[candidate] 预防落位：在未来 `contract` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Multi-dispatch silent merge` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-SF-05 — Multi-PR topology drift

[candidate] 预防落位：在未来 `contract` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Multi-PR topology drift` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-SF-10 — Boundary silent expand

[candidate] 预防落位：在未来 `contract` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Boundary silent expand` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-AC-01 — Dual-window writes docs/current.md

[candidate] 预防落位：在未来 `contract` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Dual-window writes docs/current.md` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-AC-05 — contract-index baseline drift

[candidate] 预防落位：在未来 `contract` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `contract-index baseline drift` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-AC-07 — Authority promote skips audit gate

[candidate] 预防落位：在未来 `contract` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Authority promote skips audit gate` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-BL-01 — write_enabled=False implies future unlock

[candidate] 预防落位：在未来 `contract` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `write_enabled=False implies future unlock` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-BL-04 — Browser automation implied approval

[candidate] 预防落位：在未来 `contract` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Browser automation implied approval` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-BL-06 — Five overflow lanes unlocked in one PR

[candidate] 预防落位：在未来 `contract` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Five overflow lanes unlocked in one PR` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-BL-08 — Vendor candidate silently accepted

[candidate] 预防落位：在未来 `contract` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Vendor candidate silently accepted` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-VF-02 — Subtitle or toast occludes critical content

[candidate] 预防落位：在未来 `contract` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Subtitle or toast occludes critical content` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-VF-05 — Decoration heavier than evidence

[candidate] 预防落位：在未来 `contract` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Decoration heavier than evidence` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-VF-08 — Good-enough visual pass

[candidate] 预防落位：在未来 `contract` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Good-enough visual pass` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-VF-10 — Mobile safe-area occlusion

[candidate] 预防落位：在未来 `contract` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Mobile safe-area occlusion` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-VS-01 — Single vendor lane lock-in

[candidate] 预防落位：在未来 `contract` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Single vendor lane lock-in` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-VS-03 — BBDown cease-and-desist not rechecked

[candidate] 预防落位：在未来 `contract` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `BBDown cease-and-desist not rechecked` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-VS-04 — yt-dlp legal refresh skipped

[candidate] 预防落位：在未来 `contract` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `yt-dlp legal refresh skipped` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-MC-06 — Cross-session context assumed persistent

[candidate] 预防落位：在未来 `contract` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Cross-session context assumed persistent` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-MA-02 — amend_and_proceed skips user authorization

[candidate] 预防落位：在未来 `contract` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `amend_and_proceed skips user authorization` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-MA-07 — Cross-window memory drift

[candidate] 预防落位：在未来 `contract` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Cross-window memory drift` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-ED-03 — Code-review agent skipped

[candidate] 预防落位：在未来 `contract` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Code-review agent skipped` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-ED-07 — Destructive git misuse

[candidate] 预防落位：在未来 `contract` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Destructive git misuse` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-DT-03 — Live web claimed without live web

[candidate] 预防落位：在未来 `contract` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Live web claimed without live web` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-DT-05 — Evidence not refreshed

[candidate] 预防落位：在未来 `contract` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Evidence not refreshed` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

## template

### AP-SF-02 — Run-1 amendment proceeds without explicit gate replay

[candidate] 预防落位：在未来 `template` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Run-1 amendment proceeds without explicit gate replay` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-SF-08 — Threshold silent loosen

[candidate] 预防落位：在未来 `template` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Threshold silent loosen` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-SF-09 — Verdict wording silent escalate

[candidate] 预防落位：在未来 `template` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Verdict wording silent escalate` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-AC-04 — decision-log append rewritten as replace

[candidate] 预防落位：在未来 `template` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `decision-log append rewritten as replace` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-AC-06 — AGENTS.md rewritten instead of amended

[candidate] 预防落位：在未来 `template` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `AGENTS.md rewritten instead of amended` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-BL-10 — Candidate file silently becomes authority

[candidate] 预防落位：在未来 `template` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Candidate file silently becomes authority` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-VF-01 — Primary title loses hierarchy to subtitle

[candidate] 预防落位：在未来 `template` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Primary title loses hierarchy to subtitle` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-VF-03 — Random spacing and alignment

[candidate] 预防落位：在未来 `template` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Random spacing and alignment` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-VF-04 — Contrast below durable review threshold

[candidate] 预防落位：在未来 `template` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Contrast below durable review threshold` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-VF-06 — Saturation hijacks attention

[candidate] 预防落位：在未来 `template` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Saturation hijacks attention` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-VF-07 — CJK/Latin baseline mismatch

[candidate] 预防落位：在未来 `template` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `CJK/Latin baseline mismatch` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-VF-09 — Retrofitted visual after code

[candidate] 预防落位：在未来 `template` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Retrofitted visual after code` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-VS-02 — Vendor selection without spike audit

[candidate] 预防落位：在未来 `template` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Vendor selection without spike audit` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-VS-05 — ASR vendor not benchmarked

[candidate] 预防落位：在未来 `template` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `ASR vendor not benchmarked` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-VS-07 — Cloud API treated as free

[candidate] 预防落位：在未来 `template` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Cloud API treated as free` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-MC-01 — Handoff as transcript dump

[candidate] 预防落位：在未来 `template` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Handoff as transcript dump` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-MC-02 — Handoff missing closure Step 5

[candidate] 预防落位：在未来 `template` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Handoff missing closure Step 5` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-MC-04 — /compact without anchor

[candidate] 预防落位：在未来 `template` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `/compact without anchor` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-MA-03 — Three-window cloud audit only uses one or two windows

[candidate] 预防落位：在未来 `template` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Three-window cloud audit only uses one or two windows` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-MA-06 — introduced vs exposed ignored

[candidate] 预防落位：在未来 `template` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `introduced vs exposed ignored` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-CT-01 — Dispatch without token estimate

[candidate] 预防落位：在未来 `template` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Dispatch without token estimate` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-CT-03 — /compact loses anchors

[candidate] 预防落位：在未来 `template` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `/compact loses anchors` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-CT-04 — No cost dashboard

[candidate] 预防落位：在未来 `template` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `No cost dashboard` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-ED-01 — No TDD before implementation

[candidate] 预防落位：在未来 `template` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `No TDD before implementation` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-ED-04 — No verification loop

[candidate] 预防落位：在未来 `template` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `No verification loop` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-DT-01 — PASS/DONE/OK wording creep

[candidate] 预防落位：在未来 `template` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `PASS/DONE/OK wording creep` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-DT-02 — Fake wall-clock duration

[candidate] 预防落位：在未来 `template` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Fake wall-clock duration` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-DT-04 — Claim label missing

[candidate] 预防落位：在未来 `template` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Claim label missing` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-DT-06 — Tested claim without evidence

[candidate] 预防落位：在未来 `template` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Tested claim without evidence` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

## hook

### AP-SF-07 — Allowed path silent change

[candidate] 预防落位：在未来 `hook` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Allowed path silent change` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-AC-03 — task-index numbering conflict

[candidate] 预防落位：在未来 `hook` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `task-index numbering conflict` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-BL-05 — Migration implied approval

[candidate] 预防落位：在未来 `hook` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Migration implied approval` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-BL-09 — Preview-only drifts into production write

[candidate] 预防落位：在未来 `hook` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Preview-only drifts into production write` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-VS-06 — Whisper local install not verified

[candidate] 预防落位：在未来 `hook` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Whisper local install not verified` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-MC-05 — MEMORY.md grows past usable size

[candidate] 预防落位：在未来 `hook` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `MEMORY.md grows past usable size` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-MC-07 — Recover without git fetch

[candidate] 预防落位：在未来 `hook` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Recover without git fetch` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-MA-04 — Silent-flexibility detector not run

[candidate] 预防落位：在未来 `hook` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Silent-flexibility detector not run` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-CT-05 — API retry without backoff

[candidate] 预防落位：在未来 `hook` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `API retry without backoff` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-ED-02 — Coverage threshold below 80 without waiver

[candidate] 预防落位：在未来 `hook` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Coverage threshold below 80 without waiver` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-ED-05 — Import path assumption

[candidate] 预防落位：在未来 `hook` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Import path assumption` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-ED-06 — Diagnose without git fetch

[candidate] 预防落位：在未来 `hook` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Diagnose without git fetch` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-ED-08 — Hooks skipped for speed

[candidate] 预防落位：在未来 `hook` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Hooks skipped for speed` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

## skill

### AP-MC-03 — /clear decided by duration not semantic boundary

[candidate] 预防落位：在未来 `skill` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `/clear decided by duration not semantic boundary` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-CT-02 — Long session without /clear

[candidate] 预防落位：在未来 `skill` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Long session without /clear` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

### AP-CT-06 — Repeat prompt without cache

[candidate] 预防落位：在未来 `skill` 中加入 `scope_delta`、`evidence_label`、`introduced_or_exposed`、`user_authorization_ref`、`escape_clause`。如果 `Repeat prompt without cache` 相关字段缺失，则默认输出 partial/needs-amendment，不输出 clear。

## Minimal schema proposal

```yaml
scope_delta: none|narrower|wider|replacement
authority_surface_touched: []
evidence_label: canonical_fact|reported_evidence|candidate|inference|needs_refresh
introduced_or_exposed: introduced|exposed|hypothetical
user_authorization_ref: null|string
escape_clause: keep|rollback|defer|amend_and_proceed|needs_user
no_actual_rule_deployment_implied: true
```

