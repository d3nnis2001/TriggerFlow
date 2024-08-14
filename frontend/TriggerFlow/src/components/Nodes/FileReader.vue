<script lang="js" setup>
import { Handle, Position } from "@vue-flow/core";
import { ref } from "vue";
import { getFilereader } from "../../api/nodes";

const filePath = ref("");
const valueHandler = ref([]);
const from = ref("");
const till = ref("");
const firstRowHeading = ref(true);
const handlerOptions = [
    {
        value: "pdf",
        label: "PDF",
    },
    {
        value: "csv",
        label: "CSV",
    },
    {
        value: "excel",
        label: "Excel",
    },
    {
        value: "fixedcol",
        label: "Fixed Column",
    },
];
</script>

<template>
    <div class="custom-node">
        <Handle type="target" :position="Position.Top" />
        <h2 style="color: black">File Reader</h2>
        <div class="file-input-container">
            <input type="text" v-model="filePath" placeholder="Dateipfad" />
        </div>
        <h4 style="color: black">Handler</h4>
        <ElCascader
            v-model="valueHandler"
            :options="handlerOptions"
            placeholder="Wählen Sie einen Handler"
        />
        <el-checkbox v-model="firstRowHeading"
            >Erste Zeile Überschrift</el-checkbox
        >
        <h4 style="color: black">Teilselektion</h4>
        <div class="fromtill">
            <input type="text" v-model="from" placeholder="Von Zeile" />
            <input type="text" v-model="till" placeholder="Bis Zeile" />
        </div>
        <Handle type="source" :position="Position.Bottom" />
    </div>
</template>

<style scoped>
.custom-node {
    display: flex;
    flex-direction: column;
    height: 100%;
    justify-content: space-around;
    width: 100%;
    padding: 1rem;
    background: white;
    border: 1px solid black;
    border-radius: 4px;
}
.fromtill {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
}
.file-input-container {
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 10px;
}
input[type="text"] {
    flex-grow: 1;
    padding: 5px;
    border: 1px solid #ccc;
    border-radius: 4px;
}
.file-button {
    background: none;
    border: none;
    cursor: pointer;
    font-size: 1.2rem;
}
</style>
