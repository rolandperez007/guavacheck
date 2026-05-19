"use client"

import { useEffect } from "react"
import { supabase } from "@/lib/supabase"

export default function TestSupabase() {

  useEffect(() => {
    const test = async () => {
      const { data, error } = await supabase.from("properties").select("*")
      console.log("DATA:", data)
      console.log("ERROR:", error)
    }

    test()
  }, [])

  return (
    <main style={{ padding: 40 }}>
      <h1>Supabase Test Running...</h1>
      <p>Check browser console</p>
    </main>
  )
}
