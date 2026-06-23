"use client"

import { useState } from "react"
import { supabase } from "../../../lib/supabase"

export default function UploadProperty() {

  const [title, setTitle] = useState("")
  const [price, setPrice] = useState("")
  const [location, setLocation] = useState("")

  const uploadProperty = async () => {

    const { error } = await supabase
      .from("properties")
      .insert([
        {
          title,
          price,
          location
        }
      ])

    if (error) {
      alert(error.message)
    } else {
      alert("Property uploaded successfully")
    }
  }

  return (
    <main style={{ padding: 40 }}>

      <h1>Upload Property</h1>

      <input
        placeholder="Property title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        style={{ display: "block", marginTop: 20 }}
      />

      <input
        placeholder="Price"
        value={price}
        onChange={(e) => setPrice(e.target.value)}
        style={{ display: "block", marginTop: 20 }}
      />

      <input
        placeholder="Location"
        value={location}
        onChange={(e) => setLocation(e.target.value)}
        style={{ display: "block", marginTop: 20 }}
      />

      <button
        onClick={uploadProperty}
        style={{ marginTop: 20 }}
      >
        Upload Property
      </button>

    </main>
  )
}
async function uploadImage(file: File) {
  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch("/api/properties/upload", {
    method: "POST",
    body: formData,
  });

  return await res.json();
}




