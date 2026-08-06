"use client";

import { useEffect, useState } from "react";

type Property = {
  id: string;
  title: string;
  location: string;
  price: number | null;
  status: string;
  image_url?: string | null;

  aiScore?: {
    investmentScore?: number;
    roiScore?: number;
    livabilityScore?: number;
    riskScore?: number;
    finalScore?: number;
    grade?: string;
  };
};

export default function PropertiesPage() {
  const [properties, setProperties] = useState<Property[]>([]);
  const [filtered, setFiltered] = useState<Property[]>([]);
  const [loading, setLoading] = useState(true);

  // filters
  const [search, setSearch] = useState("");
  const [minPrice, setMinPrice] = useState("");
  const [maxPrice, setMaxPrice] = useState("");
  const [status, setStatus] = useState("all");

  useEffect(() => {
    async function load() {
      try {
        const res = await fetch("/api/properties/ai-feed");
        const data = await res.json();

        const list = data?.data || [];

        setProperties(list);
        setFiltered(list);
      } catch (err) {
        console.error("Failed to load properties", err);
      } finally {
        setLoading(false);
      }
    }

    load();
  }, []);

  useEffect(() => {
    let result = [...properties];

    if (search) {
      result = result.filter(
        (p) =>
          p.title?.toLowerCase().includes(search.toLowerCase()) ||
          p.location?.toLowerCase().includes(search.toLowerCase()),
      );
    }

    if (minPrice) {
      result = result.filter((p) => (p.price || 0) >= Number(minPrice));
    }

    if (maxPrice) {
      result = result.filter((p) => (p.price || 0) <= Number(maxPrice));
    }

    if (status !== "all") {
      result = result.filter((p) => p.status === status);
    }

    setFiltered(result);
  }, [search, minPrice, maxPrice, status, properties]);

  if (loading) {
    return <div style={{ padding: 30 }}>Loading AI properties...</div>;
  }

  return (
    <div style={{ padding: 30 }}>
      <h1 style={{ fontSize: 28, marginBottom: 20 }}>AI Property Intelligence Feed</h1>

      {/* FILTERS */}
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "2fr 1fr 1fr 1fr",
          gap: 10,
          marginBottom: 20,
        }}
      >
        <input
          placeholder="Search title or location..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          style={{ padding: 10 }}
        />

        <input
          placeholder="Min Price"
          value={minPrice}
          onChange={(e) => setMinPrice(e.target.value)}
          style={{ padding: 10 }}
        />

        <input
          placeholder="Max Price"
          value={maxPrice}
          onChange={(e) => setMaxPrice(e.target.value)}
          style={{ padding: 10 }}
        />

        <select value={status} onChange={(e) => setStatus(e.target.value)} style={{ padding: 10 }}>
          <option value="all">All</option>
          <option value="draft">Draft</option>
          <option value="active">Active</option>
          <option value="sold">Sold</option>
        </select>
      </div>

      {/* RESULTS */}
      {filtered.length === 0 ? (
        <p>No properties found.</p>
      ) : (
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fit, minmax(320px, 1fr))",
            gap: 20,
          }}
        >
          {filtered.map((p) => (
            <div
              key={p.id}
              style={{
                border: "1px solid #ddd",
                borderRadius: 12,
                padding: 16,
              }}
            >
              <h3>{p.title}</h3>
              <p>📍 {p.location}</p>

              <p style={{ fontWeight: "bold" }}>
                ₦{p.price ? Number(p.price).toLocaleString() : "0"}
              </p>

              {/* AI BLOCK */}
              {p.aiScore && (
                <div
                  style={{
                    marginTop: 10,
                    padding: 10,
                    background: "#f8f8f8",
                    borderRadius: 8,
                  }}
                >
                  <strong>AI Score</strong>
                  <p>Grade: {p.aiScore.grade}</p>
                  <p>Final: {p.aiScore.finalScore}</p>
                  <p>ROI: {p.aiScore.roiScore}%</p>
                  <p>Risk: {p.aiScore.riskScore}</p>
                </div>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
