import { useState } from "react";

import AppShell from "./components/AppShell/AppShell";
import AppShellOverview from "./components/AppShell/AppShellOverview";
import CapturePlan from "./features/capture-plan/CapturePlan";
import CaptureScope from "./features/capture-scope/CaptureScope";
import DensitySpec from "./features/_specs/DensitySpec";
import TypeSpec from "./features/_specs/TypeSpec";
import LiveMetadata from "./features/live-metadata/LiveMetadata";
import SignalHypothesis from "./features/signal-hypothesis/SignalHypothesis";
import TrustTrace from "./features/trust-trace/TrustTrace";
import TopicCardLite from "./features/topic-card-preview/TopicCardLite";
import TopicCardVault from "./features/topic-card-vault/TopicCardVault";
import UrlBar from "./features/url-bar/UrlBar";
import VaultCommit from "./features/vault-commit/VaultCommit";
import VaultPreview from "./features/vault-preview/VaultPreview";

const surfaces = [
  { id: "00-app-shell", title: "00 App Shell", caption: "工作站总览" },
  { id: "01-url-bar", title: "01 URL Bar", caption: "输入、校验、历史" },
  { id: "02-live-metadata", title: "02 Live Metadata", caption: "元数据状态集" },
  { id: "03-capture-scope", title: "03 Capture Scope", caption: "生命周期与边界" },
  { id: "04-trust-trace", title: "04 Trust Trace", caption: "图谱 / 时间轴 / 错误路径" },
  { id: "05-vault-preview", title: "05 Vault Preview", caption: "预览与 frontmatter" },
  { id: "06-vault-commit", title: "06 Vault Commit", caption: "干跑与弹窗" },
  { id: "07-topic-card-lite", title: "07 Topic Card Lite", caption: "新闻 / 视频 / 对比" },
  { id: "08-topic-card-vault", title: "08 Topic Card Vault", caption: "聚合 / promote / sync" },
  { id: "09-signal-hypothesis", title: "09 Signal / Hypothesis", caption: "展开 / 对比 / 生命周期" },
  { id: "10-capture-plan", title: "10 Capture Plan", caption: "I/O / 干跑 / 日志" },
  { id: "11-density-spec", title: "11 Density Spec", caption: "V3 compact reference" },
  { id: "12-type-spec", title: "12 Type Spec", caption: "V4 weight-heavy reference" },
] as const;

export default function App() {
  const [current, setCurrent] = useState<(typeof surfaces)[number]["id"]>("00-app-shell");

  const currentSurface =
    current === "00-app-shell" ? <AppShellOverview /> :
    current === "01-url-bar" ? <UrlBar /> :
    current === "02-live-metadata" ? <LiveMetadata /> :
    current === "03-capture-scope" ? <CaptureScope /> :
    current === "04-trust-trace" ? <TrustTrace /> :
    current === "05-vault-preview" ? <VaultPreview /> :
    current === "06-vault-commit" ? <VaultCommit /> :
    current === "07-topic-card-lite" ? <TopicCardLite /> :
    current === "08-topic-card-vault" ? <TopicCardVault /> :
    current === "09-signal-hypothesis" ? <SignalHypothesis /> :
    current === "10-capture-plan" ? <CapturePlan /> :
    current === "11-density-spec" ? <DensitySpec /> :
    <TypeSpec />;

  return (
    <AppShell current={current} onSelect={(id) => setCurrent(id as (typeof surfaces)[number]["id"])} surfaces={[...surfaces]}>
      {currentSurface}
    </AppShell>
  );
}
