import type { Metadata } from "next";

export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug: string }>;
}): Promise<Metadata> {
  const { slug } = await params;

  const title = slug.replace(/-/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());

  return {
    title: `${title} | GuavaCheck`,
    description: "Verified property listing powered by GuavaCheck AI.",

    alternates: {
      canonical: `https://www.guavacheck.com/properties/${slug}`,
    },

    openGraph: {
      title,
      description: "Verified global property listing.",

      url: `https://www.guavacheck.com/properties/${slug}`,

      siteName: "GuavaCheck",

      locale: "en_US",

      type: "website",
    },

    twitter: {
      card: "summary_large_image",
      title,
      description: "Verified property listing.",
    },
  };
}

export default function PropertyLayout({ children }: { children: React.ReactNode }) {
  return children;
}
