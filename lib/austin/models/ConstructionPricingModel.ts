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

  static 
  calculate(input: {
    sqm: number;
    level: "basic" | "standard" | "luxury";
    location?: string;
    risk?: "low" | "medium" | "high";
    currency?: string;
  }) {

    const sqm = input.sqm;
    const level = input.level;
    const location = (input.location || "default").toLowerCase();

    const baseRate = this.baseRates.perSqm[level];
    const locationMultiplier = this.locationIndex[location] || 1;
    const riskMultiplier = this.riskIndex?.[input.risk || "low"] || 1;
    const currency = input.currency || "NGN";
    const currencyRate = this.currencyRates?.[currency] || 1;

    const rawCost = sqm * baseRate * locationMultiplier * riskMultiplier;

    const finalCost = rawCost * currencyRate;

    return {
      sqm,
      level,
      location,
      risk: input.risk || "low",
      currency,

      breakdown: {
        baseRate,
        locationMultiplier,
        riskMultiplier,
        currencyRate
      },

      estimatedCost: Math.round(finalCost),

      range: {
        low: Math.round(finalCost * 0.9),
        high: Math.round(finalCost * 1.15)
      },

      meta: {
        model: "construction-pricing-v2-global",
        confidence: 0.91
      }
    };
  }
;
  }
}




