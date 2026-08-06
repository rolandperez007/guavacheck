"use client";

import AustinOrb from "@/components/icons/AustinOrb";

export default function Dock() {
  return (
    <footer className="fixed bottom-6 left-1/2 z-50 -translate-x-1/2">
      <div className="flex items-center gap-4 rounded-2xl border border-neutral-800 bg-neutral-950/90 px-6 py-4 backdrop-blur-xl">
        <button className="rounded-xl p-3 transition hover:bg-neutral-800">🏠</button>

        <button className="rounded-xl p-3 transition hover:bg-neutral-800">📁</button>

        <button className="rounded-xl p-3 transition hover:bg-neutral-800">📈</button>

        <button className="rounded-xl bg-neutral-800 p-3">
          <AustinOrb size={30} state="processing" />
        </button>

        <button className="rounded-xl p-3 transition hover:bg-neutral-800">🔔</button>

        <button className="rounded-xl p-3 transition hover:bg-neutral-800">⚙️</button>
      </div>
    </footer>
  );
}
