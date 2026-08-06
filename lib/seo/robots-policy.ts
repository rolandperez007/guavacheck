/**
 * ==========================================================
 * Robots Policy
 * ==========================================================
 */

import { PRIVATE_ROUTE_PREFIXES } from "@/app/seo/route-policy";

export const ROBOTS_POLICY = {
  userAgent: "*",

  allow: ["/"],

  disallow: PRIVATE_ROUTE_PREFIXES,
};

export default ROBOTS_POLICY;
