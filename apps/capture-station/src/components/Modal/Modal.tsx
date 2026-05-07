import type { ReactNode } from "react";

import styles from "./Modal.module.css";

export type ModalTone = "pass" | "fail" | "promote";

export type ModalProps = {
  title: ReactNode;
  tone?: ModalTone;
  footer?: ReactNode;
  children: ReactNode;
};

export default function Modal({ children, footer, title, tone = "promote" }: ModalProps) {
  const classes = [styles.dialog, styles[tone]].filter(Boolean).join(" ");

  return (
    <dialog className={classes} open>
      <h3 className={styles.title}>{title}</h3>
      <div className={styles.body}>{children}</div>
      {footer ? <footer className={styles.footer}>{footer}</footer> : null}
    </dialog>
  );
}
