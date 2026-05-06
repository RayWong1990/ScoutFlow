---
title: Run-2 Codex CLI Commander Prompt — PF Wave D (frontend) + closeout
status: candidate / commander-prompt / not-authority
created_at: 2026-05-06
target_writer: Codex CLI single window (unattended with one UAT-1 break)
project_root: /Users/wanglei/workspace/ScoutFlow
relates_to:
  - run-1-codex-commander-prompt-2026-05-06.md
  - 80-pack-source/02_task_packs/_PACK-DEFAULTS.md
---

# Run-2 Codex CLI Commander Prompt — PF Wave D (frontend) + closeout

> 14 dispatch / 强依赖前向链 / Phase A unattended（11 dispatch ≈ 35 min）→ user UAT-1（5 min）→ Phase B 续跑（3 dispatch ≈ 10 min）。
> 启动前提：Run-1 三方外审 V-PASS、`origin/main` 已含 LP-01 mount + LP-02 smoke + LP-13 contract。

---

```
<<<COMMANDER PROMPT BEGIN>>>

你是 ScoutFlow Codex0 单写者，执行 Run-2：把 14 个 PF-LP frontend + closeout dispatch 跑完。

## 项目身份
- repo: /Users/wanglei/workspace/ScoutFlow
- live status: WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED
- Run-1 已 V-PASS，origin/main 含 bridge router mount + write_enabled=False schema + golden contract
- 你是 Codex0 唯一 main writer + checkpoint truth owner

## Run-2 范围（14 dispatch / 真依赖图）

```
LP-04 (依赖 LP-01) ─┬─ LP-05 ── LP-06 ── LP-07 (+ LP-02) ── LP-08 ─┬─ LP-09
                    ├─ LP-12 (依赖 LP-01 + LP-04, docs)             ├─ LP-10
                    └─ LP-14 (依赖 LP-04, frontend tests)           └─ LP-11 (+ LP-07)
                                                                    LP-15 (依赖 LP-04~10, frontend tests)
                                                                    └─ LP-16 (依赖 LP-01+05+10, ★ user UAT-1 ★)
                                                                       └─ LP-17 (依赖 LP-16)
                                                                          └─ LP-18 (依赖 LP-17, authority-safe note)
```

按真依赖自决 stage 拆分，stage 表是建议不是硬规则。

## 不停歇协议
- Phase A（LP-04 ~ LP-15 共 11 dispatch）unattended，auto-merge on `mergeStateStatus=CLEAN` + 5 checks 全绿
- Phase B（LP-16 / 17 / 18）需要 user 本地实跑 evidence，跑到 LP-16 时按下面 UAT-1 钩子处理
- per-PR pause 仅当 dispatch frontmatter 含 `external_audit: required` 触发

## ★ UAT-1 钩子（LP-16 处理）★
LP-16 §8 要求 manual run note 含 exact URL / capture_id / markdown excerpt / copy/download result。这必须 user 本地实跑。

你的处理：
1. 跑到 LP-16 时先检查 `docs/research/post-frozen/evidence/PF-LP-16-manual-localhost-run-2026-05-06.md` 是否已存在
2. **存在** → user 已跑 UAT-1，直接 wrap 成 dispatch 输出 + push + merge，继续 LP-17/18
3. **不存在** → 写一份 skeleton 含字段占位 + 在 stdout 输出 "WAITING FOR UAT-1: 请按 docs/research/post-frozen/run-2-codex-commander-prompt-2026-05-06.md UAT-1 步骤跑 + 写 evidence file" + EXIT
4. user 跑完 UAT-1 写 evidence file 后会重 paste 这个 prompt，你检测 evidence 已存在 → 继续 LP-16/17/18

## Subagent 自由调度
你按任务特点自决：
- frontend wiring 链强依赖串行，但 LP-12 docs / LP-14 frontend tests 可与 LP-04~11 并行（不同 worktree）
- 读面并行、live truth check 并行、cross-PR diff audit subagent 并行 — 你说了算
- 写面只 Codex0，subagent 只读 + 提 findings，不写 authority
- 开足马力

## Cold-start 必跑
1. `git fetch origin --prune` + `git rev-parse origin/main`
2. 确认 origin/main 包含 LP-01 / LP-02 / LP-13 commit（grep "PF-LP-01" git log）
3. `cat docs/research/post-frozen/runs/RUN-1-CODEX0-REPORT-2026-05-06.md`（确认 Run-1 V-PASS）
4. `cat services/api/scoutflow_api/main.py` 验证 bridge_router 已 mount（include_router 行）
5. `cat services/api/scoutflow_api/bridge/schemas.py` 验证 write_enabled: Literal[False] 已加

如果 live truth 与 Run-1 假设冲突 → 写 `RUN-Run2-truth-conflict-2026-05-06.md` → 停下来等我

## 三类中断分级（沿用 Run-1）
- slot-local retry → 自己修
- control-plane interruption → 自己接得住
- post-merge ledger interruption → GitHub live truth 补 ledger

只有 control-plane / ledger 接不住才停下来报 user。

## 强视觉钩子（仅提示，不强制）
LP-08~11 涉及 UI 组件（VaultPreviewPanel render / copy / download / error UX），你判断需要时可让 subagent 在 commit 前跑：
- `pnpm --dir apps/capture-station typecheck`
- `pnpm --dir apps/capture-station test -- VaultPreviewPanel`

LP-16 user UAT-1 是 *真实视觉验证* 的入口，你不要替代 user 跑（不要启 Playwright / browser automation）。

## 末尾产出（外审用）
完成 14 dispatch 全 merged 后，写：
1. `docs/research/post-frozen/runs/RUN-2-CODEX0-REPORT-2026-05-06.md`（含 14 stage receipt + UAT-1 evidence path + 三类中断各几次）
2. `docs/research/post-frozen/runs/DIFF-BUNDLE-Run2-2026-05-06.md`（14 PR 跨 PR 一致性 diff，给 GPT Pro / Hermes / Claude 三方并行外审）
3. `docs/research/post-frozen/runs/CHECKPOINT-Run2-final.json`（含 run_complete=true + final origin/main SHA + UAT-1 verdict 引用）

stdout 末尾输出：
```
COMMANDER RUN-2 COMPLETE
final_origin_main: <sha>
prs_merged: [14 PR numbers]
uat_1_evidence_path: <path>
uat_1_verdict: works | partial | broken
high_blast_audit_verdict: [LP-08: clean | LP-15: clean]  # 你自决哪几个 high-blast
interruption_count: {slot_local: N, control_plane: N, ledger: N}
diff_bundle_path: <path>
report_path: <path>
ready_for_external_audit: yes
ready_for_run_3: yes | no
```

## 边界硬规则（沿用）
- Dispatch126-176 frozen，不 reopen / reorder / re-execute
- 不写 docs/current.md / AGENTS.md / docs/task-index.md / docs/decision-log.md
- 不解禁 true vault write / BBDown live / yt-dlp / ffmpeg / ASR / browser automation / migrations
- bridge/config.py:24,36 keep write_enabled=False
- 措辞用 T-PASS / V-PASS / partial / FAIL_ENV / REJECT_AS_X，禁裸 PASS / DONE
- LP-18 closeout authority-safe note 即使涉及 docs/current.md 引用也 *只读*，不写

## 派单顺序提示（最高马力）
- LP-12 / LP-14 docs/test 与 LP-04~11 frontend wiring 三路并行
- LP-04 → LP-05 必串行（LP-05 调 LP-04 的 createCapture）
- LP-08 → LP-09 / LP-10 可并行（同 panel 上不同 action）
- LP-15 frontend component tests 等 LP-04~10 都 land 后跑
- LP-16/17/18 是 Phase B（UAT-1 后）

开始动笔。

<<<COMMANDER PROMPT END>>>
```

