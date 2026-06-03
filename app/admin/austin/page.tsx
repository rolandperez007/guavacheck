"use client";

import { useEffect, useState } from "react";

export default function AustinAdminDashboard() {

  const [data, setData] = useState<any>(null);

  useEffect(() => {

    async function load() {

      const res = await fetch("/api/public/austin");
      const json = await res.json();

      setData(json);
    }

    load();

  }, []);

  return (
    <div style={{ padding: 20, fontFamily: "Arial" }}>

      <h1>🏦 Austin Intelligence Admin Dashboard</h1>

      <div style={{ marginTop: 20 }}>

        <h2>📊 System Overview</h2>

        <pre>{JSON.stringify(data, null, 2)}</pre>

      </div>

      <div style={{ marginTop: 20 }}>

        <h2>🧠 Live Metrics</h2>

        <ul>
          <li>API Active: YES</li>
          <li>AI Engine: ONLINE</li>
          <li>Forecasting: ENABLED</li>
          <li>Ingestion: ACTIVE</li>
        </ul>

      </div>

    </div>
  );
}
