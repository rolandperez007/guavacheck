import AustinSidebar from "@/app/components/austin/AustinSidebar";
import Dashboard from "@/app/components/dashboard/Dashboard";

export default function HomePage() {
  return (
    <main style={{ display: "flex" }}>
      <AustinSidebar />
      <Dashboard />
    </main>
  );
}






