export class NegotiationEngine {

  static analyze(input: {
    askingPrice: number;
    marketValue: number;
    urgencyLevel?: "low" | "medium" | "high";
    buyerBudget?: number;
  }) {

    const discount = (input.marketValue - input.askingPrice) / input.marketValue * 100;

    const urgencyMultiplier =
      input.urgencyLevel === "high" ? 1.3 :
      input.urgencyLevel === "medium" ? 1.1 : 1.0;

    const buyerGap = input.buyerBudget
      ? ((input.buyerBudget - input.askingPrice) / input.askingPrice) * 100
      : null;

    const negotiationRangeLow = input.askingPrice * 0.92 * urgencyMultiplier;
    const negotiationRangeHigh = input.askingPrice * 1.03;

    let strategy = "HOLD";

    if (discount > 20 && urgencyMultiplier > 1.1) {
      strategy = "AGGRESSIVE BUY";
    } else if (discount > 10) {
      strategy = "NEGOTIATE DOWN";
    } else if (buyerGap && buyerGap < 0) {
      strategy = "PRICE ABOVE BUDGET — COUNTER REQUIRED";
    }

    const probabilityOfClose =
      Math.min(95,
        Math.max(20,
          (discount * 1.5) +
          (input.urgencyLevel === "high" ? 25 : 10)
        )
      );

    return {
      discount: Math.round(discount),
      urgencyMultiplier,
      buyerGap: buyerGap ? Math.round(buyerGap) : null,

      negotiationRange: {
        low: Math.round(negotiationRangeLow),
        high: Math.round(negotiationRangeHigh)
      },

      strategy,
      probabilityOfClose: Math.round(probabilityOfClose),

      recommendation:
        probabilityOfClose > 70
          ? "STRONGLY RECOMMEND CLOSE"
          : probabilityOfClose > 40
          ? "NEGOTIATE"
          : "WAIT OR REPRICE"
    };
  }
}

