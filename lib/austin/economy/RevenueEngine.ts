export class RevenueEngine {
  static calculateRevenue() {
    return 0;
  }

  static charge(apiKey: string, plan: string) {
    return {
      success: true,
      charged: 0,
      plan,
    };
  }
}
