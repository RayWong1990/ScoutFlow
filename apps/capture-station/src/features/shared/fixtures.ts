import type { LifecycleStep } from "../../components/LifecycleStepper/LifecycleStepper";
import type { EvidenceColumn, EvidenceRow } from "../../components/EvidenceTable/EvidenceTable";
import type { PromoteGateItem } from "../../components/PromoteGate/PromoteGate";
import type { TagItem } from "../../components/TagList/TagList";
import type { SyncState } from "../../components/SyncBadge/SyncBadge";

export const urlHistory = [
  {
    captureId: "cap_20260506_8a3f2",
    url: "https://www.bilibili.com/video/BV1xK4y1f7yC",
    time: "14:32 UTC",
    label: "已加载",
  },
  {
    captureId: "cap_20260505_8a243",
    url: "https://www.bilibili.com/video/BV19z4y1m7Qa",
    time: "13:08 UTC",
    label: "已加载",
  },
  {
    captureId: "cap_20260504_8a094",
    url: "https://example.com/article/workflow",
    time: "12:45 UTC",
    label: "已加载",
  },
];

export const metadataFields = [
  { label: "视频标题", value: "深度工作流 vs 普通工作流 — 高效操作员的 5 个习惯" },
  { label: "上传者", value: "@scout_ops_archive" },
  { label: "时长", value: "12:34" },
  { label: "播放量", value: "24,891" },
  { label: "点赞", value: "3,142" },
  { label: "评论", value: "287" },
  { label: "capture_id", value: "cap_20260506_8a3f2" },
  { label: "最后更新", value: "2026-05-06 14:32 UTC" },
] as const;

export const metadataTags: TagItem[] = [
  { label: "深度工作" },
  { label: "操作员" },
  { label: "采集线" },
  { label: "证据入账" },
  { label: "异步协作" },
  { label: "内容研究" },
  { label: "+5 更多", tone: "info" },
];

export const captureScopeStepsStart: LifecycleStep[] = [
  { label: "URL 验证", status: "active" },
  { label: "元数据加载", status: "idle" },
  { label: "正文抓取", status: "idle" },
  { label: "入库预览", status: "idle" },
  { label: "入库提交", status: "idle" },
];

export const captureScopeStepsPreview: LifecycleStep[] = [
  { label: "URL 验证", status: "done" },
  { label: "元数据加载", status: "done" },
  { label: "正文抓取", status: "done" },
  { label: "入库预览", status: "active" },
  { label: "入库提交", status: "idle" },
];

export const captureScopeStepsCommit: LifecycleStep[] = [
  { label: "URL 验证", status: "done" },
  { label: "元数据加载", status: "done" },
  { label: "正文抓取", status: "done" },
  { label: "入库预览", status: "done" },
  { label: "入库提交", status: "active" },
];

export const traceColumns: EvidenceColumn[] = [
  { key: "status", label: "状态" },
  { key: "field", label: "字段" },
  { key: "path", label: "DOM 路径", code: true },
  { key: "value", label: "值" },
  { key: "confidence", label: "置信度" },
] as const;

export const traceRows: EvidenceRow[] = [
  {
    id: "title",
    cells: {
      status: "—",
      field: "title",
      path: "dom.meta.og:title",
      value: "深度工作流 vs 普通工作流 — 高效操作员的 5 个习惯",
      confidence: "98%",
    },
  },
  {
    id: "uploader",
    cells: {
      status: "—",
      field: "uploader",
      path: "dom.handle",
      value: "@scout_ops_archive",
      confidence: "96%",
    },
  },
  {
    id: "duration",
    cells: {
      status: "—",
      field: "duration",
      path: "json.ld.duration",
      value: "12:34",
      confidence: "92%",
    },
  },
  {
    id: "error-path",
    tone: "error",
    cells: {
      status: "blocked",
      field: "comments",
      path: "dom.stats.comment",
      value: "287",
      confidence: "89%",
    },
  },
];

export const previewMarkdown = `---
title: 深度工作流 vs 普通工作流 — 高效操作员的 5 个习惯
capture_id: cap_20260506_8a3f2
status: preview_only
write_enabled: false
vault_target: ~/workspace/raw/00-Inbox/
---
`;

export const previewFrontmatterFields = [
  { label: "title", value: "深度工作流 vs 普通工作流 — 高效操作员的 5 个习惯" },
  { label: "capture_id", value: "cap_20260506_8a3f2" },
  { label: "status", value: "preview_only" },
  { label: "write_enabled", value: "false" },
] as const;

export const syncCards: Array<{ captureId: string; title: string; state: SyncState }> = [
  { captureId: "cap_20260506_8a3f2", title: "深度工作流", state: "synced" },
  { captureId: "cap_20260506_91b7c", title: "异步协作", state: "pending" },
  { captureId: "cap_20260506_a02ef", title: "知识飞轮", state: "external-changed" },
];

export const promoteGateItems: PromoteGateItem[] = [
  { label: "信号 ≥ 3", status: "met" },
  { label: "假设 ≥ 1", status: "met" },
  { label: "证据已链接", status: "met" },
  { label: "操作员已标记有用", status: "met" },
];

export const signalRows = [
  {
    title: "异步协作降低上下文切换成本",
    score: "76.4%",
    hypotheses: ["高频采集场景中，异步优先减少即时响应压力。", "证据先入账再判断，能降低误判。", "选题卡可作为内容生产前置缓冲。"],
  },
  {
    title: "同步确认更可靠",
    score: "43.1%",
    hypotheses: ["人工裁决能避免错误晋升。", "跨系统同步可能引入额外确认成本。"],
  },
];

export const capturePlanHooks = [
  { label: "URL 校验通过", status: "met" },
  { label: "Frontmatter 结构通过", status: "met" },
  { label: "评论抓取未请求", status: "pending" },
  { label: "写入开关关闭", status: "pending" },
] as const;

export const executionLogRows: EvidenceRow[] = [
  {
    id: "run-start",
    cells: {
      time: "2026-05-06 14:32 UTC",
      event: "run_start",
      note: "开始执行计划",
    },
  },
  {
    id: "capture",
    cells: {
      time: "2026-05-06 14:34 UTC",
      event: "capture",
      note: "12 条采集完成",
    },
  },
  {
    id: "topic-card",
    cells: {
      time: "2026-05-06 14:36 UTC",
      event: "topic_card",
      note: "14 张选题卡生成",
    },
  },
  {
    id: "error",
    tone: "error",
    cells: {
      time: "2026-05-06 14:38 UTC",
      event: "error",
      note: "1 条 URL 超时",
    },
  },
  {
    id: "done",
    cells: {
      time: "2026-05-06 14:39 UTC",
      event: "done",
      note: "最终状态: 仅预览",
    },
  },
];

export const executionLogColumns: EvidenceColumn[] = [
  { key: "time", label: "时间", code: true },
  { key: "event", label: "事件", code: true },
  { key: "note", label: "说明" },
];
