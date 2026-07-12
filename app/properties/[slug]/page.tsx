import Script from "next/script";

export default async function PropertyPage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;

  const propertyName = slug
    .replace(/-/g, " ")
    .replace(/\b\w/g, (c) => c.toUpperCase());

  const propertyUrl =
    `https://www.guavacheck.com/properties/${slug}`;

  const jsonLd = {
    "@context": "https://schema.org",

    "@type": "RealEstateListing",

    name: propertyName,

    url: propertyUrl,

    description:
      "Verified property listing by GuavaCheck.",

    image: [
      "https://www.guavacheck.com/icon.png",
    ],

    provider: {
      "@type": "Organization",

      name: "GuavaCheck",

      url: "https://www.guavacheck.com",
    },
  };

  return (
    <>
      <Script
        id="property-jsonld"
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify(jsonLd),
        }}
      />

      <main className="container mx-auto py-10">

        <h1 className="text-4xl font-bold">

          {propertyName}

        </h1>

        <p className="mt-6 text-lg">

          Verified by GuavaCheck AI.

        </p>

      </main>
    </>
  );
}