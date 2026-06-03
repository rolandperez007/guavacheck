import { ConstructionPricingModel } from "@/lib/austin/models/ConstructionPricingModel";
export class BOQService {

  // 🧱 Base mock data (you will later replace with real market feeds / Supabase)
  static materialRates = {
    cement: 9500,
    blocks: 220,
    sand: 45000,
    granite: 75000,
    ironRod: 850000,
    wood: 600000
  };

  static laborRates = {
    masonPerDay: 12000,
    carpenterPerDay: 15000,
    ironBenderPerDay: 18000,
    laborerPerDay: 8000
  };

  // 📦 1. Material pricing
  static async getMaterialPrices() {
    return {
      source: "BOQService",
      data: this.materialRates
    };
  }

  // 👷 2. Labor rates
  static async getLaborRates() {
    return {
      source: "BOQService",
      data: this.laborRates
    };
  }

  // 📍 3. Location multiplier (Lagos default logic)
  static async applyLocationMultiplier(data: any) {

    const multiplier = 1.0; // later: Lekki = 1.3, Ajah = 1.15, etc.

    return {
      ...data,
      locationMultiplier: multiplier,
      adjusted: true
    };
  }

  // 🧮 4. Cost calculation engine
  
  // 🧮 4. Unified Global Cost Engine (NOW POWERED BY AUSTIN CORE MODEL)
  static async calculateTotalCost(input: any = {}) {

    const result = ConstructionPricingModel.calculate({
      sqm: input.sqm || 100,
      level: input.level || "standard",
      location: input.location || "default",
      risk: input.risk || "low",
      currency: input.currency || "NGN"
    });

    return {
      source: "ConstructionPricingModel",
      breakdown: result.breakdown,
      total: result.estimatedCost,
      range: result.range,
      meta: result.meta
    };
  }

  }

  // 📊 5. BOQ table generator (THIS powers your UI tables)
  
  static async generateTable(data: any) {

    const breakdown = data?.breakdown;

    const safeBreakdown = breakdown || {
      foundation: 0,
      structure: 0,
      roofing: 0,
      finishing: 0,
      externalWorks: 0
    };

    const total = Object.values(safeBreakdown).reduce((a: any, b: any) => a + b, 0);

    const table = Object.entries(safeBreakdown).map(([key, value]) => ({
      item: key,
      cost: value,
      percentage: total ? ((value as number) / total) * 100 : 0
    }));

    return {
      type: "boq_table",
      rows: table,
      total
    };
  }

  }
}


