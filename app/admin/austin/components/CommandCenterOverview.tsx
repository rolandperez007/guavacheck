"use client";

import { useEffect, useState } from "react";

interface MetricCardProps {
  label: string;
  value: string;
  tone?: "emerald" | "amber" | "sky" | "rose";
}

function MetricCard({ label, value, tone = "sky" }: MetricCardProps) {
  const toneStyles: Record<string, string> = {
    emerald: "text-emerald-300",
    amber: "text-amber-300",
    sky: "text-sky-300",
    rose: "text-rose-300",
  };

  return (
    <div className="rounded-xl border border-slate-800 bg-slate-950/80 p-4">
      <p className="text-sm text-slate-400">{label}</p>
      <p className={`mt-2 text-2xl font-semibold ${toneStyles[tone]}`}>{value}</p>
    </div>
  );
}

export default function CommandCenterOverview() {
  const [now, setNow] = useState(new Date());

  useEffect(() => {
    const timer = window.setInterval(() => setNow(new Date()), 1000);
    return () => window.clearInterval(timer);
  }, []);

  return (
    <section className="rounded-2xl border border-slate-800 bg-slate-950/90 p-6 shadow-2xl shadow-black/20">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <div>
          <p className="text-sm uppercase tracking-[0.35em] text-slate-500">
            Austin Command Center
          </p>
          <h2 className="mt-2 text-2xl font-semibold text-white">Global platform overview</h2>
        </div>
        <div className="rounded-full border border-emerald-500/30 bg-emerald-500/10 px-3 py-1 text-sm text-emerald-300">
          Live • {now.toLocaleTimeString()}
        </div>
      </div>

      <div className="mt-6 grid gap-4 md:grid-cols-2 xl:grid-cols-4">
        <MetricCard label="Active users" value="12.4k" tone="emerald" />
        <MetricCard label="Active sessions" value="3.1k" tone="sky" />
        <MetricCard label="Verification requests" value="842" tone="amber" />
        <MetricCard label="Revenue today" value="$184k" tone="rose" />
      </div>

      <div className="mt-4 rounded-xl border border-slate-800 bg-slate-900/80 p-4 text-sm text-slate-300">
        Austin recommends: queue depth is stable, but high verification demand in Lagos warrants a
        proactive capacity review in the next 10 minutes.
      </div>
    </section>
  );
}
