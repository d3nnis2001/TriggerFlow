<script setup>
import { ref, onMounted, onUnmounted } from "vue";
import { Handle, Position } from "@vue-flow/core";

const props = defineProps({
    data: {
        type: Object,
        required: true,
    },
});

const emit = defineEmits(["updateNode"]);

const comment = ref(props.data.comment || "");
const width = ref(props.data.width || 200);
const height = ref(props.data.height || 100);
const backgroundColor = ref(props.data.backgroundColor || "#FFFFFF");

const isResizing = ref(false);
const startX = ref(0);
const startY = ref(0);
const startWidth = ref(0);
const startHeight = ref(0);

const updateNode = () => {
    emit("updateNode", {
        comment: comment.value,
        width: width.value,
        height: height.value,
        backgroundColor: backgroundColor.value,
    });
};

const startResize = (e) => {
    isResizing.value = true;
    startX.value = e.clientX;
    startY.value = e.clientY;
    startWidth.value = width.value;
    startHeight.value = height.value;
    document.addEventListener("mousemove", resize);
    document.addEventListener("mouseup", stopResize);
};

const resize = (e) => {
    if (!isResizing.value) return;
    const newWidth = startWidth.value + e.clientX - startX.value;
    const newHeight = startHeight.value + e.clientY - startY.value;
    width.value = Math.max(100, newWidth);
    height.value = Math.max(50, newHeight);
    updateNode();
};

const stopResize = () => {
    isResizing.value = false;
    document.removeEventListener("mousemove", resize);
    document.removeEventListener("mouseup", stopResize);
};

onMounted(() => {
    document.addEventListener("mousemove", resize);
    document.addEventListener("mouseup", stopResize);
});

onUnmounted(() => {
    document.removeEventListener("mousemove", resize);
    document.removeEventListener("mouseup", stopResize);
});
</script>

<template>
    <div
        class="resizable-comment-node"
        :style="{
            width: `${width}px`,
            height: `${height}px`,
            backgroundColor: backgroundColor,
        }"
    >
        <Handle type="target" :position="Position.Top" />
        <textarea
            v-model="comment"
            @input="updateNode"
            :style="{ width: '100%', height: 'calc(100% - 40px)' }"
            placeholder="Kommentar eingeben"
        ></textarea>
        <div class="color-picker">
            <input
                type="color"
                v-model="backgroundColor"
                @input="updateNode"
                title="Hintergrundfarbe auswählen"
            />
        </div>
        <div class="resize-handle" @mousedown="startResize"></div>
        <Handle type="source" :position="Position.Bottom" />
    </div>
</template>

<style scoped>
.resizable-comment-node {
    position: relative;
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 10px;
    min-width: 100px;
    min-height: 50px;
    overflow: hidden;
}

textarea {
    border: none;
    resize: none;
    background: transparent;
}

.color-picker {
    position: absolute;
    bottom: 5px;
    left: 5px;
}

.color-picker input {
    width: 30px;
    height: 30px;
    padding: 0;
    border: none;
    cursor: pointer;
}

.resize-handle {
    position: absolute;
    right: 0;
    bottom: 0;
    width: 10px;
    height: 10px;
    cursor: se-resize;
    background: #ddd;
}
</style>
