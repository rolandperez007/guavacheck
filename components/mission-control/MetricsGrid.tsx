"use client";

const metrics = [
  ["Active Properties", "18,492"],

  ["Countries", "42"],

  ["Verifications", "1,832"],

  ["Austin Missions", "218"],

  ["Construction Models", "684"],

  ["Investor Portfolios", "529"],
];

export default function MetricsGrid() {
  return (
    <div className="grid grid-cols-2 gap-4">
      {metrics.map(([title, value]) => (
        <div
          key={title}

          className="rounded-2xl border border-neutral-800 bg-neutral-950 p-5"
        >
          <p className="text-xs uppercase tracking-widest text-neutral-500">{title}</p>

          <h2 className="mt-4 text-3xl font-bold text-white">{value}</h2>
        </div>
      ))}
    </div>
  );
}
