import { DistressedScoringEngine } from "@/lib/austin/intelligence/DistressedScoringEngine";
import { ConstructionPricingModel } from "@/lib/austin/models/ConstructionPricingModel";

export class DistressedMarketplaceEngine {

  // 🏚 Score and list distressed opportunity
  static analyzeListing(property: any) {

    const construction = ConstructionPricingModel.calculate({
      sqm: property.sqm || 100,
      level: property.level || "standard",
      location: property.location
    });

    const distressed = DistressedScoringEngine.score({
      marketValue: property.marketValue,
      askingPrice: property.askingPrice,
      location: property.location,
      condition: property.condition
    });

    const spread = property.marketValue - property.askingPrice;

    const roiPotential = spread / (construction.estimatedCost || 1);

    return {
      id: property.id,
      title: property.title,
      location: property.location,

      pricing: {
        askingPrice: property.askingPrice,
        marketValue: property.marketValue,
        spread
      },

      constructionEstimate: construction.estimatedCost,

      distressedScore: distressed.score,

      roiPotential: Math.round(roiPotential * 100),

      grade: distressed.grade,

      investmentTag:
        distressed.score > 70
          ? "HOT DEAL"
          : distressed.score > 40
          ? "WATCHLIST"
          : "LOW PRIORITY",

      meta: {
        model: "distressed-market-v1"
      }
    };
  }

  // 📊 Bulk ranking
  static rankListings(listings: any[]) {
    return listings
      .map(this.analyzeListing)
      .sort((a, b) => b.distressedScore - a.distressedScore);
  }
}

