---
name: dual-truth-separation
description: ZIP truth / GitHub live truth / RAW truth 三层分离; 现状以 GitHub live 为准
type: project
source_atlas_node: P-DUAL-TRUTH-SEPARATION
cross_vendor_readers: [cc0, cc1, codex, gpt-pro, hermes]
status: current authority
---

# Triple truth separation

ScoutFlow 跨 vendor 协作场景 3 层 truth 必须分离: (1) **ZIP truth** = 上传 storage 包 (16 ZIP 等), 时点冻结 (2) **GitHub live truth** = `git fetch origin/main` 当前 HEAD, 真现状 (3) **RAW truth** = 用户本地 raw vault 内容. 三者**不互相覆盖**, 不混读.

**Why:** ScoutFlow `~/.claude/projects/.../memory/feedback_pre_diagnose_git_fetch.md` 已锁 "诊断前必须 git fetch". 历史多次出现 ZIP storage 旧 current.md 被当现状 (而 main 已超前). 跨 vendor (cloud GPT Pro / Codex CLI / Claude Code) 各自 access 不同 truth source, 必须显式声明.

**How to apply:** 任何"现状判断"前 git fetch + 看 origin/main HEAD. 引用 storage ZIP 内 file 显式标 "[ZIP truth, time-frozen 2026-XX-XX]". 引用 RAW vault 内容显式标 "[RAW truth, 用户本地]". 跨 vendor paste 内容前明确 source layer.
