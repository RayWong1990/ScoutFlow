import Icon from "../Icon/Icon";
import styles from "./SyncBadge.module.css";

export type SyncState = "synced" | "pending" | "external-changed";

const syncMeta = {
  synced: { className: styles.synced, icon: "success", label: "已同步" },
  pending: { className: styles.pending, icon: "warning", label: "待同步" },
  "external-changed": { className: styles.externalChanged, icon: "focus", label: "外部已改" },
} as const;

export type SyncBadgeProps = {
  state: SyncState;
  className?: string;
};

export default function SyncBadge({ className, state }: SyncBadgeProps) {
  const meta = syncMeta[state];
  const classes = [styles.root, meta.className, className].filter(Boolean).join(" ");

  return (
    <span className={classes}>
      <Icon sprite="state" name={meta.icon} />
      <span>{meta.label}</span>
    </span>
  );
}
