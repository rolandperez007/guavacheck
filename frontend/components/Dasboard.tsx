"use client";

import { useEffect, useState } from "react";

export default function Dashboard() {
  const [data, setData] = useState<any>(null);

  useEffect(() => {
    const fetchData = async () => {
      const res = await fetch("http://127.0.0.1:8000/dashboard/summary");
      const json = await res.json();
      setData(json);
    };

    fetchData();
    const interval = setInterval(fetchData, 3000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ width: "100%", padding: 20, background: "#111", color: "#fff" }}>
      <h2>📊 Austin Intelligence Dashboard</h2>

      <pre style={{ fontSize: 12 }}>
        {JSON.stringify(data, null, 2)}
      </pre>
    </div>
  );
}