export interface VerificationAnomaly {

    id: string;

    entityId: string;

    category: string;

    severity: "low" | "medium" | "high" | "critical";

    message: string;

    timestamp: Date;

}

export class AnomalyEngine {

    static detect(

        anomalies: VerificationAnomaly[]

    ): boolean {

        return anomalies.some(

            a => a.severity === "critical"

        );

    }

}