const cards = [
  {
    title: "Backend",
    value: "Healthy",
    color: "text-emerald-400"
  },
  {
    title: "Database",
    value: "Connected",
    color: "text-green-400"
  },
  {
    title: "Redis",
    value: "Ready",
    color: "text-cyan-400"
  },
  {
    title: "Austin AI",
    value: "Running",
    color: "text-yellow-400"
  },
  {
    title: "Verification",
    value: "Online",
    color: "text-blue-400"
  },
  {
    title: "Memory",
    value: "18%",
    color: "text-pink-400"
  }
];

export default function StatusCards() {
  return (

    <div className="grid grid-cols-3 gap-5">

      {cards.map((card) => (

        <div
          key={card.title}
          className="rounded-xl border border-slate-800 bg-[#0d1a28] p-5 shadow-lg"
        >

          <p className="text-sm text-slate-400">
            {card.title}
          </p>

          <h2 className={`mt-3 text-2xl font-bold ${card.color}`}>
            {card.value}
          </h2>

        </div>

      ))}

    </div>

  );
}