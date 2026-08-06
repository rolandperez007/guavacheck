export type IntentType = "valuation" | "mortgage" | "boq" | "market" | "report" | "agent";

export type AustinOutput =
  "table" | "insight" | "report" | "scorecard" | "finance_table" | "listings" | "message";

export interface AustinIntent {
  raw: string;
  confidence: number;
  type: IntentType;
  entities: Record<string, any>;
}

export interface AustinPlan {
  intent: IntentType;
  steps: string[];
  output: AustinOutput;
}
