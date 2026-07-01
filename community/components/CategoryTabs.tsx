const tabs = [
  "Building",
  "Architecture",
  "Interior",
  "Construction",
  "Materials",
  "Finance",
  "Real Estate",
  "Ideas"
];

export default function CategoryTabs() {
  return (
    <div className="flex gap-3 flex-wrap mt-6">

      {tabs.map(tab => (

        <button
          key={tab}
          className="rounded-full border px-5 py-2 hover:bg-black hover:text-white transition"
        >
          {tab}
        </button>

      ))}

    </div>
  );
}