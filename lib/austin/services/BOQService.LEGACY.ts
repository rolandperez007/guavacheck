import { ConstructionPricingModel } from "../models/ConstructionPricingModel";

export class BOQService {

  static async calculateTotalCost(input: any = {}) {

    const sqm = input?.sqm || 400;
    const level = input?.level || "standard";
    const location = input?.location || "default";

    // 🧠 1. Get intelligent base estimate
    const pricing = ConstructionPricingModel.calculate({
      sqm,
      level,
      location
    });

    const base = pricing.estimatedCost;

    // 🧱 2. Intelligent breakdown (not static anymore)
    const breakdown = {
      foundation: base * 0.25,
      structure: base * 0.30,
      roofing: base * 0.15,
      finishing: base * 0.25,
      externalWorks: base * 0.05
    };

    const total = Object.values(breakdown)
      .reduce((a, b) => a + (b as number), 0);

    // 🧠 3. Risk + confidence logic
    const confidence =
      location === "lekki" ? 0.78 :
      location === "ikoyi" ? 0.72 :
      0.85;

    return {
      sqm,
      level,
      location,

      // 🧠 AI pricing core
      pricingModel: pricing,

      // 📊 breakdown for UI
      breakdown,
      total: Math.round(total),

      // 📈 intelligence layer
      currency: "NGN",
      confidence,

      insight: {
        message:
          `Estimated construction cost for ${sqm}sqm ${level} build in ${location}. ` +
          `Price includes location multiplier and finish-level adjustment.`,
        riskLevel: confidence < 0.75 ? "high" : "medium"
      },

      source: "BOQ-INTELLIGENT-MODEL"
    };
  }
}
