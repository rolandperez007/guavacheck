export type ReportInput = {
  projectType: string;
  location: string;
  estimatedDurationWeeks: number;
};

export class ReportService {
  static generateReport(input: ReportInput) {
    return {
      projectType: input.projectType,
      location: input.location,
      estimatedDurationWeeks: input.estimatedDurationWeeks,
    };
  }
}
