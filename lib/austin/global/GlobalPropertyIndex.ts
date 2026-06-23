export class GlobalPropertyIndex {

  static currencyMap: Record<string, number> = {
    USD: 1,
    EUR: 1.1,
    GBP: 1.3,
    NGN: 0.0008,
    AED: 0.27,
    CAD: 0.75
  };

  static regionMultiplier: Record<string, number> = {
    "north_america": 1.0,
    "europe": 1.05,
    "middle_east": 0.95,
    "africa": 0.65,
    "asia": 0.9,
    "south_america": 0.8
  };

  static normalize(property: any) {

    const price = property.price || 0;
    const currency = property.currency || "USD";
    const region = property.region || "north_america";

    const usdValue = price * (this.currencyMap[currency] || 1);

    const adjustedValue = usdValue * (this.regionMultiplier[region] || 1);

    return {
      originalPrice: price,
      currency,
      region,

      usdValue: Math.round(usdValue),
      normalizedValue: Math.round(adjustedValue),

      globalIndexScore: this.calculateIndex(adjustedValue)
    };
  }

  static calculateIndex(value: number) {

    // universal scoring baseline (0 - 100)
    const score = Math.min(100, Math.max(0,
      (value / 500000) * 100
    ));

    return Math.round(score);
  }

  static compare(propertyA: any, propertyB: any) {

    const a = this.normalize(propertyA).normalizedValue;
    const b = this.normalize(propertyB).normalizedValue;

    return {
      difference: Math.abs(a - b),
      betterValue: a < b ? "PROPERTY_A" : "PROPERTY_B"
    };
  }
}

