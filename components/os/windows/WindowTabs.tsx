"use client";

const tabs = [
  "Dashboard",
  "Properties",
  "Austin",
  "Verification",
];

export default function WindowTabs() {
  return (
    <div className="flex border-b border-neutral-800 bg-black">

      {tabs.map((tab, index) => (

        <button
          key={tab}
          className={`
            px-6 py-4 text-sm
            ${
              index === 0
                ? "border-b-2 border-emerald-500 text-white"
                : "text-neutral-500 hover:text-white"
            }
          `}
        >
          {tab}
        </button>

      ))}

    </div>
  );
}