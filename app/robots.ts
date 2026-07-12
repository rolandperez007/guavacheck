import { MetadataRoute } from "next";

export default function robots(): MetadataRoute.Robots {
  return {
    rules: [
      {
        userAgent: "*",
        allow: ["/"],
        disallow: [
          "/app",
          "/login",
          "/dashboard",
          "/api",
          "/admin",
          "/memory",
          "/middleware",
          "/models",
          "/orchestrator",
        ],
      },
    ],
    sitemap: "https://www.guavacheck.com/sitemap.xml",
  };
}