export enum SupportLevel {
  NONE = "none",
  PLANNED = "planned",
  PARTIAL = "partial",
  GLOBAL_AI = "global_ai",
  FULL = "full",
}

export type CapabilityLevel = "none" | "basic" | "standard" | "advanced" | "full";

export interface CapabilitySet {
  construction: CapabilityLevel;
  valuation: CapabilityLevel;
  mortgage: CapabilityLevel;
  insurance: CapabilityLevel;
  distress: CapabilityLevel;
  buildingPassport: CapabilityLevel;
  regulations: CapabilityLevel;
  materials: CapabilityLevel;
  climate: CapabilityLevel;
  taxation: CapabilityLevel;

  subscriptions: "standard" | "premium" | "enterprise";
  payments: "standard" | "premium";
}

export interface CountryProfile {
  code: string;
  name: string;

  continent: string;
  region?: string;

  currency: string;
  languages: string[];

  supportLevel: SupportLevel;

  paymentProviders: string[];

  capabilities: CapabilitySet;
}
