# Phase 1A Readiness — Bilibili manual_url quick_capture

> Status: readiness draft
> Product-code approval: No
> Implementation task to be approved later: T-P1A-001

## 1. Scope

本 readiness pack 只把 Phase 1A 候选实现范围收敛成一个后续可审批的最小代码任务：

```text
Bilibili manual_url quick_capture preparation
```

当前任务 `T-P0-007` 只做文档与 contract 对齐，不实现 API / worker / Console，不创建产品代码目录，不运行真实采集。

## 2. Authority sources

本文件只引用仓库文件，不引用聊天摘要作为 authority：

- `docs/PRD-v1-2026-05-02.md`
- `docs/PRD-v1.1-amendment-2026-05-02.md`
- `docs/SRD-v1-2026-05-02.md`
- `docs/SRD-v1.1-amendment-2026-05-03.md`
- `docs/specs/contracts-index.md`
- `docs/specs/locked-principles.md`
- `docs/specs/worker-receipt-contract.md`
- `docs/specs/platform-adapter-risk-contract.md`
- `docs/specs/raw-response-redaction.md`
- `docs/current.md`
- `docs/task-index.md`

当前 authority chain 以 `docs/SRD-v1.1-amendment-2026-05-03.md` A001 为准：user 最新拍板 > locked principles > decision log > PRD + amendment > SRD > operating model > 历史对话 / agent 记忆。

## 3. What Phase 1A is allowed to implement

后续 `T-P1A-001` 可以被提议为第一项 code-bearing Phase 1A 任务，但只允许覆盖以下最小范围：

- `manual_url` quick_capture entry
- Bilibili 单条 URL metadata / audio / transcript preparation
- `POST /captures/discover` 作为 capture creation entrypoint
- `artifact_assets` / receipt / redaction discipline
- SQLite + FS authority alignment
- docs-check + minimal tests

上述内容仍需要 user 另行批准。当前文档只提供开工门，不代表批准开始实现。

## 4. What remains forbidden

Phase 1A 首个实现任务不得包含：

- recommendation-driven capture
- keyword / RAW gap direct capture
- Signal Workbench runtime
- Capture Plan UI / runtime
- XHS
- YouTube
- Hermes scheduling
- browser automation
- real recommendation / rerank
- comment chain
- multi-user / SaaS
- Phase 2-4 runtime logic

`recommendation / keyword / RAW gap` 可以作为 Phase 2+ 的信号来源 outline，但不得直接创建 capture。

## 5. Minimal T-P1A-001 candidate

`T-P1A-001` 的候选最小任务应是：

```text
Implement Bilibili manual_url quick_capture creation path with contract tests.
```

候选边界：

- 输入：user 手动粘贴的单条 Bilibili URL
- 入口：`POST /captures/discover`
- 允许 `source_kind`：`manual_url`
- 允许 `quick_capture_preset`：`metadata_only` / `audio_transcript`
- 最小产物：capture record、capture manifest、worker receipt contract 对齐、artifact ledger 对齐
- 最小验证：LP-001 拒收测试、receipt/redaction contract 测试、docs redline check

建议状态机：

```text
draft
  -> user_approved
  -> branch_implemented
  -> validation_review
  -> merge_candidate
```

转移门：

- `draft -> user_approved`：user 明确批准 `T-P1A-001` 可写产品代码
- `user_approved -> branch_implemented`：任务分支只改授权路径
- `branch_implemented -> validation_review`：最小测试与 docs-check 已执行
- `validation_review -> merge_candidate`：PR diff 证明无 Phase 2+ 抢跑、无凭据泄露、无禁区路径

## 6. Required contracts

`T-P1A-001` 必须引用并满足以下 contract：

- `C-AUTH-001`：Authority Chain
- `C-SCOPE-001`：Phase Scope Freeze
- `C-PROC-001`：Definition of Ready / Done / Stop-the-line
- `C-CAP-001`：Capture Entry API Semantics
- `C-CAP-002`：`capture_mode` / `quick_capture_preset`
- `C-CAP-003`：`source_kind` / `created_by_path`
- `C-ART-001`：`artifact_assets` 命名与台账入口
- `C-WRK-001`：Worker Receipt & Artifact Ledger
- `C-PLT-001`：Platform Adapter Risk Contract
- `C-SEC-001`：Raw Response Redaction & Credential Safety

当前仍属待拍板 / candidate baseline 的 contract，不应写成已经完成的产品事实。

## 7. `/captures/discover` semantics

当前语义必须保持：

```text
POST /captures/discover = capture creation entrypoint
not source discovery
not search
not recommendation discovery
```

Phase 1A 只允许：

```text
source_kind=manual_url
quick_capture_preset=metadata_only | audio_transcript
```

非 `manual_url` 当前应拒绝，不得把 recommendation、keyword、RAW gap、list、agent 写成 capture creation 的合法入口来源。

## 8. Data / artifact boundaries

Phase 1A 后续实现必须遵守 PRD §5 的 FS authority：

```text
data/artifacts/<platform>/<capture_id>/{bundle,media,transcript,normalized,links,logs}/
```

边界规则：

- 当前任务不修改 `data/`
- `data/` 不进 git
- `referencerepo/` 不进 git
- worker 只提交相对路径，不提交绝对路径
- API 负责把 receipt 映射到 `artifact_assets`
- `links` 区当前只保留为允许区，真实 RAW link 产物从 Phase 1B 起产生

PRD base 中旧的完整 Phase 1A 链路和 Phase 2+ 目录描述只作为背景；后续 `T-P1A-001` 不能借此抢跑 RAW link、Signal Workbench、推荐或多平台采集。

