import { Background } from "@vue-flow/background";
import { MarkerType } from "@vue-flow/core";

export const initialNodes = [
  {
    id: "6",
    type: "filereader",
    data: { label: "Node 6" },
    position: { x: 400, y: 400 },
    class: "light",
  },
  {
    id: "7",
    type: "split",
    data: { label: "Node 7" },
    position: { x: 800, y: 800 },
    class: "light",
  },
];

export const initialEdges = [];
