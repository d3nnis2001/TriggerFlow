<template>
    <div class="data-view">
        <table class="data-table">
            <thead>
                <tr>
                    <th
                        v-for="column in visibleColumns"
                        :key="column.id"
                        @click="$emit('select-column', column)"
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
                        @click="$emit('select-column', column)"
                    >
                        {{ row[column.id] }}
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    name: "DataView",
    props: {
        data: Array,
        visibleColumns: Array,
    },
    emits: ["select-column"],
};
</script>
