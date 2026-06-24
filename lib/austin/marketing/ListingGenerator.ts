import { CommunityEngine } from "./CommunityEngine";

export class ListingGenerator {

  static generate(property: any) {

    const tags: string[] = [];

    if (property.price > 200_000_000) tags.push("luxury");

    const location = (property.location ?? "").toLowerCase();

    if (location.includes("lekki")) {
      tags.push("prime-location");
    }

    if ((property.investment?.score ?? 0) > 70) {
      tags.push("high-roi");
    }

    tags.push("real-estate", "investment", "property");

    const post = CommunityEngine.generatePost(property);

    return {
      headline: property.title ?? "Premium Property Listing",
      description: property.description ?? "A well-structured investment opportunity.",
      seoTags: tags,
      tone: "professional",
      post
    };
  }
}
