"use client";

const watchlist = [
  ["Ocean View Towers", "92"],

  ["Eko Atlantic Plot", "98"],

  ["Victoria Island Office", "88"],

  ["Banana Island Villa", "96"],
];

export default function InvestorWatchlist() {
  return (
    <section className="rounded-3xl border border-neutral-800 bg-neutral-950 p-8">
      <h2 className="text-3xl font-semibold">Investor Watchlist</h2>

      <div className="mt-8 space-y-5">
        {watchlist.map(([name, score]) => (
          <div key={name} className="rounded-2xl border border-neutral-800 p-5">
            <div className="flex justify-between">
              <div>{name}</div>

              <div className="text-emerald-400">AI Score {score}</div>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
