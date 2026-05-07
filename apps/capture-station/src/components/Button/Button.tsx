import type { ButtonHTMLAttributes, ReactNode } from "react";

import styles from "./Button.module.css";

type ButtonVariant = "primary" | "secondary" | "success" | "blocked";

export type ButtonProps = ButtonHTMLAttributes<HTMLButtonElement> & {
  icon?: ReactNode;
  variant?: ButtonVariant;
};

export default function Button({ children, className, icon, variant = "secondary", type = "button", ...props }: ButtonProps) {
  const classes = [styles.root, styles[variant], className].filter(Boolean).join(" ");

  return (
    <button type={type} className={classes} {...props}>
      {icon}
      <span>{children}</span>
    </button>
  );
}
