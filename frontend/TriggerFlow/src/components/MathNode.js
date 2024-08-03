import {
  defineNode,
  NumberInterface,
  SelectInterface,
  NodeInterface,
  TextInterface,
  TextInputInterface,
} from "baklavajs";

export const MathNode = defineNode({
  type: "MathNode",
  title: "Math",
  inputs: {
    name: () => new TextInputInterface("Name", "0001").setPort(false),
  },
  outputs: {
    tag: () => new TextInterface("Tag", ""),
  },
  calculate(inputs) {
    return {
      tag: inputs.name,
    };
  },
});
