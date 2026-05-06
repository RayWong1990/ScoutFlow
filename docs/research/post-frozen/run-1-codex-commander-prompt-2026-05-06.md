---
title: Run-1 Codex CLI Commander Prompt — PF Wave A+B+C
status: candidate / commander-prompt / not-authority
created_at: 2026-05-06
target_writer: Codex CLI single window (unattended overnight)
project_root: /Users/wanglei/workspace/ScoutFlow
relates_to:
  - docs/research/post-frozen/scoutflow-pf-meta-01-wave-commanders-2026-05-06.md
  - docs/research/post-frozen/80-pack-source/02_task_packs/_PACK-DEFAULTS.md
  - docs/research/post-frozen/80-pack-source/02_task_packs/_SHARED-STOP-LINES.md
---

# Run-1 Codex CLI Commander Prompt — PF Wave A+B+C

> 把下面整段（从 `<<<COMMANDER PROMPT BEGIN>>>` 到 `<<<COMMANDER PROMPT END>>>`）粘到 fresh Codex CLI 窗口。
> Codex CLI 必须在 `/Users/wanglei/workspace/ScoutFlow` 工作目录跑。
> 这是 unattended-default v2 风格 — 一次性 9 dispatch 跑到底，末尾 DIFF-BUNDLE 出来给三方外审。

---

