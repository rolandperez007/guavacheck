import { BOQService } from "./services/BOQService";
import { ValuationService } from "./services/ValuationService";
import { MortgageService } from "./services/MortgageService";
import { FraudService } from "./services/FraudService";
import { ReportService } from "./services/ReportService";

export const ToolRegistry = {
  boq: BOQService,
  valuation: ValuationService,
  mortgage: MortgageService,
  fraud: FraudService,
  report: ReportService,
};