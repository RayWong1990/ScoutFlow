# ScoutFlow 参考仓探针研究

日期：2026-05-03  
模式：`deep`  
输入形态：`立场驱动 claim` + 本地项目主题  
本地克隆根目录：`/Users/wanglei/workspace/ScoutFlow/referencerepo/`

## Phase 0：反确认偏差 + 假设拆解

### 检测到的用户立场

用户立场压缩如下：

- ScoutFlow 是长期跑的工程项目。
- 不应该继承 DiloFlow / ContentFlow 那种治理重量。
- 真正有价值的经验要保留，但最好通过工程惯例、lint、format、test 来约束，而不是靠阶段化文书和流程仪式。

把问题中性化后，得到的研究问题是：

> 对一个本地优先、带 H5 前端、后台任务、多 agent 开发协作的采集项目来说，哪些开源参考仓的项目管理模式是真正能落地的？当前 ScoutFlow 治理草案里哪些部分偏重？

最强反方立场：

> 如果 ScoutFlow 把治理削得太轻，多 agent 漂移、spec 与实现脱节、source adapter 改坏安全边界，这些问题会以更难排查的方式回来。

### 核心假设

H1：对 ScoutFlow 最有参考价值的仓库，主要靠代码结构、CI、贡献文档、issue/PR 模板来管理复杂度，而不是靠厚重的顶层治理目录。

- 隐含前提：
  - 成熟的采集 / 前端 / 归档项目都会把工程稳定面沉到代码和 CI 里 `[已验证]`
  - 成功项目通常不会把治理目录做成仓库中心 `[已验证]`
  - 多 agent 编码压力可以先用轻入口文档 + 自动化来处理 `[合理推测]`

H2：多平台爬虫仓对 ScoutFlow 的价值主要在 source adapter、反风控、平台接入策略，不在项目管理方式。

- 隐含前提：
  - 爬虫仓的首要目标是“拿到源”，不是长期产品工程体验 `[已验证]`
  - 它们通常在 contributor workflow 上投入弱于产品型仓库 `[已验证]`

H3：ScoutFlow 最可复用的中心模式，应该是三类能力的混合：

- RAW 式可 lint 文档
- MyTube / Karakeep 式产品仓工程表面
- ArchiveBox 式 durability 与 evidence 边界

- 隐含前提：
  - 这三类能力是互补的，不是互斥的 `[合理推测]`
  - ScoutFlow 的真实工作负载同时包含采集、证据保存、产品 UI 三层 `[已验证]`

H4：Opus 结论里很多“原则层”内容是成立的，但很多“文件治理形状”如果直接照搬，会偏重。

- 隐含前提：
  - 原则可以迁移 `[已验证]`
  - `candidates/`、`dispatches/`、`audits/`、`decisions.md` 这些顶层治理面，在没有真实实现压力前不一定成立 `[合理推测]`

### 当前仍未验证的重点前提

- ScoutFlow 未来是否真的会高频出现多个 agent 同时写重叠文件
- repo-local 的 doc lint 是否足以覆盖 `current/PRD/spec` 漂移
- B 站 / XHS adapter 是否会逼出比当前预想更重的运行 SOP

## Phase 0.5：洋葱剥离

### Layer 1：本质提炼

这批参考仓可以分成四个原型：

1. 下载器 UI：浏览器表单 + `yt-dlp`
2. 归档管理器：长期媒体库 / 订阅 / 索引 / 自动下载
3. 收藏 / 知识收集平台：保存一切 + 搜索 + 后台 enrichment
4. 社媒爬虫框架：source adapter 和反风控优先

ScoutFlow 不属于其中任一单一类别。它最接近的是：

- 产品形态上靠近“收藏 / 收集平台”
- durability 上靠近“归档管理器”
- source adapter 上需要借“社媒爬虫框架”

### Layer 2：机制拆解

强样本仓在系统结构上高度收敛：

```text
web/app UI
  -> backend/API
     -> workers / queues / task runners
        -> database + filesystem
           -> source adapters / external tools
```

它们在项目管理表面上也有类似收敛：

```text
README / 入口文档
  -> CONTRIBUTING / 开发文档
     -> CI / lint / test / release workflows
        -> 明确的目录边界
```

最值得注意的是，样本仓普遍没有把下面这些东西做成仓库核心：

