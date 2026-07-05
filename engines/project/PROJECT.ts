/**
 * guavacheck
 * Project Model
 */

export type ProjectStatus =
    | "draft"
    | "planning"
    | "bidding"
    | "funding"
    | "active"
    | "paused"
    | "completed"
    | "cancelled";

export type ProjectType =
    | "residential"
    | "commercial"
    | "industrial"
    | "renovation"
    | "infrastructure"
    | "inspection"
    | "maintenance";

export interface ProjectLocation {
    country: string;
    state?: string;
    city?: string;
    address?: string;
    latitude?: number;
    longitude?: number;
}

export interface ProjectBudget {
    estimated: number;
    approved: number;
    spent: number;
    remaining: number;
    currency: string;
}

export interface ProjectTimeline {
    createdAt: Date;
    startDate?: Date;
    estimatedCompletion?: Date;
    completedAt?: Date;
}

export interface Project {
    id: string;
    name: string;
    description?: string;
    type: ProjectType;
    status: ProjectStatus;
    ownerId: string;
    location: ProjectLocation;
    budget: ProjectBudget;
    timeline: ProjectTimeline;
    trustScore?: number;
    createdBy: string;
    updatedAt: Date;
}