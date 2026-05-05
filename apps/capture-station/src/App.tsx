import { Suspense, lazy, type ComponentType } from "react";

type ShellModule = { default: ComponentType };

const shellModules = import.meta.glob<ShellModule>("./layout/FourPanelShell.tsx");
const shellLoader = shellModules["./layout/FourPanelShell.tsx"];
const LazyShell = shellLoader ? lazy(shellLoader as () => Promise<ShellModule>) : null;

const fallbackPanels = [
  {
    id: "url-bar",
    title: "Manual URL",
    body: "等待 URL Bar panel 接管输入边界。"
  },
  {
    id: "live-metadata",
    title: "Live Metadata",
    body: "等待 metadata panel 接管占位数据。"
  },
  {
    id: "capture-scope",
    title: "Capture Scope",
    body: "等待 scope panel 接管 blocked/pending 视图。"
  },
  {
    id: "trust-trace",
    title: "Trust Trace",
    body: "等待 trust trace graph 接管投影视图。"
  }
];

function StaticFallbackShell() {
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
            Wave 4 B2 scaffold. Four-panel shell will be progressively mounted by later slots.
          </p>
        </header>

        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(2, minmax(0, 1fr))",
            gap: "24px"
          }}
        >
          {fallbackPanels.map((panel) => (
            <section
              key={panel.id}
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
              <p style={{ margin: 0, color: "#a6b8cf", fontSize: "14px", lineHeight: 1.45 }}>{panel.body}</p>
            </section>
          ))}
        </div>
      </section>
    </main>
  );
}

export default function App() {
  if (!LazyShell) {
    return <StaticFallbackShell />;
  }

  return (
    <Suspense fallback={<StaticFallbackShell />}>
      <LazyShell />
    </Suspense>
  );
}
