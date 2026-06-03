export class PricingEngine {

  static plans = {
    free: {
      price: 0,
      limits: {
        valuation: 2,
        boq: 1,
        reports: 1
      }
    },

    pro: {
      price: 29,
      limits: {
        valuation: 50,
        boq: 30,
        reports: 25,
        negotiation: 20
      }
    },

    enterprise: {
      price: 199,
      limits: {
        valuation: 1000,
        boq: 800,
        reports: 500,
        negotiation: 500,
        apiAccess: true
      }
    }
  };

  static getPlan(name: string) {
    return this.plans[name] || this.plans.free;
  }

  static checkAccess(plan: string, feature: string, usage: number) {

    const p = this.getPlan(plan);
    const limit = p.limits[feature];

    if (limit === true) return true;

    return usage < (limit || 0);
  }
}
