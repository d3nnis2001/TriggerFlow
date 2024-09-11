import { defineStore } from 'pinia';
import { ref, computed } from 'vue';
import axios from 'axios';

export const useTableStore = defineStore('table', () => {
    const tables = ref([]);
    const currentTable = ref(null);

    const getTableById = computed(() => {
        return (id) => tables.value.find(table => table.id === id);
    });

    function setCurrentTable(table) {
        currentTable.value = table;
    }

    async function fetchTables() {
        try {
            const response = await axios.get('/api/tables');
            tables.value = response.data;
        } catch (error) {
            console.error('Error fetching tables:', error);
        }
    }

    async function saveTable(table) {
        try {
            if (table.id) {
                await axios.put(`/api/tables/${table.id}`, table);
                const index = tables.value.findIndex(t => t.id === table.id);
                if (index !== -1) {
                    tables.value[index] = table;
                }
            } else {
                const response = await axios.post('/api/tables', table);
                tables.value.push(response.data);
            }
        } catch (error) {
            console.error('Error saving table:', error);
            throw error;
        }
    }

    async function deleteTable(tableId) {
        try {
            await axios.delete(`/api/tables/${tableId}`);
            tables.value = tables.value.filter(t => t.id !== tableId);
            if (currentTable.value && currentTable.value.id === tableId) {
                currentTable.value = null;
            }
        } catch (error) {
            console.error('Error deleting table:', error);
            throw error;
        }
    }

    return {
        tables,
        currentTable,
        getTableById,
        setCurrentTable,
        fetchTables,
        saveTable,
        deleteTable
    };
});