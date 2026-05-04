# PRD v1.1 Amendment — 2026-05-02

> **非全文重写，仅补丁。** 与 `PRD-v1-2026-05-02.md` 一同生效。
> 冲突时本 amendment 为准（amendment > base PRD）。
> Lock 项以本 amendment 的 D022-D033 为准，与 `PRD-v1` D001-D021 联合构成 v1.1 契约。

---

## 0. Amendment 元信息

| 字段 | 值 |
|---|---|
| amendment ID | A001 |
| 版本 | v1.1 |
| 提案日期 | 2026-05-02 |
| 提案人 | user（基于 Opus + Codex 协调） |
| 触发原因 | 原 PRD 缺采集前置 gate；推荐信号 → 直接采集会导致 artifact 暴涨 + 文案库噪声 |
| 影响章节（base PRD） | §1 / §2 / §6 / §7 / §8 / §10 / §11 / §13 / §15 |
| 不动章节（base PRD） | §4 Authority-first / §5 FS Layout 6 区核心 / §14 安全合规红线 / §22-§24 附录 |
| 本 amendment 行数 | ~1500 行 |
| 状态 | DRAFT，待 user 拍板锁定 |

---

## 1. 新增 Locked Principle — LP-001 Capture Scope Gate

### 1.1 原则文本（lock）

> **LP-001（Capture Scope Gate）**：任何推荐信号、选题想法、RAW 缺口、关键词扫描结果，**不得默认直接进入采集**。必须先经过 Capture Scope 确认，生成 Capture Plan，且 Plan estimate 完成后由 user approve，才能进入 Capture Pipeline。

### 1.2 例外（quick_capture）

仅在以下**全部条件同时成立**时允许 user 直接触发采集，绕过 Scope Builder：

1. 来源是 **user 手动粘贴的单条 URL**（不是推荐流、不是关键词扩散、不是 RAW gap 反推）
2. capture_mode ∈ `{metadata_only, audio_transcript}`（不允许 video / 不允许评论 / 不允许 OCR / 不允许图片原图）
3. 不抓作者扩展（不"顺便采该 UP 主最近 N 条"）
4. 不抓关键词扩展（不"顺便搜相关"）
5. 估算媒体 ≤ 100 MB / ASR ≤ 30 min / LLM token ≤ 50k
6. 风险等级 = low（无登录依赖 / 无版权敏感）

任一条件不满足 → quick_capture 拒绝，走标准 Scope 流程。

### 1.3 与 LP-001 冲突的旧 PRD 段落（明示废止）

- ❌ 原 §10.4 Source Radar 卡片操作按钮 `[采集 audio][仅 metadata][忽略]` → 改为 `[打开 Scope][验证信号][稍后看][忽略]`
- ❌ 原 §11 Recommendation `suggested_action='capture'` → 改为 `open_scope` / `verify_signal` / `quick_capture`（quick_capture 仅在 LP-001 §1.2 条件下出现）
- ❌ 原 §2.2 用户路径 P1 "推荐 → 直接采集" → 改为 "推荐 → 打开 Scope → 浏览证据 → 决定 scope → estimate → approve → 采集"

### 1.4 LP-001 落地的物理 enforcement

- API 层：`POST /captures/discover` 拒绝来源 = recommendation 且未携带 `capture_plan_id` 的请求
- UI 层：Source Radar 卡片不渲染 `[采集]` 按钮（仅渲染 `[打开 Scope]`）
- worker 层：media-download worker 收到 job 时校验 `job.params.capture_plan_id` 存在且 plan.status='approved'
- 仪表盘：`v_dashboard_counts` 增加 `pending_scope_decisions` / `pending_plan_approvals` 字段

---

## 2. 四前置实体（新增）

补全 ScoutFlow 实体链：

```text
source           信号来源（账号 / 关键词 / 链接 / 列表 / RSS）
source_item      source 扫描到的平台对象
signal           系统认为"这里可能有价值"的观察（新增）
hypothesis       user 对 signal 的即时判断（新增）
capture_plan     为验证 hypothesis 而生成的采集范围（新增）
capture          真正落盘入库的证据单元
topic_card       被证据反复打磨后的候选选题卡（新增）
normalized_doc   单 capture 的规整产物
knowledge_link   capture 与 RAW / Obsidian 的关联
candidate        agent 提交的提案
```

### 2.1 signals 表

```sql
CREATE TABLE signals (
    id TEXT PRIMARY KEY,                    -- ULID
    signal_type TEXT NOT NULL CHECK (signal_type IN
        ('platform_item',         -- 单平台对象（一个视频 / 一篇笔记）
         'multi_source_cluster',  -- 多源同主题聚类
         'keyword_spike',         -- 关键词热度异常
         'creator_change',        -- 关注创作者风格 / 节奏变化
         'raw_gap',               -- RAW 缺口反推
         'manual_observation')),  -- user 手动打"这个有戏"
    title TEXT NOT NULL,
    summary TEXT,
    origin_kind TEXT NOT NULL CHECK (origin_kind IN
        ('source_item', 'recommendation', 'raw_node', 'manual', 'agent')),
    origin_id TEXT,                          -- 指回 source_items.id / recommendations.id 等
    score REAL,                              -- 系统评分 0-1
    reason TEXT,                             -- 系统给出的"为什么是 signal"
    related_creator_id TEXT REFERENCES creators(id),
    related_keywords_json TEXT,              -- ["低质量旅行","年轻人不爱旅游"]
    related_platforms_json TEXT,             -- ["bilibili","xhs"]
    status TEXT NOT NULL DEFAULT 'observed' CHECK (status IN
        ('observed',          -- 系统刚发现 / user 还未打开
         'opened',            -- user 在 Signal Workbench 打开了它
         'hypothesized',      -- user 写下了至少一条 hypothesis
         'browsing',          -- 在 Evidence Browser 浏览中
         'scope_decided',     -- user 决定了 scope（但未 approve）
         'plan_ready',        -- capture_plan 已 estimate 完成
         'capturing',         -- 实际采集执行中
         'evidence_locked',   -- 采集完成 + raw evidence 落盘
         'refined',           -- 选题卡已 refine
         'dismissed')),       -- user 主动放弃
    promoted_topic_card_id TEXT REFERENCES topic_cards(id),
    created_by TEXT NOT NULL DEFAULT 'system',
    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    updated_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now'))
);

CREATE INDEX idx_signals_status ON signals(status);
CREATE INDEX idx_signals_type ON signals(signal_type);
CREATE INDEX idx_signals_score ON signals(status, score DESC) WHERE status IN ('observed','opened');
CREATE INDEX idx_signals_origin ON signals(origin_kind, origin_id);
```

### 2.2 hypotheses 表

```sql
CREATE TABLE hypotheses (
    id TEXT PRIMARY KEY,                     -- ULID
    signal_id TEXT NOT NULL REFERENCES signals(id) ON DELETE CASCADE,
    hypothesis_text TEXT NOT NULL,           -- "这不是旅游热点，而是消费降级体验焦虑"
    confidence REAL,                         -- user 自评 0-1
    needed_evidence_kind TEXT,               -- "高赞评论的语气 / 多平台同时出现 / 反对方论点"
    status TEXT NOT NULL DEFAULT 'draft' CHECK (status IN
        ('draft',
         'needs_evidence',
         'validated',
         'weakened',
         'rejected')),
    created_by TEXT NOT NULL DEFAULT 'user',
    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    updated_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now'))
);

CREATE INDEX idx_hypotheses_signal ON hypotheses(signal_id, created_at);
CREATE INDEX idx_hypotheses_status ON hypotheses(status);
```

### 2.3 capture_plans 表

```sql
CREATE TABLE capture_plans (
    id TEXT PRIMARY KEY,                     -- ULID
    signal_id TEXT REFERENCES signals(id) ON DELETE SET NULL,
    hypothesis_id TEXT REFERENCES hypotheses(id) ON DELETE SET NULL,
    title TEXT NOT NULL,
    scope_json TEXT NOT NULL,                -- 见 §2.3.1
    budget_json TEXT NOT NULL,               -- 见 §2.3.2
    risk_level TEXT NOT NULL DEFAULT 'low' CHECK (risk_level IN
        ('low', 'medium', 'high')),
    estimate_json TEXT,                      -- 估算结果（estimate API 写）
    status TEXT NOT NULL DEFAULT 'draft' CHECK (status IN
        ('draft',          -- user 在 Scope Builder 编辑中
         'estimating',     -- API 已收 estimate 请求，估算 worker 跑
         'estimated',      -- 估算完成，等 user approve
         'approved',       -- user 已 approve，可入 capture pipeline
         'running',        -- capture 任务执行中
         'completed',      -- 全部 capture 跑完
         'canceled',       -- user 取消
         'failed')),       -- 部分 capture 失败超阈值
    created_by TEXT NOT NULL DEFAULT 'user',
    approved_by TEXT,
    approved_at TEXT,
    started_at TEXT,
    completed_at TEXT,
    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    updated_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now'))
);

CREATE INDEX idx_plans_signal ON capture_plans(signal_id);
CREATE INDEX idx_plans_hypothesis ON capture_plans(hypothesis_id);
CREATE INDEX idx_plans_status ON capture_plans(status);

-- 单 signal 同时只能有 1 个 active plan（不允许平行计划）
CREATE UNIQUE INDEX idx_plans_one_active_per_signal
ON capture_plans(signal_id)
WHERE status IN ('draft', 'estimating', 'estimated', 'approved', 'running');
```

#### 2.3.1 scope_json schema

