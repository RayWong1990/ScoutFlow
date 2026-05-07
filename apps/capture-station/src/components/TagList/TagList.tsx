import styles from "./TagList.module.css";

export type TagTone = "default" | "info" | "success" | "focus" | "blocked";

export type TagItem = {
  label: string;
  tone?: TagTone;
};

export type TagListProps = {
  items: TagItem[];
};

export default function TagList({ items }: TagListProps) {
  return (
    <ul className={styles.list}>
      {items.map((item) => {
        const classes = [styles.item, item.tone && item.tone !== "default" ? styles[item.tone] : ""].filter(Boolean).join(" ");
        return <li key={`${item.label}-${item.tone ?? "default"}`} className={classes}>{item.label}</li>;
      })}
    </ul>
  );
}
