<template>
    <div class="data-table">
        <h1>{{ tableName }}</h1>

        <div class="main-container">
            <div class="column-controls">
                <table>
                    <thead>
                        <tr>
                            <th>Visible</th>
                            <th>Position</th>
                            <th>Name</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr
                            v-for="(column, index) in columns"
                            :key="index"
                            class="column-control"
                        >
                            <td>
                                <input
                                    type="checkbox"
                                    v-model="column.visible"
                                    :id="'col-' + index"
                                />
                            </td>
                            <td>
                                <select
                                    v-model="column.position"
                                    @change="reorderColumns"
                                >
                                    <option
                                        v-for="n in columns.length"
                                        :key="n"
                                        :value="n - 1"
                                    >
                                        {{ n }}
                                    </option>
                                </select>
                            </td>
                            <td>
                                <input
                                    v-model="column.name"
                                    @input="
                                        updateColumnName(
                                            index,
                                            $event.target.value,
                                        )
                                    "
                                />
                            </td>
                            <td>
                                <button @click="duplicateColumn(index)">
                                    Duplicate
                                </button>
                                <button @click="deleteColumn(index)">
                                    Delete
                                </button>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="data-view">
                <table class="data-table">
                    <thead>
                        <tr>
                            <th
                                v-for="column in visibleColumns"
                                :key="column.id"
                                @click="selectColumn(column)"
                            >
                                {{ column.name }}
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(row, rowIndex) in data" :key="rowIndex">
                            <td
                                v-for="column in visibleColumns"
                                :key="column.id"
                                @click="selectColumn(column)"
                            >
                                {{ row[column.id] }}
                            </td>
                        </tr>
                    </tbody>
                </table>

                <div v-if="selectedColumn" class="selected-column">
                    <h2>{{ selectedColumn.name }}</h2>
                    <div class="column-values">
                        <div
                            v-for="(value, index) in getColumnValues(
                                selectedColumn,
                            )"
                            :key="index"
                        >
                            {{ value }}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { ref, computed } from "vue";

export default {
    name: "DataTable",
    props: {
        initialData: {
            type: Array,
            required: true,
        },
        initialTableName: {
            type: String,
            default: "Data Table",
        },
    },
    setup(props) {
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

.column-controls {
    flex: 0 0 auto;
    max-height: 400px;
    overflow-y: auto;
}

.column-controls table {
    border-collapse: collapse;
}

.column-controls th,
.column-controls td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}

.column-controls th {
    background-color: #f2f2f2;
}

.data-view {
    flex: 1;
    display: flex;
    gap: 20px;
}

.data-table {
    flex: 1;
    border-collapse: collapse;
}

.data-table th,
.data-table td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
    cursor: pointer;
}

.data-table th {
    background-color: #f2f2f2;
}

.selected-column {
    flex: 0 0 200px;
    border-left: 1px solid #ddd;
    padding-left: 20px;
}

.column-values {
    max-height: 400px;
    overflow-y: auto;
}
</style>
