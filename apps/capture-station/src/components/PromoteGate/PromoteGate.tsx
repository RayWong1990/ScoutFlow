import Icon from "../Icon/Icon";
import styles from "./PromoteGate.module.css";

export type PromoteGateItem = {
  label: string;
  status: "met" | "pending" | "blocked" | "disabled";
};

export type PromoteGateProps = {
  title: string;
  items: PromoteGateItem[];
};

export default function PromoteGate({ items, title }: PromoteGateProps) {
  const iconByStatus = {
    met: "success",
    pending: "loading",
    blocked: "blocked",
    disabled: "locked",
  } as const;

  return (
    <section className={styles.root}>
      <h3 className={styles.title}>{title}</h3>
      <ul className={styles.list}>
        {items.map((item) => (
          <li key={item.label} className={[styles.item, styles[item.status]].join(" ")}>
            <Icon sprite="state" name={iconByStatus[item.status]} />
            <span>{item.label}</span>
          </li>
        ))}
      </ul>
    </section>
  );
}
