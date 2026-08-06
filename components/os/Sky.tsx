"use client";

import WorldClock from "./WorldClock";

export default function Sky() {
  return (
    <div className="absolute inset-0 overflow-hidden">
      <div
        className="
        absolute inset-0
        bg-gradient-to-b
        from-sky-300
        via-blue-200
        to-orange-100
        dark:from-slate-950
        dark:via-indigo-950
        dark:to-black
        transition-colors
        duration-[3000ms]
        "
      />

      <WorldClock />
    </div>
  );
}
