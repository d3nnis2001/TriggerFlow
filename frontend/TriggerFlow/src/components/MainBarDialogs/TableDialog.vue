<template>
  <Dialog :visible="visible" @update:visible="$emit('update:visible', $event)" :modal="true" :header="'Konfigurationstabellen'" class="w-4/5 h-4/5 max-w-6xl">
    <div class="flex h-full bg-gradient-to-br from-gray-900 to-gray-800 text-white">
      <!-- Linke Seitenleiste -->
      <div class="w-64 bg-gradient-to-b from-gray-800 to-gray-700 p-4 overflow-y-auto">
        <h3 class="text-xl font-bold mb-4">Tabellen</h3>
        <ul class="space-y-2">
          <li v-for="table in tableStore.tables" :key="table.id" @click="selectTable(table)" class="flex justify-between items-center cursor-pointer hover:bg-gray-700 p-2 rounded">
            {{ table.name }}
            <Button icon="pi pi-trash" class="p-button-rounded p-button-danger p-button-text" @click.stop="deleteTable(table)" />
          </li>
        </ul>
        <Button label="Neue Tabelle" icon="pi pi-plus" @click="createNewTable" class="mt-4 w-full bg-emerald-500 hover:bg-emerald-600" />
      </div>

      <!-- Rechter Hauptbereich -->
      <div class="flex-1 flex flex-col h-full overflow-hidden">
        <div v-if="tableStore.tables.length === 0" class="flex-1 flex items-center justify-center">
          <p class="text-xl text-gray-500">Keine Tabellen vorhanden. Klicken Sie auf "Neue Tabelle", um zu beginnen.</p>
        </div>
        <template v-else>
          <!-- Tabellenname und Beschreibung -->
          <div class="p-4">
            <div class="mb-4">
              <label for="tableName" class="block mb-2">Tabellenname:</label>
              <InputText id="tableName" v-model="currentTable.name" class="w-full bg-gray-700 text-white" @input="ensureUniqueTableName" />
            </div>
            <div class="mb-4">
              <label for="tableDescription" class="block mb-2">Beschreibung:</label>
              <Textarea id="tableDescription" v-model="currentTable.description" rows="3" class="w-full bg-gray-700 text-white" />
            </div>
          </div>

          <!-- Tabellenbereich -->
          <div class="flex-1 overflow-hidden flex flex-col">
            <DataTable :value="currentTable.data" editMode="cell" @cell-edit-complete="onCellEditComplete"
                       class="flex-1 bg-gradient-to-r from-gray-800 to-gray-700" :scrollable="true" scrollHeight="flex">
              <Column field="id" header="ID" :sortable="true" style="width:100px;">
                <template #body="slotProps">
                  {{ slotProps.index + 1 }}
                </template>
              </Column>
              <Column v-for="(col, index) in currentTable.columns" :key="col.field" :field="col.field"
                      class="border border-gray-600" style="width:200px; min-width:200px;">
                <template #header>
                  <InputText v-model="col.header" @input="updateColumnHeader(index, $event)"
                             class="w-full bg-gray-700 text-white border-none" />
                </template>
                <template #editor="{ data, field }">
                  <InputText v-model="data[field]" class="w-full bg-gray-700 text-white" />
                </template>
              </Column>
            </DataTable>
          </div>

          <!-- Buttons für Spalten/Zeilen und Speichern -->
          <div class="bg-gray-800 p-4">
            <div class="flex justify-between mb-4">
              <div>
                <Button label="Spalte +" icon="pi pi-plus" @click="addColumn" class="mr-2 bg-green-500 hover:bg-green-600" />
                <Button label="Spalte -" icon="pi-minus" @click="removeColumn" :disabled="currentTable.columns.length <= 5" class="bg-green-500 hover:bg-green-600" />
              </div>
              <div>
                <Button label="Zeile +" icon="pi pi-plus" @click="addRow" class="mr-2 bg-green-500 hover:bg-green-600" />
                <Button label="Zeile -" icon="pi pi-minus" @click="removeRow" :disabled="currentTable.data.length <= 7" class="bg-green-500 hover:bg-green-600" />
              </div>
            </div>
            <Button label="Speichern" icon="pi pi-save" @click="saveTable" class="w-full bg-emerald-500 hover:bg-emerald-600" />
          </div>
        </template>
      </div>
    </div>
  </Dialog>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import { useTableStore } from '@/stores/tableStore';
