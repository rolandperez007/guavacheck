"use client";

import React from "react";

interface ProvidersProps {
  children: React.ReactNode;
}

export default function Providers({
  children,
}: ProvidersProps) {
  /**
   * Global Application Providers
   *
   * This component becomes the single place where
   * global providers are composed.
   *
   * Future providers include:
   *
   * • ThemeProvider
   * • SessionProvider
   * • LocalizationProvider
   * • FeatureFlagProvider
   * • ToastProvider
   * • ErrorBoundary
   *
   * Austin Kernel is NOT initialized here.
   * This component only prepares the application environment.
   */

  return <>{children}</>;
}