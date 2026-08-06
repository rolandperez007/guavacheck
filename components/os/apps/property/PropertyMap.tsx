"use client";

export default function PropertyMap() {
  return (
    <div className="relative h-[650px] rounded-2xl border border-neutral-800 bg-black">
      <div className="absolute inset-0 opacity-20">
        <div className="h-full w-full bg-[linear-gradient(#333_1px,transparent_1px),linear-gradient(90deg,#333_1px,transparent_1px)] bg-[size:40px_40px]" />
      </div>

      <div className="absolute left-1/2 top-1/2 h-5 w-5 -translate-x-1/2 -translate-y-1/2 rounded-full bg-emerald-400 animate-ping" />

      <div className="absolute bottom-6 left-6 rounded-xl bg-neutral-900 px-5 py-3">
        🌍 Global Property Map
      </div>
    </div>
  );
}
