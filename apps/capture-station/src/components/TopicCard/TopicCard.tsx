import type { ReactNode } from "react";

import CaptureIdChip from "../CaptureIdChip/CaptureIdChip";
import StateBadge, { type StateBadgeTone } from "../StateBadge/StateBadge";
import styles from "./TopicCard.module.css";

export type TopicCardProps = {
  captureId: string;
  title: string;
  abstract?: string;
  source: string;
  selected?: boolean;
  badge?: { label: string; tone: StateBadgeTone };
  footer?: ReactNode;
  thumbnailLabel?: string;
  meta?: ReactNode;
};

export default function TopicCard({ abstract, badge, captureId, footer, meta, selected = false, source, thumbnailLabel, title }: TopicCardProps) {
  const classes = [styles.root, selected ? styles.selected : ""].filter(Boolean).join(" ");

  return (
    <article className={classes}>
      <header className={styles.header}>
        <div className={styles.meta}>
          <CaptureIdChip value={captureId} />
          <span>{source}</span>
          {meta}
        </div>
        {badge ? <StateBadge tone={badge.tone} label={badge.label} /> : null}
      </header>
      {thumbnailLabel ? (
        <figure className={styles.thumbnail}>
          <div className={styles.thumbnailLabel}>
            <CaptureIdChip value={thumbnailLabel} muted />
          </div>
        </figure>
      ) : null}
      <h3 className={styles.title}>{title}</h3>
      {abstract ? <p className={styles.abstract}>{abstract}</p> : null}
      {footer ? <footer className={styles.footer}>{footer}</footer> : null}
    </article>
  );
}
