import { DistressedScoringEngine } from "@/lib/austin/intelligence/DistressedScoringEngine";
import { ConstructionPricingModel } from "./ConstructionPricingModel";

export class DistressedMarketplaceEngine {

  static analyzeListing(property: any) {
    const construction = ConstructionPricingModel.calculate({
      sqm: property.sqm || 100,
      level: property.level || "standard",
      location: property.location,
    });

    return {
      score: DistressedScoringEngine.score(property),
      rehabEstimate: construction,
    };
  }

  static rankListings(listings: any[]) {
    return listings
      .map((listing) => ({
        ...listing,
        analysis: this.analyzeListing(listing),
      }))
      .sort((a, b) => {
        const scoreA = a.analysis?.score || 0;
        const scoreB = b.analysis?.score || 0;
        return scoreB - scoreA;
      });
  }
}