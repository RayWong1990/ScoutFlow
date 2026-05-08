import styles from "./EvidenceTable.module.css";

export type EvidenceColumn = {
  key: string;
  label: string;
  code?: boolean;
};

export type EvidenceRow = {
  id: string;
  tone?: "default" | "preview" | "blocked" | "failed" | "partial" | "committed" | "error";
  cells: Record<string, string>;
};

export type EvidenceTableProps = {
  title?: string;
  description?: string;
  columns: EvidenceColumn[];
  rows: EvidenceRow[];
  emptyCopy?: string;
};

export default function EvidenceTable({ columns, description, emptyCopy = "当前还没有可展示的 evidence 行。", rows, title }: EvidenceTableProps) {
  return (
    <section className={styles.root}>
      {title || description ? (
        <header className={styles.header}>
          {title ? <h3 className={styles.title}>{title}</h3> : null}
          {description ? <p className={styles.description}>{description}</p> : null}
        </header>
      ) : null}

      <table className={styles.table}>
        <thead>
          <tr>
            {columns.map((column) => (
              <th key={column.key}>{column.label}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows.length === 0 ? (
            <tr>
              <td className={styles.emptyCell} colSpan={Math.max(columns.length, 1)}>
                {emptyCopy}
              </td>
            </tr>
          ) : (
            rows.map((row) => (
              <tr key={row.id} className={row.tone ? styles[row.tone] : undefined} data-tone={row.tone ?? "default"}>
                {columns.map((column) => {
                  const value = row.cells[column.key] ?? "";
                  return <td key={column.key}>{column.code ? <code>{value}</code> : value}</td>;
                })}
              </tr>
            ))
          )}
        </tbody>
      </table>
    </section>
  );
}
