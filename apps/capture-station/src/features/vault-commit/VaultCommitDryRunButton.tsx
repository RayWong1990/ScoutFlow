import Button from "../../components/Button/Button";
import PanelCard from "../../components/PanelCard/PanelCard";

export type VaultCommitDryRunButtonProps = {
  committed?: boolean;
  dryRun?: boolean;
  writeDisabled?: boolean;
  onDryRun?: () => void;
};

export default function VaultCommitDryRunButton({
  committed = false,
  dryRun = true,
  onDryRun,
  writeDisabled = true,
}: VaultCommitDryRunButtonProps) {
  return (
    <PanelCard title="Vault Commit Dry-run Button" eyebrow="vault-commit">
      <div data-testid="panel-vault-commit">
        <p>dry-run only</p>
        <p>dry_run: true</p>
        <p>commit.dry_run = {String(dryRun)}</p>
        <p>committed = {String(committed)}</p>
        <p>write_disabled = {String(writeDisabled)}</p>
        <Button variant="secondary" onClick={onDryRun}>
          Run dry-run check
        </Button>
        <Button variant="blocked" disabled>
          Commit to vault (disabled)
        </Button>
      </div>
    </PanelCard>
  );
}
