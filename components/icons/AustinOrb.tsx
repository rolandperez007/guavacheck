"use client";

interface AustinOrbProps {
  size?: number;
  state?: "idle" | "thinking" | "processing" | "listening" | "offline" | "error";
  className?: string;
}

export default function AustinOrb({ size = 24, state = "idle", className = "" }: AustinOrbProps) {
  const stateClasses = {
    idle: "animate-pulse",
    thinking: "animate-spin",
    processing: "animate-pulse",
    listening: "animate-ping",
    offline: "opacity-40",
    error: "animate-pulse",
  };

  const glow = {
    idle: "#10b981",
    thinking: "#22c55e",
    processing: "#34d399",
    listening: "#6ee7b7",
    offline: "#4b5563",
    error: "#ef4444",
  };

  return (
    <div
      className={`relative inline-flex items-center justify-center ${className}`}
      style={{
        width: size,
        height: size,
      }}
    >
      {/* Outer Glow */}
      <div
        className={`absolute rounded-full blur-xl ${stateClasses[state]}`}
        style={{
          width: size,
          height: size,
          background: glow[state],
          opacity: 0.35,
        }}
      />

      {/* Ring */}
      <div
        className="absolute rounded-full border"
        style={{
          width: size,
          height: size,
          borderColor: glow[state],
          opacity: 0.55,
        }}
      />

      {/* Middle Ring */}
      <div
        className="absolute rounded-full border"
        style={{
          width: size * 0.68,
          height: size * 0.68,
          borderColor: glow[state],
          opacity: 0.7,
        }}
      />

      {/* Core */}
      <div
        className={`rounded-full ${stateClasses[state]}`}
        style={{
          width: size * 0.34,
          height: size * 0.34,
          background: glow[state],
          boxShadow: `0 0 18px ${glow[state]}`,
        }}
      />
    </div>
  );
}
