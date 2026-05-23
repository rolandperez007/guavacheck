import { Analytics } from '@vercel/analytics/next';

export const metadata = {
  title: "GuavaCheck",
  description: "AI Real Estate Platform",
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        {children}
        <Analytics />
      </body>
    </html>
  )
}
