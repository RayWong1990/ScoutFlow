import { Suspense, lazy, type ComponentType } from "react";

import { PANEL_SPECS, type CaptureStationPanelSpec } from "./panels";

type PanelModule = { default: ComponentType };

const panelModules = import.meta.glob<PanelModule>(["../features/**/*.tsx", "!../features/**/*.test.tsx"]);

function FallbackPanel({ panel }: { panel: CaptureStationPanelSpec }) {
  return (
    <section
      data-testid={`panel-${panel.id}`}
      style={{
        minHeight: "220px",
        borderRadius: "8px",
        border: "1px solid #27415d",
        background: "#111f31",
        padding: "16px"
      }}
    >
      <p style={{ margin: 0, color: "#6d8099", fontSize: "12px" }}>{panel.id}</p>
      <h2 style={{ margin: "8px 0 12px", fontSize: "20px", lineHeight: 1.15 }}>{panel.title}</h2>
      <p style={{ margin: 0, color: "#a6b8cf", fontSize: "14px", lineHeight: 1.45 }}>{panel.description}</p>
    </section>
  );
}

function PanelSurface({ panel }: { panel: CaptureStationPanelSpec }) {
  const loader = panelModules[panel.modulePath];
  if (!loader) {
    return <FallbackPanel panel={panel} />;
  }

  const LazyPanel = lazy(loader as () => Promise<PanelModule>);
  return (
    <Suspense fallback={<FallbackPanel panel={panel} />}>
      <LazyPanel />
    </Suspense>
  );
}

export default function FourPanelShell() {
  return (
    <main
      style={{
        minHeight: "100vh",
        background: "#07111b",
        color: "#eef4ff",
        fontFamily: 'Inter, "PingFang SC", "Helvetica Neue", sans-serif',
        padding: "24px"
      }}
    >
      <section
        style={{
          maxWidth: "1360px",
          margin: "0 auto",
          border: "1px solid #1d3148",
          borderRadius: "8px",
          background: "#0d1826",
          boxShadow: "0 24px 48px rgba(0, 0, 0, 0.32)",
          padding: "24px"
        }}
      >
        <header style={{ marginBottom: "24px" }}>
          <p style={{ margin: 0, color: "#50d4ff", fontSize: "12px", letterSpacing: 0 }}>ScoutFlow</p>
          <h1 style={{ margin: "8px 0 4px", fontSize: "28px", lineHeight: 1.1 }}>Capture Station</h1>
          <p style={{ margin: 0, color: "#a6b8cf", fontSize: "14px", lineHeight: 1.45 }}>
            Four-panel shell mounted under explicit dispatch-only frontend lane.
          </p>
        </header>

        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(2, minmax(0, 1fr))",
            gap: "24px"
          }}
        >
          {PANEL_SPECS.map((panel) => (
            <PanelSurface key={panel.id} panel={panel} />
          ))}
        </div>
      </section>
    </main>
  );
}
