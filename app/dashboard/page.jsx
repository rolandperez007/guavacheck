"use client"

import { useEffect, useState } from "react"
import { supabase } from "../../lib/supabase"
import { useRouter } from "next/navigation"

export default function Dashboard() {

  const router = useRouter()
  const [role, setRole] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {

    const loadUser = async () => {

      const { data: userData } = await supabase.auth.getUser()
      const user = userData.user

      if (!user) {
        router.push("/auth")
        return
      }

      const { data: profile } = await supabase
        .from("profiles")
        .select("*")
        .eq("id", user.id)
        .single()

      if (!profile) {
        router.push("/onboarding")
        return
      }

      setRole(profile.role)
      setLoading(false)
    }

    loadUser()

  }, [])

  if (loading) {
    return <main style={{ padding: 40 }}>Loading dashboard...</main>
  }

  return (
    <main style={{ padding: 40 }}>

      <h1>Global Dashboard</h1>

      {role === "Buyer" && <BuyerView />}
      {role === "Agent" && <AgentView />}
      {role === "Developer" && <DeveloperView />}
      {role === "Contractor" && <ContractorView />}
      {role === "Investor" && <InvestorView />}

    </main>
  )
}
function BuyerView() {
  return (
    <div>
      <h2>Buyer Dashboard</h2>
      <p>Search properties, track investments, save listings.</p>
    </div>
  )
}

function AgentView() {
  return (
    <div>
      <h2>Agent Dashboard</h2>
      <p>Manage listings, upload properties, track leads.</p>
    </div>
  )
}

function DeveloperView() {
  return (
    <div>
      <h2>Developer Dashboard</h2>
      <p>Project tracking, land analysis, planning tools.</p>
    </div>
  )
}

function ContractorView() {
  return (
    <div>
      <h2>Contractor Dashboard</h2>
      <p>Find jobs, manage projects, submit bids.</p>
    </div>
  )
}

function InvestorView() {
  return (
    <div>
      <h2>Investor Dashboard</h2>
      <p>Portfolio tracking, ROI analysis, market insights.</p>
    </div>
  )
}