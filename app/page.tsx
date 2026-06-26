"use client";

export default function Home() {
  return (
    <main
      style={{
        minHeight: "100vh",
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        background: "#0b0f17",
        color: "white",
        textAlign: "center",
        padding: "40px",
      }}
    >
      <h1 style={{ fontSize: "3rem", marginBottom: "10px" }}>
        GuavaCheck
      </h1>

      <p style={{ opacity: 0.7, marginBottom: "30px", maxWidth: "500px" }}>
        AI-powered real estate intelligence system for pricing,
        investment scoring, and property analysis.
      </p>

      <div
        style={{
          display: "flex",
          gap: "12px",
          flexWrap: "wrap",
          justifyContent: "center",
        }}
      >
        <a href="/dashboard" style={btn}>Open Dashboard</a>
        <a href="/investor" style={btn}>Investor View</a>
        <a href="/marketplace" style={btn}>Marketplace</a>
        <a href="/ai/architect" style={btn}>AI Architect</a>
      </div>
    </main>
  );
}

const btn: React.CSSProperties = {
  padding: "12px 18px",
  background: "#4f46e5",
  color: "white",
  borderRadius: "8px",
  textDecoration: "none",
  fontSize: "14px",
};