<script lang="js" setup>
import { Handle, Position } from "@vue-flow/core";
import LargeFileUpload from "./SubComponents/LargeFileUploader.vue";
import { ref } from "vue";

const uploadedFiles = ref([]);

const handleFileUploaded = (file) => {
    uploadedFiles.value.push(file);
    console.log("Neue Datei:", file);
    // API CALL hier
};
</script>

<template>
    <div class="custom-node">
        <Handle type="target" :position="Position.Top" />
        <h2 class="text-black">File Uploader</h2>
        <LargeFileUpload @file-uploaded="handleFileUploaded" />
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
</style>
