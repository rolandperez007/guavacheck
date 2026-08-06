"use client";

import { usePropertyWizard } from "@/hooks/usePropertyWizard";

export default function StepWelcome() {
  const { nextStep } = usePropertyWizard();

  return (
    <div className="mx-auto flex max-w-3xl flex-col items-center py-12 text-center">
      {/* Logo */}

      <div className="mb-8 flex h-24 w-24 items-center justify-center rounded-full bg-green-100 text-5xl shadow">
        🏡
      </div>

      {/* Title */}

      <h1 className="mb-4 text-4xl font-bold text-gray-900">Welcome to guavacheck</h1>

      {/* Subtitle */}

      <p className="mb-10 max-w-2xl text-lg leading-8 text-gray-600">
        Let's prepare your property with a guided experience. Austin AI will help verify
        information, estimate value, and recommend the next best actions before you publish.
      </p>

      {/* Highlights */}

      <div className="mb-12 grid w-full gap-4 md:grid-cols-3">
        <div className="rounded-xl border bg-white p-6 shadow-sm">
          <div className="mb-3 text-3xl">⚡</div>

          <h3 className="mb-2 font-semibold">Fast</h3>

          <p className="text-sm text-gray-600">Complete your listing in about five minutes.</p>
        </div>

        <div className="rounded-xl border bg-white p-6 shadow-sm">
          <div className="mb-3 text-3xl">🤖</div>

          <h3 className="mb-2 font-semibold">Austin AI</h3>

          <p className="text-sm text-gray-600">
            Receive intelligent guidance throughout the process.
          </p>
        </div>

        <div className="rounded-xl border bg-white p-6 shadow-sm">
          <div className="mb-3 text-3xl">🛡️</div>

          <h3 className="mb-2 font-semibold">Secure</h3>

          <p className="text-sm text-gray-600">
            Every listing goes through verification before publication.
          </p>
        </div>
      </div>

      {/* Call to Action */}

      <button
        onClick={nextStep}
        className="rounded-xl bg-green-600 px-10 py-4 text-lg font-semibold text-white transition hover:bg-green-700"
      >
        Start Property Wizard →
      </button>

      {/* Footer */}

      <p className="mt-8 text-sm text-gray-500">
        Estimated completion time: <strong>5 minutes</strong>
      </p>
    </div>
  );
}
