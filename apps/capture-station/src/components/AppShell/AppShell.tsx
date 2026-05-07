import type { ReactNode } from "react";

import styles from "./AppShell.module.css";

export type ShellSurface = {
  id: string;
  title: string;
  caption: string;
};

export type AppShellProps = {
  current: string;
  onSelect: (id: string) => void;
  surfaces: ShellSurface[];
  children: ReactNode;
};

export default function AppShell({ children, current, onSelect, surfaces }: AppShellProps) {
  return (
    <div className={styles.frame}>
      <div className={styles.shell}>
        <aside className={styles.sidebar}>
          <div className={styles.brand}>
            <p className={styles.eyebrow}>ScoutFlow PF-C4-01</p>
            <h1 className={styles.title}>Capture Station · 本地操作员工作站</h1>
            <p className={styles.note}>13 个 surface 已转为 React TSX，保持 token 单源、sync-badge 三态和诚实 TODO 占位。</p>
          </div>

          <nav className={styles.nav} aria-label="Surface navigation">
            {surfaces.map((surface) => {
              const classes = [styles.navButton, current === surface.id ? styles.navButtonActive : ""].filter(Boolean).join(" ");
              return (
                <button key={surface.id} type="button" className={classes} onClick={() => onSelect(surface.id)}>
                  <span className={styles.navTitle}>{surface.title}</span>
                  <span className={styles.navCaption}>{surface.caption}</span>
                </button>
              );
            })}
          </nav>
        </aside>

        <section className={styles.content}>{children}</section>
      </div>
    </div>
  );
}
