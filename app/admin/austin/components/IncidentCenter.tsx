"use client";

const incidents = [
  {
    severity: "High",
    service: "Verification pipeline",
    customers: "1.2k",
    impact: "$18k",
    rootCause: "AI document classifier latency spike",
    action: "Auto-retry and requeue affected verification requests",
    status: "Mitigating",
    age: "7m",
    progress: "72%",
  },
  {
    severity: "Medium",
    service: "Search API",
    customers: "340",
    impact: "$4.2k",
    rootCause: "Burst traffic in Lagos region",
    action: "Scale read replicas and warm caches",
    status: "Monitoring",
    age: "14m",
    progress: "45%",
  },
];

export default function IncidentCenter() {
  return (
    <section className="rounded-2xl border border-slate-800 bg-slate-950/90 p-6">
      <div className="flex items-center justify-between">
        <div>
          <p className="text-sm uppercase tracking-[0.35em] text-slate-500">Incident center</p>
          <h3 className="mt-2 text-xl font-semibold text-white">Actionable operations incidents</h3>
        </div>
      </div>

      <div className="mt-5 space-y-4">
        {incidents.map((incident) => (
          <div key={incident.service} className="rounded-xl border border-slate-800 bg-slate-900/80 p-4 text-sm text-slate-300">
            <div className="flex flex-wrap items-center justify-between gap-2">
              <div className="font-semibold text-white">{incident.service}</div>
              <div className="rounded-full bg-amber-500/15 px-3 py-1 text-xs uppercase tracking-[0.3em] text-amber-300">{incident.severity}</div>
            </div>
            <div className="mt-3 grid gap-3 md:grid-cols-2">
              <div>Customers affected: {incident.customers}</div>
              <div>Estimated impact: {incident.impact}</div>
              <div>Root cause: {incident.rootCause}</div>
              <div>Recommended action: {incident.action}</div>
            </div>
            <div className="mt-3 flex flex-wrap items-center justify-between gap-2 text-xs uppercase tracking-[0.25em] text-slate-500">
              <span>Status: {incident.status}</span>
              <span>Open: {incident.age}</span>
              <span>Recovery: {incident.progress}</span>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
