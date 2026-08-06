"use client";

import { useMemo } from "react";

import { WizardStep } from "@/types/PropertyWizard";

import { usePropertyWizardContext } from "@/context/PropertyWizardContext";

const steps: WizardStep[] = [
  "welcome",
  "intent",
  "property",
  "location",
  "media",
  "documents",
  "austin",
  "services",
  "review",
  "complete",
];

export function usePropertyWizard() {
  const { wizard, updateWizard, goToStep, resetWizard } = usePropertyWizardContext();

  const currentIndex = useMemo(() => {
    return steps.indexOf(wizard.progress.currentStep);
  }, [wizard.progress.currentStep]);

  const totalSteps = steps.length;

  const percentage = Math.round(((currentIndex + 1) / totalSteps) * 100);

  function nextStep() {
    if (currentIndex >= totalSteps - 1) return;

    const next = steps[currentIndex + 1];

    updateWizard({
      progress: {
        ...wizard.progress,
        currentStep: next,
        percentage,
        completedSteps: [
          ...new Set([...wizard.progress.completedSteps, wizard.progress.currentStep]),
        ],
      },
    });
  }

  function previousStep() {
    if (currentIndex <= 0) return;

    const previous = steps[currentIndex - 1];

    goToStep(previous);
  }

  function jumpToStep(step: WizardStep) {
    goToStep(step);
  }

  function completeWizard() {
    updateWizard({
      progress: {
        ...wizard.progress,
        currentStep: "complete",
        completedSteps: [...steps],
        percentage: 100,
        isComplete: true,
      },
    });
  }

  function saveDraft() {
    if (typeof window === "undefined") return;

    localStorage.setItem("guavacheck-property-wizard", JSON.stringify(wizard));
  }

  function loadDraft() {
    if (typeof window === "undefined") return;

    const draft = localStorage.getItem("guavacheck-property-wizard");

    if (!draft) return;

    updateWizard(JSON.parse(draft));
  }

  function clearDraft() {
    if (typeof window === "undefined") return;

    localStorage.removeItem("guavacheck-property-wizard");
  }

  return {
    wizard,

    steps,

    totalSteps,

    currentIndex,

    currentStep: wizard.progress.currentStep,

    percentage,

    nextStep,

    previousStep,

    jumpToStep,

    completeWizard,

    saveDraft,

    loadDraft,

    clearDraft,

    resetWizard,
  };
}
