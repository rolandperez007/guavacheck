export type PropertyInput = {
  location?: string;
  price?: number;
  landSize?: number;
};

export type ArchitectureSuggestion = {
  recommendedType: "flat" | "duplex" | "terrace";
  floors: number;
  reason: string;
  estimatedCost: number;
  roiScore: number;
};

// 🌍 Simple architecture intelligence engine
export function generateArchitectAdvice(input: PropertyInput): ArchitectureSuggestion {
  const landSize = input.landSize ?? 300;
  const price = input.price ?? 0;

  let recommendedType: "flat" | "duplex" | "terrace" = "flat";
  let floors = 1;

  // 💰 base construction cost (naira per sqm)
  let baseCost = landSize * 1200;

  // 🧠 Decision logic
  if (landSize > 500) {
    recommendedType = "terrace";
    floors = 3;
    baseCost *= 1.8;
  } else if (landSize > 300) {
    recommendedType = "duplex";
    floors = 2;
    baseCost *= 1.4;
  }

  // 📈 ROI model
  const estimatedRevenue = price * 1.6;
  const roiScore = estimatedRevenue / (baseCost || 1);

  return {
    recommendedType,
    floors,
    estimatedCost: Math.round(baseCost),
    roiScore: Number(roiScore.toFixed(2)),
    reason:
      recommendedType === "terrace"
        ? "Large land favors multi-unit development for maximum yield"
        : recommendedType === "duplex"
          ? "Medium land optimized for duplex structure and resale value"
          : "Small land best suited for compact flat design",
  };
}
