"use client"

import { useState } from "react"
import { supabase } from "../../lib/supabase"

export default function AuthPage() {

  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")

  const signUp = async () => {

    const { error } = await supabase.auth.signUp({
      email,
      password
    })

    if (error) {
      alert(error.message)
    } else {
      alert("Signup successful")
    }
  }

  const login = async () => {

    const { error } = await supabase.auth.signInWithPassword({
      email,
      password
    })

    if (error) {
      alert(error.message)
    } else {
      alert("Login successful")
    }
  }

  return (
    <main style={{ padding: 40 }}>

      <h1>GuavaCheck Auth</h1>

      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />

      <br /><br />

      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />

      <br /><br />

      <button onClick={signUp}>
        Sign Up
      </button>

      <button
        onClick={login}
        style={{ marginLeft: 10 }}
      >
        Login
      </button>

    </main>
  )
}
