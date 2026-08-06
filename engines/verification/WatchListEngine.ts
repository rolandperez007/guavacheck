export interface WatchlistEntry {
  entityId: string;

  reason: string;

  addedAt: Date;
}

export class WatchlistEngine {
  private static entries: WatchlistEntry[] = [];

  static add(entry: WatchlistEntry): void {
    this.entries.push(entry);
  }

  static all(): WatchlistEntry[] {
    return this.entries;
  }
}
