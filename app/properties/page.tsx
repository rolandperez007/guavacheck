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

  const [search, setSearch] = useState("");
  const [minPrice, setMinPrice] = useState("");
  const [maxPrice, setMaxPrice] = useState("");
  const [status, setStatus] = useState("all");

  // ✅ FETCH DATA (clean separation)
  const loadProperties = async () => {
    try {
      const res = await fetch("/api/properties");
      const data = await res.json();

      setProperties(data || []);
      setFiltered(data || []);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadProperties();
  }, []);

  // FILTER ENGINE
  useEffect(() => {
    let result = [...properties];

    if (search) {
      result = result.filter(
        (p) =>
          p.title?.toLowerCase().includes(search.toLowerCase()) ||
          p.location?.toLowerCase().includes(search.toLowerCase())
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
    return <div style={{ padding: 30 }}>Loading properties...</div>;
  }

  return (
    <div style={{ padding: 30 }}>
      <h1>Property Listings</h1>

      <div style={{ display: "grid", gridTemplateColumns: "2fr 1fr 1fr 1fr", gap: 10 }}>
        <input placeholder="Search..." value={search} onChange={(e) => setSearch(e.target.value)} />
        <input placeholder="Min Price" value={minPrice} onChange={(e) => setMinPrice(e.target.value)} />
        <input placeholder="Max Price" value={maxPrice} onChange={(e) => setMaxPrice(e.target.value)} />

        <select value={status} onChange={(e) => setStatus(e.target.value)}>
          <option value="all">All</option>
          <option value="draft">Draft</option>
          <option value="active">Active</option>
          <option value="sold">Sold</option>
        </select>
      </div>

      <div style={{ marginTop: 20 }}>
        {filtered.map((p) => (
          <div key={p.id} style={{ padding: 10, border: "1px solid #ddd", marginBottom: 10 }}>
            <h3>{p.title}</h3>
            <p>{p.location}</p>
            <strong>₦{p.price ?? 0}</strong>
          </div>
        ))}
      </div>
    </div>
  );
}
