"use client";

import { useAuth } from "@/contexts/AuthContext";
import { useRouter } from "next/navigation";
import { useEffect } from "react";

export default function RoleGuard({
  children,
  role,
}) {

  const { user, profile, loading } = useAuth();
  const router = useRouter();

  useEffect(() => {

    if (!loading) {

      if (!user) {
        router.push("/auth");
      }

      else if (profile?.role !== role) {
        router.push("/unauthorized");
      }

    }

  }, [user, profile, loading]);

  if (loading) {
    return <div>Loading...</div>;
  }

  return children;
}
