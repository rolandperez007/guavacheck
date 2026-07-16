/**
 * ============================================================================
 * Default Metadata
 * ============================================================================
 *
 * Global metadata configuration for guavacheck.
 * Used as the default metadata throughout the application.
 */

import type { Metadata } from "next";
import { SITE } from "./constants";

export const defaultMetadata: Metadata = {
  metadataBase: new URL(SITE.url),

  title: {
    default: SITE.name,
    template: `%s | ${SITE.name}`,
  },

  description: SITE.description,

  applicationName: SITE.name,

  creator: SITE.company,

  publisher: SITE.company,

  authors: [
    {
      name: SITE.company,
      url: SITE.url,
    },
  ],

  category: "Technology",

  keywords: [
    "guavacheck",
    "Guava Networks Limited",
    "Artificial Intelligence",
    "Property Intelligence",
    "Property Valuation",
    "Construction Cost Estimation",
    "Investment Analytics",
    "Property Verification",
    "Real Estate Technology",
    "PropTech",
  ],

  alternates: {
    canonical: SITE.url,
  },

  robots: {
    index: true,
    follow: true,

    googleBot: {
      index: true,
      follow: true,
      "max-image-preview": "large",
      "max-snippet": -1,
      "max-video-preview": -1,
    },
  },

  openGraph: {
    type: "website",

    url: SITE.url,

    title: SITE.name,

    description: SITE.description,

    siteName: SITE.name,

    locale: "en_US",

    images: [
      {
        url: SITE.logo,
        width: 1200,
        height: 630,
        alt: SITE.name,
      },
    ],
  },

  twitter: {
    card: "summary_large_image",

    title: SITE.name,

    description: SITE.description,

    images: [SITE.logo],
  },

  icons: {
    icon: "/favicon.ico",
    shortcut: "/favicon.ico",
    apple: "/icon.png",
  },
};