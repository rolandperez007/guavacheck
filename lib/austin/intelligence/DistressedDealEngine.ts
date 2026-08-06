export class DistressedDealEngine {
  static analyze(property: any) {
    const price = property.price || 0;
    const marketValue = property.aiScore?.marketValue || price * 1.2;

    // discount depth (how undervalued)
    const discount = ((marketValue - price) / marketValue) * 100;

    // urgency signals
    const urgencyKeywords = ["urgent", "must sell", "bank", "liquidation", "distress"];
    const text = `${property.title} ${property.description || ""}`.toLowerCase();

    let urgencyScore = 0;

    urgencyKeywords.forEach((k) => {
      if (text.includes(k)) urgencyScore += 15;
    });

    // location liquidity proxy
    const liquidityMap: Record<string, number> = {
      luxury: 0.7,
      urban: 1.0,
      suburban: 0.8,
      remote: 0.5,
    };

    const liquidity = liquidityMap[property.segment || "urban"] || 0.8;

    // final opportunity score
    const opportunityScore = discount * 0.5 + urgencyScore * 0.3 + (1 - liquidity) * 20;

    let label = "NORMAL";

    if (opportunityScore > 70) label = "HOT DEAL";
    else if (opportunityScore > 40) label = "OPPORTUNITY";
    else if (discount > 20) label = "UNDERVALUED";

    return {
      discount: Math.round(discount),
      urgencyScore,
      liquidity,
      opportunityScore: Math.round(opportunityScore),
      label,
    };
  }
}
