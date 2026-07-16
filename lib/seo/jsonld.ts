/**
 * ============================================================================
 * Root JSON-LD Graph
 * ============================================================================
 */

import { organizationSchema } from "./organization";
import { softwareSchema } from "./software";
import { websiteSchema } from "./website";

export function rootJsonLd() {
  return {
    "@context": "https://schema.org",

    "@graph": [
      organizationSchema(),
      websiteSchema(),
      softwareSchema(),
    ],
  };
}