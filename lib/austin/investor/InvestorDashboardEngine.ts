import { PropertyRankingEngine } from "@/lib/austin/ranking/PropertyRankingEngine";
import { DistressedScoringEngine } from "@/lib/austin/intelligence/DistressedScoringEngine";

export class InvestorDashboardEngine {
  static buildPortfolio(properties: any[]) {
    const enriched = properties.map((p) => {
      const ranking = PropertyRankingEngine.rank(p);

      const distressed = DistressedScoringEngine.score({
        marketValue: p.marketValue,
        askingPrice: p.askingPrice,
        location: p.location,
        condition: p.condition,
      });

      return {
        id: p.id,
        title: p.title,

        investmentScore: ranking.investmentScore,
        distressedScore: distressed.score,

        roi: p.rentalYield || 0,

        combinedScore: ranking.investmentScore * 0.6 + distressed.score * 0.4,

        recommendation:
          ranking.investmentScore > 75 ? "BUY" : ranking.investmentScore > 50 ? "REVIEW" : "IGNORE",
      };
    });

    return enriched.sort((a, b) => b.combinedScore - a.combinedScore);
  }
}
