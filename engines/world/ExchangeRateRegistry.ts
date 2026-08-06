export interface ExchangeRateProfile {
  base: string;
  target: string;
  rate: number;
  updatedAt: string;
}

export class ExchangeRateRegistry {
  private static registry = new Map<string, ExchangeRateProfile>();

  static register(profile: ExchangeRateProfile): void {
    this.registry.set(`${profile.base}_${profile.target}`, profile);
  }

  static get(base: string, target: string) {
    return this.registry.get(`${base.toUpperCase()}_${target.toUpperCase()}`);
  }

  static all(): ExchangeRateProfile[] {
    return [...this.registry.values()];
  }
}
