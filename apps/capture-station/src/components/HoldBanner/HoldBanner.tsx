import Icon from "../Icon/Icon";
import styles from "./HoldBanner.module.css";

export type HoldBannerProps = {
  title?: string;
  holdId: string;
  reason: string;
  unlockPath: string;
  note?: string;
};

export default function HoldBanner({ holdId, note, reason, title = "当前 Hold", unlockPath }: HoldBannerProps) {
  return (
    <section className={styles.root} role="status" aria-live="polite">
      <header className={styles.header}>
        <span className={styles.iconWrap}>
          <Icon sprite="state" name="blocked" title="Hold" />
        </span>
        <div className={styles.headline}>
          <p className={styles.eyebrow}>always-visible hold</p>
          <h3 className={styles.title}>{title}</h3>
        </div>
      </header>

      <dl className={styles.grid}>
        <div className={styles.contents}>
          <dt>原因</dt>
          <dd>{reason}</dd>
        </div>
        <div className={styles.contents}>
          <dt>Hold ID</dt>
          <dd>
            <code>{holdId}</code>
          </dd>
        </div>
        <div className={styles.contents}>
          <dt>解锁路径</dt>
          <dd>{unlockPath}</dd>
        </div>
      </dl>

      {note ? <p className={styles.note}>{note}</p> : null}
    </section>
  );
}
