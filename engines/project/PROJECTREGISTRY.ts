import { Project } from "./PROJECT";

export class ProjectRegistry {
  private static projects = new Map<string, Project>();

  static register(project: Project): void {
    this.projects.set(project.id, project);
  }

  static get(id: string): Project | undefined {
    return this.projects.get(id);
  }

  static exists(id: string): boolean {
    return this.projects.has(id);
  }

  static all(): Project[] {
    return [...this.projects.values()];
  }

  static count(): number {
    return this.projects.size;
  }

  static remove(id: string): boolean {
    return this.projects.delete(id);
  }
}