```json
{
  "targets": [
    {
      "platform": "bilibili",
      "target_type": "single_video",
      "url": "https://www.bilibili.com/video/BV...",
      "actions": ["metadata", "audio", "transcript", "top_comments"]
    },
    {
      "platform": "bilibili",
      "target_type": "creator_recent",
      "creator_id": "1234567",
      "limit": 3,
      "since_days": 30,
      "actions": ["metadata", "audio", "transcript"]
    },
    {
      "platform": "xhs",
      "target_type": "keyword",
      "query": "低质量旅行",
      "limit": 10,
      "actions": ["metadata", "images", "ocr", "top_comments"]
    },
    {
      "platform": "xhs",
      "target_type": "single_note",
      "url": "https://www.xiaohongshu.com/explore/...",
      "actions": ["metadata", "images", "ocr"]
    }
  ]
}
```

allowed `target_type`：
- `single_video` / `single_note` — 单条
- `creator_recent` — 作者最近 N 条
- `keyword` — 关键词扫描（限 limit）
- `list` — 收藏夹 / 合集 / playlist
- `rss_window` — RSS feed 时间窗

allowed `actions`（按平台过滤）：
- `metadata` — 平台 metadata
- `source_snapshot` — HTML / 截图存档
- `media` — video 或 audio 下载
- `audio` — 仅音频
- `transcript` — ASR 转写
- `images` — 图片原图（XHS）
- `ocr` — 图片 OCR（XHS）
- `top_comments` — 高赞评论 Top N（默认 N=20）
- `comment_threads` — 评论楼中楼（默认 depth=1）
- `danmaku` — 弹幕（B 站）
- `subtitle` — 平台原生字幕

#### 2.3.2 budget_json schema

```json
{
  "max_items": 15,
  "max_media_mb": 1200,
  "max_audio_minutes": 90,
  "max_asr_minutes": 90,
  "max_comment_count": 300,
  "max_comment_depth": 1,
  "max_image_count": 50,
  "max_ocr_image_count": 20,
  "max_llm_tokens": 200000,
  "allow_video_download": false,
  "allow_image_originals": true,
  "allow_comment_threads": false,
  "requires_manual_confirm": true,
  "estimated_cost_usd_max": 0.50,
  "estimated_duration_minutes_max": 25
}
```

#### 2.3.3 estimate_json schema（estimate API 填）

```json
{
  "estimated_at": "2026-05-02T11:00:00Z",
  "items_count": 14,
  "media_size_mb": 980,
  "audio_minutes": 78,
  "asr_minutes_estimated": 78,
  "comment_count_estimated": 280,
  "image_count": 42,
  "ocr_image_count": 18,
  "llm_tokens_estimated": 165000,
  "llm_cost_usd_estimated": 0.42,
  "duration_minutes_estimated": 22,
  "risk_factors": [
    "xhs_high_rate_limit_risk",
    "audio_extract_for_3_videos"
  ],
  "warnings": []
}
```

### 2.4 topic_cards 表

```sql
CREATE TABLE topic_cards (
    id TEXT PRIMARY KEY,                     -- ULID
    signal_id TEXT REFERENCES signals(id) ON DELETE SET NULL,
    title_direction TEXT NOT NULL,           -- "年轻人不是不爱旅行，是不想再为低质量体验付费"
    core_hypothesis TEXT,
    evidence_summary TEXT,
    counterpoints TEXT,                      -- 反对方论点（避免单边叙事）
    platform_diff_json TEXT,                 -- 跨平台语境差异
    suggested_anchor_moments_json TEXT,      -- DiloFlow 友好：可作 anchor 的素材
    status TEXT NOT NULL DEFAULT 'candidate' CHECK (status IN
        ('seed',                     -- 刚从 signal promote 出
         'candidate',                -- 已写主张 + 至少一条 hypothesis
         'validating',               -- 在等更多 evidence
         'evidence_ready',           -- evidence 充足，可考虑做选题
         'promoted_to_diloflow',     -- 已导出给 DiloFlow
         'archived',                 -- 完成或时效过
         'rejected')),
    diloflow_export_path TEXT,               -- 导出到 DiloFlow 时的目标路径
    diloflow_episode_id TEXT,                -- 若已立项 EP，回写
    created_by TEXT NOT NULL DEFAULT 'user',
    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    updated_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now'))
);

CREATE INDEX idx_topic_cards_status ON topic_cards(status);
CREATE INDEX idx_topic_cards_signal ON topic_cards(signal_id);
```

### 2.5 topic_card_evidence 关系表

```sql
CREATE TABLE topic_card_evidence (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic_card_id TEXT NOT NULL REFERENCES topic_cards(id) ON DELETE CASCADE,
    capture_id TEXT REFERENCES captures(id) ON DELETE SET NULL,
    transcript_segment_id INTEGER REFERENCES transcript_segments(id) ON DELETE SET NULL,
    relation_type TEXT NOT NULL CHECK (relation_type IN
        ('supports',
         'contradicts',
         'example',
         'quote',
         'trend_signal',
         'platform_diff')),
    note TEXT,
    weight REAL,                              -- 这条证据的权重 0-1
    added_by TEXT NOT NULL DEFAULT 'user',
    added_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now'))
);

CREATE INDEX idx_tce_topic ON topic_card_evidence(topic_card_id);
CREATE INDEX idx_tce_capture ON topic_card_evidence(capture_id);
CREATE INDEX idx_tce_relation ON topic_card_evidence(relation_type);
```

---

## 3. State Machine 拆双轨

### 3.1 Signal Lifecycle（新增前置状态机）

```text
observed                            系统发现 / 用户标记
   ↓ user 在 Signal Workbench 打开
opened
   ↓ user 写假设
hypothesized
   ↓ user 进 Evidence Browser
browsing
   ↓ user 决定 scope（点 Scope Builder【保存】）
scope_decided
   ↓ Plan estimate 跑完
plan_ready
   ↓ user approve + 进 Capture Pipeline
capturing
   ↓ 全部 capture evidence_locked
evidence_locked
   ↓ user 在 Topic Card 编辑 + refine
refined

* → dismissed       任意阶段 user 主动放弃
```

### 3.2 Capture Plan Lifecycle

```text
draft → estimating → estimated → approved → running → completed
                          ↓                   ↓
                       canceled            canceled / failed
```

### 3.3 Capture Lifecycle（保留原 §6.3 不变）

原 PRD §6.3 的 17 状态 + 7 失败状态全部保留。Capture 现在是 capture_plan 的子产物，不再单独从 `discovered` 起头。

### 3.4 双轨衔接规则

- 一个 `capture_plan` 可以产生 N 个 `captures`（plan.scope.targets 数量）
- 每个 capture 仍走原 capture lifecycle
- plan.status='running' 时，至少有一个 capture 处于 lifecycle 中段
- 全部 captures 进入 `linked` 或终态 → plan.status='completed' → signal.status='evidence_locked'
- 任意 capture 不可恢复失败 → 不阻塞 plan 完成（只标 plan.warnings），除非 user 取消

### 3.5 quick_capture 的状态特殊处理

quick_capture 路径下：

- 不创建 signal（user 跳过了 signal 阶段）
- 不创建 capture_plan（绕过 Scope Builder）
- 直接创建 capture，从 `discovered` 起
- API 在 `captures.created_by_path` 字段标 `quick_capture`，便于审计区分

新增字段（修订原 captures 表）：

```sql
ALTER TABLE captures ADD COLUMN created_by_path TEXT NOT NULL DEFAULT 'capture_plan'
    CHECK (created_by_path IN ('capture_plan', 'quick_capture', 'manual_admin'));
ALTER TABLE captures ADD COLUMN capture_plan_id TEXT REFERENCES capture_plans(id);
CREATE INDEX idx_captures_plan ON captures(capture_plan_id);
CREATE INDEX idx_captures_path ON captures(created_by_path);
```

---

## 4. SQLite Schema 修订

### 4.1 修订总览

| 表 | 操作 |
|---|---|
| `signals` | 新增（§2.1） |
| `hypotheses` | 新增（§2.2） |
| `capture_plans` | 新增（§2.3） |
| `topic_cards` | 新增（§2.4） |
| `topic_card_evidence` | 新增（§2.5） |
| `artifact_versions` | 新增（§4.4） |
| `browsing_sessions` | 新增（§4.5） |
| `browsing_events` | 新增（§4.5） |
| `media_assets` | **改名 → `artifact_assets`**（§4.2） |
| `source_items.raw_metadata_json` | **拆 path + sha + excerpt**（§4.3） |
| `jobs` | 加 partial unique index（§4.6） |
| `captures` | 加 `created_by_path` + `capture_plan_id`（§3.5） |
| `recommendations.suggested_action` | 调整 enum（§7） |

新增表合计：8 张。

### 4.2 media_assets → artifact_assets

#### 4.2.1 改名理由

原 `media_assets.asset_type` 已经包含 `raw_response` / `page_snapshot` / `waveform` / `audio_segment`，超出 media 语义。Evidence Ledger 视角下，所有 6 区下的 file 都是 artifact，统一命名更准确。

#### 4.2.2 新表 DDL

