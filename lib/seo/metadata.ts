/**
 * ============================================================================
 * Default Metadata
 * ============================================================================
 *
 * Global metadata configuration for guavacheck.
 * ============================================================================
 */

import type { Metadata } from "next";
import { SITE } from "./constants";


export const defaultMetadata: Metadata = {

  metadataBase:
    new URL(SITE.url),


  title: {

    default:
      "guavacheck | AI-Powered Global Property Intelligence Platform",

    template:
      `%s | guavacheck`,

  },


  description:
    SITE.description,


  applicationName:
    SITE.name,


  generator:
    "Next.js",


  creator:
    SITE.company,


  publisher:
    SITE.company,


  authors: [
    {
      name:
        SITE.company,

      url:
        SITE.url,
    },
  ],


  category:
    "Technology",


  keywords: [

    "guavacheck",

    "Guava Networks Limited",

    "Artificial Intelligence",

    "Global Property Intelligence",

    "AI Real Estate Platform",

    "Property Valuation",

    "Construction Intelligence",

    "Investment Analytics",

    "Property Verification",

    "Real Estate Technology",

    "PropTech",

  ],


  alternates: {

    canonical:
      SITE.url,

  },


  robots: {

    index:
      true,

    follow:
      true,

    googleBot: {

      index:
        true,

      follow:
        true,

      "max-image-preview":
        "large",

      "max-snippet":
        -1,

      "max-video-preview":
        -1,

    },

  },


  openGraph: {

    type:
      "website",

    url:
      SITE.url,

    title:
      "guavacheck | AI-Powered Global Property Intelligence Platform",

    description:
      SITE.description,

    siteName:
      SITE.name,

    locale:
      SITE.locale,

    images: [

      {

        url:
          SITE.logo,

        width:
          1200,

        height:
          630,

        alt:
          "guavacheck",

      },

    ],

  },


  twitter: {

    card:
      "summary_large_image",

    title:
      "guavacheck | AI-Powered Property Intelligence",

    description:
      SITE.description,

    images:
      [SITE.logo],

  },


  icons: {

    icon:
      SITE.favicon,

    shortcut:
      SITE.favicon,

    apple:
      SITE.appleIcon,

  },

};