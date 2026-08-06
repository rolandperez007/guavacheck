"use client";

const ticker = [
  "🇳🇬 Lagos +18%",
  "🇦🇪 Dubai +11%",
  "🇬🇧 London +5%",
  "🇰🇪 Nairobi +9%",
  "🇺🇸 Miami +12%",
  "🇸🇬 Singapore +6%",
];

export default function GlobalTicker() {
  return (
    <section className="overflow-hidden rounded-2xl border border-neutral-800 bg-black py-4">
      <div className="animate-marquee whitespace-nowrap text-lg">
        {ticker.map((item, index) => (
          <span key={index} className="mx-10">
            {item}
          </span>
        ))}
      </div>
    </section>
  );
}
