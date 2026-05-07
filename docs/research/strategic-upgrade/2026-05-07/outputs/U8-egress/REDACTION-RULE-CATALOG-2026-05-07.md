---
title: REDACTION RULE CATALOG — ScoutFlow Egress
status: candidate / redaction-catalog / not-authority
authority: not-authority
claim_label: "95% spec coverage; rules not executed in this session"
created_at: 2026-05-07
generated_in_environment: 2026-05-06
write_enabled: false
redaction_execution: not-run
---

# REDACTION RULE CATALOG — ScoutFlow Egress

## 0. 证据与边界口径

本交付只声明 ScoutFlow 单方面写出的文件级 egress contract，不定义 SDK、OpenAPI client、双向同步 broker，也不修改任何下游。PRD v2 的最高边界是：ScoutFlow 是单 user、local-first 的采集与证据工作台；RAW、Obsidian、DiloFlow 是下游消费者，不是 ScoutFlow 项目的一部分。SRD v2 的最高边界是：当前生效的是 metadata-only、receipt、trust trace、redaction/secret scan baseline；Phase 2+ 对象仍主要是 outline，不能被文件导出契约误读成 runtime unlock。

本环境已经读取上传的 post176 audit pack 与 GitHub 上的 PRD/SRD、Run-3+4 C2 文件。普通 live web 浏览在当前会话被禁用，所以本文所有外部 vendor/frontmatter 口径只作为“需刷新验证的公共模式候选”，不标记为 live verified。`~/workspace/DiloFlow/`、`~/workspace/raw/`、`~/workspace/hermes-agent/` 与 Obsidian 本地 vault 在当前容器没有出现；因此 DiloFlow 与 hermes-agent 的 receiver-side parser 只能给出单方、保守、低耦合的文件契约，不能声称已经被下游 repo 实测接受。

硬边界在所有下游一致：`write_enabled=false` 保持；ScoutFlow 永不直写 `~/workspace/raw/`；凭据、cookie、token、QR 图片、browser profile path、auth sidecar、raw stdout/stderr 中可能含秘密的片段不得进入 egress；Bilibili/XHS 等平台原作者隐私字段只允许最小必要、脱敏后的事实摘要；manifest 是一次 handoff 的索引，不是下游 acceptance 证明；supersede 只能标记资产生命周期，不允许反向覆盖下游知识库事实。

## 1. 基本原则

Redaction 是 egress 前置条件，不是下游自愿步骤。任何进入 DiloFlow、RAW、Obsidian、hermes-agent 的文件，都必须先经过同一套最小规则：先 omit 高风险字段，再 mask 可保留字段，再 hash 需要去重但不能泄露的标识。checksum 必须对 redacted payload 计算，不能对原文计算后再导出。

本目录是 specification，不是执行日志。当前没有运行实际 regex/NER/redaction scanner；因此 artifact 的 `redaction_applied=true` 是未来生成器的要求，不是对本次聊天输入的运行结果声明。

## 2. 字段处置等级

| 等级 | 动作 | 适用 | 输出示例 |
|---|---|---|---|
| `omit` | 完全删除字段和值 | 凭据、QR、profile path、auth sidecar | 字段不存在 |
| `mask` | 保留类别和局部形状 | email/phone/ID、作者公开名旁的敏感 ID | `ma***@example.com` |
| `hash` | 稳定去重但不可逆 | user_id、device_id、request_id | `sha256:abcd...` |
| `generalize` | 降精度 | 时间、地理位置、文件路径 | `2026-05-07`, `<local_path>` |
| `allow` | 原样保留 | capture_id、platform_item_id、canonical public URL | `BV...` |

## 3. Credential / secret 规则

| rule_id | 命中对象 | 动作 | 说明 |
|---|---|---|---|
| `SEC-CRED-001` | `cookie`, `session`, `csrf`, `token`, `authorization`, `bearer` | omit | key/value 都不可导出 |
| `SEC-CRED-002` | `BBDown.data`, `BBDownTV.data`, auth sidecar | omit | 文件名、路径、内容都不可导出 |
| `SEC-CRED-003` | `qrcode.png`, QR base64, login QR URL | omit | QR 是登录材料，不是 evidence |
| `SEC-CRED-004` | browser profile path, `User Data`, `Default/Cookies` | omit/generalize | 不暴露本机登录态位置 |
| `SEC-CRED-005` | signed URL, expiring query, `expires`, `signature`, `auth_key` | strip query or omit | 只保留 canonical URL |
| `SEC-CRED-006` | raw stdout/stderr that may contain secrets | omit | 只保留 classified summary |
| `SEC-CRED-007` | API key / OpenAI key / GitHub token / PAT | omit | 任何下游都不能看到 |

