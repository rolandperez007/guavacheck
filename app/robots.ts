import { MetadataRoute } from "next";
import { SITE } from "@/lib/seo/constants";

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

    sitemap: `${SITE.url}/sitemap.xml`,
  };
}
