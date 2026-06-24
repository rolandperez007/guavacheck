"use client";

import { useParams } from "next/navigation";

export default function EditPropertyPage() {
  const params = useParams();
  const id = params?.id as string;

  return (
    <div>
      <h1>Edit Property</h1>
      <p>Property ID: {id}</p>
    </div>
  );
}