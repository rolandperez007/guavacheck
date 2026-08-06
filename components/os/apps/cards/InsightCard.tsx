"use client";

export default function InsightCard() {
  return (
    <section className="rounded-3xl border border-neutral-800 bg-gradient-to-br from-neutral-950 to-neutral-900 p-8">
      <div className="text-sm uppercase tracking-widest text-emerald-400">AI Insight</div>

      <h2 className="mt-4 text-3xl font-semibold">
        Property demand is increasing across premium coastal districts.
      </h2>

      <p className="mt-6 leading-8 text-neutral-400">
        Austin analysed market activity, investor demand, listing velocity and construction trends
        to produce this recommendation.
      </p>

      <button className="mt-8 rounded-xl bg-emerald-500 px-6 py-3 font-semibold text-black">
        View Analysis
      </button>
    </section>
  );
}
