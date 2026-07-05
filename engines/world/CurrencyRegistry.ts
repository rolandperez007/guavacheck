export interface CurrencyInfo {
  code: string;
  symbol: string;
  name: string;
}

export class CurrencyRegistry {
  private static registry = new Map<string, CurrencyInfo>();

  static register(currency: CurrencyInfo) {
    this.registry.set(currency.code, currency);
  }

  static byCode(code: string) {
    return this.registry.get(code);
  }

  static all() {
    return [...this.registry.values()];
  }
}