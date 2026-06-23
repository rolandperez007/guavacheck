export type IntentType =
  | "boq_analysis"
  | "property_valuation"
  | "contractor_verification"
  | "investment_analysis"
  | "mortgage_analysis"
  | "property_search"
  | "risk_analysis"
  | "unknown";

export interface AustinIntent {
  type: IntentType;
  confidence: number;
  raw: string;
  entities?: Record<string, any>;
}

export interface AustinPlan {
  intent: IntentType;
  steps: string[];
  output:
    | "table"
    | "insight"
    | "report"
    | "scorecard"
    | "listings"
    | "message"
    | "finance_table";
}

export interface ExecutionStepResult {
  step: string;
  data: any;
}

export interface AustinExecutionResult {
  stepsCompleted: string[];
  tables: any[];
  insights: any[];
  raw: any[];
}

export interface AustinReport {
  project: {
    location: string;
    sqm: number;
    level: "basic" | "standard" | "luxury";
  };

  summary: {
    totalCost: number;
    costPerSqm: number;
    durationWeeks: number;
    breakdown?: Record<string, number>;
  };

  phases: {
    phase: string;
    durationWeeks: number;
    cost: number;
  }[];

  insights: string[];
}
