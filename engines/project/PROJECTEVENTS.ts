export interface ProjectEvent {
  id: string;

  projectId: string;

  type: string;

  message: string;

  actor: string;

  createdAt: Date;
}
