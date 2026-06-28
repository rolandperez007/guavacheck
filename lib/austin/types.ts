/**
 * Austin AI Core Types
 * The shared language of the entire intelligence system
 */

/* -----------------------------
   BASIC CONTEXT
------------------------------*/

export interface PropertyContext {
  id?: string;

  intent?: UserIntent;

  property?: any;     // will tighten later
  location?: any;
  media?: any;
  documents?: any;

  timestamp?: number;
}

/* -----------------------------
   USER INTENT
------------------------------*/

export type UserIntent =
  | "price_estimate"
  | "valuation"
  | "verification"
  | "sell_advice"
  | "distress_analysis"
  | "construction_analysis"
  | "design_advice"
  | "market_insight"
  | "media_review"
  | "document_review"
  | "general_query";

/* -----------------------------
   SPECIALISTS
------------------------------*/

export type AustinSpecialist =
  | "valuation"
  | "construction"
  | "legal"
  | "media"
  | "distress"
  | "design"
  | "inspection"
  | "market";

/* -----------------------------
   SPECIALIST REQUEST
------------------------------*/

export interface SpecialistRequest {
  specialist: AustinSpecialist;

  task: string;

  context: PropertyContext;

  priority: "low" | "medium" | "high";
}

/* -----------------------------
   SPECIALIST RESPONSE
------------------------------*/

export interface SpecialistResponse {
  specialist: AustinSpecialist;

  summary: string;

  findings: string[];

  risks?: string[];

  opportunities?: string[];

  data?: Record<string, any>;
}

/* -----------------------------
   CONFIDENCE MODEL
------------------------------*/

export interface ConfidenceScore {
  value: number; // 0 - 100

  factors: string[];

  limitations?: string[];
}

/* -----------------------------
   AUSTIN DECISION
------------------------------*/

export interface AustinDecision {
  intent: UserIntent;

  specialistsUsed: AustinSpecialist[];

  reasoning: string[];

  confidence: ConfidenceScore;
}

/* -----------------------------
   FINAL RESPONSE
------------------------------*/

export interface AustinResponse {
  title: string;

  summary: string;

  insights: string[];

  warnings: string[];

  recommendations: string[];

  confidence: ConfidenceScore;

  nextActions: string[];

  raw?: any; // internal debug data
}

/* -----------------------------
   WIZARD INTEGRATION TYPES
------------------------------*/

export interface WizardAustinInput {
  property: any;
  location: any;
  media: any;
  documents: any;
  intent: string | null;
}

/* -----------------------------
   INTERNAL THINKING STEP
------------------------------*/

export interface AustinThinkingStep {
  step: string;

  description: string;

  result?: string;

  confidenceImpact?: number;
}