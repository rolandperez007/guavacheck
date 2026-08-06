"use client";

const recommendations = [
  "3 undervalued waterfront properties found.",

  "Mortgage rates dropped by 0.8%.",

  "Construction materials cheaper this week.",

  "Land prices rising around Lekki Free Zone.",
];

export default function RecommendationCard() {
  return (
    <section className="rounded-3xl border border-emerald-500/20 bg-neutral-950 p-8">
      <h2 className="text-2xl font-semibold">Austin Recommendations</h2>

      <div className="mt-8 space-y-4">
        {recommendations.map((item, index) => (
          <div
            key={index}

            className="rounded-xl bg-neutral-900 p-5"
          >
            {item}
          </div>
        ))}
      </div>
    </section>
  );
}
