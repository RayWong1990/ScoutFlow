import styles from "./StateBadge.module.css";

export type StateBadgeTone =
  | "idle"
  | "loading"
  | "ready"
  | "candidate"
  | "blocked"
  | "stale"
  | "metadataLoaded"
  | "previewOnly"
  | "metadataOnly"
  | "locked"
  | "error"
  | "success";

export type StateBadgeProps = {
  tone: StateBadgeTone;
  label: string;
  className?: string;
};

export default function StateBadge({ className, label, tone }: StateBadgeProps) {
  const classes = [styles.root, styles[tone], className].filter(Boolean).join(" ");
  return <span className={classes}>{label}</span>;
}
