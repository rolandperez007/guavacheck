import { ThreeElements } from "@react-three/fiber";
import { ReactThreeFiber } from "@react-three/fiber";
import * as THREE from "three";

declare global {
  namespace JSX {
    interface IntrinsicElements extends ReactThreeFiber.IntrinsicElements {}
  }
}
export {};
