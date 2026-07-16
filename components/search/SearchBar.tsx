"use client";

export default function SearchBar() {
  return (
    <input
      type="search"
      placeholder="Search guavacheck..."
      style={{
        width: 350,
        padding: "10px 16px",
        borderRadius: 12,
        border: "1px solid #d1d5db",
      }}
    />
  );
}