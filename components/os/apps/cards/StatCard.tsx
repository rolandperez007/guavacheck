"use client";

type Props = {
  title: string;
  value: string;
  subtitle: string;
};

export default function StatCard({
  title,
  value,
  subtitle,
}: Props) {
  return (
    <div className="rounded-2xl border border-neutral-800 bg-neutral-950 p-6">

      <p className="text-sm text-neutral-400">
        {title}
      </p>

      <h2 className="mt-3 text-4xl font-bold">
        {value}
      </h2>

      <p className="mt-2 text-neutral-500">
        {subtitle}
      </p>

    </div>
  );
}