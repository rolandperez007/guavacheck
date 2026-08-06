export interface Session {
  user: string;

  workspace: string;

  openedApps: string[];

  recentDocuments: string[];

  notifications: number;
}
