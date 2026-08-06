"use client";

import CommandBar from "./CommandBar";

export default function Topbar() {
  return (
    <header className="sticky top-0 z-50 border-b border-neutral-800 bg-neutral-950/95 backdrop-blur">
      <div className="flex h-20 items-center justify-between gap-8 px-8">
        <div>
          <h1 className="text-2xl font-bold">Dashboard</h1>

          <p className="text-sm text-neutral-500">Global Property Intelligence Platform</p>
        </div>

        <div className="flex-1 max-w-3xl">
          <CommandBar />
        </div>

        <div className="flex items-center gap-4">
          <button className="rounded-full bg-neutral-900 px-4 py-2">🔔</button>

          <button className="rounded-full bg-neutral-900 px-4 py-2">⚙️</button>

          <div className="flex h-12 w-12 items-center justify-center rounded-full bg-emerald-500 font-bold text-black">
            G
          </div>
        </div>
      </div>
    </header>
  );
}
