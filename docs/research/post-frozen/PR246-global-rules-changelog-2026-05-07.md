---
title: PR #246 Global Rules Changelog (~/.claude/ 改动 audit trail)
status: reference storage
created_at: 2026-05-07
target_pr: 246
parent_branch: chore/pr246-governance-harness-integration
purpose: |
  PR #246 commit message 显式声明 "全局改动 (~/.claude/, 不在 PR diff 但已生效)".
  本 file 是这部分改动的 audit trail manifest, 让 PR review 时 ~/.claude/ 改动可见.
  不替代 git tracked, 仅 mitigate Layer 2 audit H-1 finding (cross-vendor 不可见 + drift 风险).
mitigation_for: H-1 (~/.claude/ 全局改动 in commit message but not in PR diff)
long_term_solution: W6K — ~/.claude/rules/* + ~/.claude/projects/.../memory/* 镜像到 ScoutFlow git tracked (docs/global-rules/ + docs/memory/) 实现跨 vendor 真共享
---

# PR #246 Global Rules Changelog

> **Audit trail mitigation** for PR #246 commit `20d18e6` + `9bf2251` 中声明的 "~/.claude/ 全局改动". 这部分改动**不在 PR diff** (本机本 path), 但 commit message 已显式列, 本 file 进一步细化为 manifest 形式. **不替代 git tracked source-of-truth** — long term 解法是 W6K 镜像到 git tracked.

---

## §1 改动 file 清单 (3 file)

### 1.1 `~/.claude/rules/codex-metacognition-learnings.md`

**改动段**: §3 自检清单

**改前**: 8 条 instinct (§1.1-§1.8 对应)

**改后**: 19 条 (8 原 + 11 新增 #9-#19)

**新增 11 条 instinct (摘要)**:

| # | 主题 | 触发场景 |
|---|---|---|
| 9 | `find -type f` 校验 file count | 任何"~N file"估值前必加 -type f, ≥3 位数 wc -l 二次校验 |
| 10 | candidate vs authority | grep frontmatter `status:` + 核 PR merge 状态. `-candidate-` 后缀不是 authority |
| 11 | 24h actionable consumer | 资源分配前必问 "每窗 / 每 agent 24h 内是否有 actionable consumer"; 没 consumer 的 spec 是 over-engineering |
| 12 | read-heavy vs judgment-heavy | 派 agent 前先问. read-heavy 适合 Codex 并行, judgment-heavy 适合 Opus 单跑 |
| 13 | master spec § 13/15.2/16 必扫 | 任何调研 / 推荐 / 派单 prompt 前必扫. ScoutFlow 治理状态机 single source of truth |
| 14 | 16 ZIP / U 系列 vs § 9.x | 12/16 U 跟 § 9.x 1:1 映射, § 9 给消费路线 |
| 15 | ScoutFlow ad-hoc 工作文件路径 | 必须 raw PARA (`~/workspace/raw/05-Projects/<Project>/dispatches/`), 不是 git tracked. CC0 + CC1 同 session 双失忆教训 |
| 16 | Anthropic Opus self-audit 不替代 Layer 2 | 同 vendor / 同 model family bias. PR #244 4 High + PR #245 1 High + 3 Medium 实证 |
| 17 | PR # 验证 | 引"PR #N merged"前必 grep + 核 commit SHA |
| 18 | handoff ≤ 15 行 | 跨 session 决策落地 handoff template, ≤ 15 行 (frontmatter 不含). 长 narrative 跨 session 复利价值低 |
| 19 | default 推荐标 ⭐ | 多选项推荐时 default ⭐ 显式标记, 减少战友决策疲劳 |

**Source commit**: `20d18e6` (#9-#15) + `9bf2251` (#16-#19)

### 1.2 `~/.claude/projects/-Users-wanglei-workspace-ScoutFlow/memory/project_4_agent_division_v3.md`

**改动段**: 新增 §8 双 Opus 互审常态化 SOP

**新增内容摘要**:
- CC1 ↔ CC0 双 Opus 实证 catch 4+ 错 (PR #244 4 High + PR #245 1 High + 3 Medium 全是 CC0/CC1 self-audit 漏 / Layer 2 catch)
- 战友 paste 流程: **战友 → CC1 v1 → CC0 critical review → CC1 v2 → 战友拍 → 执行**
- ⚠️ same-family bias 警示: 双 Opus 仍同 vendor, 真正 cross-vendor strong gate 需 Codex / GPT Pro / Hermes 一轮 audit
- Hermes 降级 candidate role (建议性, 不阻 Codex 启动)

**Source commit**: `20d18e6` + `9bf2251`

### 1.3 `~/.claude/projects/-Users-wanglei-workspace-ScoutFlow/memory/MEMORY.md`

**改动**: 新增 3 pointer

| pointer | 指向 | 含义 |
|---|---|---|
| 1 | `codex-metacognition-learnings.md §3 (19 条)` | instinct 升级 entry |
| 2 | `project_4_agent_division_v3.md §8` | 双 Opus 互审 SOP |
| 3 | `docs/research/post-frozen/handoff-template.md` (git tracked) | handoff 跨 session 落地模板 (instinct §3 #18 配套) |

**Source commit**: `20d18e6`

---

## §2 风险声明 (H-1 mitigation 性质)

本 manifest 是 audit trail, **不是真源**. PR review 时仍**无法**看到 ~/.claude/ 实际 diff (本机 path, 不进 git diff). 所以:

| 风险 | 当前 mitigation | Long-term 解 |
|---|---|---|
| 跨 vendor 不可见 (Codex / GPT Pro 云端 / Hermes 看不到 ~/.claude/) | 本 manifest + commit message 文字描述 | W6K 镜像到 `docs/global-rules/` git tracked, 类似 `docs/memory/` 跨 vendor land 模式 (PR #245 同源问题) |
| Drift 风险 (~/.claude/ 实际改动跟 manifest 不同步) | 本批 manifest 由 CC1 在改动 commit 同 session 写, 时间一致 | W6K 镜像 + git pre-commit hook check ~/.claude/ checksum vs manifest |
| Audit trail 不可 grep 实际 instinct 内容 | 本 manifest 列摘要, 跨 session agent 仍需直接 Read ~/.claude/ 看具体 | W6K 镜像后实际 instinct 内容 git tracked, 任何 vendor grep 可达 |

---

## §3 W6K 长期议程 (跨 vendor instinct 真镜像)

PR #245 (docs/memory/) + PR #246 (docs/global-rules/ — 待) 是同源问题的两个相位:

- **PR #245** 已修: 项目 instinct memory cross-vendor land (docs/memory/ 17 file, lesson + feedback + pattern)
- **PR #246 (本)** 部分修: governance harness + handoff template + 元认知 instinct 升级到 ~/.claude/ (本机) — **未跨 vendor 镜像**
- **W6K (待)**: ~/.claude/rules/* + ~/.claude/projects/.../memory/* 全镜像到 ScoutFlow `docs/global-rules/` 目录, 跨 vendor 完整可读

W6K 候选 PR 范围:
1. 新建 `docs/global-rules/` 目录, mirror ~/.claude/rules/* (codex-metacognition / coding-style / token-hygiene / aesthetic-first / session-closure / parallel-safety / claude-code-tips 等)
2. 新建 `docs/agent-memory/` 目录, mirror ~/.claude/projects/.../memory/* 19 条
3. tools/sync-global-rules.py — 双向 sync + checksum + drift detection
4. CI integration (类似 refresh-start-here.py --check)

---

## §4 关联

- PR #246 主线: https://github.com/RayWong1990/ScoutFlow/pull/246
- PR #245 同源问题修 (docs/memory/ 跨 vendor land): https://github.com/RayWong1990/ScoutFlow/pull/245
- master spec §13.1 W6K wave: `docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md`
- CC1 retrospective §6.2 "战友是唯一 context bridge": `docs/research/post-frozen/CC1-session-retrospective-2026-05-07.md`
- Layer 2 audit verdict (本 PR audit trail): CONCERN with H-1 mitigated by 本 file

---

> **本 file by CC0 (Anthropic Opus 4.7), 2026-05-07.** Audit trail mitigation, 不替代 W6K long-term 镜像方案. 进 main 后 future agent grep "PR #246 global rules" 能找到这份 manifest, 知道 ~/.claude/ 改了什么但需 long-term W6K 才真跨 vendor 共享.
