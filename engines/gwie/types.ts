export enum SupportLevel {
  NONE = 0,
  GLOBAL_AI = 1,
  BASIC = 2,
  DEVELOPING = 3,
  GROWING = 4,
  ADVANCED = 5,
  VERIFIED = 6,
  ENTERPRISE = 7,
  NATIONAL = 8,
  PREMIUM = 9,
  COMPLETE = 10,
}

/**
 * Capability strength model (replaces booleans for scalability)
 */
export type CapabilityState = "none" | "basic" | "standard" | "advanced" | "regulated";

/**
 * Core feature capabilities per country
 */
export interface CapabilitySet {
  construction: CapabilityState;
  valuation: CapabilityState;
  mortgage: CapabilityState;
  insurance: CapabilityState;
  distress: CapabilityState;
  buildingPassport: CapabilityState;
  regulations: CapabilityState;
  materials: CapabilityState;
  climate: CapabilityState;
  taxation: CapabilityState;
  subscriptions: CapabilityState;
  payments: CapabilityState;
}

/**
 * Payment integrations
 */
export interface PaymentProvider {
  id: string;
  name: string;
  supported: boolean;
}

/**
 * Infrastructure maturity per country
 */
export interface InfrastructureProfile {
  internetReliability: "low" | "medium" | "high";
  digitalPaymentsAdoption: number; // 0 - 100
  dataAvailability: "low" | "medium" | "high";
}

/**
 * Legal/regulatory environment
 */
export interface RegulatoryProfile {
  regulatoryStrength: "low" | "medium" | "high" | "strict";
  legalSystem: "common_law" | "civil_law" | "mixed";
}

/**
 * Country configuration model
 */
export interface CountryProfile {
  code: string;
  iso3: string;
  name: string;
  continent: string;
  capital: string;

  currency: string;
  language: string[];
  timezone: string[];
  measurementSystem: "metric" | "imperial";

  supportLevel: SupportLevel;

  capabilities: CapabilitySet;
  paymentProviders: PaymentProvider[];

  infrastructure?: InfrastructureProfile;
  regulation?: RegulatoryProfile;
}

/**
 * User runtime context
 */
export interface UserContext {
  country: string;
  language: string;
  currency: string;
  timezone: string;
}

/**
 * Project runtime context
 */
export interface ProjectContext {
  country: string;
  supportLevel: SupportLevel;
  profile: CountryProfile;
}

/**
 * Engine runtime context
 */
export interface EngineContext {
  user: UserContext;
  project: ProjectContext;
}

/**
 * Fallback system for missing/unknown data
 */
export interface FallbackStrategy {
  enabled: boolean;
  strategy: "ai_estimate" | "regional_proxy" | "manual_override";
}

/**
 * Main system context (runtime brain)
 */
export interface AustinContext extends EngineContext {
  fallback?: FallbackStrategy;
}
