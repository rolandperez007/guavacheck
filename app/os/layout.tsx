export default function OSLayout({ children }: { children: React.ReactNode }) {
  return <main className="w-screen h-screen overflow-hidden bg-black">{children}</main>;
}
