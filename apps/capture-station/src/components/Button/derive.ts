export type ButtonStateInput = {
  committed?: boolean;
  writeEnabled?: boolean;
  dryRun?: boolean;
  blocked?: boolean;
};

export type ButtonVariant =
  | "primary"
  | "secondary"
  | "preview-only"
  | "blocked"
  | "committed"
  | "success";

export function normalizeButtonVariant(variant: ButtonVariant): Exclude<ButtonVariant, "success"> {
  if (variant === "success") {
    return "preview-only";
  }
  return variant;
}

export function deriveButtonVariant(input: ButtonStateInput): Exclude<ButtonVariant, "success"> {
  if (input.blocked) {
    return "blocked";
  }

  if (input.dryRun || input.committed === false || input.writeEnabled === false) {
    return "preview-only";
  }

  if (input.committed) {
    return "committed";
  }

  return "secondary";
}
