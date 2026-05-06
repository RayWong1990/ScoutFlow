---
title: Run-1 Amendment Ledger — Post-External-Audit Closeout
status: candidate / amendment_ledger / not-authority
created_at: 2026-05-06
authors: [codex-cli-amendment-run]
audit_inputs:
  - docs/research/post-frozen/audits/run-1-audit-gpt-pro-independent-a-2026-05-06.md
  - docs/research/post-frozen/audits/run-1-audit-gpt-5-codex-cloud-2026-05-06.md
  - docs/research/post-frozen/audits/run-1-audit-hermes-2026-05-06.md
synthesis_verdict: REJECT_AS_SCOPE_DRIFT
synthesis_decision: amend_and_proceed
run_1_state_after_merge: closed_with_accepted_amendments
ready_for_run_2: yes
---

# Executive Summary

Run-1（PR #199–#206）3 家外审中 2/3 给 REJECT，1/3 给 V-PASS_WITH_AMENDMENTS。authority 未碰、硬红线守住，但 PF-LP-01 / PF-LP-02 / PF-LP-13 三处越 §4 allowed_paths。

本 ledger 追认 A1–A3 为 `accepted_partial_scope_deviation`（KEEP，无 rollback），落 A4–A6 为 doc/rule fix，前置 A7 为 Run-2 硬 stop-line，A8 仅 note。

# Findings Detail

## A1 — PF-LP-02 / PR #205：production code 越 §4

- finding_id: A1
- severity: CRITICAL
- auditor_consensus: gpt-pro / gpt-5.5 / hermes
- evidence_paths:
  - `docs/research/post-frozen/80-pack-source/02_task_packs/PF-localhost-preview-pack/dispatches/PF-LP-02-bridge-preview-route-smoke-tests.md:25-30`
  - `services/api/scoutflow_api/bridge/vault_preview.py:47-88`
  - `services/api/scoutflow_api/vault/renderer.py:46-82`
  - `tests/contracts/test_vault_renderer_contract.py:71-110`
  - `tests/fixtures/vault_inbox/expected_scoutflow_note.md:1-30`
- decision: `KEEP_AS_ACCEPTED_PARTIAL_SCOPE_DEVIATION`
- rationale: 无 true write 语义；preview-only draft shape 是 `>=20` line excerpt proof bar 的必需扩展。当前 `origin/main` 已含 PF-LP-04 / PF-LP-05 / PF-LP-06 后继 wiring，直接 rollback 会把 preview-only 消费链路重新打断，且不会带来新的安全收益。
- forward_rule: 任何 future dispatch 若 proof requirement 与 §4 allowed_paths 冲突，必须 `STOP + 写 truth-conflict + 等用户 re-scope`，不许 silently 扩 path（详见 `docs/research/post-frozen/run-2-commander-prompt-template-rules-2026-05-06.md`）。

## A2 — PF-LP-13 / PR #206：`tests/conftest.py` 越 §4

- finding_id: A2
- severity: HIGH
- auditor_consensus: gpt-pro / gpt-5.5 / hermes
- evidence_paths:
  - `docs/research/post-frozen/80-pack-source/02_task_packs/PF-localhost-preview-pack/dispatches/PF-LP-13-backend-contract-validation-bundle.md:25-31`
  - `tests/conftest.py:4-10`
- decision: `KEEP_AS_ACCEPTED_PARTIAL_SCOPE_DEVIATION`
- rationale: `tests/conftest.py` 仅加入 `--golden` option plumbing；无 autouse fixture、无 monkeypatch side effect、无 runtime write 语义。技术风险低于再次拆分 test harness 的扰动风险。
- forward_rule: dispatch §4 若需 pytest shared option，必须显式列 `tests/conftest.py`；否则改为 test-local helper 或 env-driven local parsing。

## A3 — PF-LP-01 / PR #204：contract test de-dup 越 §4

- finding_id: A3
- severity: MEDIUM
- auditor_consensus: gpt-pro / gpt-5.5 / hermes
- evidence_paths:
  - `docs/research/post-frozen/80-pack-source/02_task_packs/PF-localhost-preview-pack/dispatches/PF-LP-01-bridge-router-mount-in-create_app.md:25-33`
  - `services/api/scoutflow_api/main.py:60-63`
  - `tests/api/test_main_app_routers.py:39-71`
- decision: `KEEP_AS_ACCEPTED_PARTIAL_SCOPE_DEVIATION`
- rationale: companion contract tests 的修改属于机械 de-dup，删除的是手动 `app.include_router(bridge_router)`，不是断言本身；新主测试补齐路由、health、commit schema 三类 required assertions，coverage 未丢。
- forward_rule: companion-test edits 必须在 dispatch §4 declared；若执行中才发现需要触碰 companion tests，必须在 30 分钟内补 amendment note 或 truth-conflict。

