export interface TimelineEvent {

    id: string;

    projectId: string;

    title: string;

    description?: string;

    createdAt: Date;

    createdBy: string;

}