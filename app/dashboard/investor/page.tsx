"use client";

import { useEffect, useState } from "react";
import {
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell,
  Tooltip,
  BarChart,
  Bar,
  XAxis,
  YAxis
} from "recharts";

type Property = {
  id: string;
  title: string;
  location: string;
  price: number;
  investment?: {
    score: number;
    decision: string;
  };
  mortgage?: {
    monthlyPayment: number;
    status: string;
    recommendation: string;
  };
};

export default function InvestorDashboard() {
  const [data, setData] = useState<Property[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function load() {
      try {
        const res = await fetch("/api/investor", {
          method: "POST",
          body: JSON.stringify({
            properties: await (await fetch('/api/properties/ai-feed')).json()
          })
        });

        const json = await res.json();
        setData(json?.data || []);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    }

    load();
  }, []);

  if (loading) {
    return <div style={{ padding: 30 }}>Loading investor dashboard...</div>;
  }

  return (
    <div style={{ padding: 30 }}>
      <h1 style={{ fontSize: 28, marginBottom: 20 }}>
        Investor Intelligence Dashboard
      </h1>

      <div style={{ display: "grid", gap: 16 }}>
        {data.map((p) => (
          <div
            key={p.id}
            style={{
              border: "1px solid #ddd",
              borderRadius: 12,
              padding: 16
            }}
          >
            <h3>{p.title}</h3>
            <p>📍 {p.location}</p>
            <p>₦{p.price?.toLocaleString()}</p>

            {/* INVESTMENT SCORE */}
            {p.investment && (
              <div style={{ marginTop: 10 }}>
                <strong>Investment Score: {p.investment.score}</strong>
                <p>Decision: {p.investment.decision}</p>
              </div>
            )}

            {/* MORTGAGE LAYER */}
            {p.mortgage && (
              <div
                style={{
                  marginTop: 10,
                  padding: 10,
                  background: "#f8f8f8",
                  borderRadius: 8
                }}
              >
                <p>Monthly: ₦{p.mortgage.monthlyPayment}</p>
                <p>Status: {p.mortgage.status}</p>
                <p>Recommendation: {p.mortgage.recommendation}</p>
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

const COLORS = ["#0088FE", "#00C49F", "#FFBB28", "#FF8042"];

const decisionData = [
  { name: "Buy", value: 10 },
  { name: "Review", value: 5 },
  { name: "Reject", value: 2 }
];

const roiTrend = [
  { name: "Jan", score: 60 },
  { name: "Feb", score: 72 },
  { name: "Mar", score: 88 }
];










