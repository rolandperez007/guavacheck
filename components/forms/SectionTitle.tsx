"use client";

interface SectionTitleProps {
  title: string;
  subtitle?: string;
}

export default function SectionTitle({ title, subtitle }: SectionTitleProps) {
  return (
    <div className="mb-8">
      <h1 className="text-3xl font-bold text-gray-900">{title}</h1>

      {subtitle && <p className="mt-3 text-gray-600">{subtitle}</p>}
    </div>
  );
}
