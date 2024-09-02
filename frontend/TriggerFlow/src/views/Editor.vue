<template>
  <div class="flex flex-col h-screen w-screen">
    <div class="flex mb-2">
      <button @click="runTheCode" class="bg-gray-200 border border-gray-300 rounded p-1 mr-1 cursor-pointer">
        <i class="pi pi-code text-gray-700"></i>
      </button>
      <button @click="openSnippetManager" class="bg-gray-200 border border-gray-300 rounded p-1 mr-1 cursor-pointer">
        <i class="pi pi-save text-gray-700"></i>
      </button>
      <button @click="refreshOutput" class="bg-gray-200 border border-gray-300 rounded p-1 cursor-pointer">
        <i class="pi pi-refresh text-gray-700"></i>
      </button>
    </div>
    <div class="flex justify-start mb-2">
      <ToggleSwitch v-model="checked" />
    </div>
    <Splitter layout="vertical" class="flex flex-col h-screen">
    <SplitterPanel :size="66">
        <Splitter layout="horizontal" class="h-full">
        <SplitterPanel :size="75" class="flex">
            <div v-if="!checked" class="flex-grow border border-gray-300 rounded overflow-hidden mr-2">
            <EditorComponent v-model="code" @scroll="handleEditorScroll" />
            </div>
            <div v-else class="w-full">
            <Playground ref="playground"/>
            </div>
        </SplitterPanel>
        <SplitterPanel :size="25">
            <RightPanelComponent :codeSnippets="docsFunctions" @drag-start="onDragStart"/>
        </SplitterPanel>
        </Splitter>
    </SplitterPanel>
    <SplitterPanel :size="34">
        <div class="h-full overflow-auto border border-gray-300 rounded mt-2">
        <TableComponent :data="tableData"/>
        </div>
    </SplitterPanel>
    </Splitter>
</div>
</template>

<script>
import { defineComponent, onMounted, ref, watch } from "vue";
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
import Splitter from 'primevue/splitter';
import SplitterPanel from 'primevue/splitterpanel';

export default {
    components: {
        EditorComponent,
        OutputComponent,
        RightPanelComponent,
        TableComponent,
        SnippetManagerComponent,
        ToggleSwitch,
        Playground,
        Splitter,
        SplitterPanel,
    },
    setup() {
        const code = ref("");
        const outputs = ref([]);
        const editorScrollTop = ref(0);
        const outputContainer = ref(null);
        const showSnippetManager = ref(false);
        const route = useRoute();
        const fileName = ref("");
        const tableData = ref([]);
        const checked = ref(false);
        const playground = ref(null);

        tableData.value = [
                { id: 1, name: 'Produkt A', category: 'Elektronik', quantity: 50, price: 199.99 },
                { id: 2, name: 'Produkt B', category: 'Möbel', quantity: 30, price: 299.99 },
                { id: 3, name: 'Produkt C', category: 'Kleidung', quantity: 100, price: 49.99 },
        ];

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


        return {
            code,
            outputs,
            editorScrollTop,
            docsFunctions,
            runTheCode,
            refreshOutput,
            handleEditorScroll,
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
</style>