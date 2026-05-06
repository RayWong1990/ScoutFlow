import { buildPlaceholderTopicCardVaultCandidateData, type TopicCardVaultCandidateData } from "./topicCardVaultCandidateData";

const stanceColors = {
  support: "#7adf9b",
  counter: "#ff9b7a",
  process: "#50d4ff",
} as const;

type TopicCardVaultCandidateProps = {
  data?: TopicCardVaultCandidateData;
};

export default function TopicCardVaultCandidate({
  data = buildPlaceholderTopicCardVaultCandidateData(),
}: TopicCardVaultCandidateProps) {
  return (
    <section
      data-testid="topic-card-vault-candidate"
      style={{
        minHeight: "320px",
        borderRadius: "8px",
        border: "1px solid #27415d",
        background: "#111f31",
        padding: "16px",
        display: "grid",
        gap: "14px",
      }}
    >
      <header style={{ display: "flex", justifyContent: "space-between", gap: "12px", alignItems: "flex-start" }}>
        <div style={{ minWidth: 0 }}>
          <p style={{ margin: 0, color: "#6d8099", fontSize: "12px" }}>topic-card-vault</p>
          <h2 style={{ margin: "8px 0 6px", fontSize: "20px", lineHeight: 1.15 }}>{data.title}</h2>
          <p style={{ margin: 0, color: "#a6b8cf", fontSize: "14px", lineHeight: 1.5 }}>{data.hypothesisSummary}</p>
        </div>

        <div style={{ display: "grid", gap: "8px", justifyItems: "end" }}>
          <span
            style={{
              borderRadius: "999px",
              border: "1px solid #ffcf7a",
              color: "#ffcf7a",
              padding: "6px 10px",
              fontSize: "12px",
              background: "#16263c",
            }}
          >
            {data.gate}
          </span>
          <span
            style={{
              borderRadius: "999px",
              border: "1px solid #27415d",
              color: "#50d4ff",
              padding: "6px 10px",
              fontSize: "12px",
              background: "#16263c",
            }}
          >
            {data.exportPosture}
          </span>
        </div>
      </header>

      <div style={{ display: "grid", gridTemplateColumns: "minmax(0, 0.95fr) minmax(0, 1.05fr)", gap: "14px" }}>
        <article
          style={{
            borderRadius: "8px",
            border: "1px solid #27415d",
            background: "#0b1624",
            padding: "12px",
            display: "grid",
            gap: "10px",
          }}
        >
          <div style={{ display: "flex", justifyContent: "space-between", gap: "12px", alignItems: "center" }}>
            <h3 style={{ margin: 0, fontSize: "14px", lineHeight: 1.3 }}>Evidence balance</h3>
            <span style={{ color: "#6d8099", fontSize: "12px" }}>{data.evidence.length} lanes</span>
          </div>

          {data.evidence.map((row) => (
            <div
              key={row.label}
              style={{
                borderRadius: "8px",
                border: "1px solid #27415d",
                background: "#101d2e",
                padding: "10px",
              }}
            >
              <div style={{ display: "flex", justifyContent: "space-between", gap: "10px", alignItems: "center" }}>
                <strong style={{ fontSize: "13px", lineHeight: 1.35 }}>{row.label}</strong>
                <span
                  style={{
                    borderRadius: "999px",
                    border: `1px solid ${stanceColors[row.stance]}`,
                    color: stanceColors[row.stance],
                    padding: "3px 8px",
                    fontSize: "11px",
                    textTransform: "uppercase",
                  }}
                >
                  {row.stance}
                </span>
              </div>
              <p style={{ margin: "8px 0 0", color: "#a6b8cf", fontSize: "13px", lineHeight: 1.45 }}>{row.note}</p>
            </div>
          ))}
        </article>

        <article
          style={{
            borderRadius: "8px",
            border: "1px solid #27415d",
            background: "#0b1624",
            padding: "12px",
            display: "grid",
            gap: "10px",
          }}
        >
          <div style={{ display: "grid", gap: "6px" }}>
            <div style={{ display: "flex", justifyContent: "space-between", gap: "12px", alignItems: "center" }}>
              <h3 style={{ margin: 0, fontSize: "14px", lineHeight: 1.3 }}>Markdown preview</h3>
              <span style={{ color: "#6d8099", fontSize: "12px" }}>vault candidate only</span>
            </div>
            <p style={{ margin: 0, color: "#6d8099", fontSize: "12px", wordBreak: "break-all" }}>{data.targetPath}</p>
          </div>

          <pre
            style={{
              margin: 0,
              borderRadius: "8px",
              border: "1px solid #27415d",
              background: "#07111b",
              color: "#d8e3f2",
              padding: "12px",
              fontSize: "12px",
              lineHeight: 1.55,
              whiteSpace: "pre-wrap",
            }}
          >
            {data.markdownPreview}
          </pre>
        </article>
      </div>

      <footer
        style={{
          borderRadius: "8px",
          border: "1px solid #27415d",
          background: "#0b1624",
          padding: "12px",
          display: "grid",
          gap: "6px",
        }}
      >
        <p style={{ margin: 0, color: "#eef4ff", fontSize: "13px" }}>
          Vault write remains disabled. This candidate prepares a reviewable bundle shape, not a commit path.
        </p>
        <p style={{ margin: 0, color: "#6d8099", fontSize: "12px" }}>
          `deferred_visual_evidence`: desktop / tablet / mobile screenshot packet still requires separate authorization.
        </p>
      </footer>
    </section>
  );
}
