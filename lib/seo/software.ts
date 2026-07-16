/**
 * ============================================================================
 * Software Application Schema
 * ============================================================================
 */

import { SITE } from "./constants";

export function softwareSchema() {
  return {
    "@type": "Organization",

    "@id": `${SITE.url}/#software`,

    name: SITE.name,

    applicationCategory: "BusinessApplication",

    operatingSystem: "All",

    url: SITE.url,

    author: {
      "@id": `${SITE.url}/#organization`,
    },

    description:
      "AI-powered global property intelligence platform featuring valuation engines, market intelligence, construction intelligence, investor tools and multilingual AI.",

    offers: {
      "@type": "Offer",

      price: "0",

      priceCurrency: "USD",

      availability: "https://schema.org/InStock",
    },
  };
}