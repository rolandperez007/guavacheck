"use client";

const forecasts = [
  { label: "Queue saturation", value: "Low risk in 15m" },
  { label: "Worker exhaustion", value: "Monitor worker #3" },
  { label: "Traffic spikes", value: "Expected in Lagos at 18:00" },
  { label: "Revenue anomalies", value: "No unusual deviation" },
];

export default function PredictiveIntelligence() {
  return (
    <section className="rounded-2xl border border-slate-800 bg-slate-950/90 p-6">
      <div>
        <p className="text-sm uppercase tracking-[0.35em] text-slate-500">
          Predictive intelligence
        </p>
        <h3 className="mt-2 text-xl font-semibold text-white">
          Austin forecasts and recommendations
        </h3>
      </div>

      <div className="mt-5 grid gap-3 md:grid-cols-2">
        {forecasts.map((forecast) => (
          <div
            key={forecast.label}
            className="rounded-xl border border-slate-800 bg-slate-900/80 p-4 text-sm text-slate-300"
          >
            <div className="font-semibold text-white">{forecast.label}</div>
            <div className="mt-2 text-slate-400">{forecast.value}</div>
          </div>
        ))}
      </div>
    </section>
  );
}
