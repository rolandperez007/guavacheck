export interface TimezoneProfile {
  country: string;
  timezone: string;
  utcOffset: string;
}

export class TimezoneRegistry {
  private static registry = new Map<string, TimezoneProfile>();

  static register(profile: TimezoneProfile): void {
    this.registry.set(profile.country.toUpperCase(), profile);
  }

  static byCountry(code: string): TimezoneProfile | undefined {
    return this.registry.get(code.toUpperCase());
  }
}