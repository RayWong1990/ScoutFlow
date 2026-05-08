import styles from "./EvidenceTable.module.css";

export type EvidenceColumn = {
  key: string;
  label: string;
  code?: boolean;
};

export type EvidenceRow = {
  id: string;
  tone?: "default" | "error" | "preview" | "blocked" | "partial";
  cells: Record<string, string>;
};

export type EvidenceTableProps = {
  columns: EvidenceColumn[];
  rows: EvidenceRow[];
};

export default function EvidenceTable({ columns, rows }: EvidenceTableProps) {
  return (
    <table className={styles.table}>
      <thead>
        <tr>
          {columns.map((column) => (
            <th key={column.key}>{column.label}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {rows.map((row) => (
          <tr
            key={row.id}
            className={row.tone && row.tone !== "default" ? styles[row.tone] : undefined}
            data-tone={row.tone ?? "default"}
          >
            {columns.map((column) => {
              const value = row.cells[column.key] ?? "";
              return <td key={column.key}>{column.code ? <code>{value}</code> : value}</td>;
            })}
          </tr>
        ))}
      </tbody>
    </table>
  );
}
