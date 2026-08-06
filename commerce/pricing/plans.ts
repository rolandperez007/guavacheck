import { Plan } from "./pricing-types";

export const Plans: Plan[] = [
  {
    id: "free",
    name: "Free",
    basePriceUSD: 0,
    billingCycle: "monthly",
    active: true,
    features: ["Limited AI", "Community Access"],
  },

  {
    id: "starter",
    name: "Starter",
    basePriceUSD: 19,
    billingCycle: "monthly",
    active: true,
    features: ["Austin AI", "Basic Reports", "Property Wizard"],
  },

  {
    id: "professional",
    name: "Professional",
    basePriceUSD: 77,
    billingCycle: "monthly",
    active: true,
    features: [
      "Everything in Starter",
      "Building Passport",
      "Unlimited AI",
      "Investor Reports",
      "Priority Support",
    ],
  },

  {
    id: "business",
    name: "Business",
    basePriceUSD: 197,
    billingCycle: "monthly",
    active: true,
    features: ["Team Accounts", "API Access", "Advanced Analytics"],
  },

  {
    id: "enterprise",
    name: "Enterprise",
    basePriceUSD: 0,
    billingCycle: "monthly",
    active: true,
    features: ["Custom Pricing", "Dedicated Support", "Private Deployment"],
  },
];
