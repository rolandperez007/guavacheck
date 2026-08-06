"use client";

const insights = [
  "Verification demand increased 18% in Lagos.",
  "Mortgage searches doubled today.",
  "Search latency improved by 22%.",
  "Worker #3 restarted automatically after an elevated error burst.",
];

export default function OperationalIntelligenceFeed() {
  return (
    <section className="rounded-2xl border border-slate-800 bg-slate-950/90 p-6">
      <div className="flex items-center justify-between">
        <div>
          <p className="text-sm uppercase tracking-[0.35em] text-slate-500">
            Austin intelligence feed
          </p>
          <h3 className="mt-2 text-xl font-semibold text-white">Proactive platform guidance</h3>
        </div>
      </div>

      <div className="mt-5 space-y-3">
        {insights.map((insight, index) => (
          <div
            key={insight}
            className="rounded-xl border border-slate-800 bg-slate-900/80 p-4 text-sm text-slate-300"
          >
            <div className="mb-1 text-xs uppercase tracking-[0.3em] text-slate-500">
              Signal {index + 1}
            </div>
            {insight}
          </div>
        ))}
      </div>
    </section>
  );
}
