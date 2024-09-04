<template>
  <div class="h-screen w-full flex flex-col">
    <Panel class="flex-grow flex flex-col">
      <template #header>
        <div class="mb-4">
          <Select v-model="selectedFormat" :options="satzformate" optionLabel="name" placeholder="Satzformat auswählen" class="w-full mb-2" />
          <InputText v-if="selectedFormat" v-model="selectedFormat.name" placeholder="Formatname" class="w-full" />
        </div>

        <!-- Icons -->
        <div class="flex justify-between mb-4">
          <Button icon="pi pi-plus" @click="createNewFormat" label="Neu" class="p-button-sm" />
          <Button icon="pi pi-save" @click="saveChanges" label="Speichern" :disabled="!canSave" class="p-button-sm" />
          <Button icon="pi pi-trash" @click="confirmDeleteFormat" label="Löschen" :disabled="!selectedFormat" class="p-button-sm p-button-danger" />
        </div>
      </template>

    <!-- Table mit den Werten -->
      <div v-if="selectedFormat" class="flex-grow overflow-auto">
        <DataTable :value="selectedFormat.rows" dataKey="id" :rowHover="true" v-model:selection="selectedRow" selectionMode="single" @reorder="onRowReorder" class="mb-4" responsiveLayout="scroll">
          <Column :rowReorder="true" style="width: 3rem" />
          <Column field="name" header="Name" class="w-1/3">
            <template #body="slotProps">
              <InputText v-model="slotProps.data.name" placeholder="Name" class="w-full" :class="{'p-invalid': showValidation && !slotProps.data.name}" />
            </template>
          </Column>
          <Column field="required" header="Pflichtfeld" class="w-1/6">
            <template #body="slotProps">
              <div class="flex justify-center">
                <Checkbox v-model="slotProps.data.required" :binary="true" />
              </div>
            </template>
          </Column>
          <Column field="defaultValue" header="Standardwert" class="w-1/3">
            <template #body="slotProps">
              <InputText v-model="slotProps.data.defaultValue" placeholder="Standardwert" class="w-full" />
            </template>
          </Column>
          <Column class="w-16">
            <template #body="slotProps">
              <Button icon="pi pi-trash" @click="deleteRow(slotProps.data)" text />
            </template>
          </Column>
        </DataTable>
        <Button label="Neue Zeile hinzufügen" @click="addNewRow" class="mb-4" />
      </div>
    </Panel>

    <Dialog v-model:visible="deleteDialogVisible" header="Satzformat löschen" :modal="true">
      <p>Möchten Sie dieses Satzformat wirklich löschen?</p>
      <template #footer>
        <Button label="Nein" icon="pi pi-times" @click="deleteDialogVisible = false" text />
        <Button label="Ja" icon="pi pi-check" @click="deleteFormat" autofocus />
      </template>
    </Dialog>
  </div>
</template>

<script>
import { ref, reactive, watch, computed } from 'vue';
import Panel from 'primevue/panel';
import Select from 'primevue/select';
import Button from 'primevue/button';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import InputText from 'primevue/inputtext';
import Checkbox from 'primevue/checkbox';
import Dialog from 'primevue/dialog';

export default {
  components: {
    Panel,
    Select,
    Button,
    DataTable,
    Column,
    InputText,
    Checkbox,
    Dialog
  },
  setup() {
    const satzformate = reactive([]);
    const selectedFormat = ref(null);
    const selectedRow = ref(null);
    const deleteDialogVisible = ref(false);
    const unsavedChanges = ref(false);
    const showValidation = ref(false);

    const canSave = computed(() => {
      if (!selectedFormat.value) return false;
      return selectedFormat.value.name.trim() !== '' && 
             selectedFormat.value.rows.every(row => row.name.trim() !== '');
    });

    watch(selectedFormat, () => {
      selectedRow.value = null;
      showValidation.value = false;
    });

    const createNewFormat = () => {
      const newFormat = {
        id: Date.now(),
        name: `Neues Format ${satzformate.length + 1}`,
        rows: []
      };
      satzformate.push(newFormat);
      selectedFormat.value = newFormat;
      unsavedChanges.value = true;
    };

    const confirmDeleteFormat = () => {
      deleteDialogVisible.value = true;
    };

    const deleteFormat = () => {
      const index = satzformate.findIndex(format => format.id === selectedFormat.value.id);
      if (index !== -1) {
        satzformate.splice(index, 1);
        selectedFormat.value = null;
      }
      deleteDialogVisible.value = false;
      unsavedChanges.value = true;
    };

    const addNewRow = () => {
      selectedFormat.value.rows.push({
        id: Date.now(),
        name: '',
        required: false,
        defaultValue: ''
      });
      unsavedChanges.value = true;
    };

    const deleteRow = (row) => {
      const index = selectedFormat.value.rows.findIndex(r => r.id === row.id);
      if (index !== -1) {
        selectedFormat.value.rows.splice(index, 1);
      }
      unsavedChanges.value = true;
    };

    const onRowReorder = (event) => {
      selectedFormat.value.rows.splice(event.dropIndex, 0, selectedFormat.value.rows.splice(event.dragIndex, 1)[0]);
      unsavedChanges.value = true;
    };

    const saveChanges = () => {
      showValidation.value = true;
      if (canSave.value) {
        // Hier würden Sie die Änderungen an Ihrem Backend speichern
        console.log('Speichere Änderungen:', selectedFormat.value);
        unsavedChanges.value = false;
        showValidation.value = false;
        // Implementieren Sie hier Ihre Speicherlogik
      }
    };

    return {
      satzformate,
      selectedFormat,
      selectedRow,
      deleteDialogVisible,
      unsavedChanges,
      showValidation,
      canSave,
      createNewFormat,
      confirmDeleteFormat,
      deleteFormat,
      addNewRow,
      deleteRow,
      onRowReorder,
      saveChanges
    };
  }
}
</script>