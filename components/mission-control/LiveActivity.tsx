"use client";

const activity = [
  "Property verified • 2 sec ago",

  "Market updated • 12 sec ago",

  "Portfolio synced • 24 sec ago",

  "Construction estimate completed",

  "Satellite imagery refreshed",

  "AI report exported",
];

export default function LiveActivity() {
  return (
    <div className="rounded-2xl border border-neutral-800 bg-neutral-950 p-6">
      <h2 className="mb-5 text-lg font-semibold text-white">Live Intelligence</h2>

      <div className="space-y-3">
        {activity.map((item) => (
          <div
            key={item}

            className="rounded-xl bg-black p-4 text-neutral-300"
          >
            {item}
          </div>
        ))}
      </div>
    </div>
  );
}
