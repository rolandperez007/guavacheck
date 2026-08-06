export interface RegionProfile {
  continent: string;
  region: string;
  countries: string[];
}

export class RegionRegistry {
  private static registry = new Map<string, RegionProfile>();

  static register(profile: RegionProfile): void {
    this.registry.set(profile.region, profile);
  }

  static byRegion(region: string): RegionProfile | undefined {
    return this.registry.get(region);
  }

  static all(): RegionProfile[] {
    return [...this.registry.values()];
  }
}
