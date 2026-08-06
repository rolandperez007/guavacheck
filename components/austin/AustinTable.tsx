"use client";

import { useEffect, useState } from "react";

export function AustinTable({ table }: any) {
  const [visibleRows, setVisibleRows] = useState<any[]>([]);

  useEffect(() => {
    if (!table?.rows) return;

    setVisibleRows([]);

    let i = 0;
    const interval = setInterval(() => {
      setVisibleRows((prev) => [...prev, table.rows[i]]);
      i++;

      if (i >= table.rows.length) {
        clearInterval(interval);
      }
    }, 400); // cinematic reveal speed

    return () => clearInterval(interval);
  }, [table]);

  return (
    <div className="border rounded p-4 bg-white shadow">
      <h3 className="font-bold mb-3">BOQ Breakdown</h3>

      <table className="w-full text-sm">
        <thead>
          <tr className="text-left border-b">
            <th>Item</th>
            <th>Cost</th>
            <th>%</th>
          </tr>
        </thead>

        <tbody>
          {visibleRows.map((row: any, i: number) => (
            <tr key={i} className="border-b transition-all duration-300">
              <td>{row.item}</td>
              <td>₦{row.cost.toLocaleString()}</td>
              <td>{row.percentage?.toFixed(1)}%</td>
            </tr>
          ))}
        </tbody>
      </table>

      <div className="mt-3 font-bold">Total: ₦{table.total?.toLocaleString()}</div>
    </div>
  );
}
