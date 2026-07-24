"use client";

export default function WorldMap() {
  return (
    <section className="relative overflow-hidden rounded-3xl border border-neutral-800 bg-neutral-950 p-8">

      <div className="absolute inset-0 opacity-10">
        <div className="h-full w-full bg-[radial-gradient(circle_at_center,#10b981_1px,transparent_1px)] bg-[length:28px_28px]" />
      </div>

      <div className="relative">

        <h2 className="text-3xl font-semibold">
          Global Intelligence
        </h2>

        <p className="mt-2 text-neutral-400">
          Live monitoring across property markets.
        </p>

        <div className="mt-12 flex items-center justify-center">

          <div className="relative h-[420px] w-full rounded-2xl border border-neutral-800 bg-black">

            <div className="absolute left-[18%] top-[38%] h-4 w-4 rounded-full bg-emerald-400 animate-ping" />
            <div className="absolute left-[46%] top-[28%] h-4 w-4 rounded-full bg-sky-400 animate-ping" />
            <div className="absolute left-[70%] top-[46%] h-4 w-4 rounded-full bg-orange-400 animate-ping" />
            <div className="absolute left-[62%] top-[18%] h-4 w-4 rounded-full bg-purple-400 animate-ping" />

            <div className="absolute bottom-6 left-6 rounded-xl bg-neutral-900 px-4 py-2">
              🌍 7 Languages Active
            </div>

          </div>

        </div>

      </div>

    </section>
  );
}