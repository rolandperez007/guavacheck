"use client";

import RoleGuard from "@/components/RoleGuard";

export default function ContractorDashboard() {

  return (
    <RoleGuard role="contractor">

      <div style={{ padding: 20 }}>

        <h1>Contractor Dashboard</h1>

        <p>Protected contractor ecosystem.</p>

      </div>

    </RoleGuard>
  );
}
