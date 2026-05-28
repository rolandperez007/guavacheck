"use client"

import { useEffect, useState } from "react"
import { supabase } from "../../lib/supabase"

export default function MyProperties() {

  const [properties, setProperties] = useState([])

  useEffect(() => {

    const fetchMyProperties = async () => {

      const { data: userData } = await supabase.auth.getUser()
      const user = userData.user

      const { data, error } = await supabase
        .from("properties")
        .select("*")
        .eq("user_id", user?.id)
        .order("created_at", { ascending: false })

      if (!error) {
        setProperties(data || [])
      }

    }

    fetchMyProperties()

  }, [])

  return (
    <main style={{ padding: 40 }}>

      <h1>My Properties</h1>

      {properties.length === 0 ? (
        <p>No properties uploaded yet</p>
      ) : (
        properties.map((item) => (
          <div
            key={item.id}
            style={{
              border: "1px solid #ddd",
              padding: 10,
              marginBottom: 10
            }}
          >
            <h3>{item.title}</h3>
            <p>Price: {item.price}</p>
            <p>Location: {item.location}</p>
          </div>
        ))
      )}

    </main>
  )
}