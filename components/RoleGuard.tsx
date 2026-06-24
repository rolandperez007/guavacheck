"use client";

import { ReactNode, useEffect, useState } from "react";

// TEMP fallback auth (prevents build crashes)
function getMockUser() {
  if (typeof window === "undefined") return null;

  const raw = localStorage.getItem("user");
  if (!raw) return null;

  try {
    return JSON.parse(raw);
  } catch {
    return null;
  }
}

interface RoleGuardProps {
  role: string;
  children: ReactNode;
}

export default function RoleGuard({ role, children }: RoleGuardProps) {
  const [user, setUser] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const u = getMockUser();
    setUser(u);
    setLoading(false);
  }, []);

  if (loading) return null;

  if (!user) {
    return <p>Not authenticated</p>;
  }

  if (user.role !== role) {
    return <p>Access denied: insufficient permissions</p>;
  }

  return <>{children}</>;
}