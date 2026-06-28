"use client";

import { useState } from "react";
import { runAustin } from "@/lib/austin/brain";

export default function AustinPage() {
  const [input, setInput] = useState<any>({
    intent: "sell",
    property: {
      name: "Test Property",
      propertyType: "duplex",
      bedrooms: 4,
      bathrooms: 3,
      toilets: 4,
      parkingSpaces: 2,
      landSize: 600,
      buildingSize: 450,
      floors: 2,
      condition: "good",
      furnished: true,
      description: "Sample property for Austin testing",
    },
    location: {
      country: "Nigeria",
      state: "Lagos",
      city: "Lekki",
      area: "Ikate",
      street: "Test Street",
    },
    media: {
      photos: [],
      videos: [],
      floorPlans: [],
      droneImages: [],
      virtualTours: [],
    },
    documents: {
      certificateOfOccupancy: [],
      surveyPlan: [],
      deedOfAssignment: [],
      buildingApproval: [],
      taxClearance: [],
      valuationReport: [],
      otherDocuments: [],
    },
  });

  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  async function run() {
    setLoading(true);

    const output = await runAustin(input);

    setResult(output);

    setLoading(false);
  }

  return (
    <div className="grid grid-cols-2 gap-6 p-6">

      {/* LEFT PANEL */}
      <div className="space-y-4">

        <h1 className="text-2xl font-bold">
          Austin Console
        </h1>

        <button
          onClick={run}
          className="rounded-lg bg-black px-4 py-2 text-white"
        >
          Run Austin Analysis
        </button>

        <pre className="h-[600px] overflow-auto rounded-lg bg-gray-100 p-4 text-xs">
{JSON.stringify(input, null, 2)}
        </pre>
      </div>

      {/* RIGHT PANEL */}
      <div className="space-y-4">

        <h2 className="text-xl font-semibold">
          Austin Output
        </h2>

        {loading && (
          <p className="text-blue-600">
            Austin is thinking...
          </p>
        )}

        {result && (
          <div className="space-y-4">

            {/* TITLE */}
            <div className="rounded-lg border p-4">
              <h3 className="font-bold">
                {result.title}
              </h3>
              <p className="text-sm text-gray-600">
                {result.summary}
              </p>
            </div>

            {/* INSIGHTS */}
            <div className="rounded-lg border p-4">
              <h4 className="font-semibold">Insights</h4>
              <ul className="list-disc pl-5 text-sm">
                {result.insights.map((i: string, idx: number) => (
                  <li key={idx}>{i}</li>
                ))}
              </ul>
            </div>

            {/* WARNINGS */}
            <div className="rounded-lg border p-4">
              <h4 className="font-semibold text-red-600">
                Warnings
              </h4>
              <ul className="list-disc pl-5 text-sm">
                {result.warnings.map((w: string, idx: number) => (
                  <li key={idx}>{w}</li>
                ))}
              </ul>
            </div>

            {/* RECOMMENDATIONS */}
            <div className="rounded-lg border p-4">
              <h4 className="font-semibold text-green-600">
                Recommendations
              </h4>
              <ul className="list-disc pl-5 text-sm">
                {result.recommendations.map((r: string, idx: number) => (
                  <li key={idx}>{r}</li>
                ))}
              </ul>
            </div>

            {/* CONFIDENCE */}
            <div className="rounded-lg border p-4">
              <h4 className="font-semibold">
                Confidence
              </h4>
              <p className="text-lg">
                {result.confidence.value}%
              </p>
            </div>

          </div>
        )}
      </div>
    </div>
  );
}