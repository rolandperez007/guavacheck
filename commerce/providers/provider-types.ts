/**
 * ===========================================================
 * GUAVA COMMERCE ENGINE
 * Provider Types
 *
 * Guava Networks Inc.
 * ===========================================================
 */

export interface PaymentProvider {
  id: string;

  name: string;

  supportedCountries: string[];

  supportedCurrencies: string[];

  supportsSubscriptions: boolean;

  supportsRefunds: boolean;

  supportsWebhooks: boolean;

  enabled: boolean;
}
