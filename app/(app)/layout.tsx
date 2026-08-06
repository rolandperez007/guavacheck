import "./globals.css";

import type { Metadata } from "next";

import { AuthProvider } from "@/app/context/AuthContext";

import SiteLayout from "@/components/layout/SiteLayout";
import { rootJsonLd } from "@/lib/seo/jsonld";
import { defaultMetadata } from "@/lib/seo/metadata";

import JsonLd from "@/components/seo/JsonLd";

import { Analytics } from "@vercel/analytics/react";
import { SpeedInsights } from "@vercel/speed-insights/next";

export const metadata: Metadata = defaultMetadata;

const jsonLd = rootJsonLd();

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body>
        <JsonLd data={jsonLd} />

        <AuthProvider>
          <SiteLayout>{children}</SiteLayout>
        </AuthProvider>

        <Analytics />
        <SpeedInsights />
      </body>
    </html>
  );
}
