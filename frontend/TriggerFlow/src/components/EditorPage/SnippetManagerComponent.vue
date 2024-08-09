<template>
    <el-drawer
        v-model="visible"
        title="Code Snippets"
        size="30%"
        :before-close="handleClose"
    >
        <el-scrollbar height="calc(100vh - 200px)">
            <el-list v-if="snippets.length">
                <el-list-item v-for="snippet in snippets" :key="snippet.name">
                    <el-row :gutter="20" style="width: 100%">
                        <el-col :span="16">
                            <span>{{ snippet.name }}</span>
                        </el-col>
                        <el-col :span="8" class="text-right">
                            <el-button
                                size="small"
                                @click="loadSnippet(snippet)"
                                >Load</el-button
                            >
                            <el-button
                                size="small"
                                type="danger"
                                @click="deleteSnippet(snippet)"
                                >Delete</el-button
                            >
                        </el-col>
                    </el-row>
                </el-list-item>
            </el-list>
            <el-empty v-else description="No snippets found" />
        </el-scrollbar>

        <template #footer>
            <el-input
                v-model="newSnippetName"
                placeholder="New snippet name"
                style="margin-bottom: 10px"
            >
                <template #append>
                    <el-button @click="saveNewSnippet">Save</el-button>
                </template>
            </el-input>
        </template>
    </el-drawer>
</template>

<script>
import { ref, onMounted } from "vue";
import { ElMessage } from "element-plus";
import { getCodeSnippets, saveCodeSnippet } from "../../api/editor";

export default {
    props: {
        currentCode: String,
        modelValue: Boolean,
    },
    emits: ["update:modelValue", "load-snippet"],
    setup(props, { emit }) {
        const snippets = ref([]);
        const newSnippetName = ref("");
        const visible = ref(props.modelValue);

        onMounted(async () => {
            try {
                snippets.value = await getCodeSnippets();
            } catch (error) {
                console.error("Failed to fetch snippets:", error);
                ElMessage.error("Failed to load snippets");
            }
        });

        async function saveNewSnippet() {
            if (newSnippetName.value) {
                try {
                    await saveCodeSnippet(
                        newSnippetName.value,
                        props.currentCode,
                    );
                    snippets.value = await getCodeSnippets(); // Refresh list
                    newSnippetName.value = "";
                    ElMessage.success("Snippet saved successfully");
                } catch (error) {
                    console.error("Failed to save snippet:", error);
                    ElMessage.error("Failed to save snippet");
                }
            }
        }

        async function deleteSnippet(snippet) {
            try {
                //await deleteCodeSnippet(snippet.name);
                //snippets.value = await getCodeSnippets(); // Refresh list
                ElMessage.success("Snippet deleted successfully");
            } catch (error) {
                console.error("Failed to delete snippet:", error);
                ElMessage.error("Failed to delete snippet");
            }
        }

        function loadSnippet(snippet) {
            emit("load-snippet", snippet.code);
            ElMessage.success("Snippet loaded successfully");
        }

        function handleClose(done) {
            emit("update:modelValue", false);
            done();
        }

        return {
            snippets,
            newSnippetName,
            visible,
            saveNewSnippet,
            deleteSnippet,
            loadSnippet,
            handleClose,
        };
    },
};
</script>

<style scoped>
.text-right {
    text-align: right;
}
</style>
