---
title: 修订版 First 4 Dispatch — Post-Frozen Successor Entry
status: candidate / research / not-authority
created_at: 2026-05-06
author: Claude (CC0)
relates_to:
  - docs/research/post-frozen/claude-deep-review-2026-05-06.md
  - docs/research/post-frozen/80-pack-source/02_task_packs/PF-C0-O1-successor-entry-pack/
  - docs/research/post-frozen/pf-meta-01-commander-prompt-2026-05-06.md
---

# 修订版 First 4 Dispatch（PF-C0/O1 successor entry near-term mainline）

> 本文件给出 user 决策 3 接受的修订建议：把原 80-pack 的 PF-C0-O1-successor-entry-pack 12 dispatch
> 压成实际开工的 4 个修订 dispatch。
>
> 原 12 dispatch 仍保留为 reservoir（在 `docs/research/post-frozen/80-pack-source/`），
> 本文件是它们的 *commander-ready 修订版*，可直接被 PF-META-01 元任务消费产出 production-grade dispatch。

## 修订原则

按 `claude-deep-review-2026-05-06.md` §3 W1/W6/W10 的修复方向：

- W1 修：每 dispatch §1 Goal 必须任务原生（一句话覆盖动词 + 对象 + 接缝点）
- W6 修：合并 PF-O1-02 ~ PF-O1-06 五个 overflow gate 进 PF-O1-01 的五行表
- W10 修：合并 PF-C0-03（successor entry gate memo）+ PF-C0-04（preview-only scope note）为一份
- 同时：drop PF-C0-02（frozen boundary lock — 已在 §0 重述够多次，不需独立 dispatch）

## 修订后 4 dispatch 速查

| Code | Title | Replaces | Output | proof_kind | human_gate |
|---|---|---|---|---|---|
| PF-C0-01R | Live authority readback after PR194 | PF-C0-01 | `docs/research/post-frozen/live-authority-readback-after-pr194.md` | shape_only | none |
| PF-C0-MERGED-03+04 | Successor entry & preview-only scope memo | PF-C0-03 + PF-C0-04 + PF-C0-05 | `docs/research/post-frozen/successor-entry-and-preview-scope-2026-05-06.md` | shape_only | none |
| PF-C0-06R | Near-term execution matrix（20-30 mainline） | PF-C0-06 | `docs/research/post-frozen/near-term-execution-matrix-2026-05-06.md` | shape_only | none |
| PF-O1-01R | Overflow registry v0（含原 O1-02~06 五行表） | PF-O1-01 ∪ PF-O1-02~06 | `docs/research/post-frozen/overflow-registry-v0.md` | none | none |

## 修订原 12 dispatch 命运表

| 原 dispatch | 命运 | 理由 |
|---|---|---|
| PF-C0-01 | 保留为 PF-C0-01R | 内容直接可用，仅 §1 Goal 要任务原生化 |
| PF-C0-02 | DROP | 每 dispatch §0 已 80 处重述 frozen boundary，不需独立 |
| PF-C0-03 | 合并 → MERGED-03+04 | 与 04 写作目标重叠 |
| PF-C0-04 | 合并 → MERGED-03+04 | 同上 |
| PF-C0-05 | 合并 → MERGED-03+04 | dispatch naming reset 与 successor entry 是同一份 memo |
| PF-C0-06 | 保留为 PF-C0-06R | execution matrix 是独立产出，保留 |
| PF-O1-01 | 保留为 PF-O1-01R | 改为承载五行 overflow 表 |
| PF-O1-02 | 合并 → O1-01R 行 1 | true vault write |
| PF-O1-03 | 合并 → O1-01R 行 2 | runtime tools |
| PF-O1-04 | 合并 → O1-01R 行 3 | browser automation |
| PF-O1-05 | 合并 → O1-01R 行 4 | DBvNext + migration |
| PF-O1-06 | 合并 → O1-01R 行 5 | full Signal Workbench |

12 → 4，但产出信息无丢失。

## 4 个修订 dispatch 完整文本

### PF-C0-01R — Live authority readback after PR194

```yaml
status: candidate_task_draft_not_authority
pack: PF-C0-O1-successor-entry-pack
cluster: PF-C0
dispatch_class: successor_entry
open_after_state: live_authority_readback_after_PR194
proof_kind: shape_only
human_gate: none
priority: blocker
can_parallel: yes
serial_gate: none
```

