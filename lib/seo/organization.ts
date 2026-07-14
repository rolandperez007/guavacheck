/**
 * ============================================================================
 * Guava Networks Limited
 * Organization Schema (Schema.org JSON-LD)
 * ============================================================================
 *
 * Primary corporate identity for guavacheck.com
 * Used by Google, Bing, AI crawlers, and knowledge graphs.
 */

export const ORGANIZATION = {
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://www.guavacheck.com/#organization",

  name: "Guava Networks Limited",
  legalName: "Guava Networks Limited",

  identifier: "RC 9273437",

  url: "https://www.guavacheck.com",

  logo: {
    "@type": "ImageObject",
    url: "https://www.guavacheck.com/logo.png",
  },

  image: "https://www.guavacheck.com/logo.png",

  foundingDate: "2025",

  founder: {
    "@type": "Person",
    name: "Roland Perez",
  },

  description:
    "Guava Networks Limited is a technology company developing AI-powered software for global property intelligence, valuation, construction intelligence, investment analytics, verification, and digital real estate services. Its flagship platform is guavacheck.",

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
    "Machine Learning"
  ],

  brand: [
    {
      "@type": "Brand",
      name: "guavacheck",
      description:
        "AI-powered global property intelligence platform.",
    },
    {
      "@type": "Brand",
      name: "Guava AI",
      description:
        "Artificial intelligence technologies developed by Guava Networks Limited.",
    }
  ],

  sameAs: [
    "https://www.linkedin.com/company/guava-networks",
    "https://www.facebook.com/guavacheck"
  ]
};