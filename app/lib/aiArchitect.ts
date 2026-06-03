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

// 🌍 Simple intelligence model (upgradeable to ML later)
export function generateArchitectAdvice(
  input: PropertyInput
): ArchitectureSuggestion {
  const landSize = input.landSize || 300; // sqm default
  const price = input.price || 0;

  let recommendedType: "flat" | "duplex" | "terrace" = "flat";
  let floors = 1;
  let baseCost = landSize * 1200; // construction baseline (naira per sqm)

  // 🧠 DECISION ENGINE
  if (landSize > 500) {
    recommendedType = "terrace";
    floors = 3;
    baseCost *= 1.8;
  } else if (landSize > 300) {
    recommendedType = "duplex";
    floors = 2;
    baseCost *= 1.4;
  }

  // 💰 ROI logic (simplified)
  const estimatedRevenue = price * 1.6; // resale uplift assumption
  const roiScore = estimatedRevenue / (baseCost || 1);

  return {
    recommendedType,
    floors,
    reason:
      recommendedType === "terrace"
        ? "Large land favors multi-unit development for maximum yield"
        : recommendedType === "duplex"
        ? "Medium land optimized for duplex structure and resale value"
        : "Small land best suited for compact flat design",
    estimatedCost: Math.round(baseCost),
    roiScore: Number(roiScore.toFixed(2)),
  };
}