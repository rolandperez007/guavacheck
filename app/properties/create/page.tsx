"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

export default function CreatePropertyPage() {
  const router = useRouter();

  const [title, setTitle] = useState("");
  const [location, setLocation] = useState("");
  const [price, setPrice] = useState("");
  const [imageUrl, setImageUrl] = useState("");
  const [uploading, setUploading] = useState(false);
  const [loading, setLoading] = useState(false);

  // 📤 IMAGE UPLOAD
  async function uploadImage(file: File) {
    setUploading(true);

    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("/api/properties/upload", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();

    setUploading(false);

    if (data.url) {
      setImageUrl(data.url);
    } else {
      alert("Image upload failed");
    }
  }

  // 📦 SUBMIT PROPERTY
  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);

    const res = await fetch("/api/properties", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        title,
        location,
        price: Number(price),
        image_url: imageUrl,
        status: "draft",
      }),
    });

    const data = await res.json();

    setLoading(false);

    if (res.ok) {
      router.push("/properties");
    } else {
      alert(data.error || "Failed to create property");
    }
  }

  return (
    <div style={{ padding: 30, maxWidth: 600 }}>
      <h1 style={{ fontSize: 28, marginBottom: 20 }}>
        Create Property
      </h1>

      <form onSubmit={handleSubmit}>
        {/* TITLE */}
        <input
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          style={inputStyle}
        />

        {/* LOCATION */}
        <input
          placeholder="Location"
          value={location}
          onChange={(e) => setLocation(e.target.value)}
          style={inputStyle}
        />

        {/* PRICE */}
        <input
          placeholder="Price"
          type="number"
          value={price}
          onChange={(e) => setPrice(e.target.value)}
          style={inputStyle}
        />

        {/* IMAGE UPLOAD */}
        <input
          type="file"
          onChange={(e) => {
            const file = e.target.files?.[0];
            if (file) uploadImage(file);
          }}
          style={{ marginBottom: 15 }}
        />

        {uploading && <p>Uploading image...</p>}

        {imageUrl && (
          <img
            src={imageUrl}
            style={{ width: "100%", marginBottom: 15 }}
          />
        )}

        {/* SUBMIT */}
        <button
          type="submit"
          disabled={loading}
          style={buttonStyle}
        >
          {loading ? "Creating..." : "Create Property"}
        </button>
      </form>
    </div>
  );
}

// 🎨 STYLES
const inputStyle: React.CSSProperties = {
  display: "block",
  width: "100%",
  padding: 12,
  marginBottom: 12,
  border: "1px solid #ddd",
  borderRadius: 8,
};

const buttonStyle: React.CSSProperties = {
  width: "100%",
  padding: 12,
  background: "black",
  color: "white",
  border: "none",
  borderRadius: 8,
  cursor: "pointer",
};