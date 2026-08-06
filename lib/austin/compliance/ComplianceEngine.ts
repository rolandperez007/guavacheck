export class ComplianceEngine {
  static kycRecords: any[] = [];
  static amlFlags: any[] = [];

  static runKYC(user: any) {
    const score = this.calculateIdentityScore(user);

    const record = {
      id: Math.random().toString(36).substring(2),
      user,
      verified: score > 70,
      score,
      timestamp: new Date(),
    };

    this.kycRecords.push(record);

    return record;
  }

  static calculateIdentityScore(user: any) {
    let score = 50;

    if (user.email?.includes("@")) score += 10;
    if (user.phone) score += 10;
    if (user.idDocument) score += 20;
    if (user.address) score += 10;

    return Math.min(100, score);
  }

  static amlCheck(transaction: any) {
    let risk = 20;

    if (transaction.amount > 100000000) risk += 30;
    if (transaction.country === "unknown") risk += 20;
    if (transaction.source === "crypto") risk += 15;

    const flagged = risk > 60;

    const result = {
      id: Math.random().toString(36).substring(2),
      transaction,
      riskScore: risk,
      flagged,
      timestamp: new Date(),
    };

    this.amlFlags.push(result);

    return result;
  }

  static complianceScore(user: any, transaction: any) {
    const kyc = this.calculateIdentityScore(user);
    const aml = this.amlCheck(transaction).riskScore;

    const score = Math.max(0, kyc - aml);

    return {
      kycScore: kyc,
      amlRisk: aml,
      complianceScore: score,
      approved: score > 50,
    };
  }

  static getReports() {
    return {
      kyc: this.kycRecords,
      aml: this.amlFlags,
    };
  }
}
