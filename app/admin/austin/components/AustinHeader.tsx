export default function AustinHeader() {
  const now = new Date().toLocaleString();

  return (
    <header className="flex items-center justify-between border-b border-slate-800 bg-[#0b1724] px-8 py-5">

      <div>
        <h1 className="text-3xl font-bold text-white">
          Austin Engineering Console
        </h1>

        <p className="mt-1 text-sm text-slate-400">
          guavacheck Internal AI Administrator
        </p>
      </div>

      <div className="text-right">

        <div className="flex items-center justify-end gap-2">

          <div className="h-3 w-3 rounded-full bg-emerald-500 animate-pulse" />

          <span className="font-semibold text-emerald-400">
            ONLINE
          </span>

        </div>

        <p className="mt-2 text-xs text-slate-500">
          {now}
        </p>

      </div>

    </header>
  );
}