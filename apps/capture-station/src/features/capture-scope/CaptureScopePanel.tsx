type ScopeRow = {
  label: string;
  status: "allowed" | "blocked" | "candidate";
  note: string;
};

const scopeRows: ScopeRow[] = [
  {
    label: "manual_url / metadata_only",
    status: "allowed",
    note: "Single discover-path entry approved in the current phase."
  },
  {
    label: "recommendation / keyword / RAW gap",
    status: "blocked",
    note: "Cannot create captures directly."
  },
  {
    label: "audio_transcript",
    status: "blocked",
    note: "Runtime remains blocked."
  },
  {
    label: "DB vNext / migration dry-run",
    status: "candidate",
    note: "Candidate-only; requires explicit later gate."
  }
];

const statusColors = {
  allowed: "#7adf9b",
  blocked: "#ff7b7b",
  candidate: "#ffbe55"
} as const;

export default function CaptureScopePanel() {
  return (
    <section
      data-testid="panel-capture-scope"
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
      <p style={{ margin: 0, color: "#6d8099", fontSize: "12px" }}>capture-scope</p>
      <h2 style={{ margin: 0, fontSize: "20px", lineHeight: 1.15 }}>Capture Scope</h2>
      <p style={{ margin: 0, color: "#a6b8cf", fontSize: "14px", lineHeight: 1.45 }}>
        The station can show blocked and candidate lanes, but it must not imply runtime unlock where the authority says no.
      </p>

      <div style={{ display: "grid", gap: "10px" }}>
        {scopeRows.map((row) => (
          <article
            key={row.label}
            style={{
              borderRadius: "8px",
              border: "1px solid #27415d",
              background: "#0b1624",
              padding: "12px"
            }}
          >
            <div style={{ display: "flex", justifyContent: "space-between", gap: "12px", alignItems: "center" }}>
              <h3 style={{ margin: 0, fontSize: "14px", lineHeight: 1.3 }}>{row.label}</h3>
              <span
                style={{
                  borderRadius: "999px",
                  border: `1px solid ${statusColors[row.status]}`,
                  color: statusColors[row.status],
                  padding: "4px 8px",
                  fontSize: "11px",
                  textTransform: "uppercase"
                }}
              >
                {row.status}
              </span>
            </div>
            <p style={{ margin: "8px 0 0", color: "#a6b8cf", fontSize: "13px", lineHeight: 1.45 }}>{row.note}</p>
          </article>
        ))}
      </div>
    </section>
  );
}
