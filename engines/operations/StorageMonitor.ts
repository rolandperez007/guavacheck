export interface StorageUsage {

    totalGB: number;

    usedGB: number;

}

export class StorageMonitor {

    static free(storage: StorageUsage): number {

        return storage.totalGB - storage.usedGB;

    }

}