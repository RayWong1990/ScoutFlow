import type { ButtonHTMLAttributes, ReactNode } from "react";

import { normalizeButtonVariant, type ButtonVariant } from "./derive";
import styles from "./Button.module.css";

export type ButtonProps = ButtonHTMLAttributes<HTMLButtonElement> & {
  icon?: ReactNode;
  variant?: ButtonVariant;
};

export default function Button({ children, className, icon, variant = "secondary", type = "button", ...props }: ButtonProps) {
  const normalizedVariant = normalizeButtonVariant(variant);
  const classes = [styles.root, styles[normalizedVariant], className].filter(Boolean).join(" ");

  return (
    <button type={type} className={classes} data-variant={normalizedVariant} {...props}>
      {icon}
      <span>{children}</span>
    </button>
  );
}
