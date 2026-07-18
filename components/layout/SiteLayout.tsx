"use client";

import { usePathname } from "next/navigation";

import Header from "@/components/navigation/Header";
import Footer from "@/components/navigation/Footer";

interface Props {
  children: React.ReactNode;
}

export default function SiteLayout({
  children,
}: Props) {

  const pathname = usePathname();

  const isGateway = pathname?.startsWith("/gateway");

  return (
    <>
      {!isGateway && <Header />}

      <main>
        {children}
      </main>

      {!isGateway && <Footer />}
    </>
  );
}