/**
 * ===========================================================
 * GUAVA COMMERCE ENGINE
 * Pricing Type Definitions
 *
 * Guava Networks Inc.
 * ===========================================================
 */

export type BillingCycle = "monthly" | "yearly";

export type PlanType = "free" | "starter" | "professional" | "business" | "enterprise";

export interface Plan {
  id: PlanType;

  name: string;

  basePriceUSD: number;

  billingCycle: BillingCycle;

  features: string[];

  active: boolean;
}

export interface CountryTier {
  countryCode: string;

  tier: number;

  purchasingPowerMultiplier: number;

  preferredCurrency: string;

  preferredProvider: string;
}

export interface PricingRequest {
  country: string;

  currency?: string;

  plan: PlanType;

  billingCycle: BillingCycle;
}

export interface PricingResult {
  success: boolean;

  originalPriceUSD: number;

  localizedPrice: number;

  currency: string;

  country: string;

  provider: string;

  multiplier: number;

  savings: number;
}