#### §0 Frozen historical boundary

Inherits `_PACK-DEFAULTS.md` (Dispatch126-176 frozen, no reopen).

#### §1 Goal

在 `docs/research/post-frozen/live-authority-readback-after-pr194.md` 落一份 readback 表，区分 zip-derived fact / live GitHub fact / PR194 candidate truth；明确 PR193/194 已基本完成 authority sync，PR194 STEP0 模板仅 candidate-only，AGENTS.md 已不 stale。

#### §2 Expected output

`docs/research/post-frozen/live-authority-readback-after-pr194.md`

#### §3 Dependencies

- none

#### §4 Files preview

```
files_to_create:
  - docs/research/post-frozen/live-authority-readback-after-pr194.md
files_to_modify:
  - (none)
files_will_NOT_touch:
  - docs/current.md
  - AGENTS.md
  - docs/task-index.md
  - docs/decision-log.md
  - services/api/**
  - apps/**
```

#### §5 Forbidden paths / claims

Inherits `_PACK-DEFAULTS.md` (services/api/migrations/, workers/, packages/, data/, referencerepo/, raw credentials, true vault write).

#### §6 Blocked claims that remain blocked

Inherits `_PACK-DEFAULTS.md` + 显式补：mount Bridge router 不解禁 write（`bridge/config.py:24,36` `write_enabled=False` 硬挂）。

#### §7 Enter condition

Inherits `_PACK-DEFAULTS.md`.

#### §8 Pass condition

Readback 表至少含 5 行：(1) zip 上传时 truth；(2) PR192 时 Codex readback；(3) PR193 batch ABC closeout；(4) PR194 STEP0 templates；(5) live 当前 docs/current.md / AGENTS.md / main.py 状态。每行带证据 path 或 commit SHA。

#### §9-11 Partial / Fail / Kill

Inherits `_PACK-DEFAULTS.md`.

#### §12 Validation

```bash
python tools/check-docs-redlines.py docs/research/post-frozen/
python tools/check-secrets-redlines.py docs/research/post-frozen/
git diff --check docs/research/post-frozen/
```

#### §13 Evidence shape

```yaml
proof_kind: shape_only
evidence_shape:
  output_path: docs/research/post-frozen/live-authority-readback-after-pr194.md
  required_rows: 5
  required_columns: [class, claim, evidence_path_or_sha, verdict]
```

---

### PF-C0-MERGED-03+04 — Successor entry & preview-only scope memo

```yaml
status: candidate_task_draft_not_authority
pack: PF-C0-O1-successor-entry-pack
cluster: PF-C0
dispatch_class: successor_entry
open_after_state: live_authority_readback_after_PR194
proof_kind: shape_only
human_gate: none
priority: high
can_parallel: yes
serial_gate: PF-C0-01R must merge first
```

#### §1 Goal

在 `docs/research/post-frozen/successor-entry-and-preview-scope-2026-05-06.md` 一份 memo 中明示：(a) 后继路线 = PF-C0/O1 → PF-LP → PF-C1 → PF-C2 → PF-C4，不接受线性 Dispatch177+；(b) preview-only A 档目标 = localhost paste URL → create capture → vault-preview markdown → copy/download；(c) PF-* dispatch 命名取代 Dispatch177+ 自动续号。

#### §2 Expected output

`docs/research/post-frozen/successor-entry-and-preview-scope-2026-05-06.md`

#### §3 Dependencies

- PF-C0-01R

#### §4 Files preview

```
files_to_create:
  - docs/research/post-frozen/successor-entry-and-preview-scope-2026-05-06.md
files_to_modify: (none)
files_will_NOT_touch:
  - docs/current.md
  - AGENTS.md
  - docs/task-index.md
  - 80-pack-source/**
```

#### §8 Pass condition

Memo 含三段：(1) successor route mermaid + frozen boundary；(2) preview-only A 档 pass bar 七步；(3) PF-* naming + 拒绝 Dispatch177+ 自动续号。

#### §13 Evidence shape

```yaml
proof_kind: shape_only
evidence_shape:
  output_path: docs/research/post-frozen/successor-entry-and-preview-scope-2026-05-06.md
  required_sections: [successor_route_diagram, preview_only_pass_bar, dispatch_naming_reset]
```

(其余 §0/§5/§6/§7/§9/§10/§11/§12 inherits `_PACK-DEFAULTS.md`)

---

