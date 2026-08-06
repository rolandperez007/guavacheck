const events = [
  "New property verified",

  "Mortgage approved",

  "Construction milestone reached",

  "Investor joined marketplace",

  "Property listed",

  "Drone survey completed",

  "Austin completed valuation",

  "Title verification completed",

  "Market confidence increased",

  "Currency updated",
];

export function randomEvent() {
  return events[Math.floor(Math.random() * events.length)];
}
