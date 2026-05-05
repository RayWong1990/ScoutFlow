type PreviewMetric = {
  label: string;
  value: string;
  tone: "support" | "counter" | "process";
};

type ReviewStep = {
  label: string;
  state: "ready" | "deferred" | "needs_review";
};

type TopicCardPreviewCandidateData = {
  title: string;
  hypothesisSummary: string;
  reviewState: "mapped" | "reviewed";
  exportPosture: "local_only" | "handoff_candidate";
  metrics: PreviewMetric[];
  reviewSteps: ReviewStep[];
  counterNote: string;
};

const toneColors = {
  support: "#7adf9b",
  counter: "#ff9b7a",
  process: "#50d4ff",
} as const;

const stepColors = {
  ready: "#7adf9b",
  deferred: "#ffbe55",
  needs_review: "#50d4ff",
} as const;

const placeholderData: TopicCardPreviewCandidateData = {
  title: "ScoutFlow topic-card candidate",
  hypothesisSummary: "metadata proof is enough to frame a review card, but not enough to claim human visual clarity.",
  reviewState: "mapped",
  exportPosture: "local_only",
  metrics: [
    { label: "strength", value: "evidence_sufficient", tone: "support" },
    { label: "coverage", value: "metadata + trust-trace", tone: "process" },
    { label: "risk", value: "missing visual verdict", tone: "counter" },
  ],
  reviewSteps: [
    { label: "intake shell", state: "ready" },
    { label: "evidence review", state: "needs_review" },
    { label: "retain or defer", state: "deferred" },
  ],
  counterNote: "Counter-evidence stays visible: no screenshot packet, no browser-run proof, no publish action.",
};

type TopicCardPreviewCandidateProps = {
  data?: TopicCardPreviewCandidateData;
};

export default function TopicCardPreviewCandidate({ data = placeholderData }: TopicCardPreviewCandidateProps) {
  return (
    <section
      data-testid="topic-card-preview-candidate"
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
          <p style={{ margin: 0, color: "#6d8099", fontSize: "12px" }}>topic-card-preview</p>
          <h2 style={{ margin: "8px 0 6px", fontSize: "20px", lineHeight: 1.15 }}>{data.title}</h2>
          <p style={{ margin: 0, color: "#a6b8cf", fontSize: "14px", lineHeight: 1.5 }}>{data.hypothesisSummary}</p>
        </div>

        <div style={{ display: "grid", gap: "8px", justifyItems: "end" }}>
          <span
            style={{
              borderRadius: "999px",
              border: "1px solid #50d4ff",
              color: "#50d4ff",
              padding: "6px 10px",
              fontSize: "12px",
              background: "#16263c",
            }}
          >
            {data.reviewState}
          </span>
          <span
            style={{
              borderRadius: "999px",
              border: "1px solid #27415d",
              color: "#ffcf7a",
              padding: "6px 10px",
              fontSize: "12px",
              background: "#16263c",
            }}
          >
            {data.exportPosture}
          </span>
        </div>
      </header>

      <div style={{ display: "grid", gridTemplateColumns: "minmax(0, 1.05fr) minmax(0, 0.95fr)", gap: "14px" }}>
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
            <h3 style={{ margin: 0, fontSize: "14px", lineHeight: 1.3 }}>Preview metrics</h3>
            <span style={{ color: "#6d8099", fontSize: "12px" }}>candidate vocabulary only</span>
          </div>

          <div style={{ display: "grid", gridTemplateColumns: "repeat(3, minmax(0, 1fr))", gap: "10px" }}>
            {data.metrics.map((metric) => (
              <div
                key={metric.label}
                style={{
                  borderRadius: "8px",
                  border: "1px solid #27415d",
                  background: "#101d2e",
                  padding: "10px",
                  display: "grid",
                  gap: "6px",
                }}
              >
                <span style={{ color: "#6d8099", fontSize: "12px" }}>{metric.label}</span>
                <strong style={{ color: toneColors[metric.tone], fontSize: "13px", lineHeight: 1.35 }}>{metric.value}</strong>
              </div>
            ))}
          </div>

          <div
            style={{
              borderRadius: "8px",
              border: "1px solid #3d3043",
              background: "#171320",
              padding: "12px",
            }}
          >
            <p style={{ margin: 0, color: "#ffb5a1", fontSize: "13px", lineHeight: 1.45 }}>{data.counterNote}</p>
          </div>
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
          <div style={{ display: "flex", justifyContent: "space-between", gap: "12px", alignItems: "center" }}>
            <h3 style={{ margin: 0, fontSize: "14px", lineHeight: 1.3 }}>Review flow</h3>
            <span style={{ color: "#6d8099", fontSize: "12px" }}>manual-first</span>
          </div>

          {data.reviewSteps.map((step, index) => (
            <div key={step.label} style={{ display: "grid", gridTemplateColumns: "24px minmax(0, 1fr)", gap: "10px" }}>
              <div style={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
                <span
                  style={{
                    width: "12px",
                    height: "12px",
                    borderRadius: "999px",
                    marginTop: "4px",
                    background: stepColors[step.state],
                  }}
                />
                {index < data.reviewSteps.length - 1 ? (
                  <span style={{ width: "2px", flex: 1, minHeight: "24px", marginTop: "4px", background: "#27415d" }} />
                ) : null}
              </div>

              <div
                style={{
                  borderRadius: "8px",
                  border: "1px solid #27415d",
                  background: "#101d2e",
                  padding: "10px",
                  display: "flex",
                  justifyContent: "space-between",
                  gap: "10px",
                  alignItems: "center",
                }}
              >
                <strong style={{ fontSize: "13px", lineHeight: 1.35 }}>{step.label}</strong>
                <span
                  style={{
                    borderRadius: "999px",
                    border: `1px solid ${stepColors[step.state]}`,
                    color: stepColors[step.state],
                    padding: "3px 8px",
                    fontSize: "11px",
                    textTransform: "uppercase",
                  }}
                >
                  {step.state}
                </span>
              </div>
            </div>
          ))}
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
          This preview exposes reviewable structure only. It does not call topic-card APIs or change the four-panel shell.
        </p>
        <p style={{ margin: 0, color: "#6d8099", fontSize: "12px" }}>
          `deferred_visual_evidence`: screenshot packet and human verdict remain out of scope for this dispatch.
        </p>
      </footer>
    </section>
  );
}
