---
title: Run-2 + Window-2 External Audit Prompt — 3-Window Cloud Triangulation
status: candidate / audit-prompt / not-authority
created_at: 2026-05-06
target_writer: 3 independent cloud auditors (Hermes / GPT Pro web / Codex CLI fresh window)
project_root: /Users/wanglei/workspace/ScoutFlow
github_repo: https://github.com/RayWong1990/ScoutFlow
audit_baseline_sha: 9d90d0a436ee756bfc31dde4616f14b326a540c3
audit_final_sha: 8cf334905ef1dda388737680bf27c552260a9a9b
audited_runs: [Run-2, Window-2]
audited_prs_run2: [207, 216, 226, 228, 230, 231, 232, 233, 234, 235, 236, 237, 238]
audited_prs_window2: [208, 209, 210, 211, 212, 213, 214, 215, 217, 218, 219, 220, 221, 222, 223, 224, 225, 227]
known_user_authorized_amendment: PR #231 (Run-1 amendment ledger + 3 external audits)
---

# Run-2 + Window-2 严格外审 Commander Prompt — 3 窗口云端三角验证

> 把下面 `<<<AUDIT BEGIN>>>` ... `<<<AUDIT END>>>` 段同时粘到 3 个独立云端窗口（Hermes / GPT Pro web / Codex CLI fresh window）。
> 所有输入都是 **GitHub URL**（receipts 已全部 merged 到 `main`）。
> 每个审计员独立审、独立写报告，user 三角对比。

---

## 派单前必跑（一次，把审计 prompt 推到 GitHub）

```bash
cd /Users/wanglei/workspace/ScoutFlow
git fetch origin --prune
git checkout -b run2-audit-handoff origin/main

git add docs/research/post-frozen/run-2-resume-codex-commander-prompt-2026-05-06.md \
        docs/research/post-frozen/run-2-external-audit-prompt-2026-05-06.md

git commit -m "chore(post-frozen): snapshot Run-2 audit prompt + resume prompt for external audit"
git push -u origin run2-audit-handoff
```

> 不开 PR、不 merge — 只推分支让云端 fetch。

---

## 已锁事实（审计员开工前 user 已确认，不要再质疑）

