import { PUBLIC_ROUTES } from "@/app/seo/route-policy";

export const SITEMAP_ROUTES = PUBLIC_ROUTES.map((route) => ({
  route,

  priority: route === "/" ? 1.0 : 0.9,

  changeFrequency: "weekly",
}));
