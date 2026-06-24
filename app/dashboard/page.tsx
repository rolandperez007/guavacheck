"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

type Property = {
  id: string;
  title?: string;
};

export default function DashboardPage() {
  const router = useRouter();

  const [properties, setProperties] = useState<Property[]>([]);
  const [fetching, setFetching] = useState(true);

  // 🔐 TEMP SAFE REDIRECT (no auth system required)
  useEffect(() => {
    const isLoggedIn = false; // replace later when auth is ready

    if (!isLoggedIn) {
      router.push("/login");
    }
  }, [router]);

  // 📦 mock data
  useEffect(() => {
    const mockData: Property[] = [
      { id: "1", title: "Sample Property 1" },
      { id: "2", title: "Sample Property 2" }
    ];

    setProperties(mockData);
    setFetching(false);
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h1>Dashboard</h1>

      <h2>Your Properties</h2>

      {fetching ? (
        <p>Loading...</p>
      ) : (
        <ul>
          {properties.map((p) => (
            <li key={p.id}>{p.title}</li>
          ))}
        </ul>
      )}
    </div>
  );
}