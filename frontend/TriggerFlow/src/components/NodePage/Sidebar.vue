<script setup>
import { ref } from "vue";
import useDragAndDrop from "./useDnD";

const { onDragStart } = useDragAndDrop();
const isOpen = ref(true);

const toggleSidebar = () => {
    isOpen.value = !isOpen.value;
};
</script>

<template>
    <aside :class="{ 'sidebar-closed': !isOpen }">
        <button @click="toggleSidebar" class="toggle-btn">
            {{ isOpen ? ">>" : "<<" }}
        </button>
        <div v-if="isOpen" class="sidebar-content">
            <div class="description">Node Auswahl</div>

            <div class="nodes">
                <div
                    class="vue-flow__node-output"
                    :draggable="true"
                    @dragstart="onDragStart($event, 'filereader')"
                >
                    File Reader
                </div>
                <div
                    class="vue-flow__node-output"
                    :draggable="true"
                    @dragstart="onDragStart($event, 'split')"
                >
                    Split
                </div>
                <div
                    class="vue-flow__node-output"
                    :draggable="true"
                    @dragstart="onDragStart($event, 'merge')"
                >
                    Merge
                </div>
                <div
                    class="vue-flow__node-output"
                    :draggable="true"
                    @dragstart="onDragStart($event, 'email')"
                >
                    E-Mail Service
                </div>
                <div
                    class="vue-flow__node-output"
                    :draggable="true"
                    @dragstart="onDragStart($event, 'editor')"
                >
                    Editor
                </div>
                <div
                    class="vue-flow__node-output"
                    :draggable="true"
                    @dragstart="onDragStart($event, 'comment')"
                >
                    Kommentar
                </div>
                <div
                    class="vue-flow__node-output"
                    :draggable="true"
                    @dragstart="onDragStart($event, 'rest')"
                >
                    REST Operation
                </div>
                <div
                    class="vue-flow__node-output"
                    :draggable="true"
                    @dragstart="onDragStart($event, 'upload')"
                >
                    File Uploader
                </div>
                <div
                    class="vue-flow__node-output"
                    :draggable="true"
                    @dragstart="onDragStart($event, 'mapping')"
                >
                    Mapping
                </div>
            </div>
        </div>
    </aside>
</template>

<style scoped>
aside {
    position: absolute;
    color: #000000;
    right: 0;
    top: 0;
    bottom: 0;
    width: 200px;
    background-color: #f8f8f8;
    padding: 10px;
    transition: transform 0.3s ease;
}

.sidebar-closed {
    transform: translateX(190px);
}

.toggle-btn {
    position: absolute;
    left: -30px;
    top: 10px;
    background-color: #f8f8f8;
    border: none;
    padding: 5px 10px;
    cursor: pointer;
}

.sidebar-content {
    overflow-y: auto;
    height: 100%;
}

.description {
    margin-bottom: 10px;
}

.nodes > div {
    margin-bottom: 10px;
    padding: 10px;
    border: 1px solid #ccc;
    cursor: grab;
}
</style>
