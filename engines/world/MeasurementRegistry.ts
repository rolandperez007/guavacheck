export interface MeasurementProfile {
  country: string;
  system: "metric" | "imperial";
}

export class MeasurementRegistry {
  private static registry = new Map<string, MeasurementProfile>();

  static register(profile: MeasurementProfile): void {
    this.registry.set(profile.country.toUpperCase(), profile);
  }

  static byCountry(code: string): MeasurementProfile | undefined {
    return this.registry.get(code.toUpperCase());
  }
}
