"use client";

import { ReactNode } from "react";
import WindowHeader from "./WindowHeader";

interface Props {
  title: string;
  children: ReactNode;
}

export default function AppWindow({
  title,
  children,
}: Props) {
  return (
    <section
      className="
      overflow-hidden
      rounded-3xl
      border
      border-neutral-800
      bg-neutral-950
      shadow-2xl
      "
    >

      <WindowHeader title={title} />

      <div className="h-full overflow-auto">

        {children}

      </div>

    </section>
  );
}