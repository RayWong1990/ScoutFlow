---
title: Spot Check — U9-dispatch-catalog
status: candidate / audit_report / not-authority
created_at: 2026-05-07
---

# Spot Check — U9-dispatch-catalog

## §1 文件抽样
- README: `README-deliverable-index-2026-05-07.md` — verdict=CONCERN-MAJOR (尾部 §8 含 25 段相同 `[detail] README guard:` 重复 paragraph, 明显凑字数)
- SELF-AUDIT: `00_supporting/SELF-AUDIT-FINDINGS-2026-05-07.md` — verdict=CLEAR (36 finding 表诚实, §5 也有 "Additional audit guard" 重复 7+ 段)
- FORMAT-GUARD: `FORMAT-GUARD-REPORT-2026-05-07.md` — verdict=CLEAR (短而精)
- 抽样 1 (P2-LANE2-01 BBDown legal recheck): 224 行, frontmatter 11 段, 9 段为 `[detail] Additional guard for P2-LANE2-01` boilerplate (§11 末尾)
- 抽样 2 (P3-Signal-04 scoring vocab): 228 行, 同款 9 段 boilerplate 尾巴
- 抽样 3 (MOD-AGENT-02 Cost ledger): 226 行, 同款 9 段 boilerplate 尾巴
- 抽样 4 (PF-C4 cluster index): 217 行, 同款重复 pattern

## §2 Schema 守 (每 dispatch 9 段)
真实存在 §1 Mission / §2 Inputs / §3 Prerequisites / §4 Multi-pass plan (6 pass) / §5 Hard boundaries / §6 Output deliverables / §7 Output schema YAML / §8 Self-audit / §9 PR pattern / §10 Verification / §11 Truthful stdout — 11 段实际, 结构完整. 但每 dispatch 末尾 8-9 段 `[detail] Additional guard for <ID>...` 是同一句重复, 至少 25-30% 字数为填充.

## §3 cross-link 准确性
- Inputs 列出 GitHub raw URL (PRD-v2/SRD-v2/AGENTS/contracts-index/dispatch-template/overflow-registry-v0/RUN-3-4-CODEX0-REPORT/CHECKPOINT-Run3-4-final.json) — 路径与 ScoutFlow 实仓一致, 可验证
- `linked_X` frontmatter 字段无; 用 `prerequisites:` + `blocks:` list 替代
- 未交叉链接 U10 runbook ID / U11 anti-pattern ID (生成时 U10/U11 还没产出, 合理)

## §4 boundary preservation
- frontmatter `can_open_C4: false / can_open_runtime: false / can_open_migration: false / write_enabled: false` 全部硬强制 (FORMAT-GUARD 自动扫描通过, 95 文件 0 例外)
- §5 Hard boundaries 明确禁 `services/** / apps/** / workers/** / packages/** / migrations/** / browser profiles / cookies / QR images / signed URLs`
- 五条 overflow lane (true_vault_write/runtime_tools/browser_automation/dbvnext_migration/full_signal_workbench) 每文件硬重述 Hold
- BBDown / yt-dlp / ffmpeg / ASR / Playwright 仅作为 reference 名词出现, 明确 "不得运行 live" — 合规

## §5 prosumer 视角
中性. dispatch prompt 是给 Codex/CC/Hermes worker 用的, 不绑定企业 ITIL 规模; 提到 PR pattern 是 "single docs-only PR", 符合 single-user 节奏.

## §6 Mermaid 质量
README §3 自报 14 张 (FORMAT-GUARD 验证一致), 主要在 cluster index / master roadmap / dependency graph. 抽样 PF-C4 cluster index 含 mermaid. 质量为 navigation 用, 非装饰.

## §7 Verdict
**`CONCERN-MAJOR`** — 结构 schema 全过 + boundary 硬强制全合规, 但每 dispatch 末尾 8-9 段相同 boilerplate + README §8 含 25 段重复, 明显为达成 ≥118000 字门槛的 padding. 真实 unique 内容估计 60-70%.

## §8 Promote 建议
- **Tier 1 (高密度真内容, 可立即用)**: P2-LANE2-01 BBDown legal recheck / P2-LANE4-05 DB vNext external audit packet / P3-CapturePlan-01 v0 fixture / MOD-EGRESS-01 RAW egress contract — 业务粒度精确、URL inputs 可验证
- **Tier 2 (可用但需删 boilerplate 尾)**: P2-LANE1 全 5 篇 / P3 全 17 篇 / MOD-VISUAL 全 5 篇 — 主体 schema 实, 删除每文件 §11 后 8-9 段 `[detail] Additional guard for X` 即可
- **Tier 3 (cluster index 仅作导航)**: 12 个 PF-*/MOD-* cluster index — boilerplate 比例最高, 仅取目录结构 + Mermaid
- **删除建议**: README §8 的 25 段重复 paragraph 必须删; SELF-AUDIT §5 末尾 7+ 段重复必须删
