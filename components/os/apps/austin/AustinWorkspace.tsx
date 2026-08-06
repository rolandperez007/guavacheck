"use client";

import ConversationList from "./ConversationList";
import ChatWindow from "./ChatWindow";
import ReasoningPanel from "./ReasoningPanel";
import SuggestedActions from "./SuggestedActions";

export default function AustinWorkspace() {
  return (
    <section className="rounded-3xl border border-neutral-800 bg-neutral-950">
      <div className="border-b border-neutral-800 p-8">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-4xl font-bold">Austin AI Workspace</h2>

            <p className="mt-3 text-neutral-400">Your intelligent property operating partner.</p>
          </div>

          <div className="rounded-full bg-emerald-500/20 px-5 py-2 text-emerald-400">● Online</div>
        </div>
      </div>

      <div className="grid h-[850px] xl:grid-cols-12">
        <div className="border-r border-neutral-800 xl:col-span-3">
          <ConversationList />
        </div>

        <div className="border-r border-neutral-800 xl:col-span-6">
          <ChatWindow />
        </div>

        <div className="xl:col-span-3">
          <ReasoningPanel />

          <SuggestedActions />
        </div>
      </div>
    </section>
  );
}