```sql
DROP TABLE IF EXISTS media_assets;

CREATE TABLE artifact_assets (
    id TEXT PRIMARY KEY,                     -- ULID
    capture_id TEXT NOT NULL REFERENCES captures(id) ON DELETE CASCADE,
    artifact_zone TEXT NOT NULL CHECK (artifact_zone IN
        ('bundle', 'media', 'transcript', 'normalized', 'links', 'logs')),
    artifact_kind TEXT NOT NULL,             -- 比 zone 细一级
    file_path TEXT NOT NULL,                 -- 相对项目根
    mime_type TEXT,
    size_bytes INTEGER,
    sha256 TEXT,
    duration_seconds REAL,
    width INTEGER,
    height INTEGER,
    bitrate INTEGER,
    sample_rate INTEGER,
    channels INTEGER,
    producer_job_id TEXT REFERENCES jobs(id),
    is_raw_evidence INTEGER NOT NULL DEFAULT 0,    -- bundle/raw-* 必为 1
    is_active INTEGER NOT NULL DEFAULT 1,          -- 是否当前 active 版本
    metadata_json TEXT,
    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    UNIQUE(capture_id, file_path)
);

CREATE INDEX idx_artifacts_capture ON artifact_assets(capture_id);
CREATE INDEX idx_artifacts_zone ON artifact_assets(artifact_zone);
CREATE INDEX idx_artifacts_active ON artifact_assets(capture_id, artifact_zone, is_active);
CREATE INDEX idx_artifacts_raw ON artifact_assets(capture_id, is_raw_evidence) WHERE is_raw_evidence = 1;
```

#### 4.2.3 artifact_kind 枚举（按 zone 列）

| zone | kind |
|---|---|
| bundle | `raw_api_response` / `source_page_snapshot_html` / `source_page_snapshot_png` / `capture_manifest` / `xhs_note_detail` |
| media | `video` / `audio` / `thumbnail` / `subtitle_native` / `danmaku` / `image_original` / `preview` / `waveform` / `audio_segment` |
| transcript | `raw` / `segments` / `reviewed` |
| normalized | `summary` / `claims` / `quotes` / `topic_candidates` / `structured` / `comments_summary` / `ocr` / `image_captions` |
| links | `raw_suggestions` / `obsidian_suggestions` / `knowledge_edges` |
| logs | `job_log` / `receipt` / `stderr` |

#### 4.2.4 迁移策略

- 新建 `migrations/004_rename_media_to_artifact.sql`
- 数据迁移：`INSERT INTO artifact_assets (...) SELECT ... FROM media_assets;`
- 应用层全部 import 改名：`MediaAsset` → `ArtifactAsset`
- API 路径同步改：`GET /captures/{id}/assets`（路径不变，response schema 字段重命名）

### 4.3 source_items.raw_metadata_json 拆分

#### 4.3.1 原状（违反"大对象 vs 小对象边界"）

```sql
-- 原 PRD §7.5.4
raw_metadata_json TEXT,                 -- 完整 raw 平台响应（也存 FS 副本）
```

完整 raw response 双存（DB + FS）有一致性风险，且 DB 体积膨胀快。

#### 4.3.2 新版

```sql
-- 替换为
raw_metadata_path TEXT,                 -- 'data/artifacts/<platform>/<capture_id>/bundle/raw-api-response.json'
                                        -- 仅当 source_item 已转化为 capture 时填
raw_metadata_sha256 TEXT,               -- evidence 防篡改
metadata_excerpt_json TEXT,             -- 索引摘要（≤4KB），用于 Source Radar 卡片渲染
```

`metadata_excerpt_json` 内容（必有字段）：

```json
{
  "platform": "bilibili",
  "title": "...",
  "creator_name": "...",
  "duration_seconds": 845,
  "published_at": "...",
  "thumbnail_url": "...",
  "engagement_summary": {"views": 12345, "likes": 678, "comments": 45},
  "first_3_tags": ["..."],
  "snippet": "前 200 字描述"
}
```

不存：完整 description / 完整 tag list / 完整推荐 metadata（这些进 FS）。

#### 4.3.3 迁移

- 现存 `source_items.raw_metadata_json` 数据：写入 `bundle/raw-api-response.json`（如对应 capture 已存在），DB 字段移除
- migration 003 完成后 schema 更新

### 4.4 artifact_versions 表（应对 Evidence Ledger 历史）

#### 4.4.1 设计目标

raw evidence 一旦写入不可覆盖；derived artifact 可重算，但必须保留版本历史。

#### 4.4.2 FS 子目录约定（不新增 7 区，仅在 6 区内加 `versions/`）

```text
transcript/
  raw.json                              # 当前 active 版本（symlink 或 copy）
  reviewed.json
  versions/
    {producer_job_id}.raw.json          # 历史版本
    {producer_job_id}.reviewed.json
normalized/
  structured.md                          # 当前 active 版本
  summary.md
  claims.jsonl
  quotes.jsonl
  topic-candidates.jsonl
  versions/
    {producer_job_id}.structured.md     # 历史版本
    {producer_job_id}.summary.md
    ...
```

bundle / 区永远不允许 versions/（raw evidence 不可变）。
media / 区一般不变（重新下载会替换 active），但保留 `media/versions/` 给 user 主动 force 重下时使用。
links / logs 不需要 versions（links 是 derived，每次重生成；logs 是 append-only 已经天然保留历史）。

#### 4.4.3 DDL

```sql
CREATE TABLE artifact_versions (
    id TEXT PRIMARY KEY,                     -- ULID
    capture_id TEXT NOT NULL REFERENCES captures(id) ON DELETE CASCADE,
    artifact_zone TEXT NOT NULL,             -- 'transcript' / 'normalized' / 'media'
    artifact_kind TEXT NOT NULL,             -- 'raw' / 'structured' / 'summary' 等
    active_path TEXT NOT NULL,               -- 'transcript/raw.json'
    version_path TEXT NOT NULL,              -- 'transcript/versions/{job_id}.raw.json'
    producer_job_id TEXT REFERENCES jobs(id),
    sha256 TEXT,
    is_active INTEGER NOT NULL DEFAULT 0,    -- 该 zone+kind 的当前 active 是否 = 本行
    superseded_at TEXT,                      -- 被新版本替代的时间（is_active 转 0 时）
    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now'))
);

CREATE INDEX idx_av_capture ON artifact_versions(capture_id, artifact_zone, artifact_kind);
CREATE INDEX idx_av_active ON artifact_versions(capture_id, artifact_zone, artifact_kind, is_active)
    WHERE is_active = 1;
```

#### 4.4.4 worker 写规则

新原则（继承原 §5.9 worker 隔离规则）：

> **任何 derived artifact 重算必须**：
> 1. 先把 active 文件 rename 到 `versions/{producer_job_id}.<file>`
> 2. 写新 active 文件
> 3. UPDATE artifact_versions：旧版 is_active=0，新版 is_active=1
> 4. 写 capture_state_history audit 一行

worker 不允许直接 `open(active_path, 'w')` 覆盖。

### 4.5 browsing_sessions / browsing_events 表

#### 4.5.1 目的

Evidence Browser 浏览行为入账（不创建 capture，但保留谱系）。

#### 4.5.2 DDL

```sql
CREATE TABLE browsing_sessions (
    id TEXT PRIMARY KEY,                     -- ULID
    signal_id TEXT REFERENCES signals(id) ON DELETE SET NULL,
    started_by TEXT NOT NULL DEFAULT 'user',
    started_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    ended_at TEXT,
    note TEXT
);

CREATE INDEX idx_bs_signal ON browsing_sessions(signal_id);

CREATE TABLE browsing_events (
    id TEXT PRIMARY KEY,                     -- ULID
    session_id TEXT NOT NULL REFERENCES browsing_sessions(id) ON DELETE CASCADE,
    url TEXT NOT NULL,
    platform TEXT,
    event_type TEXT NOT NULL CHECK (event_type IN
        ('open_url',                         -- user 打开 URL（外部浏览器或内嵌）
         'view_metadata',                    -- 看 metadata preview
         'copy_url',                         -- 把 URL 复制到 Scope Builder
         'note_added',                       -- 在 Brainstorm Notes 加一条
         'scope_action_clicked',             -- 点 Scope Builder 任意按钮
         'external_browser_opened',          -- 系统浏览器打开
         'screenshot_captured',              -- 截图
         'comments_previewed')),             -- 看了评论预览（不抓）
    note TEXT,
    payload_json TEXT,
    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now'))
);

CREATE INDEX idx_be_session ON browsing_events(session_id, created_at);
CREATE INDEX idx_be_type ON browsing_events(event_type);
```

### 4.6 jobs 幂等约束加固

#### 4.6.1 原约束（不够硬）

```sql
UNIQUE(capture_id, job_type, queued_at)   -- 不同 queued_at 即可重复入队
```

#### 4.6.2 新增 partial unique index

```sql
CREATE UNIQUE INDEX idx_jobs_one_active_per_type
ON jobs(capture_id, job_type)
WHERE status IN ('queued', 'running');
```

#### 4.6.3 含义

- 同一 capture 同一 job_type 任意时刻**最多 1 个 active job**（queued 或 running）
- 重跑：旧 job 必须先转 `succeeded` / `failed` / `canceled`，新 job 才能 queued
- 并发执行同 worker 类型同一 capture 物理不可能

#### 4.6.4 API enforcement

`POST /captures/{id}/jobs/{type}` 收到请求时：
- 若已有 active job → 返 409 + 既有 job_id
- 若旧 job 是 succeeded → 返 409 + "use POST /jobs/{id}/retry to re-run"
- 若旧 job 是 failed / canceled → 创建新 job

---

## 5. Thin API 扩展

新增约 28 路由。原 §8.3 路由表全部保留，本节仅列新增。

### 5.1 Signals 路由

