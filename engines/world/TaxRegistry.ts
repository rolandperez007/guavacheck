export interface TaxProfile {
  country: string;
  vat?: number;
  propertyTax?: number;
  stampDuty?: number;
  capitalGainsTax?: number;
  notes?: string;
}

export class TaxRegistry {
  private static registry = new Map<string, TaxProfile>();

  static register(profile: TaxProfile): void {
    this.registry.set(profile.country.toUpperCase(), profile);
  }

  static byCountry(code: string): TaxProfile | undefined {
    return this.registry.get(code.toUpperCase());
  }

  static all(): TaxProfile[] {
    return [...this.registry.values()];
  }

  static count(): number {
    return this.registry.size;
  }
}