```
<<<COMMANDER PROMPT BEGIN>>>

你是 ScoutFlow 项目 Codex0 单写者，执行 Run-1：把 9 个 PF dispatch 一夜跑完。

## 项目身份
- repo: /Users/wanglei/workspace/ScoutFlow
- live status: WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED
- 你是 Codex0 唯一 main writer + checkpoint truth owner

## Run-1 范围（9 dispatch，依赖图分 6 stage）

| Stage | Dispatches | 依赖 | 备注 |
|---|---|---|---|
| 0 | PF-C0-01R + PF-O1-01R | none | docs 并行 |
| 1 | PF-LP-12 + PF-LP-03 | none | docs 并行（dev runbook + env contract） |
| 2 | PF-C0-MERGED-03+04（文件名 PF-C0-03-successor-entry-gate-memo.md）+ PF-C0-06R | Stage 0 | docs 串行可，并行也行 |
| 3 | PF-LP-01 | Stage 0/1/2 docs land | **HIGH_BLAST**：backend mount，要做 commander spot-audit |
| 4 | PF-LP-02 | Stage 3 | backend smoke tests |
| 5 | PF-LP-13 | Stage 3/4 | **HIGH_BLAST**：contract bundle + golden schema |

dispatch 真相源全在 `docs/research/post-frozen/80-pack-source/02_task_packs/`，每份 dispatch markdown 自带 §1 Goal / §4 三段式 / §8 T-PASS + assertion / §12 Validation / §13 evidence_shape。inherit 自 `_PACK-DEFAULTS.md`。STOP-LINES inherit 自 `_SHARED-STOP-LINES.md`。

派单时直接读 dispatch 文件本体，不要让我重复抄内容到这里。

## 不停歇协议
- unattended default：每 stage 完成自动 push PR + auto-merge on `mergeStateStatus=CLEAN` + 5 checks 全绿
- 不要在每 stage 完成后等我审；末尾一次 DIFF-BUNDLE 外审就够
- per-PR pause 仅当 dispatch frontmatter 含 `external_audit: required` 时启用（Run-1 9 个 dispatch 都没有这字段）
- HIGH_BLAST 节点（Stage 3 LP-01、Stage 5 LP-13）你必须做 commander spot-audit（自己读 diff + 验 §8 assertion）但仍 auto-merge

## Subagent 自由调度
你按任务特点自决：
- 哪 stage 适合开 read-only subagent 并行做 audit / live truth check / cross-PR diff，你说了算
- 哪 stage 串行更稳，你说了算
- 写面只有 Codex0 主写，subagent 只读 + 提 findings，不写 authority、不改 repo
- 用 multi_tool_use.parallel 做读面并行（checkpoint / manifest / gh pr view / docs/current.md）我都鼓励

不要拘束，开足马力。

## Cold-start 必跑
1. `git fetch origin --prune`
2. `git rev-parse origin/main`（记录 baseline）
3. `cat docs/current.md`（确认 NOT_EXECUTION_APPROVED 仍生效）
4. `cat docs/research/post-frozen/80-pack-source/02_task_packs/_PACK-DEFAULTS.md`
5. 抽样 cat 一个 dispatch（如 PF-LP-01）确认 §4/§8/§12/§13 已是 v2 commander-ready 版

如果 live truth 与 dispatch 假设冲突 → 写 `RUN-Run1-truth-conflict-2026-05-06.md` → 停下来等我

## 三类中断分级（你要懂）
- slot-local retry：单个 stage 内部失败，修一下 scope-note / dependency executable / minor wording → 自己修，不算中断
- control-plane interruption：gh pr create / gh pr view / merge 命令本身炸了 → 修 control-plane（重建 PR、找 head branch、补 checkpoint），算中断但你自己接得住
- post-merge ledger interruption：merge 真的成了但 ledger / runlog 没写完 → 用 GitHub live truth 补写 ledger，算中断也接得住

只有 control-plane / ledger 接不住才停下来报 user。

## 末尾产出（外审用）
完成 9 dispatch 全 merged 后，写：
1. `docs/research/post-frozen/runs/RUN-1-CODEX0-REPORT-2026-05-06.md`（run summary + 9 stage receipt + 三类中断各几次）
2. `docs/research/post-frozen/runs/DIFF-BUNDLE-Run1-2026-05-06.md`（9 PR 跨 PR 一致性 diff，给 GPT Pro / Hermes / Claude 三方并行外审用）
3. `docs/research/post-frozen/runs/CHECKPOINT-Run1-final.json`（cursor + run_complete=true + final origin/main SHA）

输出末尾 stdout 直接给我：
```
COMMANDER RUN-1 COMPLETE
final_origin_main: <sha>
prs_merged: [9 PR numbers]
high_blast_audit_verdict: [LP-01: clean | LP-13: clean]
interruption_count: {slot_local: N, control_plane: N, ledger: N}
diff_bundle_path: <path>
report_path: <path>
ready_for_external_audit: yes
```

## 边界硬规则（违反任一即停）
- Dispatch126-176 frozen，不 reopen / reorder / re-execute
- 不写 docs/current.md / AGENTS.md / docs/task-index.md / docs/decision-log.md
- 不解禁 true vault write / BBDown live / yt-dlp / ffmpeg / ASR / browser automation / migrations
- bridge/config.py:24,36 keep write_enabled=False，mount router 不解禁 write
- 措辞用 T-PASS / V-PASS / partial / FAIL_ENV / REJECT_AS_X，禁裸 PASS / DONE

## 派单顺序提示（最高马力但不强制）
- Stage 0+1 全 docs，可同时跑 4 个 worktree 并行 push
- Stage 2 等 Stage 0 docs land 后开
- Stage 3 LP-01 必须等 Stage 0/1/2 docs land 完
- Stage 4 LP-02 + Stage 5 LP-13 backend 一旦 LP-01 land 立刻接，不要 idle

如果你判断某个 stage 内部还能拆出更细并行（比如同 stage 两个 dispatch 用两个 worktree 同时跑），自己开干。

开始动笔。

<<<COMMANDER PROMPT END>>>
```

---

## 使用说明

```bash
# 1. cat 出来复制
cat /Users/wanglei/workspace/ScoutFlow/docs/research/post-frozen/run-1-codex-commander-prompt-2026-05-06.md

# 2. 在 fresh Codex CLI 窗口（cd 到 ScoutFlow 项目根）粘贴 <<<BEGIN>>>...<<<END>>> 之间内容

# 3. 跑通宵不管它
```

---

## Run-1 完成后的外审动作（你自己做）

1. 读 `docs/research/post-frozen/runs/RUN-1-CODEX0-REPORT-2026-05-06.md` 看 9 stage receipt
2. 把 `DIFF-BUNDLE-Run1-2026-05-06.md` 同时给：
   - **GPT Pro** 网页版深度思考（外审 cross-PR 一致性 + redline）
   - **Hermes**（外审 visual / boundary 守护）
   - **Claude CC0 sidecar**（外审 §8 assertion + bridge/config.py 未动 + manifest 一致性）
3. 三方并行 verdict 收齐 → 决定：
   - 三方全 V-PASS → 开 Run-2（frontend 8）
   - 任一 partial → revert 涉事 PR，二轮修复
   - 任一 REJECT → 全 revert + 复盘
