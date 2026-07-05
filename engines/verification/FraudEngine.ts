export interface FraudSignal {

    id: string;

    entityId: string;

    type: string;

    severity: "low" | "medium" | "high" | "critical";

    detectedAt: Date;

}

export class FraudEngine {

    static suspicious(signals: FraudSignal[]): boolean {

        return signals.some(signal =>

            signal.severity === "critical"

        );

    }

}