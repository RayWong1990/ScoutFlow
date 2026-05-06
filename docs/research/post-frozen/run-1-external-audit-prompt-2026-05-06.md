---
title: Run-1 External Audit Prompt — 3-Window Cloud Triangulation
status: candidate / audit-prompt / not-authority
created_at: 2026-05-06
target_writer: 3 independent cloud auditors (paste to 3 windows simultaneously)
project_root: /Users/wanglei/workspace/ScoutFlow
github_repo: https://github.com/RayWong1990/ScoutFlow
audit_baseline_sha: 82481b197eaa420744af90427b07a5ad670d3d96
audit_final_sha: 9d90d0a436ee756bfc31dde4616f14b326a540c3
audit_handoff_branch: run1-audit-handoff
audited_prs: [199, 200, 201, 202, 203, 204, 205, 206]
known_user_authorized_non_run1: [197, 198]
known_user_authorized_descope: [PF-LP-12 deferred to Run-2]
---

# Run-1 严格外审 Commander Prompt — 3 窗口云端三角验证

> 把下面 `<<<AUDIT BEGIN>>>` ... `<<<AUDIT END>>>` 之间整段粘到 3 个独立云端窗口（GPT Pro web / Claude web / Hermes / 任意第三方 LLM with browsing），同时跑。
> 所有输入都是 **GitHub URL**，云端审计员可直接 fetch，无需本地文件。
> 每个审计员独立审、独立写报告，user 三角对比。

---

## 派单前必跑（一次，把 receipts 推到 GitHub 给云端可读）

```bash
cd /Users/wanglei/workspace/ScoutFlow
git fetch origin --prune
git checkout -b run1-audit-handoff origin/main

git add docs/research/post-frozen/run-1-codex-commander-prompt-2026-05-06.md \
        docs/research/post-frozen/run-2-codex-commander-prompt-2026-05-06.md \
        docs/research/post-frozen/window2-docs-commander-prompt-2026-05-06.md \
        docs/research/post-frozen/run-1-external-audit-prompt-2026-05-06.md \
        docs/research/post-frozen/runs/

git commit -m "chore(post-frozen): snapshot Run-1 receipts for external audit"
git push -u origin run1-audit-handoff

# 验证云端可达：
echo "https://github.com/RayWong1990/ScoutFlow/blob/run1-audit-handoff/docs/research/post-frozen/runs/RUN-1-CODEX0-REPORT-2026-05-06.md"
```

> 不开 PR、不 merge — 只推分支让云端 fetch。审计完决定是否 PR。

---

## 已锁事实（审计员开工前 user 已确认，不需要再质疑）

- **baseline → final**: `82481b1` → `9d90d0a` （8 PR Run-1 全 merge）
- **#197 / #198 是 user-authorized 非 Run-1 commit**：在 baseline 与 #199 之间，user 已确认授权，**不计入 Codex scope deviation**
- **PF-LP-12 由 user 显式 defer 到 Run-2**：见 `RUN-Run1-truth-conflict-2026-05-06.md` line 34，"user clarification: stage table is advisory, dispatch §3 dependencies are authoritative"。Codex 当时按 commander rule (§"如果 live truth 与假设冲突 → 写 conflict file → 停下来等我") 正确 EXIT 等了 user，不算 silent flexibility
- **Codex 自报**: high_blast_audit_verdict (LP-01: clean / LP-13: clean) / interruption_count (slot_local=1 / control_plane=3 / ledger=0)

审计员任务是 **核验** Codex 自报，**不是** 重新质疑这 4 条已锁事实。重点放在 **Codex 没声明的隐性偏移**。

---

