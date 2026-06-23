export class ConstructionPricingModel {

  static baseRates = {
    perSqm: {
      basic: 180000,
      standard: 250000,
      luxury: 380000
    }
  };

  
  static riskIndex: Record<string, number> = {
    low: 1.0,
    medium: 1.1,
    high: 1.25
  };

  static currencyRates: Record<string, number> = {
    USD: 1,
    NGN: 1500,
    GBP: 0.79,
    EUR: 0.92
  };

  static locationIndex: Record<string, number> = {
    lekki: 1.25,
    ajah: 1.1,
    ikoyi: 1.6,
    victoria_island: 1.7,
    ikorodu: 0.9,
    default: 1.0
  };

    // -----------------------------
  // CORE PRICING ENGINE
  // -----------------------------

  static calculateConstructionCost(input: {
    area: number;
    type?: string;
    quality?: "low" | "standard" | "premium";
  }) {
    const baseRate = {
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

  static estimateMaterials(area: number) {
    return {
      cementBags: Math.ceil(area * 0.8),
      blocks: Math.ceil(area * 12),
      sandTons: Math.ceil(area * 0.5),
      rodsKg: Math.ceil(area * 8),
    };
  }

  static generateReport(input: any) {
    const cost = this.calculateConstructionCost(input);

    return {
      summary: cost,
      materials: this.estimateMaterials(input.area),
      timestamp: new Date().toISOString(),
    };
  }
}  