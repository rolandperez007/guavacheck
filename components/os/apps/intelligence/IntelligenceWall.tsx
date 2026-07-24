"use client";

const engines = [
  "Austin AI",
  "Verification Engine",
  "Market Intelligence",
  "Construction Intelligence",
  "Investment Intelligence",
  "Geo Intelligence",
  "Currency Engine",
  "Knowledge Engine"
];

export default function IntelligenceWall() {
  return (
    <section className="rounded-3xl border border-neutral-800 bg-neutral-950 p-8">

      <h2 className="text-3xl font-semibold">
        Intelligence Wall
      </h2>

      <div className="mt-8 grid gap-5 md:grid-cols-2 xl:grid-cols-4">

        {engines.map((engine) => (

          <div
            key={engine}
            className="rounded-2xl border border-neutral-800 bg-black p-6 hover:border-emerald-500 transition"
          >

            <div className="mb-5 h-3 w-3 rounded-full bg-emerald-400 animate-pulse" />

            <h3 className="font-semibold">
              {engine}
            </h3>

            <p className="mt-3 text-sm text-neutral-500">
              Ready
            </p>

          </div>

        ))}

      </div>

    </section>
  );
}