"use client"

import { useEffect, useState } from "react"
import { supabase } from "../../lib/supabase"

export default function Properties() {

  const [properties, setProperties] = useState([])

  useEffect(() => {

    const fetchProperties = async () => {

      const { data, error } = await supabase
        .from("properties")
        .select("*")
        .order("created_at", { ascending: false })

      if (!error) {
        setProperties(data)
      }

    }

    fetchProperties()

  }, [])

  return (
    <main style={{
      padding: 40,
      display: "grid",
      gridTemplateColumns: "repeat(auto-fit, minmax(300px, 1fr))",
      gap: 20
    }}>

      {properties.map((item) => (

        <div
          key={item.id}
          style={{
            border: "1px solid #ddd",
            borderRadius: 10,
            overflow: "hidden",
            background: "#fff"
          }}
        >

          {item.image_url && (
            <img
              src={item.image_url}
              alt={item.title}
              style={{
                width: "100%",
                height: 220,
                objectFit: "cover"
              }}
            />
          )}

          <div style={{ padding: 15 }}>

            <h2>{item.title}</h2>

            <p>
              <strong>Price:</strong> {item.price}
            </p>

            <p>
              <strong>Location:</strong> {item.location}
            </p>

          </div>

        </div>

      ))}

    </main>
  )
}