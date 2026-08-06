"use client";

export default function PropertyPreview() {
  return (
    <div className="rounded-2xl border border-neutral-800 bg-black p-6">
      <div className="h-48 rounded-xl bg-neutral-900" />

      <h3 className="mt-6 text-2xl font-semibold">No Property Selected</h3>

      <div className="mt-6 space-y-4">
        <div className="flex justify-between">
          <span>Valuation</span>
          <span>-</span>
        </div>

        <div className="flex justify-between">
          <span>Owner</span>
          <span>-</span>
        </div>

        <div className="flex justify-between">
          <span>Verification</span>
          <span>-</span>
        </div>

        <div className="flex justify-between">
          <span>Risk Score</span>
          <span>-</span>
        </div>

        <div className="flex justify-between">
          <span>AI Confidence</span>
          <span>-</span>
        </div>
      </div>

      <button className="mt-8 w-full rounded-xl bg-emerald-500 py-3 font-semibold text-black">
        Analyse with Austin
      </button>
    </div>
  );
}
