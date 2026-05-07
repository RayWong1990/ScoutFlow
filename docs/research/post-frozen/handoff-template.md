---
title: <一句话, 主题>
date: YYYY-MM-DD
session_id: <CC1/CC0 session id, optional>
agent: CC1 / CC0 / GPT Pro / Codex / Hermes / 战友
type: decision / pr-merge / wave-start / lane-unlock / audit-verdict / amend
related_pr: PR #N (optional)
related_wave: WnX (optional, 对应 master spec § 13.1)
status: candidate / handoff / not-authority
---

# Handoff: <一句话标题>

## 背景 (1-2 行)

<触发的事件 / 为什么写这个 handoff>

## 决策 / 动作 (1-2 行)

<具体决定了什么 / 做了什么>

## 影响 (1-2 行, 含 main HEAD / Active 数 / lane 状态变更)

<对真态的影响>

## 后续 (1-2 行)

<下一步是什么 / 谁负责 / 什么时候>

---

> 模板 by CC1 (Anthropic), 2026-05-07. 关联: docs/research/post-frozen/CC1-session-retrospective-2026-05-07.md / 元认知 instinct §3 第 18 条落地.
> 使用方法: 复制本模板 → 改文件名为 `<YYYY-MM-DD>-<topic-slug>.md` → 落 `docs/research/post-frozen/handoff/`. 不进 authority writer slot.
