# Project Context

## ScoutFlow 是什么

ScoutFlow 是一个面向个人研究工作流的 authority-first 内容采集、转写、规整与证据账本系统。

## 不是什麼

- 不是全平台全量抓取系统
- 不是多用户 SaaS
- 不是当前就要实现的推荐平台
- 不是当前就要实现的产品代码仓

## Authority-first 四层

- `L0 Authority`: SQLite + FS layout + state words
- `L1 Workers`: 后续 stateless worker
- `L2 Thin API`: 后续 contract enforcement
- `L3 Console`: 后续 UI projection

## FS 六区

- `bundle`
- `media`
- `transcript`
- `normalized`
- `links`
- `logs`

## Phase Scope Freeze

- 当前批准范围：`Phase 0`、`Phase 1A`
- 当前只作参考 outline：`Phase 1B`、`Phase 2`、`Phase 3`、`Phase 4`

## 当前工具栈

- `Codex Desktop`
- `Claude Code / VSCode`
- `ChatGPT Pro`
- `OpenClaw`
- `Hermes CLI`

## 当前红线

- 不写 API / worker / Console 产品代码
- 不修改 `data/`
- 不修改 `referencerepo/`
- 不创建重治理顶层目录
- `/captures/discover` 继续是 `capture 创建入口（capture creation entrypoint）`
- `recommendation / keyword / RAW gap` 不直接创建 capture

## 后续 Phase 0 / 1A 目标

- `Phase 0`: Git bootstrap、根轻配置、入口文档、contract 基线、后续目录骨架准备
- `Phase 1A`: 未来只收口 Bilibili `manual_url` quick_capture 主路径，不扩展到 Phase 2+
