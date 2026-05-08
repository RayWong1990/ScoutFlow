import Button from "../../components/Button/Button";
import PanelCard from "../../components/PanelCard/PanelCard";

export type VaultPreviewPanelProps = {
  body_markdown?: string;
  target_path?: string;
  canInteract?: boolean;
  onCopy?: () => void;
  onDownload?: () => void;
};

export default function VaultPreviewPanel({
  body_markdown = "",
  canInteract = false,
  onCopy,
  onDownload,
  target_path = "pending",
}: VaultPreviewPanelProps) {
  return (
    <PanelCard title="Vault Preview Panel" eyebrow="vault-preview">
      <div data-testid="panel-vault-preview">
        <p>Create a metadata-only capture to load preview.</p>
        <p>target_path: {target_path}</p>
        <pre>{body_markdown || "body_markdown pending"}</pre>
        <div>
          <Button variant={canInteract ? "primary" : "blocked"} onClick={onCopy} disabled={!canInteract}>
            Copy markdown
          </Button>
          <Button variant={canInteract ? "secondary" : "blocked"} onClick={onDownload} disabled={!canInteract}>
            Download .md
          </Button>
        </div>
      </div>
    </PanelCard>
  );
}
