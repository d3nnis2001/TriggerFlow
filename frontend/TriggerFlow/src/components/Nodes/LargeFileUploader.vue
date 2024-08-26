<template>
    <div class="card">
        <Toast />
        <FileUpload
            name="demo[]"
            url="/api/upload"
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
import { useToast } from "primevue/usetoast";
import FileUpload from "primevue/fileupload";
const toast = useToast();

const onAdvancedUpload = () => {
    toast.add({
        severity: "info",
        summary: "Success",
        detail: "File Uploaded",
        life: 3000,
    });
};
</script>
