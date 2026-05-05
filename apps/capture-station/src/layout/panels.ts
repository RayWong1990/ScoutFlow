export type CaptureStationPanelId =
  | "url-bar"
  | "live-metadata"
  | "capture-scope"
  | "trust-trace";

export type CaptureStationPanelSpec = {
  id: CaptureStationPanelId;
  title: string;
  description: string;
  modulePath: string;
};

export const PANEL_SPECS: CaptureStationPanelSpec[] = [
  {
    id: "url-bar",
    title: "Manual URL",
    description: "Capture creation entrypoint for manual_url only.",
    modulePath: "../features/url-bar/UrlBar.tsx"
  },
  {
    id: "live-metadata",
    title: "Live Metadata",
    description: "BBDown-safe placeholder metadata surface.",
    modulePath: "../features/live-metadata/LiveMetadataPanel.tsx"
  },
  {
    id: "capture-scope",
    title: "Capture Scope",
    description: "Blocked and allowed lanes stay visible in one panel.",
    modulePath: "../features/capture-scope/CaptureScopePanel.tsx"
  },
  {
    id: "trust-trace",
    title: "Trust Trace",
    description: "Projection-only graph of receipt and audit layers.",
    modulePath: "../features/trust-trace/TrustTraceGraph.tsx"
  }
];