```text
GET    /signals                          列出（filter: status, signal_type, since, score_gte）
POST   /signals                          系统或 user 创建 signal
GET    /signals/{id}                     详情（含关联 hypotheses + capture_plans + topic_card）
PATCH  /signals/{id}                     修改 title / summary / status
POST   /signals/{id}/open                user 打开 signal（status observed → opened）
POST   /signals/{id}/dismiss             放弃
POST   /signals/{id}/promote-to-topic    promote 为 topic_card
GET    /signals/{id}/timeline            该 signal 的全部生命周期事件
```

### 5.2 Hypotheses 路由

```text
GET    /signals/{id}/hypotheses          列出该 signal 的假设
POST   /signals/{id}/hypotheses          新增一条假设
PATCH  /hypotheses/{id}                  修改假设文本 / confidence
POST   /hypotheses/{id}/validate         user 标 validated（基于已有 evidence）
POST   /hypotheses/{id}/weaken           标 weakened
POST   /hypotheses/{id}/reject           标 rejected
```

### 5.3 Capture Plans 路由

```text
GET    /capture-plans                    列出（filter: status, signal_id, hypothesis_id）
POST   /capture-plans                    创建（draft 状态，scope_json + budget_json 必填）
GET    /capture-plans/{id}               详情
PATCH  /capture-plans/{id}               修改 scope / budget（仅 draft / estimated 状态）
POST   /capture-plans/{id}/estimate      触发估算（异步，写 estimate_json）
POST   /capture-plans/{id}/approve       user approve（前置：estimate 完成 + budget 未超）
POST   /capture-plans/{id}/run           启动 capture pipeline（前置：approved）
POST   /capture-plans/{id}/cancel        取消（任意阶段）
GET    /capture-plans/{id}/captures      该 plan 产生的所有 captures
GET    /capture-plans/{id}/progress      运行进度（已完成 / 总数 / 各 capture 状态）
```

### 5.4 Topic Cards 路由

```text
GET    /topic-cards                      列出（filter: status, since）
POST   /topic-cards                      手动创建
GET    /topic-cards/{id}                 详情（含 evidence list）
PATCH  /topic-cards/{id}                 修改 title / hypothesis / counterpoints
POST   /topic-cards/{id}/evidence        加一条 evidence link
DELETE /topic-cards/{id}/evidence/{eid}  删一条
POST   /topic-cards/{id}/promote         promote_to_diloflow（生成导出包）
GET    /topic-cards/{id}/export          导出 markdown bundle
```

### 5.5 Browsing Sessions 路由

```text
POST   /browsing-sessions                开启 session（带 signal_id）
PATCH  /browsing-sessions/{id}/end       结束 session
POST   /browsing-sessions/{id}/events    添加事件
GET    /browsing-sessions/{id}           session 详情 + events 列表
GET    /signals/{id}/browsing-sessions   某 signal 的所有 session 历史
```

### 5.6 Recommendation 路由调整

`PATCH /recommendations/{id}/accept` 行为修订：

- **旧行为**：直接创建 capture
- **新行为**：根据 `recommendations.suggested_action`：
  - `open_scope` → 创建 signal + 跳转到 Signal Workbench
  - `verify_signal` → 同 open_scope
  - `quick_capture` → 校验 LP-001 §1.2 条件，满足则创建 capture，不满足则 reject + 改 open_scope
  - 其他 → 拒绝（API 返 422）

### 5.7 LP-001 enforcement 路由

```text
POST   /captures/discover                旧路径，行为修订：
                                          - 若 source = recommendation 且无 capture_plan_id → 422
                                          - 若 source = manual_url + meets quick_capture conditions → 创建
                                          - 若 source = capture_plan → 创建（plan 必须 approved）
```

### 5.8 完整 API 路由清单（v1.1 总和）

原 PRD §8.3 路由 + 本 amendment §5.1-§5.7 新增 = 总计约 76 个端点。完整路由表见 `docs/specs/api-routes-v1.1.md`（待 Codex 整理）。

---

## 6. UI IA 修订

### 6.1 总览改动

| 原 PRD §10 | amendment v1.1 |
|---|---|
| Source Radar | **Signal Radar**（改名） |
| Source Radar 详情态 = 卡片打开 | **Signal Workbench**（三栏工作区，详见 §6.2） |
| Source Radar 卡片操作 = `[采集 audio][仅 metadata][忽略]` | **`[打开 Scope][验证信号][稍后看][忽略]`** |
| 9 页面（含 Source Radar） | 9 页面（Source Radar → Signal Radar；新增 Signal Workbench 作为详情态，不算独立页） |

### 6.2 Signal Workbench 三栏布局

Signal Workbench 是 Signal Radar 卡片打开后的详情工作区。三栏：

```text
╔══════════════════════════════════════════════════════════════════════════════╗
║  Signal Workbench: <signal title>                            [关闭][归档]      ║
╠═══════════════════════════╦═════════════════════════╦══════════════════════════╣
║                           ║                          ║                            ║
║  左栏 Signal Board        ║  中栏 Signal Brief       ║  右栏 Evidence Workspace   ║
║  ─────────────────────    ║  ─────────────────────  ║  ──────────────────────    ║
║                           ║                          ║                            ║
║  其他 signal 列表（按状态）║  Signal Title           ║  Evidence Browser (60%)    ║
║  • observed  (12)         ║  Summary                 ║  ┌────────────────────┐   ║
║  • opened    (3)          ║  Origin: source_item     ║  │ 原始页面 metadata    │   ║
║  • hypothesized (5)       ║  Score: 0.78             ║  │ thumbnail/截图       │   ║
║  • browsing  (1)          ║  ─────                   ║  │ engagement summary  │   ║
║  • plan_ready (2)         ║  Hypothesis (user)       ║  │                     │   ║
║  • capturing (1)          ║  • "这是消费降级体验焦虑" ║  │ [打开原始页]         │   ║
║  ─────                    ║    confidence 0.7        ║  │ [开 browsing session]│   ║
║  快速过滤                 ║  [+ 新假设]              ║  └────────────────────┘   ║
║                           ║                          ║                            ║
║  当前 signal 高亮          ║  Related Signals        ║  Brainstorm Notes (30%)    ║
║                           ║  • 同主题多源命中        ║  ┌────────────────────┐   ║
║                           ║  • RAW gap: 用户洞察     ║  │ 我即时假设...        │   ║
║                           ║                          ║  │ 我想验证...          │   ║
║                           ║  Topic Card link         ║  │ 担心是不是标题党...  │   ║
║                           ║  → tc_xxx (validating)   ║  │                     │   ║
║                           ║                          ║  │ [生成 Capture Scope]│   ║
║                           ║                          ║  └────────────────────┘   ║
║                           ║                          ║                            ║
║                           ║                          ║  Scope Builder (展开式)     ║
║                           ║                          ║  ┌────────────────────┐   ║
║                           ║                          ║  │ targets: [+]        │   ║
║                           ║                          ║  │ budget: ...          │   ║
║                           ║                          ║  │ [Estimate][Approve] │   ║
║                           ║                          ║  └────────────────────┘   ║
╚═══════════════════════════╩═════════════════════════╩══════════════════════════╝
```

### 6.3 三栏交互规则

#### 6.3.1 左栏 Signal Board

- 显示该 user 当前所有 signals（按 status 分组）
- 点任意 signal 切换中栏 / 右栏内容
- 不在左栏直接操作（不允许左栏直接 dismiss / approve）

#### 6.3.2 中栏 Signal Brief + Hypothesis

- Signal Title / Summary / Score / 系统给的 reason
- Hypothesis 列表（多条），每条可编辑 / 标 confidence
- Related Signals（多源聚合 / RAW gap 反向触发）
- 关联 Topic Card link（已 promote 时）
- 不在中栏直接 capture（必须先去右栏 Scope Builder）

#### 6.3.3 右栏 Evidence Workspace（60% / 30% / 10% 弹性）

##### 6.3.3.1 Evidence Browser（默认 60%）

- Phase 1：metadata preview + thumbnail + engagement summary + 评论数预估（不抓评论本身）
- 顶部 URL bar（不可编辑，但可复制）
- 操作按钮：
  - `[打开原始页]` — 系统浏览器打开
  - `[开 browsing session]` — 进入审计模式（之后所有点击留痕）
  - `[加入 Capture Scope]` — 加到右下 Scope Builder
- **Phase 1 不承诺 iframe 真内嵌**（详见 §11）

##### 6.3.3.2 Brainstorm Notes（默认 30%，常驻不可隐藏）

- 自由文本，markdown
- 自动绑定到当前 signal_id（保存 = POST /signals/{id}/hypotheses 或 PATCH note）
- 顶部按钮：`[生成 Capture Scope]` — 用 LLM 把 notes 转 scope_json 草稿
- 关键 UX：**不能被 hide / minimized**（user 浏览时假设容易消失，必须常驻）

##### 6.3.3.3 Scope Builder（展开式，10% 默认折叠）

- 点 `[加入 Capture Scope]` 时展开
- 表单 + 预算面板（详见 §8）
- 三档按钮：`[Estimate]` → `[Approve]` → `[Run]`

### 6.4 Source Radar 卡片操作改动

#### 6.4.1 新版卡片

```text
┌─────────────────────────────────────┐
│ [Bilibili] 影视飓风                   │
│ AI 工具实测：哪个最好用                 │
│ ⏱ 14:25  📅 4-29  💯 0.86            │
│ 理由：与 RAW『AI Agent 选型』高度相关  │
│ 命中：账号订阅 + 关键词命中            │
│                                       │
│ 操作：[打开 Scope] [验证信号]          │
│       [稍后看]    [忽略]              │
│                                       │
│ ⓘ 单条 URL 可以快速采集（quick）       │
│   [快速采: 仅 metadata]               │
│   [快速采: audio + transcript]         │
└─────────────────────────────────────┘
```

