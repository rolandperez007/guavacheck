/**
 * Asia Provider Placeholder
 *
 * Reserved for future regional gateway.
 *
 * Examples:
 *
 * - Airwallex
 * - Xendit
 * - HitPay
 * - Omise
 * - Razorpay
 */

export class AsiaProvider {
  async initialize(data: unknown) {
    return {
      success: false,

      provider: "asia",

      message: "Asia provider not yet configured.",

      data,
    };
  }
}

export const asiaProvider = new AsiaProvider();
