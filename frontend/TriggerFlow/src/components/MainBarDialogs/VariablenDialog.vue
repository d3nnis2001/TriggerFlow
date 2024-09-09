<template>
  <Dialog :visible="visible" @update:visible="$emit('update:visible', $event)" :modal="true" :header="'Variablen'" class="w-2/5 max-w-2xl">
    <div class="flex flex-col h-[500px] bg-gradient-to-br from-gray-900 to-gray-800 text-white p-4">

      <!-- Variablentabelle -->
      <div class="flex-1 overflow-hidden flex flex-col mb-4">
        <DataTable :value="variables" editMode="cell" @cell-edit-complete="onCellEditComplete"
                   class="flex-1 bg-gradient-to-r from-gray-800 to-gray-700" :scrollable="true" scrollHeight="350px">
          <Column field="name" header="Variablenname" style="width:50%">
            <template #editor="{ data, field }">
              <InputText v-model="data[field]" class="w-full bg-gray-700 text-white" />
            </template>
          </Column>
          <Column field="value" header="Wert" style="width:50%">
            <template #editor="{ data, field }">
              <InputText v-model="data[field]" class="w-full bg-gray-700 text-white" />
            </template>
          </Column>
        </DataTable>
      </div>

      <!-- Button zum Hinzufügen neuer Variablen -->
      <div class="flex justify-center">
        <Button label="Neue Variable" icon="pi pi-plus" @click="addVariable" class="bg-green-500 hover:bg-green-600" />
      </div>
    </div>
  </Dialog>
</template>

<script setup>
import { ref } from 'vue';
import Dialog from 'primevue/dialog';
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';

const props = defineProps({
  visible: Boolean
});

const emit = defineEmits(['update:visible']);

const variables = ref([
  { name: 'Variable 1', value: 'Wert 1' },
  { name: 'Variable 2', value: 'Wert 2' },
  // Fügen Sie hier mehr Variablen hinzu, um das Scrollverhalten zu testen
]);

const addVariable = () => {
  variables.value.push({ name: '', value: '' });
};

const onCellEditComplete = (event) => {
  const { data, newValue, field } = event;
  data[field] = newValue;
};
</script>

<style scoped>
:deep(.p-dialog-content) {
  padding: 0 !important;
}

:deep(.p-datatable) {
  background-color: transparent;
}

:deep(.p-datatable .p-datatable-thead > tr > th) {
  background-color: #374151;
  color: white;
  border: 1px solid #4B5563;
}

:deep(.p-datatable .p-datatable-tbody > tr > td) {
  background-color: #1F2937;
  color: white;
  border: 1px solid #4B5563;
}

:deep(.p-datatable .p-datatable-tbody > tr:nth-child(even)) {
  background-color: #283548;
}

:deep(.p-inputtext) {
  background-color: #374151;
  color: white;
  border-color: #4B5563;
}

:deep(.p-button) {
  background-color: #10B981;
  border-color: #10B981;
}

:deep(.p-button:hover) {
  background-color: #059669;
  border-color: #059669;
}
</style>