#### 6.4.2 行为差异

- **`[打开 Scope]`**：进入 Signal Workbench（创建 signal if not exists）
- **`[验证信号]`**：等价于 `[打开 Scope]` + 自动开 browsing session
- **`[稍后看]`**：标 status='watchlist'，进 watchlist 视图
- **`[忽略]`**：标 status='ignored'，3 天后从默认视图消失
- **`[快速采: ...]`**：仅在 LP-001 §1.2 条件全满足时渲染（来源是 manual URL / 单条 / 不抓扩展），其他情况不显示

### 6.5 Mission Control 加 Decision Dock 新条目

原 §10.3.2 Decision Dock 加：

- `[plan_ready]` — capture_plan 已 estimate 完成等 user approve
- `[needs_scope]` — signal 已 hypothesized 但未进 Scope Builder（提醒 user 不要堆积）
- `[topic_validating]` — topic_card 在 validating 但 evidence 不够

### 6.6 Capture Pipeline 页修订

- 顶部加"按 plan 分组"切换：默认按 plan 分组（plan_id → 多 capture），可切回按 capture 平铺
- 每个 plan 显示：进度（已完成 / 总数）/ 当前阶段 / 预估剩余时间
- plan 失败超阈值 → 红色边框 + `[查看失败]` `[取消剩余]` 按钮

### 6.7 新增 Topic Card 页面（10.5 后插入）

实际是 Library 内的 sub-tab：

```text
Library
├── Captures（原内容）
└── Topic Cards（新增 sub-tab）
    ├── seed
    ├── candidate
    ├── validating
    ├── evidence_ready
    └── promoted_to_diloflow
```

不增加顶级 nav 项，Topic Cards 作为 Library 的"成品输出"层。

---

## 7. Recommendation 修订

### 7.1 suggested_action enum 调整

#### 7.1.1 原 enum

```sql
suggested_action TEXT CHECK (suggested_action IN
    ('capture', 'watch', 'ignore', 'topic_seed', 'script_material'))
```

#### 7.1.2 新 enum

```sql
suggested_action TEXT CHECK (suggested_action IN
    ('open_scope',          -- 默认，进 Signal Workbench
     'verify_signal',       -- 等价 open_scope + 开 browsing session
     'watch',               -- 加入 watchlist
     'ignore',
     'topic_seed',          -- 直接 promote 为 topic_card seed
     'script_material',     -- 标记为 DiloFlow 台本素材候选
     'quick_capture'))      -- 仅在满足 LP-001 §1.2 条件时
```

`'capture'` 值 **废止**（旧数据迁移时统一改为 `'open_scope'`）。

### 7.2 默认推荐策略（推荐流入口）

| 信号来源 | 默认 suggested_action |
|---|---|
| 账号订阅命中 | `open_scope` |
| 关键词命中 | `open_scope` |
| 多源聚类 | `verify_signal` |
| RAW gap 反推 | `verify_signal` |
| 单条 manual URL（在 Explore 页） | `quick_capture`（如条件满足） / `open_scope`（否则） |
| 列表批量导入 | `open_scope`（不允许批量直接 capture） |

### 7.3 quick_capture 在推荐流的可见性

仅在以下情况，Source Radar 卡片显示 `[快速采: ...]` 按钮：

- `recommendations.suggested_action='quick_capture'`
- 且 source 类型 = `link`（单条链接）
- 且 estimate 可静态算出（无关键词扩展 / 无作者扩展）

其他情况一律不显示快速采按钮。

---

## 8. Capture Plan estimate / approve / run 三段式（硬门）

### 8.1 LP-002（lock）

> **任何 Capture Plan 在执行前必须完成 estimate**；未估算或估算超 budget，不允许进入 `running`。worker 不允许在没有 plan_id 的情况下创建 capture（除 quick_capture 路径）。

### 8.2 estimate worker 实现

新增 worker：`workers/plan_estimator/`。

输入：`capture_plan.scope_json` + `budget_json`
输出：`capture_plan.estimate_json`

估算逻辑：

```text
for each target in scope.targets:
    if target_type = single_video / single_note:
        items_count += 1
        media_size_mb += estimate_media_size(platform, duration)
        asr_minutes += estimate_audio_duration(platform, duration)
    elif target_type = creator_recent:
        items_count += target.limit
        media_size_mb += target.limit × avg_video_size
        ...
    elif target_type = keyword:
        items_count += target.limit
        ...
    elif actions includes 'top_comments':
        comment_count += min(target.limit, budget.max_comment_count) × 20
    elif actions includes 'ocr':
        ocr_image_count += target.limit × avg_images_per_note
        llm_tokens += ocr_image_count × 500

estimate.duration_minutes = (
    items_count × source_fetch_avg
    + media_size_mb / download_throughput
    + asr_minutes × asr_speed_factor
    + llm_tokens / llm_throughput
)

estimate.cost_usd = sum(llm_token_cost × tokens)
```

risk_factors 规则：
- xhs target 数 > 5 → +`xhs_high_rate_limit_risk`
- 总 asr_minutes > 60 → +`long_asr_load`
- comment_count 估算 > 200 → +`comment_volume_high`

### 8.3 approve gate

`POST /capture-plans/{id}/approve` 校验：

- `plan.status = 'estimated'`（必须先 estimate）
- `plan.estimate_json.items_count <= plan.budget_json.max_items`
- `plan.estimate_json.media_size_mb <= plan.budget_json.max_media_mb`
- `plan.estimate_json.asr_minutes <= plan.budget_json.max_asr_minutes`
- `plan.estimate_json.llm_tokens <= plan.budget_json.max_llm_tokens`
- `plan.estimate_json.comment_count <= plan.budget_json.max_comment_count`

任一超阈值 → 返 422 + `{超过的字段, 实际值, 预算值}`。user 必须先：
- 修改 scope（缩小 limit / 删 target）
- 修改 budget（提高阈值，但提高 budget 必须留 audit 记录）

### 8.4 run gate

`POST /capture-plans/{id}/run` 校验：

- `plan.status = 'approved'`
- 当前**正在 running 的 plans 总数 < 系统并发上限**（默认 3）
- 当前 hour 内已 run 的 plans 数 < 阈值（防爆冲）

满足 → status 转 `running` + 给 plan.scope.targets 每个创建 capture + 每个 capture 入对应 worker 队列。

### 8.5 plan 进度反馈

`GET /capture-plans/{id}/progress`：

```json
{
  "plan_id": "01HX...",
  "status": "running",
  "captures_total": 14,
  "captures_done": 8,
  "captures_failed": 1,
  "captures_in_progress": 5,
  "current_stages": {
    "metadata_fetched": 1,
    "media_downloading": 2,
    "transcribing": 1,
    "normalizing": 1
  },
  "estimated_remaining_minutes": 12,
  "cost_so_far_usd": 0.18,
  "warnings": ["1 capture failed: xhs_rate_limit"]
}
```

---

## 9. Multi-agent 治理 — merger-of-record 模型

### 9.1 LP-003（lock）— 合并仲裁权重写

> **不再"谁先 review 谁优先"。每类变更有 merger-of-record。**

### 9.2 merger-of-record 表

| 变更类型 | 默认 merger | 必经审 | 是否需 user 拍板 |
|---|---|---|---|
| 代码 patch（worker / API / Console） | **Codex** | Opus 可 audit | 否 |
| schema / state words / FS layout | **Codex review + Opus review** | 必双签 | **是** |
| PRD 文字 / 产品叙事 / IA 设计 | **Opus draft + Codex sanity check** | 必双签 | **是** |
| worker 实现细节（不动 contract） | **Codex** | Opus 可 audit | 否 |
| 安全合规边界（§14） | Codex + Opus | 双签 | **是** |
| 多 agent SOP 改动 | Codex + Opus | 双签 | **是** |
| migration 文件 | **Codex** | Opus audit schema 一致性 | 仅当涉及 lock 项 |
| candidate review 流程 | Codex | Opus audit | 否 |
| Phase 范围调整 | Opus + Codex | 双签 | **是** |

### 9.3 角色权限重写

| Agent | 权限 |
|---|---|
| user | final arbiter / showrunner / 任意写入 / 任意拒决 |
| **Codex** | **merger-of-record（代码 / schema / migration / worker）** + auditor |
| **Opus** | **PRD 主笔 / 架构纠偏 / IA 设计** + auditor |
| Hermes | scheduler + signal generator（写 signals 表）+ candidate（不直接改主线） |
| OpenClaw | scheduler + secondary scout + candidate |
| ChatGPT Pro | research candidate（offline 文件） |

### 9.4 冲突解决流程

Codex 和 Opus 对同一变更分歧时：

1. 双方各写一份 candidate（不互改对方文件）
2. 由 user 在 Agent Dispatch 页比较 + 拍板
3. 拍板结果写 decisions.md amendment
4. **不允许"谁先合并谁赢"**

### 9.5 candidate 24h 默认转 needs_user 规则保留

但额外补：

- candidate 涉及 lock 项 → 跳过 24h 等待，立即转 needs_user
- candidate 修订 PRD 三章以上 → 立即 needs_user
- candidate 是 schema breaking change → 立即 needs_user

---

## 10. Phase 1 拆为 1A / 1B

### 10.1 原 Phase 1（拆分前）

