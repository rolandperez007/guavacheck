"use client";

import { useEffect, useState } from "react";
import { useParams, useRouter } from "next/navigation";

type Property = {
  id: string;
  title: string;
  location: string;
  price: number | null;
  status: string;
  image_url?: string | null;
};

export default function EditPropertyPage() {
  const { id } = useParams();
  const router = useRouter();

  const [loading, setLoading] = useState(true);

  const [title, setTitle] = useState("");
  const [location, setLocation] = useState("");
  const [price, setPrice] = useState("");
  const [status, setStatus] = useState("draft");
  const [image_url, setImageUrl] = useState("");

  // 🔄 LOAD PROPERTY
  useEffect(() => {
    async function load() {
      try {
        const res = await fetch("/api/properties");
        const data = await res.json();

        const property = data.find((p: Property) => p.id === id);

        if (!property) return;

        setTitle(property.title || "");
        setLocation(property.location || "");
        setPrice(property.price ? String(property.price) : "");
        setStatus(property.status || "draft");
        setImageUrl(property.image_url || "");
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    }

    if (id) load();
  }, [id]);

  // 💾 UPDATE PROPERTY
  async function updateProperty() {
    const res = await fetch("/api/properties/update", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        id,
        title,
        location,
        price: price ? Number(price) : 0,
        status,
        image_url,
      }),
    });

    const data = await res.json();

    if (!res.ok) {
      alert(data.error || "Update failed");
      return;
    }

    alert("Property updated successfully");
    router.push("/dashboard");
  }

  if (loading) {
    return <div style={{ padding: 30 }}>Loading property...</div>;
  }

  return (
    <div style={{ padding: 30, maxWidth: 500 }}>
      <h1>Edit Property</h1>

      <input
        placeholder="Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        style={{ display: "block", margin: 10, width: "100%" }}
      />

      <input
        placeholder="Location"
        value={location}
        onChange={(e) => setLocation(e.target.value)}
        style={{ display: "block", margin: 10, width: "100%" }}
      />

      <input
        placeholder="Price"
        value={price}
        onChange={(e) => setPrice(e.target.value)}
        style={{ display: "block", margin: 10, width: "100%" }}
      />

      <input
        placeholder="Image URL"
        value={image_url}
        onChange={(e) => setImageUrl(e.target.value)}
        style={{ display: "block", margin: 10, width: "100%" }}
      />

      <select
        value={status}
        onChange={(e) => setStatus(e.target.value)}
        style={{ display: "block", margin: 10, width: "100%" }}
      >
        <option value="draft">Draft</option>
        <option value="active">Active</option>
        <option value="sold">Sold</option>
      </select>

      <button
        onClick={updateProperty}
        style={{
          background: "green",
          color: "white",
          padding: "10px 15px",
          border: "none",
          marginTop: 10,
          cursor: "pointer",
        }}
      >
        Save Changes
      </button>
    </div>
  );
}