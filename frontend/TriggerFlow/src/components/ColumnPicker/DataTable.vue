<template>
    <div class="data-table">
        <h1>{{ tableName }}</h1>

        <div class="main-container">
            <ColumnControls
                :columns="columns"
                @update-column-name="updateColumnName"
                @reorder-columns="reorderColumns"
                @duplicate-column="duplicateColumn"
                @delete-column="deleteColumn"
                @edit-column="editColumn"
            />

            <DataView
                :data="data"
                :visibleColumns="visibleColumns"
                @select-column="selectColumn"
            />

            <SelectedColumn
                v-if="selectedColumn"
                :column="selectedColumn"
                :columnValues="getColumnValues(selectedColumn)"
            />
        </div>
    </div>
</template>

<script>
import { ref, computed } from "vue";
import { useRouter } from "vue-router";
import ColumnControls from "./ColumnControls.vue";
import DataView from "./DataView.vue";
import SelectedColumn from "./SelectedColumn.vue";

export default {
    name: "DataTable",
    components: {
        ColumnControls,
        DataView,
        SelectedColumn,
    },
    props: {
        initialData: {
            type: Array,
            required: true,
        },
        initialTableName: {
            type: String,
            default: "Data Table",
        },
        rawCsvData: {
            type: String,
            required: true,
        },
    },
    setup(props) {
        const router = useRouter();
        const tableName = ref(props.initialTableName);
        const data = ref(props.initialData);
        const columns = ref([]);
        const selectedColumn = ref(null);

        // Initialize columns based on the first row of data
        if (data.value.length > 0) {
            columns.value = Object.keys(data.value[0]).map((key, index) => ({
                id: key,
                name: key,
                position: index,
                visible: true,
            }));
        }

        const visibleColumns = computed(() => {
            return columns.value
                .filter((column) => column.visible)
                .sort((a, b) => a.position - b.position);
        });

        const updateColumnName = (index, newName) => {
            const oldName = columns.value[index].name;
            columns.value[index].name = newName;

            // Update the actual column name in the data
            data.value.forEach((row) => {
                row[newName] = row[oldName];
                delete row[oldName];
            });
        };

        const reorderColumns = () => {
            columns.value.sort((a, b) => a.position - b.position);
        };

        const duplicateColumn = (index) => {
            const newColumn = { ...columns.value[index] };
            newColumn.id = `${newColumn.id}_copy`;
            newColumn.name = `${newColumn.name} (Copy)`;
            newColumn.position = columns.value.length;
            columns.value.push(newColumn);

            // Duplicate the data for this column
            data.value.forEach((row) => {
                row[newColumn.id] = row[columns.value[index].id];
            });
        };

        const deleteColumn = (index) => {
            const columnToDelete = columns.value[index];
            columns.value.splice(index, 1);

            // Remove the column data
            data.value.forEach((row) => {
                delete row[columnToDelete.id];
            });

            // Deselect the column if it was selected
            if (
                selectedColumn.value &&
                selectedColumn.value.id === columnToDelete.id
            ) {
                selectedColumn.value = null;
            }
        };

        const selectColumn = (column) => {
            selectedColumn.value = column;
        };

        const getColumnValues = (column) => {
            return data.value.map((row) => row[column.id]);
        };

        const editColumn = (index) => {
            const columnData = JSON.stringify(columns.value[index]);
            router.push({
                path: "/editor",
                query: {
                    columnIndex: index,
                    columnData: columnData,
                    tableData: JSON.stringify(data.value),
                    rawCsvData: encodeURIComponent(props.rawCsvData),
                },
            });
        };

        return {
            tableName,
            data,
            columns,
            visibleColumns,
            selectedColumn,
            updateColumnName,
            reorderColumns,
            duplicateColumn,
            deleteColumn,
            selectColumn,
            getColumnValues,
            editColumn,
        };
    },
};
</script>

<style scoped>
.data-table {
    font-family: Arial, sans-serif;
}

.main-container {
    display: flex;
    gap: 20px;
}

:deep(.column-controls) {
    flex: 0 0 auto;
    max-height: 400px;
    overflow-y: auto;
}

:deep(.column-controls table) {
    border-collapse: collapse;
}

:deep(.column-controls th),
:deep(.column-controls td) {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}

:deep(.column-controls th) {
    background-color: #f2f2f2;
}

:deep(.data-view) {
    flex: 1;
    display: flex;
    gap: 20px;
}

:deep(.data-table) {
    flex: 1;
    border-collapse: collapse;
}

:deep(.data-table th),
:deep(.data-table td) {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
    cursor: pointer;
}

:deep(.data-table th) {
    background-color: #f2f2f2;
}

:deep(.selected-column) {
    flex: 0 0 200px;
    border-left: 1px solid #ddd;
    padding-left: 20px;
}

:deep(.column-values) {
    max-height: 400px;
    overflow-y: auto;
}
</style>