```text
B 站 URL → metadata → media → audio → ASR → postprocess → normalize
        → index → raw-linker → linked
```

太重，被 RAW bridge 拖住。

### 10.2 新 Phase 1A — B 站单条文案库闭环

#### 10.2.1 范围

```text
B 站 URL（quick_capture 路径）
   → metadata
   → audio
   → ASR (faster-whisper)
   → asr-postprocess
   → normalize (claude-sonnet)
   → SQLite 入库 + FTS 索引
   → Library 可搜索
```

#### 10.2.2 Deliverables

```text
✅ workers/bili/                 metadata + audio download
✅ workers/asr/                  faster-whisper
✅ workers/asr_postprocess/
✅ workers/normalize/            claude-sonnet 默认
✅ workers/index/                FTS5 索引
✅ services/api/ Phase 1A 路由全开
✅ Console: Capture Pipeline 真实 + Library 检索
```

#### 10.2.3 验收（Phase 1A pass 条件）

- [ ] 单 B 站 URL（user 在 Explore 粘贴）→ Library 可检索 < 20 min
- [ ] Library FTS 检索 < 200ms
- [ ] capture lifecycle 走完 indexed（不要求 linked）
- [ ] FS layout 完全符合 §5（含 versions/）
- [ ] artifact_assets 表数据正确（每个文件登记）

#### 10.2.4 不在 Phase 1A 内

- raw-linker（RAW patch 生成）
- knowledge_links 表填充
- Capture Plan / Signal Workbench（这些 Phase 2 启用）
- 小红书任何采集（Phase 2）
- Hermes 定时调度（Phase 3）

### 10.3 新 Phase 1B — RAW Link stub

#### 10.3.1 范围

```text
normalized.md（Phase 1A 已完成）
   → raw-linker worker
   → 生成 raw-suggestions.jsonl（不要求真合并到 RAW）
   → UI 显示 suggestion list
   → user 手动 accept 写到 ~/raw/inbox/scoutflow/
```

#### 10.3.2 Deliverables

```text
✅ workers/raw_linker/           LLM 提取 + RAW node 匹配（基础版）
✅ Knowledge Bridge UI（基础展示，不要求 reverse discovery）
✅ raw inbox 写入逻辑
```

#### 10.3.3 验收（Phase 1B pass 条件）

- [ ] 任意 capture 在 indexed 后能生成 ≥1 条 raw-suggestion
- [ ] suggestion 包含原文片段 + 目标 RAW node 路径建议 + relation_type
- [ ] user accept 后 patch 文件写到 RAW inbox（格式见原 PRD §12.4）
- [ ] knowledge_links.status='accepted' 入库

#### 10.3.4 不在 Phase 1B 内

- Reverse discovery（RAW gap → 触发探索）
- Topic card promotion
- Obsidian inbox（仅 RAW）

### 10.4 后续 Phase 调整

| Phase | 原范围 | 新范围 |
|---|---|---|
| Phase 2 | 文案库 + RAW 关联 | **Capture Plan / Signal Workbench / Topic Card 三段式启用** + 小红书 metadata 采集 + Reverse Discovery |
| Phase 3 | 主动推荐 | 不变（Hermes 定时扫描 + Recommender + Reranker） |
| Phase 4 | 多 agent 治理 | 不变 |

### 10.5 Phase 2 的关键 deliverables（从 Phase 1 平移过来 + 新增）

```text
✅ signals / hypotheses / capture_plans / topic_cards 表 + API
✅ Signal Workbench 三栏 UI
✅ Scope Builder + estimate worker
✅ Browsing Session 入账
✅ XHS metadata + 笔记正文 + 图片原图（不抓评论 / 楼中楼）
✅ Reverse Discovery
✅ artifact_versions 完整启用
```

---

## 11. Evidence Browser 三档实现路径

### 11.1 LP-004（lock）

> **Phase 1 / 1A / 1B 不承诺 iframe 真内嵌。**
> Phase 2 启用 metadata preview + 系统浏览器 + scope builder 组合。
> Phase 3+ 才考虑 Tauri / Electron WebView / Chrome DevTools Protocol。

### 11.2 三档详细

| 档 | 实现 | 启用 phase |
|---|---|---|
| 档 1 | 视觉 mock（Evidence Browser 是假窗口，展示 mock 截图 / metadata） | Phase 0 |
| 档 2 | 真实但保守（metadata preview + 系统浏览器 open + screenshot 静态展示 + scope builder） | Phase 2 |
| 档 3 | 真嵌入（Tauri WebView / Electron / Chrome DevTools） | Phase 3+ |

### 11.3 档 2 的 metadata preview 必有字段

- 平台 logo + canonical URL
- title + creator name + handle
- thumbnail（高清，从 bundle/raw fetch）
- engagement summary（views / likes / comments count，**评论本身不抓**）
- duration / publish time
- 平台原生字幕状态（"字幕已就绪 / 字幕缺失 / 字幕需付费"）
- 评论氛围简略（**仅评论数 + 评论密度，不抓评论文本**）

### 11.4 Evidence Browser 不做的事

- ❌ 不在 ScoutFlow 内嵌登录页
- ❌ 不存登录 cookie 到 ScoutFlow（cookie 只在 source-adapter 层使用）
- ❌ 不做 reader mode（不重排平台 HTML）
- ❌ 不做评论原文展示（评论必须走 Capture Plan + Scope）

### 11.5 系统浏览器衔接

- `[打开原始页]` 调用 macOS `open` 命令打开默认浏览器
- 打开后 user 在浏览器看，看完回 ScoutFlow（不需要回流通信）
- ScoutFlow 在 user 回 tab 时显示提示："你刚浏览了 X，要不要加入 Capture Scope？"

### 11.6 Browsing Session enforcement

任何 Evidence Browser 内的点击或外部浏览器打开行为，必须先开 browsing_session：

- 进 Signal Workbench → 自动开 session（关联当前 signal_id）
- 离开 Signal Workbench → 自动 end session
- session 内所有 events 入 browsing_events 表

---

## 12. 命名禁区扩展（LP-005）

### 12.1 LP-005（lock）— 命名禁区扩展

原 PRD §6.8 禁用词（done / processing / error / pending / complete / success / ok）保留。**新增**：

| 禁用词 | 替代 | 理由 |
|---|---|---|
| `crawl` / `crawler` / `crawling` | `source scan` / `metadata fetch` / `evidence collect` | 诱导往"全网爬虫"走 |
| `spider` / `spidering` | `source scan` | 同上 |
| `scrape_all` / `scrape_everything` | `capture_with_scope` | 默认全抓违反 LP-001 |
| `auto_capture` | `quick_capture`（在限定条件下）/ `scope_then_capture` | 模糊 vs 精确 |
| `bulk_download` | `capture_plan` 内有 `bulk` target | 同上 |
| `harvest` / `harvesting` | `evidence_collect` | 同 crawl |

### 12.2 任何 PR / spec / PRD 修订出现禁用词必须 reject

代码层：
- worker 类名不能叫 `XHSCrawler` / `BiliSpider`
- 路径不能叫 `services/crawler/`
- log 不能写 "crawling 5 items"

---

## 13. 安全合规增补（基于 LP-001）

### 13.1 XHS Phase 1 进一步降级

原 PRD §14.1 已经规定 XHS 只读 + 低频。本 amendment 增补：

| 能力 | Phase 1 | Phase 2 | Phase 3+ |
|---|---|---|---|
| metadata + 笔记 URL 探针 | ✅ | ✅ | ✅ |
| 笔记正文（图文） | ❌ | ✅ | ✅ |
| 图片原图 | ❌ | ✅ | ✅ |
| 图片 OCR | ❌ | ✅ | ✅ |
| 评论 metadata（仅数量） | ✅（在 Evidence Browser 显示数） | ✅ | ✅ |
| 评论原文（高赞 Top N） | ❌ | ❌ | **✅（必须 Scope 明确确认）** |
| 评论楼中楼 | ❌ | ❌ | **✅（必须 Scope + 显式 depth）** |
| 视频笔记的视频本体 | ❌ | ❌ | **✅（仅 quick_capture 单条 + 显式确认）** |
| 视频笔记的字幕 / ASR | ❌ | ❌ | ✅ |

### 13.2 Scope Builder 评论默认 off

```text
评论选项（在 Scope Builder 内，默认全部 unchecked）：
[ ] 抓评论（高赞 Top N）
[ ] 抓楼中楼

展开后强制显示：
预计评论数：50
最大楼层深度：1
最大请求页数：3
```

任意 checkbox 勾选 → 必须配套填 limit。

### 13.3 评论文件位置（Scope 一旦允许）

```text
data/artifacts/<platform>/<capture_id>/
  bundle/raw/
    comments-page-001.json         (raw evidence, 不可变)
    comments-page-002.json
  normalized/
    comments-summary.md             (LLM 总结)
```

### 13.4 图片 / OCR 文件位置（XHS Phase 2）

```text
data/artifacts/xhs/<capture_id>/
  media/images/
    image_001.jpg                   (原图，is_raw_evidence=1)
    image_002.jpg
  normalized/
    ocr.jsonl                       (OCR 结果，可重算)
    image-captions.jsonl
```

不增加第 7 个 FS 区。images 进 media/，OCR 派生进 normalized/。

---

## 14. Decision Lock 增补（D022 - D033）

### 14.1 新增 Locked Principles

