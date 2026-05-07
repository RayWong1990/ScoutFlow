---
title: ScoutFlow docs/memory/ — Cross-Vendor Memory Path
status: current authority
created_at: 2026-05-07
---

# docs/memory/

ScoutFlow 跨 vendor 可读的 instinct memory 真源.

**入口**: [INDEX.md](./INDEX.md)

**4 状态词锁**: 本目录所有 file `status: current authority` (跟 `docs/current.md` / `docs/task-index.md` / `docs/decision-log.md` / `docs/00-START-HERE.md` 同级).

**跨 vendor 共享**:

- 任何 agent (Claude Code / Codex / GPT Pro / Hermes) 可通过 git tracked path 读
- cloud LLM 可通过 GitHub raw URL fetch (e.g. `https://github.com/RayWong1990/ScoutFlow/blob/main/docs/memory/lessons/L-CANDIDATE-PROMOTION.md`)
- 不双写到 `~/.claude/`, 唯一真源即 git tracked

**第一批**: 2026-05-07 W2D U16 memory ingest 入选 16 条 (lesson 6 + feedback 5 + pattern 5), source = `MASTER-MEMORY-ATLAS.md` 79 candidate node.

**format**: 每 file 含 frontmatter (`name` / `description` / `type` / `source_atlas_node` / `cross_vendor_readers` / `status`) + body 三段 (rule / Why / How to apply, ≤600 字 中文+半角混排).

**维护**: 见 [INDEX.md §维护规则](./INDEX.md).
