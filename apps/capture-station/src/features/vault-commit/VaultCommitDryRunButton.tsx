import type { BridgeVaultCommitResponse } from "../../lib/api-client";

const placeholderCommit: BridgeVaultCommitResponse = {
  capture_id: "cap_placeholder",
  committed: false,
  dry_run: true,
  target_path: "/tmp/scoutflow-vault/00-Inbox/scoutflow-cap_placeholder-bv1placeholder.md",
  error: {
    code: "write_disabled",
    message: "Bridge write path is not approved in the current phase."
  }
};

type VaultCommitDryRunButtonProps = {
  commit?: BridgeVaultCommitResponse;
};

export default function VaultCommitDryRunButton({ commit = placeholderCommit }: VaultCommitDryRunButtonProps) {
  return (
    <section
      data-testid="panel-vault-commit"
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
          <p style={{ margin: 0, color: "#6d8099", fontSize: "12px" }}>vault-commit</p>
          <h2 style={{ margin: "8px 0 0", fontSize: "20px", lineHeight: 1.15 }}>Vault Commit Dry Run</h2>
        </div>
        <span
          style={{
            borderRadius: "999px",
            border: "1px solid #27415d",
            background: "#16263c",
            color: "#ffcf7a",
            padding: "6px 10px",
            fontSize: "12px"
          }}
        >
          dry-run only
        </span>
      </div>

      <p style={{ margin: 0, color: "#a6b8cf", fontSize: "14px", lineHeight: 1.45 }}>
        This surface exposes the current-phase commit contract without claiming actual vault writes.
      </p>

      <div
        style={{
          borderRadius: "8px",
          border: "1px solid #27415d",
          background: "#0b1624",
          padding: "12px",
          display: "grid",
          gap: "8px"
        }}
      >
        <div style={{ display: "flex", justifyContent: "space-between", gap: "12px" }}>
          <span style={{ color: "#6d8099", fontSize: "12px" }}>capture_id</span>
          <span style={{ color: "#eef4ff", fontSize: "14px" }}>{commit.capture_id}</span>
        </div>
        <div style={{ display: "flex", justifyContent: "space-between", gap: "12px" }}>
          <span style={{ color: "#6d8099", fontSize: "12px" }}>dry_run</span>
          <span style={{ color: "#eef4ff", fontSize: "14px" }}>{String(commit.dry_run)}</span>
        </div>
        <div style={{ display: "flex", justifyContent: "space-between", gap: "12px" }}>
          <span style={{ color: "#6d8099", fontSize: "12px" }}>committed</span>
          <span style={{ color: "#eef4ff", fontSize: "14px" }}>{String(commit.committed)}</span>
        </div>
        <div style={{ display: "flex", justifyContent: "space-between", gap: "12px" }}>
          <span style={{ color: "#6d8099", fontSize: "12px" }}>target_path</span>
          <span style={{ color: "#eef4ff", fontSize: "14px", wordBreak: "break-all" }}>
            {commit.target_path ?? "unset"}
          </span>
        </div>
        <div style={{ display: "flex", justifyContent: "space-between", gap: "12px" }}>
          <span style={{ color: "#6d8099", fontSize: "12px" }}>gate</span>
          <span style={{ color: "#ffcf7a", fontSize: "14px" }}>{commit.error?.code ?? "pending"}</span>
        </div>
      </div>

      <button
        type="button"
        disabled
        style={{
          marginTop: "auto",
          borderRadius: "10px",
          border: "1px solid #27415d",
          background: "#16263c",
          color: "#6d8099",
          padding: "12px 14px",
          fontSize: "14px",
          fontWeight: 600,
          cursor: "not-allowed"
        }}
      >
        Commit to vault (disabled)
      </button>
    </section>
  );
}
