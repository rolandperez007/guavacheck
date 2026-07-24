"use client";

const chats = [
  "Investment Analysis",
  "Verify Land Title",
  "Construction Estimate",
  "Property Valuation",
  "Mortgage Advice",
  "Market Research"
];

export default function ConversationList() {
  return (
    <aside className="h-full overflow-y-auto p-6">

      <button className="mb-8 w-full rounded-xl bg-emerald-500 py-3 font-semibold text-black">
        + New Conversation
      </button>

      <div className="space-y-3">

        {chats.map((chat) => (

          <button
            key={chat}
            className="w-full rounded-xl border border-neutral-800 p-4 text-left hover:border-emerald-500"
          >

            {chat}

          </button>

        ))}

      </div>

    </aside>
  );
}