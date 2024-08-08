import {
  TextInterface,
    FileInterface,
  TextInputInterface,
} from "@baklavajs/renderer-vue";

import { defineNode } from "@baklavajs/core";

export const MathNode = defineNode({
  type: "MathNode",
  title: "Math",
  inputs: {
    name:() => new FileInterface(),
  },
  outputs: {
  },
  calculate(inputs) {
    return {
      tag: inputs.name,
    };
  },
});
