import Icon from "../Icon/Icon";
import { STATE_COPY_ZH, type CaptureSurfaceState } from "../../styles/state-tokens";
import { normalizeStateBadgeTone, type StateBadgeTone } from "./derive";
import styles from "./StateBadge.module.css";

export type { StateBadgeTone } from "./derive";

export type StateBadgeProps = {
  tone: StateBadgeTone;
  label?: string;
  className?: string;
};

export default function StateBadge({ className, label, tone }: StateBadgeProps) {
  const normalizedTone = normalizeStateBadgeTone(tone);
  const classes = [styles.root, styles[normalizedTone], className].filter(Boolean).join(" ");

  return (
    <span className={classes} data-state={normalizedTone}>
      <span className={styles.iconWrap}>
        <Icon sprite="state" name={getStateBadgeIcon(normalizedTone)} />
      </span>
      <span>{label ?? STATE_COPY_ZH[normalizedTone]}</span>
    </span>
  );
}

function getStateBadgeIcon(tone: CaptureSurfaceState) {
  switch (tone) {
    case "empty":
      return "empty";
    case "loading":
      return "loading";
    case "disabled":
      return "locked";
    case "blocked":
      return "blocked";
    case "preview":
      return "focus";
    case "committed":
      return "success";
    case "failed":
      return "error";
    case "partial":
      return "warning";
    case "skipped":
      return "empty";
  }
}
