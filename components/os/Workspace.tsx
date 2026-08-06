"use client";

import WindowManager from "./windows/WindowManager";

export default function Workspace() {
  return (
    <section className="flex-1 overflow-hidden bg-black">
      <WindowManager />
    </section>
  );
}
