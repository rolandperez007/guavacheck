"use client";

const markets = [
  {
    city: "Lekki",
    growth: "+18%",
    sentiment: "Bullish",
  },
  {
    city: "Ikoyi",
    growth: "+11%",
    sentiment: "Strong",
  },
  {
    city: "Abuja",
    growth: "+9%",
    sentiment: "Growing",
  },
  {
    city: "Dubai",
    growth: "+16%",
    sentiment: "Hot",
  },
  {
    city: "London",
    growth: "+5%",
    sentiment: "Stable",
  },
];

export default function TrendingMarkets() {
  return (
    <section className="rounded-3xl border border-neutral-800 bg-neutral-950 p-8">
      <h2 className="text-3xl font-semibold">Trending Markets</h2>

      <div className="mt-8 space-y-4">
        {markets.map((market) => (
          <div
            key={market.city}
            className="flex items-center justify-between rounded-2xl border border-neutral-800 p-5"
          >
            <div>
              <h3 className="font-semibold">{market.city}</h3>

              <p className="text-neutral-500">{market.sentiment}</p>
            </div>

            <div className="text-right">
              <div className="text-xl font-bold text-emerald-400">{market.growth}</div>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
