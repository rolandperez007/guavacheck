export class UIEngine {
  static formatProperty(property: any) {
    return {
      title: property.title,
      location: property.location,
      price: new Intl.NumberFormat().format(property.price),
      badge: this.getBadge(property),
      riskLabel: this.getRiskLabel(property.risk || 0),
    };
  }

  static getBadge(property: any) {
    if (property.price > 500000000) return "PREMIUM";
    if (property.price > 100000000) return "HIGH VALUE";
    return "STANDARD";
  }

  static getRiskLabel(risk: number) {
    if (risk < 30) return "LOW RISK";
    if (risk < 70) return "MEDIUM RISK";
    return "HIGH RISK";
  }
}
