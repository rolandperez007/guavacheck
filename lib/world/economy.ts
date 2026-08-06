export function getEconomy() {
  const hour = new Date().getHours();

  return {
    confidence: 82,

    transactions: Math.floor(Math.random() * 80) + 20,

    listings: 1480,

    rentalDemand: 74,

    mortgageDemand: 68,

    activeInvestors: 312,

    sentiment: hour < 18 ? "Bullish" : "Neutral",
  };
}
