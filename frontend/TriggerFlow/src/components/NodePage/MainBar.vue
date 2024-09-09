
<template>
    <div class="card flex justify-center">
        <Drawer v-model:visible="visible">
            <template #container="{ closeCallback }">
                <div class="flex flex-col h-full">
                    <div class="flex items-center justify-between px-6 pt-4 shrink-0">
                        <span class="inline-flex items-center gap-2">
                          <svg width="35" height="35" viewBox="0 0 742 923" fill="none" xmlns="http://www.w3.org/2000/svg">
                          <path fill-rule="evenodd" clip-rule="evenodd" d="M368.183 276C444.398 276 506.183 214.215 506.183 138C506.183 61.7847 444.398 0 368.183 0C291.968 0 230.183 61.7847 230.183 138C230.183 214.215 291.968 276 368.183 276ZM728.768 312.823C702.029 265.977 642.37 249.664 595.515 276.388L369.394 405.359L146.859 276.925C100.041 249.905 40.1705 265.947 13.1351 312.757C-13.9004 359.566 2.13676 419.418 48.9551 446.439L270.218 574.138V824.925C270.218 879.09 314.127 923 368.292 923C422.458 923 466.367 879.09 466.367 824.925V574.923L692.345 446.034C739.2 419.31 755.507 359.669 728.768 312.823Z" fill="url(#paint0_linear_115_683)"/>
                            <defs>
                            <linearGradient id="paint0_linear_115_683" x1="370.814" y1="4.4212e-09" x2="371.183" y2="1928.5" gradientUnits="userSpaceOnUse">
                            <stop stop-color="#34D399"/>
                            <stop offset="1" stop-color="white"/>
                            </linearGradient>
                            </defs>
                          </svg>
                          <span class="font-semibold text-2xl text-primary">Triggerflow</span>
                        </span>
                        <span>
                            <Button type="button" @click="closeCallback" icon="pi pi-times" rounded outlined></Button>
                        </span>
                    </div>
                    <div class="overflow-y-auto">
                        <ul class="list-none p-4 m-0">
                            <li>
                                <div
                                    v-ripple
                                    v-styleclass="{
                                        selector: '@next',
                                        enterFromClass: 'hidden',
                                        enterActiveClass: 'animate-slidedown',
                                        leaveToClass: 'hidden',
                                        leaveActiveClass: 'animate-slideup'
                                    }"
                                    class="p-4 flex items-center justify-between text-surface-500 dark:text-surface-400 cursor-pointer p-ripple"
                                >
                                    <span class="font-medium">ALLGEMEIN</span>
                                    <i class="pi pi-chevron-down"></i>
                                </div>
                                <ul class="list-none p-0 m-0 overflow-hidden">
                                    <li>
                                        <a v-ripple @click="openDialog('eigenschaften')" class="flex items-center cursor-pointer p-4 rounded text-surface-700 hover:bg-surface-100 dark:text-surface-0 dark:hover:bg-surface-800 duration-150 transition-colors p-ripple">
                                            <i class="pi pi-pen-to-square  mr-2"></i>
                                            <span class="font-medium">Eigenschaften</span>
                                        </a>
                                    </li>
                                    <li>
                                        <a v-ripple @click="openDialog('zeitplan')" class="flex items-center cursor-pointer p-4 rounded text-surface-700 hover:bg-surface-100 dark:text-surface-0 dark:hover:bg-surface-800 duration-150 transition-colors p-ripple">
                                            <i class="pi pi-clock mr-2"></i>
                                            <span class="font-medium">Zeitplan</span>
                                        </a>
                                    </li>
                                    <li>
                                        <a
                                            v-ripple
                                            v-styleclass="{
                                                selector: '@next',
                                                enterFromClass: 'hidden',
                                                enterActiveClass: 'animate-slidedown',
                                                leaveToClass: 'hidden',
                                                leaveActiveClass: 'animate-slideup'
                                            }"
                                            class="flex items-center cursor-pointer p-4 rounded text-surface-700 hover:bg-surface-100 dark:text-surface-0 dark:hover:bg-surface-800 duration-150 transition-colors p-ripple"
                                        >
                                            <i class="pi pi-file mr-2"></i>
                                            <span class="font-medium">Import/Export</span>
                                            <i class="pi pi-chevron-down ml-auto"></i>
                                        </a>
                                        <ul class="list-none py-0 pl-4 pr-0 m-0 hidden overflow-y-hidden transition-all duration-[400ms] ease-in-out">
                                          <li>
                                            <a v-ripple @click="openDialog('export')"  class="flex items-center cursor-pointer p-4 rounded text-surface-700 hover:bg-surface-100 dark:text-surface-0 dark:hover:bg-surface-800 duration-150 transition-colors p-ripple">
                                              <i class="pi pi-file-export mr-2"></i>
                                              <span class="font-medium">Export</span>
                                            </a>
                                          </li>
                                          <li>
                                              <a v-ripple @click="openDialog('import')"  class="flex items-center cursor-pointer p-4 rounded text-surface-700 hover:bg-surface-100 dark:text-surface-0 dark:hover:bg-surface-800 duration-150 transition-colors p-ripple">
                                                  <i class="pi pi-file-import mr-2"></i>
                                                  <span class="font-medium">Import</span>
                                              </a>
                                          </li>
                                        </ul>
                                    </li>
                                    <li>
                                        <a v-ripple @click="openDialog('format')"  class="flex items-center cursor-pointer p-4 rounded text-surface-700 hover:bg-surface-100 dark:text-surface-0 dark:hover:bg-surface-800 duration-150 transition-colors p-ripple">
                                            <i class="pi pi-cog mr-2"></i>
                                            <span class="font-medium">Format Einstellungen</span>
                                        </a>
                                    </li>
                                    <li>
                                        <a v-ripple class="flex items-center cursor-pointer p-4 rounded text-surface-700 hover:bg-surface-100 dark:text-surface-0 dark:hover:bg-surface-800 duration-150 transition-colors p-ripple">
                                            <i class="pi pi-play-circle mr-2"></i>
                                            <span class="font-medium">Run</span>
                                        </a>
                                    </li>
                                </ul>
                            </li>
                        </ul>
                        <ul class="list-none p-4 m-0">
                            <li>
                                <div
                                    v-ripple
                                    v-styleclass="{
                                        selector: '@next',
                                        enterFromClass: 'hidden',
                                        enterActiveClass: 'animate-slidedown',
                                        leaveToClass: 'hidden',
                                        leaveActiveClass: 'animate-slideup'
                                    }"
                                    class="p-4 flex items-center justify-between text-surface-500 dark:text-surface-400 cursor-pointer p-ripple"
                                >
                                    <span class="font-medium">JOB ITEMS</span>
                                    <i class="pi pi-chevron-down"></i>
                                </div>
                                <ul class="list-none p-0 m-0 overflow-hidden">
                                    <li>
                                        <a v-ripple class="flex items-center cursor-pointer p-4 rounded text-surface-700 hover:bg-surface-100 dark:text-surface-0 dark:hover:bg-surface-800 duration-150 transition-colors p-ripple">
                                            <i class="pi pi-th-large mr-2"></i>
                                            <span class="font-medium">Shapes</span>
                                        </a>
                                    </li>
                                    <li>
                                        <a v-ripple @click="openDialog('table')" class="flex items-center cursor-pointer p-4 rounded text-surface-700 hover:bg-surface-100 dark:text-surface-0 dark:hover:bg-surface-800 duration-150 transition-colors p-ripple">
                                            <i class="pi pi-table mr-2"></i>
                                            <span class="font-medium">Tabelle</span>
                                        </a>
                                    </li>
                                    <li>
                                        <a v-ripple @click="openDialog('variablen')" class="flex items-center cursor-pointer p-4 rounded text-surface-700 hover:bg-surface-100 dark:text-surface-0 dark:hover:bg-surface-800 duration-150 transition-colors p-ripple">
                                            <i class="pi pi-code mr-2"></i>
                                            <span class="font-medium">Job-Variablen</span>
                                        </a>
                                    </li>
                                </ul>
                            </li>
                        </ul>
                    </div>
                    <div class="mt-auto">
                        <hr class="mb-4 mx-4 border-t border-0 border-surface-200 dark:border-surface-700" />
                        <a v-ripple class="m-4 flex items-center cursor-pointer p-4 gap-2 rounded text-surface-700 hover:bg-surface-100 dark:text-surface-0 dark:hover:bg-surface-800 duration-150 transition-colors p-ripple">
                            <Avatar image="https://primefaces.org/cdn/primevue/images/avatar/amyelsner.png" shape="circle" />
                            <span class="font-bold">Dennis Schielke</span>
                        </a>
                    </div>
                </div>
            </template>
        </Drawer>
        <Button icon="pi pi-bars" class="bg-white text-black" @click="visible = true" style="font-size: 4rem" rounded outlined raised text/>
      <TableDialog v-model:visible="tableDialogVisible" />
      <EigenschaftenDialog v-model:visible="eigenschaftenDialogVisible" />
      <VariablenDialog v-model:visible="variablenDialogVisible" />
      <FormatDialog v-model:visible="formatDialogVisible" />
      <ZeitplanDialog v-model:visible="zeitplanDialogVisible" />
      <ExportDialog v-model:visible="exportDialogVisible" />
      <ImportDialog v-model:visible="importDialogVisible" />
    </div>
