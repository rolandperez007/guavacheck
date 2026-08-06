"use client";

export default function Clouds() {
  return (
    <div className="absolute inset-0 overflow-hidden pointer-events-none">
      <div
        className="
        absolute top-20 left-0
        h-32 w-72
        rounded-full
        bg-white/30
        blur-3xl
        animate-[cloud_60s_linear_infinite]
        "
      />

      <div
        className="
        absolute top-48 right-0
        h-40 w-96
        rounded-full
        bg-white/20
        blur-3xl
        animate-[cloud_90s_linear_infinite]
        "
      />
    </div>
  );
}
