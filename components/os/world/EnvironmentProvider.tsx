"use client";

import { WorldProvider } from "./WorldProvider";

export default function EnvironmentProvider({

  children,

}: {

  children: React.ReactNode;

}) {

  return (

    <WorldProvider>

      {children}

    </WorldProvider>

  );

}