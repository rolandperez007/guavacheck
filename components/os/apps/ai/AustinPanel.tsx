"use client";

export default function AustinPanel() {
  return (
    <aside className="rounded-3xl border border-emerald-500/20 bg-neutral-950 p-8">
      <div className="mb-6 flex items-center gap-3">
        <div className="h-4 w-4 rounded-full bg-emerald-400 animate-pulse" />

        <h2 className="text-2xl font-semibold">Austin AI</h2>
      </div>

      <p className="leading-8 text-neutral-300">Good afternoon.</p>

      <p className="mt-4 leading-8 text-neutral-400">
        I am monitoring property markets, investment trends, verification requests and construction
        intelligence across the platform.
      </p>

      <div className="mt-8 space-y-3">
        <button className="w-full rounded-xl bg-white py-3 font-semibold text-black">
          Start Conversation
        </button>

        <button className="w-full rounded-xl border border-neutral-700 py-3">
          Generate Report
        </button>
      </div>
    </aside>
  );
}
