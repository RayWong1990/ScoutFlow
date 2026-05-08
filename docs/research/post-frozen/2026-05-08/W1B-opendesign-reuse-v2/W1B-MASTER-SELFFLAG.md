---
title: W1B OpenDesign Reuse v2 — Master Self-flag (cross-deliverable caveat)
status: candidate / self-flag / not-authority
authority: not-authority
created_by: gpt-pro (extracted by CC0 from full-output.md line 1454-1457)
parent_cluster: W1B
extracted_at: 2026-05-08
extracted_reason: |
  Master Self-flag 在 GPT Pro 输出的 full-output.md 末尾 3 条 caveat, 但 zip 内 4 文件 (01 cluster spec / 02 dispatch pack / 03 codex commander / 04 hermes audit) 没复刻这 3 条. CC0 mv 到 docs/research/post-frozen/2026-05-08/W1B-opendesign-reuse-v2/ 时, 4 文件下游 (Codex/Hermes) 拿到的就丢了这 3 条硬约束.
  本文件抽出独立保存, 跟 4 文件平级落地, PR body 也 inline.
upstream_audit_finding: "W3 audit P2: Master Self-flag 没在 zip 内 4 文件复刻, 下游会丢 caveat"
disclaimer: 真态数字以 GitHub live main HEAD 为准; 撰写时刻数字仅为历史参考。
---

# W1B Master Self-flag (跨 4 deliverable caveat)

> 本文件 3 条 caveat 来自 W1B GPT Pro 60min one-shot 输出末尾, 适用于 4 deliverable 全部 (cluster spec / dispatch pack / codex commander / hermes audit). 任何下游消费者 (Codex / Hermes / CC1 audit) 起手必读, 不得忽略.

## ⚠️ Caveat 1 — Authority anchor / commit search split-truth

Live authority anchor (`docs/current.md` body 写的 `c802de4`) 跟 recent commit search (live `git log origin/main` 的 `6dd27d7`) 存在 split-truth.

**处置**: 在 W1B 真 register (D-W1B-001 preflight) 前, 必须 refresh authority docs (current.md / 00-START-HERE.md last_refreshed_from_main_sha) 到 live main HEAD. Hermes audit 跑 D-W1B-002 时也必须先 verify 这点, 不背 anchor 漂.

跟 instinct §3 #17 (PR # ≠ chronological, 必 grep verify) 直接对应.

## ⚠️ Caveat 2 — Bundle-size / tree-shaking gates 需要 local build evidence

Bundle-size budget (v2-D19 ≤ 50kB gzip) 与 tree-shaking 验证, **GPT Pro 在 60min one-shot 内不能真测**, 因为不能跑 `pnpm build` / `vite build --report` / 真 base bundle measure.

**处置**: 这两个 gate 是 Codex Long Runner 实施 D-W1B-007 (bundle baseline) 时的硬验收, 不允许从 GPT Pro 输出推断真值. CC0 在 mv 4 deliverable 时, dispatch pack §4 acceptance 列要求 Codex 跑 build 真测, 给 numerical evidence (kB 数, before/after baseline diff).

## ⚠️ Caveat 3 — Browser visual evidence remains conditional on current execution gate

Browser visual gate (V-PASS / 5 Gate human review) 仍受当前 execution gate 限制 (5 overflow lane Hold / write_enabled=False / no browser_automation runtime). v2-D 路径任何 visual evidence claim 都不能假装 execution gate 已解禁.

**处置**: dispatch pack 任何 V-PASS 字段 / Hermes audit dimension 含 visual review 的部分, 必须显式 condition 在 "若 browser_automation lane 解禁后" 或 "本地 manual screenshot capture without runtime" 两个限定路径之一. 不允许写"V-PASS 直接通过"暗示 lane 解禁.

跟 master spec §16.1 #4 (browser_automation 5 overflow lane Hold) 直接对应.

---

## 应用边界

本 Master Self-flag 适用于 W1B 4 deliverable **全部**:
- 01-cluster-spec.md
- 02-dispatch-pack.md
- 03-codex-commander.md
- 04-hermes-audit.md

下游消费者 (Codex / Hermes / CC1 audit) 跑任何 4 文件之前, 必先核 3 条 caveat. PR body 也必 inline 这 3 条.

---

## Origin

- 提取自: `/Users/wanglei/Downloads/5个任务/W1B-opendesign-reuse-v2-full-output.md` line 1454-1457 (GPT Pro 60min 输出末尾)
- audit catch: ScoutFlow 2026-05-08 W3 product audit P2 — Master Self-flag 没在 zip 4 文件复刻, 下游会丢 caveat
- 提取目的: 跟 4 文件平级落地 docs/research/post-frozen/2026-05-08/W1B-opendesign-reuse-v2/, 防 caveat 流失
