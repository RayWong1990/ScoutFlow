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
  return (
    <section className={styles.root}>
      <h3 className={styles.title}>{title}</h3>
      <ul className={styles.list}>
        {items.map((item) => (
          <li key={item.label} className={[styles.item, styles[item.status]].join(" ")} data-status={item.status}>
            <Icon sprite="state" name={iconForStatus(item.status)} />
            <span>{item.label}</span>
          </li>
        ))}
      </ul>
    </section>
  );
}

function iconForStatus(status: PromoteGateItem["status"]) {
  switch (status) {
    case "met":
      return "success";
    case "pending":
      return "loading";
    case "blocked":
      return "blocked";
    case "disabled":
      return "locked";
  }
}
