/**
 * ============================================================================
 * Guava Networks Limited
 * Organization Schema
 * ============================================================================
 */

import { SITE } from "./constants";

export function organizationSchema() {
  return {
    "@type": "Organization",

    "@id": `${SITE.url}/#organization`,

    name: SITE.company,

    legalName: SITE.company,

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
      "Guava Networks Limited is a technology company building AI-powered property intelligence software. Its flagship platform, guavacheck, provides property intelligence, valuation tools, construction insights, investment analytics and verification services.",

    slogan: "Where premium properties meet the right owners",

    email: "info@guavacheck.com",

    areaServed: {
      "@type": "Place",
      name: "Worldwide",
    },

    knowsLanguage: ["English", "French", "Spanish", "Portuguese", "Arabic", "German", "Chinese"],

    knowsAbout: [
      "Artificial Intelligence",
      "Property Intelligence",
      "Real Estate Technology",
      "Property Valuation",
      "Construction Intelligence",
      "Investment Analytics",
      "Geospatial Intelligence",
      "PropTech",
      "Machine Learning",
    ],

    brand: {
      "@type": "Brand",

      "@id": `${SITE.url}/#guavacheck`,

      name: "guavacheck",

      url: SITE.url,

      description: "AI-powered global property intelligence platform.",
    },

    sameAs: [SITE.social.linkedin, SITE.social.facebook, SITE.social.github],
  };
}
