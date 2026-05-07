import type { ReactNode } from "react";

import styles from "./GovernanceTooltip.module.css";

export type GovernanceTooltipProps = {
  title: string;
  children: ReactNode;
};

export default function GovernanceTooltip({ children, title }: GovernanceTooltipProps) {
  return (
    <aside className={styles.root} role="note">
      <h4 className={styles.title}>{title}</h4>
      <div className={styles.body}>{children}</div>
    </aside>
  );
}