## A4 — #199 live-authority-readback supersession

- finding_id: A4
- severity: MEDIUM
- auditor_consensus: gpt-pro / gpt-5.5
- evidence_paths:
  - `docs/research/post-frozen/live-authority-readback-after-pr194.md:31-54`
  - `services/api/scoutflow_api/main.py:60-63`
  - `tests/contracts/golden/bridge-openapi-2026-05-06.json:2-27`
- decision: `DOC_FIX`
- rationale: 该文档捕获的是 PR194 boundary truth，不应继续被读成 current truth source。A4 不是 authority drift，但需要显式 supersession 头避免误读。
- forward_rule: 任何带 `readback` / `live truth` 命名的阶段性 candidate 文档，一旦被后续 landed code 取代，必须追加 `superseded_by` 或 `valid_at_*_boundary_only` 标记。

## A5 — #198 boundary note

- finding_id: A5
- severity: MEDIUM
- auditor_consensus: gpt-pro / gpt-5.5
- evidence_paths:
  - `docs/research/post-frozen/audits/run-1-audit-gpt-pro-independent-a-2026-05-06.md:104-109`
  - `docs/research/post-frozen/audits/run-1-audit-gpt-5-codex-cloud-2026-05-06.md:90-96`
- decision: `RULE_CLARIFICATION`
- rationale: baseline 到 final compare 区间包含 user-authorized PR #198，但它不是 Run-1 stage receipt。这个边界必须显式说清，不然外审读 compare 时会误把 interleaving commit 当成 commander deviation。
- action: 本 ledger 记录 `#198` 是 user-authorized non-Run-1 interleaving commit；未来 run receipts 必须把 compare 区间内的非本 run commit 单列。
- forward_rule: future Run-N handoff report 必须在 receipt 段后追加 `compare_boundary_notes` 字段，列出区间内非本 Run 的 user-authorized commits。

## A6 — Frontmatter J 规则澄清

- finding_id: A6
- severity: MEDIUM
- auditor_consensus: gpt-5.5
- evidence_paths:
  - `tests/fixtures/vault_inbox/expected_scoutflow_note.md:1-6`
  - `docs/research/post-frozen/audits/run-1-audit-gpt-5-codex-cloud-2026-05-06.md:84-88`
- decision: `RULE_CLARIFICATION`
- rationale: `tests/fixtures/**` 下的 markdown frontmatter 是测试数据，不是治理状态；J 检查如果不区分治理 markdown 与 fixture markdown，会把非 authority 的测试载荷误判为流程违规。
- new_rule: J 检查仅适用于 `docs/research/**` 下的 governance markdown。`tests/fixtures/**` 下的 fixture markdown豁免。
- forward_rule: 后续 audit / commander prompt 若保留 frontmatter status gate，必须写清 governance markdown scope，不得把 fixture markdown 一起纳入。

## A7 — Run-2 commander template stop-line（preventive）

- finding_id: A7
- severity: LOW
- auditor_consensus: gpt-pro / gpt-5.5
- evidence_paths:
  - `docs/research/post-frozen/audits/run-1-audit-gpt-pro-independent-a-2026-05-06.md:280-287`
  - `docs/research/post-frozen/audits/run-1-audit-gpt-5-codex-cloud-2026-05-06.md:134-142`
  - `docs/research/post-frozen/run-2-commander-prompt-template-rules-2026-05-06.md:19-38`
- decision: `RULE_CLARIFICATION`
- rationale: Run-1 的共同模式不是“功能错”，而是“proof bar 与 §4 合同冲突时默认扩 path”。不把 stop-line 提前锁到模板层，Run-2 还会重复同型偏移。
- action: 创建 `docs/research/post-frozen/run-2-commander-prompt-template-rules-2026-05-06.md`，将 Rule 1/2/3 明文化。
- forward_rule: 任何 future Run-N commander prompt 若未引用 A7 规则文件，视为 invalid，不得执行。

## A8 — PR body shell-safe quotes

- finding_id: A8
- severity: LOW
- auditor_consensus: gpt-pro
- evidence_paths:
  - `docs/research/post-frozen/audits/run-1-audit-gpt-pro-independent-a-2026-05-06.md:129-136`
- decision: `NOTE_ONLY`
- rationale: 这是 PR body formatting 问题，不触及 repo runtime、authority 或 contract state，不值得再开独立修复。保留 note 即可。
- note: 后续 commander prompt / PR body 模板应强制 shell-safe quoting（尤其 `python -c` 片段）。

# Run-1 final state

- `closed_with_accepted_amendments`
- `ready_for_run_2: yes`
- Run-2 必须遵守 `docs/research/post-frozen/run-2-commander-prompt-template-rules-2026-05-06.md`
