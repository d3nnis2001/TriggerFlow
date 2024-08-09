<template>
    <div class="table-container">
        <vue-good-table
            :columns="columns"
            :rows="rows"
            :sort-options="{
                enabled: true,
            }"
            :pagination-options="{
                enabled: true,
                perPage: 15,
            }"
            :search-options="{
                enabled: true,
            }"
            :filter-options="{
                enabled: true,
                filterByColumn: true,
            }"
            :line-numbers="true"
            styleClass="vgt-table condensed"
            theme="nocturnal"
        >
            <template #table-row="props">
                <span v-if="props.column.field == 'col1'" class="custom-td">
                    {{ props.row.col1 }}
                </span>
                <span
                    v-else-if="props.column.field == 'col2'"
                    class="custom-td"
                >
                    {{ props.row.col2 }}
                </span>
            </template>
        </vue-good-table>
    </div>
</template>

<script>
import { VueGoodTable } from "vue-good-table-next";
import "vue-good-table-next/dist/vue-good-table-next.css";

export default {
    components: {
        VueGoodTable,
    },
    data() {
        return {
            columns: [
                {
                    label: "Header 1",
                    field: "col1",
                    filterOptions: {
                        enabled: true,
                        placeholder: "Filter Header 1",
                    },
                },
                {
                    label: "Header 2",
                    field: "col2",
                    filterOptions: {
                        enabled: true,
                        placeholder: "Filter Header 2",
                    },
                },
                // ... weitere Spalten
            ],
            rows: [
                { col1: "Value 1", col2: "Value 2" },
                // ... weitere Zeilen
            ],
        };
    },
};
</script>

<style scoped>
.table-container {
    max-width: 100%;
    overflow-x: auto;
}

:deep(.vgt-table) {
    font-size: 0.85rem;
}

:deep(.vgt-table th),
:deep(.vgt-table td) {
    padding: 0.5rem;
}

:deep(.vgt-table.nocturnal) {
    background-color: #1e1e1e;
    border-color: #2d2d2d;
    color: #ffffff;
}

:deep(.vgt-table.nocturnal th) {
    background-color: #2d2d2d;
    border-color: #3a3a3a;
    color: #ffffff;
}

:deep(.vgt-table.nocturnal td) {
    border-color: #2d2d2d;
}

:deep(.vgt-table.nocturnal .vgt-input, .vgt-table.nocturnal .vgt-select) {
    background-color: #2d2d2d;
    color: #ffffff;
    border-color: #3a3a3a;
}

:deep(.vgt-table.nocturnal .vgt-pagination) {
    background-color: #1e1e1e;
    color: #ffffff;
}

:deep(.vgt-table.nocturnal .page-link) {
    background-color: #2d2d2d;
    border-color: #3a3a3a;
    color: #ffffff;
}

:deep(.vgt-table.nocturnal .page-link:hover) {
    background-color: #3a3a3a;
}

:deep(.custom-td) {
    display: block;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: 150px;
}
</style>
