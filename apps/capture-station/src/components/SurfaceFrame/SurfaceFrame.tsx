import type { ReactNode } from "react";

import styles from "./SurfaceFrame.module.css";

export type SurfaceFrameProps = {
  title: string;
  description?: string;
  children: ReactNode;
};

export function SurfaceSection({ children, title }: { children: ReactNode; title: string }) {
  return (
    <section className={styles.section}>
      <h3 className={styles.sectionTitle}>{title}</h3>
      {children}
    </section>
  );
}

export function SurfaceDivider() {
  return <hr className={styles.divider} />;
}

export default function SurfaceFrame({ children, description, title }: SurfaceFrameProps) {
  return (
    <main className={styles.root}>
      <header className={styles.header}>
        <h1 className={styles.title}>{title}</h1>
        {description ? <p className={styles.description}>{description}</p> : null}
      </header>
      {children}
    </main>
  );
}
