<template>
  <Dialog
      :visible="visible"
      @update:visible="handleVisibilityChange"
      :modal="true"
      :header="'Variablen'"
      class="w-2/5 max-w-2xl"
      :closable="false"
  >
    <div class="flex flex-col h-[500px] bg-gradient-to-br from-gray-900 to-gray-800 text-white p-4">
      <!-- Loading indicator -->
      <div v-if="loading" class="flex-1 flex items-center justify-center">
        <ProgressSpinner />
      </div>

      <!-- Variablentabelle -->
      <div v-else class="flex-1 overflow-hidden flex flex-col mb-4">
        <DataTable
            :value="variables"
            editMode="cell"
            @cell-edit-complete="onCellEditComplete"
            class="flex-1 bg-gradient-to-r from-gray-800 to-gray-700"
            :scrollable="true"
            scrollHeight="350px"
        >
          <Column field="variable_name" header="Variablenname" style="width:50%">
            <template #editor="{ data, field }">
              <InputText v-model="data[field]" class="w-full bg-gray-700 text-white" />
            </template>
          </Column>
          <Column field="variable_value" header="Wert" style="width:50%">
            <template #editor="{ data, field }">
              <InputText v-model="data[field]" class="w-full bg-gray-700 text-white" />
            </template>
          </Column>
        </DataTable>
      </div>

      <!-- Button zum Hinzufügen neuer Variablen -->
      <div class="flex justify-between">
        <Button label="Neue Variable" icon="pi pi-plus" @click="addVariable" class="bg-green-500 hover:bg-green-600" />
        <Button label="Schließen" icon="pi pi-check" @click="closeDialog" class="bg-blue-500 hover:bg-blue-600" />
      </div>
    </div>
  </Dialog>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import Dialog from 'primevue/dialog';
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import ProgressSpinner from 'primevue/progressspinner';
import { getGlobalVariables, createGlobalVariable, updateGlobalVariable, checkExistance } from '@/api/variable.js';

const job_id = 1

const props = defineProps({
  visible: Boolean,
});

const emit = defineEmits(['update:visible']);

const variables = ref([]);
const loading = ref(false);
const hasChanges = ref(false);

const loadVariables = async () => {
  loading.value = true;
  try {
    const exists = await checkExistance(job_id)
    if (exists.exists) {
      const data = await getGlobalVariables(job_id);
      variables.value = data;
    } else {
      await createGlobalVariable(job_id, 'Default Variable', 'Default Value');
      variables.value = await getGlobalVariables(job_id);
    }
  } catch (error) {
    console.error('Failed to load variables:', error);
    // Here you might want to show an error message to the user
  } finally {
    loading.value = false;
  }
};

const addVariable = () => {
  variables.value.push({variable_name: '', variable_value: ''});
  hasChanges.value = true;
};

const onCellEditComplete = (event) => {
  const {data, newValue, field} = event;
  data[field] = newValue;
  hasChanges.value = true;
};

const saveChanges = async () => {
  loading.value = true;
  try {
    for (const variable of variables.value) {
      await updateGlobalVariable(job_id, variable.variable_name, variable.variable_value);
    }
    hasChanges.value = false;
  } catch (error) {
    console.error('Failed to save changes:', error);
  } finally {
    loading.value = false;
  }
};

const closeDialog = async () => {
  if (hasChanges.value) {
    await saveChanges();
  }
  emit('update:visible', false);
};

const handleVisibilityChange = (newVisible) => {
  if (newVisible) {
    loadVariables();
  } else {
    closeDialog();
  }
};

watch(() => props.visible, (newVisible) => {
  if (newVisible) {
    loadVariables();
  }
});

onMounted(() => {
  if (props.visible) {
    loadVariables();
  }
});
</script>

<style scoped>
</style>