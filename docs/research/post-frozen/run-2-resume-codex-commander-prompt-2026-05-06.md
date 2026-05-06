---
title: Run-2 RESUME Codex CLI Commander Prompt — Mid-Run Recovery
status: candidate / commander-prompt / not-authority
created_at: 2026-05-06
target_writer: fresh Codex CLI window (主窗口被意外关闭后续跑)
project_root: /Users/wanglei/workspace/ScoutFlow
relates_to:
  - run-2-codex-commander-prompt-2026-05-06.md (原 prompt，0 进度假设)
  - 已 merged: PR #207 / #216 / #226 / #228 / #229(closed→#230) / #230
  - 缺 LP-09 / LP-10 / LP-14 / Phase B (LP-16/17/18) + Run-2 收尾 receipt
---

# Run-2 RESUME Commander Prompt — 半途接管

> 用户两次意外关掉 Run-2 + Window-2 窗口。Window-2 已自然完结（17/17 + receipt 齐），Run-2 停在 #230 后无收尾。
> 把下面 `<<<RESUME BEGIN>>>` ... `<<<RESUME END>>>` 段粘到 fresh Codex CLI 窗口。
> Codex 必须先 forensic 验真态，再续跑，禁止盲目重跑已 merge 内容。

---

## Mid-Run 已锁事实（fresh Codex 必读）