建议 regex 草案：

```text
(?i)(cookie|session|csrf|xsrf|token|authorization|bearer|api[_-]?key|secret|password|passwd)\s*[:=]
(?i)(BBDown(?:TV)?\.data|qrcode\.(?:png|jpg|jpeg)|User Data|Default/Cookies)
(?i)([?&](?:sign|signature|auth_key|token|expires|expire|session|cookie)=)[^&\s]+
```

## 4. PII 规则

| rule_id | 命中对象 | 动作 | 说明 |
|---|---|---|---|
| `PII-EMAIL-001` | email address | mask | `name@example.com` → `n***@example.com` |
| `PII-PHONE-001` | phone number | mask | 保留国家码/后两位即可 |
| `PII-ID-001` | 身份证、护照、学号、工号 | omit/hash | 若非 public evidence，禁止导出 |
| `PII-ADDR-001` | 家庭住址/精确地理位置 | generalize | 城市级或 omit |
| `PII-NAME-001` | 非公众人物真实姓名 | mask/generalize | 与平台公开名分开处理 |
| `PII-IMAGE-001` | 人脸、二维码、私聊截图 | omit | U8 文件级合同不导出图片 |
| `PII-COMMENT-001` | 评论区用户隐私信息 | omit/mask | 默认不收评论区个人数据 |

Regex 草案：

```text
[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}
(?<!\d)(?:\+?86[- ]?)?1[3-9]\d{9}(?!\d)
(?<!\d)\d{17}[0-9Xx](?!\d)
```

这些 regex 只是第一层。中文姓名、地址和平台隐私字段需要基于字段名、上下文和人工审核，不应完全依赖 regex。

## 5. 平台/法律敏感规则

| rule_id | 对象 | 动作 | 原因 |
|---|---|---|---|
| `PLAT-BILI-001` | Bilibili 原作者公开视频 BV ID / canonical URL | allow | 公共可引用入口 |
| `PLAT-BILI-002` | 原作者 uid、私信入口、粉丝精确画像、非必要账号属性 | omit/hash | 法律/隐私敏感，且非 egress 必要 |
| `PLAT-BILI-003` | 评论用户 ID / 弹幕用户信息 | omit | 当前 metadata-only 不应包含评论个人数据 |
| `PLAT-XHS-001` | XHS 账号、笔记隐私字段、图片原图 EXIF | omit | XHS 当前更严格只读边界 |
| `PLAT-YT-001` | YouTube later runtime evidence | conditional | 当前 later，非默认 |
| `PLAT-TOS-001` | 绕过付费/地区/访问控制的材料 | omit | 不进入 evidence 或 egress |

## 6. 本地路径规则

本地路径暴露会泄露用户名、项目布局、登录态位置。规则：

- `/Users/<name>/workspace/ScoutFlow/...` 在公开或下游 LLM 中 generalize 为 `<SCOUTFLOW_ROOT>/...`。
- `~/workspace/raw/` 可以作为概念性目标路径出现，因为合同边界需要，但不得显示真实用户 home 细节以外的敏感路径。
- browser profile、cookie DB、auth cache、venv secret 文件、`.env` 路径一律 omit。
- checksum/report 可以记录 relative_path，不记录任意绝对路径。

## 7. Markdown redaction 检查顺序

1. 解析 frontmatter，检查重复 key。
2. 对 frontmatter key/value 跑 forbidden key scan。
3. 对正文跑 URL canonicalization，去 signed query。
4. 对正文跑 secret regex。
5. 对正文跑 PII regex。
6. 对路径样式跑 local path scanner。
7. 对 fenced code block 单独检查，不因在代码块内就豁免。
8. 生成 redaction report。
9. 仅对 redacted payload 计算 checksum。
10. 写 manifest。

## 8. redaction-report.json 建议

```json
{
  "ruleset_version": "scoutflow-redaction-v1",
  "created_at": "2026-05-07T00:00:00Z",
  "applied": true,
  "scanner_mode": "regex_plus_field_policy",
  "assets_scanned": 2,
  "findings_count": 3,
  "findings": [
    {"rule_id": "SEC-CRED-005", "action": "strip_query", "field": "source_url"},
    {"rule_id": "PII-EMAIL-001", "action": "mask", "field": "body"}
  ],
  "blocked": false,
  "blocked_reason": null
}
```