## 9. Worker receipt and redaction requirements

后续实现必须满足 `docs/specs/worker-receipt-contract.md`：

- receipt 顶层必须包含 `job_id`、`capture_id`、`job_type`、`producer`、`producer_version`、`idempotency`、`platform_result`、`produced_assets`、`next_status`
- `produced_assets[]` 必须包含 `zone`、`artifact_kind`、`relative_path`、`sha256`、`bytes`、`is_raw_evidence`、`is_derived`、`redaction_applied`、`created_by_job`
- `relative_path` 必须位于 capture root 之下
- `zone` 必须与 `relative_path` 首目录一致
- `raw_api_response` 必须 `redaction_applied=true`

后续实现还必须满足 `docs/specs/raw-response-redaction.md`：

- 凭据不是 evidence
- request headers、cookie jar、本地登录态文件、浏览器 profile 不进 artifact ledger
- `Cookie`、`Authorization`、`Set-Cookie`、token、`SESSDATA`、`bili_jct`、`DedeUserID` 等不得落盘
- receipt、job event、日志、stderr 使用同一脱敏纪律

## 10. Platform risk rules

后续 Bilibili adapter 必须按 `docs/specs/platform-adapter-risk-contract.md` 输出 typed `platform_result`：

```text
ok
auth_required
rate_limited
forbidden
not_found
region_blocked
vip_required
parser_drift
network_error
timeout
unavailable
unknown_error
```

Phase 1A 当前允许的技术表面只包括 metadata fetch、`BBDown`、`yt-dlp` fallback、`ffmpeg`。不得通过浏览器自动化补平台缺口，不得把所有异常合并成通用 `failed`。

## 11. Acceptance criteria for T-P1A-001

`T-P1A-001` 进入 review 前至少需要满足：

- task 已在 `docs/task-index.md` 登记，owner、scope、allowed paths、forbidden paths、validation、stop-the-line 明确
- user 明确批准该任务可写产品代码
- 只实现 Bilibili `manual_url` quick_capture 最小路径
- `POST /captures/discover` 只作为 capture creation entrypoint
- `manual_url` 满足 quick_capture 条件时可创建 capture
- `recommendation` / `keyword` / `raw_gap` 等入口返回 LP-001 拒收结果
- 不实现 Signal Workbench、Capture Plan UI/runtime、XHS、YouTube、Hermes、推荐、重排、评论链路
- raw response、receipt、logs 不泄露凭据
- `artifact_assets` 与 worker receipt 映射可测试
- docs-check 与最小 contract tests 已执行

## 12. Validation commands

本 `T-P0-007` docs-only readiness task 的验证命令：

```bash
python -m py_compile tools/check-docs-redlines.py
python tools/check-docs-redlines.py
find . -maxdepth 1 -type d \( -name apps -o -name services -o -name workers -o -name packages -o -name candidates -o -name dispatches -o -name audits -o -name example -o -name examples \) -print
git ls-files | grep -E '^(data|referencerepo|example|examples)/' || true
grep -RIn "T-P0-005\|T-P0-006\|github queue\|sync smoke\|Codex adapter\|MCP communication" AGENTS.md README.md docs/current.md docs/task-index.md docs/decision-log.md docs/plans/phase1a-manual-url-quick-capture-readiness-2026-05-03.md || true
```

后续 `T-P1A-001` 应补充产品代码测试命令；本文件不提前创建测试文件或产品目录。

## 13. Stop-the-line rules

命中以下任一情况，当前或后续任务必须停线：

- docs-only 任务触碰产品代码
- 创建 `apps/`、`services/`、`workers/`、`packages/`
- 修改或跟踪 `data/`、`referencerepo/`
- 创建 `example/`、`examples/`
- 创建根级 `candidates/`、`dispatches/`、`audits/`
- `recommendation / keyword / RAW gap` 被允许直接创建 capture
- `/captures/discover` 被写成 source discovery / search / recommendation discovery
- 实现浏览器自动化
- 引入 Phase 2-4 runtime logic
- raw response、receipt、日志、stderr 泄露凭据
- platform failure 没有 typed `platform_result`
- 旧 `media_assets` 回流为当前实体名

## 14. User decisions still needed

仍需 user 拍板：

- 是否批准本 readiness pack 作为 `T-P1A-001` 的开工依据
- 是否明确授权 `T-P1A-001` 成为第一项 code-bearing Phase 1A 任务
- quick_capture 阈值是否继续采用 `100 MB / 30 min / 50k token`
- `manual_admin` 是否保留在最小 Step0 / Phase 1A contract
- `auth_required`、`region_blocked`、`vip_required` 对 `source.status` 的最终映射
- `T-P1A-001` 是否只做 `metadata_only`，还是同时允许 `audio_transcript`

## 15. User decision matrix for T-P1A-001

| Decision | Options | Recommended default | Blocks T-P1A-001? |
|---|---|---|---|
| First implementation mode | `metadata_only only` / `metadata + audio_transcript` | `metadata_only only` | Yes |
| quick_capture thresholds | `keep 100 MB / 30 min / 50k token` / `change` | `keep current` | Yes |
| `manual_admin` | `include` / `exclude` | `exclude from first implementation` | Yes |
| Bilibili `auth_required` handling | `source blocked` / `capture failed typed result` / `manual retry` | `capture failed typed result first` | Yes |
| PR style | `one implementation PR` / `split API + worker PRs` | `one tiny implementation PR` | Yes |
