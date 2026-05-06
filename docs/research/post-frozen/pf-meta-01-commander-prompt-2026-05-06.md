---
title: PF-META-01 — Dispatch Body Rewrite Commander Prompt
status: candidate / research / not-authority
created_at: 2026-05-06
author: Claude (CC0)
target_writer: Codex Desktop single writer (preferred) | GPT Pro web | CC0
relates_to:
  - docs/research/post-frozen/claude-deep-review-2026-05-06.md
  - docs/research/post-frozen/revised-first-4-dispatches-2026-05-06.md
  - docs/research/post-frozen/80-pack-source/
  - docs/research/web-gpt-step0/step0-localhost-preview-dispatch-template-2026-05-06.md
---

# PF-META-01 — Dispatch Body Rewrite Commander Prompt

> 这是一份 *元任务* commander prompt：把 80-pack-source 中 17 个 near-term mainline dispatch 的 body
> 从 ~85% 模板复刻 重写为 commander-ready production grade，使后续可直接派 single-writer。
>
> 元任务本身不写产品代码。它是 dispatch authoring 的 quality lift。

---

## 0. 元任务身份

```yaml
code: PF-META-01
title: Dispatch Body Rewrite for 17 near-term mainline dispatches
pack: meta
cluster: PF-META
dispatch_class: meta_authoring
open_after_state: claude_deep_review_landed
proof_kind: shape_only_with_quality_rubric
human_gate: usefulness_verdict (抽样 3 个 dispatch 由 user shape-level 复核)
priority: blocker (必须先于 PF-LP-01 实施)
can_parallel: no
serial_gate: PF-C0-01R + PF-O1-01R must complete shape readback first
estimated_duration: 2-3 hours (Codex Desktop) | 1-2 hours (GPT Pro)
```

---

## 1. 任务背景（给 writer 的 cold-start 上下文）

### 1.1 项目状态

- 项目: ScoutFlow（GitHub `RayWong1990/ScoutFlow`）
- 当前阶段: Phase 1A / WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED
- live `docs/current.md` 已记录 `Dispatch131-176 / T-P1A-110 ~ T-P1A-155` 为 landed Wave 5 closeout + Wave 6 open/overflow/handoff
- live `AGENTS.md` 已记录 Wave 6 candidate open，已不再 stale
- live `services/api/scoutflow_api/main.py:create_app()` 在 line 59-60 仅 include `captures_router` + `jobs_router`，**未 mount** `bridge.router`
- live `services/api/scoutflow_api/bridge/{config,vault_commit}.py` 已硬挂 `write_enabled=False`（即使 mount router 也不解禁 write）

### 1.2 Frozen historical boundary

`Dispatch126-176` 是 frozen historical assets/evidence。本元任务和被它重写的 17 dispatch 都不得 reopen / reorder / re-execute 它们；只允许引用为 evidence。

### 1.3 80-pack 评判结果

详见 `docs/research/post-frozen/claude-deep-review-2026-05-06.md`。核心问题：

- 80 dispatch ~85% 模板复刻
- §1 Goal 在所有 80 dispatch 字面相同
- §12 Validation 全 80 通用
- 跨 pack STOP-LINES / OPEN-QUESTIONS 字节相同
- 缺 dry-run preview 三段式
- 缺 evidence shape 与 proof_kind 绑定

---

## 2. 元任务范围

### 2.1 必做：重写 17 个 near-term dispatch 的 body

| # | Pack | Dispatch | 优先级 |
|---|---|---|---|
| 1 | PF-C0/O1 | PF-C0-01R（已在 revised-first-4 给出修订） | blocker |
| 2 | PF-C0/O1 | PF-C0-MERGED-03+04（已在 revised-first-4 给出） | high |
| 3 | PF-C0/O1 | PF-C0-06R | high |
| 4 | PF-C0/O1 | PF-O1-01R（含五行 overflow 表） | blocker |
| 5-17 | PF-localhost-preview | PF-LP-01 ~ PF-LP-13（13 个 mainline，含 LP-12 dev run / LP-13 contract test） | blocker / high |

