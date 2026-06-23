"use client";

import { useEffect, useRef } from "react";
import * as THREE from "three";

export default function PropertyScene() {
  const mountRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!mountRef.current) return;

    // -----------------------
    // 1. SCENE
    // -----------------------
    const scene = new THREE.Scene();
    scene.background = new THREE.Color("#0b0f17");

    // -----------------------
    // 2. CAMERA
    // -----------------------
    const camera = new THREE.PerspectiveCamera(
      75,
      window.innerWidth / window.innerHeight,
      0.1,
      1000
    );
    camera.position.z = 5;

    // -----------------------
    // 3. RENDERER
    // -----------------------
    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    mountRef.current.appendChild(renderer.domElement);

    // -----------------------
    // 4. LIGHTS
    // -----------------------
    const light = new THREE.AmbientLight(0xffffff, 1);
    scene.add(light);

    // -----------------------
    // 5. SAMPLE BUILDING (ESCROW BASE OBJECT)
    // -----------------------
    const geometry = new THREE.BoxGeometry(1, 1, 1);
    const material = new THREE.MeshStandardMaterial({ color: "#4ade80" });
    const building = new THREE.Mesh(geometry, material);

    scene.add(building);

    // -----------------------
    // 6. ANIMATION LOOP
    // -----------------------
    const animate = () => {
      requestAnimationFrame(animate);

      building.rotation.y += 0.01;
      building.scale.y = 1 + Math.sin(Date.now() * 0.001) * 0.2;

      renderer.render(scene, camera);
    };

    animate();

    // -----------------------
    // CLEANUP
    // -----------------------
    return () => {
      mountRef.current?.removeChild(renderer.domElement);
    };
  }, []);

  return <div ref={mountRef} />;
}