import Dialog from 'primevue/dialog';
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import Textarea from 'primevue/textarea';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';

const props = defineProps({
  visible: Boolean
});

const emit = defineEmits(['update:visible']);

const tableStore = useTableStore();

const currentTable = ref({
  id: null,
  name: '',
  description: '',
  columns: [],
  data: []
});

onMounted(async () => {
  await tableStore.fetchTables();
});

watch(() => tableStore.currentTable, (newTable) => {
  if (newTable) {
    currentTable.value = { ...newTable };
  }
}, { deep: true });

const createNewTable = () => {
  const baseName = 'Neue Tabelle';
  let newName = baseName;
  let counter = 1;
  while (tableStore.tables.some(table => table.name === newName)) {
    counter++;
    newName = `${baseName} ${counter}`;
  }
  currentTable.value = {
    id: null,
    name: newName,
    description: '',
    columns: Array.from({ length: 5 }, (_, i) => ({ field: `col${i + 1}`, header: `Spalte ${i + 1}` })),
    data: Array.from({ length: 7 }, (_, i) => {
      const row = { id: i + 1 };
      currentTable.value.columns.forEach(col => {
        row[col.field] = '';
      });
      return row;
    })
  };
};

const selectTable = (table) => {
  tableStore.setCurrentTable(table);
};

const deleteTable = async (table) => {
  try {
    await tableStore.deleteTable(table.id);
    if (tableStore.tables.length > 0) {
      selectTable(tableStore.tables[0]);
    } else {
      currentTable.value = { id: null, name: '', description: '', columns: [], data: [] };
    }
  } catch (error) {
    // Handle error (e.g., show error message to user)
  }
};

const addColumn = () => {
  const newField = `col${currentTable.value.columns.length + 1}`;
  currentTable.value.columns.push({ field: newField, header: `Spalte ${currentTable.value.columns.length + 1}` });
  currentTable.value.data.forEach(row => {
    row[newField] = '';
  });
};

const removeColumn = () => {
  if (currentTable.value.columns.length > 5) {
    const lastField = currentTable.value.columns[currentTable.value.columns.length - 1].field;
    currentTable.value.columns.pop();
    currentTable.value.data.forEach(row => {
      delete row[lastField];
    });
  }
};

const addRow = () => {
  const newRow = { id: currentTable.value.data.length + 1 };
  currentTable.value.columns.forEach(col => {
    newRow[col.field] = '';
  });
  currentTable.value.data.push(newRow);
};

const removeRow = () => {
  if (currentTable.value.data.length > 7) {
    currentTable.value.data.pop();
  }
};

const onCellEditComplete = (event) => {
  const { data, newValue, field } = event;
  data[field] = newValue;
};

const updateColumnHeader = (index, event) => {
  currentTable.value.columns[index].header = event.target.value;
};

const saveTable = async () => {
  try {
    await tableStore.saveTable(currentTable.value);
    // Optional: Show success message
  } catch (error) {
    // Handle error (e.g., show error message to user)
  }
};

const ensureUniqueTableName = () => {
  let newName = currentTable.value.name;
  let counter = 1;
  while (tableStore.tables.some(table => table.id !== currentTable.value.id && table.name === newName)) {
    counter++;
    newName = `${currentTable.value.name} ${counter}`;
  }
  currentTable.value.name = newName;
};

</script>