# PF-V P7 输出包 — Rough HTML5 Wireframe Bundle

本输出包由 65 张 ScoutFlow 采集线视觉 mockup 转换而来，定位是给 PF-C4-01 Local Frontend Bootstrap 继续翻译为 React TSX 的结构参考包。

## 零安装使用方式

1. 解压本目录。
2. 直接用浏览器打开任意 `html5-rough/*.html`，检查结构、状态段落与扫描顺序。
3. 查看 `tokens.css`，它是颜色、字体、间距、圆角、阴影与状态底色的唯一 token 来源。

## 文件结构

- `tokens.css` — 全局设计 token：15 个主色 token、字体、字号、间距、圆角、阴影、状态底色。
- `density-compact.css` — V3 紧凑密度覆盖文件。
- `type-weight-heavy.css` — V4 高字重覆盖文件。
- `html5-rough/*.html` — 13 个 surface HTML5 wireframe。
- `html5-rough/*.module.css` — 与 surface 同目录的浏览器可打开样式文件。
- `html5-rough/*.model.json` — 每个 surface group 的 Step 1 JSON UI structural model。
- `css-modules-candidate/*.module.css` + `*.html` — 15 个复用组件候选及用法片段。
- `icons/system.svg` — 10 个系统操作图标 symbol。
- `icons/state.svg` — 10 个状态图标 symbol。
- `MAPPING.md` — 65 张输入图到输出文件的映射。
- `README.md` — 本说明文件。

## PF-C4 消费建议

1. 先读 `html5-rough/*.model.json`，确认每个 surface 的区域、状态、复用组件与图标引用。
2. 再打开 `html5-rough/*.html`，验证 IA、状态 modifier、语义标签和中文 UI 文案。
3. 将 HTML 结构翻译为 React TSX，按 PF-C4 项目约定拆分组件。
4. 将 `*.module.css` 候选迁移为真实 CSS Modules；所有颜色继续引用 `tokens.css` 变量。
5. 将 SVG sprite 的 `<symbol>` 转换为项目内图标系统或继续通过 `<use>` 引用。
6. 替换 TODO 占位：图谱、时间轴、缩略图数据与真实后端状态接线。

## PF-C4 需要关注的 TODO 占位

| 文件 | 行号 | 原因 |
|---|---:|---|
| `html5-rough/02-live-metadata.html` | 69 | 来源图 `task-10_thumbnail-field.png` 包含视频缩略图；PF-C4 应从 BBDown 抽取的元数据中接入真实缩略图。 |
| `html5-rough/04-trust-trace.html` | 21 | 来源图 `task-14_filter-dom-only.png` 包含复杂 DOM 图谱；PF-C4 应使用 D3 / vis-network / cytoscape 等图谱库实现。 |
| `html5-rough/04-trust-trace.html` | 40 | 来源图 `task-15_time-axis.png` 包含时间轴；PF-C4 应实现 hover 时间戳与证据定位。 |
| `html5-rough/04-trust-trace.html` | 64 | 来源图 `task-16_error-path.png` 包含错误路径高亮；PF-C4 应在图谱实现中接入高亮路径。 |

## 禁止事项

- 不要把这些 HTML 当作运行时代码直接引入生产应用；它们只是 rough wireframe。
- 不要不加审查地照搬 class name；PF-C4 应按项目组件命名规则迁移。
- 不要在 `tokens.css` 外硬编码 hex 颜色。
- 不要引入 Tailwind / shadcn / npm 包；本包是零安装参考物。
- 不要改变入库语义：ScoutFlow 只把干净 Markdown 交付到 `~/workspace/raw/00-Inbox/`，后续增强、双链回填与知识飞轮由 Obsidian 接管。

## 自检摘要

- 65 张输入 PNG 已全部枚举并写入 `MAPPING.md`。
- 13 个 surface HTML 已生成，均包含对应状态 modifier section。
- 13 个 JSON UI structural model 已生成，用于 PF-C4 先审结构再转 TSX。
- 15 个组件候选已抽取为 `.module.css` + `.html` 配对文件。
- 2 个 SVG sprite 已生成，每个 sprite 含 10 个 `<symbol>`。
- 生成 HTML 的可见 UI chrome 已按简体中文处理；URL、ID、路径、YAML key、DOM-path 字段名保留原始代码格式。
- 入库路径统一使用 `~/workspace/raw/00-Inbox/`。
