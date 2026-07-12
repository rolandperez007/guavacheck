import type { Metadata } from "next";

export const defaultMetadata: Metadata = {
  metadataBase: new URL("https://www.guavacheck.com"),

  title: {
    default: "GuavaCheck | Global AI Property Intelligence Platform",
    template: "%s | GuavaCheck",
  },

  description:
    "GuavaCheck is an AI-powered global property intelligence platform providing property verification, engineering intelligence, construction cost estimation, valuation, multilingual support and multi-currency services.",

  keywords: [
    "GuavaCheck",
    "Property Verification",
    "Real Estate",
    "AI",
    "Engineering",
    "Construction",
    "Property Valuation",
    "Building Cost Estimator",
    "Mortgage Calculator",
    "Property Intelligence",
    "Fraud Detection",
    "Investment Analysis",
    "Global Real Estate",
    "Property Search",
  ],

  applicationName: "GuavaCheck",

  category: "Technology",

  robots: {
    index: true,
    follow: true,
    nocache: false,
    googleBot: {
      index: true,
      follow: true,
      "max-image-preview": "large",
      "max-snippet": -1,
      "max-video-preview": -1,
    },
  },

  alternates: {
    canonical: "https://www.guavacheck.com",
  },
};