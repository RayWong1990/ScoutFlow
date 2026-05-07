---
title: LIVE WEB EVIDENCE REFRESH — U8 Egress
status: candidate / evidence-refresh-blocked / not-authority
authority: not-authority
claim_label: "blocked for live verification; 95% honesty on boundary reporting"
created_at: 2026-05-07
generated_in_environment: 2026-05-06
live_web_browsing_used: false
live_verified_count: 0
web_tool_status: disabled
---

# LIVE WEB EVIDENCE REFRESH — U8 Egress

## 1. Truthful status

本 Cloud Prompt 要求 ≥12 次真实 live web search：Obsidian frontmatter、Logseq/Tana/Capacities/Heptabase/Reflect export、YAML frontmatter、inter-app Markdown、Hugo/Jekyll/11ty、file-based event sourcing、PII redaction、Apple Spotlight/xattr 等。当前会话的普通 web 浏览工具被禁用，且系统要求不得通过其他工具规避访问网页。因此本文不能声称已经访问这些页面，不能写“访问日期已验证”，也不能把旧知识包装成 live 证据。

本文件仍提供两个价值：第一，列出未来应该真实刷新的 evidence checklist；第二，把这些外部模式如何影响 U8 contract 的设计原则写清楚。所有条目均标记 `live_verified: false`，等待后续有浏览权限的环境刷新。

## 2. 未验证候选清单（需后续 live refresh）

| # | 主题 | 候选来源/关键词 | U8 设计影响 | live_verified |
|---:|---|---|---|---:|
| 1 | Obsidian Properties / frontmatter | Obsidian help properties YAML frontmatter | 使用 YAML frontmatter、tags/aliases，但专用字段 namespace | false |
| 2 | Obsidian Publish/Sync | Obsidian Publish, Sync docs | 默认 local_only，不把 sync/publish 当 acceptance | false |
| 3 | Dataview plugin | Dataview frontmatter fields | `scoutflow_*` 字段便于查询，不依赖正文 parser | false |
| 4 | Logseq Markdown export | Logseq export markdown properties | 保持 Markdown 单文件可读，避免插件专属语法 | false |
| 5 | Tana export | Tana export markdown/supertags | 不把复杂图谱属性强加给 ScoutFlow | false |
| 6 | Capacities export | Capacities object export markdown | 资产用 kind + manifest，而不是对象数据库同步 | false |
| 7 | Heptabase export | Heptabase markdown export/cards | topic card 可导出 Markdown，但不是 true knowledge | false |
| 8 | Reflect notes export | Reflect markdown export | 简化 frontmatter，保证人工可迁移 | false |
| 9 | YAML frontmatter | YAML metadata block convention | frontmatter key 唯一，值类型稳定 | false |
| 10 | Jekyll front matter | static site generator metadata | `---` YAML block 是广泛模式，但不要引入 site build 字段 | false |
| 11 | Hugo front matter | TOML/YAML/JSON frontmatter | U8 选 YAML，避免格式多样化 | false |
| 12 | Eleventy data/front matter | 11ty frontmatter data cascade | 不让全局 data cascade 污染单文件合同 | false |
| 13 | File-based event sourcing | filesystem event log pattern | manifest + checksums + immutable revisions | false |
| 14 | Filesystem-as-database | local-first file database pattern | 不把 FS 替代 SQLite authority，只做 handoff staging | false |
| 15 | PII redaction in Markdown | regex + NER redaction practices | regex 是第一层，字段策略 +人工审核必须保留 | false |
| 16 | Apple Spotlight metadata/xattr | macOS extended attributes | 不依赖 xattr；manifest 作为跨系统 metadata | false |

## 3. 设计结论（不依赖 live 声称）

即使没有 live refresh，也可以基于 ScoutFlow 已有 PRD/SRD/RAW staging evidence 做出保守结论：

