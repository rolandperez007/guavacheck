
import "./globals.css";
import { AuthProvider } from "@/app/context/AuthContext";
import { Analytics } from "@vercel/analytics/react";
import { SpeedInsights } from "@vercel/speed-insights/next";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <AuthProvider>{children}</AuthProvider>

         <Analytics />    
        <SpeedInsights /> 
      </body>
    </html>
  );
}









