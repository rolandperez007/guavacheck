export class DataNormalizer {

  static normalize(raw: any) {

    return {
      id: raw.id || Math.random().toString(36).substring(2),
      title: raw.title || raw.name || "Untitled Property",
      location: raw.location || raw.city || "Unknown",
      price: Number(raw.price || 0),
      sqm: raw.sqm || raw.size || 0,
      bedrooms: raw.bedrooms || 0,
      bathrooms: raw.bathrooms || 0,
      type: raw.type || "residential",
      source: raw.source || "external_feed",
      timestamp: new Date(),

      geo: this.resolveGeo(raw.location),

      metadata: {
        raw: raw
      }
    };
  }

  static resolveGeo(location: string) {

    const map: Record<string, any> = {
      "London": { lat: 51.5072, lng: -0.1276 },
      "Dubai": { lat: 25.2048, lng: 55.2708 },
      "New York": { lat: 40.7128, lng: -74.0060 },
      "Lagos": { lat: 6.5244, lng: 3.3792 }
    };

    return map[location] || { lat: 0, lng: 0 };
  }
}
