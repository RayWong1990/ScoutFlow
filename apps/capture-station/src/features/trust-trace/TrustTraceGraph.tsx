type TraceNode = {
  id: string;
  title: string;
  state: "ready" | "pending" | "blocked";
};

const nodes: TraceNode[] = [
  { id: "capture", title: "Capture", state: "ready" },
  { id: "metadata-job", title: "Metadata Job", state: "ready" },
  { id: "probe-evidence", title: "Probe Evidence", state: "ready" },
  { id: "receipt-ledger", title: "Receipt Ledger", state: "pending" },
  { id: "media-audio", title: "Media Audio", state: "blocked" }
];

const stateColors = {
  ready: "#7adf9b",
  pending: "#ffbe55",
  blocked: "#ff7b7b"
} as const;

export default function TrustTraceGraph() {
  return (
    <section
      data-testid="panel-trust-trace"
      style={{
        minHeight: "220px",
        borderRadius: "8px",
        border: "1px solid #27415d",
        background: "#111f31",
        padding: "16px",
        display: "flex",
        flexDirection: "column",
        gap: "12px"
      }}
    >
      <p style={{ margin: 0, color: "#6d8099", fontSize: "12px" }}>trust-trace</p>
      <h2 style={{ margin: 0, fontSize: "20px", lineHeight: 1.15 }}>Trust Trace</h2>
      <p style={{ margin: 0, color: "#a6b8cf", fontSize: "14px", lineHeight: 1.45 }}>
        Projection-only graph. The panel visualizes receipt layers but does not write authority or unlock runtime.
      </p>

      <div style={{ display: "grid", gap: "10px" }}>
        {nodes.map((node, index) => (
          <div key={node.id} style={{ display: "grid", gridTemplateColumns: "24px minmax(0, 1fr)", gap: "12px" }}>
            <div style={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
              <span
                style={{
                  width: "12px",
                  height: "12px",
                  borderRadius: "999px",
                  marginTop: "4px",
                  background: stateColors[node.state]
                }}
              />
              {index < nodes.length - 1 ? (
                <span
                  style={{
                    width: "2px",
                    flex: 1,
                    minHeight: "26px",
                    marginTop: "4px",
                    background: "#27415d"
                  }}
                />
              ) : null}
            </div>

            <article
              style={{
                borderRadius: "8px",
                border: "1px solid #27415d",
                background: "#0b1624",
                padding: "12px"
              }}
            >
              <div style={{ display: "flex", justifyContent: "space-between", gap: "12px", alignItems: "center" }}>
                <h3 style={{ margin: 0, fontSize: "14px", lineHeight: 1.3 }}>{node.title}</h3>
                <span
                  style={{
                    borderRadius: "999px",
                    border: `1px solid ${stateColors[node.state]}`,
                    color: stateColors[node.state],
                    padding: "4px 8px",
                    fontSize: "11px",
                    textTransform: "uppercase"
                  }}
                >
                  {node.state}
                </span>
              </div>
              <p style={{ margin: "8px 0 0", color: "#a6b8cf", fontSize: "13px", lineHeight: 1.45 }}>
                {node.id === "media-audio"
                  ? "audio_transcript remains blocked and stays outside the current runtime lane."
                  : "Current phase keeps this layer visible for operator scanning and downstream audit."}
              </p>
            </article>
          </div>
        ))}
      </div>
    </section>
  );
}
