"use client";

export default function PortfolioSummary() {
  return (
    <section className="rounded-3xl border border-neutral-800 bg-neutral-950 p-8">

      <div className="flex items-center justify-between">

        <div>

          <h2 className="text-3xl font-semibold">
            Portfolio
          </h2>

          <p className="mt-2 text-neutral-400">
            Your verified property assets will appear here.
          </p>

        </div>

        <button className="rounded-xl bg-emerald-500 px-5 py-3 font-semibold text-black">
          Add Property
        </button>

      </div>

      <div className="mt-10 rounded-2xl border-2 border-dashed border-neutral-700 p-16 text-center">

        <h3 className="text-2xl font-semibold">
          Your portfolio is empty
        </h3>

        <p className="mt-4 text-neutral-400">
          Verify your first property or import an existing portfolio
          to unlock analytics, valuation and investment intelligence.
        </p>

      </div>

    </section>
  );
}