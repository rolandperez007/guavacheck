"use client";

export default function HeroCard() {
  return (
    <section className="relative overflow-hidden rounded-3xl border border-neutral-800 bg-gradient-to-br from-black via-neutral-950 to-neutral-900 p-10">

      <div className="absolute right-0 top-0 h-72 w-72 rounded-full bg-emerald-500/10 blur-3xl" />

      <div className="relative z-10 max-w-3xl">

        <p className="text-sm uppercase tracking-[0.35em] text-emerald-400">
          Guava Intelligence
        </p>

        <h1 className="mt-4 text-5xl font-bold leading-tight">
          Welcome to your Global Property Intelligence Dashboard
        </h1>

        <p className="mt-6 max-w-2xl text-lg leading-8 text-neutral-300">
          Search, verify, analyse and invest with Austin AI while monitoring
          markets across the world from a single workspace.
        </p>

        <div className="mt-10 flex flex-wrap gap-4">

          <button className="rounded-xl bg-emerald-500 px-6 py-3 font-semibold text-black hover:bg-emerald-400">
            Explore Opportunities
          </button>

          <button className="rounded-xl border border-neutral-700 px-6 py-3 hover:bg-neutral-900">
            Open Austin AI
          </button>

        </div>

      </div>

    </section>
  );
}