"use client";

export default function AmbientLife() {
  return (
    <div className="absolute inset-0 pointer-events-none">
      {/* Future simulation layer:
          vehicles
          pedestrians
          birds
          city activity
          weather particles
      */}

      <div
        className="
        absolute bottom-10 left-1/3
        h-1 w-32
        bg-white/20
        rounded-full
        blur-sm
        "
      />
    </div>
  );
}
