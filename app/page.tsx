// app/page.tsx
import AustinSidebar from "../components/AustinSidebar";
import Dashboard from "../components/Dashboard";

export default function Home() {
  return (
    <div style={{ display: "flex" }}>
      <AustinSidebar />
      <Dashboard />
    </div>
  );
}