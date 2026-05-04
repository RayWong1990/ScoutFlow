---
title: Explore Preview 视觉候选
date: 2026-05-04
status: candidate
not_authority: true
not_implementation_gate: true
not_acceptance_checklist: true
not_runtime_approval: true
source_pr: "#40"
source_task: T-P1A-024
future_destination: "未来 Explore design spec"
---

# 1. 状态 / 边界

这份 note 记录 Explore preview 区的候选视觉语言。它只给未来 Explore design spec 留 forward pointer，不是 authority。

这份 note 不是：

- 不是 acceptance checklist。
- 不可 enforce。
- 不进入 `docs/task-index.md` 的 active task。
- 不批准 frontend implementation。
- 不改变 schema、DTO、runtime 或 Trust Trace contract。
- 不解锁 `audio_transcript`、comments、danmaku、screenshot、BBDown、ffmpeg、ASR、workers 或 frontend runtime。

下面的约束刻意使用 candidate / 建议语气。未来 Explore design spec 可以吸收、改写或废弃它们；在 spec 吸收前，它们不是 implementation gate。

# 2. 为什么需要这份候选

PR #40 把 `试一下` 和 `只采 metadata` 分开：前者是 local preview / parse，后者才是正式 capture intent。视觉语言也必须维持这个分层，否则 UI 会暗示 preview 已经创建 ledger，或者已经拿到了 metadata。

真正的风险是 `B-strict`：标题、UP、时长这些占位字段能让产品形态更具体，但如果它们看起来像 loading 或真实内容，就会滑向伪 metadata。这份 note 只保存当前讨论出的防滑坡 guardrails。

# 3. 候选视觉约束

## 3.1 未探测字段不要长得像 loading

候选视觉语言：未探测字段使用静态虚线字段区，直接写字段状态，例如 `标题 · 未探测`、`UP · 未探测`、`时长 · 未探测`。

候选理由：skeleton 灰条通常暗示“数据正在加载”。Explore 的 local preview 不是在加载平台 metadata，而是明确处于“尚未探测”。

依据：5 Gate #1 视觉层级 + 诚实状态表达。

## 3.2 真相 badge 的视觉重量高于 placeholder

候选视觉语言：`metadata 未采集`、`capture 未创建` 这类 truth badge 的视觉重量高于 placeholder 字段。placeholder 文案保持更低权重和更安静的视觉处理。

候选理由：用户 3 秒扫视时，第一眼应该先读到状态真相；placeholder 只是辅助理解未来会出现哪些字段。

依据：5 Gate #5 视觉重量 + 5 Gate #4 字体可读。

## 3.3 preview 卡和 capture 后卡片保持稳定结构

候选视觉语言：preview 状态和 capture 后状态使用稳定卡片框架，卡片高度和主要结构尽量一致，只替换内部 label 与字段状态。

候选理由：capture 创建后不应该出现明显 layout shift。稳定结构能让 solo user 在前后状态之间对比，而不是重新扫描整页。

依据：5 Gate #2 空间 / 对齐 + 扫描路径连续性。

## 3.4 本地真实、未探测字段、状态声明三层视觉分开

候选视觉语言：

- URL、BV、`source_kind` 这类本地真实数据使用正常不透明度和实线字段处理。
- 未来 metadata 占位字段使用虚线处理和更安静的文字。
- `未创建 capture` 这类状态声明在三层里视觉强度最高。

候选理由：6 个月后再看界面，也应该能一眼分清哪些字段是本地已知，哪些是占位，哪些是状态声明。

依据：5 Gate #1 视觉层级 + 5 Gate #5 视觉重量。

## 3.5 CTA 放在确认之后

候选视觉语言：`只采 metadata` action 出现在用户能先扫过本地真实信息和未探测状态之后；它不应该成为卡片中最先抢眼的对象。

候选理由：动线应是 `看清对象 -> 看到未创建 / 未探测状态 -> 决定 capture`，不是 `先点按钮 -> 再回头确认`。

依据：5 Gate #1 视觉层级 + 扫描路径安全。

# 4. 后续处理

未来 Explore design spec 可以吸收、改写或废弃这份 candidate note。如果被吸收，这份 note 应标记为 `superseded`，保留 provenance，不删除。

来源：派生自 PR #40（T-P1A-024）brainstorm 链，2026-05-04，user / Codex / Opus 三方讨论。
