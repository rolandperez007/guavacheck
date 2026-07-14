import type { Metadata } from "next";

export const defaultMetadata: Metadata = {

  metadataBase: new URL("https://www.guavacheck.com"),

  title: {

    default: "GuavaCheck",

    template: "%s | GuavaCheck",

  },

  description:
    "Global AI platform for property intelligence, valuation, construction, verification and investment.",

  keywords: [

    "AI",

    "Artificial Intelligence",

    "Property Intelligence",

    "Real Estate",

    "Valuation",

    "Construction",

    "Investment",

    "Verification",

    "Guava AI",

    "GuavaCheck"

  ],

  applicationName: "GuavaCheck",

  creator: "Guava Networks Limited",

  publisher: "Guava Networks Limited",

  category: "Artificial Intelligence",

  robots: {

    index: true,

    follow: true,

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