const { generateFloorplan } = require("./lib/floorplanEngine.js");

console.log(
  generateFloorplan({ type: "flat", floors: 1 })
);