export class ConstructionPricingModel {
  // -------------------------------------------------
  // LOCATION MULTIPLIERS
  // -------------------------------------------------
  static locationIndex: Record<string, number> = {
    lekki: 1.25,
    ajah: 1.1,
    ikoyi: 1.6,
    victoria_island: 1.7,
    ikorodu: 0.9,
    default: 1.0,
  };

  // -------------------------------------------------
  // COMPATIBILITY WRAPPER (used by engines)
  // -------------------------------------------------
  static calculate(input: {
    sqm: number;
    level?: "basic" | "standard" | "premium";
    location?: string;
  }) {
    const qualityMap: Record<
      "basic" | "standard" | "premium",
      "low" | "standard" | "premium"
    > = {
      basic: "low",
      standard: "standard",
      premium: "premium",
    };

    const report = this.calculateConstructionCost({
      area: input.sqm,
      quality: qualityMap[input.level ?? "standard"],
    });

    const key = (input.location ?? "")
      .toLowerCase()
      .replace(/\s+/g, "_");

    const multiplier = this.locationIndex[key] ?? this.locationIndex.default;

    return {
      baseCost: report.totalCost,
      adjustedCost: Math.round(report.totalCost * multiplier),
      costPerSqm: report.ratePerSqm * multiplier,
      locationMultiplier: multiplier,
      currency: report.currency,
    };
  }

  // -------------------------------------------------
  // CORE PRICING ENGINE
  // -------------------------------------------------
  static calculateConstructionCost(input: {
    area: number;
    type?: string;
    quality?: "low" | "standard" | "premium";
  }) {
    const baseRate: Record<string, number> = {
      low: 12000,
      standard: 18000,
      premium: 25000,
    };

    const quality = input.quality || "standard";
    const rate = baseRate[quality] || baseRate.standard;

    const total = input.area * rate;

    return {
      area: input.area,
      quality,
      ratePerSqm: rate,
      totalCost: total,
      currency: "NGN",
    };
  }

  // -------------------------------------------------
  // MATERIAL ESTIMATION
  // -------------------------------------------------
  static estimateMaterials(area: number) {
    return {
      cementBags: Math.ceil(area * 0.8),
      blocks: Math.ceil(area * 12),
      sandTons: Math.ceil(area * 0.5),
      rodsKg: Math.ceil(area * 8),
    };
  }

  // -------------------------------------------------
  // FULL REPORT GENERATOR
  // -------------------------------------------------
  static generateReport(input: any) {
    const cost = this.calculateConstructionCost(input);

    return {
      summary: cost,
      materials: this.estimateMaterials(input.area),
      timestamp: new Date().toISOString(),
    };
  }
}