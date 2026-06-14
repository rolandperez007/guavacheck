import React from "react";
import { useAustinStream } from "../hooks/useAustinStream";
import { austinAnimator } from "../animations/austinAnimator";

export default function AustinPanel() {

    const event = useAustinStream();
    const animation = austinAnimator(event);

    return (
        <div style={{ padding: 20, color: "white" }}>

            <h2>Austin Live Engine</h2>

            <pre>
                {JSON.stringify(event, null, 2)}
            </pre>

            <hr />

            <h3>Animation State</h3>

            <pre>
                {JSON.stringify(animation, null, 2)}
            </pre>

        </div>
    );
}