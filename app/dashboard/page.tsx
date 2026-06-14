"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { useAuth } from "@/contexts/AuthContext";

type Property = {
  id: string;
  title: string;
  location: string;
  price: number | null;
  status: string;
  user_id: string | null;
  image_url?: string | null;
};

export default function DashboardPage() {
  const { user, loading } = useAuth();
  const router = useRouter();

  const [properties, setProperties] = useState<Property[]>([]);
  const [fetching, setFetching] = useState(true);

  // 🔐 Redirect if not logged in
  useEffect(() => {
    if (!loading && !user) {
      router.push("/login");
    }
  }, [user, loading, router]);

  useEffect(() => {
    async function load() {
      try {
        const res = await fetch("/api/properties");
        const data = await res.json();

        // show only logged-in user's properties
        const mine = (data || []).filter(
          (p: Property) => p.user_id === user?.id
        );

        setProperties(mine);
      } catch (err) {
        console.error(err);
      } finally {
        setFetching(false);
      }
    }

    if (user) load();
  }, [user]);

  if (loading || fetching) {
    return <div style={{ padding: 30 }}>Loading dashboard...</div>;
  }

  return (
    <div style={{ padding: 30 }}>
      <h1 style={{ fontSize: 28, marginBottom: 20 }}>
        My Properties Dashboard
      </h1>

      {properties.length === 0 ? (
        <p>No properties found. Create your first listing.</p>
      ) : (
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))",
            gap: 20,
          }}
        >
          {properties.map((p) => (
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

              <p>
                ₦
                {p.price
                  ? Number(p.price).toLocaleString()
                  : "Price on request"}
              </p>

              <span
                style={{
                  display: "inline-block",
                  padding: "4px 10px",
                  borderRadius: 20,
                  background:
                    p.status === "active" ? "#d4edda" : "#fff3cd",
                  marginTop: 8,
                }}
              >
                {p.status}
              </span>

              <div style={{ marginTop: 12 }}>
                {/* DELETE */}
                <button
                  onClick={async () => {
                    await fetch("/api/properties/delete", {
                      method: "POST",
                      headers: {
                        "Content-Type": "application/json",
                      },
                      body: JSON.stringify({ id: p.id }),
                    });

                    setProperties((prev) =>
                      prev.filter((item) => item.id !== p.id)
                    );
                  }}
                  style={{
                    background: "red",
                    color: "white",
                    border: "none",
                    padding: "6px 10px",
                    marginRight: 10,
                    borderRadius: 6,
                    cursor: "pointer",
                  }}
                >
                  Delete
                </button>

                {/* EDIT (placeholder) */}
                <button
                  onClick={() =>
                    router.push(`/properties/edit/${p.id}`)
                  }
                  style={{
                    background: "black",
                    color: "white",
                    border: "none",
                    padding: "6px 10px",
                    borderRadius: 6,
                    cursor: "pointer",
                  }}
                >
                  Edit
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}