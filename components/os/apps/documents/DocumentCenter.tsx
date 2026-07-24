"use client";

const docs = [
  "Land Titles",
  "Survey Plans",
  "Building Approval",
  "Architectural Drawings",
  "Mortgage Documents",
  "Investment Reports"
];

export default function DocumentCenter() {
  return (
    <section className="rounded-3xl border border-neutral-800 bg-neutral-950 p-8">

      <h2 className="text-3xl font-semibold">
        Document Center
      </h2>

      <div className="mt-8 grid gap-4 md:grid-cols-2">

        {docs.map((doc) => (

          <button
            key={doc}
            className="rounded-2xl border border-neutral-800 p-6 text-left hover:bg-neutral-900 transition"
          >

            📄 {doc}

          </button>

        ))}

      </div>

    </section>
  );
}