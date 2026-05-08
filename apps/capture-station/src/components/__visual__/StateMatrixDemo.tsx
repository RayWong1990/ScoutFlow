import Button from "../Button/Button";
import HoldBanner from "../HoldBanner/HoldBanner";
import { DEFAULT_HOLDS } from "../HoldBanner/holds";
import EvidenceTable from "../EvidenceTable/EvidenceTable";
import PromoteGate from "../PromoteGate/PromoteGate";
import StateBadge from "../StateBadge/StateBadge";

const stateRows = [
  "empty",
  "loading",
  "disabled",
  "blocked",
  "preview",
  "committed",
  "failed",
  "partial",
  "skipped",
] as const;

export default function StateMatrixDemo() {
  return (
    <div style={{ display: "grid", gap: "24px" }}>
      <section style={{ display: "flex", gap: "12px", flexWrap: "wrap" }}>
        {stateRows.map((state) => (
          <StateBadge key={state} tone={state} />
        ))}
      </section>

      <PromoteGate
        title="PromoteGate 4 态"
        items={[
          { label: "idle / met", status: "met" },
          { label: "pending", status: "pending" },
          { label: "blocked", status: "blocked" },
          { label: "disabled", status: "disabled" },
        ]}
      />

      <div style={{ display: "flex", gap: "12px", flexWrap: "wrap" }}>
        <Button variant="primary">default</Button>
        <Button variant="secondary" disabled>
          disabled
        </Button>
        <Button variant="preview-only">preview-only</Button>
        <Button variant="blocked" disabled>
          blocked
        </Button>
        <Button variant="committed">committed</Button>
      </div>

      <div style={{ display: "grid", gap: "12px" }}>
        <HoldBanner {...DEFAULT_HOLDS.true_vault_write} />
        <HoldBanner {...DEFAULT_HOLDS.runtime_tools} />
        <HoldBanner {...DEFAULT_HOLDS.browser_automation} />
        <HoldBanner {...DEFAULT_HOLDS.dbvnext_migration} />
        <HoldBanner {...DEFAULT_HOLDS.audio_transcript} />
      </div>

      <EvidenceTable
        title="EvidenceTable 3 行"
        columns={[
          { key: "field", label: "字段" },
          { key: "value", label: "值" },
        ]}
        rows={[
          { id: "preview", tone: "preview", cells: { field: "preview hash", value: "sha256:abc..." } },
          { id: "blocked", tone: "blocked", cells: { field: "transcript", value: "blocked" } },
          { id: "receipt", tone: "partial", cells: { field: "source receipt", value: "present(3)" } },
        ]}
      />
    </div>
  );
}
