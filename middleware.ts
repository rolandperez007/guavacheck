import { NextRequest, NextResponse } from "next/server";
import launchConfig from "@/lib/launch";

const protectedRoutes = [
  "/city",
  "/austin",
  "/community",
  "/marketplace",
  "/builder",
  "/construction",
  "/verification",
  "/dashboard",
  "/developer",
  "/admin",
  "/analytics",
  "/billing",
  "/commerce",
  "/engineering",
  "/scheduler",
  "/security",
  "/storage",
  "/world",
];

export function middleware(request: NextRequest) {
  const pathname = request.nextUrl.pathname;

  // Allow framework assets
  if (
    pathname.startsWith("/_next") ||
    pathname.startsWith("/api") ||
    pathname === "/favicon.ico" ||
    pathname === "/robots.txt" ||
    pathname === "/sitemap.xml" ||
    pathname.startsWith("/images")
  ) {
    return NextResponse.next();
  }

  if (launchConfig.launchMode && protectedRoutes.some((route) => pathname.startsWith(route))) {
    return NextResponse.redirect(new URL("/", request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ["/:path*"],
};
