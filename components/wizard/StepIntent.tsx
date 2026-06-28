"use client";

import { WizardIntent } from "@/types/PropertyWizard";
import { usePropertyWizardContext } from "@/context/PropertyWizardContext";
import { usePropertyWizard } from "@/hooks/usePropertyWizard";

interface IntentCard {
  title: string;
  subtitle: string;
  icon: string;
  value: WizardIntent;
}

const intents: IntentCard[] = [
  {
    title: "Sell Property",
    subtitle: "List an existing residential property for sale.",
    icon: "🏠",
    value: "sell",
  },
  {
    title: "Sell Distress Property",
    subtitle: "Privately list a verified distress opportunity.",
    icon: "🚨",
    value: "distress",
  },
  {
    title: "Rent Property",
    subtitle: "Advertise a property for rent or lease.",
    icon: "🏘️",
    value: "rent",
  },
  {
    title: "Build a New Property",
    subtitle: "Start a new residential construction project.",
    icon: "🏗️",
    value: "build",
  },
  {
    title: "Commercial Project",
    subtitle: "Create an office, retail, industrial or mixed-use project.",
    icon: "🏢",
    value: "commercial",
  },
  {
    title: "AI Design Studio",
    subtitle: "Generate architectural concepts with Austin AI.",
    icon: "📐",
    value: "design",
  },
  {
    title: "Cost Estimation",
    subtitle: "Generate an intelligent construction estimate.",
    icon: "💰",
    value: "estimate",
  },
];

export default function StepIntent() {
  const { wizard, updateWizard } = usePropertyWizardContext();
  const { nextStep } = usePropertyWizard();

  function selectIntent(intent: WizardIntent) {
    updateWizard({
      intent,
    });

    nextStep();
  }

  return (
    <div className="mx-auto max-w-6xl">

      <div className="mb-10 text-center">

        <h1 className="mb-3 text-4xl font-bold text-gray-900">
          What would you like to do?
        </h1>

        <p className="text-lg text-gray-600">
          Choose the experience that best matches your goal.
          Austin will tailor the remaining steps accordingly.
        </p>

      </div>

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-3">

        {intents.map((item) => {
          const active = wizard.intent === item.value;

          return (
            <button
              key={item.value}
              type="button"
              onClick={() => selectIntent(item.value)}
              className={`rounded-2xl border p-6 text-left transition-all duration-200 ${
                active
                  ? "border-green-600 bg-green-50 shadow-lg"
                  : "border-gray-200 bg-white hover:border-green-400 hover:shadow-md"
              }`}
            >
              <div className="mb-5 text-5xl">
                {item.icon}
              </div>

              <h2 className="mb-2 text-xl font-semibold text-gray-900">
                {item.title}
              </h2>

              <p className="text-sm leading-6 text-gray-600">
                {item.subtitle}
              </p>

              <div className="mt-6 text-sm font-semibold text-green-600">
                Continue →
              </div>
            </button>
          );
        })}

      </div>

    </div>
  );
}