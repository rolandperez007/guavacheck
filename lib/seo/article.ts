/**
 * ============================================================================
 * Article Schema (Schema.org)
 * ============================================================================
 */

import { SITE } from "./constants";

interface ArticleOptions {
  headline: string;
  description: string;
  path: string;
  published: string;
  modified: string;
}

export function articleSchema({
  headline,
  description,
  path,
  published,
  modified,
}: ArticleOptions) {
  return {
    "@type": "Organization",

    "@id": `${SITE.url}${path}#article`,

    headline,

    description,

    datePublished: published,

    dateModified: modified,

    mainEntityOfPage: {
      "@id": `${SITE.url}${path}#webpage`,
    },

    author: {
      "@id": `${SITE.url}/#organization`,
    },

    publisher: {
      "@id": `${SITE.url}/#organization`,
    },

    image: SITE.logo,
  };
}