PF-LP-14 ~ PF-LP-18 暂不在本批（user 决策后视情况追加）。

### 2.2 不做：其余 63 dispatch

- PF-C1 / PF-C2 / PF-C3 / PF-C4 全部保留 reservoir 状态
- 重写仅修 dispatch markdown body，不动 manifest.jsonl 字段（schema 已合理）
- 不动 `_QUALITY-NOTE.md` / `00_overview/` / `01_route_decision/` / `03_supporting_files/`

### 2.3 不解禁

- true vault write
- BBDown live / yt-dlp / ffmpeg / ASR / audio_transcript
- browser automation / Playwright execution
- migrations / DBvNext
- full Signal Workbench
- workers/ packages/ data/ referencerepo/

---

## 3. 必须遵守的写作 Rubric（Quality Bar）

### 3.1 §1 Goal 任务原生化（必修）

每个 dispatch §1 Goal 必须是单句任务原生 sentence，包含：
- **动词**: mount / wire / fetch / render / copy / download / verify / record / etc.
- **对象**: 具体的代码文件、API 端点、UI 组件、test target
- **接缝点**: 这一步连接了哪两个已有断点

示例（PF-LP-01）：
> ❌ 旧: "Keeps successor work bounded and prevents old candidate truth from becoming execution truth"
> ✅ 新: "在 `services/api/scoutflow_api/main.py:create_app()` include `bridge.router`，使 `/bridge/health`、`/captures/{id}/vault-preview`、`/captures/{id}/vault-commit` 可达，但保持 `bridge/config.py:24` `write_enabled=False`"

### 3.2 §4 Files preview 三段式（必修）

替换原 §4 Allowed paths（仅 glob）为：

```yaml
files_to_create:
  - <绝对/相对路径>
files_to_modify:
  - <文件>:<行号范围或函数名> (<动作: replace / insert / wire>)
files_will_NOT_touch:
  - <显式列出 forbidden + 容易误改的邻近文件>
```

### 3.3 §12 Validation 任务特化（必修）

按 dispatch 性质分四档：

| dispatch 性质 | §12 必含 |
|---|---|
| backend code-bearing | `pytest tests/api/<specific>` + OpenAPI smoke + `python -c` 导入校验 |
| frontend code-bearing | `pnpm typecheck` + Vitest 组件测试 + manual screenshot or playground note |
| docs / shape_only | `python tools/check-docs-redlines.py <path>` + `check-secrets-redlines.py` + `git diff --check` |
| contract test | pytest contract suite + JSON schema validate against golden |

### 3.4 §13 Evidence shape 与 proof_kind 绑定（必修）

每个 dispatch §13 改为：

```yaml
proof_kind: <enum: shape_only | preview_only | human_verdict | raw_intake | script_seed | screenshot_visual>
evidence_shape:
  <字段名>: <类型 / 路径 / 阈值>
```

每种 proof_kind 的 evidence_shape 词典见 §3.7。

### 3.5 抽出共享 _PACK-DEFAULTS.md（必修）

新建 `docs/research/post-frozen/80-pack-source/02_task_packs/_PACK-DEFAULTS.md`，含：

- §0 Frozen historical boundary
- §5 Forbidden paths / claims（services/api/migrations/、workers/、packages/、data/、referencerepo/、raw credentials、true vault write）
- §6 Blocked claims（no_true_vault_write / no_runtime_approval / no_browser_automation / no_migration / no_ASR / no_BBDown_live）
- §7 Enter condition（generic）
- §9 Partial pass condition（generic）
- §10 Fail condition（generic）
- §11 Kill signal（generic）

每个重写后的 dispatch 顶部 yaml 加 `inherits: ../../_PACK-DEFAULTS.md`，对应 sections 改为 `Inherits _PACK-DEFAULTS.md` 一行。

### 3.6 修复 STOP-LINES / OPEN-QUESTIONS 重复（必修）

