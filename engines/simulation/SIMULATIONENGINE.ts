import { Simulation } from "./SIMULATION";

export class SimulationEngine {

    private static simulations: Simulation[] = [];

    static register(simulation: Simulation): void {

        this.simulations.push(simulation);

    }

    static all(): Simulation[] {

        return this.simulations;

    }

    static count(): number {

        return this.simulations.length;

    }

}