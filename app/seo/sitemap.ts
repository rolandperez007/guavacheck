import type { MetadataRoute } from "next";

export default function sitemap(): MetadataRoute.Sitemap {
  const now = new Date();

  return [
    {
      url: "https://www.guavacheck.com",

      lastModified: now,

      changeFrequency: "daily",

      priority: 1,
    },

    {
      url: "https://www.guavacheck.com/about",

      lastModified: now,

      changeFrequency: "monthly",

      priority: 0.9,
    },

    {
      url: "https://www.guavacheck.com/properties",

      lastModified: now,

      changeFrequency: "hourly",

      priority: 0.95,
    },

    {
      url: "https://www.guavacheck.com/services",

      lastModified: now,

      changeFrequency: "monthly",

      priority: 0.9,
    },

    {
      url: "https://www.guavacheck.com/blog",

      lastModified: now,

      changeFrequency: "daily",

      priority: 0.9,
    },

    {
      url: "https://www.guavacheck.com/contact",

      lastModified: now,

      changeFrequency: "monthly",

      priority: 0.8,
    },

    {
      url: "https://www.guavacheck.com/pricing",

      lastModified: now,

      changeFrequency: "monthly",

      priority: 0.8,
    },
  ];
}
