import { PropertyEconomyEngine } from "../economy/PropertyEconomyEngine";
import { NegotiationEngine } from "../negotiation/NegotiationEngine";
import { EscrowEngine } from "../escrow/EscrowEngine";

export class AustinAutonomousAgent {
  static async run(property: any) {
    // 1. FULL ECONOMY ANALYSIS
    const analysis = PropertyEconomyEngine.analyze(property);

    // 2. NEGOTIATION STRATEGY
    const negotiation = NegotiationEngine.analyze({
      askingPrice: property.price,
      marketValue: analysis?.valuation?.total || property.price,
      urgencyLevel: property.urgency || "medium",
      buyerBudget: property.buyerBudget,
    });

    // 3. DEAL DECISION ENGINE
    const decision = this.decide(analysis, negotiation);

    // 4. ESCROW PREVIEW (ONLY IF PROCEED)
    let escrowPreview: any = null;

    if (decision.action === "PROCEED") {
      escrowPreview = EscrowEngine.createDeal({
        buyer: "AUTO_AGENT",
        seller: property.ownerId || "UNKNOWN",
        propertyId: property.id || "PROPERTY",
        amount: property.price || 0,
      });
    }

    return {
      analysis,
      negotiation,
      decision,
      escrowPreview,
    };
  }

  static decide(analysis: any, negotiation: any) {
    const score = analysis?.economyScore || 0;
    const close = negotiation?.probabilityOfClose || 0;

    let action: "PROCEED" | "MONITOR" | "IGNORE" = "IGNORE";

    if (score > 75 && close > 70) {
      action = "PROCEED";
    } else if (score > 60) {
      action = "MONITOR";
    }

    return {
      action,
      confidence: Math.round((score + close) / 2),
      reasoning:
        action === "PROCEED"
          ? "High-value asset with strong closing probability"
          : action === "MONITOR"
            ? "Potential opportunity but needs tracking"
            : "Low ROI or weak deal signals",
    };
  }
}
