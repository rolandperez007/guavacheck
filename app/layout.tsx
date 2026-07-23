import "./globals.css";
import type { Metadata } from "next";
import Script from "next/script";
import { SITE } from "@/lib/seo/constants";
import {
  organizationSchema,
  softwareSchema,
} from "@/app/seo/schema";

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

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang={SITE.language}>
      <body>
        {/* Google Analytics */}
        <Script
          src="https://www.googletagmanager.com/gtag/js?id=G-D1XB03RNNW"
          strategy="afterInteractive"
        />

        <Script id="google-analytics" strategy="afterInteractive">
          {`
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());

            gtag('config', 'G-D1XB03RNNW');
          `}
        </Script>

        {/* Structured Data */}
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify([
              organizationSchema(),
              softwareSchema(),
            ]),
          }}
        />

        {children}
      </body>
    </html>
  );
} 