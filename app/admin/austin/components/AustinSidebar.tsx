const menu = [
  "Dashboard",
  "Conversation",
  "Architecture",
  "Agents",
  "Memory",
  "Verification",
  "Construction",
  "Investment",
  "Geo Engine",
  "Localization",
  "World Engine",
  "Jobs",
  "Analytics",
  "Settings"
];

export default function AustinSidebar() {
  return (
    <aside className="w-72 border-r border-slate-800 bg-[#08121c]">

      <div className="border-b border-slate-800 p-6">

        <h2 className="text-2xl font-bold text-emerald-400">
          AUSTIN
        </h2>

        <p className="mt-2 text-sm text-slate-500">
          Engineering Intelligence
        </p>

      </div>

      <nav className="p-4">

        {menu.map((item) => (

          <button
            key={item}
            className="mb-2 w-full rounded-lg px-4 py-3 text-left text-slate-300 transition hover:bg-emerald-600 hover:text-white"
          >
            {item}
          </button>

        ))}

      </nav>

    </aside>
  );
}