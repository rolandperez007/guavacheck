"use client";

const opportunities = [
  {
    title: "Waterfront Apartment",
    location: "Ikoyi",
    roi: "18.4%",
    confidence: "97%"
  },
  {
    title: "Commercial Tower",
    location: "Victoria Island",
    roi: "15.1%",
    confidence: "94%"
  },
  {
    title: "Mixed Use Estate",
    location: "Lekki",
    roi: "21.8%",
    confidence: "96%"
  },
  {
    title: "Residential Land",
    location: "Epe",
    roi: "31.4%",
    confidence: "92%"
  }
];

export default function OpportunityFeed() {
  return (
    <section className="rounded-3xl border border-neutral-800 bg-neutral-950 p-8">

      <div className="flex items-center justify-between">

        <h2 className="text-3xl font-semibold">
          AI Opportunities
        </h2>

        <span className="rounded-full bg-emerald-500/20 px-4 py-2 text-sm text-emerald-400">
          Austin Ranked
        </span>

      </div>

      <div className="mt-8 space-y-4">

        {opportunities.map((item) => (

          <div
            key={item.title}
            className="rounded-2xl border border-neutral-800 p-5 hover:border-emerald-500 transition"
          >

            <div className="flex justify-between">

              <div>

                <h3 className="font-semibold">
                  {item.title}
                </h3>

                <p className="text-neutral-500">
                  {item.location}
                </p>

              </div>

              <div className="text-right">

                <div className="text-xl font-bold text-emerald-400">
                  {item.roi}
                </div>

                <div className="text-sm text-neutral-500">
                  Confidence {item.confidence}
                </div>

              </div>

            </div>

          </div>

        ))}

      </div>

    </section>
  );
}