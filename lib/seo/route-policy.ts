/**
 * Route Policy
 * Centralized rules for indexing, crawling, and route visibility.
 */

export type RoutePolicy = {
  allowIndex: boolean;
  allowFollow: boolean;
  sitemap: boolean;
  reason?: string;
};

const privateRoutes = [
  "/admin",
  "/dashboard",
  "/api",
  "/auth",
  "/login",
  "/signup",
  "/settings",
  "/billing",
  "/internal",
];

const noIndexRoutes = ["/404", "/500", "/maintenance", "/preview", "/test"];

function matchesRoute(pathname: string, routes: string[]) {
  return routes.some((route) => pathname === route || pathname.startsWith(`${route}/`));
}

/**
 * Determines SEO behavior for every application route.
 */
export function getRoutePolicy(pathname: string): RoutePolicy {
  const normalizedPath = pathname.split("?")[0];

  if (matchesRoute(normalizedPath, privateRoutes)) {
    return {
      allowIndex: false,
      allowFollow: false,
      sitemap: false,
      reason: "Private application route",
    };
  }

  if (matchesRoute(normalizedPath, noIndexRoutes)) {
    return {
      allowIndex: false,
      allowFollow: true,
      sitemap: false,
      reason: "Temporary or system route",
    };
  }

  return {
    allowIndex: true,
    allowFollow: true,
    sitemap: true,
    reason: "Public route",
  };
}

/**
 * Generates robots meta directives.
 */
export function getRobotsDirective(pathname: string): string {
  const policy = getRoutePolicy(pathname);

  if (!policy.allowIndex && !policy.allowFollow) {
    return "noindex, nofollow";
  }

  if (!policy.allowIndex) {
    return "noindex, follow";
  }

  return "index, follow";
}

/**
 * Check whether a route should appear in sitemap.
 */
export function shouldIncludeInSitemap(pathname: string): boolean {
  return getRoutePolicy(pathname).sitemap;
}
