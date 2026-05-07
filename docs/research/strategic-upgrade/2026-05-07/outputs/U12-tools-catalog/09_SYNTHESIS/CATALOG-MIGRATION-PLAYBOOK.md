---
title: Catalog Migration Playbook
status: candidate / evidence-bounded / not-authority
created_at: 2026-05-06
---

# Catalog Migration Playbook

## Goal

把本 evidence-bounded pack 升级为真实 U12 catalog，需要从“候选描述”迁移到“本机事实”。迁移不要一次性重写所有文件，而应按 cluster 批量推进，每批先读路径、再抽 frontmatter、再比对冲突、最后更新 stdout。

## Batch Order

推荐顺序：先 G（Codex/RAW skill surfaces，因为上传 AGENTS 已有证据），再 A/B（skills 与 agents），再 C/D（plugin 与 MCP），最后 E/F（hooks 与 scripts）。原因是 hook/script 具有最大副作用风险，不能在未掌握技能和插件全貌前贸然归并。

## Merge Rules

当发现本地真实 entry 与本包候选 entry 同名时，不要简单覆盖。应保留本包的治理字段，补入真实 source path、frontmatter 摘要、版本、实际 activation、实际 dependencies；若真实文件和候选描述不一致，以真实文件为准，并把候选段落改为 migration note。

## Deletion Rules

不存在的条目不必强行保留。可以移到 backlog，或保留为 `proposed`，但必须从 master count 的 verified subtotal 中扣除。用户需要的是可用目录，不是数字好看的目录。