### PF-C0-06R — Near-term execution matrix（20-30 mainline only）

```yaml
status: candidate_task_draft_not_authority
pack: PF-C0-O1-successor-entry-pack
cluster: PF-C0
dispatch_class: successor_entry
open_after_state: live_authority_readback_after_PR194
proof_kind: shape_only
human_gate: none
priority: high
can_parallel: yes
serial_gate: PF-C0-MERGED-03+04 should land first
```

#### §1 Goal

在 `docs/research/post-frozen/near-term-execution-matrix-2026-05-06.md` 给出一张表，明示 80 dispatch 中哪 20-30 个是 near-term mainline、哪些是 reservoir、哪些是永久 overflow；每行带 cluster、priority、open_after_state、estimated_dispatch_count。

#### §2 Expected output

`docs/research/post-frozen/near-term-execution-matrix-2026-05-06.md`

#### §3 Dependencies

- PF-C0-MERGED-03+04
- PF-O1-01R

#### §8 Pass condition

矩阵表至少含 80 行（每 dispatch 一行）+ priority 列分 blocker/high/medium/reservoir/permanent_overflow + cluster 列对齐 manifest.jsonl。可执行 near-term 总数在 [20, 30] 内。

#### §13 Evidence shape

```yaml
proof_kind: shape_only
evidence_shape:
  output_path: docs/research/post-frozen/near-term-execution-matrix-2026-05-06.md
  required_rows: 80
  required_columns: [code, cluster, priority, open_after_state, estimated_count, status]
  near_term_count_range: [20, 30]
```

(inheriting blocks omitted)

---

### PF-O1-01R — Overflow registry v0（含 5 行 overflow gate 表）

```yaml
status: candidate_task_draft_not_authority
pack: PF-C0-O1-successor-entry-pack
cluster: PF-O1
dispatch_class: overflow
open_after_state: live_authority_readback_after_PR194
proof_kind: none
human_gate: none
priority: blocker
can_parallel: yes
serial_gate: none
```

#### §1 Goal

在 `docs/research/post-frozen/overflow-registry-v0.md` 落一份 overflow registry，含 5 行 high-risk 主题（true vault write / runtime tools / browser automation / DBvNext+migration / full Signal Workbench），每行带 blocked_reason / reopen_condition / human_gate / kill_switch_ref / owner。

#### §2 Expected output

`docs/research/post-frozen/overflow-registry-v0.md`

#### §3 Dependencies

- none

#### §4 Files preview

```
files_to_create:
  - docs/research/post-frozen/overflow-registry-v0.md
files_to_modify: (none)
files_will_NOT_touch:
  - services/**
  - apps/**
  - workers/**
  - packages/**
  - data/**
```

#### §8 Pass condition

Registry 含 5 行 + 每行 5 列（blocked_reason / reopen_condition / human_gate / kill_switch_ref / owner）+ 无单独 PF-O1-02~06 dispatch 需要后续派单。

#### §13 Evidence shape

```yaml
proof_kind: none
evidence_shape:
  output_path: docs/research/post-frozen/overflow-registry-v0.md
  required_rows: 5
  required_columns: [topic, blocked_reason, reopen_condition, human_gate, kill_switch_ref, owner]
  topics_required:
    - true_vault_write
    - runtime_tools (BBDown / yt-dlp / ffmpeg / ASR / audio_transcript)
    - browser_automation / playwright_execution
    - dbvnext / migrations
    - full_signal_workbench
```

(其余 inheriting blocks omitted)

## 派单顺序建议

```text
Day 1
  -> 并行: PF-C0-01R + PF-O1-01R（无依赖，shape_only）
  -> verdict: 各自 readback 后由 user shape-level 复核

Day 2
  -> 串行: PF-C0-MERGED-03+04（依赖 01R）
  -> 串行: PF-C0-06R（依赖 03+04 + O1-01R）
  -> verdict: user 看 execution matrix 确认 near-term 20-30 选择

完成 4 dispatch 后：
  -> A 档 mainline 启动条件成熟
  -> 进 PF-LP-01 等 8-13 dispatch
```

## 边界

- 本文件 candidate-only，非 authority
- 不直接覆盖原 80-pack-source 的 dispatch markdown — 它们仍保留为 reservoir
- PF-META-01 元任务（commander prompt 见 `pf-meta-01-commander-prompt-2026-05-06.md`）会按本修订版重写 80-pack-source 中相关 dispatch