1. Markdown + YAML frontmatter 是最小跨工具载体，但每个下游对字段、tags、aliases 的解释不同，所以 ScoutFlow 必须声明字段而不是让下游猜。
2. manifest 是必要的，因为单个 `.md` 不能可靠表达一次 handoff 的 asset list、checksum、redaction、supersede、origin。
3. Obsidian/Logseq/Tana/Capacities/Heptabase/Reflect 这类工具都可能把 Markdown 当知识对象，但 U8 不能因此把 ScoutFlow preview 写成 knowledge final。
4. Static site generator 的 frontmatter 经验说明 YAML block 很通用，但也提醒我们不要把 `layout`, `permalink`, `draft` 等站点字段引入 ScoutFlow egress。
5. File-based event sourcing 的思想适合 handoff manifest：append-only revision、checksum、supersede，而不是就地覆盖。
6. xattr/Spotlight metadata 不适合作为核心合同，因为跨平台、跨 zip、跨 Git 保存不稳定；manifest 更稳。

## 4. 后续 live refresh runbook

当 web browsing 可用时，执行：

1. 搜索 Obsidian Properties YAML frontmatter docs，记录 URL、标题、访问日期、关键字段。
2. 搜索 Obsidian tags / aliases / Publish / Sync docs，确认 tags 格式和 Publish 风险。
3. 搜索 Dataview frontmatter field syntax，确认 `scoutflow_*` 查询友好性。
4. 搜索 Logseq Markdown export properties，确认不引入 Logseq block refs。
5. 搜索 Tana export/supertags，确认复杂对象不适合 U8。
6. 搜索 Capacities export Markdown，确认 object export 模式。
7. 搜索 Heptabase export Markdown/cards，确认 card-to-Markdown 风险。
8. 搜索 Reflect notes export，确认 Markdown export 实态。
9. 搜索 YAML frontmatter standard/commonmark notes，确认 YAML block 不是 CommonMark 核心但为生态约定。
10. 搜索 Jekyll/Hugo/Eleventy frontmatter docs，确认 static generator fields 不应污染。
11. 搜索 file-based event sourcing / filesystem-as-database，确认 manifest/checksum/revision 模式。
12. 搜索 PII redaction markdown regex NER，确认 redaction catalog 是否要升级。
13. 搜索 Apple Spotlight metadata/xattr，确认不能依赖 metadata forks。

每条 live evidence 应写：`url`, `title`, `publisher`, `accessed_at`, `observed_claim`, `impact_on_contract`, `confidence`, `limitations`。没有真实访问前，不允许写 `live_verified=true`。

## 5. 本交付对 live gap 的处理

- DiloFlow/hermes-agent：因本地 repo 未观测，采用单方 file contract。
- Obsidian：采用保守 Markdown/YAML namespace，不声称插件最新行为。
- RAW：主要依据已读取的 Run-3+4 staging 与 RAW frontmatter 模板，受 live gap 影响较小。
- Redaction：采用安全优先策略，宁可 omit。
- Supersede：采用 append-only manifest，不依赖 vendor 特性。

## 6. 建议验收口径

本文件不满足 Cloud Prompt 中“≥12 live search 已完成”的事实要求；它满足“不得伪造 live evidence”的可信要求。若验收必须严格要求 live search，本包应标为 `ready_for_user_audit: yes_with_live_web_gap`，并在有浏览权限后补跑 Pass 2。

## 自检清单

| # | 检查项 | 结论 |
|---:|---|---|
| 1 | 是否漂移成 SDK / OpenAPI / broker | 否，仅文件级 frontmatter、目录、manifest |
| 2 | 是否把 RAW / Obsidian / DiloFlow 当 ScoutFlow 子模块 | 否，全部是 downstream candidate |
| 3 | 是否暗示 ScoutFlow 直写 `~/workspace/raw/` | 否，RAW 仅 staging + manual transfer |
| 4 | 是否把 C2 partial 写成 pass | 否，保留 pending_user_manual_transfer |
| 5 | 是否把 vault preview 当 true write | 否，preview_only / write_enabled=false |
| 6 | 是否解锁 media / ffmpeg / ASR / browser automation | 否，blocked lanes 原样保留 |
| 7 | 是否包含凭据、cookie、token、QR 图片 | 规范中禁止，实际未导出此类文件 |
| 8 | 是否覆盖 supersede | 是，软标记 + manifest 索引 + 下游 prune 触发 |
| 9 | 是否覆盖 redaction | 是，字段级 omit/mask/hash + 自动检查建议 |
| 10 | 是否声称 live web 已完成 | 否，明确 blocked / not live verified |
| 11 | 是否声称本地 DiloFlow/hermes repo 已验证 | 否，当前容器未发现 sibling repo |
| 12 | 是否污染 Obsidian template | 否，仅给兼容字段，不要求替换用户模板 |
| 13 | 是否让下游必须遵守 | 否，单方声明，建议遵守 |
| 14 | 是否可由单人实现 | 是，建议 ≤400 LOC + 4 schema 文件 |
| 15 | 是否与 U1-U7 基线冲突 | 未发现直接冲突；保持 v2 boundaries |
| 16 | 是否允许旧资产静默失效 | 否，必须写 superseded_by / manifest supersede_summary |
| 17 | 是否混淆 source_url 与 signed URL | 否，signed URL 需去签名或 omit |
| 18 | 是否把 PII redaction 当真实已跑 | 否，本文是 spec，非执行日志 |
## 7. 未来 live evidence 记录模板

