export class ListingGenerator {

  static generate(property: any) {

    const price = property.price || 0;
    const location = property.location || "Prime Location";
    const title = property.title || "Luxury Property";

    const isLuxury = price > 200000000;
    const isMid = price > 50000000 && price <= 200000000;

    const tone = isLuxury
      ? "premium"
      : isMid
      ? "professional"
      : "opportunity";

    const description = this.buildDescription(property, tone);

    const seoTags = this.generateTags(property);

    const headline = this.generateHeadline(property, tone);

    return {
      headline,
      description,
      seoTags,
      tone
    };
  }

  static generateHeadline(property: any, tone: string) {

    if (tone === "premium") {
      return `Exclusive Luxury Residence in ${property.location}`;
    }

    if (tone === "professional") {
      return `Modern Investment Property in ${property.location}`;
    }

    return `High-Value Opportunity in ${property.location}`;
  }

  static buildDescription(property: any, tone: string) {

    const base = `Located in ${property.location}, this property presents a strong opportunity for investors and homeowners.`;

    if (tone === "premium") {
      return base + " Designed with luxury finishes, premium architecture, and high-end lifestyle appeal. Ideal for elite buyers seeking exclusivity and long-term value appreciation.";
    }

    if (tone === "professional") {
      return base + " Offers strong rental yield potential, strategic location advantages, and stable appreciation prospects for serious investors.";
    }

    return base + " This is a high-potential asset with strong upside for buyers seeking undervalued opportunities in a growing market.";
  }

  static generateTags(property: any) {

    const tags = [];

    if (property.price > 200000000) tags.push("luxury");
    if (property.location?.toLowerCase().includes("lekki")) tags.push("prime-location");
    if (property.investment?.score > 70) tags.push("high-roi");

    tags.push("real-estate", "investment", "property");

    return tags;
  }
}

