"use client";

import AustinOrb from "@/components/icons/AustinOrb";

export default function StatusBar() {
  return (
    <footer className="flex h-10 items-center justify-between border-t border-neutral-800 bg-neutral-950 px-6 text-xs text-neutral-400">
      <div className="flex items-center gap-6">
        <span>Workspace: Default</span>

        <span>Server: Connected</span>

        <span>Supabase: Ready</span>
      </div>

      <div className="flex items-center gap-3">
        <AustinOrb
          size={14}

          state="processing"
        />

        <span>Austin Operational</span>
      </div>
    </footer>
  );
}
