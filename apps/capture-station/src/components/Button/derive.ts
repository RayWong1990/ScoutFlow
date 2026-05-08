import type { ButtonVariant } from "./Button";

export type VaultActionButtonInput = {
  committed: boolean;
  writeEnabled: boolean;
  dryRun: boolean;
};

export function deriveVaultActionButtonVariant(input: VaultActionButtonInput): ButtonVariant {
  if (!input.writeEnabled) {
    return "blocked";
  }

  if (input.dryRun || !input.committed) {
    return "preview-only";
  }

  return "success";
}

