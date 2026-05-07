import Icon from "../Icon/Icon";
import styles from "./PromoteGate.module.css";

export type PromoteGateItem = {
  label: string;
  status: "met" | "pending";
};

export type PromoteGateProps = {
  title: string;
  items: PromoteGateItem[];
};

export default function PromoteGate({ items, title }: PromoteGateProps) {
  return (
    <section className={styles.root}>
      <h3 className={styles.title}>{title}</h3>
      <ul className={styles.list}>
        {items.map((item) => (
          <li key={item.label} className={[styles.item, styles[item.status]].join(" ")}>
            <Icon sprite="state" name={item.status === "met" ? "success" : "loading"} />
            <span>{item.label}</span>
          </li>
        ))}
      </ul>
    </section>
  );
}
