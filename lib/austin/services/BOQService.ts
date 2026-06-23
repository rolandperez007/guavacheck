export class BOQService {
  static getMaterialPrices() {
    return {};
  }

  static getLaborRates() {
    return {};
  }

  static applyLocationMultiplier(data: any) {
    return data;
  }

  static calculateTotalCost(data: any) {
    return {
      total: 0,
      breakdown: []
    };
  }
}