export interface PoolStatus {
  maxConnections: number;

  activeConnections: number;

  waitingClients: number;
}

export class ConnectionPoolMonitor {
  static utilization(pool: PoolStatus): number {
    return (pool.activeConnections / pool.maxConnections) * 100;
  }
}
