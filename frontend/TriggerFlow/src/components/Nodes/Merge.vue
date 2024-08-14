<script setup>
import { Handle, Position, useVueFlow } from "@vue-flow/core";
import { ref, computed, watch } from "vue";

const props = defineProps(["id"]);
const { findNode, removeEdges, edges } = useVueFlow();

const inputCount = ref(2);

const inputOptions = [
    { value: 2, label: "2 Inputs" },
    { value: 3, label: "3 Inputs" },
    { value: 4, label: "4 Inputs" },
];

const handles = computed(() => {
    const baseHandles = [
        { id: "input-1", position: Position.Top, style: { left: "33%" } },
        { id: "input-2", position: Position.Top, style: { left: "66%" } },
    ];
    if (inputCount.value >= 3) {
        baseHandles.push({
            id: "input-3",
            position: Position.Top,
            style: { left: "0%" },
        });
    }
    if (inputCount.value >= 4) {
        baseHandles.push({
            id: "input-4",
            position: Position.Top,
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

watch(inputCount, removeConnectedEdges);
removeConnectedEdges();
</script>

<template>
    <div class="custom-node merge-node">
        <Handle
            v-for="handle in handles"
            :key="handle.id"
            type="target"
            :id="handle.id"
            :position="handle.position"
            :style="handle.style"
        />
        <h2 style="color: black">Merge</h2>
        <div class="input-selector">
            <el-cascader
                v-model="inputCount"
                :options="inputOptions"
                placeholder="Select number of inputs"
            />
        </div>
        <Handle type="source" :position="Position.Bottom" />
    </div>
</template>

<style scoped>
.custom-node.merge-node {
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
.input-selector {
    margin-top: 1rem;
    width: 100%;
}
</style>