| ID | Principle | 来源 |
|---|---|---|
| **LP-001** | Capture Scope Gate（推荐 / 关键词 / RAW gap 不直接采集） | §1 |
| **LP-002** | Capture Plan estimate → approve → run 三段式 | §8 |
| **LP-003** | merger-of-record 模型（不"谁先 review 谁优先"） | §9 |
| **LP-004** | Evidence Browser 三档实现路径（Phase 1 不真内嵌） | §11 |
| **LP-005** | 命名禁区扩展（crawl / spider / scrape_all / harvest 等） | §12 |

### 14.2 新增 Decision Locks

| ID | 决策 | 锁定章节 | 锁定日期 |
|---|---|---|---|
| **D022** | Capture Scope Gate 原则（LP-001） | §1 | 2026-05-02 |
| **D023** | 4 前置实体（signals / hypotheses / capture_plans / topic_cards） | §2 | 2026-05-02 |
| **D024** | State Machine 拆双轨（Signal Lifecycle + Capture Lifecycle） | §3 | 2026-05-02 |
| **D025** | jobs 单 capture × 单 job_type 任意时刻最多 1 active | §4.6 | 2026-05-02 |
| **D026** | media_assets → artifact_assets 命名修正 | §4.2 | 2026-05-02 |
| **D027** | source_items.raw_metadata_json 拆 path + sha + excerpt | §4.3 | 2026-05-02 |
| **D028** | Codex = merger-of-record（代码 / schema），Opus = PRD 主笔 / auditor | §9 | 2026-05-02 |
| **D029** | Phase 1 拆 1A B 站文案库闭环 + 1B RAW link stub | §10 | 2026-05-02 |
| **D030** | 命名禁区扩展（LP-005） | §12 | 2026-05-02 |
| **D031** | XHS Phase 1 仅 metadata + 外部浏览；评论 / 楼中楼 Phase 3+ | §13 | 2026-05-02 |
| **D032** | Evidence Browser Phase 1 不真内嵌（LP-004） | §11 | 2026-05-02 |
| **D033** | Capture Plan estimate → approve → run 三段式硬门（LP-002） | §8 | 2026-05-02 |
| **D034** | Source Radar 默认动作 [打开 Scope]，quick_capture 仅在 LP-001 §1.2 条件全满足时 | §6.4 | 2026-05-02 |
| **D035** | Signal Workbench 三栏布局 + Brainstorm Notes 常驻不可隐藏 | §6.2 / §6.3 | 2026-05-02 |
| **D036** | artifact_versions 表 + versions/ 子目录约定（raw evidence 不可变） | §4.4 | 2026-05-02 |
| **D037** | browsing_sessions / browsing_events 入账（不创建 capture） | §4.5 | 2026-05-02 |
| **D038** | recommendations.suggested_action 废止 capture，新增 open_scope / verify_signal / quick_capture | §7 | 2026-05-02 |

### 14.3 待 user 拍板锁定

D022-D038 全部为 amendment v1.1 提案。user 拍板顺序建议：

1. 先拍板 LP-001 / D022（Capture Scope Gate） — 最关键，影响所有其他章节
2. 拍板 D023 / D024（4 实体 + 双轨状态机） — schema 主体
3. 拍板 D025-D027 / D036（schema 修订）
4. 拍板 D028（merger-of-record）
5. 拍板 D029（Phase 1 拆分）
6. 拍板 D030-D034 / D037-D038（细节锁定）

---

## 15. 与原 PRD 章节对应表（修订映射）

| 原 PRD 章节 | 修订状态 | amendment 引用章节 |
|---|---|---|
| §0 元信息 | 加 amendment notice | §16 |
| §1 Mission / 范围 | + 加 LP-001 Capture Scope Gate 一条 | §1 |
| §1.4 不做（红线） | + 加禁用词 crawl / harvest 等 | §12 |
| §2 用户路径 | P1 / P3 / P5 改起点为 signal observed | §17 |
| §4 Authority-first | **不变** | — |
| §5 FS Layout 6 区 | **核心不变**，加 versions/ 子目录约定 | §4.4 |
| §5.4 文件命名约定 | + comments-page / images / ocr 等新文件名 | §13.3 / §13.4 |
| §6 State Words | + signals.status / hypotheses.status / capture_plans.status / topic_cards.status | §2 / §3 |
| §6.3 Capture Lifecycle | **不变**（17 + 7 状态保留） | — |
| §7 SQLite Schema | + 8 新表 + 3 修订（含 jobs 幂等约束） | §2 / §4 |
| §7.5.10 media_assets | **改名 → artifact_assets** | §4.2 |
| §7.5.4 source_items | raw_metadata_json 拆 path + sha + excerpt | §4.3 |
| §7.5.8 jobs | + partial unique index | §4.6 |
| §7.5.5 captures | + created_by_path + capture_plan_id | §3.5 |
| §7.5.15 recommendations | suggested_action enum 调整 | §7.1 |
| §7.7 views | + v_pending_signals / v_active_plans / v_topic_cards 等 | §15.1 |
| §8 Thin API | + 28 新路由 | §5 |
| §8.4.3 State Transition Enforcement | + signal lifecycle / plan lifecycle 转移规则 | §3 |
| §9 Workers | + plan_estimator worker | §8.2 |
| §10 UI IA | Source Radar → Signal Radar；+ Signal Workbench 三栏 | §6 |
| §10.4 Source Radar | 卡片操作改 | §6.4 |
| §11 Recommendation | suggested_action 调整；默认 open_scope | §7 |
| §12 Knowledge Bridge | **不变**，但与 topic_cards 联动 | §17 |
| §13 Multi-agent | merger-of-record 模型 | §9 |
| §14 安全合规 | XHS Phase 1 进一步降级 | §13 |
| §15 Phase 计划 | Phase 1 拆 1A / 1B；Phase 2 平移 | §10 |
| §16 技术栈 | **不变** | — |
| §17-§19 测试部署 KPI | **不变**（KPI 加 plan-level 指标） | §19 |
| §20 Decisions | + D022-D038 | §14 |
| §21 Open Questions | + 12 新 Q（amendment 引发） | §18 |
| §22-§24 附录 | **不变** | — |

---

## 16. 在原 PRD 文件加 amendment notice 的位置

在 `PRD-v1-2026-05-02.md` 最顶部（第 1 行 H1 标题之后）加：

```markdown
> ⚠ **重要**：本 PRD 已有 v1.1 amendment（2026-05-02）。
> 必须配合 `PRD-v1.1-amendment-2026-05-02.md` 一起阅读。
> 冲突时 amendment > base PRD。新增 LP-001 至 LP-005 五条 locked principles，
> 影响章节：§1 / §2 / §6 / §7 / §8 / §10 / §11 / §13 / §15。
```

并在 §0.3 拍板状态总览表加一行：

```markdown
| **v1.1 amendment** | LP-001 至 LP-005 + D022-D038 + 4 前置实体 | DRAFT，待 user 拍板 | — |
```

---

## 17. 用户路径修订（覆盖原 PRD §2.2）

### 17.1 P1 修订 — 白名单订阅触发主动推荐（新版）

```text
user 在 Sources 页加 B 站 UP 主"影视飓风"为账号源（state=ready）
   ↓
Hermes 定时扫描发现新作品"AI 工具实测"
   ↓
Recommender 规则召回 + LLM Reranker 重排，suggested_action=open_scope
   ↓
推送到 Mission Control Decision Dock + Source Radar
   ↓
user 在 Source Radar 卡片点 [打开 Scope]   <—— 注意不再是 [采集]
   ↓
进入 Signal Workbench
   ↓
中栏 Signal Brief 显示推荐理由 + 关联 RAW 节点
   ↓
user 写一条 Hypothesis："这条评测可能补充 RAW『AI Agent 选型』缺口"
   ↓
右栏 Evidence Browser 显示 metadata + 评论氛围概况（不抓评论）
   ↓
[打开原始页] 在系统浏览器查看 5 分钟
   ↓
user 回 ScoutFlow，在 Brainstorm Notes 写：
"前 5 分钟说三类工具，5-12 分钟有具体案例，评论区有反方意见"
   ↓
[生成 Capture Scope] → LLM 把 notes 转 scope_json 草稿
   ↓
Scope Builder 显示草稿：
  targets: [BV1xxx full audio + transcript]
  budget: max_audio_minutes=15, no comments
   ↓
[Estimate] → estimate 完成：38MB / 12 min ASR / $0.08
   ↓
[Approve] → user approve
   ↓
[Run] → 进 Capture Pipeline，用 plan_id 触发
   ↓
12 分钟后 Mission Control 提示"plan 完成"
   ↓
进 Library 看 normalized.md / 进 Knowledge Bridge 看 RAW patch 候选
   ↓
2 条 RAW patch accept → 写到 ~/raw/inbox/scoutflow/
   ↓
user 在 Topic Card 创建：
"AI 工具评测 - 是否真的减少了内容生产时间"
   ↓
关联本 capture 为 example/quote 证据
```

**关键差异**：从原版的 "user 点采集 → 12 分钟后完成" 变成 "user 点打开 Scope → 浏览 5 分钟 → 写 hypothesis → estimate → approve → 12 分钟完成 → 关联 Topic Card"。慢了 5-10 分钟，但避免了 80% 的低质量采集。

### 17.2 P2 修订 — 单条 URL 即时探针（quick_capture 路径）

```text
user 在微信看到 B 站视频链接，复制
   ↓
打开 ScoutFlow Explore 页粘贴 URL
   ↓
Explore 显示预览：metadata + RAW 匹配预估
   ↓
检查 quick_capture 条件：
  ✓ manual URL
  ✓ 估算 < 100MB / 30min / $0.30
  ✓ 不抓扩展
   ↓ 满足
显示 [快速采: audio + transcript] 按钮
   ↓
user 点 [快速采]
   ↓ 不创建 signal / 不创建 plan
直接创建 capture（created_by_path='quick_capture'）
   ↓
12 分钟后入 Library
```

