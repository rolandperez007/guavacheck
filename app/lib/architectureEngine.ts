export type PropertyRecord = {
  id: string;
  title: string;
  price?: number;
  location?: string;
  property_type?: "flat" | "duplex" | "terrace";
};

export function mapPropertyToModel(property: PropertyRecord) {
  const type = property.property_type || "flat";

  // 🧠 intelligent defaults based on type
  const defaults = {
    flat: { floors: 1, width: 2, length: 2 },
    duplex: { floors: 2, width: 2.5, length: 3 },
    terrace: { floors: 3, width: 2, length: 4 },
  };

  const config = defaults[type];

  return {
    ...config,
    type,
  };
}