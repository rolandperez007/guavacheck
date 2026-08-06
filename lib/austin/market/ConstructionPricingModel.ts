export type PricingInput = {
  sqm: number;
  level: "basic" | "standard" | "premium";
  location?: string;
};

export type PricingOutput = {
  baseCost: number;
  adjustedCost: number;
  costPerSqm: number;
};

export class ConstructionPricingModel {
  private static baseRates: Record<PricingInput["level"], number> = {
    basic: 120000,
    standard: 180000,
    premium: 300000,
  };

  private static locationMultiplier(location?: string): number {
    if (!location) return 1;

    const l = location.toLowerCase();

    if (l.includes("lagos")) return 1.25;
    if (l.includes("abuja")) return 1.3;
    if (l.includes("lekki")) return 1.4;
    if (l.includes("ajah")) return 1.35;

    return 1;
  }

  static calculate(input: PricingInput): PricingOutput {
    const sqm = input.sqm || 100;
    const level = input.level || "standard";

    const baseRate = this.baseRates[level];
    const baseCost = baseRate * sqm;

    const multiplier = this.locationMultiplier(input.location);
    const adjustedCost = baseCost * multiplier;

    return {
      baseCost,
      adjustedCost,
      costPerSqm: baseRate * multiplier,
    };
  }
}
