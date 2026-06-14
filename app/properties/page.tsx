"use client";

import { useEffect, useState } from "react";

type Property = {
  id: string;
  title: string;
  location: string;
  price: number | null;
  status: string;
  image_url?: string | null;
};

export default function PropertiesPage() {
  const [properties, setProperties] = useState<Property[]>([]);
  const [filtered, setFiltered] = useState<Property[]>([]);
  const [loading, setLoading] = useState(true);

  // 🔎 filters
  const [search, setSearch] = useState("");
  const [minPrice, setMinPrice] = useState("");
  const [maxPrice, setMaxPrice] = useState("");
  const [status, setStatus] = useState("all");

  useEffect(() => {
    async function load() {
      const res = await fetch("/api/properties/ai-feed
      const data = await res.json();

      setProperties(data || []);
      setFiltered(data || []);
      setLoading(false);
    }

    load();
  }, []);

  useEffect(() => {
    let result = [...properties];

    // 🔎 text search
    if (search) {
      result = result.filter(
        (p) =>
          p.title?.toLowerCase().includes(search.toLowerCase()) ||
          p.location?.toLowerCase().includes(search.toLowerCase())
      );
    }

    // 💰 price filter
    if (minPrice) {
      result = result.filter(
        (p) => (p.price || 0) >= Number(minPrice)
      );
    }

    if (maxPrice) {
      result = result.filter(
        (p) => (p.price || 0) <= Number(maxPrice)
      );
    }

    // 📌 status filter
    if (status !== "all") {
      result = result.filter((p) => p.status === status);
    }

    setFiltered(result);
  }, [search, minPrice, maxPrice, status, properties]);

  if (loading) {
    return <div style={{ padding: 30 }}>Loading properties...</div>;
  }

  return (
    <div style={{ padding: 30 }}>
      <h1 style={{ fontSize: 28, marginBottom: 20 }}>
        Property Listings
      </h1>

      {/* 🔎 SEARCH PANEL */}
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

        <select
          value={status}
          onChange={(e) => setStatus(e.target.value)}
          style={{ padding: 10 }}
        >
          <option value="all">All</option>
          <option value="draft">Draft</option>
          <option value="active">Active</option>
          <option value="sold">Sold</option>
        </select>
      </div>

      {/* 🏠 RESULTS */}
      {filtered.length === 0 ? (
        <p>No properties found.</p>
      ) : (
        <div
          style={{
            display: "grid",
            gridTemplateColumns:
              "repeat(auto-fit, minmax(300px, 1fr))",
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
{/* ===== AI INTELLIGENCE LAYER ===== */}
<AustinInsightCard ai={p.aiScore} />

{/* ===== MORTGAGE INTELLIGENCE LAYER ===== */}
<RecommendationCard mortgage={p.mortgage} />
              <p>📍 {p.location}</p>

              <p style={{ fontWeight: "bold" }}>
                ₦
                {p.price
                  ? Number(p.price).toLocaleString()
                  : "0"}
              </p>

              <span>{p.status}</span>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

{/* AI ENHANCEMENT BLOCK */}
{/* Add this inside your property map render */}
{/* Replace existing card content with AI-aware version */}

{/* Example:
<div>
  <h3>{p.title}</h3>
{/* ===== AI INTELLIGENCE LAYER ===== */}
<AustinInsightCard ai={p.aiScore} />

{/* ===== MORTGAGE INTELLIGENCE LAYER ===== */}
<RecommendationCard mortgage={p.mortgage} />
  <p>📍 {p.location}</p>
  <p>₦{p.price?.toLocaleString()}</p>

  <div style={{marginTop:10}}>
    <strong>AI Score:</strong>
    <p>Grade: {p.aiScore?.grade}</p>
    <p>Final: {p.aiScore?.finalScore}</p>
    <p>ROI: {p.aiScore?.roiScore}%</p>
    <p>Risk: {p.aiScore?.riskScore}</p>
  </div>
</div>
*/}



