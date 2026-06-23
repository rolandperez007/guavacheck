export class PropertyService {
  static async search() {
    return [
      {
        id: "p1",
        title: "4 Bedroom Duplex",
        location: "Lekki Phase 1",
        price: 250000000,
        demandScore: 82,
        conditionScore: 78
      },
      {
        id: "p2",
        title: "Mini Flat",
        location: "Ajah",
        price: 45000000,
        demandScore: 70,
        conditionScore: 65
      }
    ];
  }

  static async rank(properties: any[]) {
    return properties || [];
  }

  static async formatListings(properties: any[]) {
    return (properties || []).map(p => ({
      ...p,
      formattedPrice: `₦${p.price ?? 0}`
    }));
  }
}
