"use client";

import FormCard from "@/components/forms/FormCard";
import SectionTitle from "@/components/forms/SectionTitle";
import FileUpload from "@/components/forms/FileUpload";

import { usePropertyWizardContext } from "@/context/PropertyWizardContext";

export default function StepMedia() {
  const { wizard, updateWizard } = usePropertyWizardContext();

  const media = wizard.media;

  function updateMedia(field: keyof typeof media, files: File[]) {
    updateWizard({
      media: {
        ...media,
        [field]: files,
      },
    });
  }

  return (
    <FormCard>
      <SectionTitle
        title="Property Media"
        subtitle="Great media increases buyer confidence. Upload as much as possible for the best results."
      />

      <div className="space-y-10">
        <FileUpload
          label="Property Photos"
          accept="image/*"
          files={media.photos}
          helperText="Living room, bedrooms, bathrooms, kitchen, exterior and compound."
          onChange={(files) => updateMedia("photos", files)}
        />

        <FileUpload
          label="Property Videos"
          accept="video/*"
          files={media.videos}
          helperText="Walk-through videos improve engagement."
          onChange={(files) => updateMedia("videos", files)}
        />

        <FileUpload
          label="Floor Plans"
          accept=".pdf,image/*"
          files={media.floorPlans}
          helperText="Architectural drawings or scanned plans."
          onChange={(files) => updateMedia("floorPlans", files)}
        />

        <FileUpload
          label="Drone Images"
          accept="image/*"
          files={media.droneImages}
          helperText="Optional aerial photographs."
          onChange={(files) => updateMedia("droneImages", files)}
        />

        <FileUpload
          label="Virtual Tours"
          accept="video/*"
          files={media.virtualTours}
          helperText="360° walkthroughs or virtual property tours."
          onChange={(files) => updateMedia("virtualTours", files)}
        />
      </div>

      <div className="mt-10 rounded-xl border border-green-200 bg-green-50 p-6">
        <h3 className="mb-3 text-lg font-semibold text-green-700">Austin AI Media Assistant</h3>

        <ul className="list-disc space-y-2 pl-5 text-sm text-gray-700">
          <li>Detect blurry or low-quality photos.</li>

          <li>Recommend missing rooms to photograph.</li>

          <li>Suggest better image order for listings.</li>

          <li>Calculate a media quality score.</li>

          <li>Recommend drone photography if needed.</li>
        </ul>
      </div>
    </FormCard>
  );
}
