"use client"

import { useState } from "react"
import { supabase } from "../../lib/supabase"

export default function Upload() {

  const [title, setTitle] = useState("")
  const [price, setPrice] = useState("")
  const [location, setLocation] = useState("")
  const [image, setImage] = useState(null)

  const uploadProperty = async () => {

    const { data: userData } = await supabase.auth.getUser()

    const user = userData.user

    if (!user) {
      alert("User not logged in")
      return
    }

    let imageUrl = ""

    // Upload image first
    if (image) {

      const fileName = `${Date.now()}-${image.name}`

      const { error: imageError } = await supabase.storage
        .from("property-images")
        .upload(fileName, image)

      if (imageError) {
        alert(imageError.message)
        return
      }

      const { data } = supabase.storage
        .from("property-images")
        .getPublicUrl(fileName)

      imageUrl = data.publicUrl
    }

    // Insert property into database
    const { error } = await supabase
      .from("properties")
      .insert([
        {
          title,
          price,
          location,
          image_url: imageUrl,
          user_id: user.id
        }
      ])

    if (error) {
      console.log(error)
      alert(error.message)
    } else {

      alert("Property uploaded successfully")

      setTitle("")
      setPrice("")
      setLocation("")
      setImage(null)
    }
  }

  return (
    <main style={{ padding: 40 }}>

      <h1>Upload Property</h1>

      <input
        placeholder="Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />

      <br /><br />

      <input
        placeholder="Price"
        value={price}
        onChange={(e) => setPrice(e.target.value)}
      />

      <br /><br />

      <input
        placeholder="Location"
        value={location}
        onChange={(e) => setLocation(e.target.value)}
      />

      <br /><br />

      <input
        type="file"
        onChange={(e) => setImage(e.target.files[0])}
      />

      <br /><br />

      <button onClick={uploadProperty}>
        Submit Property
      </button>

    </main>
  )
}

    