- stage ledger
- candidate 队列目录
- amendment 树
- 手写多 agent 行政系统

### Layer 3：成本与天花板

如果直接抄 downloader 仓：

- 优点：URL 输入快，交互简单
- 缺点：evidence lineage、跨源建模、控制面会很弱

如果直接抄 archive 仓：

- 优点：durability、运维边界、长期稳定性更强
- 缺点：容易把 ScoutFlow 拉成“存档中心”，而不是“主动探测与采集中台”

如果直接抄 crawler 仓：

- 优点：adapter 多、反风控经验强
- 缺点：产品工程表面通常不够成熟，repo 管理不适合作为主模板

如果直接抄 bookmark / collector 仓：

- 优点：产品仓味道强，多入口、后台 worker、搜索和扩展性都比较像 ScoutFlow 未来形态
- 缺点：对 source-specific capture lifecycle 和 media-processing 队列的建模可能不够重

### Layer 4：前沿扫描

截至 2026-05-03，这批样本的现实意义如下：

| 仓库 | 说明 | 仓库链接 | 最近更新时间 |
|---|---|---|---|
| `franklioxygen/MyTube` | 最新多源 downloader/player，带明确的分层文档 | [GitHub](https://github.com/franklioxygen/MyTube) | 2026-05-01 |
| `karakeep-app/karakeep` | 收藏平台型产品，docs / MCP / CLI / workers / mobile 很完整 | [GitHub](https://github.com/karakeep-app/karakeep) | 2026-05-02 |
| `ArchiveBox/ArchiveBox` | durability 理念最强，CLI/UI/API/filesystem 共存 | [GitHub](https://github.com/ArchiveBox/ArchiveBox) | 2026-05-02 |
| `tubearchivist/tubearchivist` | 成熟的单平台 archive manager，社区治理较强 | [GitHub](https://github.com/tubearchivist/tubearchivist) | 2026-05-02 |
| `kieraneglin/pinchflat` | 轻量规则驱动的订阅下载器 | [GitHub](https://github.com/kieraneglin/pinchflat) | 2026-05-02 |
| `NanmiCoder/MediaCrawler` | 中文社媒 source adapter 最广，甚至带 WebUI | [GitHub](https://github.com/NanmiCoder/MediaCrawler) | 2026-05-02 |
| `alexta69/metube` | 最薄 downloader 基线 | [GitHub](https://github.com/alexta69/metube) | 2026-05-02 |

两个额外前沿信号：

1. agent 入口文档正在成为真实项目的一部分。
   - `referencerepo/ArchiveBox/CLAUDE.md`
   - `referencerepo/karakeep/AGENTS.md`
   - `referencerepo/metube/AGENTS.md`
2. 收藏型产品正在自然外溢到 MCP / CLI / 扩展 / mobile 多表面。
   - ScoutFlow 如果做成，仓库形态很可能不止一个 web app。

### Layer 5：代际演进

| 代际 | 核心方法 | 代表仓 | 突破点 | 天花板 |
|---|---|---|---|---|
| G1 | 单用途下载 UI | `metube` | URL -> 文件最快 | 知识模型很弱 |
| G2 | 订阅 / 归档管理 | `tubearchivist`、`pinchflat` | 周期扫描、队列、规则过滤 | 单平台偏置明显 |
| G3 | 收藏 / 收集产品平台 | `karakeep`、`MyTube` | 多入口、worker、API、产品化文档 | 运维复杂度上升 |
| G4 | 可编程归档系统 | `ArchiveBox` | CLI/UI/API/filesystem 等价 | 容易太宽 |
| Gx | 广谱社媒爬虫框架 | `MediaCrawler` | source breadth、反风控 | 管理方式不适合作主模板 |

未来方向判断：

1. agent-facing repo surface 会越来越常见
   - certainty：`高`
   - window：`6-12` 个月
2. collector 产品会继续加后台 worker、MCP、CLI 等可编排表面
   - certainty：`高`
   - window：`6-18` 个月
3. source adapter 仓会继续分化成 OSS 核心 + 商业增强层
   - certainty：`高`
   - window：`已经在发生`

## Phase 1：证据搜集 + ACH

### 证据集

E1：`MyTube` 和 ScoutFlow 目标形态最接近：

- 多源
- H5 前端
- SQLite
- layered backend
- 目录结构文档
- deployment security model

来源：

- [README.md](/Users/wanglei/workspace/ScoutFlow/referencerepo/MyTube/README.md)
- [directory-structure.md](/Users/wanglei/workspace/ScoutFlow/referencerepo/MyTube/documents/en/directory-structure.md)
- [deployment-security-model.md](/Users/wanglei/workspace/ScoutFlow/referencerepo/MyTube/documents/en/deployment-security-model.md)

E2：`Karakeep` 主要通过 monorepo 边界、共享 tooling、版本化文档、issue/PR 流程来管理复杂度，而不是靠治理目录。

来源：

- [README.md](/Users/wanglei/workspace/ScoutFlow/referencerepo/karakeep/README.md)
- [architecture.md](/Users/wanglei/workspace/ScoutFlow/referencerepo/karakeep/docs/versioned_docs/version-v0.30.0/08-development/04-architecture.md)
- [directories.md](/Users/wanglei/workspace/ScoutFlow/referencerepo/karakeep/docs/versioned_docs/version-v0.30.0/08-development/02-directories.md)
- [CONTRIBUTING.md](/Users/wanglei/workspace/ScoutFlow/referencerepo/karakeep/CONTRIBUTING.md)

E3：`TubeArchivist` 社区协作很强，但真正承载规则的仍然是 issue template、`pre-commit`、分支纪律、docs，不是厚重治理文件。

来源：

- [README.md](/Users/wanglei/workspace/ScoutFlow/referencerepo/tubearchivist/README.md)
- [CONTRIBUTING.md](/Users/wanglei/workspace/ScoutFlow/referencerepo/tubearchivist/CONTRIBUTING.md)
- [pre_commit.yml](/Users/wanglei/workspace/ScoutFlow/referencerepo/tubearchivist/.github/workflows/pre_commit.yml)

E4：`Pinchflat` 对 scope 说得很清楚：

- 擅长 source-rule 下载
- 明确说自己不是 in-app consumption 产品
- CI 和检查链路很简洁

来源：

- [README.md](/Users/wanglei/workspace/ScoutFlow/referencerepo/pinchflat/README.md)
- [lint_and_test.yml](/Users/wanglei/workspace/ScoutFlow/referencerepo/pinchflat/.github/workflows/lint_and_test.yml)

E5：`MediaCrawler` 的 source adapter 价值很强，甚至有 WebUI，但 repo 管理表面明显弱于其爬虫能力表面。

来源：

- [README.md](/Users/wanglei/workspace/ScoutFlow/referencerepo/MediaCrawler/README.md)
- [项目架构文档.md](</Users/wanglei/workspace/ScoutFlow/referencerepo/MediaCrawler/docs/项目架构文档.md>)

E6：`ArchiveBox` 的 durability 理念和“普通文件 + 多接口共存”最强，但它的范围比 ScoutFlow 更大，容易把设计往通用归档平台拉。

来源：

- [README.md](/Users/wanglei/workspace/ScoutFlow/referencerepo/ArchiveBox/README.md)
- [CLAUDE.md](/Users/wanglei/workspace/ScoutFlow/referencerepo/ArchiveBox/CLAUDE.md)

E7：`MeTube` 是一个有用的下界样本：

- 有 AGENTS 说明
- 有 CI
- 但整体就是很薄的 downloader

来源：

- [README.md](/Users/wanglei/workspace/ScoutFlow/referencerepo/metube/README.md)
- [AGENTS.md](/Users/wanglei/workspace/ScoutFlow/referencerepo/metube/AGENTS.md)
- [main.yml](/Users/wanglei/workspace/ScoutFlow/referencerepo/metube/.github/workflows/main.yml)

### ACH 矩阵

| 证据 | 可信度 | H1 | H2 | H3 | H4 | 诊断性 |
|---|---|---|---|---|---|---|
| E1 MyTube 分层文档 + 安全模型 | HIGH | 支持 | 弱 | 支持 | 削弱重文件治理 | 高 |
| E2 Karakeep monorepo + docs + labels | HIGH | 支持 | 中性 | 支持 | 削弱顶层治理目录方案 | 高 |
| E3 TubeArchivist docs + pre-commit + branch discipline | HIGH | 支持 | 中性 | 支持 | 部分支持更强约束 | 中 |
| E4 Pinchflat 窄 scope + 简洁 CI | HIGH | 支持 | 中性 | 部分支持 | 削弱启动期重治理 | 中 |
| E5 MediaCrawler 强 adapter / 弱管理面 | HIGH | 中性 | 支持 | 部分支持 | 支持“别拿它当管理模板” | 高 |
| E6 ArchiveBox durability + CLAUDE.md | HIGH | 部分支持 | 中性 | 支持 | 说明入口文档重要，但不支持 D-lock 树 | 高 |
| E7 MeTube 极简基线 | MED | 支持 | 中性 | 弱 | 强烈削弱重治理 bootstrap | 中 |

### ACH 解释

最稳的假设：

- H1
- H2
- H3

最弱、最依赖条件的假设：

- H4 的“文件形状”部分

含义：

- Opus 的“原则层”大体成立。
- Opus 的“仓库形状”不能原样成立。

## Phase 2：法庭审理

### 检方

反对当前 Opus 文件计划的最强论据是经验事实：

- 样本里没有任何一个强仓把 `candidates/`、`dispatches/`、`audits/` 做成协作中心
- 即使是多表面、多维护者产品仓，也更依赖 CI、labels、CONTRIBUTING、架构文档、包边界
- ScoutFlow 已经明确要逃离“治理先膨胀”，那就不该再以轻量版行政系统重新走回去

### 辩方

支持 Opus 结论的最强论据不是目录，而是那些坑：

- 多 agent 确实会漂
- source adapter 改动确实有合规和运行风险
- 根部入口文档和 current 状态文件确实能降低 handoff 成本
- RAW 已经证明“可 lint 文档”比口头规则更稳

### 法官判决

- `H1` -> `✅ 成立`，confidence `86`
- `H2` -> `✅ 成立`，confidence `90`
- `H3` -> `⚠️ 部分成立`，confidence `79`
- `H4` -> `⚠️ 部分成立`，confidence `68`

共同盲点：

- 这些参考仓主要是人类团队 OSS 项目，不是完整 multi-agent 开发工作区。ScoutFlow 可能仍需要比它们略强的根部入口文档。

法官自身盲点：

- 目前看到的是 ScoutFlow 的规划漂移风险，不是已经发生的真实代码漂移。

## Phase 3：压力测试

### 3a 预演失败

如果 ScoutFlow 按 Opus 文件治理形状照搬，6 个月后的典型失败可能是：

1. 文档先于代码爆炸。
   - `dispatches/`、`audits/`、`decisions.md`、`current.md`、handoff、amendments 都有了，但还没有一个稳定 adapter 或 UI 主路径。
2. agent 实际上绕开这些文档。
   - 真正的工作仍在代码和 PR 里，治理文件变成仪式。
3. 真源漂移以新形态回来。
   - “官方 markdown”太多，且没有 lint 去兜底。

如果 ScoutFlow 反过来治理削得太轻，6 个月后的典型失败可能是：

1. PRD、schema、runtime path 漂移。
2. RAW 边界或 capture scope 规则被静默修改。
3. 多 agent session 重叠时 handoff 质量崩。

### 3b 最终前提复核

已从未验证转为已验证：

- 强参考仓大多依赖代码 / CI / docs / issue 模板，而不是治理树。
- 收藏 / 采集产品仓确实值得保留 root entry docs。
- crawler repo 不适合当 ScoutFlow 的管理模板。

仍未验证：

- ScoutFlow 在 Phase 1A 前是否真的需要正式 `decisions.md`
- `current.md` 如果没有模板 lint，是否能长期保持有用

### 3c 红队 memo

对领先结论的最强攻击：

> 你现在看到的是“人类 OSS 仓”的管理面，不是“多 agent 工程仓”的管理面。ScoutFlow 既然明确会多 agent 协作，如果现在把流程削太轻，后面很可能只是换个名字重新长回来。更稳的方式不是恢复大治理，而是保留少量控制点，但把它们写成模板和 lint，而不是顶层治理目录。

这个攻击成立，而且应该吸收。

## Phase 4：裁决

### 最终排序

1. `Karakeep`：最强的“产品仓管理方式”参考肩膀。
2. `MyTube`：最强的“ScoutFlow 近邻形态”参考肩膀。
3. `ArchiveBox`：最强的 durability / interface doctrine 肩膀。
4. `TubeArchivist`：运维和社区纪律很强，但更偏单平台 archive。
5. `Pinchflat`：窄范围订阅规则管理器，适合借 rule model，不适合借全控制面。
6. `MediaCrawler`：适合借 adapter，不适合借项目管理。
7. `MeTube`：仅适合作为极简下界。

### 从 Opus 结论里保留什么

保留：

- 不继承 DiloFlow / ContentFlow 的治理重量
- 明确区分代码表面和运行时数据
- 给 agent 明确入口路径
- 能保持单一真源的地方尽量保持单一真源
- 风险改动最好有 preview 和 impact surface
- lint / format / test 应该成为真正约束器

削弱或后置：

- 启动期就放顶层 `candidates/`、`dispatches/`、`audits/`
- 把 `decisions.md` 做成重 contract 文件
- 固定 Codex / Opus / Hermes / OpenClaw 的官职角色表
- 固定 stage gate 和 session-closure 仪式

### 对 ScoutFlow 的实际仓库建议

更合理的重心应该是：

```text
README.md
CLAUDE.md
AGENTS.md
docs/
  project-context.md
  current.md
  specs/
  research/
tools/
  lint-docs
  format-docs
apps/
services/
workers/
data/   # gitignored runtime truth
referencerepo/
```

说明：

- `docs/project-context.md` 比早先的 `decisions.md + _ENTRY-POINTS.md + SOP 分散文档` 更合适。
- 如果后面真的证明需要 `handoffs/` 或 `audits/`，优先加在 `docs/` 下，并且做成薄、可 lint 的子目录，不要一上来做治理纪念碑。
- 如果后面真的需要 decision log，也应该先上薄版 `docs/decision-log.md`，而不是 D-lock 体系。

### 负空间分析

强参考仓“没有做什么”同样重要：

- 它们没有把 amendment 文件变成协作中心
- 它们没有把顶层治理目录变成仓库生命中枢
- 它们没有把流程复杂度误当成工程严谨度

### 置信度

总体结论置信度：`82/100`

主要不确定性：

- 如果 ScoutFlow 很快进入 3+ agent 高频并发改重叠文件，可能仍然需要比样本仓略强的轻治理。

可推翻条件：

- 一旦 ScoutFlow 真实出现并发文档 / 代码漂移，最小化的 `docs/handoffs/` + 更严格的 doc lint 就应立即上马。

## 具体下一步

1. 把肩膀按角色拆开借：
   - 仓库形状：`karakeep`、`MyTube`
   - durability / interface：`ArchiveBox`
   - 订阅 / archive 行为：`pinchflat`、`tubearchivist`
   - source adapter：`MediaCrawler`
   - 最低下界提醒：`metube`
2. ScoutFlow 启动时先上 root entry docs + doc lint，不先上治理队列目录。
3. 写代码时，优先借 `MyTube` 和 `Karakeep` 的目录分层，不借它们的全部产品范围。
4. 先做一个小的 `lint-docs`，检查：
   - `current/spec/handoff/research` 的 frontmatter / 必要字段
   - stale date
   - broken internal links
   - duplicate truth-source 定义
   - 是否误写成“直接写 RAW”
5. `referencerepo/` 保持只读，只在探针研究 session 里刷新。

## 样本与来源

本地克隆：

- `/Users/wanglei/workspace/ScoutFlow/referencerepo/MyTube`
- `/Users/wanglei/workspace/ScoutFlow/referencerepo/tubearchivist`
- `/Users/wanglei/workspace/ScoutFlow/referencerepo/pinchflat`
- `/Users/wanglei/workspace/ScoutFlow/referencerepo/karakeep`
- `/Users/wanglei/workspace/ScoutFlow/referencerepo/ArchiveBox`
- `/Users/wanglei/workspace/ScoutFlow/referencerepo/MediaCrawler`
- `/Users/wanglei/workspace/ScoutFlow/referencerepo/metube`

GitHub 仓库：

- [MyTube](https://github.com/franklioxygen/MyTube)
- [TubeArchivist](https://github.com/tubearchivist/tubearchivist)
- [Pinchflat](https://github.com/kieraneglin/pinchflat)
- [Karakeep](https://github.com/karakeep-app/karakeep)
- [ArchiveBox](https://github.com/ArchiveBox/ArchiveBox)
- [MediaCrawler](https://github.com/NanmiCoder/MediaCrawler)
- [MeTube](https://github.com/alexta69/metube)
