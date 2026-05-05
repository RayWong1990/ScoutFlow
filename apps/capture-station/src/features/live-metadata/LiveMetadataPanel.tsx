const metadataRows = [
  { label: "Platform", value: "bilibili" },
  { label: "Probe mode", value: "auth-present fixture" },
  { label: "Evidence task", value: "T-P1A-011C" },
  { label: "audio_transcript", value: "blocked" }
];

export default function LiveMetadataPanel() {
  return (
    <section
      data-testid="panel-live-metadata"
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
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <div>
          <p style={{ margin: 0, color: "#6d8099", fontSize: "12px" }}>live-metadata</p>
          <h2 style={{ margin: "8px 0 0", fontSize: "20px", lineHeight: 1.15 }}>Live Metadata</h2>
        </div>
        <span
          style={{
            borderRadius: "999px",
            border: "1px solid #27415d",
            background: "#16263c",
            color: "#50d4ff",
            padding: "6px 10px",
            fontSize: "12px"
          }}
        >
          fixture only
        </span>
      </div>

      <p style={{ margin: 0, color: "#a6b8cf", fontSize: "14px", lineHeight: 1.45 }}>
        This panel surfaces safe metadata placeholders and evidence provenance. It does not unlock live BBDown runtime.
      </p>

      <dl
        style={{
          display: "grid",
          gridTemplateColumns: "minmax(0, 120px) minmax(0, 1fr)",
          gap: "10px 16px",
          margin: 0
        }}
      >
        {metadataRows.map((row) => (
          <div key={row.label} style={{ display: "contents" }}>
            <dt style={{ color: "#6d8099", fontSize: "12px" }}>{row.label}</dt>
            <dd style={{ margin: 0, color: "#eef4ff", fontSize: "14px" }}>{row.value}</dd>
          </div>
        ))}
      </dl>

      <div
        style={{
          marginTop: "auto",
          borderRadius: "8px",
          border: "1px solid #27415d",
          background: "#0b1624",
          padding: "12px"
        }}
      >
        <p style={{ margin: 0, color: "#6d8099", fontSize: "12px" }}>Safe surfaced fields</p>
        <p style={{ margin: "6px 0 0", color: "#a6b8cf", fontSize: "14px", lineHeight: 1.45 }}>
          title, duration, page_count, selected_page, and trust-trace provenance summary.
        </p>
      </div>
    </section>
  );
}
