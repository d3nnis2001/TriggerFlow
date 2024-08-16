<script setup>
import { Handle, Position } from "@vue-flow/core";
import { NodeResizer } from "@vue-flow/node-resizer";
import "@vue-flow/node-resizer/dist/style.css";

const props = defineProps(["data"]);
</script>

<template>
    <NodeResizer :minWidth="100" :minHeight="50" />
    <Handle type="target" :position="Position.Left" />
    <div class="resizable-node">
        <textarea
            v-model="props.data.label"
            placeholder="Kommentar eingeben"
        ></textarea>
        <div class="color-pickers">
            <input
                type="color"
                v-model="props.data.backgroundColor"
                title="Hintergrundfarbe auswählen"
            />
            <input
                type="color"
                v-model="props.data.textColor"
                title="Textfarbe auswählen"
            />
        </div>
    </div>
    <Handle type="source" :position="Position.Right" />
</template>

<style scoped>
.resizable-node {
    padding: 10px;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
}

textarea {
    flex-grow: 1;
    border: none;
    resize: none;
    background: transparent;
    font-family: sans-serif;
    color: v-bind("props.data.textColor");
}

.color-pickers {
    display: flex;
    gap: 5px;
    margin-top: 5px;
}

.color-pickers input {
    width: 20px;
    height: 20px;
    padding: 0;
    border: none;
    cursor: pointer;
}
</style>
