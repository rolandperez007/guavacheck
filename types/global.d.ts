import * as THREE from "three";
import { ReactThreeFiber } from "@react-three/fiber";

declare global {
  namespace JSX {
    interface IntrinsicElements extends ReactThreeFiber.Object3DNode<
      THREE.Object3D,
      typeof THREE.Object3D
    > {}
  }
}

export {};
