export interface ApiMetric {

    endpoint: string;

    averageResponse: number;

    requests: number;

    errors: number;

    timestamp: Date;

}

export class ApiMonitor {

    static health(metric: ApiMetric): string {

        if (metric.errors > 10)
            return "critical";

        if (metric.averageResponse > 500)
            return "warning";

        return "healthy";

    }

}