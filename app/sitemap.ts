import { MetadataRoute } from "next";
import { SITE } from "@/lib/seo/constants";


export default function sitemap(): MetadataRoute.Sitemap {

  const now = new Date();

  return [

    {
      url: SITE.url,
      lastModified: now,
      changeFrequency: "daily",
      priority: 1,
    },


    {
      url: `${SITE.url}/about`,
      lastModified: now,
      changeFrequency: "monthly",
      priority: 0.8,
    },


    {
      url: `${SITE.url}/services`,
      lastModified: now,
      changeFrequency: "monthly",
      priority: 0.9,
    },


    {
      url: `${SITE.url}/property-finder`,
      lastModified: now,
      changeFrequency: "daily",
      priority: 0.95,
    },


    {
      url: `${SITE.url}/valuation`,
      lastModified: now,
      changeFrequency: "weekly",
      priority: 0.9,
    },


    {
      url: `${SITE.url}/construction`,
      lastModified: now,
      changeFrequency: "weekly",
      priority: 0.9,
    },


    {
      url: `${SITE.url}/investors`,
      lastModified: now,
      changeFrequency: "monthly",
      priority: 0.85,
    },


    {
      url: `${SITE.url}/community`,
      lastModified: now,
      changeFrequency: "daily",
      priority: 0.85,
    },


    {
      url: `${SITE.url}/blog`,
      lastModified: now,
      changeFrequency: "daily",
      priority: 0.8,
    },


    {
      url: `${SITE.url}/contact`,
      lastModified: now,
      changeFrequency: "monthly",
      priority: 0.6,
    },

  ];
}