每一次 live refresh 都应以同一模板记录，避免“搜过但不可审计”：

```yaml
evidence_id: WEB-OBS-001
topic: Obsidian Properties / frontmatter
url: <actual URL>
publisher: <publisher>
accessed_at: <ISO timestamp>
live_verified: true
observed_claim: <one sentence>
impact_on_u8: <field/path/redaction/supersede implication>
confidence: high | medium | low
limitations: <what this source does not prove>
```

重要的是 `limitations`。例如 Obsidian 文档只能证明 Obsidian 如何解析 Properties，不能证明 RAW vault 的四字段模板，也不能证明 DiloFlow parser。Jekyll/Hugo 文档只能证明 frontmatter 是成熟模式，不能证明 Obsidian 或 RAW 接受某个字段。PII redaction 文章只能提供方法，不能证明 ScoutFlow 的具体 scanner 已运行。

## 8. 可能改变当前合同的 live findings

如果后续 live refresh 发现 Obsidian Properties 对某些 YAML 类型有新限制，应调整 Obsidian variant，但不影响 RAW 四字段。若发现某个工具导出 Markdown 时会丢弃未知 frontmatter，应强化 manifest，而不是减少 ScoutFlow fields。若 PII redaction 最新实践强烈建议 NER/LLM hybrid，应把 redaction catalog 升级为 regex + field allowlist + NER optional，但仍不能把 LLM side process 当秘密扫描唯一机制。若 xattr/Spotlight 在 zip/Git 下仍不稳定，继续不用；若某工具可靠保存 xattr，也只能作为辅助，不能替代 manifest。

## 9. Why this gap is not hidden

本交付选择把 live gap 写成文件，是因为 egress contract 的核心价值之一就是防 silent breakage。伪造 live evidence 会比缺 evidence 更危险：下游可能基于错误“已验证”做 parser 或 template。当前做法是保守：本地/ GitHub/上传 pack 证据足以定义 ScoutFlow-side 不变量；vendor/tool 细节保留为待刷新项。
## 10. Evidence freshness policy

Live refresh 不是一次性动作。凡是会受产品更新影响的外部工具，例如 Obsidian Properties、Dataview、Tana、Capacities、Heptabase、Reflect，都应在 contract promoted 前刷新；凡是相对稳定的模式，例如 YAML frontmatter、Jekyll/Hugo/Eleventy metadata block、append-only manifest、checksum，则可以降低刷新频率，但仍要记录来源。若外部工具改变导出格式，U8 的应对不是改变 ScoutFlow authority，而是更新对应 downstream renderer 和 README-handoff。

## 11. Evidence conflict handling

如果 live evidence 之间冲突，以 ScoutFlow 安全边界优先。例如某工具允许在 frontmatter 中放任意对象，并不意味着 ScoutFlow 可以放凭据；某工具支持双向同步，并不意味着 U8 可以打开 true write；某工具支持自动导入 Markdown，并不意味着 RAW acceptance 自动成立。外部 evidence 只能增强兼容性判断，不能削弱 PRD/SRD 的红线。

## 12. Minimum promotion gate

在没有 live refresh 前，本文件只能作为 gap register。promotion gate 应要求：至少 12 条 `live_verified=true` 记录、每条都有 URL 和访问时间、至少 3 条与 Obsidian/Markdown 直接相关、至少 2 条与 redaction/privacy 相关、至少 2 条与 file-based metadata/manifest 相关。未达到这些条件时，不得把本包的 external evidence 部分标为 complete。
