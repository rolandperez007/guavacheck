"use client";

import RoleGuard from "@/components/RoleGuard";

export default function InvestorDashboard() {

  return (
    <RoleGuard role="investor">

      <div style={{ padding: 20 }}>

        <h1>Investor Dashboard</h1>

        <p>Protected investor analytics panel.</p>

      </div>

    </RoleGuard>
  );
}
