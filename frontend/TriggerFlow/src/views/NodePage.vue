<script setup>
import { ref, markRaw } from "vue";
import { VueFlow, useVueFlow } from "@vue-flow/core";
import { Background } from "@vue-flow/background";
import {
    initialEdges,
    initialNodes,
} from "../components/NodePage/initial-elements.js";
import DropzoneBackground from "../components/NodePage/DropzoneBackground.vue";
import useDragAndDrop from "../components/NodePage/useDnD.js";
import FileReader from "../components/Nodes/FileReader.vue";
import Split from "../components/Nodes/Split.vue";
import Merge from "../components/Nodes/Merge.vue";
import EmailService from "../components/Nodes/EmailService.vue";
import Editor from "../components/Nodes/Editor.vue";
import Comment from "../components/Nodes/Comment.vue";
import Rest from "@/components/Nodes/REST.vue";
import FileUploader from "../components/Nodes/FileUploader.vue";
import Mapping from "../components/Nodes/Mapping.vue";
import MainBar from "../components/NodePage/MainBar.vue";
import Button from "primevue/button";

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


const nodeTypes = {
    filereader: markRaw(FileReader),
    split: markRaw(Split),
    merge: markRaw(Merge),
    email: markRaw(EmailService),
    editor: markRaw(Editor),
    comment: markRaw(Comment),
    rest: markRaw(Rest),
    upload: markRaw(FileUploader),
    mapping: markRaw(Mapping),
};
</script>

<template>
    <div class="flex flex-row background-item">
      <MainBar class="text-white"/>
      <Button icon="pi pi-save" class="bg-white text-black" style="font-size: 4rem" rounded outlined raised text/>
    </div>
    <VueFlow
        :nodes="nodes"
        :edges="edges"
        :nodeTypes="nodeTypes"
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

    
    </VueFlow>
</template>

<style>

.background-item {
    position: absolute;
    top: 10px;
    left: 10px;
    z-index: 1000;
}

</style>