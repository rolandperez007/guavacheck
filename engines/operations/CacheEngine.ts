export interface CacheStats {

    hits: number;

    misses: number;

}

export class CacheEngine {

    static hitRate(stats: CacheStats): number {

        const total = stats.hits + stats.misses;

        if (total === 0) return 0;

        return (stats.hits / total) * 100;

    }

}