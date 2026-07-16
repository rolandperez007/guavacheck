/**
 * ============================================================================
 * Guava Networks Limited
 * Organization Schema (Schema.org JSON-LD)
 * ============================================================================
 *
 * Primary corporate identity for guavacheck.com
 * Used by Google, Bing, AI crawlers and Knowledge Graphs.
 */

import { SITE } from "./constants";

export function organizationSchema() {
  return {
    "@type": "Organization",

    "@id": `${SITE.url}/#organization`,

    name: SITE.company,

    legalName: SITE.company,

    identifier: SITE.identifier,

    url: SITE.url,

    logo: {
      "@type": "ImageObject",
      url: SITE.logo,
    },

    image: SITE.logo,

    foundingDate: SITE.foundingYear,

    founder: {
      "@type": "Person",
      name: SITE.founder,
    },

    description:
       "Guava Networks Limited is a technology company specializing in artificial intelligence and global property intelligence software. Its flagship platform, guavacheck, delivers AI-powered property valuation, construction intelligence, investment analytics, verification, multilingual search and market intelligence for users worldwide.",

    slogan: "Where premium properties meet the right owners",

    email: "info@guavacheck.com",

    telephone: "+1 432 276 1388",

    areaServed: {
      "@type": "Place",
      name: "Worldwide",
    },

    knowsLanguage: [
      "English",
      "French",
      "Spanish",
      "Portuguese",
      "Arabic",
      "German",
      "Chinese",
    ],

    knowsAbout: [
      "Artificial Intelligence",
      "Property Intelligence",
      "Real Estate Technology",
      "Property Valuation",
      "Construction Cost Estimation",
      "Investment Analytics",
      "Property Verification",
      "Geospatial Intelligence",
      "Digital Real Estate",
      "PropTech",
      "Machine Learning",
    ],

    brand: [
      {
        "@type": "Brand",

        "@id": `${SITE.url}/#guavacheck`,

        name: "guavacheck",

        description:
          "AI-powered global property intelligence platform.",
      },
      {
        "@type": "Brand",

        "@id": `${SITE.url}/#guava-ai`,

        name: "Guava AI",

        description:
          "Artificial intelligence technologies developed by Guava Networks Limited.",
      },
    ],

    sameAs: [
      SITE.social.linkedin,
      SITE.social.facebook,
      SITE.social.github,
    ],
  };
}