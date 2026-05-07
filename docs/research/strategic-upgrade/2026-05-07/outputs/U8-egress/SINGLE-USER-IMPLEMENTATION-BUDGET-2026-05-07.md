---
title: SINGLE-USER IMPLEMENTATION BUDGET — U8 Egress
status: candidate / implementation-budget / not-authority
authority: not-authority
claim_label: "95%"
created_at: 2026-05-07
generated_in_environment: 2026-05-06
single_user_budget_loc: 360
single_user_budget_dev_days: 4
write_enabled: false
---

# SINGLE-USER IMPLEMENTATION BUDGET — U8 Egress

## 0. 证据与边界口径

本交付只声明 ScoutFlow 单方面写出的文件级 egress contract，不定义 SDK、OpenAPI client、双向同步 broker，也不修改任何下游。PRD v2 的最高边界是：ScoutFlow 是单 user、local-first 的采集与证据工作台；RAW、Obsidian、DiloFlow 是下游消费者，不是 ScoutFlow 项目的一部分。SRD v2 的最高边界是：当前生效的是 metadata-only、receipt、trust trace、redaction/secret scan baseline；Phase 2+ 对象仍主要是 outline，不能被文件导出契约误读成 runtime unlock。

本环境已经读取上传的 post176 audit pack 与 GitHub 上的 PRD/SRD、Run-3+4 C2 文件。普通 live web 浏览在当前会话被禁用，所以本文所有外部 vendor/frontmatter 口径只作为“需刷新验证的公共模式候选”，不标记为 live verified。`~/workspace/DiloFlow/`、`~/workspace/raw/`、`~/workspace/hermes-agent/` 与 Obsidian 本地 vault 在当前容器没有出现；因此 DiloFlow 与 hermes-agent 的 receiver-side parser 只能给出单方、保守、低耦合的文件契约，不能声称已经被下游 repo 实测接受。

硬边界在所有下游一致：`write_enabled=false` 保持；ScoutFlow 永不直写 `~/workspace/raw/`；凭据、cookie、token、QR 图片、browser profile path、auth sidecar、raw stdout/stderr 中可能含秘密的片段不得进入 egress；Bilibili/XHS 等平台原作者隐私字段只允许最小必要、脱敏后的事实摘要；manifest 是一次 handoff 的索引，不是下游 acceptance 证明；supersede 只能标记资产生命周期，不允许反向覆盖下游知识库事实。

## 1. 实现原则

U8 不需要服务化，不需要 API client，不需要 worker runtime，不需要数据库迁移。一个单人可维护的实现应是：读取已存在的 redacted ScoutFlow preview/capture summary，按下游 variant 渲染 Markdown，生成 manifest，计算 checksum，写入 ScoutFlow repo-local staging。任何对 `~/workspace/raw/`、Obsidian vault、DiloFlow repo、hermes-agent repo 的写入都不在实现范围内。

## 2. 文件与代码预算

| 组件 | 估算 LOC | 说明 |
|---|---:|---|
| `tools/egress/build_manifest.py` | 90 | manifest dataclass / dict builder / checksum |
| `tools/egress/render_markdown.py` | 85 | 四种 downstream Markdown renderer |
| `tools/egress/redaction.py` | 90 | regex + field policy + report |
| `tools/egress/supersede.py` | 45 | revision、graph、status validation |
| `tools/egress/cli.py` | 50 | `python -m tools.egress --target raw_vault ...` |
| JSON schema files | 4 files | manifest + 4 downstream variants，或 v1 common + variants |
| tests | 可另计 | 单元测试不算 U8 最小 LOC，但建议加入 |

核心生产代码可控制在约 360 LOC。若把 JSON schema 和测试都算入总 LOC，会超过 400；因此“≤400 LOC”应理解为 generator 核心，而不是测试/文档/schema 总量。

## 3. 开发日程（≤4 天）

| Day | 目标 | 产出 |
|---|---|---|
| Day 1 | Manifest + checksum + path safety | 通用 manifest builder，relative_path containment check |
| Day 2 | RAW + Obsidian renderer | 四字段 RAW candidate、Obsidian namespace note |
| Day 3 | DiloFlow + hermes renderer + redaction | routing fields、agent packet、redaction report |
| Day 4 | Supersede + validation + docs | revision graph、schema validate、README/stdout |

## 4. CLI 草案

```bash
python -m tools.egress   --target raw_vault   --capture-id 01KQYY9KP26SSZA6285MAY706S   --handoff-id sfh_20260507_raw_01   --out docs/research/post-frozen/raw-handoff-staging/sfh_20260507_raw_01   --write-enabled false
```

