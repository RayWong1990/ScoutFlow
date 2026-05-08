import blockedIconUrl from "../../assets/state-icons/blocked.svg";
import styles from "./HoldBanner.module.css";

export type HoldBannerProps = {
  holdId: string;
  title: string;
  reason: string;
  unlockPath: string;
  className?: string;
};

export default function HoldBanner({ className, holdId, reason, title, unlockPath }: HoldBannerProps) {
  const classes = [styles.root, className].filter(Boolean).join(" ");

  return (
    <aside className={classes} role="status" aria-label={`${holdId} hold`}>
      <img className={styles.icon} src={blockedIconUrl} alt="" aria-hidden="true" />
      <div className={styles.copy}>
        <div className={styles.header}>
          <span className={styles.holdId}>{holdId}</span>
          <h3>{title}</h3>
        </div>
        <p className={styles.reason}>{reason}</p>
        <p className={styles.unlockPath}>解锁路径：{unlockPath}</p>
      </div>
    </aside>
  );
}
