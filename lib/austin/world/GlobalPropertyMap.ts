export class GlobalPropertyMap {

  static feed: any[] = [];

  static ingest(property: any) {

    const enriched = {
      ...property,
      coordinates: this.resolveCoordinates(property.location),
      trendScore: this.calculateTrend(property),
      heatZone: this.assignHeatZone(property.price)
    };

    this.feed.push(enriched);

    return enriched;
  }

  static resolveCoordinates(location: string) {

    const map: Record<string, any> = {
      "Lagos": { lat: 6.5244, lng: 3.3792 },
      "Dubai": { lat: 25.2048, lng: 55.2708 },
      "London": { lat: 51.5072, lng: -0.1276 },
      "New York": { lat: 40.7128, lng: -74.0060 }
    };

    return map[location] || { lat: 0, lng: 0 };
  }

  static calculateTrend(property: any) {

    const base = property.price || 0;
    const roi = property.investment?.score || 50;

    return Math.round((roi * 0.6) + (base / 1000000));
  }

  static assignHeatZone(price: number) {

    if (price > 500000000) return "HOT";
    if (price > 100000000) return "WARM";
    return "COLD";
  }

  static getFeed() {
    return this.feed;
  }
}

