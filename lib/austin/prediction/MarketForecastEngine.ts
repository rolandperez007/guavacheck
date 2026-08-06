export class MarketForecastEngine {
  static history: any[] = [];

  static predict(property: any) {
    const price = property?.price ?? 0;
    const location = (property?.location ?? "").toLowerCase();

    // simple risk scoring baseline
    let riskScore = 0;

    if (price > 200_000_000) riskScore += 30;
    if (location.includes("lekki")) riskScore -= 10;
    if (location.includes("ikorodu")) riskScore += 15;

    // clamp values safely
    riskScore = Math.max(0, Math.min(100, riskScore));

    const confidence = 0.7;

    let recommendation: "BUY" | "AVOID" | "HOLD" = "HOLD";

    if (riskScore < 30) recommendation = "BUY";
    if (riskScore > 70) recommendation = "AVOID";

    // ✅ FIX: create proper result object
    const result = {
      propertyId: property?.id ?? null,
      price,
      location,
      riskScore,
      confidence,
      recommendation,
      growthRate: property?.growthRate ?? 5,
      timestamp: new Date().toISOString(),
    };

    // store safely
    MarketForecastEngine.history.push(result);

    return {
      riskScore,
      confidence,
      recommendation,
      growthRate: property?.growthRate ?? 5,
    };
  }
}