</template>

<script setup>
import { ref } from "vue";
import Drawer from 'primevue/drawer';
import Button from "primevue/button";
import Avatar from "primevue/avatar";
import TableDialog from "../MainBarDialogs/TableDialog.vue"
import ExportDialog from "@/components/MainBarDialogs/ExportDialog.vue";
import ImportDialog from "@/components/MainBarDialogs/ImportDialog.vue";
import EigenschaftenDialog from "@/components/MainBarDialogs/EigenschaftenDialog.vue";
import VariablenDialog from "@/components/MainBarDialogs/VariablenDialog.vue";
import FormatDialog from "@/components/MainBarDialogs/FormatDialog.vue";
import ZeitplanDialog from "@/components/MainBarDialogs/ZeitplanDialog.vue";

const eigenschaftenDialogVisible = ref(false);
const tableDialogVisible = ref(false);
const variablenDialogVisible = ref(false);
const formatDialogVisible = ref(false);
const zeitplanDialogVisible = ref(false);
const exportDialogVisible = ref(false);
const importDialogVisible = ref(false);


const openDialog = (dialogType) => {
  switch(dialogType) {
    case 'eigenschaften':
      eigenschaftenDialogVisible.value = true;
      break;
    case 'table':
      tableDialogVisible.value = true;
      break;
    case 'variablen':
      variablenDialogVisible.value = true;
      break;
    case 'format':
      formatDialogVisible.value = true;
      break;
    case 'zeitplan':
      zeitplanDialogVisible.value = true;
      break;
    case 'export':
      exportDialogVisible.value = true;
      break;
    case 'import':
      importDialogVisible.value = true;
      break;
  }
  visible.value = false; // Close the drawer when opening a dialog
};


const visible = ref(false);
</script>
