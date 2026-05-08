import Icon from "../Icon/Icon";
import { STATE_ICON_NAME, type CaptureSurfaceState } from "../../styles/state-tokens";
import { resolveStateBadgeTone } from "./derive";
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
  | "success"
  | CaptureSurfaceState;

export type StateBadgeProps = {
  tone: StateBadgeTone;
  label: string;
  className?: string;
};

export default function StateBadge({ className, label, tone }: StateBadgeProps) {
  const stateTone = resolveStateBadgeTone(tone);
  const classes = [styles.root, styles[stateTone], className].filter(Boolean).join(" ");

  return (
    <span className={classes} data-state={stateTone}>
      <Icon className={styles.icon} sprite="state" name={STATE_ICON_NAME[stateTone]} />
      <span>{label}</span>
    </span>
  );
}
