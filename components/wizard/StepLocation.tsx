"use client";

import FormCard from "@/components/forms/FormCard";
import SectionTitle from "@/components/forms/SectionTitle";
import TextField from "@/components/forms/TextField";

import { usePropertyWizardContext } from "@/context/PropertyWizardContext";

export default function StepLocation() {
  const { wizard, updateWizard } = usePropertyWizardContext();

  const location = wizard.location;

  function updateField(
    field: keyof typeof location,
    value: string
  ) {
    updateWizard({
      location: {
        ...location,
        [field]: value,
      },
    });
  }

  return (
    <FormCard>

      <SectionTitle
        title="Property Location"
        subtitle="Austin uses your property's location to estimate value, verify details and provide local market intelligence."
      />

      <div className="grid gap-6 md:grid-cols-2">

        <TextField
          label="Country"
          value={location.country}
          onChange={(value) =>
            updateField("country", value)
          }
        />

        <TextField
          label="State / Province"
          value={location.state}
          onChange={(value) =>
            updateField("state", value)
          }
        />

        <TextField
          label="City"
          value={location.city}
          onChange={(value) =>
            updateField("city", value)
          }
        />

        <TextField
          label="Area"
          value={location.area}
          onChange={(value) =>
            updateField("area", value)
          }
        />

        <TextField
          label="Street Address"
          value={location.street}
          onChange={(value) =>
            updateField("street", value)
          }
        />

        <TextField
          label="Postal Code"
          value={location.postalCode ?? ""}
          onChange={(value) =>
            updateField("postalCode", value)
          }
        />

        <TextField
          label="Nearest Landmark"
          value={location.landmark ?? ""}
          onChange={(value) =>
            updateField("landmark", value)
          }
        />

      </div>

      <div className="mt-10 rounded-xl border border-dashed border-green-300 bg-green-50 p-8 text-center">

        <div className="text-5xl mb-3">
          📍
        </div>

        <h3 className="text-xl font-semibold">
          Interactive Map
        </h3>

        <p className="mt-2 text-gray-600">
          Coming in the next update.
        </p>

        <p className="text-sm text-gray-500 mt-2">
          Users will be able to drop a pin, detect GPS,
          or search any address worldwide.
        </p>

      </div>

    </FormCard>
  );
}