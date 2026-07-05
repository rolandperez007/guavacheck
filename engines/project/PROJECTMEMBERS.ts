export interface ProjectMember {

    userId: string;

    role:
        | "owner"
        | "architect"
        | "engineer"
        | "contractor"
        | "lawyer"
        | "surveyor"
        | "quantitySurveyor"
        | "inspector"
        | "supplier";

    joinedAt: Date;

}