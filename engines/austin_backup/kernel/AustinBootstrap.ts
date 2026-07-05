/**
 * ============================================================
 * guavacheck
 * Austin Operating System
 * ------------------------------------------------------------
 * File: AustinBootstrap.ts
 *
 * Description:
 * Boots the Austin Operating System.
 *
 * Responsibilities:
 *  - Read configuration
 *  - Create kernel
 *  - Initialize registry
 *  - Start core services
 *  - Transition Austin into READY state
 * ============================================================
 */

import { AustinConfiguration } from "./AustinConfiguration";
import { DefaultAustinConfiguration } from "./AustinConfiguration";
import { AustinKernel } from "./AustinKernel";

export class AustinBootstrap {

    /**
     * Current Austin configuration.
     */
    private readonly configuration: AustinConfiguration;

    /**
     * Austin Kernel instance.
     */
    private readonly kernel: AustinKernel;

    constructor(
        configuration: AustinConfiguration = DefaultAustinConfiguration
    ) {

        this.configuration = configuration;
        this.kernel = new AustinKernel(configuration);

    }

    /**
     * Starts the Austin Operating System.
     */
    public async boot(): Promise<void> {

        console.log("=====================================");
        console.log(" Austin Operating System");
        console.log(" Boot Sequence Starting...");
        console.log("=====================================");

        await this.kernel.initialize();

        await this.kernel.start();

        console.log("=====================================");
        console.log(" Austin Ready");
        console.log("=====================================");

    }

}