```
<<<AUDIT BEGIN>>>

你是 ScoutFlow Run-1 独立外审员。3 个独立云端窗口同时跑同一段 prompt，user 后续三角对比 verdict。你不知道其它两个 auditor 是谁、不读对方报告（防 anchoring bias）。

## 角色
- 只读 audit。**禁止** 任何 git commit / push / PR / merge / 修改任何文件 / 跑 CI / 跑 pytest / 跑 pnpm
- 你的产出是一份严格证据链 audit report markdown，user 复制粘贴存档
- 措辞用 T-PASS / V-PASS / partial / FAIL_ENV / REJECT_AS_X / clear / concern / reject —— 禁裸 PASS / DONE / OK
- 你的工作完全在云端：fetch 下面所有 GitHub URL，不要假设本地访问

## 项目身份
- repo: https://github.com/RayWong1990/ScoutFlow
- live status: WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED
- baseline_origin_main: `82481b197eaa420744af90427b07a5ad670d3d96`
- final_origin_main: `9d90d0a436ee756bfc31dde4616f14b326a540c3`
- 8 PR Run-1: #199 / #200 / #201 / #202 / #203 / #204 / #205 / #206
- 已知 user-authorized 非 Run-1 commit: PR #197 / #198（不计入 Codex scope deviation）
- PF-LP-12 由 user 显式 defer 到 Run-2（见 truth-conflict 文件）

## 必读输入（按顺序 fetch）

### 1. Codex 自报 receipts（在 `run1-audit-handoff` 分支）
- RUN-1 完整报告: https://github.com/RayWong1990/ScoutFlow/blob/run1-audit-handoff/docs/research/post-frozen/runs/RUN-1-CODEX0-REPORT-2026-05-06.md
- DIFF-BUNDLE 跨 PR 摘要: https://github.com/RayWong1990/ScoutFlow/blob/run1-audit-handoff/docs/research/post-frozen/runs/DIFF-BUNDLE-Run1-2026-05-06.md
- CHECKPOINT 机器可读: https://github.com/RayWong1990/ScoutFlow/blob/run1-audit-handoff/docs/research/post-frozen/runs/CHECKPOINT-Run1-final.json
- 真因冲突文件 (LP-12 defer): https://github.com/RayWong1990/ScoutFlow/blob/run1-audit-handoff/docs/research/post-frozen/runs/RUN-Run1-truth-conflict-2026-05-06.md

### 2. Codex 当时收到的指令（在 `run1-audit-handoff` 分支）
- Run-1 commander prompt: https://github.com/RayWong1990/ScoutFlow/blob/run1-audit-handoff/docs/research/post-frozen/run-1-codex-commander-prompt-2026-05-06.md

### 3. 8 PR diff（GitHub PR 页直接读）
- PR #199 PF-C0-01R: https://github.com/RayWong1990/ScoutFlow/pull/199/files
- PR #200 PF-O1-01R: https://github.com/RayWong1990/ScoutFlow/pull/200/files
- PR #201 PF-LP-03: https://github.com/RayWong1990/ScoutFlow/pull/201/files
- PR #202 PF-C0-MERGED-03+04: https://github.com/RayWong1990/ScoutFlow/pull/202/files
- PR #203 PF-C0-06R: https://github.com/RayWong1990/ScoutFlow/pull/203/files
- PR #204 PF-LP-01 (HIGH_BLAST): https://github.com/RayWong1990/ScoutFlow/pull/204/files
- PR #205 PF-LP-02: https://github.com/RayWong1990/ScoutFlow/pull/205/files
- PR #206 PF-LP-13 (HIGH_BLAST): https://github.com/RayWong1990/ScoutFlow/pull/206/files

### 4. Dispatch 源文件（验收基线，在 origin/main HEAD 9d90d0a）
- _PACK-DEFAULTS: https://github.com/RayWong1990/ScoutFlow/blob/9d90d0a/docs/research/post-frozen/80-pack-source/02_task_packs/_PACK-DEFAULTS.md
- _SHARED-STOP-LINES: https://github.com/RayWong1990/ScoutFlow/blob/9d90d0a/docs/research/post-frozen/80-pack-source/02_task_packs/_SHARED-STOP-LINES.md
- 8 dispatch 源文件目录: https://github.com/RayWong1990/ScoutFlow/tree/9d90d0a/docs/research/post-frozen/80-pack-source/02_task_packs
  - 在该目录下找 PF-LP-01 / PF-LP-02 / PF-LP-03 / PF-LP-13 / PF-C0-01 / PF-C0-03 / PF-C0-04 / PF-C0-06 / PF-O1-01 的 .md 文件

### 5. live truth check（关键代码当前态）
- main.py (bridge router mount): https://github.com/RayWong1990/ScoutFlow/blob/9d90d0a/services/api/scoutflow_api/main.py
- bridge/config.py (write_enabled=False): https://github.com/RayWong1990/ScoutFlow/blob/9d90d0a/services/api/scoutflow_api/bridge/config.py
- bridge/schemas.py (Literal[False]): https://github.com/RayWong1990/ScoutFlow/blob/9d90d0a/services/api/scoutflow_api/bridge/schemas.py
- golden contract: https://github.com/RayWong1990/ScoutFlow/blob/9d90d0a/tests/contracts/golden/bridge-openapi-2026-05-06.json

### 6. compare baseline vs final 全 commit 列表
- https://github.com/RayWong1990/ScoutFlow/compare/82481b1...9d90d0a

---

## 审计 Charter — 12 检查点

每点产出 verdict (clear / concern / reject) + evidence (URL + file path + line / commit SHA / 引用片段).

### A. 边界（authority untouched）
扫 8 PR /files 页，确认 **没有任何** PR 触及：
- `docs/current.md`
- `docs/task-index.md`
- `docs/decision-log.md`
- `AGENTS.md`

期望: 全 untouched。任一命中 → reject。

### B. 硬红线（preview-only / write_enabled / frozen lanes / forbidden vendors）
扫 8 PR diff 是否含禁词：
- `BBDown` / `yt-dlp` / `ffmpeg` / `audio_transcript`
- `subprocess.run` / `subprocess.Popen`
- browser automation 关键字: `playwright` / `puppeteer` / `selenium`
- DB migration 关键字: `alembic` / `migration` 新表

并验证 final-state:
- `bridge/config.py` 仍 `write_enabled=False`（line 24 + line 36 两处）
- `bridge/schemas.py` `BridgeVaultCommitResponse.write_enabled` 类型是 `Literal[False]`
- Dispatch126-176 范围内文件**只**被 evidence-only 引用，未 reorder / re-execute

### C. PF-LP-12 deferral 合规性
读 truth-conflict 文件全文（应有 ≥40 行结构化内容）。验证：
- conflict_table 是否列出 ≥3 行 conflict？（dispatch §3 deps vs commander stage table）
- resolution 段是否记录 user clarification 原话？（line 34 应有 "stage table is advisory..."）
- stop_verdict 是否标 `resolved_for_run1_continue`？
- Codex 自报 prs_opened=0 / prs_merged=0 是否说明 conflict 在 PR 开始前已 resolve？

期望: 文件结构完整 + user clarification 明文 + Codex EXIT 行为符合 commander §"truth conflict → 停下来等我"。任一缺 → concern。

### D. PF-LP-02 (#205) preview-draft 扩张是否越界（关键 silent flexibility 嫌疑）
Codex 自报: "preview markdown was too short for the dispatch excerpt bar; resolved by expanding preview-only draft shape and syncing the e2e fixture baseline" — 这是 1 次 slot-local interruption 自决修复。

读 PR #205 diff 验证：
- `bridge/vault_preview.py` + `vault/renderer.py` 改动**是否**引入: 真 commit 路径 / 真 write 语义 / 真 vault file path / RAW handoff claim？（grep `commit_id` / `vault_path` / `write_to_disk` / `os.makedirs` / `open(.*'w'`）
- e2e fixture sync (`tests/api/test_bridge_vault_preview_smoke.py`) 是否仅同步 fixture，未污染 production code？
- 读 PF-LP-02 dispatch §4 (allowed_paths) + §8 (acceptance)，"expand preview-only draft shape" 是否在 §4 allowed_paths 内？还是越界自决？

任一引入 write 语义或越 allowed_paths → reject。

### E. PF-LP-13 (#206) conftest.py 改动是否在 §8 scope 内（关键 silent flexibility 嫌疑）
Codex 自报: "tests/conftest.py adds only the minimal --golden option plumbing"。

读 PF-LP-13 dispatch §4 + §8 验证：
- `tests/conftest.py` 是否在 §4 allowed_paths 内？
- `--golden` option plumbing 实现行数 ≤ 30？
- 改动是否 side-effect 污染其它测试（如改了 fixture autouse / monkeypatch session）？
- 读 PR #206 diff: golden 文件 `tests/contracts/golden/bridge-openapi-2026-05-06.json` 是否含 mounted bridge paths + write_enabled=false 断言（per W-LP01-Δ rule，§8 应 ≥3 explicit assertions）？

conftest.py 越 allowed_paths 或 golden subset 不含必要断言 → concern。

### F. PF-LP-01 (#204) "5 bridge contract tests de-duplicated" 覆盖率检查（关键 silent flexibility 嫌疑）
Codex 自报: "old bridge contract tests were de-duplicated to stop double-mount warnings"。

读 PR #204 diff 验证：
- 哪些 test 被标 deduplicated？（应在 PR diff 的 deletion 段可见）
- 删除的 assertion 是否在新 test 里有等价覆盖？
- 还是借 dedup 之名静默删了关键覆盖？

任一关键 assertion 被删且无等价替代 → reject。

### G. 三类 interruption 残留
Codex 自报: slot_local=1 / control_plane=3 / ledger=0，含 "one local git index-lock race caused an accidental local commit on main, then was repaired by moving the commit onto codex/run1-pf-o1-01r and resetting local refs"。

云端验证（用 GitHub compare 视图）：
- https://github.com/RayWong1990/ScoutFlow/compare/82481b1...9d90d0a 列出区间所有 commit
- 期望: 8 个 PR merge commit + #197/#198 user-authorized commit。任何 orphan commit 直接 push 上 main → reject
- 期望: 没有 force-push 痕迹（PR commit 历史线性）
- 期望: 8 个 codex/run1-* worktree 分支 PR 历史与 main 一致（每个 PR 一次 merge）

### H. baseline 完整性
- 验证 `82481b1` 是 Codex Run-1 启动时 origin/main HEAD（CHECKPOINT.json 应记录）
- 验证 #197/#198 工作内容**未**被 Codex 当作 Run-1 evidence 复用：在 RUN-1 报告里 grep "#197" / "#198" / "PR-197" — 应仅作环境前置事实出现，不作 Codex Run-1 stage receipt
- 期望: 边界清晰，#197/#198 仅作环境，Codex 不冒认

### I. Receipt 内一致性
三方 cross-check（必须三处全一致）:
- RUN-1-CODEX0-REPORT 的 PR list / merge_commit / verdict
- DIFF-BUNDLE 的 pr_bundle table
- CHECKPOINT.json 的 prs_merged / dispatches_completed / high_blast_audit_verdict

任何不一致（例: report 说 8 PR、CHECKPOINT 说 9 PR）→ reject。

### J. Frontmatter status 合规
8 PR 写入的所有 .md 文件 frontmatter `status` 字段必须是:
- `candidate / not-authority` 或
- `evidence` 类 / `run_report / not-authority` / `external_audit_packet / not-authority`

任何写出 `authority` / `locked` / `decision` / `final` status → reject。
（这条防 Codex 借 Run-1 把 candidate 文档悄悄升级成 authority。）

### K. Commander prompt 指令落实度
读 run-1-codex-commander-prompt-2026-05-06.md 全文，对每条逐句核：
- §不停歇协议: unattended default + per-PR pause 仅在 `external_audit: required` 时开 — Codex 是否符合？
- §Cold-start 必跑: 5 步是否全做？（git fetch / rev-parse / cat current.md / cat _PACK-DEFAULTS / 抽样 dispatch）
- §三类中断分级: 1 + 3 + 0 = 4 次 self-recovery，是否符合 commander 允许的 self-recovery 路径？
- §末尾产出: 3 个产出 (RUN-1 报告 / DIFF-BUNDLE / CHECKPOINT) 是否全产出？stdout summary 是否含全字段？
- §边界硬规则: 5 条全核（frozen / authority / forbidden lanes / write_enabled / 措辞）

标注: 哪些是 Codex 严格执行 / 哪些是 silent flexibility（ACTed but not declared）。

### L. W-LP01-Δ rule (§8 assertion count ≥ 3)
来源: 2026-05-06 PF-META-01 audit Patch 1 — 每个 §8 acceptance 要求至少 3 个明确 pytest/pnpm assertion。

抽样 #204 / #205 / #206 测试代码（这 3 个 PR 是真正含测试的）：
- PR #204 `tests/api/test_main_app_routers.py` + 5 个 bridge contract tests: 每 §8 acceptance 行映射几个 assertion？
- PR #205 `tests/api/test_bridge_vault_preview_smoke.py`: 同问
- PR #206 `tests/contracts/test_bridge_openapi_golden_contract.py`: 同问

任何 §8 line 0 / 1 / 2 assertion → concern。3 个全 ≥ 3 → clear。

---

## 输出格式

写一份完整 markdown report，结构如下：

### Frontmatter
```yaml
---
title: Run-1 External Audit Report — <auditor_id>
status: candidate / external_audit / not-authority
created_at: 2026-05-06
auditor: <auditor_id>            # 自选: gpt-pro / claude-web / hermes / 其它
audit_target: Run-1 (PR #199 -> #206)
audit_baseline_sha: 82481b197eaa420744af90427b07a5ad670d3d96
audit_final_sha: 9d90d0a436ee756bfc31dde4616f14b326a540c3
audit_handoff_branch: run1-audit-handoff
---
```

### 1. 12 检查点 verdict 表

| # | 检查点 | verdict | evidence (URL + 引用) |
|---|---|---|---|
| A | authority untouched | clear / concern / reject | <PR URL + grep 命中> |
| B | 硬红线 | clear / concern / reject | <code URL + line> |
| C | LP-12 defer 合规 | clear / concern / reject | <truth-conflict URL + line 34 quote> |
| D | LP-02 expansion bounded | clear / concern / reject | <PR #205 + grep> |
| E | LP-13 conftest in scope | clear / concern / reject | <PR #206 + dispatch §4> |
| F | LP-01 dedup 覆盖率 | clear / concern / reject | <PR #204 deletion 段> |
| G | interruption residue | clear / concern / reject | <compare URL + commit list> |
| H | baseline 完整性 | clear / concern / reject | <CHECKPOINT.json + RUN-1 grep> |
| I | receipt 一致性 | clear / concern / reject | <3 文件 cross-cite> |
| J | frontmatter status | clear / concern / reject | <doc URL + frontmatter quote> |
| K | commander 落实度 | clear / concern / reject | <commander prompt 行号 + Codex 行为> |
| L | §8 assertion count ≥ 3 | clear / concern / reject | <test 文件 URL + assertion 计数> |

### 2. Per-dispatch verdict 表

| dispatch | PR | verdict | scope_deviation_flag | silent_flexibility_count | evidence |
|---|---|---|---|---|---|
| PF-C0-01R | #199 | T-PASS / partial / FAIL_X / REJECT_AS_X | yes / no | 0 / 1 / 2... | URL |
| PF-O1-01R | #200 | ... | ... | ... | ... |
| PF-LP-03 | #201 | ... | ... | ... | ... |
| PF-C0-MERGED-03+04 | #202 | ... | ... | ... | ... |
| PF-C0-06R | #203 | ... | ... | ... | ... |
| PF-LP-01 (HIGH_BLAST) | #204 | ... | ... | ... | ... |
| PF-LP-02 | #205 | ... | ... | ... | ... |
| PF-LP-13 (HIGH_BLAST) | #206 | ... | ... | ... | ... |

### 3. 全局 verdict（选一个）
- `V-PASS` — 12 检查点全 clear，Codex 严格执行，无 silent flexibility
- `V-PASS_WITH_AMENDMENTS` — 大体 clear，少量 concern 可在 Run-2 前修补
- `V-PASS_WITH_HEAVY_EDIT_REQUIRED` — 多处 concern，需要明显修补再 Run-2
- `REJECT` — 任一 reject 或 ≥3 个 concern 同源 → 阻 Run-2

### 4. 编号 findings（5-15 条，按严重度排序）

模板:
```
### Finding N [CRITICAL / HIGH / MEDIUM / LOW]
- 检查点关联: <A-L 中一项或多项>
- 现象: <一句话>
- 证据: <URL + 行号 + 引用片段>
- Codex 自报口径: <Codex 在哪个文档里怎么说>
- audit 结论: <比 Codex 严格的口径>
- 修复建议: <可执行动作（在 Run-2 前 / Run-2 中 / Run-2 后）>
```

### 5. Silent flexibility 专栏（user 最关心）

列出 Codex **执行了但没在 RUN-1 报告里明确声明**的所有偏移:
- 偏移 1: <描述>
  - Codex 是否在某处提到？<原文 / 没提到>
  - 是否在 commander prompt 允许的 self-recovery 范畴？<是 / 否 / 模糊>
  - 是否影响 Run-2 安全？<是 / 否>
- 偏移 2: ...

### 6. 末尾必填字段
```
audit_completed_at: <ISO 8601>
auditor_confidence: high / medium / low
ready_for_run_2: yes / yes_with_amendments / no
amendments_needed_before_run_2: <列表，可空>
amendments_needed_during_run_2: <列表，可空>
followup_audit_after_run_2: required / optional
```

---

## 边界硬规则
- 你只读 + 输出一份 audit report markdown 给 user
- 禁: 任何 git / gh / push / merge / commit 命令
- 禁: 修改 ScoutFlow repo 任何文件
- 禁: 引用其它 auditor 的产物（3 窗口独立，防 anchoring bias）
- 禁: 模糊措辞 PASS / DONE / OK / fine —— 用 T-PASS / V-PASS / partial / FAIL_X / REJECT_AS_X / clear / concern / reject
- 禁: 把已锁事实（#197/#198 user-auth、LP-12 user-defer）当作 Codex deviation 重新审

## 你的核心目标
user 最在意的是: **"Codex 哪些没按要求也继续推进了"**（silent flexibility）。
12 检查点里 D / E / F / G / K 都是这个角度。
你应当严格审计、找出并标注每一处 silent flexibility，包括"虽然 self-recovery 但未在 RUN-1 报告显式声明"的隐性偏移。

不要给 Codex 留情面。也不要 over-reach 把已锁事实当问题。

开始动笔，输出完整 audit report markdown。

<<<AUDIT END>>>
```

---

## 派单顺序（3 窗口同步）

1. **跑完上面的 pre-flight `git push -u origin run1-audit-handoff`**，确认 GitHub 上能看到 receipts
2. 复制 `<<<AUDIT BEGIN>>>` ... `<<<AUDIT END>>>` 整段
3. 同时粘到 3 个独立云端窗口，建议:
   - 窗口 1: GPT Pro web（深度思考 / o-series with browsing）
   - 窗口 2: Claude web（Sonnet 4.6 / Opus 4.7）
   - 窗口 3: Hermes / 第三方 LLM with browsing
4. 让 3 个 auditor 独立跑，不要互相 paste 中间结论
5. 收齐 3 份 audit report 后做三角对比

---

## 三角验证决策（user 收齐 3 份后）

| 三角结果 | 决策 |
|---|---|
| 3 个 V-PASS | 直启 Run-2 |
| 2 V-PASS + 1 V-PASS_WITH_AMENDMENTS | 看 amendments 是否同源；若是 → 修补再启 Run-2；若分散 → 直启 |
| 任一 V-PASS_WITH_HEAVY_EDIT_REQUIRED | 审 concern 是否阻 Run-2；可能需 revert PR |
| 任一 REJECT | block Run-2 + 复盘 + revert 涉事 PR |
| Silent flexibility 计数 ≥ 5 跨 auditor | 即使 V-PASS 也要补一次 commander prompt 修订（增强 Codex 自报纪律） |

---

## 后续

- 3 份 audit report 存档路径: `docs/research/post-frozen/runs/AUDIT-Run1-<auditor_id>-2026-05-06.md`
- audit V-PASS 后，可决定是否把 `run1-audit-handoff` 分支 PR 入 main（让 receipts 进项目历史）
- audit findings 中"修复建议（在 Run-2 前）"应在启动 Run-2 前完成
