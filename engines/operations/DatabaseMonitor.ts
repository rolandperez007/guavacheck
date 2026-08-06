export interface DatabaseHealth {
  activeConnections: number;

  idleConnections: number;

  averageQueryTime: number;

  slowQueries: number;

  cacheHitRate: number;

  sequentialScans: number;

  missingIndexes: number;

  timestamp: Date;
}

export class DatabaseMonitor {
  static evaluate(health: DatabaseHealth): string[] {
    const recommendations: string[] = [];

    if (health.averageQueryTime > 100) recommendations.push("Investigate slow queries.");

    if (health.cacheHitRate < 95) recommendations.push("Increase cache efficiency.");

    if (health.missingIndexes > 0) recommendations.push("Create recommended indexes.");

    if (health.sequentialScans > 100) recommendations.push("Review execution plans.");

    return recommendations;
  }
}
