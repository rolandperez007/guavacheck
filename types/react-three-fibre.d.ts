import { ReactThreeFiber } from "@react-three/fiber";

declare module "@react-three/fiber" {
  interface ThreeElements extends ReactThreeFiber.IntrinsicElements {}
}
