"use client";

import FormCard from "@/components/forms/FormCard";
import SectionTitle from "@/components/forms/SectionTitle";

import { usePropertyWizardContext } from "@/context/PropertyWizardContext";

export default function StepAustin() {
  const { wizard } = usePropertyWizardContext();

  const analysis = wizard.ai;

  return (
    <FormCard>
      <SectionTitle
        title="Austin AI Analysis"
        subtitle="Austin has reviewed the information you've provided and is preparing intelligent recommendations."
      />

      <div className="space-y-6">
        {/* Estimated Value */}

        <div className="rounded-xl border bg-white p-5">
          <h3 className="font-semibold text-lg">Estimated Market Value</h3>

          <p className="mt-3 text-3xl font-bold text-green-600">
            {analysis.estimatedValue
              ? `$${analysis.estimatedValue.toLocaleString()}`
              : "Pending Analysis"}
          </p>
        </div>

        {/* Suggested Price */}

        <div className="rounded-xl border bg-white p-5">
          <h3 className="font-semibold text-lg">Suggested Listing Price</h3>

          <p className="mt-3 text-3xl font-bold text-blue-600">
            {analysis.suggestedPrice
              ? `$${analysis.suggestedPrice.toLocaleString()}`
              : "Pending Analysis"}
          </p>
        </div>

        {/* Confidence */}

        <div className="rounded-xl border bg-white p-5">
          <h3 className="font-semibold text-lg">Confidence Score</h3>

          <p className="mt-3 text-3xl font-bold text-purple-600">
            {analysis.confidence ? `${analysis.confidence}%` : "--"}
          </p>
        </div>

        {/* Recommendations */}

        <div className="rounded-xl border bg-green-50 p-6">
          <h3 className="font-semibold text-green-700">Recommendations</h3>

          {analysis.recommendations.length === 0 ? (
            <p className="mt-3 text-gray-600">
              Austin will generate recommendations after valuation and verification.
            </p>
          ) : (
            <ul className="mt-3 list-disc space-y-2 pl-6">
              {analysis.recommendations.map((item, index) => (
                <li key={index}>{item}</li>
              ))}
            </ul>
          )}
        </div>

        {/* Strengths */}

        <div className="rounded-xl border bg-blue-50 p-6">
          <h3 className="font-semibold text-blue-700">Property Strengths</h3>

          {analysis.strengths.length === 0 ? (
            <p className="mt-3 text-gray-600">Austin is still evaluating your property.</p>
          ) : (
            <ul className="mt-3 list-disc space-y-2 pl-6">
              {analysis.strengths.map((item, index) => (
                <li key={index}>{item}</li>
              ))}
            </ul>
          )}
        </div>

        {/* Warnings */}

        <div className="rounded-xl border bg-yellow-50 p-6">
          <h3 className="font-semibold text-yellow-700">Items Requiring Attention</h3>

          {analysis.warnings.length === 0 ? (
            <p className="mt-3 text-gray-600">No issues detected yet.</p>
          ) : (
            <ul className="mt-3 list-disc space-y-2 pl-6">
              {analysis.warnings.map((item, index) => (
                <li key={index}>{item}</li>
              ))}
            </ul>
          )}
        </div>
      </div>
    </FormCard>
  );
}
