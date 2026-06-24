import { BOQService } from "../../../lib/austin/services/BOQService";
import { ValuationService } from "../services/ValuationService";
import { MortgageService } from "../services/MortgageService";

import { FraudService } from "../services/FraudService";

export const ToolRegistry = {
  boq: BOQService,
  valuation: ValuationService,
  mortgage: MortgageService,
  
  fraud: FraudService,
};