# ScoutFlow AGENTS.md 草案 v0.1

> 目的：给所有 agent 一个短入口。任何 agent 进入 ScoutFlow 项目，先读本文件，再读 `docs/project-context.md` 与 `docs/current.md`。

---

## 0. 红线：Locked Principles

### LP-001 — Capture Scope Gate

推荐信号、关键词扫描、RAW gap、agent 观察不得直接创建 capture。除 `manual_url` quick_capture 外，必须走 Capture Plan。

Enforce：

```text
services/api/middleware/scope_gate.py
tests/api/test_lp001_scope_gate.py
```

### LP-002 — Plan estimate → approve → run

Capture Plan 未 estimate 不允许 approve；未 approve 不允许 run；超 budget 不允许 run。

Enforce：

```text
services/api/services/state_guard.py
tests/api/test_lp002_plan_state.py
```

### LP-003 — merger-of-record

代码 / schema / migration 由 Codex 做 merger-of-record。PRD / IA / 产品叙事由 Opus 主笔。FS layout / schema / state words / LP 改动必须 user 拍板。

Enforce：

```text
.github/pull_request_template.md
本文件
```

### LP-004 — Evidence Browser 不真嵌

Phase 1 / 1A / 1B 不承诺 iframe / WebView 真内嵌，不内嵌登录页。只做 metadata preview + 系统浏览器打开 + browsing event 入账。

Enforce：

```text
docs/product-design.md
tools/check-ui-redlines
```

### LP-005 — 命名禁区

禁止在路径、类名、函数名、日志、spec 中使用：

```text
crawl
crawler
crawling
spider
spidering
scrape_all
scrape_everything
auto_capture
bulk_download
harvest
harvesting
```

替代：

```text
source_scan
metadata_fetch
evidence_collect
quick_capture
scope_then_capture
capture_plan
```

Enforce：

```text
tools/check-banned-words
```

---

## 1. 项目真源

ScoutFlow 的工程真源是：

```text
SQLite schema
FS artifact layout
state words
OpenAPI contract
worker write-zone rules
```

聊天历史不是事实。agent 记忆不是事实。未经 commit 的文件不是事实。

---

## 2. 目录权限

### 可以改

按任务范围改对应目录：

```text
apps/console/
services/api/
workers/
packages/shared-contracts/
docs/
tools/
tests/
```

### 禁止改

```text
data/                # runtime data，不进 git
referencerepo/       # 只读参考仓，不 import，不改
RAW 主仓             # 只能写 RAW inbox，不能自动合并
```

---

## 3. Worker 写区

| Worker | 允许写 | 禁止写 |
|---|---|---|
| bili | `bundle/` | 其他 zone |
| media | `media/` | 其他 zone |
| asr | `transcript/raw.json` | 其他 zone |
| asr_postprocess | `transcript/segments.jsonl`, `media/derived/` | `normalized/`, `links/` |
| normalize | `normalized/` | `transcript/`, `links/` |
| index | DB FTS/index | FS |
| raw_linker | `links/` | RAW 主仓 |
| plan_estimator | `capture_plans.estimate_json` | artifacts |
| recommender | `recommendations`, `signals` | captures / artifacts |
| reranker | `recommendations` | captures / artifacts |

Console 不直接写 DB / FS。Worker 不直连 DB。所有状态转移走 API。

---

## 4. PR / Handoff 模板

```markdown
# PR / Handoff

## 1. 改了什么

## 2. 触碰了哪些 contract
- [ ] SQLite schema
- [ ] FS layout
- [ ] state words
- [ ] OpenAPI
- [ ] worker write-zone
- [ ] LP / safety boundary

## 3. 是否需要 migration
- [ ] No
- [ ] Yes: ...

## 4. 如何验证
- [ ] ruff
- [ ] pytest
- [ ] pnpm typecheck
- [ ] pnpm build
- [ ] check-banned-words
- [ ] check-fs-layout
- [ ] lint-contracts
- [ ] 手动验证：...

## 5. 风险

## 6. 触碰了哪个其他 worker 的写区
- 没有 / 有：...
- 如有，是否需要 cross-zone audit：是 / 否

## 7. introduced vs exposed
- 本次变更引入的问题：...
- 本次变更暴露的历史债：...
```

---

## 5. 故障复盘规则

任何 capture / job / plan 失败复盘必须分两栏：

```text
introduced by this change:
  本次变更新引入的问题

exposed by this change:
  本次变更暴露出的历史债
```

禁止默认把所有问题归因到最近 PR。

---

## 6. Phase 边界

### Phase 0

只做 repo skeleton、docs、lint、API stub、Console mock、migration runner、FS checker。

不做真实采集。

### Phase 1A

只做 B 站单条 manual URL quick_capture → Library 可检索。

不做 Signal Workbench、XHS、RAW patch、Hermes 推荐。

### Phase 1B

只做 RAW Link stub：生成 suggestion，user accept 后写 RAW inbox。

### Phase 2

启用 Signal Workbench、Capture Plan、Plan Estimator、XHS metadata、Reverse Discovery。

### Phase 3+

主动推荐、Hermes、多 agent UI。

---

## 7. 命令入口

优先使用统一命令，不要手写随机命令：

```bash
make test
make lint
make build
make check-contracts
make check-fs
make check-docs
```

如果使用 `justfile`，同理。

---

## 8. 合并仲裁

| 变更 | merger-of-record |
|---|---|
| API / worker / tests / CI | Codex |
| schema / state words / FS layout | Codex + Opus + user |
| PRD / IA / 产品叙事 | Opus + Codex sanity + user |
| UI implementation | Codex |
| visual direction | Opus + user，Claude Design 只做原型 |
| LP / 安全边界 | Codex + Opus + user |

---

## 9. 参考仓规则

`referencerepo/` 只读。

如果引用参考仓经验，先更新或查看：

```text
docs/research/reference-repo-index.md
```

不要重新搜索已经索引过的参考仓，除非 user 明确要求刷新。