- **baseline → final**: `9d90d0a` → `8cf3349`（Run-1 收口 → Run-2 + Window-2 双线收口）
- **Run-2 (frontend wiring + closeout)**: 14 dispatches LP-04..18，13 PR (含 #231 amendment) 全 merged
- **Window-2 (docs only)**: 17 dispatches PF-C3 + PF-GLOBAL，18 PR 全 merged（含 #227 receipt bundle）
- **PR #231 amendment ledger**: user 看完 Run-1 三方外审 (gpt-pro REJECT / gpt-5-codex REJECT / hermes V-PASS_WITH_AMENDMENTS) 后授权 Codex "amend_and_proceed" KEEP without rollback。**审计员不需要再质疑这个上层决策**，但需要核 amendment ledger 是否如实记录所有 finding
- **Synthetic UAT-1**: user 显式授权 partial-evidence 模式（不本地手跑浏览器）— Codex curl + pnpm JSDOM 跑 smoke 取真值，verdict=works。**审计员核诚实度，不质疑 partial-evidence 模式本身**

审计员任务是 **核验** Codex 自报，**不是** 重新质疑这 4 条已锁事实。重点放在 **Codex 没声明的隐性偏移 + 6 个待挖问题**（见下文 Charter）。

---

```
<<<AUDIT BEGIN>>>

你是 ScoutFlow Run-2 + Window-2 独立外审员。3 个独立云端窗口同时跑同一段 prompt，user 后续三角对比 verdict。你不知道其它两个 auditor 是谁、不读对方报告（防 anchoring bias）。

## 角色
- 只读 audit。**禁止** 任何 git commit / push / PR / merge / 修改任何文件 / 跑 CI / 跑 pytest / 跑 pnpm
- 你的产出是一份严格证据链 audit report markdown（贴回对话即可）
- 措辞用 T-PASS / V-PASS / partial / FAIL_ENV / REJECT_AS_X / clear / concern / reject — 禁裸 PASS / DONE / OK
- 你的工作完全在云端：fetch 下面所有 GitHub URL，不要假设本地访问

## 项目身份
- repo: https://github.com/RayWong1990/ScoutFlow
- live status: WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED
- baseline_origin_main: `9d90d0a436ee756bfc31dde4616f14b326a540c3`（Run-1 final）
- final_origin_main: `8cf334905ef1dda388737680bf27c552260a9a9b`（Run-2 + Window-2 final）
- Run-2 PR: #207 / #216 / #226 / #228 / #230 / #231 / #232 / #233 / #234 / #235 / #236 / #237 / #238
- Window-2 PR: #208-#225 (skip #216 = Run-2) + #227

## 必读输入（按顺序 fetch）

### 1. Run-2 收尾产物（在 `main` 分支）
- RUN-2 完整报告: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/RUN-2-CODEX0-REPORT-2026-05-06.md
- DIFF-BUNDLE-Run2: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/DIFF-BUNDLE-Run2-2026-05-06.md
- CHECKPOINT-Run2-final: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/CHECKPOINT-Run2-final.json
- UAT-1 evidence: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/evidence/PF-LP-16-manual-localhost-run-2026-05-06.md

### 2. Forensic coverage evidence (LP-09/10/14)
- LP-09: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/RUN-2-LP-09-coverage-evidence-2026-05-06.md
- LP-10: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/RUN-2-LP-10-coverage-evidence-2026-05-06.md
- LP-14: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/RUN-2-LP-14-coverage-evidence-2026-05-06.md

### 3. Window-2 收尾产物（在 `main` 分支）
- RUN-W2-DOCS 报告: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/RUN-W2-CODEX0-DOCS-REPORT-2026-05-06.md
- DIFF-BUNDLE-W2-Docs: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/DIFF-BUNDLE-W2-Docs-2026-05-06.md
- CHECKPOINT-W2-final: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/CHECKPOINT-W2-final.json

### 4. PR #231 Run-1 Amendment 产物（在 `main` 分支，user 已授权 amend_and_proceed）
- Amendment ledger: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/RUN-1-AMENDMENT-LEDGER-2026-05-06.md
- Amendment run report: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/RUN-1-AMENDMENT-RUN-REPORT-2026-05-06.md
- DIFF-BUNDLE-Amendment: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/DIFF-BUNDLE-Amendment-2026-05-06.md
- CHECKPOINT-Amendment-final: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/CHECKPOINT-Amendment-final.json
- Run-1 audit gpt-pro: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/audits/run-1-audit-gpt-pro-independent-a-2026-05-06.md
- Run-1 audit gpt-5-codex-cloud: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/audits/run-1-audit-gpt-5-codex-cloud-2026-05-06.md
- Run-1 audit hermes: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/audits/run-1-audit-hermes-2026-05-06.md
- Run-2 commander template rules: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/run-2-commander-prompt-template-rules-2026-05-06.md

### 5. Codex 当时收到的指令（在 `run2-audit-handoff` 分支）
- Run-2 原始 commander prompt: https://github.com/RayWong1990/ScoutFlow/blob/run2-audit-handoff/docs/research/post-frozen/run-2-codex-commander-prompt-2026-05-06.md
- Run-2 RESUME commander prompt: https://github.com/RayWong1990/ScoutFlow/blob/run2-audit-handoff/docs/research/post-frozen/run-2-resume-codex-commander-prompt-2026-05-06.md

### 6. 13 + 18 PR diff（GitHub PR 页直接读）
Run-2:
- #207 LP-04: https://github.com/RayWong1990/ScoutFlow/pull/207/files
- #216 LP-05: https://github.com/RayWong1990/ScoutFlow/pull/216/files
- #226 LP-06+07 (双覆盖前半): https://github.com/RayWong1990/ScoutFlow/pull/226/files
- #228 LP-06/07/08/11/15 repair (合包): https://github.com/RayWong1990/ScoutFlow/pull/228/files
- #230 LP-12: https://github.com/RayWong1990/ScoutFlow/pull/230/files
- #231 Run-1 amendment + 3 audits (scope-creep): https://github.com/RayWong1990/ScoutFlow/pull/231/files
- #232 LP-10 coverage evidence: https://github.com/RayWong1990/ScoutFlow/pull/232/files
- #233 LP-09 coverage evidence: https://github.com/RayWong1990/ScoutFlow/pull/233/files
- #234 LP-14 coverage evidence: https://github.com/RayWong1990/ScoutFlow/pull/234/files
- #235 LP-16 synthetic UAT-1 evidence: https://github.com/RayWong1990/ScoutFlow/pull/235/files
- #236 LP-17 readback: https://github.com/RayWong1990/ScoutFlow/pull/236/files
- #237 LP-18 closeout: https://github.com/RayWong1990/ScoutFlow/pull/237/files
- #238 Run-2 closeout receipt bundle: https://github.com/RayWong1990/ScoutFlow/pull/238/files

Window-2 (PF-C3 + PF-GLOBAL): #208-#225 全 docs，#227 receipt bundle。建议抽样审 (#208 / #214 / #221 / #225 / #227) + W2 报告 cross-check。

### 7. live truth check（关键代码 final-state）
- main.py: https://github.com/RayWong1990/ScoutFlow/blob/8cf3349/services/api/scoutflow_api/main.py
- bridge/config.py (write_enabled invariant): https://github.com/RayWong1990/ScoutFlow/blob/8cf3349/services/api/scoutflow_api/bridge/config.py
- bridge/router.py: https://github.com/RayWong1990/ScoutFlow/blob/8cf3349/services/api/scoutflow_api/bridge/router.py
- bridge/schemas.py: https://github.com/RayWong1990/ScoutFlow/blob/8cf3349/services/api/scoutflow_api/bridge/schemas.py
- VaultPreviewPanel: https://github.com/RayWong1990/ScoutFlow/blob/8cf3349/apps/capture-station/src/features/vault-preview/VaultPreviewPanel.tsx
- VaultPreviewPanel.test: https://github.com/RayWong1990/ScoutFlow/blob/8cf3349/apps/capture-station/src/features/vault-preview/VaultPreviewPanel.test.tsx
- UrlBar: https://github.com/RayWong1990/ScoutFlow/blob/8cf3349/apps/capture-station/src/features/url-bar/UrlBar.tsx

### 8. baseline → final compare
- https://github.com/RayWong1990/ScoutFlow/compare/9d90d0a...8cf3349

---

## 审计 Charter — 10 检查点（紧扣 6 个 user 关心的待挖问题）

每点产出 verdict (clear / concern / reject) + evidence (URL + 引用片段 / 行号).

### A. Forensic 三 verdict 诚实度（CRITICAL — 最大嫌疑）
LP-09/10/14 全标 `COVERED_BY_228`，无新 PR 实跑代码。读 3 个 coverage evidence 文档：
- 是否每个文档都引 dispatch §1 Goal + §4 allowed_paths + §8 acceptance？
- 是否给出 #228 中 file:line 的精确引用，证明 #228 真的实现了 dispatch §1 要求的功能？
- 断言计数 ≥3 (per W-LP01-Δ rule)？
- 是否存在"#228 没真覆盖但 evidence 文档糊弄说覆盖了"的情况？

任一文档 evidence 链不全 / file:line 模糊 / 断言数 <3 → reject。

### B. Synthetic UAT-1 诚实度（HIGH）
读 evidence 文件:
- frontmatter `status: synthetic_partial` + `browser: not_started` 是诚实标注
- 但最终 `verdict: works` — 是否过激？synthetic 应否降为 `partial` verdict？
- `capture_id=01KQYEXWJYZ9X8FW7TGD1QW0XP` 是 ULID 格式，长度+字符集合规
- `markdown_excerpt_first_3_lines` 是否符合 placeholder shape（write_enabled=False 应返 placeholder 不应有真 B 站内容）？
- copy/download 分类基于 JSDOM 单测 22/22 pass — 是否合理推断？

判定: 如果 frontmatter 标 partial 但 verdict 标 works → concern 或 reject（诚实声明 vs 语义不一致）

### C. PR #231 amendment ledger 完整度（HIGH）
读 amendment ledger + 3 audit reports:
- 8 项 A1-A8 是否覆盖 2/3 REJECT 涉及的所有 finding？(at least PF-LP-02 §4 越界 charter D)
- KEEP 决策的"no true write / no runtime / no authority drift / rollback breaks Run-2" 论据是否在 ledger 里写明？
- audit reports 三份是否 cite 自 `run1-audit-handoff` 分支 URL（即 user 通过 Run-1 audit prompt 跑出来的真审计，不是 Codex 伪造的）？
- amendment 处理是否引入新 silent flexibility（如借此机会偷塞额外修改）？

ledger 缺项 / 论据空泛 / audit reports 不可溯源 → concern 或 reject。

### D. ready_for_run_3=no 真因（HIGH — 必查）
Codex stdout 报 `ready_for_run_3: no`。但 Run-2 报告 follow_up 段没明说原因。挖原因:
- Run-2 报告 / DIFF-BUNDLE / CHECKPOINT 哪里写了 Run-3 blocker？
- LP-18 verdict=`partial` 是否就是 Run-3 blocker？
- amendment ledger A7 "Run-2 stop-line: proof-requires-production-expansion → STOP and amend §4" 是否是 Run-3 前提条件？
- 若找不到明确 blocker 表述 → 标 concern + 列推测

### E. 边界（authority untouched）
扫所有 31 PR /files 页，确认 **没有任何** PR 触及:
- `docs/current.md` / `docs/task-index.md` / `docs/decision-log.md` / `AGENTS.md`

期望: 全 untouched。任一命中 → reject。

### F. 硬红线
扫 31 PR diff 是否含禁词:
- `BBDown` / `yt-dlp` / `ffmpeg` / `audio_transcript`
- `subprocess.run` / `subprocess.Popen`
- browser automation: `playwright` / `puppeteer` / `selenium` / `webdriver`
- DB migration: `alembic` / 新 migration 文件

并验证 final-state `bridge/config.py` 仍 `write_enabled=False` (两个 return 分支都是 False)。

### G. #226 + #228 双覆盖逻辑（MEDIUM）
LP-06/07 在 #226 和 #228 都标 merge_commit。读两个 PR diff:
- #228 是否替代 #226（重写覆盖）？
- 还是 #228 在 #226 基础上扩展（增量）？
- 如果替代：#226 中 land 的 logic 有无被 #228 删除（潜在覆盖率下降）？
- 如果扩展：scope note `pf-lp-06-07-dispatch-scope-note.md` 是否合理解释了双 land？

### H. #231 scope-creep 边界（MEDIUM）
PR #231 在 Run-2 RESUME 窗口里做 Run-1 amendment 工作，不在 resume prompt 范围内。读 #231 diff:
- 9 个文件全在 `docs/research/post-frozen/**`（candidate 区）？
- 没动 production code（services/ apps/ workers/ packages/ data/）？
- 没动 authority files？
- 用户 paste 三份 audit report 给 Codex 是合法授权 → 但 Codex 是否仅做 ledger 化，没扩展自创新规则？

期望: 边界严守 → clear。任一越界 → concern / reject。

### I. Receipt 内一致性
跨文件 cross-check:
- RUN-2 报告 / DIFF-BUNDLE-Run2 / CHECKPOINT-Run2-final.json 三处的 PR list / dispatch list / verdict / interruption_count 是否完全一致？
- Window-2 报告 / DIFF-BUNDLE-W2 / CHECKPOINT-W2-final 三处一致？
- Window-2 自报 PR list (208-225 + 227) 与 Run-2 PR list (207, 216, 226...) 之间无 PR 编号冲突？

任何不一致 → reject。

### J. Window-2 receipt 真实度（LOW — quick check）
Window-2 17 dispatches 已 100% 完成（CHECKPOINT-W2-final 自报）。抽样:
- #208 PF-C3-01 / #214 PF-GLOBAL-06 / #221 PF-GLOBAL-12 / #225 PF-C3-06 — 每个抽样 PR 是否真在 dispatch §4 allowed_paths 内？
- #227 receipt bundle 是否引 17 个 dispatch 的 file path + merge SHA？
- Window-2 自报里 "PR #216 standardly mention as unrelated open PR" — 是否说明并发认知偏差影响 Window-2 receipt 准确度？

期望: 抽样全 clean → clear。

---

## 输出格式

写一份完整 markdown report 贴回对话（user 自行存档为 `AUDIT-Run2-<auditor_id>-2026-05-06.md`）:

### Frontmatter
```yaml
---
title: Run-2 + Window-2 External Audit Report — <auditor_id>
status: candidate / external_audit / not-authority
created_at: 2026-05-06
auditor: <auditor_id>            # 自选: hermes / gpt-pro / codex-cloud / claude-cc 等
audit_target: Run-2 + Window-2 (PR #207..#238 + Window-2 #208..#227)
audit_baseline_sha: 9d90d0a436ee756bfc31dde4616f14b326a540c3
audit_final_sha: 8cf334905ef1dda388737680bf27c552260a9a9b
---
```

### 1. 10 检查点 verdict 表

| # | 检查点 | verdict | evidence (URL + 引用) |
|---|---|---|---|
| A | Forensic 三 verdict 诚实度 | clear / concern / reject | <evidence URL + 3 段引用> |
| B | Synthetic UAT-1 诚实度 | clear / concern / reject | <evidence URL + frontmatter / verdict 字段> |
| C | #231 amendment ledger 完整度 | clear / concern / reject | <ledger URL + audit reports cross-cite> |
| D | ready_for_run_3=no 真因 | clear / concern / reject | <报告/CHECKPOINT URL + line> |
| E | authority untouched | clear / concern / reject | <PR /files 扫描结果> |
| F | 硬红线 | clear / concern / reject | <code URL + grep 命中> |
| G | #226 + #228 双覆盖逻辑 | clear / concern / reject | <两个 PR diff 比对> |
| H | #231 scope-creep 边界 | clear / concern / reject | <PR #231 file 列表> |
| I | Receipt 内一致性 | clear / concern / reject | <3-3 cross-cite> |
| J | Window-2 receipt 真实度 | clear / concern / reject | <抽样 PR + W2 receipt> |

### 2. Per-dispatch verdict 表（Run-2 14 + Window-2 抽样）

| run | dispatch | PR | verdict | scope_deviation_flag | silent_flexibility_count | evidence |
|---|---|---|---|---|---|---|
| Run-2 | LP-04 | #207 | T-PASS / partial / FAIL_X / REJECT_AS_X | yes / no | 0..N | URL |
| Run-2 | LP-05 | #216 | ... | ... | ... | ... |
| Run-2 | LP-06 | #226 + #228 | ... | ... | ... | ... |
| Run-2 | LP-07 | #226 + #228 | ... | ... | ... | ... |
| Run-2 | LP-08 | #228 | ... | ... | ... | ... |
| Run-2 | LP-09 | #233 | COVERED_BY_228 / partial / REJECT | ... | ... | ... |
| Run-2 | LP-10 | #232 | ... | ... | ... | ... |
| Run-2 | LP-11 | #228 | ... | ... | ... | ... |
| Run-2 | LP-12 | #230 | ... | ... | ... | ... |
| Run-2 | LP-14 | #234 | ... | ... | ... | ... |
| Run-2 | LP-15 | #228 | ... | ... | ... | ... |
| Run-2 | LP-16 | #235 | works / partial（需重判） | ... | ... | ... |
| Run-2 | LP-17 | #236 | ... | ... | ... | ... |
| Run-2 | LP-18 | #237 | partial / 升降级建议 | ... | ... | ... |
| Run-2 | Run-1 amendment | #231 | clear / concern (scope-creep) | ... | ... | ... |
| Run-2 | closeout receipt | #238 | T-PASS / partial | ... | ... | ... |
| Window-2 | PF-C3-01 | #208 | (抽样 only) | ... | ... | ... |
| Window-2 | PF-GLOBAL-06 | #214 | (抽样) | ... | ... | ... |
| Window-2 | PF-GLOBAL-12 | #221 | (抽样) | ... | ... | ... |
| Window-2 | PF-C3-06 | #225 | (抽样) | ... | ... | ... |
| Window-2 | receipt bundle | #227 | T-PASS | ... | ... | ... |

### 3. 全局 verdict（选一个）
- `V-PASS` — 10 检查点全 clear
- `V-PASS_WITH_AMENDMENTS` — 大体 clear，少量 concern 可在 Run-3 前修补
- `V-PASS_WITH_HEAVY_EDIT_REQUIRED` — 多处 concern，需要明显修补再 Run-3
- `REJECT` — 任一 reject 或 ≥3 同源 concern → 阻 Run-3

### 4. 编号 findings（5-15 条，按严重度排序）
模板:
```
### Finding N [CRITICAL / HIGH / MEDIUM / LOW]
- 检查点关联: <A-J>
- 现象: <一句话>
- 证据: <URL + 行号 + 引用片段>
- Codex 自报口径: <Codex 怎么说>
- audit 结论: <比 Codex 严格的口径>
- 修复建议: <可执行动作>
```

### 5. Silent flexibility 专栏（user 最关心）
列 Codex **执行了但没在 RUN-2 / W2 报告里明确声明**的所有偏移:
- 偏移 N: <描述>
  - Codex 是否在某处提到？<原文 / 没提到>
  - 是否 user 授权？<是 / 否 / 模糊>
  - 是否影响 Run-3 安全？<是 / 否>

### 6. ready_for_run_3 重新判定（user 关心）
基于你的 audit findings:
- ready_for_run_3: yes / yes_with_amendments / no
- amendments_needed_before_run_3: <列表>
- run_3_blockers: <列表>
- 你与 Codex 自报 `ready_for_run_3=no` 是否一致？为什么？

### 7. 末尾必填字段
```
audit_completed_at: <ISO 8601>
auditor_confidence: high / medium / low
ready_for_run_3: yes / yes_with_amendments / no
amendments_needed_before_run_3: <列表>
followup_audit_after_run_3: required / optional
```

---

## 边界硬规则
- 你只读 + 输出一份 audit report markdown
- 禁: 任何 git / gh / push / merge / commit 命令
- 禁: 修改 ScoutFlow repo 任何文件
- 禁: 引用其它 auditor 的产物（3 窗口独立，防 anchoring bias）
- 禁: 模糊措辞 PASS / DONE / OK — 用 T-PASS / V-PASS / partial / FAIL_X / REJECT_AS_X / clear / concern / reject
- 禁: 把已锁事实（4 项）当作 Codex deviation 重新审

## 你的核心目标
user 最在意的是: **"Codex 哪些没按要求也继续推进了"**（silent flexibility）+ **"ready_for_run_3=no 到底为啥"**。
10 检查点里 A / B / D / G / H 都是这个角度。
你应当严格审计，找出每一处 silent flexibility，包括"虽然合规但未在报告显式声明"的隐性偏移。

不要给 Codex 留情面。也不要 over-reach 把已锁事实当问题。

开始动笔，输出完整 audit report markdown。

<<<AUDIT END>>>
```

---

## 派单顺序（3 窗口同步）

1. 跑完上面的 pre-flight `git push -u origin run2-audit-handoff`，确认 GitHub 上能看到 `run2-audit-handoff` 分支
2. 复制 `<<<AUDIT BEGIN>>>` ... `<<<AUDIT END>>>` 整段
3. 同时粘到 3 个独立云端窗口:
   - 窗口 1: **Hermes**（visual / boundary 守护视角）
   - 窗口 2: **GPT Pro web**（深度思考 / o-series with browsing — cross-PR 一致性视角）
   - 窗口 3: **Codex CLI fresh window**（工程纪律 / state machine / 接口契约视角）
4. 让 3 个 auditor 独立跑，不要互相 paste 中间结论
5. 收齐 3 份 audit report 后做三角对比

---

## 三角验证决策（user 收齐 3 份后）

| 三角结果 | 决策 |
|---|---|
| 3 个 V-PASS | 直启 Run-3 |
| 2 V-PASS + 1 V-PASS_WITH_AMENDMENTS | 看 amendments 是否同源；若是 → 修补再启 Run-3 |
| 任一 V-PASS_WITH_HEAVY_EDIT_REQUIRED | 审 concern 是否阻 Run-3；可能需 revert PR |
| 任一 REJECT | block Run-3 + 复盘 + 走 amendment 路径 |
| 3 auditor 全标 ready_for_run_3=no 且原因同源 | 优先解决该原因再启 Run-3，不强行启动 |
| Codex 自报 `ready_for_run_3=no` + 3 auditor 全 V-PASS | 复核 Codex 为何保守；若纯 process safety → 可启 Run-3 |

---

## 后续

- 3 份 audit report 存档路径建议: `docs/research/post-frozen/runs/AUDIT-Run2-<auditor_id>-2026-05-06.md`
- audit V-PASS 后，可决定是否 PR 入 main
- audit findings 中"修复建议（在 Run-3 前）"应在启动 Run-3 前完成
