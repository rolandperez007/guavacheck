import "./globals.css";

import type { Metadata } from "next";

import { AuthProvider } from "@/app/context/AuthContext";

import { Analytics } from "@vercel/analytics/react";

import { SpeedInsights } from "@vercel/speed-insights/next";

import { defaultMetadata } from "./seo/metadata";

import { jsonLd } from "./seo/jsonld";

export const metadata: Metadata = defaultMetadata;

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {

  return (

    <html lang="en">

      <body>

        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify(jsonLd()),
          }}
        />

        <AuthProvider>

          {children}

        </AuthProvider>

        <Analytics />

        <SpeedInsights />

      </body>

    </html>

  );

}









