import { MarketplaceBrain } from "@/lib/austin/market/MarketplaceBrain";

export async function GET() {

  const sampleProperties = [
    {
      id: "1",
      title: "Luxury Apartment",
      price: 250000000,
      location: "Dubai",
      sqm: 300,
      level: "luxury",
      region: "middle_east",
      currency: "AED",
      investment: { score: 78 }
    },
    {
      id: "2",
      title: "Modern Home",
      price: 120000000,
      location: "Lagos",
      sqm: 250,
      level: "standard",
      region: "africa",
      currency: "NGN",
      investment: { score: 65 }
    }
  ];

  const feed = await MarketplaceBrain.processFeed(sampleProperties);

  return Response.json({
    portfolioValue: 370000000,
    activeDeals: feed.filter(f => f.decision === "PROCEED"),
    opportunities: feed.map(f => ({
      title: f.listing.headline,
      roi: f.analysis?.economyScore || 0,
      risk: f.negotiation?.probabilityOfClose < 50 ? "HIGH" : "MEDIUM"
    })),
    insights: [
      "Global property index active",
      "Autonomous deal engine running",
      "Negotiation AI optimizing offers"
    ]
  });
}
