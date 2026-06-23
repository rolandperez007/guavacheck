"use client";

import { useEffect, useState } from "react";
import ROIChart from "@/components/investor/ROIChart";

interface Deal {
  id: string;
  title: string;
  location: string;
  investmentScore: number;
  distressedScore: number;
  roi: number;
  recommendation: string;
}

export default function InvestorDashboard() {
  const [deals, setDeals] = useState<Deal[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadDeals() {
      try {
        const res = await fetch("/api/investor/deals");

        if (!res.ok) {
          throw new Error("Failed to fetch deals");
        }

        const data = await res.json();

        setDeals(Array.isArray(data) ? data : []);
      } catch (err) {
        console.error("Investor deals error:", err);
      } finally {
        setLoading(false);
      }
    }

    loadDeals();
  }, []);

  if (loading) {
    return <div>Loading investor dashboard...</div>;
  }

  return (
    <div style={{ padding: 20 }}>
      <h1>Investor Dashboard</h1>

      <ROIChart data={deals} />
    </div>
  );
}










