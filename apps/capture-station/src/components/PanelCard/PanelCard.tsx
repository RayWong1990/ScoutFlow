import type { ReactNode } from "react";

import styles from "./PanelCard.module.css";

export type PanelCardProps = {
  title: string;
  eyebrow?: string;
  description?: string;
  aside?: ReactNode;
  elevated?: boolean;
  children: ReactNode;
  className?: string;
};

export default function PanelCard({ aside, children, className, description, elevated = false, eyebrow, title }: PanelCardProps) {
  const classes = [styles.root, elevated ? styles.elevated : "", className].filter(Boolean).join(" ");

  return (
    <section className={classes}>
      <header className={styles.header}>
        <div className={styles.headline}>
          {eyebrow ? <p className={styles.eyebrow}>{eyebrow}</p> : null}
          <h2 className={styles.title}>{title}</h2>
          {description ? <p className={styles.description}>{description}</p> : null}
        </div>
        {aside}
      </header>
      {children}
    </section>
  );
}
