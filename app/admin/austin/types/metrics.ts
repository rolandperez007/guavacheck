export interface EngineMetric {
  name: string;
  status: "active" | "idle" | "offline" | "error";
  load?: number;
  requests?: number;
  responseTime?: number;
}

export interface MemoryStats {
  total: number;
  used: number;
  free: number;

  cacheSize?: number;
  cacheHits?: number;
  cacheMisses?: number;
}

export interface QueueStats {
  pending: number;
  processing: number;
  completed: number;
  failed: number;

  workers?: number;
}

export interface LiveMetric {
  timestamp: string;

  cpu?: number;
  memory?: number;
  requests?: number;

  engines?: EngineMetric[];
  queue?: QueueStats;
  memoryStats?: MemoryStats;
}

export interface MetricsResponse {
  success: boolean;
  data: LiveMetric;
  error?: string;
}