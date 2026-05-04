---
title: Bilibili comparator scan for ScoutFlow Wave 3A
date: 2026-05-05
candidate: true
type: shoulder-scan-report
stage: 2
status: candidate
authority: research-only / not-authority / not-runtime-approval
---

# Bilibili Comparator Scan

## 1. Scan 目标

本扫描只回答一个问题：如果 ScoutFlow 未来需要一个 `BBDown` 之外的 Bilibili metadata comparator，用来做字段发现、parser drift 监控、或极窄的 fallback 参考，应该保留哪 1-2 个候选。

当前立场保持不变：

- `BBDown locked`。它仍是 ScoutFlow Phase 1A 已讨论路径里的主 capture/tool adapter 方向。
- comparator 只用于 `field discovery + parser drift 监控 + 参考性 fallback`。
- 本文不是 runtime 批准，不是 dependency 批准，也不是 `BBDown` 替换建议。
- 对 GPL 家族仓库，scan 只做 license 与字段面审查，不给出直接依赖许可。

## 2. Scan 方法与基线

### 2.1 BBDown 基线

当前 ScoutFlow 已明确或候选中的 BBDown 最小字段面是：

- `platform_item_id`
- `title`
- `duration_seconds`
- `page_count`
- `selected_page`

因此 comparator 评估重点不是“能不能下载”，而是：

1. 是否能稳定给出这些基线字段。
2. 是否还能补出 `aid/bvid/cid/pages/stats/tags/subtitles/chapters` 之类的扩展字段。
3. 一旦 Bilibili 页面或接口结构漂移，是否能帮助我们快速判断是 `BBDown parser drift` 还是站点上游变化。

### 2.2 事实窗口

以下 GitHub 元数据在 `2026-05-05` 抓取：

- repo metadata: `gh repo view`
- default branch head commit: `gh api repos/<repo>/commits/<default-branch>`
- source shape: `README.md`、`LICENSE`、`pyproject.toml`、核心源码路径

注意：`Nemo2011/bilibili-api` 的 repo `pushedAt` 是 `2026-04-22`，但 `main` 头提交日期是 `2026-01-23`。这说明 repo 近期有非 `main` 分支、tag 或 release 活动，但默认分支本身不是 4 月更新。本文按默认分支 head 评估维护活跃度。

### 2.3 总览矩阵

| Candidate | Default branch head | License | Core path | BBDown overlap | Unique fields / surface | Integration mode proposal | Value score | Drop risk | Scan verdict |
|---|---|---|---|---|---|---|---:|---|---|
| `yt-dlp/yt-dlp` | `35684c1` (`2026-05-03`) | Unlicense | `yt_dlp/extractor/bilibili.py` | `title` `duration` `platform id` | `formats` `subtitles` `chapters` `comments` `uploader` `tags` `view/like/comment count` | `reference_only` now; future `subprocess` possible | 5/5 | low | continue |
| `Nemo2011/bilibili-api` | `0147ab6` (`2026-01-23`) | GPL v3 | `bilibili_api/video.py` | `aid/bvid` `title` `pages/cid` `subtitle/player info` | async API surface, `danmaku`, tag/stat access, credential/wbi/buvid handling | `reference_only` now; future `subprocess only` if separately approved | 4/5 | medium | continue |
| `InMirrors/bilibili-api-Nemo2011` | `0147ab6` (`2026-01-23`) | GPL v3 | `bilibili_api/video.py` | same as Nemo snapshot | mirror only | `reference_only` | 2/5 | medium | keep as archive mirror |
| `shakenetwork/bilibili-api` | `a312432` (`2024-09-21`) | GPL v3 | `bilibili_api/video.py` | same family overlap | older fork; no visible differentiation | `reference_only` | 1/5 | high | drop from active pool |
| `Pudding2024/bilibili-api` | `0147ab6` (`2026-01-23`) | GPL v3 | `bilibili_api/video.py` | same as Nemo snapshot | backup wording only | `reference_only` | 2/5 | medium | keep as archive mirror |

## 3. Candidate Verdicts

### 1. yt-dlp/yt-dlp

- URL: <https://github.com/yt-dlp/yt-dlp>
- Repo metadata:
  - stars: `160518`
  - default branch: `master`
  - repo pushedAt: `2026-05-03T22:19:09Z`
  - default branch head: `35684c1171dd8b99da825cf43a0b2c06b43824b7` on `2026-05-03T22:19:08Z`