新建 `docs/research/post-frozen/80-pack-source/02_task_packs/_SHARED-STOP-LINES.md`，原文 STOP-LINES 移入；7 个 pack 各自的 STOP-LINES.md 改为：

```markdown
inherits: ../_SHARED-STOP-LINES.md

## Pack-specific overrides
（如有 — 例如 PF-C2 多一条 "do not auto-create RAW notes from script"）
```

OPEN-QUESTIONS 必须 cluster-specific 重写（C0/O1 不该问 RAW 问题；C2 不该问 visual 问题）。

### 3.7 evidence_shape 词典（写在 _PACK-DEFAULTS.md）

```yaml
shape_only:
  output_path: <required>
  required_sections: <list>
  required_rows: <int, optional>
  required_columns: <list, optional>

preview_only:
  capture_id: str
  fetch_response_path: str
  markdown_excerpt_lines: int  # >= 20
  copy_action_log: str
  download_filename: str

human_verdict:
  verdict_table_path: str
  useful_count: int
  reject_count: int
  edit_cost_log_path: str
  threshold: "useful_count >= 2 of 3"

raw_intake:
  note_paths: list  # >= 2
  intake_evidence_path: str
  not_second_inbox_check: bool

script_seed:
  seed_path: str
  downstream_consumer_log: str

screenshot_visual:
  screenshot_paths: list  # >= 3
  visual_verdict_path: str
  five_gate_checklist: bool
```

### 3.8 引用 frozen 历史资产时必须给路径（修 W7）

凡涉及 145/146 思想 / Wave 5 candidate 等历史资产的 dispatch（如 PF-C1-03、PF-C1-04），§3 Dependencies 增加 `historical_assets:` 子段，列具体路径：

```yaml
historical_assets:
  - path: docs/research/wave5/hypothesis-evidence-source-matrix-2026-05-05.md
    one_line_summary: <writer 自己读后填>
  - path: docs/research/wave5/topic-card-lite-candidate-XXXX.md
    one_line_summary: <填>
```

### 3.9 Visual hierarchy（修 W11）

每个 dispatch 顶部 yaml 加 `priority: blocker | high | medium | reservoir | permanent_overflow`。
PACK-INDEX.md 用 `🔴/🟠/🟡/🔵/⚪` emoji 区分 priority 列。

### 3.10 Bridge write_enabled 硬挂事实引用（修 W12）

凡涉及 backend mount / bridge 路径的 dispatch（PF-LP-01 / PF-LP-02 / PF-LP-13），§6 必须显式补一行：

```
mount_does_not_unlock_write: bridge/config.py:24,36 keeps write_enabled=False (hardcoded)
```

---

## 4. 输出规范

### 4.1 输出位置

直接 in-place 重写 `docs/research/post-frozen/80-pack-source/02_task_packs/<pack>/dispatches/<dispatch>.md`。
不删除原文件、不改文件名。

### 4.2 输出长度

- 旧每 dispatch 95-99 行
- 新目标 25-40 行（单 dispatch）+ 100-150 行的共享 `_PACK-DEFAULTS.md`
- 信号密度从 ~7% 提升到 50%+

### 4.3 不输出

- 不输出 `docs/current.md` / `AGENTS.md` / `docs/task-index.md` / `docs/decision-log.md` 修改
- 不输出 git commit / git push（user 后续 review 后自己 commit）
- 不输出执行报告（写完 17 dispatch 即停）

### 4.4 输出后必跑

```bash
# 在 ScoutFlow 项目根
python tools/check-docs-redlines.py docs/research/post-frozen/
python tools/check-secrets-redlines.py docs/research/post-frozen/
git diff --check docs/research/post-frozen/

# 验证 _PACK-DEFAULTS.md 引用一致
grep -l "inherits: .*_PACK-DEFAULTS.md" docs/research/post-frozen/80-pack-source/02_task_packs/*/dispatches/*.md | wc -l
# 期望: 至少 17（本批重写的 dispatch）

# 验证 §1 Goal 不再字面相同
grep -h "^## 1. Goal" -A 2 docs/research/post-frozen/80-pack-source/02_task_packs/*/dispatches/*.md | sort -u | wc -l
# 期望: 至少 17 distinct（重写的 17 个），如果原 63 个未改动它们仍同
```

