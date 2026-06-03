export class GlobalFinanceEngine {

  static defaultCurrency = "USD";

  static exchangeRates: Record<string, number> = {
    USD: 1,
    EUR: 0.92,
    GBP: 0.78,
    NGN: 1500,
    AED: 3.67
  };

  static format(amount: number, currency: string = "USD") {
    return new Intl.NumberFormat(undefined, {
      style: "currency",
      currency
    }).format(amount);
  }

  static convert(amount: number, from: string, to: string) {
    const baseUSD = amount / (this.exchangeRates[from] || 1);
    return baseUSD * (this.exchangeRates[to] || 1);
  }

  static normalizeToUSD(amount: number, currency: string) {
    return amount / (this.exchangeRates[currency] || 1);
  }

  static applyRegionMultiplier(amount: number, region?: string) {

    const multipliers: Record<string, number> = {
      global: 1,
      africa: 0.75,
      europe: 1.1,
      usa: 1.3,
      middleeast: 1.15
    };

    return amount * (multipliers[region || "global"] || 1);
  }

  static detectCurrencyFromLocale(locale?: string) {

    if (!locale) return "USD";

    if (locale.includes("ng")) return "NGN";
    if (locale.includes("gb")) return "GBP";
    if (locale.includes("de")) return "EUR";
    if (locale.includes("ae")) return "AED";

    return "USD";
  }
}
