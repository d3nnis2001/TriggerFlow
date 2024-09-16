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
      <div v-if="loading" class="flex-1 flex items-center justify-center">
        <ProgressSpinner />
      </div>
      <div v-else class="flex-1 overflow-hidden flex flex-col mb-4">
        <DataTable
            :value="variables"
            editMode="cell"
            @cell-edit-complete="onCellEditComplete"
            class="flex-1 bg-gradient-to-r from-gray-800 to-gray-700 p-datatable-sm"
            :scrollable="true"
            scrollHeight="425px"
            :showGridlines="true"
        >
          <Column field="variable_name" header="Variablenname" style="width:50%">
            <template #editor="{ data, field }">
              <InputText v-model="data[field]" class="w-full bg-gray-700 text-white h-full" />
            </template>
          </Column>
          <Column field="variable_value" header="Wert" style="width:50%">
            <template #editor="{ data, field }">
              <InputText v-model="data[field]" class="w-full bg-gray-700 text-white h-full" />
            </template>
          </Column>
        </DataTable>
      </div>
      <div class="flex justify-between">
        <Button label="Neue Variable" icon="pi pi-plus" @click="addVariable" class="bg-green-500 hover:bg-green-600" />
        <Button label="Leere Zeilen löschen" icon="pi pi-trash" @click="deleteEmptyRows" class="bg-red-500 hover:bg-red-600" />
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

const job_id = 1;

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
    const exists = await checkExistance(job_id);
    if (exists.exists) {
      const data = await getGlobalVariables(job_id);
      console.log(JSON.parse(data)[0])
      variables.value = JSON.parse(data);
    } else {
      await createGlobalVariable(job_id, [{variable_name: "Test", variable_value: "Test"}]);
      const data = await getGlobalVariables(job_id);
      variables.value = Array.isArray(data) ? data : [];
    }
  } catch (error) {
    console.error('Failed to load variables:', error);
    variables.value = [];
  } finally {
    loading.value = false;
  }
};

const deleteEmptyRows = () => {
  variables.value = variables.value.filter(
      variable => variable.variable_name.trim() !== '' || variable.variable_value.trim() !== ''
  );
  hasChanges.value = true;
};

const addVariable = () => {
  variables.value.push({variable_name: '', variable_value: ''});
  hasChanges.value = true;
};

const onCellEditComplete = (event) => {
  const { data, newValue, field } = event;
  if (data && typeof data === 'object') {
    data[field] = newValue;
    hasChanges.value = true;
  } else {
    console.error('Invalid data object in onCellEditComplete:', data);
  }
};

const saveChanges = async () => {
  loading.value = true;
  try {
    await updateGlobalVariable(job_id, variables.value);
    hasChanges.value = false;
  } catch (error) {
    console.error('Failed to save changes:', error);
  } finally {
    loading.value = false;
  }
};

const closeDialog = async () => {
  // Save changes before closing, even if hasChanges is false
  await saveChanges();
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
:deep(.p-datatable .p-datatable-thead > tr > th) {
  border: 1px solid #4a5568;  /* Dunkelgrauer Rand für Kopfzellen */
}

:deep(.p-datatable .p-datatable-tbody > tr > td) {
  border: 1px solid #4a5568;  /* Dunkelgrauer Rand für Datenzellen */
}

:deep(.p-datatable.p-datatable-sm .p-datatable-thead > tr > th) {
  padding: 0.5rem;
}

:deep(.p-datatable-tbody > tr) {
  height: 50px; /* Adjust this value to set a fixed height for rows */
}

:deep(.p-datatable.p-datatable-sm .p-datatable-tbody > tr > td) {
  padding: 0.5rem;
}
</style>