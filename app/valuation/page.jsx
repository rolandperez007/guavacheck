"use client";

import { useState } from "react";

export default function ValuationPage() {

  const [result, setResult] = useState(null);

  async function handleSubmit() {

    const res = await fetch("/api/ai/valuation", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        location: "Lekki",
        propertyType: "duplex",
        bedrooms: 4,
        landSize: 650
      })
    });

    const data = await res.json();

    setResult(data);
  }

  return (
    <div style={{ padding: 20 }}>
      <h1>Guava AI Valuation</h1>

      <button onClick={handleSubmit}>
        Run AI Valuation
      </button>

      {result && (
        <div style={{ marginTop: 20 }}>
          <p>
            Estimated Value:
            ?{result.estimatedValue?.toLocaleString()}
          </p>

          <p>
            Rental Estimate:
            ?{result.rentalEstimate?.toLocaleString()}
          </p>

          <p>
            Confidence:
            {result.confidence}
          </p>

          <p>
            AI Commentary:
            {result.commentary}
          </p>
        </div>
      )}
    </div>
  );
}
