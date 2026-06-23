import { DataNormalizer } from "./DataNormalizer";
import { GlobalPropertyMap } from "@/lib/austin/world/GlobalPropertyMap";

export class IngestionPipeline {

  static dataset: any[] = [];

  static ingestBatch(rawList: any[]) {

    const normalized = rawList.map(item => DataNormalizer.normalize(item));

    for (const item of normalized) {

      const enriched = GlobalPropertyMap.ingest(item);

      this.dataset.push(enriched);
    }

    return {
      ingested: normalized.length,
      totalDataset: this.dataset.length
    };
  }

  static search(query: string) {

    return this.dataset.filter(item =>
      item.location?.toLowerCase().includes(query.toLowerCase()) ||
      item.title?.toLowerCase().includes(query.toLowerCase())
    );
  }

  static getAll() {
    return this.dataset;
  }
}

