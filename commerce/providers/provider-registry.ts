/**
 * ===========================================================
 * GUAVA COMMERCE ENGINE
 * Provider Registry
 *
 * Guava Networks Inc.
 * ===========================================================
 */

import { PaymentProvider } from "./provider-types";

export const ProviderRegistry: PaymentProvider[] = [
  {
    id: "stripe",

    name: "Stripe",

    supportedCountries: [
      "US",
      "CA",
      "GB",
      "AU",
      "NZ",
      "JP",
      "KR",

      "SG",
      "DE",
      "FR",
      "IT",
      "ES",
      "NL",

      "BR",
      "MX",
    ],

    supportedCurrencies: ["USD", "EUR", "GBP", "JPY", "KRW", "AUD", "CAD", "BRL"],

    supportsSubscriptions: true,

    supportsRefunds: true,

    supportsWebhooks: true,

    enabled: true,
  },

  {
    id: "paystack",

    name: "Paystack",

    supportedCountries: ["NG", "GH"],

    supportedCurrencies: ["NGN", "GHS"],

    supportsSubscriptions: true,

    supportsRefunds: true,

    supportsWebhooks: true,

    enabled: true,
  },

  {
    id: "flutterwave",

    name: "Flutterwave",

    supportedCountries: ["NG", "KE", "UG", "TZ", "RW", "ZM", "ZW", "ZA"],

    supportedCurrencies: ["NGN", "KES", "UGX", "TZS", "RWF", "ZMW", "ZAR"],

    supportsSubscriptions: true,

    supportsRefunds: true,

    supportsWebhooks: true,

    enabled: true,
  },

  {
    id: "paypal",

    name: "PayPal",

    supportedCountries: ["*"],

    supportedCurrencies: ["*"],

    supportsSubscriptions: true,

    supportsRefunds: true,

    supportsWebhooks: true,

    enabled: true,
  },
];
