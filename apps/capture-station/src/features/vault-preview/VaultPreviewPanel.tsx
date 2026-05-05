import type { BridgeVaultPreviewResponse } from "../../lib/api-client";

const placeholderPreview: BridgeVaultPreviewResponse = {
  capture_id: "cap_placeholder",
  target_path: "/tmp/scoutflow-vault/00-Inbox/scoutflow-cap_placeholder-bv1placeholder.md",
  frontmatter: {
    title: "ScoutFlow BV1PLACEHOLDER",
    date: "2026-05-05",
    tags: "调研/ScoutFlow采集",
    status: "pending"
  },
  body_markdown: [
    "# ScoutFlow BV1PLACEHOLDER",
    "",
    "- capture_id: `cap_placeholder`",
    "- platform_item_id: `BV1PLACEHOLDER`",
    "- canonical_url: https://www.bilibili.com/video/BV1PLACEHOLDER",
    "",
    "Raw markdown candidate generated from existing capture truth only."
  ].join("\n"),
  warnings: ["placeholder only - bridge route wiring stays deferred"]
};

type VaultPreviewPanelProps = {
  preview?: BridgeVaultPreviewResponse;
};

export default function VaultPreviewPanel({ preview = placeholderPreview }: VaultPreviewPanelProps) {
  return (
    <section
      data-testid="panel-vault-preview"
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
          <p style={{ margin: 0, color: "#6d8099", fontSize: "12px" }}>vault-preview</p>
          <h2 style={{ margin: "8px 0 0", fontSize: "20px", lineHeight: 1.15 }}>Vault Preview</h2>
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
          placeholder only
        </span>
      </div>

      <p style={{ margin: 0, color: "#a6b8cf", fontSize: "14px", lineHeight: 1.45 }}>
        This surface previews the raw 4-field note contract without claiming live H5 -&gt; Bridge wiring.
      </p>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "minmax(0, 120px) minmax(0, 1fr)",
          gap: "8px 12px"
        }}
      >
        <span style={{ color: "#6d8099", fontSize: "12px" }}>capture_id</span>
        <span style={{ color: "#eef4ff", fontSize: "14px" }}>{preview.capture_id}</span>
        <span style={{ color: "#6d8099", fontSize: "12px" }}>target_path</span>
        <span style={{ color: "#eef4ff", fontSize: "14px", wordBreak: "break-all" }}>{preview.target_path}</span>
        <span style={{ color: "#6d8099", fontSize: "12px" }}>frontmatter</span>
        <span style={{ color: "#eef4ff", fontSize: "14px" }}>
          {preview.frontmatter.date} / {preview.frontmatter.tags} / {preview.frontmatter.status}
        </span>
      </div>

      <pre
        style={{
          margin: 0,
          borderRadius: "8px",
          border: "1px solid #27415d",
          background: "#0b1624",
          color: "#d8e3f2",
          padding: "12px",
          fontSize: "12px",
          lineHeight: 1.5,
          whiteSpace: "pre-wrap"
        }}
      >
        {preview.body_markdown}
      </pre>

      {preview.warnings.length > 0 ? (
        <ul style={{ margin: 0, paddingLeft: "18px", color: "#ffcf7a", fontSize: "12px" }}>
          {preview.warnings.map((warning) => (
            <li key={warning}>{warning}</li>
          ))}
        </ul>
      ) : null}
    </section>
  );
}
