---
title: Run-1 Amendment Commander Prompt — Codex CLI Unattended Execution
status: candidate / commander_prompt / not-authority
created_at: 2026-05-06
target_branch: codex/run1-amendments
target_baseline: origin/main (post-9d90d0a)
audit_inputs:
  - gpt-pro-independent-a (Web GPT Pro, REJECT)
  - gpt-5-codex-cloud (Codex 5.5 cloud, REJECT)
  - hermes-kimi (V-PASS_WITH_AMENDMENTS)
synthesis_verdict: REJECT_AS_SCOPE_DRIFT
synthesis_decision: amend_and_proceed (no rollback; record as accepted_partial_scope_deviation)
ready_for_run_2_after_merge: yes
---

# Mission

Run-1 (PR #199–#206) 已 closed：authority 未碰、硬红线（write_enabled=False、无 subprocess/playwright/migration/BBDown）全部守住，但 **PF-LP-01 / PF-LP-02 / PF-LP-13 三个 dispatch 都越了 §4 allowed_paths**。三家外审里 2/3 给 REJECT，1/3 给 V-PASS_WITH_AMENDMENTS（仅因未读到 handoff receipts）。

**Run-2 已先行**（PF-LP-04、PF-LP-05 已 merged 到 main，`codex/run2-pf-lp-06` 仍在 work-in-progress）。Amendment 必须在 worktree 里做，**严禁** 触碰 `codex/run2-pf-lp-06`。

本 prompt 让 Codex CLI 在一个 PR 里完成：

1. 持久化 3 份外部审计报告到 `docs/research/post-frozen/audits/`
2. 写一份 `RUN-1-AMENDMENT-LEDGER` 收录 8 项 findings + 决策（KEEP / 修复 / note-only）
3. 给 #199 doc 加 supersession header（PR194 boundary 标记）
4. 写 `run-2-commander-prompt-template-rules` — 硬 stop-line：proof requires production expansion → STOP and amend §4 first
5. 4 个并行子审计 sub-agent 复核 → 全 PASS 才 auto-merge

# Stop lines（HARD — 任一违反 = 立即 abort + 报告）

- ❌ 不修改 authority 四件套：`docs/current.md`、`docs/task-index.md`、`docs/decision-log.md`、`AGENTS.md`
- ❌ 不触碰 `services/api/**`、`apps/**`、`workers/**`、`packages/**`、`data/**`、`referencerepo/**`
- ❌ 不引入 runtime tools / write paths / migration / browser automation
- ❌ 不直 push 到 main
- ❌ 不超过 1 个 PR
- ❌ 不 cherry-pick / 不 merge `codex/run2-pf-lp-06`（Run-2 work-in-progress 不许碰）
- ❌ 不在主仓库 working tree 操作（必须 worktree）
- ⚠️ 若发现 3 份审计未覆盖的新 finding，STOP + 写 truth-conflict + 等用户裁决

# Allowed paths（CREATE / MODIFY 全清单）

CREATE：

- `docs/research/post-frozen/audits/run-1-audit-gpt-pro-independent-a-2026-05-06.md`
- `docs/research/post-frozen/audits/run-1-audit-gpt-5-codex-cloud-2026-05-06.md`
- `docs/research/post-frozen/audits/run-1-audit-hermes-2026-05-06.md`
- `docs/research/post-frozen/runs/RUN-1-AMENDMENT-LEDGER-2026-05-06.md`
- `docs/research/post-frozen/run-2-commander-prompt-template-rules-2026-05-06.md`
- `docs/research/post-frozen/runs/RUN-1-AMENDMENT-RUN-REPORT-2026-05-06.md`
- `docs/research/post-frozen/runs/DIFF-BUNDLE-Amendment-2026-05-06.md`
- `docs/research/post-frozen/runs/CHECKPOINT-Amendment-final.json`

MODIFY（仅 append / frontmatter 头部追加，禁止删改既有正文）：

- `docs/research/post-frozen/live-authority-readback-after-pr194.md`（加 supersession 头部 + frontmatter `superseded_by`）

# 8 项收敛 findings → 决策矩阵

| ID | Finding | 严重 | 三方一致？ | 决策 | 落地动作 |
|----|---------|------|----------|------|---------|
| A1 | PF-LP-02 / #205 改了 `services/api/scoutflow_api/bridge/vault_preview.py` + `services/api/scoutflow_api/vault/renderer.py` + `tests/contracts/test_vault_renderer_contract.py` + `tests/fixtures/vault_inbox/expected_scoutflow_note.md`，§4 `files_to_modify: []` | CRITICAL | ✓ | **KEEP** as `accepted_partial_scope_deviation` — 无 true write 语义；preview-only draft shape 是 ≥20 line excerpt 的 proof 必需 | Ledger A1 + Run-2 stop-line（A7） |
| A2 | PF-LP-13 / #206 加了 `tests/conftest.py`（10 行 `--golden` plumbing），§4 未列 | HIGH | ✓ | **KEEP** as `accepted_partial_scope_deviation` — minimal、无 autouse、无 side effect | Ledger A2 + 未来规则：dispatch §4 必须显式列 conftest |
| A3 | PF-LP-01 / #204 改了 5 个既有 bridge contract tests（删 manual `app.include_router(bridge_router)`），§4 未列 | MEDIUM | ✓ | **KEEP** as `accepted_partial_scope_deviation` — assertions 完整保留；机械 de-dup | Ledger A3 + 未来规则：companion-test edits 必须 declared |
| A4 | #199 live-authority-readback 称 "create_app() does not mount bridge_router"，但 final main 已 mount（#204 落地） | MEDIUM | ✓ (gpt-pro / gpt-5.5) | 加 supersession 头部 | 修改 #199 doc frontmatter + 顶部加 ⚠️ supersession block |
| A5 | #198 readback 文件出现在 baseline→final compare 区间，但 Run-1 receipts 只列 #199–#206 | MEDIUM | ✓ (gpt-pro / gpt-5.5) | Ledger note + handoff boundary 注解 | Ledger A5（若 RUN-1 report 已在 main 则 modify；否则只在 ledger 记） |
| A6 | Frontmatter J 规则对 fixture markdown vs governance markdown 的语义不清 | MEDIUM | ✓ (gpt-5.5) | 在 ledger 里给出明文规则：J 仅适用于 `docs/research/**`，fixture markdown 豁免 | Ledger A6 |
| A7 | Run-2 commander template 缺 stop-line：proof requires production expansion → STOP & amend §4 first | LOW (preventive) | ✓ (gpt-pro / gpt-5.5) | 新文件 `run-2-commander-prompt-template-rules-2026-05-06.md` 锁三条强制规则 | 见 Appendix C |
| A8 | PR body shell-safe quotes（`python -c` 片段缺引号） | LOW | gpt-pro 单独 | Note only | Ledger A8（无独立修复 PR） |

**全局裁决（charter D 严格 + amend_and_proceed 务实）：** `REJECT_AS_SCOPE_DRIFT`，但通过本 PR 追认 A1/A2/A3 为 `accepted_partial_scope_deviation` + 锁 A4/A5/A6 + 前置 A7 stop-line 后，Run-1 状态升级为 `closed_with_accepted_amendments`，Run-2 可继续。

# Step-by-step 执行协议

## Step 0 — Pre-flight dry-run preview（≤2 min，不写文件）

```bash
git fetch --all --prune
git rev-parse origin/main                                  # 确认是 9d90d0a 或其后裔
git log --oneline origin/main -5                           # 看最近 commit
gh pr list --state open --limit 5
git branch --list 'codex/run1-amendments'                  # 不应存在
git worktree list                                          # 看现有 worktree
ls docs/research/post-frozen/runs/ 2>/dev/null             # 看 RUN-1 receipts 是否已在 main
```

输出三段 preview（强制）：

```
files_to_create:
  - [5 个新文件]
files_to_modify:
  - docs/research/post-frozen/live-authority-readback-after-pr194.md
files_will_NOT_touch:
  - docs/current.md
  - docs/task-index.md
  - docs/decision-log.md
  - AGENTS.md
  - services/**
  - apps/**
  - workers/**
  - packages/**
  - data/**
  - referencerepo/**
  - codex/run2-pf-lp-06 分支上的任何文件
```

## Step 1 — Worktree 隔离（不干扰 Run-2）

```bash
git worktree add -b codex/run1-amendments ../scoutflow-run1-amend origin/main
cd ../scoutflow-run1-amend
git status   # 必须干净
```

## Step 2 — 持久化 3 份外部审计报告

用户会在 prompt 后追加 3 份审计原文（Appendix A1 / A2 / A3）。逐字写入：

- `docs/research/post-frozen/audits/run-1-audit-gpt-pro-independent-a-2026-05-06.md`
- `docs/research/post-frozen/audits/run-1-audit-gpt-5-codex-cloud-2026-05-06.md`
- `docs/research/post-frozen/audits/run-1-audit-hermes-2026-05-06.md`

每份保留原 frontmatter（`status: candidate / external_audit / not-authority`），不改正文。

## Step 3 — 写 Amendment Ledger（CREATE）

路径：`docs/research/post-frozen/runs/RUN-1-AMENDMENT-LEDGER-2026-05-06.md`

模板见 Appendix B。8 项 findings 各一节，按上表决策矩阵填。**每节必须含**：

- `finding_id` / `severity` / `auditor_consensus`（哪几家提到）
- `evidence_paths`（具体文件 + line 范围）
- `decision`：`KEEP_AS_ACCEPTED_PARTIAL_SCOPE_DEVIATION` / `DOC_FIX` / `RULE_CLARIFICATION` / `NOTE_ONLY`
- `rationale`（为什么 keep / 为什么不 rollback）
- `forward_rule`（未来 dispatch 必须遵守的新规则，A1–A3 / A6 / A7 必填）

## Step 4 — 给 #199 doc 加 supersession（MODIFY）

文件：`docs/research/post-frozen/live-authority-readback-after-pr194.md`

frontmatter 追加：

```yaml
superseded_by:
  - PR #204 for "create_app() bridge_router mount" fact (since 2026-05-06)
valid_at_pr194_boundary_only: true
```

正文最顶（在 frontmatter 后、原 H1 前）插一个块：

```markdown
> ⚠️ **Supersession note (added 2026-05-06)**：本文档捕获的是 **PR #194 boundary** 的 live truth。PR #204 已经在 `create_app()` 中 mount `bridge_router`。当前路由真相请以 `services/api/scoutflow_api/main.py` + golden contract `tests/contracts/golden/bridge-openapi-2026-05-06.json` 为准。本文档保留作为 PR194 时点存档，不是当前 truth source。
```

不修改正文其他部分。

## Step 5 — 写 Run-2 commander template 规则文件（CREATE）

路径：`docs/research/post-frozen/run-2-commander-prompt-template-rules-2026-05-06.md`

frontmatter：`status: candidate / commander_template_rules / not-authority`

正文按 Appendix C 完整写入（3 条强制规则 + 1 truth-conflict 路径 + 1 适用范围段）。

## Step 6 — 5 条本地验证（必须全过才进 Step 7）

```bash
# 1) Authority untouched
git diff origin/main...HEAD -- docs/current.md docs/task-index.md docs/decision-log.md AGENTS.md
# Expected: empty

# 2) 没碰 production code / runtime
git diff --name-only origin/main...HEAD | grep -E '^(services/|apps/|workers/|packages/|data/|referencerepo/)' || echo "PASS: no production code"
# Expected: PASS line

# 3) 全部新 .md 都有 not-authority frontmatter
for f in docs/research/post-frozen/audits/run-1-audit-*-2026-05-06.md \
         docs/research/post-frozen/runs/RUN-1-AMENDMENT-LEDGER-2026-05-06.md \
         docs/research/post-frozen/run-2-commander-prompt-template-rules-2026-05-06.md; do
  head -10 "$f" | grep -q 'not-authority' || echo "FAIL: $f"
done
# Expected: 无 FAIL 输出

# 4) 无禁词泄漏（除 audit 引用语境）
rg -n 'subprocess\.(run|Popen)|playwright|puppeteer|selenium|alembic|BBDown|yt-dlp|ffmpeg' \
   docs/research/post-frozen/runs/RUN-1-AMENDMENT-LEDGER-2026-05-06.md \
   docs/research/post-frozen/run-2-commander-prompt-template-rules-2026-05-06.md
# Expected: empty（audit 文件里命中是引用证据，可接受）

# 5) #199 doc supersession header 已写入
grep -q 'Supersession note (added 2026-05-06)' docs/research/post-frozen/live-authority-readback-after-pr194.md && echo "PASS"
# Expected: PASS
```

## Step 7 — 提交 + 开 PR（仅当 Step 6 全过）

```bash
git add docs/research/post-frozen/
git commit -m "docs(post-frozen): land Run-1 amendment ledger + 3 external audits

- Persist 3 external audit reports (gpt-pro, gpt-5.5, hermes) as candidate / not-authority
- Amendment ledger covers 8 findings (A1-A8): 3 KEEP-as-partial-scope-deviation, 5 process/doc fixes
- Supersession note added to #199 live-authority-readback (PR194 boundary marker)
- Run-2 commander template rules: 'proof-requires-production-expansion -> STOP and amend §4'
- Authority files untouched; no production code touched"

git push -u origin codex/run1-amendments

gh pr create \
  --title "docs(post-frozen): Run-1 amendment ledger + 3 external audits" \
  --body "$(cat <<'EOF'
## Summary

Lands Run-1 amendment ledger + 3 external audit reports + supersession notes + Run-2 stop-line rules. Docs-only PR; no production code changes.

## External audit synthesis

| Auditor | Verdict | 主要 reject 点 |
|---------|---------|--------------|
| gpt-pro-independent-a | REJECT | PF-LP-02 §4 越界（charter D） |
| gpt-5-codex-cloud (5.5) | REJECT | PF-LP-02 §4 越界（charter D） |
| hermes-kimi | V-PASS_WITH_AMENDMENTS | 仅未读到 run1-audit-handoff receipts |

**Synthesis verdict**: `REJECT_AS_SCOPE_DRIFT`
**Synthesis decision**: `amend_and_proceed` — KEEP + 追认 A1/A2/A3 为 `accepted_partial_scope_deviation`，不 rollback（无 true write、无 runtime/migration、无 authority drift；rollback 会破 Run-2 已 wired 的 preview 消费）

## Amendment ledger 8 项

- **A1 [CRITICAL]** PF-LP-02 / #205 production code expansion → KEEP
- **A2 [HIGH]** PF-LP-13 / #206 conftest.py → KEEP
- **A3 [MEDIUM]** PF-LP-01 / #204 contract test de-dup → KEEP
- **A4 [MEDIUM]** #199 supersession note
- **A5 [MEDIUM]** #198 boundary note
- **A6 [MEDIUM]** Frontmatter J 规则澄清（governance md vs fixture md）
- **A7 [LOW]** Run-2 stop-line：proof-requires-production-expansion → STOP and amend §4
- **A8 [LOW]** PR body shell-safe quotes（note only）

## Authority + redline 状态

- ✅ Authority files untouched
- ✅ 硬红线全过（无 subprocess/playwright/migration/BBDown）
- ✅ write_enabled=False 维持
- ✅ Allowed paths 严守（仅 docs/research/post-frozen/**）

## Sub-agent 4 维独立审计

- [ ] Sub-agent 1 — Authority + redline scan
- [ ] Sub-agent 2 — Frontmatter compliance
- [ ] Sub-agent 3 — Cross-reference completeness（3 审计 → 8 ledger）
- [ ] Sub-agent 4 — Run-2 stop-line semantic review

全 PASS → auto-merge。任一 concern/reject → 不 merge，写 fail report 等用户裁决。

## Test plan

- [x] `git diff origin/main...HEAD -- docs/current.md docs/task-index.md docs/decision-log.md AGENTS.md` → empty
- [x] `git diff --name-only origin/main...HEAD | grep -E '^(services/|apps/|workers/|packages/)'` → empty
- [x] 5 项本地验证（Step 6）全过

EOF
)"
```

记下 PR number 供 Step 8 / Step 9 使用。

## Step 8 — 4 个并行 sub-agent 独立审计

启 4 个 Codex sub-agent slot 并发跑。每个传入：本 prompt 路径 + PR number + worktree 路径。每个独立给 verdict（`clear` / `concern` / `reject`）+ evidence 行号引用。

### Sub-agent 1 — Authority + Redline Scan

任务：复核 authority 四件套、production 目录、禁词全部干净。
独立跑：

```bash
git fetch origin
git diff origin/main...HEAD -- docs/current.md docs/task-index.md docs/decision-log.md AGENTS.md
git diff --name-only origin/main...HEAD | grep -E '^(services/|apps/|workers/|packages/|data/|referencerepo/)'
rg -n 'subprocess\.(run|Popen)|playwright|puppeteer|selenium|alembic' docs/research/post-frozen/runs/RUN-1-AMENDMENT-LEDGER-2026-05-06.md docs/research/post-frozen/run-2-commander-prompt-template-rules-2026-05-06.md
```

PASS：3 条全空。
verdict：`clear` / `concern` / `reject`

### Sub-agent 2 — Frontmatter Compliance

任务：5 个新 .md 文件 frontmatter 全含 `not-authority`；audit 报告 status 字段为 `candidate / external_audit / not-authority`；ledger / template-rules 为 `candidate / ... / not-authority`。
PASS：每个文件 frontmatter 第 1–10 行内出现 `not-authority` 一次以上。
verdict：`clear` / `concern` / `reject`

### Sub-agent 3 — Cross-reference Completeness

任务：读 3 份 audit 报告 + ledger，逐条核对 audit 里每条 finding 是否映射到 A1–A8。
关键交叉：

- gpt-pro Finding 1–7 → 全部映射
- gpt-5.5 Finding 1–7 → 全部映射
- hermes Finding 1–2 → 全部映射
- 任一 audit 提到但 ledger 漏的 finding → reject

PASS：零未映射。
verdict：`clear` / `concern` / `reject`

### Sub-agent 4 — Run-2 Stop-line Semantic Review

任务：读 `run-2-commander-prompt-template-rules-2026-05-06.md`。验证：

1. 显式 STOP 动词（不是 "should consider"）
2. 触发条件清晰（"proof requires modifying files outside dispatch §4 allowed_paths"）
3. 给出后续路径（write truth-conflict + request user re-scope）
4. 适用于所有 future Run-N（不止 Run-2）

PASS：4 项全满足。
verdict：`clear` / `concern` / `reject`

## Step 9 — Auto-merge 协议

**全 4 个 sub-agent 返回 `clear`：**

```bash
gh pr merge <PR-number> --squash --delete-branch
cd /Users/wanglei/workspace/ScoutFlow
git fetch --all --prune
git worktree remove ../scoutflow-run1-amend
```

写最终 3 件 receipt：

- `docs/research/post-frozen/runs/RUN-1-AMENDMENT-RUN-REPORT-2026-05-06.md`
- `docs/research/post-frozen/runs/DIFF-BUNDLE-Amendment-2026-05-06.md`
- `docs/research/post-frozen/runs/CHECKPOINT-Amendment-final.json`

（这 3 件可在 PR 里就写好；merge 后只在主仓 fetch 验证）

**任一 sub-agent 返回 `concern` 或 `reject`：**

- 不 merge
- 在 PR comment 里贴 4 个 sub-agent verdict + evidence
- 写 `RUN-1-AMENDMENT-AUDIT-FAIL-REPORT-2026-05-06.md` 到 PR
- STOP 等用户裁决

# 成功收口判断

`Amendment PR merged` + `4 sub-agent 全 clear` + `Run-2 stop-line 已锁` → Run-1 升级为 `closed_with_accepted_amendments`，Run-2 (PF-LP-06+) 可继续。

---

# Appendix A — 3 份外部审计原文

> 用户会在本 prompt 后追加 3 份审计原文。Codex 把它们逐字写入对应路径，不做任何编辑或重排，仅在 frontmatter 缺失时补上 `status: candidate / external_audit / not-authority`。

- A1：`docs/research/post-frozen/audits/run-1-audit-gpt-pro-independent-a-2026-05-06.md`
- A2：`docs/research/post-frozen/audits/run-1-audit-gpt-5-codex-cloud-2026-05-06.md`
- A3：`docs/research/post-frozen/audits/run-1-audit-hermes-2026-05-06.md`

---

# Appendix B — Amendment Ledger 模板（写入 RUN-1-AMENDMENT-LEDGER-2026-05-06.md）

```markdown
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

- severity: CRITICAL
- auditor_consensus: gpt-pro / gpt-5.5 / hermes
- dispatch_reference: `docs/research/post-frozen/80-pack-source/02_task_packs/PF-localhost-preview-pack/dispatches/PF-LP-02-bridge-preview-route-smoke-tests.md` §4
- §4 allowed: 仅 create `tests/api/test_bridge_vault_preview_smoke.py`，`files_to_modify: []`
- evidence_paths（PR #205 实际改）：
  - `services/api/scoutflow_api/bridge/vault_preview.py`
  - `services/api/scoutflow_api/vault/renderer.py`
  - `tests/contracts/test_vault_renderer_contract.py`
  - `tests/fixtures/vault_inbox/expected_scoutflow_note.md`
- decision: `KEEP_AS_ACCEPTED_PARTIAL_SCOPE_DEVIATION`
- rationale: 无 true write 语义；preview-only draft shape 是 ≥20 line excerpt proof bar 的必需扩展；rollback 会破坏 Run-2 已 wired 的 capture-station preview 消费链路（PF-LP-04/05 已落 main）
- forward_rule: 任何 future dispatch 若 proof requirement 与 §4 allowed_paths 冲突，**必须 STOP + 写 truth-conflict + 等用户 re-scope**，不许 silently 扩 path（详见 Run-2 commander template rules A7）

## A2 — PF-LP-13 / PR #206：tests/conftest.py 越 §4

- severity: HIGH
- auditor_consensus: gpt-pro / gpt-5.5 / hermes
- §4 allowed: 仅 create golden contract test + golden JSON
- evidence: `tests/conftest.py` 新增（10 行 `--golden` plumbing，无 autouse、无 monkeypatch）
- decision: `KEEP_AS_ACCEPTED_PARTIAL_SCOPE_DEVIATION`
- rationale: minimal 实现，无 side effect
- forward_rule: dispatch §4 若需 pytest shared option，必须显式列 `tests/conftest.py`；或把 option 改为 test-local 处理

## A3 — PF-LP-01 / PR #204：contract test de-dup 越 §4

- severity: MEDIUM
- auditor_consensus: gpt-pro / gpt-5.5 / hermes
- §4 allowed: 仅 create `tests/api/test_main_app_routers.py` + modify `main.py` / `bridge/schemas.py` / `bridge/vault_commit.py`
- evidence: PR #204 改了 5 个既有 bridge contract tests（删 manual `app.include_router(bridge_router)`），但 §8 关键 assertions 完整保留
- decision: `KEEP_AS_ACCEPTED_PARTIAL_SCOPE_DEVIATION`
- rationale: 机械 de-dup（避免 double-mount warnings），coverage 未丢
- forward_rule: companion-test edits 必须在 dispatch §4 declared 或在执行后 30min 内补 amendment

## A4 — #199 live-authority-readback supersession

- severity: MEDIUM
- auditor_consensus: gpt-pro / gpt-5.5
- evidence: #199 doc 称 `create_app() does not mount bridge_router`，但 PR #204 已 mount
- decision: `DOC_FIX`
- action: 在 #199 doc frontmatter 加 `superseded_by: PR #204 ...` + `valid_at_pr194_boundary_only: true`，正文顶部加 ⚠️ supersession block

## A5 — #198 boundary note

- severity: MEDIUM
- auditor_consensus: gpt-pro / gpt-5.5
- evidence: PR #198 readback 文件出现在 baseline (82481b1) → final (9d90d0a) compare 区间，但 Run-1 receipts 只列 #199–#206
- decision: `RULE_CLARIFICATION`
- action: 在本 ledger 内显式记录："PR #198 是 user-authorized non-Run-1 interleaving commit，包含在 compare 区间但不计入 Run-1 stage receipts"
- forward_rule: future Run-N handoff report 必须在 receipt 段后追加 `compare_boundary_notes` 字段，列出区间内非本 Run 的 user-authorized commits

## A6 — Frontmatter J 规则澄清

- severity: MEDIUM
- auditor_consensus: gpt-5.5
- decision: `RULE_CLARIFICATION`
- new_rule: J 检查（frontmatter status 必为 candidate / not-authority 或 evidence / run_report / not-authority）**仅适用于** `docs/research/**` 下的 governance markdown。`tests/fixtures/**` 下的 fixture markdown 豁免（其 frontmatter 是测试数据，不是治理状态）

## A7 — Run-2 commander template stop-line（preventive）

- severity: LOW (preventive)
- auditor_consensus: gpt-pro / gpt-5.5
- decision: `RULE_CLARIFICATION`
- action: 创建 `docs/research/post-frozen/run-2-commander-prompt-template-rules-2026-05-06.md`
- 该文件锁三条强制规则：
  1. dispatch §4 allowed_paths 是窄合同，不许 slot-local 扩张
  2. 若 proof requires production expansion → STOP + 写 truth-conflict + 等用户 re-scope
  3. 任何 §4 外修改 = scope_deviation_flag=yes，必须在 PR body / RUN report 单列 + 单审

## A8 — PR body shell-safe quotes

- severity: LOW
- auditor_consensus: gpt-pro
- decision: `NOTE_ONLY`
- note: PR #204 body 含 `python -c "assert /bridge/health in paths"` 类无引号片段，作为 shell command 不可直接执行。后续 commander prompt 应在 PR body 模板里强制 single-quote shell-safe wrapping。无独立修复 PR。

# Run-1 final state

- `closed_with_accepted_amendments`
- `ready_for_run_2`: yes
- Run-2 必须遵守 `run-2-commander-prompt-template-rules-2026-05-06.md`
```

---

# Appendix C — Run-2 commander template rules 文件正文

```markdown
---
title: Run-N Commander Template Rules — §4 Enforcement
status: candidate / commander_template_rules / not-authority
created_at: 2026-05-06
applies_to: Run-2 onward (and any future post-frozen multi-dispatch run)
upstream_audit: docs/research/post-frozen/runs/RUN-1-AMENDMENT-LEDGER-2026-05-06.md
---

# Why this exists

Run-1 三个 dispatch 同型越 §4 allowed_paths（PF-LP-01 / -02 / -13）。这不是个例，是 contract enforcement 缺位的 systemic 问题：当 proof requirement（如 ≥20 line excerpt）与 §4 allowed_paths 冲突时，Codex 默认扩 path 而非停下来 amend。本规则文件锁住未来 Run-N 的 stop-line。

# Three hard rules（任一违反即 dispatch reject）

## Rule 1 — §4 是窄合同

dispatch §4 `files_to_create` / `files_to_modify` 是**穷举清单**，不是示例。任何不在清单内的文件修改 = scope deviation。

## Rule 2 — Proof-requires-production-expansion → STOP

**若执行过程中发现 proof requirement（assertion bar / line count bar / coverage bar）必须修改 §4 外的 production code 才能满足：**

1. **STOP**（不许扩张 §4，不许 slot-local self-recovery 跨 production 边界）
2. 在 worktree 写 truth-conflict 文件：`docs/research/post-frozen/runs/RUN-{N}-truth-conflict-{date}.md`
3. 在 truth-conflict 里列：dispatch §4 allowed paths / proof requirement / 实际需要的扩展 paths / 推荐的 amendment 文本
4. 提交 truth-conflict 到 dispatch 自己的 worktree branch（不 push 到 main）
5. 在 PR comment 或 commander prompt stdout 报告：`STOP: proof_requires_production_expansion / truth_conflict_at <path>`
6. 等用户裁决：`approve_amendment` / `descope_proof_bar` / `defer_to_next_run` / `roll_back`
7. **不许在没有用户 verdict 的情况下继续 merge**

## Rule 3 — §4 外的修改必须 declared

哪怕只是测试 helper de-dup / conftest plumbing / fixture sync，只要文件不在 §4 清单内：

- 在 PR body 单独一节 `Scope Deviations`（不是埋在 RUN report 里）
- 列：file_path / 修改性质 / coverage 影响 / 是否引入新 contract
- `scope_deviation_flag: yes` 自动触发 sub-agent 4-D 独立审（authority / redline / coverage / contract）
- 任一 sub-agent reject → 不 auto-merge

# Truth-conflict 文件模板

```markdown
---
title: Run-{N} Truth Conflict — {dispatch_id} proof_vs_§4
status: candidate / truth_conflict / not-authority
created_at: {date}
dispatch_id: {dispatch_id}
stop_verdict: blocked_on_truth_conflict
---

## §4 allowed_paths
- {list}

## Proof requirement
- {assertion / line count / coverage bar}

## What proof actually requires
- {production paths needed}

## Recommended amendment
- {dispatch §4 patch text}

## Awaiting user verdict
- [ ] approve_amendment
- [ ] descope_proof_bar
- [ ] defer_to_next_run
- [ ] roll_back

stop_verdict: blocked_on_truth_conflict / awaiting_user
```

# 适用范围

- 所有 post-frozen Run-N（Run-2、Run-3 ...）
- 所有 80-pack cluster dispatch（PF-LP-* / PF-C0-* / PF-O1-* / PF-META-* ...）
- 所有 high-blast 与 normal-blast dispatch（不区分）

# 与现有 _PACK-DEFAULTS / _SHARED-STOP-LINES 关系

- 本文件不修改 _PACK-DEFAULTS / _SHARED-STOP-LINES（authority-adjacent，本 PR 不碰）
- 本文件作为 candidate / commander_template_rules / not-authority 存在
- 下一次 _PACK-DEFAULTS authority 升级窗口（由 ledger owner 负责）可考虑把 Rule 1/2/3 promote 为 authority-locked

# Forward path

- Run-2 commander prompt 必须在顶部 reference 本文件
- 任何未引用本文件规则的 commander prompt = invalid，不许执行
```

---

# 终止条件 / 错误处理

| 情况 | Codex 应做 |
|------|----------|
| Step 0 dry-run 发现 worktree 已存在或有冲突 | `git worktree remove --force` 后重试；2 次失败 → STOP 报告 |
| Step 1 创建 worktree 失败 | STOP，不要 fallback 到主 working tree |
| Step 6 任一验证失败 | 不 commit、不 push；写 fail-reason 到 stdout，等用户介入 |
| Step 8 任一 sub-agent reject | 不 merge；按 Step 9 写 fail report |
| 任意时刻发现要碰 authority / production / Run-2 分支 | 立即 STOP，不许继续 |
| 用户在 Step 8 期间手动 push 新 commit 到 codex/run1-amendments | 重跑 Step 6 + Step 8 全 4 个 sub-agent |

# 一行 success line

`Run-1 closed_with_accepted_amendments → Run-2 (PF-LP-06+) cleared to proceed under §4 hardened stop-line.`
