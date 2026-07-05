export interface SystemHealth {

    database: boolean;

    api: boolean;

    ai: boolean;

    storage: boolean;

    payments: boolean;

    verification: boolean;

}

export class SystemHealthEngine {

    static healthy(system: SystemHealth): boolean {

        return Object.values(system).every(Boolean);

    }

}