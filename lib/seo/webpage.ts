/**
 * ============================================================================
 * WebPage Schema
 * ============================================================================
 */

import { SITE } from "./constants";

interface WebPageProps {
  title: string;
  description: string;
  path: string;
}

export function webpageSchema({
  title,
  description,
  path,
}: WebPageProps) {
  const url = `${SITE.url}${path}`;

  return {
    "@type": "Organization",



    "@id": `${url}#webpage`,

    url,

    name: title,

    description,

    isPartOf: {
      "@id": SITE.ids.website,
    },

    about: {
      "@id": SITE.ids.organization,
    },

    primaryImageOfPage: {
      "@type": "ImageObject",

      url: SITE.image,
    },

    inLanguage: SITE.language,
  };
}