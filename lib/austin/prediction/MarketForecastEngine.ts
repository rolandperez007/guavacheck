import { LearningEngine } from "@/lib/austin/ml/LearningEngine";
export class MarketForecastEngine {

  static history: any[] = [];

  static predict(property: any) {

    const price = property.price || 0;
    const location = property.location || "unknown";

    // 🧠 simplified predictive model (later replace with ML model)
    const growthFactor = this.getGrowthFactor(location);
    const demandScore = this.getDemandScore(property);
    const riskScore = this.getRiskScore(property);

    const futureValue = price * (1 + growthFactor);

    const confidence = LearningEngine.adjustConfidence
      Math.max(0.5, 1 - (riskScore / 100));

    const prediction = {
      currentPrice: price,
      predictedPrice: Math.round(futureValue),
      growthRate: Math.round(growthFactor * 100),
      demandScore,
      riskScore,
      confidence: Number(confidence.toFixed(2)),
      horizonMonths: 24,
      recommendation: this.getRecommendation(growthFactor, riskScore)
    };

    this.history.push({
      property,
      prediction,
      timestamp: new Date()
    });

    return prediction;
  }

  static getGrowthFactor(location: string) {

    const map: Record<string, number> = {
      "Dubai": 0.18,
      "London": 0.06,
      "New York": 0.05,
      "Lagos": 0.10,
      "default": 0.04
    };

    return map[location] || map["default"];
  }

  static getDemandScore(property: any) {

    const base = (property.bedrooms || 2) * 10;
    const priceFactor = property.price > 100000000 ? 40 : 20;

    return Math.min(100, base + priceFactor);
  }

  static getRiskScore(property: any) {

    let risk = 20;

    if (property.type === "luxury") risk += 10;
    if (property.location === "unknown") risk += 30;
    if (property.price > 500000000) risk += 15;

    return Math.min(100, risk);
  }

  static getRecommendation(growth: number, risk: number) {

    if (growth > 0.1 && risk < 30) return "STRONG_BUY";
    if (growth > 0.05) return "BUY";
    if (risk > 60) return "AVOID";

    return "HOLD";
  }
}

