export type ServiceStatus = "online" | "offline" | "degraded" | "checking" | "unknown";

export interface ServiceHealth {
  name: string;
  status: ServiceStatus;
  latency?: number;
  message?: string;
  lastChecked?: string;
}

export interface SystemHealth {
  overall: ServiceStatus;

  fastapi: ServiceHealth;
  redis: ServiceHealth;
  postgres: ServiceHealth;
  websocket: ServiceHealth;

  uptime?: number;
  version?: string;
  timestamp?: string;
}

export interface HealthResponse {
  success: boolean;
  data: SystemHealth;
  error?: string;
}
