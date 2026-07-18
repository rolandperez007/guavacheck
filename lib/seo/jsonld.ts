/**
 * ============================================================================
 * Root JSON-LD Graph
 * ============================================================================
 *
 * Central structured data graph for guavacheck.
 *
 * Connects:
 * - Organization
 * - Website
 * - Software Platform
 *
 * Additional page-level schemas should be added separately.
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