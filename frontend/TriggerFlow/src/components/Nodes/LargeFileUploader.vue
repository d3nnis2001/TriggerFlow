<template>
    <div class="card">
        <Toast />
        <FileUpload
            name="demo[]"
            url="/api/nodes/uploadFiles"
            @upload="onAdvancedUpload($event)"
            :multiple="true"
            accept=".pdf,.csv,.xls,.xlsx"
            :maxFileSize="500000000"
        >
            <template #empty>
                <span>Drag and drop files to here to upload.</span>
            </template>
        </FileUpload>
    </div>
</template>

<script setup>
import FileUpload from "primevue/fileupload";
import { uploadFiles } from "../../api/nodes.js";

const onAdvancedUpload = () => {
    const files = event.files;
    const formData = new FormData();

    files.forEach((file) => {
        formData.append("files", file);
    });
    uploadFiles(formData);
};
</script>
