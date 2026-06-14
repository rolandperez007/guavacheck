export class InflationEngine {

  static inflationRates: Record<string, number> = {
    USA: 0.03,
    UK: 0.04,
    UAE: 0.02,
    CANADA: 0.03,
    NIGERIA: 0.28,
    GLOBAL: 0.05
  };

  static adjust(cost: number, country: string, years: number = 1) {

    const rate = this.inflationRates[country?.toUpperCase()] || 0.05;

    const adjusted = cost * Math.pow(1 + rate, years);

    return {
      original: cost,
      adjusted: Math.round(adjusted),
      inflationRate: rate,
      years
    };
  }
}
