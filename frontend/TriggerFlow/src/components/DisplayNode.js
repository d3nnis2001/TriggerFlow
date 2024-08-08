import { TextInterface } from "@baklavajs/renderer-vue";
import { defineNode, NodeInterface } from "@baklavajs/core";

export const DisplayNode = defineNode({
  type: "DisplayNode",
  title: "Display",
  inputs: {
    value: () => new NodeInterface("Value", null),
  },
  outputs: {
    display: () => new TextInterface("Display", null),
  },
  calculate(inputs) {
    let code;
    code = inputs.value ? inputs.value : -1;
    return {
      display: code,
    };
  },
});
