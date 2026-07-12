"use client";

import CommandCenterOverview from "./components/CommandCenterOverview";
import OperationalIntelligenceFeed from "./components/OperationalIntelligenceFeed";
import IncidentCenter from "./components/IncidentCenter";
import PredictiveIntelligence from "./components/PredictiveIntelligence";
import SystemHealth from "./components/SystemHealth";
import EngineStatus from "./components/EngineStatus";
import JobQueue from "./components/JobQueue";
import LiveLogs from "./components/LiveLogs";
import LiveEventFeed from "./components/LiveEventFeed";

export default function AustinCommandCenter() {
  return (
    <main className="min-h-screen bg-[radial-gradient(circle_at_top,_rgba(34,197,94,0.14),_transparent_28%),linear-gradient(135deg,_#020617,_#0f172a)] p-6 text-slate-100">
      <div className="mx-auto flex max-w-7xl flex-col gap-6">
        <header className="rounded-2xl border border-slate-800 bg-slate-950/80 p-6 shadow-2xl shadow-black/20">
          <p className="text-sm uppercase tracking-[0.35em] text-emerald-400">Austin command center</p>
          <h1 className="mt-3 text-4xl font-semibold text-white">The operational brain of GuavaCheck</h1>
          <p className="mt-3 max-w-3xl text-sm text-slate-400">
            Austin continuously monitors the platform, prioritizes what needs attention, and recommends actions before customers feel the impact.
          </p>
        </header>

        <CommandCenterOverview />

        <div className="grid gap-6 xl:grid-cols-[1.2fr_0.8fr]">
          <OperationalIntelligenceFeed />
          <IncidentCenter />
        </div>

        <LiveEventFeed />

        <PredictiveIntelligence />
        <SystemHealth />
        <EngineStatus />

        <div className="grid gap-6 lg:grid-cols-[0.9fr_1.1fr]">
          <JobQueue />
          <LiveLogs />
        </div>
      </div>
    </main>
  );
}