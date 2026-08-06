/**
 * ============================================================================
 * Page Metadata Builder
 * ============================================================================
 */

import type { Metadata } from "next";
import { SITE } from "./constants";

interface MetadataProps {
  title: string;
  description: string;
  path: string;

  image?: string;

  robots?: Metadata["robots"];
}

export function createMetadata({
  title,
  description,
  path,
  image = SITE.image,
  robots,
}: MetadataProps): Metadata {
  const url = `${SITE.url}${path}`;

  return {
    title,

    description,

    robots,

    alternates: {
      canonical: url,
    },

    openGraph: {
      type: "website",

      url,

      title,

      description,

      siteName: SITE.name,

      locale: SITE.locale,

      images: [
        {
          url: image,

          width: 1200,

          height: 630,

          alt: title,
        },
      ],
    },

    twitter: {
      card: "summary_large_image",

      title,

      description,

      images: [image],
    },
  };
}
