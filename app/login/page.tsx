"use client";

import { useState } from "react";
import { supabase } from "@/lib/supabase";
import { useRouter } from "next/navigation";

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const router = useRouter();

  async function signIn() {
    const { error } = await supabase.auth.signInWithPassword({
      email,
      password,
    });

    if (error) return alert(error.message);

    router.push("/dashboard");
  }

  async function signUp() {
    const { error } = await supabase.auth.signUp({
      email,
      password,
    });

    if (error) return alert(error.message);

    alert("Check email or login now");
  }

  return (
    <div style={{ padding: 30, maxWidth: 400 }}>
      <h1>Login</h1>

      <input
        placeholder="Email"
        onChange={(e) => setEmail(e.target.value)}
        style={{ display: "block", margin: 10 }}
      />

      <input
        placeholder="Password"
        type="password"
        onChange={(e) => setPassword(e.target.value)}
        style={{ display: "block", margin: 10 }}
      />

      <button onClick={signIn}>Login</button>
      <button onClick={signUp} style={{ marginLeft: 10 }}>
        Sign Up
      </button>
    </div>
  );
}
