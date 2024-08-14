<script setup>
import { ref } from "vue";
import { VueFlow, useVueFlow } from "@vue-flow/core";
import { Background } from "@vue-flow/background";
import { ControlButton, Controls } from "@vue-flow/controls";
import { MiniMap } from "@vue-flow/minimap";
import {
    initialEdges,
    initialNodes,
} from "../components/NodePage/initial-elements.js";
import Icon from "../components/NodePage/Icon.vue";
import DropzoneBackground from "../components/NodePage/DropzoneBackground.vue";
import Sidebar from "../components/NodePage/Sidebar.vue";
import useDragAndDrop from "../components/NodePage/useDnD.js";

const { onInit, onNodeDragStop, onConnect, addEdges, setViewport, toObject } =
    useVueFlow();

const { onDragOver, onDrop, onDragLeave, isDragOver } = useDragAndDrop();

const nodes = ref(initialNodes);

const edges = ref(initialEdges);

const dark = ref(false);

onInit((vueFlowInstance) => {
    vueFlowInstance.fitView();
});

onNodeDragStop(({ event, nodes, node }) => {
    console.log("Node Drag Stop", { event, nodes, node });
});

onConnect((connection) => {
    addEdges(connection);
});

function updatePos() {
    nodes.value = nodes.value.map((node) => {
        return {
            ...node,
            position: {
                x: Math.random() * 400,
                y: Math.random() * 400,
            },
        };
    });
}

function logToObject() {
    console.log(toObject());
}

function resetTransform() {
    setViewport({ x: 0, y: 0, zoom: 1 });
}

function toggleDarkMode() {
    dark.value = !dark.value;
}
</script>

<template>
    <VueFlow
        :nodes="nodes"
        :edges="edges"
        :class="{ dark }"
        class="basic-flow"
        :default-viewport="{ zoom: 1.5 }"
        :min-zoom="0.2"
        :max-zoom="4"
        @dragover="onDragOver"
        @dragleave="onDragLeave"
        @drop="onDrop"
    >
        <DropzoneBackground
            :style="{
                backgroundColor: isDragOver ? '#e7f3ff' : 'transparent',
                transition: 'background-color 0.2s ease',
            }"
        >
            <p v-if="isDragOver">Drop here</p>
        </DropzoneBackground>
        <Background pattern-color="#aaa" :gap="16" />

        <MiniMap />

        <Controls position="top-left">
            <ControlButton title="Reset Transform" @click="resetTransform">
                <Icon name="reset" />
            </ControlButton>

            <ControlButton title="Shuffle Node Positions" @click="updatePos">
                <Icon name="update" />
            </ControlButton>

            <ControlButton title="Toggle Dark Mode" @click="toggleDarkMode">
                <Icon v-if="dark" name="sun" />
                <Icon v-else name="moon" />
            </ControlButton>

            <ControlButton title="Log `toObject`" @click="logToObject">
                <Icon name="log" />
            </ControlButton>
        </Controls>
    </VueFlow>
    <Sidebar />
</template>
