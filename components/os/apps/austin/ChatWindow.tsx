"use client";

export default function ChatWindow() {
  return (
    <section className="flex h-full flex-col">

      <div className="flex-1 space-y-6 overflow-y-auto p-8">

        <div className="max-w-lg rounded-2xl bg-neutral-900 p-5">

          Good morning.
          I am Austin.

          How can I help you today?

        </div>

        <div className="ml-auto max-w-lg rounded-2xl bg-emerald-500 p-5 text-black">

          Analyse property investment opportunities in Lekki.

        </div>

      </div>

      <div className="border-t border-neutral-800 p-6">

        <div className="flex gap-4">

          <input
            className="flex-1 rounded-xl border border-neutral-700 bg-black px-5 py-4 outline-none"
            placeholder="Ask Austin..."
          />

          <button className="rounded-xl bg-emerald-500 px-8 font-semibold text-black">
            Send
          </button>

        </div>

      </div>

    </section>
  );
}