- License: `Unlicense`
- Core path:
  - `yt_dlp/extractor/bilibili.py`
  - root `README.md`
  - root `LICENSE`
- README / source summary:
  - 它是成熟的通用 extractor 框架，不是 Bilibili 专用库。
  - Bilibili extractor 代码直接暴露了 `formats`、`subtitles`、`chapters`、`comments`、互动视频分支等处理逻辑。
  - 这类 shape 很适合当“字段上界参考”，也适合长期 drift 对照。
- 与 BBDown 字段对照:
  - overlap: `title`, `duration`, `platform_item_id`（以 `bvid/aid` 形态出现）
  - partial overlap: `page_count/selected_page` 不是它的主 contract，但 playlist / multi-part entry 能提供接近信息
- Unique fields:
  - `uploader`, `uploader_id`
  - `thumbnail`
  - `tags`
  - `view_count`, `like_count`, `comment_count`
  - `chapters`
  - `subtitles`
  - `formats`
  - interactive/video-section entries
- integration_mode_proposal:
  - 当前 PR：`reference_only`
  - 未来如真要接入，license 允许度较高，优先考虑独立 `subprocess`
- field reference value: `5/5`
- drop risk: `low`
- blockers:
  - 不是 Bilibili 专用接口层，对 `cid/page_index` 这类站内概念不如专用库直观。
  - 抽象层较厚，想做细颗粒 API 字段映射时需要二次整理。
- decision: `continue`
- next_action:
  - 进入 comparator pool 主候选。
  - Wave 3B 如果只 clone/probe 1 个低风险 comparator，优先它。

### 2. Nemo2011/bilibili-api

- URL: <https://github.com/Nemo2011/bilibili-api>
- Repo metadata:
  - stars: `3893`
  - default branch: `main`
  - repo pushedAt: `2026-04-22T13:57:28Z`
  - default branch head: `0147ab61aa5a9f821c9b441cb1ddfdc761a3d999` on `2026-01-23T12:19:00Z`
- License: `GPL v3`
- Core path:
  - `bilibili_api/video.py`
  - `bilibili_api/utils/network.py`
  - `pyproject.toml`
  - root `README.md`
- README / source summary:
  - README 明示它覆盖视频、音频、直播、动态、专栏、用户、番剧等大量 API 面。
  - 示例输出里直接出现 `bvid`, `aid`, `videos`, `tid`, `tname`, `pic`, `title`, `pubdate`, `ctime` 等字段。
  - `video.py` 里能看到 `get_pages`, `get_cid`, `get_tags`, `get_player_info`, `get_subtitle`, `get_danmakus` 等更贴近 B 站站内语义的接口。
- 与 BBDown 字段对照:
  - overlap: `platform_item_id`（`aid/bvid`）, `title`, `page_count`, `selected_page` 所依赖的 `pages/cid`
  - partial overlap: `duration_seconds` 可从 video/player/page 相关返回中取到，但不是像 BBDown 那样围绕 CLI 输出整齐暴露
- Unique fields:
  - `aid <-> bvid` 双向语义
  - `cid` / `pages`
  - `owner.mid`
  - `tags`
  - `danmaku` / `danmaku_xml` / `snapshot`
  - `subtitle`
  - `player info`
  - 更细的站内 stat / operate surface
- integration_mode_proposal:
  - 当前 PR：`reference_only`
  - 若未来必须执行：`subprocess only`
  - 该路线 `must not be python_import`
- field reference value: `4/5`
- drop risk: `medium`
- blockers:
  - `GPL v3` 是硬边界。
  - `network.py` 明显带有 `Credential`、`SESSDATA`、`buvid3/buvid4`、`wbi`、`curl_cffi|httpx|aiohttp` 等网络与凭据表面，不适合作为主 repo 直接 import 依赖。
  - 默认分支最近一次提交停在 `2026-01-23`，活跃度不算差，但不是月更主线。
- decision: `continue`
- next_action:
  - 只保留为二号 comparator 候选。
  - 如后续需要 probe，重点做字段映射与 license boundary，不做主 repo import 方案。

### 3. InMirrors/bilibili-api-Nemo2011

