"use client"

import { useState } from "react"
import { supabase } from "../../lib/supabase"
import { useRouter } from "next/navigation"

export default function Onboarding() {

  const router = useRouter()
  const [role, setRole] = useState("")
  const [currency, setCurrency] = useState("USD")
  const [language, setLanguage] = useState("en")

  const saveProfile = async () => {

    const { data: userData } = await supabase.auth.getUser()
    const user = userData.user

    if (!user) return

    await supabase.from("profiles").upsert({
      id: user.id,
      role,
      preferred_currency: currency,
      preferred_language: language
    })

    router.push("/properties")
  }

  return (
    <main style={{ padding: 40 }}>

      <h1>Setup Your Account</h1>

      <h3>Select Role</h3>
      <select onChange={(e) => setRole(e.target.value)}>
        <option>Buyer</option>
        <option>Agent</option>
        <option>Developer</option>
        <option>Contractor</option>
        <option>Investor</option>
      </select>

      <h3>Currency</h3>
      <select onChange={(e) => setCurrency(e.target.value)}>
        <option>USD</option>
        <option>EUR</option>
        <option>GBP</option>
        <option>NGN</option>
        <option>BTC</option>
      </select>

      <h3>Language</h3>
      <select onChange={(e) => setLanguage(e.target.value)}>
        <option>en</option>
        <option>fr</option>
        <option>es</option>
        <option>zh</option>
        <option>ar</option>
      </select>

      <br /><br />

      <button onClick={saveProfile}>
        Continue
      </button>

    </main>
  )
}
