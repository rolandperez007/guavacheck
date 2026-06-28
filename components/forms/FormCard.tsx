"use client";

import { ReactNode } from "react";

interface FormCardProps {
  children: ReactNode;
}

export default function FormCard({
  children,
}: FormCardProps) {
  return (
    <div className="rounded-2xl border border-gray-200 bg-white p-8 shadow-sm">
      {children}
    </div>
  );
}