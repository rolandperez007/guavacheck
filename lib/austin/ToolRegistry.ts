
import { BOQService } from "@/services/austin/BOQService";
import { ValuationService } from "@/services/austin/ValuationService";
import { PropertyService } from "@/services/austin/PropertyService";
import { ContractorService } from "@/services/austin/ContractorService";
import { MortgageService } from "@/services/austin/MortgageService";
import { FraudService } from "@/services/austin/FraudService";

import { DistressedScoringEngine } from "@/lib/austin/intelligence/DistressedScoringEngine";
import { DistressedMarketplaceEngine } from "@/lib/austin/market/DistressedMarketplaceEngine";
import { BlogEngine } from "@/lib/austin/marketing/BlogEngine";
import { CommunityEngine } from "@/lib/austin/marketing/CommunityEngine";

export const ToolRegistry = {

  // Core Services
  boq: BOQService,
  valuation: ValuationService,
  property: PropertyService,
  contractor: ContractorService,
  mortgage: MortgageService,
  fraud: FraudService,

  // Distressed Property Intelligence
  distressedScoring: DistressedScoringEngine,
  distressedMarketplace: DistressedMarketplaceEngine,

  // Content Ecosystem
  blog: BlogEngine,
  community: CommunityEngine

};



