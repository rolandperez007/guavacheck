export class LearningEngine {
  static dataset: any[] = [];

  static learn(prediction: any, actual: any) {
    const error = Math.abs(prediction.predictedPrice - actual.price);

    this.dataset.push({
      prediction,
      actual,
      error,
      timestamp: new Date(),
    });

    return {
      recorded: true,
      error,
    };
  }

  static adjustConfidence(baseConfidence: number) {
    const recent = this.dataset.slice(-50);

    const avgError = recent.reduce((sum, d) => sum + d.error, 0) / (recent.length || 1);

    const adjustment = Math.max(0.5, 1 - avgError / 100000000);

    return baseConfidence * adjustment;
  }

  static getAccuracy() {
    const recent = this.dataset.slice(-100);

    if (!recent.length) return 0.5;

    const avgError = recent.reduce((sum, d) => sum + d.error, 0) / recent.length;

    return Math.max(0, 1 - avgError / 100000000);
  }
}
