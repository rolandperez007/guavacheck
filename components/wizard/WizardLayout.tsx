"use client";

import { ReactNode } from "react";

import ProgressBar from "./ProgressBar";
import NavigationButtons from "./NavigationButtons";

interface WizardLayoutProps {
  children: ReactNode;

  currentStep: string;
  currentIndex: number;
  totalSteps: number;
  percentage: number;

  onNext: () => void;
  onPrevious: () => void;
}

export default function WizardLayout({
  children,
  currentStep,
  currentIndex,
  totalSteps,
  percentage,
  onNext,
  onPrevious,
}: WizardLayoutProps) {
  return (
    <div className="min-h-screen bg-gray-50">

      {/* Header */}

      <header className="border-b bg-white shadow-sm">
        <div className="mx-auto flex max-w-7xl items-center justify-between px-6 py-5">

          <div>
            <h1 className="text-2xl font-bold">
              guavacheck
            </h1>

            <p className="text-sm text-gray-500">
              Property Listing Wizard
            </p>
          </div>

          <div className="text-right">
            <div className="text-sm font-medium">
              Step {currentIndex + 1} of {totalSteps}
            </div>

            <div className="text-xs text-gray-500 capitalize">
              {currentStep}
            </div>
          </div>

        </div>
      </header>

      {/* Progress */}

      <div className="mx-auto max-w-7xl px-6 pt-6">
        <ProgressBar percentage={percentage} />
      </div>

      {/* Main */}

      <main className="mx-auto grid max-w-7xl grid-cols-1 gap-8 px-6 py-8 lg:grid-cols-4">

        {/* Wizard */}

        <section className="lg:col-span-3 rounded-xl bg-white p-8 shadow-sm">

          {children}

        </section>

        {/* Austin */}

        <aside className="rounded-xl bg-white p-6 shadow-sm">

          <h2 className="mb-4 text-lg font-semibold">
            Austin AI
          </h2>

          <div className="space-y-4 text-sm text-gray-600">

            <p>
              I'll guide you through every step of your
              property listing.
            </p>

            <p>
              As you complete the wizard, I'll analyse
              your information and provide recommendations.
            </p>

            <div className="rounded-lg bg-green-50 p-4">

              <p className="font-medium text-green-700">
                Status
              </p>

              <p className="mt-1 text-green-600">
                Ready to assist.
              </p>

            </div>

          </div>

        </aside>

      </main>

      {/* Footer */}

      <footer className="border-t bg-white">

        <div className="mx-auto max-w-7xl px-6 py-5">

          <NavigationButtons
            currentIndex={currentIndex}
            totalSteps={totalSteps}
            onPrevious={onPrevious}
            onNext={onNext}
          />

        </div>

      </footer>

    </div>
  );
}