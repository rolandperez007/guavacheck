export class EscrowEngine {
  static deals: any[] = [];

  static createDeal(input: { buyer: string; seller: string; propertyId: string; amount: number }) {
    const deal = {
      id: Math.random().toString(36).substring(2),
      buyer: input.buyer,
      seller: input.seller,
      propertyId: input.propertyId,
      amount: input.amount,
      status: "CREATED",
      milestones: [
        { name: "deposit", status: "pending" },
        { name: "inspection", status: "pending" },
        { name: "final_payment", status: "pending" },
      ],
      createdAt: new Date(),
    };

    this.deals.push(deal);
    return deal;
  }

  static updateMilestone(dealId: string, milestone: string, status: string) {
    const deal = this.deals.find((d) => d.id === dealId);
    if (!deal) return { error: "deal_not_found" };

    const m = deal.milestones.find((x: any) => x.name === milestone);
    if (m) m.status = status;

    return deal;
  }

  static getDeals() {
    return this.deals;
  }
}
