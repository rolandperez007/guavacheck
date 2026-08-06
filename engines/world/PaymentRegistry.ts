export interface PaymentProvider {
  id: string;
  name: string;
  countries: string[];
}

export class PaymentRegistry {
  private static registry = new Map<string, PaymentProvider>();

  static initialize(): void {
    // Payment providers will be registered here
    // Example:
    // this.register({
    //   id: "paystack",
    //   name: "Paystack",
    //   countries: ["NG", "GH", "ZA"]
    // });
  }

  static register(provider: PaymentProvider): void {
    this.registry.set(provider.id, provider);
  }

  static all(): PaymentProvider[] {
    return [...this.registry.values()];
  }

  static supportedIn(country: string): PaymentProvider[] {
    return this.all().filter((provider) => provider.countries.includes(country));
  }

  static count(): number {
    return this.registry.size;
  }

  static clear(): void {
    this.registry.clear();
  }
}
