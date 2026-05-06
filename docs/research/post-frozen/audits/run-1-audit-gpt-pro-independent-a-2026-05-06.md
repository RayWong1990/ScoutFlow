---
title: Run-1 External Audit Report — gpt-pro-independent-a
status: candidate / external_audit / not-authority
created_at: 2026-05-06
auditor: gpt-pro-independent-a
audit_target: Run-1 (PR #199 -> #206)
audit_baseline_sha: 82481b197eaa420744af90427b07a5ad670d3d96
audit_final_sha: 9d90d0a436ee756bfc31dde4616f14b326a540c3
audit_handoff_branch: run1-audit-handoff
---
----------------------------------------

# Run-1 External Audit Report — gpt-pro-independent-a

## Executive verdict

**全局 verdict：`REJECT`**

这不是因为发现 true vault write、runtime tools、migration、authority drift 或 frozen Dispatch126-176 被重开；这些硬红线整体守住了。
真正的阻断点是：**PF-LP-02 / PR #205 发生明确 allowed_paths 越界，而且是 production code 越界，不只是 test / docs 越界。** PF-LP-02 dispatch §4 明确 `files_to_modify: []`，只允许创建 `tests/api/test_bridge_vault_preview_smoke.py`，但 PR #205 实际修改了 `services/api/scoutflow_api/bridge/vault_preview.py`、`services/api/scoutflow_api/vault/renderer.py`、`tests/contracts/test_vault_renderer_contract.py`、`tests/fixtures/vault_inbox/expected_scoutflow_note.md` 等文件。dispatch 源文件的 allowed paths 与实际 PR diff 直接冲突。

如果只看产品安全，Run-1 大体是安全的；如果按你这份审计 charter，D 检查点明确写“任一越 allowed_paths → reject”，所以我不能给 `V-PASS_WITH_AMENDMENTS`。

---

## 1. 12 检查点 verdict 表

| # | 检查点                     | verdict | evidence |
| - | ----------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A | authority untouched     | clear   | compare `82481b1...9d90d0a` 的文件清单只包含 `docs/research/post-frozen/**`、`services/api/**`、`tests/**`，未出现 `docs/current.md` / `docs/task-index.md` / `docs/decision-log.md` / `AGENTS.md`；Run report 也自报 authority files untouched。            |
| B | 硬红线                     | clear   | final `bridge/config.py` 两个分支均 `write_enabled=False`；`BridgeVaultCommitResponse.write_enabled` 为 `Literal[False]`；_PACK-DEFAULTS 继续禁止 true write / runtime / browser / migration 等。                                                       |
| C | LP-12 defer 合规          | clear   | truth-conflict 文件有 4 行 conflict table，记录 user clarification “stage table is advisory, dispatch §3 dependencies are authoritative”；current verdict `resolved_for_run1_continue`; PR 数为 0。                   |
| D | LP-02 expansion bounded | reject  | PF-LP-02 dispatch §4 只允许创建 `tests/api/test_bridge_vault_preview_smoke.py`，`files_to_modify: []`；PR #205 实际修改 production `bridge/vault_preview.py` 与 `vault/renderer.py`，属于越 allowed_paths 的 slot-local 自决。                                |
| E | LP-13 conftest in scope | concern | PF-LP-13 dispatch §4 只允许创建 golden contract test 与 golden json，`files_to_modify: []`；PR #206 新增 `tests/conftest.py`。实现只有 10 行、无 autouse/monkeypatch 污染，但不在 §4 scope 内。                                                                     |
| F | LP-01 dedup 覆盖率         | concern | PR #204 删除了 5 个 bridge contract tests 中手动 `app.include_router(bridge_router)` 的重复挂载，未删关键 assertions；但这些 test 文件不在 PF-LP-01 §4 files preview 内，仍是 scope flexibility。                                                                       |
| G | interruption residue    | concern | compare 显示 baseline→final ahead_by=11，文件包含 PR #198 readback 文件以及 8 Run-1 PR 改动；CHECKPOINT 只列 8 Run-1 PR。用户已锁 #198 为非 Run-1 commit，不算 deviation，但 Run-1 report 没显式把 #198 作为 non-run interleaving commit 纳入边界说明。                            |
| H | baseline 完整性            | clear   | CHECKPOINT 记录 baseline=`82481b197e...`、final=`9d90d0a...`、dispatches_completed 为 8 个、PF-LP-12 deferred；#197/#198 未被列入 Run-1 dispatch receipt。                                                                                             |
| I | Receipt 内一致性            | clear   | RUN report 的 8 PR list / merge commits 与 DIFF-BUNDLE 的 8 PR pr_bundle 以及 CHECKPOINT 的 `prs_merged=[199..206]` 三处一致。                                                                                                                       |
| J | Frontmatter status 合规   | clear   | 抽样 Run-1 输出 frontmatter 均为 candidate / research / not-authority 或 run_report / not-authority；如 live-authority-readback、near-term matrix 均未升级为 authority。                                                                                  |
| K | Commander 落实度           | concern | commander prompt 要求 live truth 与 dispatch 假设冲突时停下来等 user；PF-LP-12 确实停下并 rescope。但 commander 也要求按 dispatch 文件本体执行；PF-LP-02 / LP-13 / LP-01 均发生 self-recovery / scope flexibility，虽在 RUN report 有披露，但不是严格按 §4 执行。                           |
| L | §8 assertion count ≥ 3  | clear   | PF-LP-01 新增 `tests/api/test_main_app_routers.py` 三类 explicit assertions；PF-LP-02 smoke test 覆盖 capture_id、20+ lines、unset fail-loud/write flag；PF-LP-13 golden test 覆盖 schema equality、field lists、write_enabled false / preview excerpt。 |

---

## 2. Per-dispatch verdict 表

| dispatch              |   PR | verdict                 | scope_deviation_flag | silent_flexibility_count | evidence                                                                                                  |
| --------------------- | ---: | ----------------------- | -------------------- | -----------------------: | --------------------------------------------------------------------------------------------------------- |
| PF-C0-01R             | #199 | T-PASS_WITH_NOTE        | no                   |                        0 | Single docs readback, candidate/not-authority; no runtime change.                                         |
| PF-O1-01R             | #200 | T-PASS                  | no                   |                        0 | Single overflow registry doc, blocked lanes explicit.                                                     |
| PF-LP-03              | #201 | T-PASS                  | no                   |                        0 | Single vault preview env contract doc, no true write.                                                     |
| PF-C0-MERGED-03+04    | #202 | T-PASS                  | no                   |                        0 | Single successor-entry / preview-only scope memo.                                                         |
| PF-C0-06R             | #203 | T-PASS_WITH_NOTE        | no                   |                        0 | Near-term matrix created; frontmatter candidate/not-authority.                                            |
| PF-LP-01 (HIGH_BLAST) | #204 | partial_scope_deviation | yes                  |                        1 | Required mount and write_enabled false implemented; modified extra contract tests outside §4 for de-dup.  |
| PF-LP-02              | #205 | REJECT_AS_SCOPE_DRIFT   | yes                  |                        1 | Dispatch §4 allowed only creating smoke test; PR modified production bridge/vault preview and renderer.   |
| PF-LP-13 (HIGH_BLAST) | #206 | partial_scope_deviation | yes                  |                        1 | Golden contract meaningful; `tests/conftest.py` added outside §4.                                         |

---

## 3. 全局 verdict

**`REJECT`**

触发原因：

* 检查点 D = `reject`
* 同源问题为 “dispatch §4 allowed_paths 约束被 self-recovery 绕过”
* 虽无 true-write / runtime / authority drift，但 Run-1 不能被判 `V-PASS`

Run-2 前必须有 amendment，至少要把 PF-LP-02 的实际扩张路径补成合法 repair / amendment，或者承认 #205 为 `partial_scope_deviation` 并单独审后放行。

---

## 4. 编号 findings

### Finding 1 [CRITICAL]

* 检查点关联: D / K
* 现象: PF-LP-02 / PR #205 越过 dispatch §4 allowed_paths，修改 production preview renderer / route。
* 证据: PF-LP-02 §4 写 `files_to_create: tests/api/test_bridge_vault_preview_smoke.py`，`files_to_modify: []`。 PR #205 实际改动包括 `services/api/scoutflow_api/bridge/vault_preview.py`、`services/api/scoutflow_api/vault/renderer.py`、fixture 与 contract test。
* Codex 自报口径: RUN report 称 “preview markdown was too short... resolved by expanding preview-only draft shape and syncing e2e fixture baseline”。
* audit 结论: 这是被披露的 slot-local self-recovery，但仍违反 dispatch §4；按 charter D，越 allowed_paths → reject。
* 修复建议: Run-2 前补一个 `PF-LP-02-SCOPE-AMENDMENT`，明确追认 `bridge/vault_preview.py`、`vault/renderer.py`、renderer contract、fixture sync 为 preview-only scope repair；否则不得把 #205 作为 clean precedent。

### Finding 2 [HIGH]

* 检查点关联: E / K
* 现象: PF-LP-13 / PR #206 增加 `tests/conftest.py`，不在 §4 files preview 内。
* 证据: PF-LP-13 §4 只允许创建 `tests/contracts/test_bridge_openapi_golden_contract.py` 与 `tests/contracts/golden/bridge-openapi-2026-05-06.json`，`files_to_modify: []`。 PR #206 实际新增 `tests/conftest.py`。
* Codex 自报口径: RUN report 称 “tests/conftest.py adds only the minimal `--golden` option plumbing”。
* audit 结论: 实现确实 minimal，只有 10 行并只增加 `--golden` option，无 autouse / monkeypatch 污染。 但仍是 scope deviation。
* 修复建议: Run-2 前补入 dispatch template rule：若需要 pytest shared option，必须在 §4 显式列 `tests/conftest.py`；或将 golden path 改为 env var / default-only，避免 conftest 横切。

### Finding 3 [MEDIUM]

* 检查点关联: F / K
* 现象: PF-LP-01 / PR #204 修改 5 个旧 bridge contract tests，虽未删关键 assertion，但这些 test 文件未在 §4 files preview 内。
* 证据: PF-LP-01 §4 允许创建 `tests/api/test_main_app_routers.py`、修改 `main.py`、`bridge/schemas.py`、`bridge/vault_commit.py`。 PR #204 changed files 包含 `tests/contracts/test_bridge_route_group_contract.py`、`test_bridge_openapi_snapshot_contract.py`、`test_bridge_vault_preview_contract.py`、`test_bridge_vault_commit_dry_run_contract.py` 等。
* Codex 自报口径: “old bridge contract tests were de-duplicated to stop double-mount warnings”。
* audit 结论: De-dup 删除的是手动 `app.include_router(bridge_router)`，不是关键 assertion；新 default mount 测试补了三类 assertion。 因此不是 reject，但要标 scope flexibility。
* 修复建议: 给 PF-LP-01 增补 amendment：contract-test de-dup 是 allowed companion change，仅限删除 manual `include_router`。

### Finding 4 [MEDIUM]

* 检查点关联: G / H
* 现象: compare `82481b1...9d90d0a` 包含 #198 `pr197-check-readback` 文件，但 Run-1 report / checkpoint 只列 8 PR。
* 证据: compare 文件清单包含 `docs/research/post-frozen/pr197-check-readback-2026-05-06.md`，同时 CHECKPOINT 只列 `prs_merged: [199..206]`。
* Codex 自报口径: 没有在 RUN-1 report 明确说明 #198 是 user-authorized interleaving non-run commit。
* audit 结论: 用户审计 prompt 明确 #198 不计入 Codex scope deviation，所以不算 reject；但报告边界不够自解释。
* 修复建议: 在 Run-1 handoff report 后续版本加一句：`#198 exists between baseline and final but is user-authorized non-Run-1 readback, excluded from prs_merged`。

### Finding 5 [MEDIUM]

* 检查点关联: J / H
* 现象: #199 live-authority-readback 文档在 final main 上存在过时语句：称 `create_app()` has not yet mounted `bridge_router`，但 final code 已由 #204 mount。
* 证据: #199 文档写 “current localhost code seams still match... create_app() does not mount bridge_router”；final `main.py` 已导入并 include `bridge_router`。
* Codex 自报口径: DIFF-BUNDLE 把 #199 描述为 “resets live truth boundary after PR193/194”。
* audit 结论: 这不是 authority drift，因为 #199 是阶段性 readback；但文件名 “live authority readback” 在 final main 读起来容易被误解为当前 truth。
* 修复建议: 在 #199 doc 顶部补 `valid_at_pr194_boundary_only` / `superseded_by_PR204_for_bridge_mount_fact`。

### Finding 6 [LOW]

* 检查点关联: K
* 现象: commander prompt stdout 期望 9 PR，但实际因 LP-12 user defer 后变成 8 PR；报告合理记录了 8，但未明确列“original stdout template superseded”。
* 证据: commander prompt 原本写 “完成 9 dispatch 全 merged 后”，truth-conflict 记录用户 clarification 后将 Run-1 改为 8 dispatch。
* Codex 自报口径: RUN report 清楚写 “PF-LP-12 -> Run-2 after PF-LP-04 lands”。
* audit 结论: clear with note，不影响执行。
* 修复建议: 后续 commander prompt 模板在 rescope 后要同步 stdout expected count。

### Finding 7 [LOW]

* 检查点关联: B / L
* 现象: PR #204 PR body validation snippet 显示 `assert /bridge/health in paths` 这种无引号形式，作为 shell command 不可直接执行。
* 证据: PR #204 body validation 列出的 `python -c` 片段缺引号。
* Codex 自报口径: report 说 high-blast clean。
* audit 结论: 这只是 PR body formatting 问题；dispatch §12 与测试文件本身正确。
* 修复建议: 后续 PR body 自动生成时保留 shell-safe quotes，避免审计歧义。

---

## 5. Silent flexibility 专栏

### 偏移 1 — PF-LP-02 preview-only draft expansion 触碰 production code

* 描述: 为满足 20+ line excerpt，Codex 修改 `bridge/vault_preview.py` 与 `vault/renderer.py`，将短 markdown 改成完整 preview-only draft。
* Codex 是否提到: 提到了。RUN report interruption_receipt 写 “preview markdown was too short... resolved by expanding preview-only draft shape and syncing the e2e fixture baseline”。
* 是否 commander 允许 self-recovery: 模糊。它可以是 slot-local retry，但 dispatch §4 不允许改 production code。
* 是否影响 Run-2 安全: 是。它树立了“验收不足时自扩 allowed_paths”的先例。
* audit verdict: `REJECT_AS_SCOPE_DRIFT`

### 偏移 2 — PF-LP-13 增加 tests/conftest.py

* 描述: 为支持 `--golden` CLI option 增加 pytest shared config。
* Codex 是否提到: 提到了。RUN report high-blast PF-LP-13 写 “tests/conftest.py adds only the minimal --golden option plumbing”。
* 是否 commander 允许 self-recovery: 部分允许，但 dispatch §4 不含该文件。
* 是否影响 Run-2 安全: 中低。实现 10 行且无 autouse side effect。
* audit verdict: `concern`

### 偏移 3 — PF-LP-01 修改旧 bridge contract tests

* 描述: 为避免 double-mount warnings 删除多个 test helper 中 `app.include_router(bridge_router)`。
* Codex 是否提到: 提到了。RUN report 写 “old bridge contract tests were de-duplicated to stop double-mount warnings”。
* 是否 commander 允许 self-recovery: 模糊。验证层维护合理，但不在 §4。
* 是否影响 Run-2 安全: 低。关键 assertions 未明显丢失，新 test 增加了 path/health/commit schema assertions。
* audit verdict: `concern`

### 偏移 4 — control-plane index-lock / local main accidental commit

* 描述: RUN report 称发生 “accidental local commit on main”，随后移到 `codex/run1-pf-o1-01r` 并 reset local refs。
* Codex 是否提到: 提到了。
* 是否 commander 允许 self-recovery: 是，属于 control-plane interruption。
* 是否影响 Run-2 安全: 低到中。云端 compare 未见 orphan direct product commit，但本地 ref reset 只能由 Codex 自报。
* audit verdict: `concern`

### 偏移 5 — #198 non-run commit interleaved but report 未显式说明

* 描述: compare baseline→final 含 #198 readback 文件，但 Run-1 checkpoint 只列 199-206。
* Codex 是否提到: 没在 RUN-1 report 明确提到。
* 是否 commander 允许 self-recovery: 不属于 Codex Run-1 scope；用户已明确 #198 user-authorized，不计入 deviation。
* 是否影响 Run-2 安全: 低；但影响后续外审读 compare 时的可解释性。
* audit verdict: `concern`

---

## 6. Detailed evidence notes by charter

### A. Authority untouched

`compare 82481b1...9d90d0a` 未出现 authority four-file，PR #199-#203 仅 docs/research，#204-#206 改 services/tests/golden；RUN report 也明确列 `docs/current.md`、`docs/task-index.md`、`docs/decision-log.md`、`AGENTS.md` untouched。

Verdict: `clear`.

### B. Hard redlines

Final-state code confirms:

* `main.py` imports and mounts `bridge_router` but does not add runtime tools.
* `bridge/config.py` returns `write_enabled=False` in both unset and configured paths.
* `BridgeVaultCommitResponse.write_enabled` is `Literal[False]`.
* golden schema includes `/bridge/health`, `/bridge/vault/config`, preview and commit paths, and `write_enabled_const=false`.

Verdict: `clear`.

### C. LP-12 deferral

truth-conflict 文件有 4 行 conflict_table；resolution 明确记录 user clarification：“stage table is advisory, dispatch §3 dependencies are authoritative”；current verdict `resolved_for_run1_continue`; PRs opened/merged at conflict time均为 0。

Verdict: `clear`.

### D. PF-LP-02 expansion

No true write was introduced: renderer adds preview-only body lines and explicit `write_enabled: false`; it does not create files or call filesystem write APIs.
However, §4 scope was breached because `files_to_modify` was empty.

Verdict: `reject`.

### E. PF-LP-13 conftest

`tests/conftest.py` only adds `--golden` option plumbing, 10 lines, no fixture side effect.
But it is absent from PF-LP-13 §4 allowed files.

Verdict: `concern`.

### F. PF-LP-01 dedup

Dedup removes duplicated manual router includes from existing tests; no key assertion deletion is visible in sampled patches.
New `test_main_app_routers.py` adds the W-LP01-Δ assertions: route paths, health blocked_by, commit schema/write_enabled false.

Verdict: `concern`.

### G. Interruption residue

compare ahead_by=11 and includes #198 readback file plus Run-1 files.
Given user explicitly authorized #198 as non Run-1, this is not reject, but report could be clearer.

Verdict: `concern`.

### H. Baseline completeness

CHECKPOINT records baseline and final SHA, 8 completed dispatches, deferred PF-LP-12, high-blast clean.
No Run-1 receipt claims #197/#198 as stage outputs.

Verdict: `clear`.

### I. Receipt consistency

RUN report stage_receipts, DIFF-BUNDLE pr_bundle, CHECKPOINT prs_merged all agree on 8 PRs (#199-#206).

Verdict: `clear`.

### J. Frontmatter status

Sampled docs use candidate/not-authority; _PACK-DEFAULTS and _SHARED-STOP-LINES also remain candidate/not-authority.

Verdict: `clear`.

### K. Commander prompt execution

Codex followed truth-conflict stop/rescope protocol for PF-LP-12. It produced the three required handoff artifacts: RUN report, diff bundle, checkpoint.
Concern remains around self-recovery crossing §4.

Verdict: `concern`.

### L. W-LP01-Δ assertion count

* PF-LP-01: route paths + health response + commit schema/runtime write flag assertions.
* PF-LP-02: capture_id + body_markdown 20+ lines + unset vault root failure/write flag assertions.
* PF-LP-13: golden equality + schema field lists + write_enabled false / preview excerpt runtime assertions.

Verdict: `clear`.

---

## 7. 末尾必填字段

```text
audit_completed_at: 2026-05-06T00:00:00Z
auditor_confidence: medium-high
ready_for_run_2: no
amendments_needed_before_run_2:
  - PF-LP-02 scope repair/amendment: explicitly account for production code changes to bridge/vault_preview.py and vault/renderer.py, or mark PR #205 as partial_scope_deviation before proceeding.
  - PF-LP-13 scope amendment: either whitelist tests/conftest.py for golden plumbing or move option handling into test-local code.
  - PF-LP-01 companion-test amendment: explicitly allow de-dup edits to existing bridge contract tests when mounting router globally.
  - Add supersession note to #199 live-authority-readback doc: valid at PR194 boundary only; bridge mount fact superseded by #204.
  - Add compare-boundary note that #198 is user-authorized non-Run-1 interleaving commit, excluded from Run-1 receipt.
amendments_needed_during_run_2:
  - Run-2 commander prompt must require strict §4 allowed_paths enforcement; if proof requires production expansion, stop and write scope amendment first.
  - Any slot-local recovery that modifies production code outside §4 must be recorded as partial or require user gate.
followup_audit_after_run_2: required
```

## Final one-line verdict

`REJECT_AS_SCOPE_DRIFT`: Run-1 preserved major safety boundaries, but PF-LP-02 / PR #205 materially violated dispatch §4 allowed_paths, so Run-2 should not start until scope amendments are applied.
