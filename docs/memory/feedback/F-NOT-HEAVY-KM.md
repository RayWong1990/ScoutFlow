---
name: not-heavy-knowledge-mirror
description: 不要建第二知识库 / mirror; 唯一真源 + 短入口指针 > 重复建 doc
type: feedback
source_atlas_node: F-NOT-HEAVY-KM
cross_vendor_readers: [cc0, cc1, codex, gpt-pro, hermes]
status: current authority
---

# No heavy knowledge mirror

每类信息只有一个真源 + 短入口指针. 不允许 "建第二个 X" — 第二份 doc 会快速 drift, 最终出现 "两份冲突真源". ScoutFlow / RAW vault / DiloFlow / ContentFlow 之间 entity 引用关系**借 asset_id 引用**, 不**镜像 copy**.

**Why:** ScoutFlow `~/.claude/rules/codex-metacognition-learnings.md §1.7` 沉淀的元认知规则. 历史多次出现 "为了方便又写一份" → drift 教训. ContentFlow L 项目 21 swap 协作中实证.

**How to apply:** 见到 "建第二个 X" 先问 "已有的 X 能不能改 / 引用". memory 跨 vendor 共享走 git tracked 主源 (本 PR docs/memory/) + 入口指针 (00-START-HERE 链 INDEX), 不双写到 ~/.claude/. handoff / commander prompt 短入口 (~80 行) 链 authority files, 不重复 PRD/SRD 长内容.