---

## 5. Pass / Partial / Fail 条件

### 5.1 Pass

- 17 个 near-term dispatch 全部按 §3 rubric 重写
- `_PACK-DEFAULTS.md` + `_SHARED-STOP-LINES.md` 落地
- 抽样 3 个 dispatch（user 选择）由 user shape-level 复核 V-PASS
- redlines / secrets / git diff --check 全 0 violation
- §1 Goal distinct count >= 17（重写后无重复）

### 5.2 Partial pass

- 重写完成 13-16 个 dispatch
- 有 1-2 个 dispatch §1 Goal 仍泛化但其他字段合规
- _PACK-DEFAULTS.md 抽出但有 1-2 个 dispatch 没正确 inherit

### 5.3 Fail

- 重写后 dispatch 仍 80% 模板复刻
- §1 Goal 仍出现 "Keeps successor work bounded and prevents old candidate truth from becoming execution truth" > 5 处
- 重写过程中触碰 forbidden paths（services/api/migrations/、workers/、packages/、data/、authority 4-file）
- 输出包含真 token / 真 cookie / 真 PII
- 任何 dispatch 解禁 true write / runtime / browser automation / migration

### 5.4 Kill signal

- writer 重新打开 / 重排 Dispatch126-176
- writer 把 placeholder / dry-run 当 product proof
- writer 在 §12 Validation 写 "no test required" 类无 enforce 措辞

---

## 6. 反例（writer 必须避免的 anti-patterns）

按 ContentFlow L 元认知教训：

### 6.1 ❌ 把 §1 Goal 写成 pack-level meta

```markdown
## 1. Goal

This task is part of the post-frozen successor entry pack.
```
→ 这等于没写。必须有动词 + 对象 + 接缝点。

### 6.2 ❌ §12 Validation 留 placeholder

```markdown
## 12. Validation
Add code-specific tests when the task touches app or service code.
```
→ 必须给具体命令 + 期望 stdout 片段或 exit code。

### 6.3 ❌ §4 仍 glob

```markdown
## 4. Allowed paths
- apps/capture-station/src/**
```
→ 必须三段式 files_to_create / files_to_modify / files_will_NOT_touch。

### 6.4 ❌ 用 PASS / DONE / 完成

→ 用 T-PASS / V-PASS / partial / REJECT_AS_X 分级（按 codex-metacognition-learnings.md §1.1）。

### 6.5 ❌ 偷偷解禁 forbidden lane

→ 任何 dispatch §6 不能改写 / 弱化 / 添加 exception。If 必须 unblock，单立 dispatch + user explicit_runtime_approval。

---

## 7. Writer 必须先做的 truth check

在动笔前 writer 必须 cat 以下 5 个文件验证 live truth：

```bash
# 1. live authority status
sed -n '1,40p' docs/current.md

# 2. live router mount status
sed -n '40,80p' services/api/scoutflow_api/main.py

# 3. live bridge write enforcement
grep -n "write_enabled\|write_disabled" services/api/scoutflow_api/bridge/config.py

# 4. live UrlBar status
sed -n '1,80p' apps/capture-station/src/features/url-bar/UrlBar.tsx

# 5. STEP0 templates (writer 必须遵守这套)
sed -n '1,100p' docs/research/web-gpt-step0/step0-localhost-preview-dispatch-template-2026-05-06.md
```

如果 truth 与 80-pack 假设冲突，writer 必须 STOP 并写 `docs/research/post-frozen/pf-meta-01-truth-conflict-2026-05-06.md` 报告冲突，等 user 裁决后才继续。

---

## 8. Writer 选择

### 8.1 首选: Codex Desktop single writer

- 单写者职责清晰
- Codex 元认知 §1.5 / §1.6 / §8.1 / §8.5 已是 native behavior
- 估算: 2-3 hours

### 8.2 备选: GPT Pro web

