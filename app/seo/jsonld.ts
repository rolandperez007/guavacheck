import { organization } from "./organization";
import { website } from "./website";

export function jsonLd() {
  return {
    "@context": "https://schema.org",

    "@graph": [
      organization,
      website,
    ],
  };
}

export function propertySchema(property: {
  name: string;
  description: string;
  image: string;
  url: string;
  price: number;
  currency: string;
  address: string;
}) {
  return {
    "@context": "https://schema.org",

    "@type": "RealEstateListing",

    name: property.name,

    description: property.description,

    image: property.image,

    url: property.url,

    offers: {
      "@type": "Offer",

      price: property.price,

      priceCurrency: property.currency,
    },

    address: {
      "@type": "PostalAddress",

      streetAddress: property.address,
    },
  };
}