import styles from "./CaptureIdChip.module.css";

export type CaptureIdChipProps = {
  value: string;
  muted?: boolean;
};

export default function CaptureIdChip({ muted = false, value }: CaptureIdChipProps) {
  const classes = [styles.chip, muted ? styles.muted : ""].filter(Boolean).join(" ");
  return <code className={classes}>{value}</code>;
}
