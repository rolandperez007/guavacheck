import { ConstructionPricingModel } from "@/lib/austin/models/ConstructionPricingModel";
import { DistressedScoringEngine } from "@/lib/austin/intelligence/DistressedScoringEngine";

export class PropertyRankingEngine {
  static rank(property: any) {
    const construction = ConstructionPricingModel.calculate({
      sqm: property.sqm || 100,
      level: property.level || "standard",
      location: property.location,
    });

    const distressed = DistressedScoringEngine.score({
      marketValue: property.marketValue,
      askingPrice: property.askingPrice,
      location: property.location,
      condition: property.condition,
    });

    const investmentScore =
      distressed.score * 0.6 +
      ((property.rentalYield || 5) * 5);

    return {
      investmentScore: Math.round(investmentScore),

      constructionEstimate:
        construction.adjustedCost ?? construction.baseCost,

      distressedScore: distressed.score,

      grade:
        investmentScore > 80
          ? "A+"
          : investmentScore > 60
          ? "A"
          : investmentScore > 40
          ? "B"
          : "C",

      meta: {
        model: "ranking-engine-v1",
      },
    };
  }
}