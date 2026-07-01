import CommunityHeader from "./components/CommunityHeader";
import SearchBar from "./components/SearchBar";
import CategoryTabs from "./components/CategoryTabs";
import AustinDigest from "./components/AustinDigest";
import TrendingPanel from "./components/TrendingPanel";
import CommunityFeed from "./components/CommunityFeed";
import RightSidebar from "./components/RightSidebar";

export default function CommunityPage() {
  return (
    <main className="min-h-screen bg-slate-50">
      <div className="mx-auto max-w-7xl px-6 py-10">

        <CommunityHeader />

        <div className="mt-8">
          <SearchBar />
        </div>

        <div className="mt-6">
          <CategoryTabs />
        </div>

        <div className="mt-10 grid grid-cols-1 gap-8 lg:grid-cols-12">

          <div className="space-y-6 lg:col-span-8">

            <AustinDigest />

            <TrendingPanel />

            <CommunityFeed />

          </div>

          <aside className="lg:col-span-4">

            <RightSidebar />

          </aside>

        </div>

      </div>
    </main>
  );
}