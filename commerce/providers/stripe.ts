/**
 * Stripe Adapter
 *
 * Guava Networks Inc.
 */

export class StripeProvider {
  async createCheckoutSession(data: unknown) {
    console.log("Stripe checkout");

    return {
      success: true,

      provider: "stripe",

      session: null,

      data,
    };
  }
}

export const stripeProvider = new StripeProvider();
