"use client";

import AustinOrb from "@/components/icons/AustinOrb";

export default function Topbar() {
  return (
    <header className="flex h-16 items-center justify-between border-b border-neutral-800 bg-neutral-950 px-8">

      <div>

        <h2 className="text-xl font-semibold text-white">
          Welcome back
        </h2>

      </div>

      <div className="flex items-center gap-5">

        <input
          placeholder="Search anything..."
          className="w-96 rounded-xl border border-neutral-800 bg-black px-4 py-2 outline-none"
        />

        <AustinOrb
          size={22}
          state="idle"
        />

      </div>

    </header>
  );
}