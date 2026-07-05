import { Project } from "./PROJECT";
import { ProjectRegistry } from "./PROJECTREGISTRY";

export class ProjectEngine {

    static create(project: Project): Project {

        ProjectRegistry.register(project);

        return project;

    }

    static find(id: string): Project | undefined {

        return ProjectRegistry.get(id);

    }

    static list(): Project[] {

        return ProjectRegistry.all();

    }

}