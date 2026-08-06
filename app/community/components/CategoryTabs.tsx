const categories = [
  "Building",
  "Architecture",
  "Construction",
  "Finance",
  "Materials",
  "Interior",
  "Ideas",
  "Land",
];

export default function CategoryTabs() {
  return (
    <div className="flex flex-wrap gap-3">
      {categories.map((item) => (
        <button
          key={item}
          className="rounded-full border px-4 py-2 text-sm hover:bg-green-600 hover:text-white transition"
        >
          {item}
        </button>
      ))}
    </div>
  );
}
