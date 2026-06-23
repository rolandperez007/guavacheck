export function austinAnimator(event: any) {

    if (!event) return null;

    switch (event.event) {

        case "ui.austin.thinking":
            return {
                type: "pulse",
                intensity: "medium",
                message: event.payload.message
            };

        case "ui.escrow.update":
            return {
                type: "progress",
                value: event.payload.progress
            };

        case "ui.milestone.update":
            return {
                type: "build_stage",
                phase: event.payload.phase
            };

        default:
            return {
                type: "idle"
            };
    }
}






