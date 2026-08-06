/**
 * Engine Metadata
 */

export interface EngineMetadata {
  id: string;

  name: string;

  displayName: string;

  description: string;

  owner: string;

  version: string;

  build: string;

  created: Date;

  updated: Date;

  tags: string[];

  category: string;

  status: "development" | "testing" | "staging" | "production" | "deprecated";
}
