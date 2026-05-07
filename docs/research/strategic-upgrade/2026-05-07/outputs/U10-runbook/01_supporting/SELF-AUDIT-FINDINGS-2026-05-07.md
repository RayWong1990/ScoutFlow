---
title: SELF AUDIT FINDINGS — U10 Runbook Library
status: candidate
authority: not-authority
created_at: 2026-05-07
runbook_id: SELF-AUDIT-FINDINGS
cluster: Supporting
trigger_keywords:
  - self-audit
  - findings
  - inline fix
risk_level: medium
single_user_applicable: true
multi_agent_applicable: true
linked_dispatch:
  - MOD-SELF-AUDIT-FINDINGS
linked_rule:
  - ~/.claude/rules/testing.md
  - ~/.claude/rules/execution-discipline.md
boundary_statement: candidate self-audit; not authority.
---

# SELF AUDIT FINDINGS

[self-audit scope] 本 self-audit 覆盖 68 个 runbook、8 个 cluster index 与 supporting files。目标是 inline fix-or-bound，而不是给出空泛 PASS。

| # | Issue | Fix or bound | Status |
|---:|---|---|---|
| 1 | Runbook 数量若只按 prompt 最低 55 生成，会缺少部分建议场景。 | 生成完整 68 个 scenario runbook，覆盖 A10/B12/C10/D10/E7/F7/G6/H6。 | fixed_inline |
| 2 | Cluster index 若没有 diagram，会不满足 Mermaid 要求。 | 8 个 cluster index 全部加入 Mermaid，master 也加入 Mermaid。 | fixed_inline |
| 3 | linked_rules 可能被误称已验证。 | 当前容器检查不存在 ~/.claude/rules/*，在 README/stdout/rules index 中标注 false。 | bounded |
| 4 | ContentFlow L 本地 retrospective 不可读。 | 只使用 prompt-stated lessons，不伪造 1749 行具体内容。 | bounded |
| 5 | GitHub external audit 2026-05-07 fetch/search 未命中。 | 使用上传审计包与本地 source excerpts，并在 limitations 写明。 | bounded |
| 6 | Capture runbook 可能暗示 XHS/YouTube runtime 可用。 | RB-CAP-02/03 明确只读 triage / planning，不创建 runtime capture。 | fixed_inline |
| 7 | BBDown/ASR tooling runbook 可能被误解为安装/运行许可。 | RB-CAP-07/08、RB-TOL-01 明确 no runtime / no install / overflow。 | fixed_inline |
| 8 | Quick capture 可能被扩大成 batch list。 | RB-CAP-04/10 强制 batch gate 与 quick-vs-gated decision tree。 | fixed_inline |
| 9 | Dispatch lane=5 容易被当全局默认。 | 所有 dispatch runbook 写明 lane=5 仅 Dispatch127-176 scoped，全局 3+1。 | fixed_inline |
| 10 | Review lane 可能写 authority。 | RB-DSP-02/03/04/09 写明 review/research 默认 read-only。 | fixed_inline |
| 11 | silent flexibility 正面化后可能鼓励越界。 | RB-DSP-07/08 将 detect/recover 分离，要求 amendment/readback。 | fixed_inline |
| 12 | Boundary scan 若只靠 grep 会漏语义批准。 | RB-BND-09 增加 semantic wording review 与 human approval。 | fixed_inline |
| 13 | write_enabled scan 可能找错 config.py 行号。 | 不硬编码当前不可见行号，只写 bridge/vault true-write scan 与 files noted in source。 | bounded |
| 14 | can_open 三 flag 来源未在源包出现。 | RB-BND-07 以 gate separation SOP 表达，不声称源包已有字段。 | bounded |
| 15 | Legal posture 需最新网页但 web 不可用。 | RB-BND-06/RB-CAP-07 写明离线环境不能给最新合规结论。 | bounded |
| 16 | Visual runbook 可能声称 5 Gate 已过。 | RB-VIS-04 明确 current.md 无 screenshot / Playwright / human final evidence。 | fixed_inline |
| 17 | OpenDesign/shadcn donor 边界容易被混用。 | Visual runbook 写明 L3 mood donor，不是 code/package/IA/layout donor。 | fixed_inline |
| 18 | Storybook/browser launch 可能触发 browser automation。 | RB-VIS-09 明确需要另开 gate，static harness 不是 execution proof。 | fixed_inline |
| 19 | Memory runbook 可能过度依赖聊天总结。 | RB-MEM-02 要求先读 authority/readback，不只读摘要。 | fixed_inline |
| 20 | Handoff 创建可能太长。 | RB-MEM-01 保留 ≤80 行约束与 Step 5 next-session prompt。 | fixed_inline |
| 21 | RAW handoff 可能把 preview 当 knowledge success。 | RB-EGR-02/07 明确 preview != RAW intake != knowledge success。 | fixed_inline |
| 22 | DiloFlow/Obsidian export 可能传播敏感信息。 | RB-EGR-01/03/06 设 egress redaction proof。 | fixed_inline |
| 23 | Tooling runbook 可能偷偷变成安装指南。 | Tooling cluster 全部使用 preflight/verify 候选语言，不给执行结论。 | fixed_inline |
| 24 | sqlite-vec 可能暗示 DB migration。 | RB-TOL-04 明确 DB vNext/migration gate blocked。 | fixed_inline |
| 25 | Recovery runbook 可能用 mirror 覆盖 SoR。 | RB-REC-01 明确 RAW SoR 优先，ScoutFlow preview 不反写 RAW truth。 | fixed_inline |
| 26 | SQLite 恢复若建议手工编辑 DB 风险过高。 | RB-REC-02 明确停止 worker、备份损坏文件、integrity_check 与备份恢复。 | fixed_inline |
| 27 | Git branch 恢复可能丢 PR lineage。 | RB-REC-05 使用 commit SHA/PR head/reflog。 | fixed_inline |
| 28 | Token over-budget 可能继续做 authority edit。 | RB-REC-06 与 Memory cluster 要求红线后暂停高风险动作。 | fixed_inline |
| 29 | file count 可能因 index 命名混入 runbook 统计。 | stdout 分开 files_count、RB-*.md count、runbooks_count_total。 | fixed_inline |
| 30 | word count 可能被英文 token 与中文字符混算。 | validator 使用 CJK chars + Latin tokens 的 approximate count，并如实标为 approx。 | fixed_inline |
| 31 | claim label coverage 可能不足。 | 正文段落全部以 bracket claim label 开头，支持文件也采用标签段落。 | fixed_inline |
| 32 | frontmatter trigger_keywords[] 可能不是 YAML 数组。 | 每个文件都用多行 list 形式。 | fixed_inline |
| 33 | runbook footer 可能忘记 no actual execution。 | 每个 runbook footer 写明 not approval。 | fixed_inline |
| 34 | supporting files 缺 risk_level 可能影响格式 guard。 | supporting/index/master 也带 risk_level 与 trigger_keywords。 | fixed_inline |
| 35 | truthful stdout 容易伪造 150 thinking minutes。 | README/stdout 不伪造；写 current-session measured/未外部计时 limitation。 | bounded |
| 36 | 最终 ZIP 可能含生成脚本或源包。 | ZIP 只打包输出目录，不包含 source zip 与 generator。 | fixed_inline |

[self-audit result] 共记录 36 条 findings；其中 fixed_inline 与 bounded 都已在 runbook、index、supporting 或 stdout 中体现。bounded 不表示解决，只表示当前环境不可验证或不应伪造。

[boundary result] 未发现 runbook 声称 runtime approved、migration approved、ASR approved、browser automation approved 或 vault true write approved。生成后 validator 还会扫描高危短语。

## Self-audit closure appendix

[audit closure] 本文件把问题分成 fixed-inline、bounded-by-limitation、requires-user-audit 三类。fixed-inline 表示文本已修改；bounded-by-limitation 表示当前环境无法验证但已如实声明；requires-user-audit 表示必须由用户在真实 ScoutFlow repo 或本地规则目录中确认。

[audit priority] 用户复核时建议先看三类高风险：runtime unlock wording、authority write wording、legal/secret/PII wording。只要发现“可执行”被写成“已批准”，即使格式检查通过，也应把对应 runbook 标为 needs_revision。

[audit evidence] 本次交付的自检不能替代你的真实仓库 CI、pre-commit、GitHub PR review 或 Claude/Codex/Hermes 外审；它只是把候选库整理到可审计状态。
