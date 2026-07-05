export interface Evidence {

    id: string;

    type: string;

    description: string;

    source: string;

    verified: boolean;

    uploadedAt: Date;

}

export class EvidenceEngine {

    static sufficient(

        evidence: Evidence[]

    ): boolean {

        return evidence.filter(

            item => item.verified

        ).length >= 2;

    }

}