<script lang="js" setup>
import { Handle, Position } from "@vue-flow/core";
import { ref } from "vue";

const filePath = ref("");
const valueHandler = ref([]);
const restOperations = [
    {
        value: "get",
        label: "GET",
    },
    {
        value: "post",
        label: "POST",
    },
    {
        value: "put",
        label: "PUT",
    },
    {
        value: "delete",
        label: "DELETE",
    },
];
</script>

<template>
    <div class="custom-node">
        <Handle type="target" :position="Position.Top" />
        <h2 style="color: black">REST Handler</h2>
        <h4 style="color: black">Handler</h4>
        <ElCascader
            v-model="valueHandler"
            :options="restOperations"
            placeholder="Wählen Sie eine REST Operation"
        />
        <div class="file-input-container">
            <input type="text" v-model="filePath" placeholder="REST URL" />
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
