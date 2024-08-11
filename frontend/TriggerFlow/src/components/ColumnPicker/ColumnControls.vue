<template>
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
                            @change="$emit('reorder-columns')"
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
                                $emit(
                                    'update-column-name',
                                    index,
                                    $event.target.value,
                                )
                            "
                        />
                    </td>
                    <td>
                        <button @click="$emit('edit-column', index)">
                            Edit
                        </button>
                        <button @click="$emit('duplicate-column', index)">
                            Duplicate
                        </button>
                        <button @click="$emit('delete-column', index)">
                            Delete
                        </button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    name: "ColumnControls",
    props: {
        columns: Array,
    },
    emits: [
        "update-column-name",
        "reorder-columns",
        "duplicate-column",
        "delete-column",
        "edit-column",
    ],
};
</script>
