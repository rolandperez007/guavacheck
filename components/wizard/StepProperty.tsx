"use client";

import { ChangeEvent } from "react";

import { usePropertyWizardContext } from "@/context/PropertyWizardContext";

export default function StepProperty() {
  const { wizard, updateWizard } = usePropertyWizardContext();

  const property = wizard.property;

  function updateField(field: keyof typeof property, value: string | number | boolean) {
    updateWizard({
      property: {
        ...property,
        [field]: value,
      },
    });
  }

  return (
    <div className="mx-auto max-w-5xl">
      <div className="mb-10">
        <h1 className="text-4xl font-bold">Tell us about your property</h1>

        <p className="mt-3 text-gray-600">
          This information helps Austin estimate value, understand the property, and prepare it for
          verification.
        </p>
      </div>

      <div className="grid gap-6 md:grid-cols-2">
        {/* Property Name */}

        <div>
          <label className="mb-2 block font-medium">Property Name</label>

          <input
            type="text"
            value={property.name}
            onChange={(e: ChangeEvent<HTMLInputElement>) => updateField("name", e.target.value)}
            className="w-full rounded-xl border p-3"
            placeholder="Sunrise Villa"
          />
        </div>

        {/* Property Type */}

        <div>
          <label className="mb-2 block font-medium">Property Type</label>

          <select
            value={property.propertyType}
            onChange={(e) => updateField("propertyType", e.target.value)}
            className="w-full rounded-xl border p-3"
          >
            <option value="">Select Property Type</option>
            <option>Detached House</option>
            <option>Semi Detached</option>
            <option>Terrace House</option>
            <option>Duplex</option>
            <option>Bungalow</option>
            <option>Apartment</option>
            <option>Penthouse</option>
            <option>Commercial Building</option>
            <option>Warehouse</option>
            <option>Land</option>
          </select>
        </div>

        {/* Bedrooms */}

        <div>
          <label className="mb-2 block font-medium">Bedrooms</label>

          <input
            type="number"
            min={0}
            value={property.bedrooms}
            onChange={(e) => updateField("bedrooms", Number(e.target.value))}
            className="w-full rounded-xl border p-3"
          />
        </div>

        {/* Bathrooms */}

        <div>
          <label className="mb-2 block font-medium">Bathrooms</label>

          <input
            type="number"
            min={0}
            value={property.bathrooms}
            onChange={(e) => updateField("bathrooms", Number(e.target.value))}
            className="w-full rounded-xl border p-3"
          />
        </div>

        {/* Toilets */}

        <div>
          <label className="mb-2 block font-medium">Toilets</label>

          <input
            type="number"
            min={0}
            value={property.toilets}
            onChange={(e) => updateField("toilets", Number(e.target.value))}
            className="w-full rounded-xl border p-3"
          />
        </div>

        {/* Parking */}

        <div>
          <label className="mb-2 block font-medium">Parking Spaces</label>

          <input
            type="number"
            min={0}
            value={property.parkingSpaces}
            onChange={(e) => updateField("parkingSpaces", Number(e.target.value))}
            className="w-full rounded-xl border p-3"
          />
        </div>

        {/* Land */}

        <div>
          <label className="mb-2 block font-medium">Land Size (sqm)</label>

          <input
            type="number"
            min={0}
            value={property.landSize}
            onChange={(e) => updateField("landSize", Number(e.target.value))}
            className="w-full rounded-xl border p-3"
          />
        </div>

        {/* Building */}

        <div>
          <label className="mb-2 block font-medium">Building Size (sqm)</label>

          <input
            type="number"
            min={0}
            value={property.buildingSize}
            onChange={(e) => updateField("buildingSize", Number(e.target.value))}
            className="w-full rounded-xl border p-3"
          />
        </div>

        {/* Floors */}

        <div>
          <label className="mb-2 block font-medium">Number of Floors</label>

          <input
            type="number"
            min={1}
            value={property.floors}
            onChange={(e) => updateField("floors", Number(e.target.value))}
            className="w-full rounded-xl border p-3"
          />
        </div>

        {/* Condition */}

        <div>
          <label className="mb-2 block font-medium">Condition</label>

          <select
            value={property.condition}
            onChange={(e) => updateField("condition", e.target.value)}
            className="w-full rounded-xl border p-3"
          >
            <option value="">Select</option>
            <option>New</option>
            <option>Excellent</option>
            <option>Good</option>
            <option>Needs Renovation</option>
            <option>Distress Sale</option>
          </select>
        </div>
      </div>

      {/* Furnished */}

      <div className="mt-8">
        <label className="flex items-center gap-3">
          <input
            type="checkbox"
            checked={property.furnished}
            onChange={(e) => updateField("furnished", e.target.checked)}
          />

          <span>This property is furnished</span>
        </label>
      </div>

      {/* Description */}

      <div className="mt-8">
        <label className="mb-2 block font-medium">Description</label>

        <textarea
          rows={6}
          value={property.description}
          onChange={(e) => updateField("description", e.target.value)}
          className="w-full rounded-xl border p-3"
          placeholder="Tell buyers about this property..."
        />
      </div>
    </div>
  );
}