- URL: <https://github.com/InMirrors/bilibili-api-Nemo2011>
- Repo metadata:
  - stars: `0`
  - default branch: `main`
  - repo pushedAt: `2026-01-23T12:20:10Z`
  - default branch head: `0147ab61aa5a9f821c9b441cb1ddfdc761a3d999` on `2026-01-23T12:19:00Z`
- License: `GPL v3`
- Core path:
  - `bilibili_api/video.py`
  - `bilibili_api/utils/network.py`
  - `pyproject.toml`
- README / source summary:
  - 从 repo 名和 tree 看，它基本就是 Nemo 仓库的镜像快照。
  - default branch head SHA 与 Nemo 相同，说明至少当前扫描点没有独立演化。
  - 价值主要在“上游失联时的档案镜像”，而不是独立技术路线。
- 与 BBDown 字段对照:
  - overlap: 与 Nemo 基本一致
  - unique fields: 与 Nemo 基本一致，无额外新增
- integration_mode_proposal:
  - `reference_only`
- field reference value: `2/5`
- drop risk: `medium`
- blockers:
  - 与 Nemo 同 GPL 边界。
  - 没有独立维护信号，也没有比 Nemo 更清晰的 README/issue/roadmap 价值。
- decision: `continue` as archive mirror only
- next_action:
  - 不进主 comparator pool。
  - 只在 Nemo 上游不可用时作为备份参考。

### 4. shakenetwork/bilibili-api

- URL: <https://github.com/shakenetwork/bilibili-api>
- Repo metadata:
  - stars: `0`
  - default branch: `main`
  - repo pushedAt: `2025-01-11T14:04:02Z`
  - default branch head: `a31243288874ad3c2a8f68b633fbf966a9c20c26` on `2024-09-21T14:05:15Z`
- License: `GPL v3`
- Core path:
  - `bilibili_api/video.py`
  - `bilibili_api/utils/network.py`
  - `pyproject.toml`
- README / source summary:
  - 仍是同一 `bilibili-api` 家族，但默认分支头明显更旧。
  - 描述没有呈现出新的架构方向或更强维护信号。
  - 作为 active comparator，它比 Nemo 和镜像快照都更弱。
- 与 BBDown 字段对照:
  - overlap: 仍然存在 `aid/bvid/pages/cid/title` 等基础字段面
  - unique fields: 理论上与 Nemo 家族相近，但没有独立增益
- integration_mode_proposal:
  - `reference_only`
- field reference value: `1/5`
- drop risk: `high`
- blockers:
  - 老旧。
  - GPL 边界仍在。
  - 相比 Nemo 本体或同 SHA 镜像，没有明显保留价值。
- decision: `drop`
- next_action:
  - 不进入后续 clone/probe 候选。

### 5. Pudding2024/bilibili-api

- URL: <https://github.com/Pudding2024/bilibili-api>
- Repo metadata:
  - stars: `0`
  - default branch: `main`
  - repo pushedAt: `2026-01-23T12:20:10Z`
  - default branch head: `0147ab61aa5a9f821c9b441cb1ddfdc761a3d999` on `2026-01-23T12:19:00Z`
- License: `GPL v3`
- Core path:
  - `bilibili_api/video.py`
  - `bilibili_api/utils/network.py`
  - `pyproject.toml`
- README / source summary:
  - README 描述直接写明这是 `2026.1.31` 的备份。
  - 从树结构和 head SHA 看，它更像保存点，不像活跃 fork。
  - 价值与 `InMirrors` 接近，也是归档型 mirror。
- 与 BBDown 字段对照:
  - overlap: 与 Nemo 基本一致
  - unique fields: 无独立新增
- integration_mode_proposal:
  - `reference_only`
- field reference value: `2/5`
- drop risk: `medium`
- blockers:
  - GPL 边界不变。
  - 与 Nemo 主线同 SHA，不构成新的比较维度。
- decision: `continue` as archive mirror only
- next_action:
  - 不进入主 comparator pool。
  - 只保留为可替换镜像快照。

## 4. License 严审结论

### 4.1 可以直接保留在候选池里的低摩擦项

- `yt-dlp/yt-dlp`: `Unlicense`
  - 作为 `reference_only` 完全没问题。
  - 如果未来另起 dispatch 讨论执行面，`subprocess` 也是可谈的。

### 4.2 必须硬隔离的 GPL 家族

