export class FraudService {

  static async checkPatterns() {
    return {
      riskLevel: 'low',
      flags: []
    };
  }

  static async scoreRisk() {
    return {
      riskScore: 22,
      status: 'safe'
    };
  }
}
