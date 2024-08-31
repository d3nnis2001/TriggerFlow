<template>
    <div class="card">
        <DataTable 
            :value="data" 
            :paginator="true" 
            :rows="10"
            ref="dt"
            resizableColumns 
            columnResizeMode="expand" 
            showGridlines 
            tableStyle="min-width: 50rem"
        >
            <template #header>
                <div class="flex justify-end">
                    <Button icon="pi pi-external-link" label="Export" @click="exportCSV($event)" />
                </div>
            </template>

            <Column 
                v-for="col in columns" 
                :key="col.field" 
                :field="col.field" 
                :header="col.header" 
                :sortable="true"
                :filter="true"
                filterMatchMode="contains"
            ></Column>
        </DataTable>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Button from 'primevue/button';

const props = defineProps({
    data: {
        type: Array,
        required: true
    }
});

const dt = ref();

const columns = computed(() => {
    if (props.data && props.data.length > 0) {
        const allKeys = new Set();
        props.data.forEach(item => {
            Object.keys(item).forEach(key => allKeys.add(key));
        });
        return Array.from(allKeys).map(key => ({
            field: key,
            header: key.charAt(0).toUpperCase() + key.slice(1) // Capitalize first letter
        }));
    }
    return [];
});

const exportCSV = () => {
    dt.value.exportCSV();
};
</script>