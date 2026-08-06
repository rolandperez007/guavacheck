import { SITE } from "@/lib/seo/constants";

export function organizationSchema() {
  return {
    "@context": "https://schema.org",
    "@type": "Organization",
    "@id": SITE.ids.organization,
    name: SITE.company,
    url: SITE.url,
    logo: SITE.logo,
    foundingDate: SITE.foundingYear,
    founder: {
      "@type": "Person",
      name: SITE.founder,
    },
    description: SITE.description,
    sameAs: [SITE.social.linkedin, SITE.social.github, SITE.social.facebook],
  };
}

export function softwareSchema() {
  return {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": SITE.ids.software,
    name: SITE.brand,
    applicationCategory: "Real Estate Software",
    operatingSystem: "Web",
    url: SITE.url,
    description: SITE.description,
  };
}
