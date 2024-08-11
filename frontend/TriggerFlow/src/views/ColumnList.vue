<template>
    <div>
        <DataTable
            v-if="csvData.length"
            :initialData="csvData"
            initialTableName="BTCUSDT3600"
            :rawCsvData="rawCsvData"
        />
        <p v-else-if="loading">Loading data...</p>
        <p v-else>No data available</p>
    </div>
</template>

<script>
import { ref, onMounted } from "vue";
import DataTable from "../components/ColumnPicker/DataTable.vue";
import Papa from "papaparse";

export default {
    components: { DataTable },
    setup() {
        const csvData = ref([]);
        const loading = ref(true);
        const rawCsvData = ref("");

        const loadCSV = async () => {
            try {
                const response = await fetch("/BTCUSDT3600.csv");
                const csvText = await response.text();
                rawCsvData.value = csvText;

                Papa.parse(csvText, {
                    header: true,
                    dynamicTyping: true,
                    complete: (results) => {
                        csvData.value = results.data.slice(0, 500); // Only take the first 500 rows
                        loading.value = false;
                    },
                    error: (error) => {
                        console.error("Error parsing CSV:", error);
                        loading.value = false;
                    },
                });
            } catch (error) {
                console.error("Error loading CSV:", error);
                loading.value = false;
            }
        };

        onMounted(() => {
            loadCSV();
        });

        return {
            csvData,
            loading,
            rawCsvData,
        };
    },
};
</script>
