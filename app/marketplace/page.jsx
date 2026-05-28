"use client";

export default function MarketplacePage() {

  return (

    <div style={{ padding: 30 }}>

      <h1>Guava Contractor Marketplace</h1>

      <p>AI-powered contractor ecosystem.</p>

      <div style={{
        display: "grid",
        gridTemplateColumns: "repeat(auto-fit,minmax(250px,1fr))",
        gap: 20,
        marginTop: 30
      }}>

        <div style={{
          background: "white",
          padding: 20,
          borderRadius: 10
        }}>
          <h3>Active Jobs</h3>
          <p>Live contractor requests.</p>
        </div>

        <div style={{
          background: "white",
          padding: 20,
          borderRadius: 10
        }}>
          <h3>Escrow Protected</h3>
          <p>Secure milestone payments.</p>
        </div>

        <div style={{
          background: "white",
          padding: 20,
          borderRadius: 10
        }}>
          <h3>AI Matching</h3>
          <p>Smart contractor recommendations.</p>
        </div>

      </div>

    </div>

  );
}