若 `blocked=true`，包不得进入 egress staging。若某个字段无法判断，默认 `omit` 或标记 `needs_human_review`，不能默认 allow。

## 9. 下游差异

| 下游 | redaction 严格度 | 特别规则 |
|---|---|---|
| DiloFlow | 高 | 保留 routing 所需字段，不给 raw stdout |
| RAW | 高 | 只给 candidate note，不给 raw API response |
| Obsidian | 更高 | 用户可能 Sync/Publish，默认 local_only，wikilink 不含隐私 |
| hermes-agent | 最高 | LLM side process 只给摘要，不给原始 JSON/长日志 |

## 10. 自动化检查伪代码

```python
FORBIDDEN_KEYS = ["cookie", "token", "authorization", "qrcode", "browser_profile_path"]

def redact_asset(asset: Asset) -> RedactedAsset:
    fm, body = parse_markdown(asset.text)
    assert_unique_frontmatter_keys(fm)
    fm = omit_forbidden_keys(fm, FORBIDDEN_KEYS)
    fm = canonicalize_source_url(fm)
    body = strip_signed_urls(body)
    body = mask_pii(body)
    body = generalize_local_paths(body)
    report = build_report(findings)
    if report.has_unresolved_secret:
        raise BlockEgress(report)
    return RedactedAsset(render(fm, body), report)
```

## 11. 人工审核触发

- 命中 secret regex。
- 出现不认识的平台字段。
- 需要保留作者信息但字段语义不清。
- 出现图片、二维码、截图、EXIF。
- 下游目标是 Obsidian Publish 或其他 public_safe。
- hermes-agent 需要长上下文。
- supersede 原因是 redaction_update，说明旧版本可能已有泄露，需要人工确认是否撤下。

## 12. 验收标准

- 每个 asset 都有 `redaction.applied=true`。
- manifest 有 `redaction_summary`。
- redaction report 与 asset checksum 匹配。
- 无 credential/PII/local path 禁止项。
- 对需要 omit 的字段，不用 `[REDACTED]` 占位暴露字段名和值形状，除非该字段名本身安全且有审计价值。
- 所有下游都不能跳过此步骤。

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
## 13. URL canonicalization 细则

URL 是最容易混入敏感残影的字段。`canonical_url` 只允许保留协议、域名、公开路径和必要的公开视频 ID。任何 query string 都先进入 deny-by-default：`utm_*`, `spm_id_from`, `vd_source`, `share_source`, `timestamp`, `session`, `token`, `sign`, `auth_key`, `expires`, `mid`, `uid` 等都不得默认保留。Bilibili BV URL 建议规范化为 `https://www.bilibili.com/video/<BV...>/`。如果原始 URL 中包含用户分享来源或追踪参数，manifest 可以记录 `source_url_was_canonicalized=true`，但不保留原始 URL。

## 14. Field allowlist 优先于 blocklist

仅靠 blocklist 不够，因为平台字段会变化。每个 downstream variant 应有 allowlist。RAW allowlist：`title`, `date`, `tags`, `status`, `capture_id`, `platform_item_id`, `canonical_url`, `export_posture`, `preview_only`, `write_enabled`, `evidence_source`, `transfer_note`。Obsidian allowlist：`title`, `aliases`, `tags`, `created`, `updated`, `scoutflow_*`。DiloFlow allowlist：`asset_id`, `kind`, `channel`, `next_action`, `operator_angle`, `capture_id`, `source_url`。hermes allowlist：`mission`, `context summary`, `allowed_operations`, `forbidden_operations`, `redacted findings`。任何不在 allowlist 且命中隐私/凭据语义的字段必须 omit。

## 15. Redaction failure posture

如果扫描器不确定，默认失败而不是默认通过。失败包应只写本地 `redaction-blocked-report.json`，不要写 downstream staging。报告可以包含 rule_id、字段名、动作建议、命中摘要，但不包含命中原文。对用户最有用的提示不是“发现 secret”，而是“哪个 asset、哪个字段、应该 omit/mask/hash”。这样既能修复，又不把秘密复制到报告里。
## 16. 最小人工审计问句

每次 egress 前，人工 reviewer 至少回答四个问题：这份资产是否包含任何登录材料或登录路径？这份资产是否包含任何非必要个人信息？这份资产的 URL 是否已经 canonical 化？这份资产如果被复制到 Obsidian Publish 或传给 hermes-agent，是否仍然安全？四个问题有任意一个不确定，就不能进入 handoff manifest 的 `assets` 列表，只能进入 blocked report。
