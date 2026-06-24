export type IntentType =
  | "GENERAL"
  | "ANALYZE"
  | "EXECUTE";

export interface AustinPlan {
  intent: IntentType;
  steps: string[];
  output: "message";
}

export interface AustinExecutionResult {
  stepsCompleted: string[];
  tables: any[];
  insights: any[];
  raw: any[];
}