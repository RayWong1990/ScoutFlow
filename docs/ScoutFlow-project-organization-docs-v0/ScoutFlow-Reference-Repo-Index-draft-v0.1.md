# ScoutFlow Reference Repo Index v0.1

> `referencerepo/` 是只读参考区，进 `.gitignore`。本文件进 git，作为 agent 的索引，避免重复搜索和重复推理。

---

## 使用规则

```text
referencerepo/ 不被产品代码 import
referencerepo/ 不作为 runtime dependency
referencerepo/ 只用于研究、对照、设计借鉴
```

每次刷新参考仓后，更新本文件的 `last_checked`。

---

## MyTube

```text
local_path: referencerepo/MyTube
role: ScoutFlow 近邻形态参考
last_checked: 2026-05-03
```

借：

```text
多源 downloader/player 的产品仓形态
React/Vite + 后端 + SQLite 分层
目录结构文档
轻量 source 管理和 UI 入口
```

不借：

```text
以播放消费为中心的心智
把 ScoutFlow 做成视频播放器
```

---

## Karakeep

```text
local_path: referencerepo/karakeep
role: 产品仓管理方式首选参考
last_checked: 2026-05-03
```

借：

```text
monorepo 边界
docs / packages / apps / workers 的组织方式
AGENTS.md 类 agent 入口
收藏卡片与标签体验
```

不借：

```text
保存一切的低门槛入口
移动端和 SaaS 范围
```

---

## ArchiveBox

```text
local_path: referencerepo/ArchiveBox
role: durability / evidence / interface doctrine 参考
last_checked: 2026-05-03
```

借：

```text
普通文件 + DB + CLI/UI/API 共存
原始 evidence 保存理念
CLAUDE.md 入口文档
长期归档的 durability 边界
```

不借：

```text
通用全网归档平台范围
过宽的 extractor 体系
```

---

## TubeArchivist

```text
local_path: referencerepo/tubearchivist
role: archive manager / ops discipline 参考
last_checked: 2026-05-03
```

借：

```text
任务队列
订阅扫描
pre-commit / contributing discipline
media archive 运维经验
```

不借：

```text
YouTube 单平台中心
Jellyfin/Plex 消费端集成方向
```

---

## Pinchflat

```text
local_path: referencerepo/pinchflat
role: source rule / narrow scope 参考
last_checked: 2026-05-03
```

借：

```text
source rule
cutoff / title filter / rule-driven subscription
窄 scope 的项目纪律
```

不借：

```text
单纯订阅下载器形态
把采集行为默认为下载
```

---

## MediaCrawler

```text
local_path: referencerepo/MediaCrawler
role: 中文社媒 source adapter 参考
last_checked: 2026-05-03
```

借：

```text
source adapter
平台接入经验
XHS/B站/抖音等平台的只读采集边界意识
```

不借：

```text
项目管理方式
crawler/spider 命名
高频/广谱爬虫心智
```

---

## MeTube

```text
local_path: referencerepo/metube
role: 极简下界参考
last_checked: 2026-05-03
```

借：

```text
URL -> task -> file 的极简输入体验
AGENTS.md 下界
CI 下界
```

不借：

```text
过薄的数据模型
下载器心智
```

---

## 总裁决

```text
仓库形状：Karakeep + MyTube
证据持久化：ArchiveBox
订阅/规则：Pinchflat + TubeArchivist
source adapter：MediaCrawler
极简提醒：MeTube
```
