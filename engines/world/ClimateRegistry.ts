export interface ClimateProfile {
  country: string;
  zone: string;
  rainfall: string;
  temperature: string;
  floodRisk?: string;
  earthquakeRisk?: string;
}

export class ClimateRegistry {
  private static registry = new Map<string, ClimateProfile>();

  static register(profile: ClimateProfile): void {
    this.registry.set(profile.country.toUpperCase(), profile);
  }

  static byCountry(code: string): ClimateProfile | undefined {
    return this.registry.get(code.toUpperCase());
  }

  static all(): ClimateProfile[] {
    return [...this.registry.values()];
  }
}