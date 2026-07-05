export interface PaymentProvider {
  id: string;
  name: string;
  countries: string[];
}

export class PaymentRegistry {
  private static registry = new Map<string, PaymentProvider>();

  static register(provider: PaymentProvider) {
    this.registry.set(provider.id, provider);
  }

  static all() {
    return [...this.registry.values()];
  }

  static supportedIn(country: string) {
    return this.all().filter((p) =>
      p.countries.includes(country)
    );
  }
}