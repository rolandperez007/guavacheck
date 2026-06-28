import { PropertyContext, SpecialistResponse } from "../types";

export function mediaSpecialist(
  context: PropertyContext
): SpecialistResponse {
  const photos = context.media?.photos || [];

  return {
    specialist: "media",

    summary: "Media quality analysis completed",

    findings: [
      photos.length > 5
        ? "Good number of property images"
        : "Insufficient property visuals",
    ],

    opportunities: [
      photos.length < 5
        ? "Add more images to improve listing performance"
        : "Media presentation is adequate",
    ],
  };
}