### 17.3 P3 修订 — 关键词扫描（必走 Scope）

```text
user 加关键词源（不变）
   ↓
Hermes 扫描，命中 8 条 → 8 个 source_items
   ↓
Recommender 按规则选 5 条 → 推到 Source Radar，suggested_action=verify_signal
   ↓
user 在 Source Radar 看 5 张卡片
   ↓
点其中 1 张 [打开 Scope]   <—— 关键词命中默认进 Scope，不允许 quick_capture
   ↓
进 Signal Workbench → 写 hypothesis → estimate → approve → run
```

**关键差异**：关键词命中**永远不允许 quick_capture**，必须走 Scope。

### 17.4 P4 修订 — 列表源批量

```text
user 加列表源（B 站收藏夹 23 条）
   ↓
ScoutFlow 一次性导入 metadata 23 条 → 23 个 source_items
   ↓
推到 Source Radar 但**默认不创建 23 个 signal**（避免噪声）
   ↓
user 在 Source Radar 批量选 12 条
   ↓
点 [合并打开 Scope]   <—— 12 条共享一个 capture_plan
   ↓
进 Signal Workbench（特殊批量模式）
   ↓
单一 Brainstorm Notes 里写"我想一次研究这 12 条评测"
   ↓
Scope Builder 显示 12 个 target，预算合并估算
   ↓
[Estimate] → "总 1.2GB / 144 min ASR / $0.96"
   ↓
[Approve] / 修改 budget 砍到 6 条
```

### 17.5 P5 修订 — Reverse Discovery（Phase 2 启用）

```text
user 在 RAW 标"用户洞察 - 缺少行业实例"
   ↓
ScoutFlow Knowledge Bridge → Reverse Discovery
   ↓
LLM 把缺口转 keywords + platforms
   ↓
创建 signal（signal_type='raw_gap', origin_kind='raw_node'）
   ↓
触发一次性 source scan（不订阅）
   ↓
返回 6 条候选 → 进 Signal Workbench
   ↓
后续路径同 P3
```

---

## 18. Open Questions 增补（A001 引发）

### 18.1 新 Q 列表

| # | 问题 | 影响 | 当前判断 |
|---|---|---|---|
| QA1 | quick_capture 阈值（100MB / 30min / $0.30）是否合理 | quick 路径可用性 | 先按这套，Phase 1A 实测后调 |
| QA2 | estimate worker 误差容忍度 | budget 准确度 | ±20% 内可接受，超 50% 触发 warning |
| QA3 | Brainstorm Notes 自动保存频率 | 用户体验 | 5 秒 debounce + 失焦立即存 |
| QA4 | Signal Workbench 关闭时 hypothesis draft 处理 | 数据保留 | draft 永久保留，user 可手动 reject |
| QA5 | 同一作品多 plan 重抓（如先 metadata，后 audio）如何避免重复下载 | 效率 | capture 复用 + plan 级 incremental scope |
| QA6 | Topic Card 与 DiloFlow 衔接的字段映射 | 跨项目 | Phase 2 设计 export 格式 |
| QA7 | Reverse Discovery LLM 把 RAW 缺口转关键词的准确率 | 推荐质量 | 需 Phase 2 实测 |
| QA8 | artifact_versions 表会不会膨胀（每次重跑都加版本） | DB 大小 | 加配额：每 capture × kind 保留最近 5 版，更早归档 |
| QA9 | 评论一旦 Phase 3 启用，UGC 内容的隐私边界 | 合规 | 必须有"敏感词过滤 + user 主动确认" gate |
| QA10 | Capture Plan 跨 plan 共享 worker 资源（如同时 4 个 plan running）的并发 | 性能 | plan 级并发 ≤ 3，capture 级 worker 并发独立计算 |
| QA11 | Brainstorm Notes 是否纳入 LLM context 影响 normalize | 信息泄漏 | 不纳入；notes 仅 user 私有，normalizer 仅看 transcript |
| QA12 | 多 agent merger-of-record 例外（紧急 hotfix）流程 | 治理灵活度 | 紧急 hotfix 由 user 直接拍板 + 事后补 candidate audit |

---

## 19. KPI 增补

原 §19 KPI 全部保留。amendment 增补：

### 19.1 Plan-level KPI

| KPI | 目标 | 测量 |
|---|---|---|
| plan estimate 准确度（实际 vs 估算） | ±20% 内 | running 完成后对比 |
| plan approve → run 转化率 | ≥ 70% | approve 后 24h 内 run |
| 平均 plan 内 capture 数 | 1-5 | scope 控制力 |
| plan 失败率（部分 / 全部 capture 失败） | < 15% | jobs.status='failed' 在 plan 内占比 |

### 19.2 Signal-level KPI

| KPI | 目标 | 测量 |
|---|---|---|
| signal observed → opened 率 | ≥ 30% | 系统推的至少 30% 被 user 打开 |
| signal opened → hypothesized 率 | ≥ 60% | 打开后至少写一条假设 |
| signal hypothesized → plan_ready 率 | ≥ 50% | 假设后真的进 plan |
| signal 全程到 evidence_locked 率 | ≥ 30% | 真做完采集 |
| signal dismissed 率 | ≤ 40% | 太多放弃 = 推荐质量差 |

### 19.3 Topic Card KPI

| KPI | 目标 | 测量 |
|---|---|---|
| 每月 promoted_to_diloflow 选题数 | ≥ 2 | 真正给 DiloFlow 用 |
| topic_card 平均 evidence 数 | ≥ 5 | 单选题至少 5 条素材 |
| topic_card refine 周期 | < 2 周 | candidate → evidence_ready |

### 19.4 治理 KPI

| KPI | 目标 | 测量 |
|---|---|---|
| candidate 24h 处理率 | ≥ 80% | 不积压 |
| Codex / Opus 越权变更次数 | 0 | 任何不走 candidate 直改主线 = critical issue |
| schema lock 项变更必双签率 | 100% | 审计 commits |

---

## 20. 不变项总览（amendment 不动）

确保 user 知道哪些**没动**：

- §4 Authority-first 4 层堆栈 — 完整保留
- §5 FS Artifact Layout 6 区核心 — 完整保留（仅加 versions/ 子目录，不动 6 区结构）
- §5.7 capture-manifest.json schema — 完整保留
- §5.9 跨 worker 写边界 — 完整保留（artifact_versions 写规则在原规则上加一条 rename-then-write）
- §5.10 三级备份策略 — 完整保留
- §6.3 Capture Lifecycle 17 + 7 状态 — 完整保留（+ created_by_path 字段，不影响状态机）
- §13.7 candidate 流程 — 完整保留
- §14 安全合规红线 — 完整保留（仅 XHS 进一步降级）
- §16 技术栈 — 完整保留
- §17 测试策略 — 完整保留
- §18 部署运维 — 完整保留
- §22-§24 附录 — 完整保留

---

## 21. Amendment 落地任务清单（给 Codex / Opus）

### 21.1 优先级 P0（user 拍板后立即做）

- [ ] 创建 `docs/decisions.md`，写入 D001-D021（来自 base PRD）+ D022-D038（本 amendment）
- [ ] 在 `PRD-v1-2026-05-02.md` 顶部加 amendment notice（§16）
- [ ] 在 `PRD-v1-2026-05-02.md` §0.3 拍板状态总览加一行
- [ ] 创建 `docs/specs/` 目录预留：
  - `docs/specs/signal-workbench-ui.md`（Phase 2 之前空 stub）
  - `docs/specs/capture-plan-estimator.md`
  - `docs/specs/api-routes-v1.1.md`

### 21.2 优先级 P1（Phase 0 完成前）

- [ ] DB migrations：004 - 011（按 §4 表逐一）
- [ ] amend §10 UI mock 加 Signal Workbench 静态版本
- [ ] amend §11 Recommendation suggested_action enum

### 21.3 优先级 P2（Phase 1A 期间）

- [ ] 实现 LP-001 enforcement（API 层 + UI 层）
- [ ] 实现 jobs partial unique index
- [ ] artifact_assets 重命名 + 数据迁移

### 21.4 优先级 P3（Phase 1B / Phase 2 期间）

- [ ] signals / hypotheses / capture_plans / topic_cards 完整实现
- [ ] Signal Workbench 三栏 UI
- [ ] plan_estimator worker
- [ ] browsing_sessions 入账

---

## 22. Amendment v1.1 完结声明

> **PRD v1.1 amendment 完结**
>
> 版本：v1.1（DRAFT，待 user 拍板）
> 起草：2026-05-02
> 行数：~1500
> 状态：5 个新 LP（LP-001 至 LP-005） + 17 个新 D（D022 至 D038） + 8 个新表 + 28 个新 API 路由 + 1 个新 UI 工作区（Signal Workbench）
>
> 与 base PRD（v1）一起读。冲突时 amendment > base。
>
> ScoutFlow v1.1 = Authority-first 的 Mission Control + **Capture Scope Gate** + Module Forge + Evidence Ledger。
>
> 工程上先锁 artifact layout（done），再锁 schema（含本 amendment 8 新表），再锁 Console（含 Signal Workbench），最后锁 worker contract。
>
> 关键不变量：信号发现 → 主理人判断 → 证据确认 → 范围控制 → 采集入账 → 选题沉淀。**不再"看到推荐 → 一键采集"**。