- **origin/main HEAD**: `f7d6c5c383fe36ed18c6ad981692cec363de3b72` (PR #230 merged)
- **Run-2 已 merge PR**: #207 / #216 / #226 / #228 / #230（共 5 PR，#229 closed 被 #230 替代）
- **Window-2 已 100% 完结**（不是 Run-2 的范围，但与 Run-2 并行跑过，origin/main 含 Window-2 所有产物）

### Run-2 已 merge dispatch 映射

| dispatch | 状态 | PR | 关键文件 |
|---|---|---|---|
| LP-04 | ✅ MERGED | #207 | apps/capture-station/src/lib/api-client.ts (createCapture) |
| LP-05 | ✅ MERGED | #216 | apps/capture-station/src/features/url-bar/UrlBar.tsx |
| LP-06 | ✅ MERGED | #226 + #228 | apps/capture-station/src/layout/FourPanelShell.tsx |
| LP-07 | ✅ MERGED | #226 + #228 | (同 LP-06，preview shell bridge) |
| LP-08 | ✅ MERGED | #228 | apps/capture-station/src/features/vault-preview/VaultPreviewPanel.tsx |
| LP-11 | ✅ MERGED | #228 | (同 LP-08，combined repair) |
| LP-12 | ✅ MERGED | #230 | docs/research/post-frozen/... (localhost dev runbook) |
| LP-15 | ✅ MERGED | #228 | tests/e2e/test_h5_bridge_preview_placeholder.py |

### Run-2 缺口（fresh Codex 待办）

| dispatch | 状态 | 操作 |
|---|---|---|
| **LP-09** | ❓ unverified | forensic 核 #228 是否覆盖；未覆盖则开新 PR |
| **LP-10** | ❓ unverified | 同上 |
| **LP-14** | ❓ unverified | 同上 (frontend tests pack) |
| **LP-16** | ❌ blocked on UAT-1 | 触发 UAT-1 钩子，user 本地跑后续 |
| **LP-17** | ❌ 依赖 LP-16 | LP-16 后接 |
| **LP-18** | ❌ 依赖 LP-17 | LP-17 后接 |
| RUN-2 receipt | ❌ 缺 | 全 6 dispatch 完后写 RUN-2 报告 / DIFF-BUNDLE / CHECKPOINT |

### Run-2 已知 silent flexibility（fresh Codex 不要重蹈）

- 原 Run-2 commander 期望 per-dispatch PR；上一轮 Codex 把 LP-06/07/08/11/15 5 个 dispatch 合包到 #228 一个 "repair PR"，并写 `pf-lp-06-07-dispatch-scope-note.md` + `pf-lp-08-11-15-dispatch-scope-note.md` 自正名
- 上一轮 Codex 没产出 RUN-2 receipt，停在 #230 就关窗口
- LP-09/10/14 是否被静默吞进 #228 不可知，需要 forensic 核

---

```
<<<RESUME BEGIN>>>

你是 ScoutFlow Codex0 fresh 单写者，半途接管 Run-2。上一轮 Codex 跑完 LP-04/05/06/07/08/11/12/15（其中 5 个合并到 #228 "repair PR"），停在 #230 后窗口被意外关闭，无收尾 receipt。你的任务是 forensic 验真态 → 补缺 → 触发 UAT-1 → 跑 Phase B → 写收尾。

## 项目身份
- repo: /Users/wanglei/workspace/ScoutFlow
- live status: WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED
- origin/main HEAD（启动时应是）: f7d6c5c383fe36ed18c6ad981692cec363de3b72
- Window-2 已 100% 完结（17 docs + receipt 全 merged，含 PF-C3-01/02/03/05/06 + PF-GLOBAL-01..12）
- Run-2 已 merge 5 PR (#207/216/226/228/230) 覆盖 8 dispatch (LP-04/05/06/07/08/11/12/15)
- 你是 Codex0 唯一 main writer + checkpoint truth owner

## 你的待办（3 阶段，严格顺序）

### Stage R1 — Forensic 验 LP-09 / LP-10 / LP-14（必须先做，禁止跳）

读 dispatch 源文件 §1 Goal + §4 allowed_paths + §8 acceptance：
- `docs/research/post-frozen/80-pack-source/02_task_packs/PF-localhost-preview-pack/dispatches/PF-LP-09-*.md`
- `docs/research/post-frozen/80-pack-source/02_task_packs/PF-localhost-preview-pack/dispatches/PF-LP-10-*.md`
- `docs/research/post-frozen/80-pack-source/02_task_packs/PF-localhost-preview-pack/dispatches/PF-LP-14-*.md`

对每个 dispatch 跑：
1. `gh pr view 228 --json files -q '.files[].path'` 拉 #228 实际文件列表
2. 对照 dispatch §4 allowed_paths：#228 是否触及该 dispatch 期望写的文件？
3. 对照 dispatch §1 Goal：#228 中触及的代码是否实现 Goal 要求的功能？
4. 对照 dispatch §8 acceptance assertions：#228 的测试是否包含 §8 要求的断言（≥3 个，per W-LP01-Δ rule）？

每 dispatch 出 verdict：
- `COVERED_BY_228` → 写 evidence 文档 `docs/research/post-frozen/runs/RUN-2-LP-XX-coverage-evidence-2026-05-06.md`，含 file:line 引用 + assertion list + commit SHA。push + 单 PR merge（标题 `docs(post-frozen): record PF-LP-XX coverage evidence under #228`）
- `NOT_COVERED` → 在新 worktree (`codex/run2-pf-lp-XX`) 开新 dispatch PR，按原 dispatch §3/§4/§8 跑，per-dispatch one PR
- `AMBIGUOUS` (覆盖部分但不全) → 写 truth-conflict 文档 `RUN-Run2-truth-conflict-2026-05-06.md` + EXIT 等 user

**禁止**：写 "scope note" 自正名合包，禁止把 NOT_COVERED 当 COVERED 糊弄。

### Stage R2 — UAT-1 钩子（LP-16）

LP-16 §8 要求 manual run note 含 exact URL / capture_id / markdown excerpt / copy/download result。这必须 user 本地实跑。

你的处理：
1. 跑到 LP-16 前先检查 `docs/research/post-frozen/evidence/PF-LP-16-manual-localhost-run-2026-05-06.md` 是否已存在
2. **存在** → user 已跑 UAT-1，直接 wrap 成 dispatch 输出 + push + merge LP-16，继续 LP-17/18
3. **不存在** → 写一份 skeleton 含字段占位 + 在 stdout 输出 `WAITING FOR UAT-1: 请按 docs/research/post-frozen/run-2-codex-commander-prompt-2026-05-06.md UAT-1 步骤跑 + 写 evidence file` + EXIT
4. user 跑完 UAT-1 写 evidence file 后会重 paste 这个 RESUME prompt，你检测 evidence 已存在 → 续跑 LP-16/17/18

### Stage R3 — Phase B 续跑 + Run-2 收尾

UAT-1 evidence 就位后：
1. LP-16 dispatch PR + merge
2. LP-17 dispatch PR + merge（依赖 LP-16）
3. LP-18 dispatch PR + merge（依赖 LP-17，authority-safe note，read-only 引用 docs/current.md 但不写）

全 14 dispatch 完成后写收尾：
1. `docs/research/post-frozen/runs/RUN-2-CODEX0-REPORT-2026-05-06.md` — 含全 14 dispatch stage receipt + R1 forensic verdict + UAT-1 evidence path + 三类中断各几次
2. `docs/research/post-frozen/runs/DIFF-BUNDLE-Run2-2026-05-06.md` — 跨 PR 一致性 diff，给三方外审用
3. `docs/research/post-frozen/runs/CHECKPOINT-Run2-final.json` — 含 run_complete=true / final origin/main SHA / 14 dispatch + 5 既存 PR + 新 PR 列表 / UAT-1 verdict 引用

## Cold-start 必跑（启动后 fresh Codex 第一件事）

1. `git fetch origin --prune` + `git rev-parse origin/main`
2. 验证 HEAD 是 `f7d6c5c` 或更新（user 在你启动后可能又有动作）；如果不是 → 警告并 EXIT
3. 验证 5 个 PR 都已 merged：
   ```
   for n in 207 216 226 228 230; do
     gh pr view $n --json state,mergeCommit -q '.state + " — " + .mergeCommit.oid'
   done
   ```
4. `cat docs/research/post-frozen/runs/CHECKPOINT-W2-final.json`（确认 Window-2 完结，不与你冲突）
5. `cat docs/research/post-frozen/run-2-codex-commander-prompt-2026-05-06.md`（理解原 Run-2 全图）

如果 live truth 与本 RESUME prompt 假设冲突（如 #228 已被 revert / 某 PR 实际 CLOSED 而不是 MERGED）→ 写 `RUN-Run2-truth-conflict-2026-05-06.md` → 停下来等 user。

## 不停歇协议
- R1 forensic 三 dispatch 可并行跑（read-only subagent）
- R1 完成后 unattended：每 stage 自动 push PR + auto-merge on `mergeStateStatus=CLEAN` + 5 checks 全绿
- R2 UAT-1 EXIT 是唯一硬中断点，等 user 跑 evidence
- R3 unattended 跑到 14 dispatch 全完结
- per-PR pause 仅当 dispatch frontmatter 含 `external_audit: required` 时（LP-09/10/14/16/17/18 均无此字段）

## Subagent 自由调度
- R1 forensic verdict 读面并行（3 dispatch 同时核）
- 写面只 Codex0 主写，subagent 只读 + 提 findings，不写 authority、不改 repo
- R3 LP-16/17/18 严依赖串行
- 不要拘束，开足马力，但不要重蹈合包覆辙

## 三类中断分级（沿用 Run-1）
- slot-local retry：单个 stage 内部失败修一下 → 自己修
- control-plane interruption：gh pr create / view / merge 命令本身炸 → 自己接得住
- post-merge ledger interruption：merge 真成了但 ledger 没写完 → 用 GitHub live truth 补 ledger

只有 control-plane / ledger 接不住才停下来报 user。

## 边界硬规则（违反任一即停）
- Dispatch126-176 frozen，不 reopen / reorder / re-execute
- 不写 docs/current.md / AGENTS.md / docs/task-index.md / docs/decision-log.md
- 不解禁 true vault write / BBDown live / yt-dlp / ffmpeg / ASR / browser automation / migrations
- bridge/config.py:24,36 keep write_enabled=False
- 措辞用 T-PASS / V-PASS / partial / FAIL_ENV / REJECT_AS_X / COVERED_BY_228 / NOT_COVERED / AMBIGUOUS，禁裸 PASS / DONE
- **禁止**：写"scope note"为合包 PR 正名（这是上一轮 Codex 的 silent flexibility 模式）
- **禁止**：把 NOT_COVERED 静默升级为 COVERED 糊弄；ambiguous 必 EXIT 等 user
- **禁止**：对已 merged PR 做 force-push / revert（如发现真问题，先写 truth-conflict 文档）
- LP-18 closeout authority-safe note 即使涉及 docs/current.md 引用也 *只读*，不写

## stdout 末尾必输出
```
COMMANDER RUN-2 RESUME COMPLETE
final_origin_main: <sha>
prs_merged_in_resume: [<只列本次 resume 新加的 PR 号>]
prs_merged_total_run2: [<5 既存 + 新加 PR>]
forensic_verdicts: {LP-09: COVERED_BY_228|NOT_COVERED|AMBIGUOUS, LP-10: ..., LP-14: ...}
uat_1_evidence_path: <path>
uat_1_verdict: works | partial | broken
high_blast_audit_verdict: [<你自决哪几个 high-blast，至少 LP-08 + LP-15>]
interruption_count: {slot_local: N, control_plane: N, ledger: N}
diff_bundle_path: <path>
report_path: <path>
ready_for_external_audit: yes
ready_for_run_3: yes | no
```

## 派单顺序提示（最高马力）
- R1 三 dispatch forensic 并行（3 subagent 各核一个）
- R1 NOT_COVERED 命中 → 立即开对应 worktree 跑新 PR，不等其它
- R2 UAT-1 EXIT 等 user
- R3 LP-16/17/18 串行
- 收尾 receipt 三件 R3 末尾一起写

开始动笔。

<<<RESUME END>>>
```

---

## 使用说明

```bash
# 1. 在 fresh Codex CLI 窗口（cd 到 ScoutFlow 项目根）
cat /Users/wanglei/workspace/ScoutFlow/docs/research/post-frozen/run-2-resume-codex-commander-prompt-2026-05-06.md

# 2. 复制 <<<RESUME BEGIN>>>...<<<RESUME END>>> 之间内容粘进去

# 3. Codex 会先 cold-start verify → R1 forensic → 卡在 R2 UAT-1（EXIT）→ user 跑 UAT-1 evidence file → 重 paste prompt → R3 续跑收尾
```

## UAT-1 user 实跑步骤（同原 run-2 prompt §UAT-1）

```bash
# 1. 启 backend
cd /Users/wanglei/workspace/ScoutFlow
uvicorn scoutflow_api.main:create_app --factory --reload --port 8000 &

# 2. 启 H5 dev server
cd apps/capture-station
pnpm dev &  # 默认 :5173

# 3. 浏览器打开 http://localhost:5173
# 4. 在 URL Bar 粘一个 Bilibili URL（如 https://www.bilibili.com/video/BV1xx411c7mu）
# 5. 点 Create capture → 等 markdown preview → 点 Copy → 验证粘贴 → 点 Download → 验证 ~/Downloads
```

写 evidence file 到 `docs/research/post-frozen/evidence/PF-LP-16-manual-localhost-run-2026-05-06.md`，含 input_url / capture_id / markdown_excerpt_lines / copy_action / download_action / verdict 字段（详见原 run-2 prompt 模板）。

## Resume 完成后

- 跑完 14 dispatch + 收尾 → 像 Run-1 那样写一份 Run-2 audit prompt 给 3 窗口外审
- 重点核 R1 forensic verdict 是否如实（特别警惕 Codex 又把 NOT_COVERED 当 COVERED）
- 重点核 #228 既往合包 PR 是否被 forensic verdict 正式追认或被新 dispatch PR 覆盖
- audit V-PASS 后再启 Run-3
