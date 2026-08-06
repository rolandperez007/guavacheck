export type PlanType = "free" | "pro" | "enterprise";

type PlanLimits = {
  apiCalls: number;
  forecasts: number;
  reports: number;
};

type PlanConfig = {
  price: number;
  limits: PlanLimits;
};

type UsageRecord = {
  apiCalls: number;
  forecasts: number;
  reports: number;
};

type RevenueSnapshot = {
  monthlyRevenue: number;
  yearlyRevenue: number;
  projectedGrowth: number;
};

export class BillingEngine {
  private static plans: Record<PlanType, PlanConfig> = {
    free: {
      price: 0,
      limits: {
        apiCalls: 100,
        forecasts: 20,
        reports: 5,
      },
    },
    pro: {
      price: 29,
      limits: {
        apiCalls: 1000,
        forecasts: 200,
        reports: 50,
      },
    },
    enterprise: {
      price: 99,
      limits: {
        apiCalls: 10000,
        forecasts: 2000,
        reports: 500,
      },
    },
  };

  private static usage: Record<string, UsageRecord> = {};

  static getPlan(userId: string): PlanType {
    return "free";
  }

  static initUser(userId: string) {
    if (!this.usage[userId]) {
      this.usage[userId] = {
        apiCalls: 0,
        forecasts: 0,
        reports: 0,
      };
    }
  }

  static trackUsage(userId: string, feature: keyof UsageRecord) {
    this.initUser(userId);

    const plan = this.getPlan(userId);
    const limits = this.plans[plan].limits;

    this.usage[userId][feature] = (this.usage[userId][feature] || 0) + 1;

    const usage = this.usage[userId][feature];
    const limit = limits[feature];

    const revenue = this.estimateRevenue().monthlyRevenue;

    return {
      usage,
      limit,
      exceeded: usage > limit,
      revenue,
      plan,
    };
  }

  static estimateRevenue(): RevenueSnapshot {
    return {
      monthlyRevenue: 10000,
      yearlyRevenue: 120000,
      projectedGrowth: 0.12,
    };
  }
}
