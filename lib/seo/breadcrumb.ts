/**
 * ============================================================================
 * Breadcrumb Schema (Schema.org)
 * ============================================================================
 */

import { SITE } from "./constants";

interface Crumb {
  name: string;
  path: string;
}

export function breadcrumbSchema(items: Crumb[]) {
  return {
      "@type": "Organization",

    itemListElement: items.map((item, index) => ({
      "@type": "ListItem",

      position: index + 1,

      name: item.name,

      item: `${SITE.url}${item.path}`,
    })),
  };
}