---

## UAT-1 user 实跑步骤（5 min）

**前提**: Codex 跑到 LP-16 EXIT 后，stdout 提示 "WAITING FOR UAT-1"。

**步骤**:

```bash
# 1. 启 backend
cd /Users/wanglei/workspace/ScoutFlow
uvicorn scoutflow_api.main:create_app --factory --reload --port 8000 &

# 2. 启 H5 dev server
cd apps/capture-station
pnpm dev &  # 默认 :5173

# 3. 浏览器打开 http://localhost:5173
# 4. 在 URL Bar 粘一个 Bilibili URL（比如 https://www.bilibili.com/video/BV1xx411c7mu）
# 5. 点 Create capture 按钮
# 6. 等 markdown preview 出来
# 7. 点 Copy → 粘到任意 text editor 验证
# 8. 点 Download → 看 .md 文件下载到 ~/Downloads
```

**写 evidence file**:

```bash
cat > /Users/wanglei/workspace/ScoutFlow/docs/research/post-frozen/evidence/PF-LP-16-manual-localhost-run-2026-05-06.md <<'EOF'
---
title: PF-LP-16 Manual Localhost Run Evidence
status: user_uat_1_evidence
date: 2026-05-06
verdict: works | partial | broken
---

# UAT-1 Manual Run Evidence

## Setup
- backend: uvicorn :8000
- h5: pnpm dev :5173
- browser: <Chrome / Safari / etc>

## Run trace
- input_url: https://www.bilibili.com/video/BV1xx411c7mu
- capture_id: <从 H5 看到的>
- markdown_excerpt_lines: <数一下 markdown 行数>
- markdown_excerpt_first_3_lines: |
    <line 1>
    <line 2>
    <line 3>
- copy_action: success | failed
- download_action: success | failed
- downloaded_filename: scoutflow-preview-<capture_id>.md

## verdict: <works | partial | broken>
## blockers (如有): <一句话>
EOF
```

**写完 evidence file 后**：
- 重 paste 这个 commander prompt 给同一 Codex 窗口（或新开 fresh 窗口）
- Codex 检测 evidence 文件存在 → 自动续跑 LP-16/17/18

---

## 派单顺序

```bash
# Run-1 V-PASS 后
cat /Users/wanglei/workspace/ScoutFlow/docs/research/post-frozen/run-2-codex-commander-prompt-2026-05-06.md
# 复制 <<<BEGIN>>>...<<<END>>> 之间内容粘到 fresh Codex CLI 窗口
```
