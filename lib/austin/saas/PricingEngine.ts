type PlanType = "free" | "pro" | "enterprise";

type Plan = {
  price: number;
  limits: Record<string, number | boolean>;
};

export class PricingEngine {
  private static plans: Record<PlanType, Plan> = {
    free: {
      price: 0,
      limits: {
        valuation: 5,
        boq: 2,
        reports: 3,
      },
    },

    pro: {
      price: 29,
      limits: {
        valuation: 50,
        boq: 20,
        reports: 30,
        negotiation: 10,
      },
    },

    enterprise: {
      price: 99,
      limits: {
        valuation: true,
        boq: true,
        reports: true,
        negotiation: true,
      },
    },
  };

  static getPlan(name: PlanType) {
    return this.plans[name];
  }

  static checkAccess(plan: PlanType, feature: string, usage: number) {
    const p = this.getPlan(plan);

    const limit = p.limits[feature];

    if (limit === true) return true;

    return usage < (typeof limit === "number" ? limit : 0);
  }
}
