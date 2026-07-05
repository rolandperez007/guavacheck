export interface Deployment {

    version: string;

    deployedAt: Date;

    deployedBy: string;

    successful: boolean;

}

export class DeploymentMonitor {

    private static history: Deployment[] = [];

    static record(deployment: Deployment): void {

        this.history.push(deployment);

    }

    static latest(): Deployment | undefined {

        return this.history.at(-1);

    }

}