- 上下文窗口足够大
- 可直接产出 17 dispatch + 共享 defaults
- 估算: 1-2 hours
- 风险: GPT 长 narrative 偏好可能让 dispatch 过长，需 user 一轮 trim

### 8.3 fallback: CC0（Claude Code）

- 仅当 Codex / GPT 都不可用时启用
- 风险: Opus 容易过度 narrative，需要 user 一轮 trim
- 估算: 3-4 hours

---

## 9. 派单语句（Copy-paste 给 writer）

```text
你是 ScoutFlow 项目的 dispatch authoring writer。

【任务】
按 docs/research/post-frozen/pf-meta-01-commander-prompt-2026-05-06.md §3 rubric，
重写 17 个 near-term mainline dispatch 的 markdown body。

【范围】
- PF-C0/O1: PF-C0-01R / PF-C0-MERGED-03+04 / PF-C0-06R / PF-O1-01R（参照
  docs/research/post-frozen/revised-first-4-dispatches-2026-05-06.md 的修订定义）
- PF-localhost-preview: PF-LP-01 ~ PF-LP-13 全部 13 个 dispatch

【输出位置】
直接 in-place 重写 docs/research/post-frozen/80-pack-source/02_task_packs/<pack>/dispatches/*.md

【共享文件】
- 新建 docs/research/post-frozen/80-pack-source/02_task_packs/_PACK-DEFAULTS.md
- 新建 docs/research/post-frozen/80-pack-source/02_task_packs/_SHARED-STOP-LINES.md
- 7 个 pack 的 STOP-LINES.md / OPEN-QUESTIONS.md 重写为 cluster-specific（参 §3.6）

【边界】
- 不动 docs/current.md / AGENTS.md / docs/task-index.md / docs/decision-log.md
- 不动 services/ apps/ workers/ packages/ data/
- 不解禁 true vault write / runtime tools / browser automation / migrations
- 不 reopen Dispatch126-176（frozen）

【动笔前必跑】
按 §7 cat 5 个 live truth 文件。

【完成定义】
- 17 dispatch 重写完成，§1 Goal distinct >= 17
- _PACK-DEFAULTS.md + _SHARED-STOP-LINES.md 落地
- redlines / secrets / git diff --check 全 0 violation
- 抽样 3 个 dispatch 等 user shape-level review

【receipt 格式】
完成后输出：
verdict: T-PASS_WITH_DEFERRED_USER_REVIEW | partial | FAIL_ENV
files_rewritten: [list]
files_created: [list of shared defaults]
truth_conflict_report: <path or "none">
sample_dispatches_for_user_review: [3 paths]
```

---

## 10. 元任务后置（PF-META-01 完成后做什么）

1. user shape-level review 抽样的 3 个 dispatch（修订 §1 / §4 / §12 / §13 是否到位）
2. 若 V-PASS：
   - PF-LP-01 / PF-LP-04 / PF-LP-05 / PF-LP-13 等 backend 路线进入派单
   - 同时 PF-LP-04 / PF-LP-05 / PF-LP-08 等 frontend 路线进入派单
3. 若 partial：
   - PF-META-01 二轮（针对未达标的 1-3 个 dispatch）
4. 若 FAIL：
   - 退回原 80-pack-source，由 user 亲自 author 关键 dispatch（PF-LP-01 一个 reference）

---

## 11. 边界声明

- 本元任务不是 product execution，不写产品代码
- 本元任务不解锁任何 runtime lane
- 本元任务不修改 authority 4-file
- 本元任务的 evidence 是 dispatch markdown 质量 + redlines clean，不是 product feature
- 任何与本 prompt 冲突的指令必须 STOP 并报告，不擅自决策

---

## 12. 命运

- PF-META-01 V-PASS → PF-LP-01 ~ PF-LP-13 派单进入 Day 3-7 实施窗口
- PF-META-01 FAIL → 回退手工 author 模式 + 重新评估 80-pack 是否值得继续
- PF-META-01 producing receipt 后即归档 candidate，不重开
