import "./globals.css";

import type { Metadata } from "next";

import { AuthProvider } from "@/app/context/AuthContext";

import SiteLayout from "@/components/layout/SiteLayout";
import { rootJsonLd } from "@/lib/seo/jsonld";
import { Analytics } from "@vercel/analytics/react";
import { SpeedInsights } from "@vercel/speed-insights/next";

import { defaultMetadata } from "@/lib/seo/metadata";
import JsonLd from "@/components/seo/JsonLd";

export const metadata: Metadata = defaultMetadata;

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <head>
        <JsonLd data={rootJsonLd()} />
      </head>

      <body>
        <AuthProvider>
          <SiteLayout>{children}</SiteLayout>
        </AuthProvider>

        <Analytics />
        <SpeedInsights />
      </body>
    </html>
  );
}