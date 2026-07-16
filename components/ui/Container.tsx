import { ReactNode } from "react";

interface ContainerProps {
  children: ReactNode;
}

export default function Container({
  children,
}: ContainerProps) {
  return (
    <div
      style={{
        maxWidth: 1320,
        margin: "0 auto",
        padding: "0 24px",
        width: "100%",
      }}
    >
      {children}
    </div>
  );
}