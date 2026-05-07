# Handoff Directory

跨 session 决策落地目录. 用 `../handoff-template.md` 模板.

## 命名 convention

`<YYYY-MM-DD>-<topic-slug>.md` (e.g. `2026-05-08-pr246-merged.md`).

## status 字段 (必填)

锁定 4 类之一 (START-HERE §2, 不引新状态词):
- `current authority` (一般不用 — 真态 ledger)
- `promoted addendum` (一般不用 — PRD/SRD 升级补丁)
- `candidate north-star` (一般不用 — 候选路线图)
- `reference storage` (**默认** — handoff 实例都用这个)

## 触发条件

元认知 instinct §3 第 18 条: 关键决策 / 跨 session 状态变更 → 落本目录:

- 新 PR merge / wave 启动 / lane 解禁 / authority 升级
- 战友拍板的重大方向 (跨 session 必须知道)
- agent 间互审结论 (CC1↔CC0 / Layer 2 audit verdict)

## 内容规范

- 每份 handoff 内容 ≤ 15 行 (frontmatter 不含)
- 4 段式: 背景 / 决策 / 影响 / 后续
- 不进 authority writer slot (max=1 不占)

## Index

(目录起步, 后续 handoff 实例会列在此)
