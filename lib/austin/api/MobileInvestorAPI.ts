import { DistressedMarketplaceEngine } from "@/lib/austin/market/DistressedMarketplaceEngine";
import { InvestorDashboardEngine } from "@/lib/austin/investor/InvestorDashboardEngine";

export class MobileInvestorAPI {

  static async getDeals(listings: any[]) {
    return DistressedMarketplaceEngine.rankListings(listings);
  }

  static async getPortfolio(userProperties: any[]) {
    return InvestorDashboardEngine.buildPortfolio(userProperties);
  }

  static async getSummary(listings: any[]) {

    const ranked = DistressedMarketplaceEngine.rankListings(listings);

    return {
      totalDeals: ranked.length,
      hotDeals: ranked.filter(d => d.investmentTag === "HOT DEAL").length,
      avgScore:
        ranked.reduce((a, b) => a + b.distressedScore, 0) / ranked.length
    };
  }
}
