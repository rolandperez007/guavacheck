import { ConstructionPricingModel } from "@/lib/austin/models/ConstructionPricingModel";

export class DistressedScoringEngine {

  static score(property: {
    marketValue: number;
    askingPrice: number;
    sqm?: number;
    location?: string;
    condition?: "good" | "fair" | "poor";
  }) {

    const undervaluation = (property.marketValue - property.askingPrice) / property.marketValue;

    const priceGapScore = Math.max(0, undervaluation * 100);

    const conditionMultiplier =
      property.condition === "poor" ? 1.3 :
      property.condition === "fair" ? 1.1 : 1;

    const locationRisk = property.location?.includes("luxury") ? 0.8 : 1;

    const finalScore = Math.min(
      100,
      (priceGapScore * conditionMultiplier * locationRisk)
    );

    return {
      score: Math.round(finalScore),

      breakdown: {
        undervaluation,
        priceGapScore,
        conditionMultiplier,
        locationRisk
      },

      grade:
        finalScore > 75 ? "A+" :
        finalScore > 50 ? "A" :
        finalScore > 30 ? "B" : "C",

      recommendation:
        finalScore > 70
          ? "HIGH PRIORITY INVESTMENT"
          : finalScore > 40
          ? "REVIEW OPPORTUNITY"
          : "LOW PRIORITY",

      meta: {
        model: "distressed-scoring-v1",
        confidence: 0.88
      }
    };
  }
}

