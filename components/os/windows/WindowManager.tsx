"use client";

import AppWindow from "./AppWindow";
import WindowTabs from "./WindowTabs";
import AustinWorkspace from "@/components/dashboard/austin/AustinWorkspace";

export default function WindowManager() {
  return (
    <main className="h-full p-6">

      <WindowTabs />

      <div className="mt-6 grid h-[calc(100vh-180px)] gap-6">

        <AppWindow title="Austin AI">

          <AustinWorkspace />

        </AppWindow>

      </div>

    </main>
  );
}