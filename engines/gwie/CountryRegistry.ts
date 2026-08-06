import countries from "@/knowledge/countries/countries.json";

import { CountryProfile, SupportLevel, CapabilitySet } from "./types";

export class CountryRegistry {
  private static registry = new Map<string, CountryProfile>();

  /**
   * Load the bundled country registry.
   * Safe to call multiple times.
   */
  static initialize(): void {
    if (this.registry.size > 0) return;

    countries.forEach((country: any) => {
      this.register({
        ...country,

        measurementSystem: country.measurement,

        supportLevel: SupportLevel.GLOBAL_AI,

        paymentProviders: [],

        capabilities: {
          construction: "none",
          valuation: "none",
          mortgage: "none",
          insurance: "none",
          distress: "none",
          buildingPassport: "none",
          regulations: "none",
          materials: "none",
          climate: "none",
          taxation: "none",
          subscriptions: "standard",
          payments: "standard",
        } satisfies CapabilitySet,
      });
    });
  }

  /**
   * Register or replace a country profile.
   */
  static register(profile: CountryProfile): void {
    this.registry.set(profile.code.toUpperCase(), profile);
  }

  /**
   * Lookup by ISO-2 code.
   */
  static byCode(code: string): CountryProfile | undefined {
    return this.registry.get(code.toUpperCase());
  }

  /**
   * Return every registered country.
   */
  static all(): CountryProfile[] {
    return [...this.registry.values()];
  }

  /**
   * Check whether a country exists.
   */
  static has(code: string): boolean {
    return this.registry.has(code.toUpperCase());
  }

  /**
   * Number of registered countries.
   */
  static count(): number {
    return this.registry.size;
  }

  /**
   * Clear registry (mainly for testing).
   */
  static clear(): void {
    this.registry.clear();
  }
}
