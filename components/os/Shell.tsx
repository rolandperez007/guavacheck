"use client";

import Sidebar from "./Sidebar";
import Topbar from "./Topbar";
import Workspace from "./Workspace";
import Dock from "./Dock";
import StatusBar from "./StatusBar";
import NotificationCenter from "./NotificationCenter";

export default function Shell() {
  return (
    <div className="relative flex h-screen overflow-hidden bg-[#050608]">
      <Sidebar />

      <div className="flex flex-1 flex-col">
        <Topbar />

        <Workspace />

        <Dock />

        <StatusBar />
      </div>

      <NotificationCenter />
    </div>
  );
}
