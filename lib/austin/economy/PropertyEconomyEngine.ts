import { DistressedDealEngine } from "@/lib/austin/intelligence/DistressedDealEngine";
import { ListingGenerator } from "@/lib/austin/marketing/ListingGenerator";
import { CommunityEngine } from "@/lib/austin/marketing/CommunityEngine";
import { BOQService } from "../services/BOQService";

export class PropertyEconomyEngine {
  static analyze(property: any) {
    const valuation = BOQService.calculateTotalCost({
      sqm: property.sqm,
      level: property.level,
    });

    const distress = DistressedDealEngine.analyze(property);
    const listing = ListingGenerator.generate(property);
    const post = CommunityEngine.generatePost(property);

    return {
      valuation,
      distress,
      listing,
      communityPost: post,

      economyScore: distress.opportunityScore * 0.4 + (property.investment?.score || 50) * 0.6,
    };
  }
}