- `Nemo2011/bilibili-api`: `GPL v3`
- `InMirrors/bilibili-api-Nemo2011`: `GPL v3`
- `shakenetwork/bilibili-api`: `GPL v3`
- `Pudding2024/bilibili-api`: `GPL v3`

这些仓库在 ScoutFlow 当前阶段都只能按以下规则理解：

- `subprocess only`
- `must not be python_import`
- 进入主 repo dependency、vendored package、直接 runtime import 之前，必须新 dispatch + 专门 license 审查

因此本轮 scan 的推荐不是“引入一个 Python Bilibili SDK”，而是“保留一个 GPL comparator 作为字段词典和站点语义参考”。

## 5. 推荐 Comparator Pool

### 推荐 1：`yt-dlp/yt-dlp`

原因：

- license 最干净。
- 默认分支活跃。
- `yt_dlp/extractor/bilibili.py` 已经给出完整的字段上界参考。
- 它对 `formats/subtitles/chapters/comments/tags/stats` 的覆盖，足以承担 monthly drift baseline。

建议角色：

- 主 comparator
- 主要用途：field discovery、parser drift triage、fixture 对照

### 推荐 2：`Nemo2011/bilibili-api`

原因：

- 它更贴近站内 API 语义，尤其是 `aid/bvid/cid/pages/tag/danmaku/subtitle/player_info` 这些 BBDown 周边字段。
- 当 ScoutFlow 需要判断“是 BBDown CLI 输出漂移，还是 Bilibili 站内字段结构变了”时，它比通用 extractor 更适合做语义词典。

硬限制：

- 只建议保留为二号参考源。
- 当前阶段不建议进入 clone/probe 优先级第一位。
- 如后续真进入执行面，只能讨论 `subprocess only`，不能走 import 路线。

### 不推荐进入主池

- `InMirrors/bilibili-api-Nemo2011`
- `Pudding2024/bilibili-api`
- `shakenetwork/bilibili-api`

理由：

- 它们要么只是 Nemo 的镜像快照，要么比 Nemo 更旧。
- 作为 archive fallback 可以留名，但不应占用 Wave 3B 主 probe 名额。

## 6. Drift 监控建议

建议把 comparator 用在“月度 fixture diff”，而不是“线上双跑强一致”。

### 6.1 最小监控批次

每月对一组固定 public fixtures 执行一次离线对照，覆盖：

- 单 P 视频
- 多 P 视频
- 带字幕视频
- 带章节或互动结构的视频

### 6.2 比对字段

第一层，BBDown 基线字段：

- `platform_item_id`
- `title`
- `duration_seconds`
- `page_count`
- `selected_page`

第二层，增强字段：

- `aid`
- `bvid`
- `cid/pages`
- `tags`
- `subtitle presence`
- `chapters`
- `view/like/comment count`

### 6.3 告警条件

- 字段消失
- 字段新增
- 字段类型变化
- `page/cid` 映射关系变化
- tag / category 语义突变
- 任何类似历史 `rpid Tag 8->2` 的枚举漂移事件

### 6.4 处置原则

- 先判定是 `BBDown parser drift`、comparator 自身变更，还是 Bilibili 上游变更。
- 不因为 comparator 与 BBDown 不一致，就自动否定 `BBDown locked` 路线。
- comparator 的职责是帮助定位原因，不是抢主路径。

## 7. Shoulders-Index 更新建议

本 PR 不修改 `docs/shoulders-index.md`。

建议保持：

- 当前 scan 结果只落 `docs/research/shoulders/`
- 如果未来有 user 批准的 Wave 3B batch，再考虑把：
  - `yt-dlp/yt-dlp`
  - `Nemo2011/bilibili-api`
  作为 `discovered` 或 `scanning` 候选写入 index
- `InMirrors` / `Pudding2024` / `shakenetwork` 不建议入主 batch，最多作为 archive note 附带记录

## 8. Final Scan Verdict

- keep:
  - `yt-dlp/yt-dlp`
  - `Nemo2011/bilibili-api`
- mirror-only:
  - `InMirrors/bilibili-api-Nemo2011`
  - `Pudding2024/bilibili-api`
- drop:
  - `shakenetwork/bilibili-api`

结论一句话：

`BBDown locked` 仍然成立；Bilibili comparator pool 应该收敛为 `yt-dlp` 主参考 + `Nemo2011` 语义参考，其余 fork/mirror 不进入主池。
