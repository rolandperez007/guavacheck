/**
 * ============================================================================
 * Website Schema
 * ============================================================================
 */

import { SITE } from "./constants";

export function websiteSchema() {
  return {
    "@type": "WebSite",

    "@id": `${SITE.url}/#website`,

    url: SITE.url,

    name: SITE.name,

    description: SITE.description,

    inLanguage: SITE.language,

    publisher: {
      "@id": `${SITE.url}/#organization`,
    },

    potentialAction: {
      "@type": "SearchAction",

      target: `${SITE.url}/search?q={search_term_string}`,

      "query-input": "required name=search_term_string",
    },
  };
}