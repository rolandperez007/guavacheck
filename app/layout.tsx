/**
 * Root Application Shell
 *
 * This file prepares the runtime environment
 * for every guavacheck experience.
 *
 * Responsibilities:
 *
 * - Global Metadata
 * - Global Providers
 * - Analytics
 * - Structured Data
 * - Austin Runtime Bootstrap
 *
 * Austin Cognitive Kernel is intentionally
 * independent of this layer.
 */

import "./globals.css";

import type { Metadata } from "next";

import { SITE } from "@/lib/seo/constants";

import Providers from "@/components/app/providers/Providers";
import Analytics from "@/components/app/analytics/Analytics";
import StructuredData from "@/components/app/seo/StructuredData";
import AustinBootstrap from "@/components/app/bootstrap/AustinBootstrap";

export const metadata: Metadata = {
  metadataBase: new URL(SITE.url),

  title: {
    default: `${SITE.name} | Global Property Intelligence Platform`,
    template: `%s | ${SITE.name}`,
  },

  description: SITE.description,

  applicationName: SITE.name,

  keywords: [
    "property intelligence",
    "real estate AI",
    "property verification",
    "property valuation",
    "construction intelligence",
    "real estate analytics",
    "investment analytics",
  ],

  authors: [
    {
      name: SITE.company,
    },
  ],

  creator: SITE.company,

  robots: {
    index: true,
    follow: true,
  },

  alternates: {
    canonical: SITE.url,
  },

  openGraph: {
    type: "website",
    url: SITE.url,
    title: `${SITE.name} | Global Property Intelligence Platform`,
    description: SITE.description,
    siteName: SITE.name,
    locale: SITE.locale,
    images: [
      {
        url: SITE.image,
        width: 1200,
        height: 630,
        alt: SITE.name,
      },
    ],
  },

  twitter: {
    card: "summary_large_image",
    title: `${SITE.name} | Global Property Intelligence Platform`,
    description: SITE.description,
    images: [SITE.image],
  },

  icons: {
    icon: SITE.favicon,
    apple: SITE.appleIcon,
  },

  manifest: SITE.manifest,
};

interface RootLayoutProps {
  children: React.ReactNode;
}

export default function RootLayout({
  children,
}: RootLayoutProps) {
  return (
    <html lang={SITE.language} suppressHydrationWarning>
      <body>
        <Providers>

          <Analytics />

          <StructuredData />

          <AustinBootstrap>

            {children}

          </AustinBootstrap>

        </Providers>
      </body>
    </html>
  );
}
