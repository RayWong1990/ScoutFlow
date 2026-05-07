---
title: LINKED DISPATCH CATALOG — U10 Candidate Mapping
status: candidate
authority: not-authority
created_at: 2026-05-07
runbook_id: LINKED-DISPATCH-CATALOG
cluster: Supporting
trigger_keywords:
  - linked dispatch
  - U9 catalog
  - dispatch mapping
risk_level: medium
single_user_applicable: true
multi_agent_applicable: true
linked_dispatch:
  - MOD-LINKED-DISPATCH-CATALOG
linked_rule:
  - ~/.claude/rules/parallel-safety.md
  - ~/.claude/rules/execution-discipline.md
boundary_statement: candidate mapping; U9 source catalog not present in current environment.
---

# LINKED DISPATCH CATALOG

[environment limitation] U10 prompt 要求 linked_dispatch 对齐 U9 catalog，但当前上传材料中没有独立 U9 catalog 文件；GitHub connector search 也未返回 2026-05-07 strategic-upgrade/U10 命中。因此本文件给出 P2-/P3-/P4-/MOD- 形式的 candidate dispatch IDs，并在 stdout 标注 linked_dispatch_validated=false。

| Candidate dispatch ID | Cluster | Meaning | Validation status |
|---|---|---|---|
| `P2-CAP-CAP-METADATA-ONLY` | Capture / Acquisition | linked from RB-CAP-01 / Single Bilibili URL metadata-only capture（Phase 1A 窄门） | candidate, not U9-validated |
| `P2-CAP-CAP-XHS-TRIAGE` | Capture / Acquisition | linked from RB-CAP-02 / Single XHS URL capture（只读 triage，不创建 runtime capture） | candidate, not U9-validated |
| `P4-BND-HARD-REDLINES` | Capture / Acquisition | linked from RB-CAP-02 / Single XHS URL capture（只读 triage，不创建 runtime capture） | candidate, not U9-validated |
| `P2-CAP-CAP-YOUTUBE-PLAN` | Capture / Acquisition | linked from RB-CAP-03 / Single YouTube URL capture（later 平台规划，不执行 runtime） | candidate, not U9-validated |
| `P2-CAP-CAP-BATCH-GATE` | Capture / Acquisition | linked from RB-CAP-04 / Batch URL ingestion（Phase 2 gate before batch） | candidate, not U9-validated |
| `P3-DSP-LANE-GUARD` | Capture / Acquisition | linked from RB-CAP-04 / Batch URL ingestion（Phase 2 gate before batch） | candidate, not U9-validated |
| `P2-CAP-CAP-RETRY-ROLLBACK` | Capture / Acquisition | linked from RB-CAP-05 / Failed capture retry + rollback（失败采集重试与证据回滚） | candidate, not U9-validated |
| `P2-CAP-CAP-WEAK-NET` | Capture / Acquisition | linked from RB-CAP-06 / 网络降级 / 弱网 capture（degraded metadata path） | candidate, not U9-validated |
| `P2-CAP-CAP-BBDOWN-LEGAL` | Capture / Acquisition | linked from RB-CAP-07 / BBDown legal posture recheck before run（工具姿态复核） | candidate, not U9-validated |
| `P2-CAP-CAP-ASR-INSTALL-CHECK` | Capture / Acquisition | linked from RB-CAP-08 / ASR local install verify（Whisper / Parakeet / Voxtral 候选检查，不安装） | candidate, not U9-validated |
| `P2-CAP-CAP-SCOPE-GATE` | Capture / Acquisition | linked from RB-CAP-09 / Capture scope gate enforce（LP-001 推荐/关键词/RAW gap 不直接 capture） | candidate, not U9-validated |
| `P2-CAP-CAP-QUICK-VS-GATE` | Capture / Acquisition | linked from RB-CAP-10 / Quick capture vs scope-gated capture（快速采集与门控采集选择） | candidate, not U9-validated |
| `P3-DSP-DSP-CODEX-SINGLE` | Dispatch / Multi-Agent | linked from RB-DSP-01 / Single dispatch 派给 Codex（主写入 / PR owner） | candidate, not U9-validated |
| `P3-DSP-DSP-CC1-REVIEW` | Dispatch / Multi-Agent | linked from RB-DSP-02 / Single dispatch 派给 CC1（review / IA / contract lane） | candidate, not U9-validated |
| `P3-DSP-DSP-HERMES-RESEARCH` | Dispatch / Multi-Agent | linked from RB-DSP-03 / Single dispatch 派给 Hermes（research / rebuttal / external critique） | candidate, not U9-validated |
| `P3-DSP-DSP-PARALLEL-WORKTREE` | Dispatch / Multi-Agent | linked from RB-DSP-04 / Parallel multi-window dispatch（3-5 worktree 编排） | candidate, not U9-validated |
| `P3-DSP-DSP-AMEND-PROCEED` | Dispatch / Multi-Agent | linked from RB-DSP-05 / amend_and_proceed pattern（先修提示/包再继续） | candidate, not U9-validated |
| `P3-DSP-DSP-THREE-WINDOW-AUDIT` | Dispatch / Multi-Agent | linked from RB-DSP-06 / 3-window cloud audit（Codex / GPT Pro / Hermes 三方外审） | candidate, not U9-validated |
| `P3-DSP-DSP-SILENT-DETECT` | Dispatch / Multi-Agent | linked from RB-DSP-07 / silent flexibility detect（模型静默灵活性识别） | candidate, not U9-validated |
| `P3-DSP-DSP-SILENT-RECOVER` | Dispatch / Multi-Agent | linked from RB-DSP-08 / silent flexibility recover（PR226-228 类修复/收束） | candidate, not U9-validated |
| `P3-DSP-DSP-SINGLE-WRITER` | Dispatch / Multi-Agent | linked from RB-DSP-09 / single-writer enforce（LP-006 authority writer guard） | candidate, not U9-validated |
| `P3-DSP-DSP-LEDGER-RECORD` | Dispatch / Multi-Agent | linked from RB-DSP-10 / dispatch ledger record（与 U5 ledger 联动） | candidate, not U9-validated |
| `P3-DSP-DSP-COST-ATTRIBUTION` | Dispatch / Multi-Agent | linked from RB-DSP-11 / cost attribution record（费用/模型/窗口归因） | candidate, not U9-validated |
| `P3-DSP-DSP-PR-PACKING` | Dispatch / Multi-Agent | linked from RB-DSP-12 / packed PR vs per-dispatch PR 决策 | candidate, not U9-validated |
| `P4-BND-BND-WRITE-ENABLED` | Boundary / Audit | linked from RB-BND-01 / write_enabled scan（bridge/vault true-write 扫描） | candidate, not U9-validated |
| `P4-BND-BND-OVERFLOW-HOLD` | Boundary / Audit | linked from RB-BND-02 / 5 overflow lane Hold scan（DB/runtime/ASR/browser/migration） | candidate, not U9-validated |
| `P4-BND-BND-AUTHORITY-SCAN` | Boundary / Audit | linked from RB-BND-03 / Authority files scan（current/task-index/decision-log/AGENTS） | candidate, not U9-validated |
| `P4-BND-BND-SECRET-SCAN` | Boundary / Audit | linked from RB-BND-04 / Credential / secret scan（strict pattern + exclude rule） | candidate, not U9-validated |
| `P4-BND-BND-PII-REDACTION` | Boundary / Audit | linked from RB-BND-05 / PII redaction scan（regex + word boundary） | candidate, not U9-validated |
| `P4-BND-BND-LEGAL-RECHECK` | Boundary / Audit | linked from RB-BND-06 / Legal posture recheck（Bilibili C&D / yt-dlp / scrapers） | candidate, not U9-validated |
| `P4-BND-BND-CAN-OPEN-FLAGS` | Boundary / Audit | linked from RB-BND-07 / can_open_C4 / can_open_runtime / can_open_migration 三 flag verify | candidate, not U9-validated |
| `P4-BND-BND-POST-MERGE` | Boundary / Audit | linked from RB-BND-08 / Post-merge integrity check（origin/main SHA / authority untouched / hard redlines） | candidate, not U9-validated |
| `P4-BND-BND-AUTO-SCAN` | Boundary / Audit | linked from RB-BND-09 / Boundary scan automation（CI / pre-commit hook） | candidate, not U9-validated |
| `P4-BND-BND-FRONTMATTER` | Boundary / Audit | linked from RB-BND-10 / Frontmatter status validator（candidate / not-authority） | candidate, not U9-validated |
| `P3-VIS-VIS-IMAGE-BATCH` | Visual Production | linked from RB-VIS-01 / GPT-Image-2 batch generation（云端 ZIP 工作流） | candidate, not U9-validated |
| `P3-VIS-VIS-PATTERN-LOOP` | Visual Production | linked from RB-VIS-02 / Pattern A-J refinement loop（视觉模式十案迭代） | candidate, not U9-validated |
| `P3-VIS-VIS-IMAGE-TO-TSX` | Visual Production | linked from RB-VIS-03 / Image → React TSX（PF-V handoff） | candidate, not U9-validated |
| `P3-VIS-VIS-FIVE-GATE` | Visual Production | linked from RB-VIS-04 / 5-Gate self-audit（3 自动 + 2 human-in-loop） | candidate, not U9-validated |
| `P3-VIS-VIS-TOKEN-CASCADE` | Visual Production | linked from RB-VIS-05 / Design token cascade rebuild（token 层级重建） | candidate, not U9-validated |
| `P3-VIS-VIS-STATE-LIBRARY` | Visual Production | linked from RB-VIS-06 / State library register（8 panel × 6 state） | candidate, not U9-validated |
| `P3-VIS-VIS-PHASH-DEDUP` | Visual Production | linked from RB-VIS-07 / Visual asset perceptual hash dedup（视觉资产去重） | candidate, not U9-validated |
| `P3-VIS-VIS-WCAG-CONTRAST` | Visual Production | linked from RB-VIS-08 / WCAG 2.2 contrast ≥4.5:1 audit（可读性门） | candidate, not U9-validated |
| `P3-VIS-VIS-STORYBOOK-LAUNCH` | Visual Production | linked from RB-VIS-09 / Storybook-style browser launch（本地预览门控） | candidate, not U9-validated |
| `P3-VIS-VIS-ASSET-REUSE` | Visual Production | linked from RB-VIS-10 / Visual asset cross-phase reuse query（跨阶段素材复用查询） | candidate, not U9-validated |
| `MOD-MEM-MEM-HANDOFF-CREATE` | Memory / Cross-Session | linked from RB-MEM-01 / Handoff 创建（≤80 行 + Step 5 next-session prompt） | candidate, not U9-validated |
| `MOD-MEM-MEM-HANDOFF-READ` | Memory / Cross-Session | linked from RB-MEM-02 / Handoff 阅读（next session 起手） | candidate, not U9-validated |
| `MOD-MEM-MEM-CLEAR-DECISION` | Memory / Cross-Session | linked from RB-MEM-03 / /clear 时机决策（60% 黄 / 85% 红） | candidate, not U9-validated |
| `MOD-MEM-MEM-COMPACT-FOCUS` | Memory / Cross-Session | linked from RB-MEM-04 / /compact 操作 + focus arg（压缩而不丢边界） | candidate, not U9-validated |
| `MOD-MEM-MEM-MEMORY-MAINTAIN` | Memory / Cross-Session | linked from RB-MEM-05 / MEMORY.md 维护（200 行限制 / 归档过时） | candidate, not U9-validated |
| `MOD-MEM-MEM-CROSS-SESSION-PROMPT` | Memory / Cross-Session | linked from RB-MEM-06 / 跨 session prompt 输出（沉淀六步 Step 5） | candidate, not U9-validated |
| `MOD-MEM-MEM-PRECOMPACT-RECOVER` | Memory / Cross-Session | linked from RB-MEM-07 / PreCompact 兜底 + SessionStart(compact) 恢复 | candidate, not U9-validated |
| `P3-EGR-EGR-DILOFLOW-HANDOFF` | Egress / Downstream | linked from RB-EGR-01 / DiloFlow handoff（manifest publish） | candidate, not U9-validated |
| `P3-EGR-EGR-RAW-STAGING` | Egress / Downstream | linked from RB-EGR-02 / RAW vault staging（永不直写） | candidate, not U9-validated |
| `P3-EGR-EGR-OBSIDIAN-EXPORT` | Egress / Downstream | linked from RB-EGR-03 / Obsidian export（properties / highlights / note candidate） | candidate, not U9-validated |
| `P3-EGR-EGR-HERMES-INTEGRATION` | Egress / Downstream | linked from RB-EGR-04 / hermes-agent integration（research lane handoff） | candidate, not U9-validated |
| `P3-EGR-EGR-SUPERSEDE` | Egress / Downstream | linked from RB-EGR-05 / Supersede protocol（旧版本 deprecated） | candidate, not U9-validated |
| `P3-EGR-EGR-REDACTION-ENFORCE` | Egress / Downstream | linked from RB-EGR-06 / Redaction enforce（PII / 凭据 / 法律敏感） | candidate, not U9-validated |
| `P3-EGR-EGR-MANIFEST-SCHEMA` | Egress / Downstream | linked from RB-EGR-07 / Cross-system manifest schema validate（跨系统 manifest 验证） | candidate, not U9-validated |
| `MOD-TOL-TOL-WHISPER-PREFLIGHT` | Tooling | linked from RB-TOL-01 / Whisper local preflight（ASR 工具候选，不启用 audio_transcript） | candidate, not U9-validated |
| `MOD-TOL-TOL-BGE-M3-PREFLIGHT` | Tooling | linked from RB-TOL-02 / bge-m3 embedding preflight（向量化候选） | candidate, not U9-validated |
| `MOD-TOL-TOL-OLLAMA-VERIFY` | Tooling | linked from RB-TOL-03 / ollama local model verify（本地模型工具门控） | candidate, not U9-validated |
| `MOD-TOL-TOL-SQLITE-VEC-PREFLIGHT` | Tooling | linked from RB-TOL-04 / sqlite-vec preflight（SQLite vector extension 候选） | candidate, not U9-validated |
| `MOD-TOL-TOL-MLX-VERIFY` | Tooling | linked from RB-TOL-05 / mlx local acceleration verify（Apple Silicon 推理候选） | candidate, not U9-validated |
| `MOD-TOL-TOL-CC-RESILIENT` | Tooling | linked from RB-TOL-06 / cc-resilient.sh wrapper（Claude/Codex resiliency 脚本候选） | candidate, not U9-validated |
| `MOD-REC-REC-RAW-WIPED` | Recovery | linked from RB-REC-01 / ~/workspace/raw wiped（RAW 工作区误删恢复） | candidate, not U9-validated |
| `MOD-REC-REC-SQLITE-CORRUPT` | Recovery | linked from RB-REC-02 / SQLite corrupt（SQLite authority 损坏恢复） | candidate, not U9-validated |
| `MOD-REC-REC-GIT-DELETE` | Recovery | linked from RB-REC-03 / git 误删（tracked file deletion recovery） | candidate, not U9-validated |
| `MOD-REC-REC-WORKTREE-OCCUPIED` | Recovery | linked from RB-REC-04 / worktree 占用 / 冲突恢复（parallel lane unblock） | candidate, not U9-validated |
| `MOD-REC-REC-BRANCH-DELETED` | Recovery | linked from RB-REC-05 / branch 误删（remote/local branch recovery） | candidate, not U9-validated |
| `MOD-REC-REC-TOKEN-OVER-BUDGET` | Recovery | linked from RB-REC-06 / token over budget（上下文超预算恢复） | candidate, not U9-validated |

[catalog rule] P2 前缀用于 capture/product proof candidate；P3 用于 dispatch/visual/egress lane coordination；P4 用于 boundary/audit/hard redline；MOD 用于 memory/tooling/recovery/supporting operational modules。此前缀语义是本库内 candidate mapping，不等同外部 U9 authority。

## Dispatch catalog appendix

[catalog rule] dispatch ID 采用 `P2-`、`P3-`、`P4-`、`MOD-` 前缀，以便和 U9 类 catalog 对齐；但 U9 原始 catalog 在当前容器不可见，所以本目录只声明候选映射。用户审计时应把这些 ID 与真实 U9 dispatch ledger 做 diff。

[catalog use] 一个 runbook 可以链接多个 dispatch，但 dispatch 不能自动继承 runbook 的 scope。实际派发时仍需在 dispatch template 中写 allowed_paths、forbidden_paths、validation command、rollback plan、owner、agent、worktree。

[catalog repair] 如果发现 dispatch ID 与真实 ledger 冲突，先改 catalog，再改 runbook frontmatter，最后在 SELF-AUDIT-FINDINGS 追加 supersede note；不要让两个 ID 同时有效。
