export class BillingEngine {

  static plans = {
    free: {
      price: 0,
      limits: {
        apiCalls: 10,
        forecasts: 5,
        reports: 2
      }
    },

    pro: {
      price: 29,
      limits: {
        apiCalls: 1000,
        forecasts: 500,
        reports: 200
      }
    },

    enterprise: {
      price: 199,
      limits: {
        apiCalls: 10000,
        forecasts: 5000,
        reports: 2000,
        whiteLabel: true
      }
    }
  };

  static usage: Record<string, any> = {};

  static getPlan(userId: string) {
    return this.usage[userId]?.plan || "free";
  }

  static setPlan(userId: string, plan: keyof typeof BillingEngine.plans) {

    if (!this.plans[plan]) {
      return { error: "invalid_plan" };
    }

    this.usage[userId] = {
      ...(this.usage[userId] || {}),
      plan,
      updatedAt: new Date()
    };

    return {
      success: true,
      plan
    };
  }

  static trackUsage(userId: string, feature: string) {

    if (!this.usage[userId]) {
      this.usage[userId] = { plan: "free", usage: {} };
    }

    const plan = this.getPlan(userId);
    const limits = this.plans[plan].limits;

    this.usage[userId].usage[feature] =
      (this.usage[userId].usage[feature] || 0) + 1;

    const used = this.usage[userId].usage[feature];
    const limit = (limits as any)[feature];

    return {
      feature,
      used,
      limit,
      allowed: used <= limit
    };
  }

  static getUsage(userId: string) {
    return this.usage[userId] || { plan: "free", usage: {} };
  }

  static estimateRevenue() {

    let revenue = 0;

    for (const user of Object.values(this.usage)) {
      const plan = (user as any).plan;

      if (plan === "pro") revenue += 29;
      if (plan === "enterprise") revenue += 199;
    }

    return {
      monthlyRevenue: revenue,
      activeUsers: Object.keys(this.usage).length
    };
  }
}

