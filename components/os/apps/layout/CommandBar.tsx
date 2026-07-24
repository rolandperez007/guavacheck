"use client";

import { Search, Sparkles } from "lucide-react";

export default function CommandBar() {
  return (
    <section className="rounded-2xl border border-neutral-800 bg-neutral-950 p-4">

      <div className="flex items-center gap-4">

        <Search className="h-5 w-5 text-neutral-500" />

        <input
          placeholder="Ask Austin anything..."
          className="flex-1 bg-transparent outline-none text-white placeholder:text-neutral-500"
        />

        <button className="flex items-center gap-2 rounded-xl bg-emerald-500 px-5 py-2 font-semibold text-black">

          <Sparkles className="h-4 w-4" />

          Ask

        </button>

      </div>

    </section>
  );
}