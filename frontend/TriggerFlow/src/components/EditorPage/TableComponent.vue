<template>
    <div class="resizable-table-container" ref="container">
        <vue-good-table
            :columns="columns"
            :rows="rows"
            :sort-options="{ enabled: true }"
            :pagination-options="{ enabled: true, perPage: 10 }"
            style="width: 100%"
        >
        </vue-good-table>
        <div class="resize-handle" ref="handle" @mousedown="startResize"></div>
    </div>
</template>

<script>
import { VueGoodTable } from "vue-good-table-next";
import "vue-good-table-next/dist/vue-good-table-next.css";

export default {
    components: { VueGoodTable },
    data() {
        return {
            columns: [
                { label: "Name", field: "name" },
                { label: "Alter", field: "age", type: "number" },
                { label: "Stadt", field: "city" },
            ],
            rows: [
                { name: "John", age: 30, city: "New York" },
                { name: "Jane", age: 25, city: "San Francisco" },
                { name: "Tom", age: 35, city: "London" },
            ],
            isDragging: false,
            startY: 0,
            startHeight: 0,
        };
    },
    methods: {
        startResize(e) {
            this.isDragging = true;
            this.startY = e.clientY;
            this.startHeight = this.$refs.container.offsetHeight;
            document.addEventListener("mousemove", this.resize);
            document.addEventListener("mouseup", this.stopResize);
        },
        resize(e) {
            if (!this.isDragging) return;
            const deltaY = e.clientY - this.startY;
            const newHeight = this.startHeight + deltaY;
            this.$refs.container.style.height = `${newHeight}px`;
        },
        stopResize() {
            this.isDragging = false;
            document.removeEventListener("mousemove", this.resize);
            document.removeEventListener("mouseup", this.stopResize);
        },
    },
    mounted() {
        this.$refs.container.style.height = "400px"; // Anfangshöhe
    },
};
</script>

<style scoped>
.resizable-table-container {
    position: relative;
    overflow: hidden;
    min-height: 200px;
    resize: vertical;
}
.resize-handle {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 10px;
    background-color: #ccc;
    cursor: ns-resize;
}
.resize-handle:hover {
    background-color: #999;
}
</style>
