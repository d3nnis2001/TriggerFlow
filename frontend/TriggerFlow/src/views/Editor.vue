<template>
    <div class="main-container">
        <div class="top-buttons">
            <div class="play-button">
                <button @click="runTheCode">
                    <i class="pi pi-code"></i>
                </button>
            </div>
            <div class="play-button">
                <button @click="openSnippetManager">
                    <i class="pi pi-save"></i>
                </button>
            </div>
            <div class="play-button">
                <button @click="refreshOutput">
                    <i class="pi pi-refresh"></i>
                </button>
            </div>
        </div>
        <div class="card flex justify-start">
            <ToggleSwitch v-model="checked" />
        </div>
        <div class="top-section">
            <div v-if="checked===false" class="editor-container">
                <EditorComponent v-model="code" @scroll="handleEditorScroll" />
                <div class="resizer" ref="resizer"></div>
                <OutputComponent
                    :outputs="outputs"
                    :editor-scroll-top="editorScrollTop"
                />
            </div>
            <div v-else>
                <Playground ref="playground"/>
            </div>
            <RightPanelComponent :codeSnippets="docsFunctions" @drag-start="onDragStart"/>
        </div>
        <div class="bottom-section">
            <table-component :data="tableData"></table-component>
        </div>
    </div>
</template>

<script>
import { onMounted, ref, watch } from "vue";
import EditorComponent from "../components/EditorPage/EditorComponent.vue";
import OutputComponent from "../components/EditorPage/OutputComponent.vue";
import SnippetManagerComponent from "../components/EditorPage/SnippetManagerComponent.vue";
import RightPanelComponent from "../components/EditorPage/RightPanelComponent.vue";
import TableComponent from "../components/EditorPage/TableComponent.vue";
import { runCode as apiRunCode } from "../api/editor";
import docsFunctions from "../assets/docs";
import { useRoute } from "vue-router";
import Papa from "papaparse";
import ToggleSwitch from 'primevue/toggleswitch';
import Playground from "../components/EditorPage/SnippetPlayground.vue"

export default {
    components: {
        EditorComponent,
        OutputComponent,
        RightPanelComponent,
        TableComponent,
        SnippetManagerComponent,
        ToggleSwitch,
        Playground
    },
    setup() {
        const code = ref("");
        const outputs = ref([]);
        const editorScrollTop = ref(0);
        const resizer = ref(null);
        const outputContainer = ref(null);
        const showSnippetManager = ref(false);
        const route = useRoute();
        const fileName = ref("");
        const tableData = ref([]);
        const checked = ref(false);
        const playground = ref(null);

        function onDragStart(item) {
            console.log('Drag started:', item);
        }

        function openSnippetManager() {
            showSnippetManager.value = true;
        }

        function closeSnippetManager() {
            showSnippetManager.value = false;
        }

        function updateOutputs(newCode) {
            const newLines = newCode.split("\n");
            const oldLines = outputs.value.length;

            // Update existing lines and add new ones
            for (let i = 0; i < newLines.length; i++) {
                if (i < oldLines) {
                    outputs.value[i] = outputs.value[i] || "";
                } else {
                    outputs.value.push("");
                }
            }

            if (newLines.length < oldLines) {
                outputs.value.splice(
                    newLines.length,
                    oldLines - newLines.length,
                );
            }
        }

        watch(code, (newCode) => {
            updateOutputs(newCode);
        });

        async function runTheCode() {
            console.log("Running code");
            const result = await apiRunCode(code.value, 20);
            console.log(result);
        }

        function refreshOutput() {
            console.log("Refreshing output");
            outputs.value = [];
            updateOutputs(code.value);
        }

        async function loadFileData() {
            if (fileName.value) {
                try {
                    const response = await fetch(`/${fileName.value}`);
                    const csvText = await response.text();

                    Papa.parse(csvText, {
                        header: true,
                        dynamicTyping: true,
                        complete: (results) => {
                            tableData.value = results.data;
                            code.value = `# File: ${fileName.value}\n\n# Your code here\n`;
                        },
                        error: (error) => {
                            console.error("Error parsing CSV:", error);
                        },
                    });
                } catch (error) {
                    console.error("Error loading file:", error);
                }
            }
        }

        function handleEditorScroll(scrollTop) {
            editorScrollTop.value = scrollTop;
        }

        function setupResizer() {
            let startX, startWidth;

            function startResize(e) {
                startX = e.clientX;
                startWidth = parseInt(
                    getComputedStyle(outputContainer.value).width,
                    10,
                );
                document.addEventListener("mousemove", resize);
                document.addEventListener("mouseup", stopResize);
            }

            function resize(e) {
                const newWidth = startWidth + startX - e.clientX;
                outputContainer.value.style.width = `${newWidth}px`;
            }

            function stopResize() {
                document.removeEventListener("mousemove", resize);
                document.removeEventListener("mouseup", stopResize);
            }

            onMounted(() => {
                resizer.value.addEventListener("mousedown", startResize);
                fileName.value = route.query.file || "";
                if (fileName.value) {
                    loadFileData();
                }
            });
        }

        setupResizer();

        return {
            code,
            outputs,
            editorScrollTop,
            docsFunctions,
            runTheCode,
            refreshOutput,
            handleEditorScroll,
            resizer,
            outputContainer,
            openSnippetManager,
            tableData,
            closeSnippetManager,
            showSnippetManager,
            checked,    
            playground, 
            onDragStart,
        };
    },
};
</script>

<style scoped>
.main-container {
    display: flex;
    flex-direction: column;
    height: 100vh;
    width: 100vw;
}


.top-section {
    display: flex;
    height: 65%;
}

.editor-container {
    display: flex;
    flex-grow: 1;
    border: 1px solid #ccc;
    border-radius: 4px;
    overflow: hidden;
    margin-right: 10px;
}

.resizer {
    width: 5px;
    background: #ccc;
    cursor: col-resize;
}

.bottom-section {
    height: 30%;
    overflow: auto;
    border: 1px solid #ccc;
    border-radius: 4px;
    margin-top: 10px;
}

.top-buttons {
    display: flex;
    margin-bottom: 10px;
}

.play-button,
.refresh-button {
    background-color: #f7f7f7;
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 5px;
    cursor: pointer;
}

.play-button button,
.refresh-button button {
    background-color: transparent;
    border: none;
    color: #333;
    font-size: 16px;
}
</style>