CLI 硬检查：

- `--write-enabled` 只能是 false。
- `--out` 必须在 ScoutFlow repo 内的 staging 路径。
- target 为 RAW 时禁止 `~/workspace/raw/`。
- redaction report 没通过就不写 assets。
- source capture 必须是当前允许的 manual_url / metadata_only 或明确标 candidate future。

## 5. 伪代码

```python
def build_handoff(target, capture, handoff_id, out_dir):
    assert target in TARGETS
    assert_write_disabled()
    assert_safe_staging_dir(out_dir)
    source = load_safe_capture_summary(capture)
    redacted = redact_source(source)
    if redacted.blocked:
        raise EgressBlocked(redacted.report)
    asset = render_asset(target, redacted)
    asset_hash = sha256(asset.bytes)
    manifest = render_manifest(target, handoff_id, [asset], redacted.report)
    validate_manifest(manifest)
    write_file(out_dir / asset.relative_path, asset.text)
    write_json(out_dir / "manifest.json", manifest)
    write_json(out_dir / "receipts/redaction-report.json", redacted.report)
```

## 6. 测试矩阵

| Test | 期望 |
|---|---|
| `test_raw_frontmatter_four_fields` | RAW note 只有 title/date/tags/status |
| `test_no_direct_raw_path` | out_dir 指向 `~/workspace/raw/` 被拒绝 |
| `test_path_escape_blocked` | `../` relative_path 被拒绝 |
| `test_redaction_cookie_blocks` | cookie/token 命中阻断 |
| `test_signed_url_stripped` | signed query 被移除 |
| `test_manifest_checksum_matches` | checksum 与 redacted asset 一致 |
| `test_supersede_graph_no_cycle` | 循环替代被拒绝 |
| `test_hermes_runtime_false` | execution/runtime approval 必须 false |
| `test_obsidian_namespace` | ScoutFlow 字段全部 `scoutflow_` |
| `test_diloflow_next_action_enum` | 无 `auto_capture` |

## 7. 不做事项

不做 GUI；不做 API endpoint；不做 watcher；不做 importer；不做 RAW/Obsidian/DiloFlow/hermes 写入；不做 live web refresh；不做 media/ASR；不做 DB migration；不做 broad schema evolution；不做自动 readback。

## 8. 验收 stdout

实现完成后应输出：

```yaml
CLOUD_U8_EGRESS_CROSS_SYSTEM_MANIFEST_COMPLETE: true
files_count: 10
write_enabled: false
no_direct_raw_write: confirmed
live_web_browsing_used: false
live_verified_count: 0
redaction_rule_count: 25+
supersede_rule_count: 12+
manifest_json_variants: 4
single_user_budget_loc: 360
single_user_budget_dev_days: 4
ready_for_user_audit: yes
```

## 9. 风险与缓解

| 风险 | 缓解 |
|---|---|
| 下游 parser 不认字段 | schema_version + README + namespace |
| RAW 第二 inbox | handoff_id 子目录 + pending_user_manual_transfer |
| redaction 漏洞 | block by default +人工审核触发 |
| Obsidian template 污染 | `scoutflow_` namespace，不写 templates |
| DiloFlow 误触发采集 | `next_action` 无 auto_capture，LP-001 重申 |
| hermes 泄露上下文 | 只给摘要，禁止 raw JSON/secrets |
| supersede 静默失效 | manifest events + README 人读摘要 |
| 单人实现过度工程 | docs-only + CLI + staging，无服务化 |

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
## 10. 代码分层建议

最小实现可以分成纯函数，避免隐藏状态：`load_capture_summary()` 只读输入；`redact()` 返回 redacted text + report；`render_<target>()` 返回 asset list；`build_manifest()` 组合资产；`validate_handoff()` 做硬检查；`write_package()` 最后落盘。只有最后一步有文件写入，且 out_dir 已经被确认在 ScoutFlow staging。这样单人维护时更容易测试，也不容易出现“renderer 已经写了文件但 validator 才发现 secret”的半成品风险。

## 11. 单人维护的 operational discipline

每次改 schema 都必须同步改 README、tests、redaction allowlist 和 downstream variant。不要让 DiloFlow、RAW、Obsidian、hermes 四个 renderer 分别自创字段；通用字段从一个常量表读取，下游只追加自己的 namespace。开发者不应为了方便把 `raw_api_response` 传进 renderer；renderer 的输入类型应已经是 `SafeCaptureSummary`，从类型层面避免 secret 残影。
