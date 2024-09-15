<template>
  <Dialog :visible="visible" @update:visible="$emit('update:visible', $event)" :modal="true" :header="'Konfigurationstabellen'" class="w-4/5 h-4/5 max-w-6xl">
    <div class="flex h-full bg-gradient-to-br from-gray-900 to-gray-800 text-white">
      <!-- Linke Seitenleiste -->
      <div class="w-64 bg-gradient-to-b from-gray-800 to-gray-700 p-4 overflow-y-auto">
        <h3 class="text-xl font-bold mb-4">Tabellen</h3>
        <ul class="space-y-2">
          <li v-for="table in tables" :key="table.id" @click="selectTable(table)" class="flex justify-between items-center cursor-pointer hover:bg-gray-700 p-2 rounded">
            {{ table.name }}
            <Button icon="pi pi-trash" class="p-button-rounded p-button-danger p-button-text" @click.stop="deleteTable(table)" />
          </li>
        </ul>
        <Button label="Neue Tabelle" icon="pi pi-plus" @click="createNewTable" class="mt-4 w-full bg-emerald-500 hover:bg-emerald-600" />
      </div>

      <!-- Rechter Hauptbereich -->
      <div class="flex-1 flex flex-col h-full overflow-hidden">
        <div v-if="tables.length === 0" class="flex-1 flex items-center justify-center">
          <p class="text-xl text-gray-500">Keine Tabellen vorhanden. Klicken Sie auf "Neue Tabelle", um zu beginnen.</p>
        </div>
        <template v-else>
          <!-- Tabellenname und Beschreibung -->
          <div class="p-4">
            <div class="mb-4">
              <label for="tableName" class="block mb-2">Tabellenname:</label>
              <InputText id="tableName" v-model="currentTable.name" class="w-full bg-gray-700 text-white" @input="ensureUniqueTableName" />
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
                <Button label="Zeile -" icon="pi pi-minus" @click="removeRow" :disabled="currentTable.data.length <= 10" class="bg-green-500 hover:bg-green-600" />
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
import {ref, reactive, onMounted} from 'vue';
import Dialog from 'primevue/dialog';
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import { createTable, getAllTablesByJob } from "@/api/configTable.js";

const props = defineProps({
  visible: Boolean
});

const emit = defineEmits(['update:visible']);

const tables = ref([]);
const currentTable = reactive({
  id: null,
  name: '',
  columns: [],
  data: []
});

// Funktion, um Tabellen von der API zu laden
const loadTables = async () => {
  const response = await getAllTablesByJob(1);
  tables.value = response.data.map((tableData, index) => {
    const jsonObject = JSON.parse(tableData.table_data.replace(/'/g, '"'));
    const columns = Object.keys(jsonObject[0]).map(key => ({
      field: key,
      header: key
    }));
    return {
      id: index,
      name: tableData.table_name,
      columns: columns,
      data: jsonObject.map((row, rowIndex) => ({
        id: rowIndex + 1,
        ...row
      }))
    };
  });
};
onMounted(() => {
  loadTables();
});

// Tabellen erstellen
const createNewTable = () => {
  const baseName = 'Neue Tabelle';
  let newName = baseName;
  let counter = 1;
  while (tables.value.some(table => table.name === newName)) {
    counter++;
    newName = `${baseName} ${counter}`;
  }
  currentTable.id = Date.now();
  currentTable.name = newName;
  currentTable.columns = Array.from({length: 5}, (_, i) => ({field: `col${i + 1}`, header: `Spalte ${i + 1}`}));
  currentTable.data = Array.from({length: 10}, (_, i) => {
    const row = {id: i + 1};
    currentTable.columns.forEach(col => {
      row[col.field] = '';
    });
    return row;
  });
  tables.value.push({...currentTable});
};

// Tabelle auswählen
const selectTable = (table) => {
  Object.assign(currentTable, table);
};

// Tabelle löschen
const deleteTable = (table) => {
  const index = tables.value.findIndex(t => t.id === table.id);
  if (index !== -1) {
    tables.value.splice(index, 1);
  }
  if (currentTable.id === table.id) {
    if (tables.value.length > 0) {
      selectTable(tables.value[0]);
    } else {
      Object.assign(currentTable, {id: null, name: '', columns: [], data: []});
    }
  }
};

// Spalte hinzufügen
const addColumn = () => {
  const newField = `col${currentTable.columns.length + 1}`;
  currentTable.columns.push({field: newField, header: `Spalte ${currentTable.columns.length + 1}`});
  currentTable.data.forEach(row => {
    row[newField] = '';
  });
};

// Spalte entfernen
const removeColumn = () => {
  if (currentTable.columns.length > 5) {
    const lastField = currentTable.columns[currentTable.columns.length - 1].field;
    currentTable.columns.pop();
    currentTable.data.forEach(row => {
      delete row[lastField];
    });
  }
};

// Zeile hinzufügen
const addRow = () => {
  const newRow = {id: currentTable.data.length + 1};
  currentTable.columns.forEach(col => {
    newRow[col.field] = '';
  });
  currentTable.data.push(newRow);
};

// Zeile entfernen
const removeRow = () => {
  if (currentTable.data.length > 10) {
    currentTable.data.pop();
  }
};

// Bearbeitung der Tabellenzellen
const onCellEditComplete = (event) => {
  const {data, newValue, field} = event;
  data[field] = newValue;
};

// Tabellenkopf aktualisieren
const updateColumnHeader = (index, event) => {
  currentTable.columns[index].header = event.target.value;
};

// Tabelle speichern
const saveTable = async () => {
  try {
    const response = await createTable(1, currentTable.name, currentTable.data);
    console.log("Table saved:", response);
    await loadTables(); // Reload tables after saving
  } catch (error) {
    console.error("Error saving table:", error);
  }
};

// Sicherstellen, dass der Tabellenname einzigartig ist
const ensureUniqueTableName = () => {
  let newName = currentTable.name;
  let counter = 1;
  while (tables.value.some(table => table.id !== currentTable.id && table.name === newName)) {
    counter++;
    newName = `${currentTable.name} ${counter}`;
  }
  currentTable.name = newName;
};
</script>