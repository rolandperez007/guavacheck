"use client";

import WindowControls from "./WindowControls";

interface Props {
  title: string;
}

export default function WindowHeader({ title }: Props) {
  return (
    <header className="flex h-14 items-center justify-between border-b border-neutral-800 bg-neutral-900 px-5">

      <WindowControls />

      <h3 className="text-sm font-semibold tracking-wide text-neutral-200">
        {title}
      </h3>

      <div className="w-16" />

    </header>
  );
}