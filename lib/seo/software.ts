/**
 * ============================================================================
 * guavacheck Software Schema
 * ============================================================================
 */

import { SITE } from "./constants";

export function softwareSchema() {
  return {
    "@type": "SoftwareApplication",

    "@id": `${SITE.url}/#software`,

    name: "guavacheck",

    applicationCategory: "BusinessApplication",

    operatingSystem: "Web",

    url: SITE.url,

    creator: {
      "@id": `${SITE.url}/#organization`,
    },

    description:
      "guavacheck is an AI-powered global property intelligence platform providing property valuation, construction intelligence, market analytics, verification tools and multilingual property search.",

    offers: {
      "@type": "Offer",

      price: "0",

      priceCurrency: "USD",

      availability: "https://schema.org/InStock",
    },
  };
}
