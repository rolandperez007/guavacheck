import { PropertyContext, WizardAustinInput, UserIntent } from "./types";

/**
 * Convert Wizard Data → Austin Context
 * This is Austin's "perception layer"
 */

export function buildAustinContext(input: WizardAustinInput): PropertyContext {
  return {
    intent: mapIntent(input.intent),

    property: normalizeProperty(input.property),

    location: normalizeLocation(input.location),

    media: normalizeMedia(input.media),

    documents: normalizeDocuments(input.documents),

    timestamp: Date.now(),
  };
}

/* -----------------------------
   INTENT MAPPING
------------------------------*/

function mapIntent(intent: string | null): UserIntent {
  switch (intent) {
    case "sell":
      return "sell_advice";

    case "distress":
      return "distress_analysis";

    case "rent":
      return "market_insight";

    case "build":
      return "construction_analysis";

    case "commercial":
      return "valuation";

    case "design":
      return "design_advice";

    case "estimate":
      return "price_estimate";

    default:
      return "general_query";
  }
}

/* -----------------------------
   PROPERTY NORMALIZATION
------------------------------*/

function normalizeProperty(property: any) {
  if (!property) return {};

  return {
    name: property.name,
    type: property.propertyType,

    bedrooms: property.bedrooms,
    bathrooms: property.bathrooms,
    toilets: property.toilets,

    parkingSpaces: property.parkingSpaces,

    landSize: property.landSize,
    buildingSize: property.buildingSize,

    floors: property.floors,

    yearBuilt: property.yearBuilt,

    condition: property.condition,

    furnished: property.furnished,

    description: property.description,
  };
}

/* -----------------------------
   LOCATION NORMALIZATION
------------------------------*/

function normalizeLocation(location: any) {
  if (!location) return {};

  return {
    country: location.country,
    state: location.state,
    city: location.city,

    area: location.area,
    street: location.street,

    postalCode: location.postalCode,

    latitude: location.latitude,
    longitude: location.longitude,

    landmark: location.landmark,
  };
}

/* -----------------------------
   MEDIA NORMALIZATION
------------------------------*/

function normalizeMedia(media: any) {
  if (!media) return {};

  return {
    photos: media.photos || [],

    videos: media.videos || [],

    floorPlans: media.floorPlans || [],

    droneImages: media.droneImages || [],

    virtualTours: media.virtualTours || [],
  };
}

/* -----------------------------
   DOCUMENT NORMALIZATION
------------------------------*/

function normalizeDocuments(documents: any) {
  if (!documents) return {};

  return {
    certificateOfOccupancy: documents.certificateOfOccupancy || [],

    surveyPlan: documents.surveyPlan || [],

    deedOfAssignment: documents.deedOfAssignment || [],

    buildingApproval: documents.buildingApproval || [],

    taxClearance: documents.taxClearance || [],

    valuationReport: documents.valuationReport || [],

    otherDocuments: documents.otherDocuments || [],
  };
}
