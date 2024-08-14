<script setup>
import { Handle, Position, useVueFlow } from "@vue-flow/core";
import { ref, computed, watch } from "vue";

const props = defineProps(["id"]);
const { findNode, removeEdges, edges } = useVueFlow();

const outputCount = ref(2);

const outputOptions = [
    { value: 2, label: "2 Outputs" },
    { value: 3, label: "3 Outputs" },
    { value: 4, label: "4 Outputs" },
];

const handles = computed(() => {
    const baseHandles = [
        { id: "output-1", position: Position.Bottom, style: { left: "33%" } },
        { id: "output-2", position: Position.Bottom, style: { left: "66%" } },
    ];

    if (outputCount.value >= 3) {
        baseHandles.push({
            id: "output-3",
            position: Position.Bottom,
            style: { left: "0%" },
        });
    }

    if (outputCount.value >= 4) {
        baseHandles.push({
            id: "output-4",
            position: Position.Bottom,
            style: { left: "100%" },
        });
    }

    return baseHandles;
});

const removeConnectedEdges = () => {
    const node = findNode(props.id);
    if (node) {
        const connectedEdges = edges.value.filter(
            (edge) => edge.source === props.id || edge.target === props.id,
        );
        removeEdges(connectedEdges);
    }
};

watch(outputCount, removeConnectedEdges);
removeConnectedEdges();
</script>

<template>
    <div class="custom-node split-node">
        <Handle type="target" :position="Position.Top" />
        <h2 style="color: black">Split</h2>
        <div class="output-selector">
            <el-cascader
                v-model="outputCount"
                :options="outputOptions"
                placeholder="Select number of outputs"
            />
        </div>
        <Handle
            v-for="handle in handles"
            :key="handle.id"
            type="source"
            :id="handle.id"
            :position="handle.position"
            :style="handle.style"
        />
    </div>
</template>

<style scoped>
.custom-node.split-node {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 200px;
    padding: 1rem;
    background: white;
    border: 1px solid black;
    border-radius: 4px;
}
.output-selector {
    margin-top: 1rem;
    width: 100%;
}
</style>
