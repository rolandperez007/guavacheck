import { MarketForecastEngine } from "@/lib/austin/prediction/MarketForecastEngine";
import { ComplianceEngine } from "@/lib/austin/compliance/ComplianceEngine";
import { EscrowEngine } from "@/lib/austin/escrow/EscrowEngine";

export class AustinAgent {
  static async analyzeDeal(input: any) {
    const prediction = MarketForecastEngine.predict(input.property);

    const compliance = ComplianceEngine.complianceScore(input.user, {
      amount: input.property.price,
      country: input.property.location,
    });

    return {
      decision: this.makeDecision(prediction, compliance),
      prediction,
      compliance,
      recommendations: this.generateRecommendations(prediction, compliance),
    };
  }

  static makeDecision(prediction: any, compliance: any) {
    if (!compliance.approved) return "REJECTED_RISK";

    if (prediction.recommendation === "STRONG_BUY" && compliance.complianceScore > 70) {
      return "APPROVE_STRATEGIC_DEAL";
    }

    if (prediction.recommendation === "BUY") {
      return "APPROVE_WITH_REVIEW";
    }

    if (prediction.recommendation === "AVOID") {
      return "BLOCK_HIGH_RISK";
    }

    return "MANUAL_REVIEW";
  }

  static generateRecommendations(prediction: any, compliance: any) {
    const recs: string[] = [];

    if (prediction.riskScore > 60) {
      recs.push("Negotiate price reduction before proceeding");
    }

    if (prediction.growthRate > 10) {
      recs.push("High-growth zone detected — prioritize acquisition");
    }

    if (!compliance.approved) {
      recs.push("User fails compliance checks — require verification upgrade");
    }

    if (prediction.confidence < 0.7) {
      recs.push("Low confidence model — request additional data sources");
    }

    return recs;
  }

  static async createAutonomousDeal(input: any) {
    const analysis = await this.analyzeDeal(input);

    if (analysis.decision !== "APPROVE_STRATEGIC_DEAL") {
      return {
        status: "BLOCKED",
        analysis,
      };
    }

    const escrow = EscrowEngine.createDeal({
      buyer: input.user.id,
      seller: input.seller,
      propertyId: input.property.id,
      amount: input.property.price,
    });

    return {
      status: "DEAL_CREATED",
      escrow,
      analysis,
    };
  }
}
